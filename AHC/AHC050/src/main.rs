#![allow(non_snake_case, unused_macros)]

use itertools::Itertools;
use proconio::{input, marker::Chars};
use rand::prelude::*;

const SEED: u64 = 123456789; 

fn main() {
    let start_time = std::time::Instant::now();

    let mut rng = rand_chacha::ChaCha20Rng::seed_from_u64(SEED);

    input! {
        N: usize, M: usize,
        S: [Chars; N],
    }
    let input = Input { N, M, S: S.clone() };

    // 袋小路判定のためのカウンタ 5以上はすでに岩がある場所
    let mut ct = vec![vec![0; N+2]; N+2];

    // 初期配置が岩
    for h in 1..N+1 {
        for w in 1..N+1 {
            if S[h][w] == '#' {
                visited[h-1][w-1] = true;
                ct[h][w] = 5; 
                // 周囲のますをカウントアップ
                for (dh, dw) in [(-1, 0), (1, 0), (0, -1), (0, 1)] {
                    let nh = h as isize + dh;
                    let nw = w as isize + dw;
                    if nh >= 0 && nh < N as isize && nw >= 0 && nw < N as isize {
                        ct[nh as usize][nw as usize] += 1;
                    }
                }
            } 
        }
    }
    // 外周も岩
    for i in 0..N+2 {
        ct[0][i] = 5; // 上の行
        ct[1][1] += 1; // 上の行の下
        ct[N+1][i] = 5; // 下の行
        ct[N][i] +=1; // 下の行の上
        ct[i][0] = 5; // 左の列
        ct[i][1] += 1; // 左の列の右
        ct[i][N+1] = 5; // 右の列
        ct[i][N] += 1; // 右の列の左
    }

    // 連結なする空きマスをリストアップ
    let mut candidates = vec![];
    for h in 1..N+1 {
        let mut stack = vec![];
        for w in 1..N+1 {
            if S[h-1][w-1] == '#' {
                if !stack.is_empty() {
                    candidates.push(stack);
                }
                stack.clear();
            } else {
                stack.push((h, w));
            }
        }
    }
    for w in 1..N+1 {
        let mut stack = vec![];
        for h in 1..N+1 {
            if S[h-1][w-1] == '#' {
                if !stack.is_empty() {
                    candidates.push(stack);
                }
                stack.clear();
            } else {
                stack.push((h, w));
            }
        }
    }
    // 長さ順に逆順ソート
    candidates.sort_by_key(|v| v.len());
    candidates.reverse();

    // 時間の許す限り貪欲法を試す
    let mut best_out = vec![];
    let mut best_score = 0;
    while start_time.elapsed().as_millis() < 1960 {
        if candidates.is_empty() {
            break;
        }
        let line = candidates.pop().unwrap();
        let mut out = vec![];
        
        
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
