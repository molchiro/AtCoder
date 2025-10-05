#![allow(non_snake_case, unused_imports)]
use proconio::input;


fn main() {
    input! {
        N: usize,
        w: [[i32; N]; N],
        d: [[i32; N]; N],
    }

    let input = Input {
        N,
        w: w.clone(),
        d: d.clone(),
    };


    let mut state = State::new(&input);

    // (0, 0) から遠い順に運ぶ
    let mut cells: Vec<(usize, usize)> = (0..N)
        .flat_map(|i| (0..N).map(move |j| (i, j)))
        .collect();
    cells.sort_by_key(|&(i, j)| -(i as i32 + j as i32)); // 距離が遠い順にソート

    for (i, j) in cells {
        // すでに運んでいるセルはスキップ
        if state.w[i][j] == 0 {
            continue;
        }
        // 指定のセルに移動
        while state.pi != i || state.pj != j {
            if state.pi < i {
                state.apply('D').unwrap();
            } else if state.pj < j {
                state.apply('R').unwrap();
            } else if state.pi > i {
                state.apply('U').unwrap();
            } else if state.pj > j {
                state.apply('L').unwrap();
            }
        }
        // println!("Moving to ({}, {})", i, j);
        // 持つ
        state.apply('1').unwrap();
        // (0, 0) に戻る
        while !(state.pi == 0 && state.pj == 0) {
            // println!("Returning from ({}, {})", state.pi, state.pj);
            if state.pi > 0 {
            state.apply('U').unwrap();
            } else if state.pj > 0 {
            state.apply('L').unwrap();
            }
            // もてるなら持つ
            if state.w[state.pi][state.pj] > 0 {
                let res = state.apply('1');
                if let Err(e) = res {
                    // println!("Error: {}", e);
                }
            }
        }
        // println!("Returning to (0, 0)");
    }

    for c in state.actions.iter() {
        println!("{}", c);
    }
}

struct State {
    pi: usize,
    pj: usize,
    w: Vec<Vec<i32>>,
    d: Vec<Vec<i32>>,
    stack: Vec<(i32, i32)>,
    T: usize,
    actions: Vec<char>,
}

impl State {
    fn new(input: &Input) -> Self {
        State {
            pi: 0,
            pj: 0,
            w: input.w.clone(),
            d: input.d.clone(),
            stack: vec![],
            T: 0,
            actions: vec![],
        }
    }
    fn apply(&mut self, c: char) -> Result<(), String> {
        let N = self.w.len();
        match c {
            '1' => {
                if self.w[self.pi][self.pj] == 0 {
                    return Err(format!(
                        "Operation 1 cannot be applied at ({}, {})",
                        self.pi, self.pj
                    ));
                }
                // 最短距離で(0, 0)に戻るルールとしたときに壊れるか先に計算
                for i in 0..self.stack.len() {
                    let (w, d) = self.stack[i];
                    let new_d = d -  self.w[self.pi][self.pj] * (self.pi as i32 + self.pj as i32);
                    if new_d <= 0 {
                        return Err(format!("The {}-th box is crushed", i));
                    }
                    self.stack[i] = (w, new_d);
                }
                self.stack
                    .push((self.w[self.pi][self.pj], self.d[self.pi][self.pj]));
                self.w[self.pi][self.pj] = 0;
                self.d[self.pi][self.pj] = 0;

            }
            '2' => {
                if self.w[self.pi][self.pj] > 0 {
                    return Err(format!(
                        "Operation 2 cannot be applied at ({}, {})",
                        self.pi, self.pj
                    ));
                }
                let (poped_w, poped_d) = self.stack.pop().ok_or("Stack is empty")?;
                // おいたことによって耐久力が回復
                for i in 0..self.stack.len() {
                    let (w, d) = self.stack[i];
                    let new_d = d - poped_w * (self.pi as i32 + self.pj as i32);
                    self.stack[i] = (w, new_d);
                }
                self.w[self.pi][self.pj] = poped_w;
                self.d[self.pi][self.pj] = poped_d;
            }
            c => {
                if let Some(dir) = DIR.iter().position(|&d| d == c) {
                    let (di, dj) = DIJ[dir];
                    // println!("{}, {}, {}, {}", di, dj, self.pi, self.pj);
                    let ni = self.pi + di;
                    let nj = self.pj + dj;
                    if ni >= N || nj >= N {
                        return Err(format!(
                            "Operation {} cannot be applied at ({}, {})",
                            c, self.pi, self.pj
                        ));
                    }
                    self.pi = ni;
                    self.pj = nj;
                    self.T += 1;
                    if self.pi == 0 && self.pj == 0 {
                        self.stack.clear();
                    }
                } else {
                    return Err(format!("Invalid operation: {}", c));
                }
            }
            
        }
        self.actions.push(c);
        Ok(())
    }
}

const DIJ: [(usize, usize); 4] = [(!0, 0), (1, 0), (0, !0), (0, 1)];
const DIR: [char; 4] = ['U', 'D', 'L', 'R'];

#[macro_export]
macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

#[derive(Clone, Debug)]
pub struct Input {
    N: usize,
    w: Vec<Vec<i32>>,
    d: Vec<Vec<i32>>,
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
