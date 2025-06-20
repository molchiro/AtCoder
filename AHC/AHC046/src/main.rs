use std::collections::VecDeque;
use proconio::input;

const N: usize = 20;
const M: usize = 40;
static DIRECTIONS: [Direction; 4] = [Direction::Up, Direction::Down, Direction::Left, Direction::Right];

fn main() {
    input! {
        _: usize, m: usize,
        destinations: [(usize, usize); m],
    }
    let mut init_game = Game::new(destinations[0], destinations[1..].to_vec());
    let mut init_ans = init_game.fast_clone();
    while !init_ans.finished() {
        init_ans.go_next_target();
    }

    let mut best_ans = init_ans.fast_clone();
    for i in 0..init_ans.actions.len() {
        if init_game.finished() {
            break;
        }

        let new_ans_init = init_game.fast_clone();

        for dir in &DIRECTIONS {

            let mut new_ans = new_ans_init.fast_clone();
            new_ans.act(&Action::Alter(*dir));
    
            while !new_ans.finished() {
                new_ans.go_next_target();
            }
            if new_ans.score() > best_ans.score() {
                best_ans = new_ans;
            }
        }

        init_game.act(&best_ans.actions[i]);
    }

    // 無駄な石の設置を削除
    let mut i = 0;
    while i < best_ans.actions.len() {
        let mut final_ans = Game::new(destinations[0], destinations[1..].to_vec());
        let actions = best_ans.actions.clone();
        // i番目の要素を除いたactionsを実行
        for j in 0..actions.len() {
            if j != i {
                final_ans.act(&actions[j]);
            }
        }
        if final_ans.finished() {
            best_ans = final_ans;
        } else {
            i += 1;
        }
    }

    for action in &best_ans.actions {
        println!("{}", action.to_string());
    }
}

#[derive(Clone)]
struct Game {
    targets: Vec<(usize, usize)>,
    grid: [[bool; N]; N],
    target_index: usize,
    now: (usize, usize),
    actions: Vec<Action>,
    turn: usize,
}

impl Game {
    fn new(now: (usize, usize), targets: Vec<(usize, usize)>) -> Self {
        Game {
            targets,
            grid: [[false; N]; N],
            target_index: 0,
            now,
            actions: vec![],
            turn: 0,
        }
    }

    fn fast_clone(&self) -> Self {
        Game {
            targets: self.targets.clone(),
            grid: self.grid,
            target_index: self.target_index,
            now: self.now,
            actions: self.actions.clone(),
            turn: self.turn,
        }
    }

    fn act(&mut self, action: &Action) {
        match action {
            Action::Move(direction) => self.move_player(direction),
            Action::Skate(direction) => self.skate(direction),
            Action::Alter(direction) => self.alter(direction),
        }
        self.actions.push(action.clone());
        if self.now == self.targets[self.target_index] {
            self.target_index += 1;
        }
        self.turn += 1;
    }

    fn move_player(&mut self, direction: &Direction) {
        let (h, w) = self.now;
        match direction {
            Direction::Up if h > 0 && !self.grid[h - 1][w] => self.now.0 -= 1,
            Direction::Down if h < N - 1 && !self.grid[h + 1][w] => self.now.0 += 1,
            Direction::Left if w > 0 && !self.grid[h][w - 1] => self.now.1 -= 1,
            Direction::Right if w < N - 1 && !self.grid[h][w + 1] => self.now.1 += 1,
            _ => {}
        }
    }

    fn skate(&mut self, direction: &Direction) {
        match direction {
            Direction::Up => while self.now.0 > 0 && !self.grid[self.now.0 - 1][self.now.1] { self.now.0 -= 1; },
            Direction::Down => while self.now.0 < N - 1 && !self.grid[self.now.0 + 1][self.now.1] { self.now.0 += 1; },
            Direction::Left => while self.now.1 > 0 && !self.grid[self.now.0][self.now.1 - 1] { self.now.1 -= 1; },
            Direction::Right => while self.now.1 < N - 1 && !self.grid[self.now.0][self.now.1 + 1] { self.now.1 += 1; },
        }
    }

    fn alter(&mut self, direction: &Direction) {
        let (h, w) = self.now;
        match direction {
            Direction::Up if h > 0 => self.grid[h - 1][w] ^= true,
            Direction::Down if h < N - 1 => self.grid[h + 1][w] ^= true,
            Direction::Left if w > 0 => self.grid[h][w - 1] ^= true,
            Direction::Right if w < N - 1 => self.grid[h][w + 1] ^= true,
            _ => {}
        }
    }

    fn go_next_target(&mut self) {
        if self.finished() {
            return;
        }

        let mut queue = VecDeque::new();
        let mut visited = vec![vec![false; N]; N];
        let mut prev = vec![vec![None; N]; N];
        queue.push_back(self.now);
        visited[self.now.0][self.now.1] = true;
        let next_target = self.targets[self.target_index];

        while let Some((h, w)) = queue.pop_front() {
            if (h, w) == next_target {
                break;
            }

            for &direction in &DIRECTIONS {
                let (mut nh, mut nw) = (h as isize, w as isize);
                match direction {
                    Direction::Up => while nh > 0 && !self.grid[(nh - 1) as usize][nw as usize] { nh -= 1; },
                    Direction::Down => while nh < N as isize - 1 && !self.grid[(nh + 1) as usize][nw as usize] { nh += 1; },
                    Direction::Left => while nw > 0 && !self.grid[nh as usize][(nw - 1) as usize] { nw -= 1; },
                    Direction::Right => while nw < N as isize - 1 && !self.grid[nh as usize][(nw + 1) as usize] { nw += 1; },
                }
                let (nh, nw) = (nh as usize, nw as usize);
                if !visited[nh][nw] {
                    visited[nh][nw] = true;
                    prev[nh][nw] = Some((h, w, Action::Skate(direction)));
                    queue.push_back((nh, nw));
                }
            }

            for &direction in &DIRECTIONS {
                let (mut nh, mut nw) = (h as isize, w as isize);
                match direction {
                    Direction::Up => nh -= 1,
                    Direction::Down => nh += 1,
                    Direction::Left => nw -= 1,
                    Direction::Right => nw += 1,
                }
                if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                    let (nh, nw) = (nh as usize, nw as usize);
                    if !visited[nh][nw] && !self.grid[nh][nw] {
                        visited[nh][nw] = true;
                        prev[nh][nw] = Some((h, w, Action::Move(direction)));
                        queue.push_back((nh, nw));
                    }
                }
            }
        }

        if !visited[next_target.0][next_target.1] {
            self.turn = 2 * N * M;
            return;
        }

        let mut actions = vec![];
        let mut now = next_target;
        while now != self.now {
            if let Some((h, w, action)) = prev[now.0][now.1].take() {
                actions.push(action);
                now = (h, w);
            }
        }

        for action in actions.into_iter().rev() {
            self.act(&action);
        }
    }

    fn finished(&self) -> bool {
        self.target_index >= self.targets.len() || self.turn >= 2 * N * M
    }

    fn score(&self) -> usize {
        if self.target_index + 1 < M {
            self.target_index + 1
        } else {
            M + 2 * N * M - self.turn
        }
    }
}

#[derive(Clone, Debug)]
enum Action {
    Move(Direction),
    Skate(Direction),
    Alter(Direction),
}

impl Action {
    fn to_string(&self) -> String {
        match self {
            Action::Move(d) => format!("M {}", d.to_string()),
            Action::Skate(d) => format!("S {}", d.to_string()),
            Action::Alter(d) => format!("A {}", d.to_string()),
        }
    }
}

#[derive(Copy, Clone, Debug)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn to_string(&self) -> String {
        match self {
            Direction::Up => "U",
            Direction::Down => "D",
            Direction::Left => "L",
            Direction::Right => "R",
        }
        .to_string()
    }
}
