#![allow(non_snake_case, unused_macros)]

use bitvec::vec;
use itertools::Itertools;
use proconio::{input, marker::Chars};
use rand::prelude::*;
use std::ops::RangeBounds;

const SEED: u64 = 123456789; 



fn main() {
    let start_time = std::time::Instant::now();

    let mut rng = rand_chacha::ChaCha20Rng::seed_from_u64(SEED);

    input! {
        N: usize, M: usize,
        S: [Chars; N],
    }
    let input = Input { N, M, S: S.clone() };

    // 袋小路判定のためのカウンタ
    let mut init_ct = vec![vec![0; N]; N];
    // 外周は岩であるため外周のますをカウントアップ
    for i in 0..N {
        init_ct[0][i] += 1; // 上の行
        init_ct[N - 1][i] += 1; // 下の行
        init_ct[i][0] += 1; // 左の列
        init_ct[i][N - 1] += 1; // 右の列
    }
    
    let mut init_visited = vec![vec![false; N]; N];
    let mut init_candidates = vec![];
    let mut init_to_fill = vec![];
    let mut init_res = vec![];
    let mut init_res_without_dummy = vec![];

    for h in 0..N {
        for w in 0..N {
            if S[h][w] == '#' {
                init_visited[h][w] = true;
                init_ct[h][w] = 5; 
                // 周囲のますをカウントアップ
                for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let nh = h as isize + dh;
                    let nw = w as isize + dw;
                    if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                        init_ct[nh as usize][nw as usize] += 1;
                    }
                }
            } 
        }
    }

    // 自分自身が0のマスに貪欲に岩を置く行動を変化がなくなるまで繰り返す
    let mut cont = true;
    while cont {
        cont = false;
        for h in 0..N {
            for w in 0..N {
                if init_ct[h][w] != 0 {
                    continue;
                }
                cont = true;
                init_res.push((h, w));
                init_res_without_dummy.push((h, w));
                init_visited[h][w] = true;
                init_ct[h][w] = 5; // ダミー値で埋める
                // 周囲のますをカウントアップ
                for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let nh = h as isize + dh;
                    let nw = w as isize + dw;
                    if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                        init_ct[nh as usize][nw as usize] += 1;
                    }
                }   
            }
        }
    }

    // 隣り合うマスが0-3の関係になっているマスに貪欲に岩を置く行動を変化がなくなるまで繰り返す
    let mut cont = true;
    while cont {
        cont = false;
        for h in 0..N {
            for w in 0..N {
                if init_ct[h][w] != 0 {
                    continue;
                }
                // 周囲を探索
                let mut f = false;
                for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let nh = h as isize + dh;
                    let nw = w as isize + dw;
                    if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                        if init_ct[nh as usize][nw as usize] == 3 {
                            f = true;
                            break;
                        }
                    }
                }
                if f {
                    cont = true;
                    init_res.push((h, w));
                    init_res_without_dummy.push((h, w));
                    init_visited[h][w] = true;
                    init_ct[h][w] = 5; 
                    // 周囲のますをカウントアップ
                    for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                        let nh = h as isize + dh;
                        let nw = w as isize + dw;
                        if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                            init_ct[nh as usize][nw as usize] += 1;
                        }
                    }   
                }
    
            }
        }

        // 0-3がなければ1-3を試す
        if cont {
            continue;
        }

        for h in 0..N {
            for w in 0..N {
                if init_ct[h][w] != 1 {
                    continue;
                }
                // 周囲を探索
                let mut f = false;
                for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let nh = h as isize + dh;
                    let nw = w as isize + dw;
                    if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                        if init_ct[nh as usize][nw as usize] == 3 {
                            f = true;
                            break;
                        }
                    }
                }
                if f {
                    cont = true;
                    init_res.push((h, w));
                    init_res_without_dummy.push((h, w));
                    init_visited[h][w] = true;
                    init_ct[h][w] = 5; 
                    // 周囲のますをカウントアップ
                    for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                        let nh = h as isize + dh;
                        let nw = w as isize + dw;
                        if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                            init_ct[nh as usize][nw as usize] += 1;
                        }
                    }   
                }
    
            }
        }
    }

    for h in 0..N {
        for w in 0..N {
            if init_ct[h][w] == 4 {
                // 袋小路ができている場合は塗る順番と独立に考えられるので後回し
                init_to_fill.push((h, w, init_res.len()));
                // 復元用に一旦ダミー値で埋める
                init_res.push((usize::MAX, usize::MAX));
                init_visited[h][w] = true;
                init_ct[h][w] = 5; // ダミー値で埋める
            } else if init_ct[h][w] < 4 {
                init_candidates.push((h, w));
            }
        }
    }

    // println!("time: {:?}", start_time.elapsed());

    let mut best_out = vec![];
    let mut best_score = 0;
    while start_time.elapsed().as_millis() < 1960 {
        let mut visited = init_visited.clone();
        let mut candidates = init_candidates.clone();
        let mut to_fill = init_to_fill.clone();
        let mut res = init_res.clone();
        let mut res_without_dummy = init_res_without_dummy.clone();
        let mut ct = init_ct.clone();
        // ランダムな順番でcandidatesをシャッフル
        candidates.shuffle(&mut rng);

        for (h, w) in candidates {
            if visited[h][w] {
                continue;
            }

            res.push((h, w));
            res_without_dummy.push((h, w));
            visited[h][w] = true;
            ct[h][w] = 5; // ダミー値で埋める
            // 周囲のますをカウントアップ
            for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                let nh = h as isize + dh;
                let nw = w as isize + dw;
                if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                    ct[nh as usize][nw as usize] += 1;
                    if ct[nh as usize][nw as usize] == 4 {
                        // 復元用に一旦ダミー値で埋める
                        res.push((usize::MAX, usize::MAX));
                        to_fill.push((nh as usize, nw as usize, res.len() - 1));
                        visited[nh as usize][nw as usize] = true;
                    }
                }
            }
        }

        // resをデバッグ出力
        // println!("res: {:?}", res);
        // to_fillをデバッグ出力
        // println!("to_fill: {:?}", to_fill);

        // to_fillについて確率の低い順に並び替え
        let (_, _, state ) = compute_score_details(&input, &res_without_dummy);
        let mut to_fill2 = vec![];
        for (h, w, idx) in to_fill {
            if state.prob[h][w] * (1600.0 - idx as f64) / 1600.0 < 0.0001 {
                // 確率が低いものは袋小路になったときに塗りつぶしてしまう
                res[idx] = (h, w);
            } else {
                // 確率が高いものは後回しにする
                to_fill2.push((h, w, state.prob[h][w]));
            }
        }
        // 確率の低い順にソート
        to_fill2.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap_or(std::cmp::Ordering::Equal));

        // res と　to_fill を結合して出力
        let mut out = vec![];
        for (h, w) in res {
            if h == usize::MAX && w == usize::MAX {
                continue; // ダミー値は出力しない
            }
            out.push((h, w));
        }
        for (h, w, _) in to_fill2 {
            out.push((h, w));
        }       

        let (score, err, state) = compute_score_details(&input, &out);
        if err.len() > 0 {
            // println!("Error: {}", err);
            continue; // エラーがある場合はスキップ
        }
        if score > best_score {
            best_score = score;
            best_out = out;
            // println!("New best score: {}", best_score);
            // println!("Output: {:?}", best_out);
        } else {
            // println!("hote")
        }

    }

    for (h, w) in best_out {
        println!("{} {}", h, w);
    }



}


pub trait SetMinMax {
    fn setmin(&mut self, v: Self) -> bool;
    fn setmax(&mut self, v: Self) -> bool;
}
impl<T> SetMinMax for T
where
    T: PartialOrd,
{
    fn setmin(&mut self, v: T) -> bool {
        *self > v && {
            *self = v;
            true
        }
    }
    fn setmax(&mut self, v: T) -> bool {
        *self < v && {
            *self = v;
            true
        }
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
pub struct Input {
    pub N: usize,
    pub M: usize,
    pub S: Vec<Vec<char>>,
}

impl std::fmt::Display for Input {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{} {}", self.N, self.M)?;
        for row in &self.S {
            writeln!(f, "{}", row.iter().collect::<String>())?;
        }
        Ok(())
    }
}

pub fn parse_input(f: &str) -> Input {
    let f = proconio::source::once::OnceSource::from(f);
    input! {
        from f,
        N: usize, M: usize,
        S: [Chars; N],
    }
    Input { N, M, S }
}

pub fn read<T: Copy + PartialOrd + std::fmt::Display + std::str::FromStr, R: RangeBounds<T>>(
    token: Option<&str>,
    range: R,
) -> Result<T, String> {
    if let Some(v) = token {
        if let Ok(v) = v.parse::<T>() {
            if !range.contains(&v) {
                Err(format!("Out of range: {}", v))
            } else {
                Ok(v)
            }
        } else {
            Err(format!("Parse error: {}", v))
        }
    } else {
        Err("Unexpected EOF".to_owned())
    }
}

pub struct Output {
    pub out: Vec<(usize, usize)>,
}

pub fn parse_output(input: &Input, f: &str) -> Result<Output, String> {
    let mut f = f.split_whitespace().peekable();
    let mut out = vec![];
    while f.peek().is_some() {
        let i = read(f.next(), 0..input.N)?;
        let j = read(f.next(), 0..input.N)?;
        out.push((i, j));
        if out.len() > input.N * input.N - input.M {
            return Err("Too many outputs".to_owned());
        }
    }
    Ok(Output { out })
}

pub fn compute_score(input: &Input, out: &Output) -> (i64, String) {
    let (mut score, err, _) = compute_score_details(input, &out.out);
    if err.len() > 0 {
        score = 0;
    }
    (score, err)
}

pub struct State {
    pub S: Vec<Vec<char>>,
    pub prob: Vec<Vec<f64>>,
    pub lives: Vec<f64>,
}

pub fn compute_score_details(input: &Input, out: &[(usize, usize)]) -> (i64, String, State) {
    let mut S = input.S.clone();
    let mut crt = mat![0.0; input.N; input.N];
    for i in 0..input.N {
        for j in 0..input.N {
            if input.S[i][j] == '.' {
                crt[i][j] = 1.0 / (input.N * input.N - input.M) as f64;
            }
        }
    }
    let mut ret = 0.0;
    let mut lives = vec![1.0];
    let mut life = 1.0;
    for t in 0.. {
        let mut next = mat![0.0; input.N; input.N];
        for i in 0..input.N {
            for j in 0..input.N {
                if crt[i][j] == 0.0 {
                    continue;
                }
                for (di, dj) in [(!0, 0), (1, 0), (0, !0), (0, 1)] {
                    let mut i2 = i;
                    let mut j2 = j;
                    while i2 + di < input.N && j2 + dj < input.N && S[i2 + di][j2 + dj] == '.' {
                        i2 += di;
                        j2 += dj;
                    }
                    next[i2][j2] += crt[i][j] * 0.25;
                }
            }
        }
        crt = next;
        if t >= out.len() {
            break;
        }
        let (bi, bj) = out[t];
        if S[bi][bj] == '#' {
            return (
                0,
                format!("({}, {}) is already blocked (turn {})", bi, bj, t),
                State {
                    S,
                    prob: crt,
                    lives,
                },
            );
        }
        life -= crt[bi][bj];
        crt[bi][bj] = 0.0;
        S[bi][bj] = '#';
        ret += life;
        lives.push(life);
    }
    let ub = (input.N * input.N - input.M - 1) as f64;
    let score = (ret / ub * 1e6).round() as i64;
    let err = if out.len() < input.N * input.N - input.M {
        "Not finished".to_owned()
    } else {
        String::new()
    };
    (
        score,
        err,
        State {
            S,
            prob: crt,
            lives,
        },
    )
}

/// 0 <= val <= 1
pub fn color(mut val: f64) -> String {
    val.setmin(1.0);
    val.setmax(0.0);
    let (r, g, b) = if val < 0.5 {
        let x = val * 2.0;
        (
            30. * (1.0 - x) + 144. * x,
            144. * (1.0 - x) + 255. * x,
            255. * (1.0 - x) + 30. * x,
        )
    } else {
        let x = val * 2.0 - 1.0;
        (
            144. * (1.0 - x) + 255. * x,
            255. * (1.0 - x) + 30. * x,
            30. * (1.0 - x) + 70. * x,
        )
    };
    format!(
        "#{:02x}{:02x}{:02x}",
        r.round() as i32,
        g.round() as i32,
        b.round() as i32
    )
}
