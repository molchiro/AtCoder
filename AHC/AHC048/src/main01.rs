#![allow(non_snake_case, unused_macros)]
use std::collections::{BinaryHeap, VecDeque};

use im_rc::HashMap;
use itertools::concat;
use proconio::input;
use rand_core::le;


fn main() {
    input! {
        N: usize, K: usize, H: usize, T: usize, D: i32,
        own: [[f64; 3]; K],
        target: [[f64; 3]; H],
    }
    let input = Input {
        N,
        K,
        H,
        T,
        D,
        own: own.into_iter().map(|x| [x[0], x[1], x[2]]).collect(),
        target: target.into_iter().map(|x| [x[0], x[1], x[2]]).collect(),
    };

    let mut recipes = vec![];
    // 1種類の絵の具
    for i in 0..input.K {
        recipes.push((input.own[i], vec![i]));
    }
    // 2種類の絵の具
    for i in 0..input.K {
        for j in i + 1..input.K {
            recipes.push((mix(1.0, input.own[i], 1.0, input.own[j]), vec![i, j]));
        }
    }
    // 3種類の絵の具
    for i in 0..input.K {
        for j in i + 1..input.K {
            for k in j + 1..input.K {
                let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                mixed = mix(2.0, mixed, 1.0, input.own[k]);
                recipes.push((mixed, vec![i, j, k]));
            }
        }
    }



    // let mut state = State::new(
    //     vec![vec![true; N - 1]; N],
    //     vec![vec![false; N]; N - 1],
    //     input.clone(),
    // );


    // // 全てチューブから直接選んだ場合を基準とする
    // for t in input.target.iter() {
    //     let mut best_d = f64::MAX;
    //     let mut best_action = Action::Add { i: 0, j: 0, k: 0 };
    //     for k in 0..input.K {
    //         let c = input.own[k];
    //         let d = ((c[0] - t[0]).powi(2) + (c[1] - t[1]).powi(2) + (c[2] - t[2]).powi(2)).sqrt();
    //         if d < best_d {
    //             best_d = d;
    //             best_action = Action::Add { i: 0, j: 0, k };
    //         }
    //     }
    //     state.apply(&input, best_action);
    //     state.apply(&input, Action::Deliver { i: 0, j: 0 });
    // }

    // let mut best_state = state.clone();
    
    let mut stock = HashMap::new(); // 余った絵の具を管理する
    let mut ct = 0;

    let mut state = State::new(
        vec![vec![true; N - 1]; N],
        vec![vec![true; N]; N - 1],
        input.clone(),
    );

    for i in 0..input.H {
        // 予約済みなら即座に届ける
        if stock.contains_key(&i) {
            let (i1, j1) = stock[&i];
            state.apply(&input, Action::Deliver { i: i1, j: j1 });
            continue;
        }


        // recipesの中から最も近い色を探す
        let mut top_recipes = vec![];
        for (color, tubes) in recipes.iter() {
            if input.H - ct == 1 {
                if tubes.len() > 1 {
                    continue; // 最後の1つは2つ以上を混ぜた絵の具は使えない
                }
            } else if input.H - ct == 2 {
                if tubes.len() > 2 {
                    continue; // 最後から2つめは3種類混ぜた絵の具は使えない
                }
            } 
            let d = ((color[0] - input.target[i][0]).powi(2)
            + (color[1] - input.target[i][1]).powi(2)
            + (color[2] - input.target[i][2]).powi(2))
            .sqrt();
            top_recipes.push((d, (color.clone(), tubes.clone())));
        }

        // 距離でソート
        top_recipes.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

        // 最も近い色から順に、パレットに配置できるか試す
        for (_, (color, tubes)) in top_recipes.iter() {
            
            let positions = state.find_n_size_well(&input, tubes.len());
            if positions.is_none() {
                continue; // パレットに置けない
            }
            ct += tubes.len();

            let positions = positions.unwrap();
            // 壁を下げる
            for i in 0..(positions.len()-1) {
                let (i1, j1) = positions[i];
                let (i2, j2) = positions[i + 1];
                state.apply(&input, Action::Toggle { i1, j1, i2, j2: j2 });
            }

            // 絵の具を混ぜる
            for tube in tubes.iter() {
                let k = *tube;
                state.apply(&input, Action::Add { i: positions[0].0, j: positions[0].1, k });
            }

            // 壁を戻す
            for i in 0..(positions.len()-1) {
                let (i1, j1) = positions[i];
                let (i2, j2) = positions[i + 1];
                state.apply(&input, Action::Toggle { i1, j1, i2, j2: j2 });

            }

            // 絵の具を届ける
            state.apply(&input, Action::Deliver { i: positions[0].0, j: positions[0].1 });

            if tubes.len() > 1{
                // 余った絵の具を使うタイミングを決める
                let mut top_targets = vec![];
                for j in i+1..input.H {
                    if stock.contains_key(&j) {
                        continue; // すでに届けたものは除外
                    }
                    let d = ((color[0] - input.target[j][0]).powi(2)
                        + (color[1] - input.target[j][1]).powi(2)
                        + (color[2] - input.target[j][2]).powi(2))
                        .sqrt();
                    top_targets.push((d, j));
                }
                // 距離でソート
                top_targets.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
                for i in 0..tubes.len() - 1 {
                    let (_, j) = top_targets[i];
                    stock.insert(j, positions[i+1].clone());
                }
            }
            
            break;
        }
    }
        
    // 必ず全ての壁を上げた状態からスタート
    for _ in 0..N {
        println!("{}", "1 ".repeat(N - 1).trim());
    }
    for _ in 0..N-1 {
        println!("{}", "1 ".repeat(N).trim());
    }

    // 最高のスコアだった時のactionsを出力
    for action in state.actions.iter() {
        match action {
            Action::Add { i, j, k } => println!("1 {} {} {}", i, j, k),
            Action::Deliver { i, j } => println!("2 {} {}", i, j),
            Action::Discard { i, j } => println!("3 {} {}", i, j),
            Action::Toggle { i1, j1, i2, j2 } => println!("4 {} {} {} {}", i1, j1, i2, j2),
        }
    }

}

macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

pub fn get_ids(
    wall_v: &Vec<Vec<bool>>,
    wall_h: &Vec<Vec<bool>>,
) -> (usize, Vec<Vec<usize>>, Vec<i32>) {
    let N = wall_v.len();
    let mut ids = mat![!0; N; N];
    let mut ID = 0;
    let mut caps = vec![];
    for i in 0..N {
        for j in 0..N {
            if ids[i][j] != !0 {
                continue;
            }
            let mut stack = vec![(i, j)];
            ids[i][j] = ID;
            let mut cap = 0;
            while let Some((i, j)) = stack.pop() {
                cap += 1;
                if j + 1 < N && !wall_v[i][j] && ids[i][j + 1] == !0 {
                    ids[i][j + 1] = ID;
                    stack.push((i, j + 1));
                }
                if i + 1 < N && !wall_h[i][j] && ids[i + 1][j] == !0 {
                    ids[i + 1][j] = ID;
                    stack.push((i + 1, j));
                }
                if j > 0 && !wall_v[i][j - 1] && ids[i][j - 1] == !0 {
                    ids[i][j - 1] = ID;
                    stack.push((i, j - 1));
                }
                if i > 0 && !wall_h[i - 1][j] && ids[i - 1][j] == !0 {
                    ids[i - 1][j] = ID;
                    stack.push((i - 1, j));
                }
            }
            caps.push(cap);
            ID += 1;
        }
    }
    (ID, ids, caps)
}

#[derive(Clone, Debug)]
pub struct Input {
    pub N: usize,
    pub K: usize,
    pub H: usize,
    pub T: usize,
    pub D: i32,
    pub own: Vec<[f64; 3]>,
    pub target: Vec<[f64; 3]>,
}
impl std::fmt::Display for Input {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{} {} {} {} {}", self.N, self.K, self.H, self.T, self.D)?;
        for i in 0..self.own.len() {
            writeln!(
                f,
                "{:.5} {:.5} {:.5}",
                self.own[i][0], self.own[i][1], self.own[i][2]
            )?;
        }
        for i in 0..self.target.len() {
            writeln!(
                f,
                "{:.5} {:.5} {:.5}",
                self.target[i][0], self.target[i][1], self.target[i][2]
            )?;
        }
        Ok(())
    }
}

#[derive(Clone, Copy, Debug)]
pub enum Action {
    Add {
        i: usize,
        j: usize,
        k: usize,
    },
    Deliver {
        i: usize,
        j: usize,
    },
    Discard {
        i: usize,
        j: usize,
    },
    Toggle {
        i1: usize,
        j1: usize,
        i2: usize,
        j2: usize,
    },
}


fn mix(v1: f64, p1: [f64; 3], v2: f64, p2: [f64; 3]) -> [f64; 3] {
    let sum = v1 + v2;
    if sum <= 0.0 {
        return [0.0, 0.0, 0.0];
    }
    [
        (v1 * p1[0] + v2 * p2[0]) / sum,
        (v1 * p1[1] + v2 * p2[1]) / sum,
        (v1 * p1[2] + v2 * p2[2]) / sum,
    ]
}


#[derive(Clone)]
struct State {
    wall_v: Vec<Vec<bool>>,
    wall_h: Vec<Vec<bool>>,
    ids: Vec<Vec<usize>>,
    caps: Vec<i32>,
    vols: Vec<f64>,
    colors: Vec<[f64; 3]>,
    delivered: Vec<[f64; 3]>,
    V: i32,
    actions: Vec<Action>,
    scores: Vec<f64>,
}

impl State {
    fn new(wall_v: Vec<Vec<bool>>, wall_h: Vec<Vec<bool>>, input: Input) -> Self {
        let (ID, ids, caps) = get_ids(&wall_v, &wall_h);
        let vols = vec![0.0; ID];
        let colors = vec![[0.0; 3]; ID];
        let scores = vec![1.0; input.H];
        Self {
            wall_v: wall_v.clone(),
            wall_h: wall_h.clone(),
            ids,
            caps,
            vols,
            colors,
            delivered: vec![],
            V: 0,
            actions: vec![],
            scores,
        }
    }

    fn apply(&mut self, input: &Input, action: Action) -> Result<(), String> {
        match action {
            Action::Add { i, j, k } => {
                self.V += 1;
                let id = self.ids[i][j];
                let w = self.caps[id] as f64 - self.vols[id];
                if w <= 1.0 {
                    self.colors[id] = mix(self.vols[id], self.colors[id], w, input.own[k]);
                    self.vols[id] = self.caps[id] as f64;
                } else {
                    self.colors[id] = mix(self.vols[id], self.colors[id], 1.0, input.own[k]);
                    self.vols[id] += 1.0;
                }
            }
            Action::Deliver { i, j } => {
                if self.delivered.len() >= input.H {
                    return Err("Cannot deliver more than H times".to_owned());
                }
                if self.vols[self.ids[i][j]] < 1.0 - 1e-6 {
                    return Err(format!(
                        "Cannot deliver: {:.10} < 1 gram",
                        self.vols[self.ids[i][j]]
                    ));
                }
                let color = self.colors[self.ids[i][j]];
                let target = input.target[self.delivered.len()];
                self.scores[self.delivered.len()] = ((color[0] - target[0]).powi(2)
                    + (color[1] - target[1]).powi(2)
                    + (color[2] - target[2]).powi(2))
                .sqrt();
                self.vols[self.ids[i][j]] = (self.vols[self.ids[i][j]] - 1.0).max(0.0);
                self.delivered.push(color);
            }
            Action::Discard { i, j } => {
                self.vols[self.ids[i][j]] = (self.vols[self.ids[i][j]] - 1.0).max(0.0);
            }
            Action::Toggle { i1, j1, i2, j2 } => {
                if i1 == i2 {
                    // Toggle vertical wall
                    let i = i1;
                    let j = j1.min(j2);
                    self.wall_v[i][j] ^= true;
                } else {
                    // Toggle horizontal wall
                    let i = i1.min(i2);
                    let j = j1;
                    self.wall_h[i][j] ^= true;
                }
                let (ID, ids, caps) = get_ids(&self.wall_v, &self.wall_h);
                if self.ids[i1][j1] == self.ids[i2][j2] && ids[i1][j1] != ids[i2][j2] {
                    let id1 = ids[i1][j1];
                    let id2 = ids[i2][j2];
                    let v = self.vols[self.ids[i1][j1]];
                    let mut vols = vec![0.0; ID];
                    let mut colors = vec![[0.0; 3]; ID];
                    for i in 0..input.N {
                        for j in 0..input.N {
                            vols[ids[i][j]] = self.vols[self.ids[i][j]];
                            colors[ids[i][j]] = self.colors[self.ids[i][j]];
                        }
                    }
                    vols[id1] = v * caps[id1] as f64 / (caps[id1] + caps[id2]) as f64;
                    vols[id2] = v * caps[id2] as f64 / (caps[id1] + caps[id2]) as f64;
                    self.ids = ids;
                    self.caps = caps;
                    self.vols = vols;
                    self.colors = colors;
                } else if self.ids[i1][j1] != self.ids[i2][j2] && ids[i1][j1] == ids[i2][j2] {
                    let id = ids[i1][j1];
                    let id1 = self.ids[i1][j1];
                    let id2 = self.ids[i2][j2];
                    let v1 = self.vols[id1];
                    let v2 = self.vols[id2];
                    let c1 = self.colors[id1];
                    let c2 = self.colors[id2];
                    let mut vols = vec![0.0; ID];
                    let mut colors = vec![[0.0; 3]; ID];
                    for i in 0..input.N {
                        for j in 0..input.N {
                            vols[ids[i][j]] = self.vols[self.ids[i][j]];
                            colors[ids[i][j]] = self.colors[self.ids[i][j]];
                        }
                    }
                    vols[id] = v1 + v2;
                    colors[id] = mix(v1, c1, v2, c2);
                    self.ids = ids;
                    self.caps = caps;
                    self.vols = vols;
                    self.colors = colors;
                }
            }
        }
        self.actions.push(action);
        Ok(())
    }

    fn get_score(&self) -> f64 {
        self.scores.iter().sum()
    }

    fn find_n_size_well(
        &self,
        input: &Input,
        n: usize,
    ) -> Option<Vec<(usize, usize)>> {
        // n == 1 の場合は必ず空きセルである最後のセルを返す
        if n == 1 {
            return Some(vec![(input.N - 1, 0)]);
        }

        let mut found = false;
        let mut positions = vec![];
        let (ID, ids, caps) = get_ids(&self.wall_v, &self.wall_h);
        // 左から右...下...右から左...とへび上に探していく
        'outer: for i in 0..input.N {
            if i%2 == 0 {
                for j in 0..input.N {
                    // println!("# i: {}, j: {}", i, j);
                    if self.vols[ids[i][j]] == 0.0 {
                        positions.push((i, j));
                        if positions.len() == n {
                            found = true;
                            break 'outer;
                        }
                    } else {
                        positions = vec![];
                    }
                }
            } else {
                for j in (0..input.N).rev() {
                    // println!("# i: {}, j: {}", i, j);

                    if i == input.N - 1 && j == 0 {
                        continue; // 最後のセルは必ず空きにしたい
                    }
                    if self.vols[ids[i][j]] == 0.0 {
                        positions.push((i, j));
                        if positions.len() == n {
                            found = true;
                            break 'outer;
                        }
                    } else {
                        positions = vec![];
                    }
                }
            }
        }

        if found {
            return Some(positions);
        } else {
            // println!("Could not find a well of size {}.", n);
            return None;
        }
    }
        
}