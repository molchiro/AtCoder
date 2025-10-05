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
    // let mut init_candidates = vec![];
    // let mut init_to_fill = vec![];
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

    // 自分自身が1のマスに貪欲に岩を置く行動を変化がなくなるまで繰り返す
    let mut cont = true;
    while cont {
        cont = false;
        for h in 0..N {
            for w in 0..N {
                if init_ct[h][w] != 1 {
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

    // 0-3か、なければ1-3から袋小路を作る
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

    // 自分自身が1のマスに貪欲に岩を置く行動を変化がなくなるまで繰り返す
    let mut cont = true;
    while cont {
        cont = false;
        for h in 0..N {
            for w in 0..N {
                if init_ct[h][w] != 1 {
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

    // 確率の低い順に埋める
    let (_, _, state ) = compute_score_details(&input, &init_res_without_dummy);
    let mut to_fill = vec![];
    for h in 0..N {
        for w in 0..N {
            if init_visited[h][w] {
                continue; // 既に訪問済み
            }
            to_fill.push((h, w, state.prob[h][w]));
        }
    }
    // 確率の低い順にソート
    to_fill.sort_by(|a, b| a.2.partial_cmp(&b.2).unwrap_or(std::cmp::Ordering::Equal));
    let mut best_out = init_res_without_dummy.clone();
    for (h, w, _) in to_fill {
        best_out.push((h, w));
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
