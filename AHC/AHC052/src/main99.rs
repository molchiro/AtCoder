#![allow(non_snake_case, unused_macros)]

use std::{collections::VecDeque, process::exit};
use std::io::Read;

use proconio::{input, marker::Chars};
use rand::prelude::*;

const SEED: u64 = 123456789;

fn main() {
    let start_time = std::time::Instant::now();

    let mut rng = rand_chacha::ChaCha20Rng::seed_from_u64(SEED);

    let mut s = String::new();
    std::io::stdin().read_to_string(&mut s).unwrap();
    let input = parse_input(&s);
    let mut cs = vec![];
    cs.push(vec![0; input.M]); // up
    cs.push(vec![1; input.M]); // down
    cs.push(vec![2; input.M]); // left
    cs.push(vec![3; input.M]); // right
    for _ in 0..6 {
        cs.push((0..input.M).map(|_| rng.gen_range(0..5)).collect());
    }

    let mut state = State::new(input, cs);
    let mut prev = (!0, !0);

    let mut best_state = zantei(&state);

    let mut candidates = vec![];
    candidates.push(state);
    'outer: while candidates[0].targetting(prev).is_some() {
        let mut new_candidates = vec![];
        // ビームサーチ
        for candidate in candidates {
            let target = candidate.targetting(prev).unwrap();
            let robot_id = candidate.find_nearest_target_robot(target);
            let dirs = culc_dirs(&candidate.input, target, candidate.robots[robot_id]);
            for dir in dirs {
                
                new_candidates.push( candidate.act(dir));
                for i in 4..10 {
                    if candidate.cs[i][robot_id] != dir {
                        continue;
                    }
                    let new_state = candidate.act(i);
                    if new_state.true_score() > best_state.true_score() {
                        best_state = new_state.clone();
                    }
                    new_candidates.push(new_state);
                }
            }
        }
        for candidate in &new_candidates {
            // 最適解が見つかっているので終了
            if candidate.rem == 0 {
                break 'outer;
            }
        }
        new_candidates.sort_by_key(|s| -s.score());
        candidates = new_candidates.into_iter().take(10).collect();
        if start_time.elapsed().as_millis() > 1950 {
            break;
        }
    }

    best_state.output();
}

fn zantei(state: &State) -> State {
    let mut prev = (!0, !0);
    let mut state = state.clone();
    while state.targetting(prev).is_some() {
        let target = state.targetting(prev).unwrap();
        let robot_id = state.find_nearest_target_robot(target);
        let dirs = culc_dirs(&state.input, target, state.robots[robot_id]);
        for dir in dirs {
            state = state.act(dir);
        }
        prev = target;
    }
    state
}

fn culc_dirs(input: &Input, target: (usize, usize), start: (usize, usize)) -> Vec<usize> {
    let (tx, ty) = target;
    let (sx, sy) = start;
    let mut queue = VecDeque::new();
    let mut visited = vec![vec![false; input.N]; input.N];
    queue.push_back((sx, sy, 0, vec![]));
    visited[sx][sy] = true;
    while let Some((x, y, dist, dirs)) = queue.pop_front() {
        // println!("x: {}, y: {}, dist: {}, dirs: {:?}", x, y, dist, dirs);
        if (x, y) == (tx, ty) {
            // 最短経路が見つかった
            // println!("yeeee");
            return dirs;
        }
        for (dir, (dx, dy)) in DIJ.iter().enumerate() {
            if !can_move(input, (x, y), dir) {
                continue;
            }
            let nx = x + dx;
            let ny = y + dy;
            if visited[nx][ny] {
                continue;
            }
            visited[nx][ny] = true;
            let mut new_dirs = dirs.clone();
            new_dirs.push(dir);
            queue.push_back((nx, ny, dist + 1, new_dirs));
        }
    }
    panic!("経路が見つからない");
    vec![]
}

#[derive(Clone)]
struct State {
    input: Input,
    cs: Vec<Vec<usize>>,
    actions: Vec<usize>,
    used: Vec<Vec<bool>>,
    robots: Vec<(usize, usize)>,
    rem: usize,
}

impl State {
    fn new(input: Input, cs: Vec<Vec<usize>>) -> Self {
        let N = input.N;
        let M = input.M;
        let mut used = mat![false; N; N];
        for i in 0..M {
            used[input.ps[i].0][input.ps[i].1] = true;
        }
        let rem = N * N - M;
        let robots = input.ps.clone();
        Self {
            input,
            cs,
            actions: vec![],
            used,
            rem,
            robots,
        }
    }

    fn output(&self) {
        for c in &self.cs {
            let s: String = c.iter().map(|&d| CMD[d]).collect();
            println!(
                "{}",
                s.chars()
                    .map(|c| c.to_string())
                    .collect::<Vec<_>>()
                    .join(" ")
            );
        }
        for &a in &self.actions {
            println!("{}", a);
        }
    }

    fn act(&self, action: usize) -> Self {
        let mut new_state = self.clone();
        new_state.actions.push(action);
        for i in 0..self.input.M {
            let dir = self.cs[action][i];
            let (x, y) = self.robots[i];
            if can_move(&self.input, (x, y), dir) {
                let (dx, dy) = DIJ[dir];
                let nx = x + dx;
                let ny = y + dy;
                new_state.robots[i] = (nx, ny);
                if !new_state.used[nx][ny] {
                    new_state.used[nx][ny] = true;
                    new_state.rem -= 1;
                }
            }
        }
        new_state
    }

    fn score(&self) -> i64 {
        self.true_score() - self.penalty_1() * 1 - self.pelnalty_2() * 10
    }

    fn true_score(&self) -> i64 {
        if self.rem == 0 {
            (3 * self.input.N * self.input.N - self.actions.len()) as i64
        } else {
            (self.input.N * self.input.N - self.rem) as i64
        }
    }

    fn penalty_1(&self) -> i64 {
        if self.rem == 0 {
            return 0;
        }
        // 各ロボットから最も近い未到達マスまでの距離の総和
        let mut total = 0;
        for i in 0..self.input.M {
            // 幅優先探索
            let (sx, sy) = self.robots[i];
            let mut queue = VecDeque::new();
            let mut visited = vec![vec![false; self.input.N]; self.input.N];
            queue.push_back((sx, sy, 0));
            visited[sx][sy] = true;
            while let Some((x, y, dist)) = queue.pop_front() {
                if !self.used[x][y] {
                    total += dist as i64;
                    break;
                }
                for (dir, (dx, dy)) in DIJ.iter().enumerate() {
                    if !can_move(&self.input, (x, y), dir) {
                        continue;
                    }
                    let nx = x + dx;
                    let ny = y + dy;
                    if visited[nx][ny] {
                        continue;
                    }
                    visited[nx][ny] = true;
                    queue.push_back((nx, ny, dist + 1));
                }
            }
        }
        total
    }

    fn pelnalty_2(&self) -> i64 {
        // ロボット同士の距離の総和
        let mut total = 0;
        for i in 0..self.input.M {
            for j in i + 1..self.input.M {
                let (x1, y1) = self.robots[i];
                let (x2, y2) = self.robots[j];
                let dist = ((x1 as i64 - x2 as i64).abs() + (y1 as i64 - y2 as i64).abs()) as i64;
                total += dist;
            }
        }
        total
    }

    fn targetting(&self, prev: (usize, usize)) -> Option<(usize, usize)> {
        if self.rem == 0 {
            return None;
        }

        if prev == (!0, !0) {
            // println!("First targetting");
            // 一番最初は左上に一番近いマスを返す
            for i in 0..self.input.N {
                for j in 0..self.input.N {
                    if !self.used[i][j] {
                        return Some((i, j));
                    }
                }
            }
        } else {
            // 前回探索したマスの4近傍のうち,(0, 0)に最も近い未到達マスを探索
            let mut candidates = vec![];
            let (px, py) = prev;
            // println!("Prev: {:?}", prev);

            for (dir, (dx, dy)) in DIJ.iter().enumerate() {
                if !can_move(&self.input, (px, py), dir) {
                    continue;
                }
                let nx = px + dx;
                let ny = py + dy;
                if self.used[nx][ny] {
                    continue;
                }
                candidates.push((nx, ny));
            }
            // (0, 0)に最も近い未到達マスを返す
            if candidates.is_empty() {
                // 4近傍に未到達マスがない場合は全探索
                for i in 0..self.input.N {
                    for j in 0..self.input.N {
                        if !self.used[i][j] {
                            return Some((i, j));
                        }
                    }
                }
            } else {
                candidates.sort_by_key(|&(x, y)| (x, y));
                if let Some(&pos) = candidates.first() {
                    return Some(pos);
                }
            }
        }
        None
    }

    fn find_nearest_target_robot(&self, target: (usize, usize)) -> usize {
        let (tx, ty) = target;
        let mut nearest = 0;
        // 全ロボットについて同時に幅優先探索し、最初にtargetに到達したロボットを採用する
        let mut queue = VecDeque::new();
        let mut visited = vec![vec![vec![false; self.input.N]; self.input.N]; self.input.M];
        for i in 0..self.input.M {
            let (x, y) = self.robots[i];
            queue.push_back((x, y, 0, i));
            visited[i][x][y] = true;
        }
        while let Some((x, y, dist, robot_id)) = queue.pop_front() {
            if (x, y) == (tx, ty) {
                nearest = robot_id;
                break;
            }
            for (dir, (dx, dy)) in DIJ.iter().enumerate() {
                if !can_move(&self.input, (x, y), dir) {
                    continue;
                }
                let nx = x + dx;
                let ny = y + dy;
                if visited[robot_id][nx][ny] {
                    continue;
                }
                visited[robot_id][nx][ny] = true;
                queue.push_back((nx, ny, dist + 1, robot_id));
            }
        }
        nearest
    }
}

#[macro_export]
macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

#[derive(Clone, Debug)]
struct Input {
    N: usize,
    M: usize,
    K: usize,
    ps: Vec<(usize, usize)>,
    wall_v: Vec<Vec<bool>>,
    wall_h: Vec<Vec<bool>>,
}

impl std::fmt::Display for Input {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{} {} {}", self.N, self.M, self.K)?;
        for (x, y) in &self.ps {
            writeln!(f, "{} {}", x, y)?;
        }
        for v in &self.wall_v {
            writeln!(
                f,
                "{}",
                v.iter()
                    .map(|&x| if x { '1' } else { '0' })
                    .collect::<String>()
            )?;
        }
        for h in &self.wall_h {
            writeln!(
                f,
                "{}",
                h.iter()
                    .map(|&x| if x { '1' } else { '0' })
                    .collect::<String>()
            )?;
        }
        Ok(())
    }
}

const CMD: [char; 5] = ['U', 'D', 'L', 'R', 'S'];
const DIJ: [(usize, usize); 5] = [(!0, 0), (1, 0), (0, !0), (0, 1), (0, 0)];

fn can_move(input: &Input, (i, j): (usize, usize), dir: usize) -> bool {
    // println!("can_move: i={}, j={}, dir={}", i, j, dir);
    if dir == 4 {
        return true;
    }
    let (di, dj) = DIJ[dir];
    let i2 = i + di;
    let j2 = j + dj;
    if i2 >= input.N || j2 >= input.N {
        return false;
    }
    if di == 0 {
        !input.wall_v[i][j.min(j2)]
    } else {
        !input.wall_h[i.min(i2)][j]
    }
}

fn parse_input(f: &str) -> Input {
    let f = proconio::source::once::OnceSource::from(f);
    input! {
        from f,
        N: usize, M: usize, K: usize,
        ps: [(usize, usize); M],
        wall_v: [Chars; N],
        wall_h: [Chars; N - 1],
    }
    let wall_v = wall_v
        .into_iter()
        .map(|s| s.into_iter().map(|c| c == '1').collect())
        .collect();
    let wall_h = wall_h
        .into_iter()
        .map(|s| s.into_iter().map(|c| c == '1').collect())
        .collect();
    Input {
        N,
        M,
        K,
        ps,
        wall_v,
        wall_h,
    }
}
