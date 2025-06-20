#![allow(non_snake_case, unused_macros)]
use proconio::input;


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

    let mut state = State::new(
        vec![vec![true; N - 1]; N],
        vec![vec![true; N]; N - 1],
    );

    for t in input.target.iter() {
        let mut best_d = f64::MAX;
        let mut best_action = Action::Add { i: 0, j: 0, k: 0 };
        for k in 0..input.K {
            let c = input.own[k];
            let d = ((c[0] - t[0]).powi(2) + (c[1] - t[1]).powi(2) + (c[2] - t[2]).powi(2)).sqrt();
            if d < best_d {
                best_d = d;
                best_action = Action::Add { i: 0, j: 0, k };
            }
        }
        state.apply(&input, best_action);
        state.apply(&input, Action::Deliver { i: 0, j: 0 });
    }

    for wall in state.wall_v.iter() {
        for &w in wall.iter() {
            print!("{} ", if w { '1' } else { '0' });
        }
        println!();
    }
    for wall in state.wall_h.iter() {
        for &w in wall.iter() {
            print!("{} ", if w { '1' } else { '0' });
        }
        println!();
    }

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


struct State {
    wall_v: Vec<Vec<bool>>,
    wall_h: Vec<Vec<bool>>,
    ids: Vec<Vec<usize>>,
    caps: Vec<i32>,
    vols: Vec<f64>,
    colors: Vec<[f64; 3]>,
    deliverd: Vec<[f64; 3]>,
    V: i32,
    E: f64,
    actions: Vec<Action>,
}

impl State {
    fn new(wall_v: Vec<Vec<bool>>, wall_h: Vec<Vec<bool>>) -> Self {
        let (ID, ids, caps) = get_ids(&wall_v, &wall_h);
        let vols = vec![0.0; ID];
        let colors = vec![[0.0; 3]; ID];
        Self {
            wall_v: wall_v.clone(),
            wall_h: wall_h.clone(),
            ids,
            caps,
            vols,
            colors,
            deliverd: vec![],
            V: 0,
            E: 0.0,
            actions: vec![],
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
                if self.deliverd.len() >= input.H {
                    return Err("Cannot deliver more than H times".to_owned());
                }
                if self.vols[self.ids[i][j]] < 1.0 - 1e-6 {
                    return Err(format!(
                        "Cannot deliver: {:.10} < 1 gram",
                        self.vols[self.ids[i][j]]
                    ));
                }
                let color = self.colors[self.ids[i][j]];
                let target = input.target[self.deliverd.len()];
                self.E += ((color[0] - target[0]).powi(2)
                    + (color[1] - target[1]).powi(2)
                    + (color[2] - target[2]).powi(2))
                    .sqrt();
                self.vols[self.ids[i][j]] = (self.vols[self.ids[i][j]] - 1.0).max(0.0);
                self.deliverd.push(color);
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
}