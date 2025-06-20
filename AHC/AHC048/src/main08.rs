#![allow(non_snake_case, unused_macros)]

use im_rc::HashMap;
use proconio::input;


fn main() {
    input! {
        N: usize, K: usize, H: usize, T: usize, D: i32,
        own: [[f64; 3]; K],
        target: [[f64; 3]; H],
    }
    
    let mut basis_d = vec![];
    for (i, colors) in target.iter().enumerate() {
        let mut best_d = f64::MAX;
        for j in 0..K {
            let c = &own[j];
            let d = ((c[0] - colors[0]).powi(2) + (c[1] - colors[1]).powi(2) + (c[2] - colors[2]).powi(2)).sqrt();
            if d < best_d {
                best_d = d;
            }
        }
        basis_d.push(best_d);
    }

    let input = Input {
        N,
        K,
        H,
        T,
        D,
        own: own.into_iter().map(|x| [x[0], x[1], x[2]]).collect(),
        target: target.into_iter().map(|x| [x[0], x[1], x[2]]).collect(),
        basis_d,
    };

    let mut recipe_map: HashMap<Vec<usize>, ([f64; 3], Vec<usize>)> = HashMap::new();
    let mut best_state = solve(input.clone(), 1, &mut recipe_map);
    let mut iterations = 3;
    if input.K < 21 {
        iterations += 1

    }
    if input.K < 18 {
        iterations += 1

    }
    if input.K < 14 {
        iterations += 1
    }
    if input.K < 10 {
        iterations += 1
    }
    if input.K < 8 {
        iterations += 1
    }

    for n in 2..=iterations {
        let state = solve(input.clone(), n, &mut recipe_map);
        // println!("Tube number: {}, Score: {}", n, state.get_score(&input));
        if state.actions.len() <= input.T && state.get_score(&input) < best_state.get_score(&input) {
            best_state = state;
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
    for action in best_state.actions.iter() {
        match action {
            Action::Add { i, j, k } => println!("1 {} {} {}", i, j, k),
            Action::Deliver { i, j } => println!("2 {} {}", i, j),
            Action::Discard { i, j } => println!("3 {} {}", i, j),
            Action::Toggle { i1, j1, i2, j2 } => println!("4 {} {} {} {}", i1, j1, i2, j2),
        }
    }

}

fn solve(input: Input, tube_number_cap: usize, recipe_map: &mut HashMap<Vec<usize>, ([f64; 3], Vec<usize>)>) -> State {
    if tube_number_cap == 1 {
        // 1種類の絵の具
        for i in 0..input.K {
            recipe_map.insert(vec![i], (input.own[i], vec![i]));

        }
    }
    if tube_number_cap == 2 {
        // 2種類の絵の具
        for i in 0..input.K {
            for j in i + 1..input.K {
                recipe_map.insert(vec![i,j],(mix(1.0, input.own[i], 1.0, input.own[j]), vec![i, j]));
            }
        }
    }

    if tube_number_cap == 3 {
        // 3種類の絵の具
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    if i == j && j == k {
                        // 絵の具一種類と同じなのでスキップ
                        continue;
                    }
                    let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                    mixed = mix(2.0, mixed, 1.0, input.own[k]);
                    let mut indices = [i, j, k];
                    indices.sort();
                    let (x, y, z) = (indices[0], indices[1], indices[2]);
                    recipe_map.insert(vec![x, y, z],(mixed, vec![i, j, k]));
                }
            }
        }
    }

    if tube_number_cap == 4 {
        // 4種類の絵の具
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    for l in 0..input.K {
                        
                        let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                        mixed = mix(2.0, mixed, 1.0, input.own[k]);
                        mixed = mix(3.0, mixed, 1.0, input.own[l]);
                        let mut indices = [i, j, k, l];
                        indices.sort();
                        let (x, y, z, w) = (indices[0], indices[1], indices[2], indices[3]);
                        if x == y && y == z && z == w {
                            // 絵の具一種類と同じなのでスキップ
                            continue;
                        }
                        if x == y && z == w {
                            // 絵の具２種類と同じなのでスキップ
                            continue;
                        }
                        recipe_map.insert(vec![x, y, z, w],(mixed, vec![i, j, k, l]));
                    }
                }
            }
        }
    }

    if tube_number_cap == 5 {
        // 5種類の絵の具
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    for l in 0..input.K {
                        for m in 0..input.K {
                            let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                            mixed = mix(2.0, mixed, 1.0, input.own[k]);
                            mixed = mix(3.0, mixed, 1.0, input.own[l]);
                            mixed = mix(4.0, mixed, 1.0, input.own[m]);
                            let mut indices = [i, j, k, l, m];
                            indices.sort();
                            let (x, y, z, w, v) = (indices[0], indices[1], indices[2], indices[3], indices[4]);
                            if x == y && y == z && z == w && w == v {
                                // 絵の具一種類と同じなのでスキップ
                                continue;
                            }
                            recipe_map.insert(vec![x, y, z, w, v],(mixed, vec![i, j, k, l, m]));
                        }
                    }
                }
            }
        }
    }

    if tube_number_cap == 6 {
        // 6種類の絵の具
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    for l in 0..input.K {
                        for m in 0..input.K {
                            for n in 0..input.K {
                                let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                                mixed = mix(2.0, mixed, 1.0, input.own[k]);
                                mixed = mix(3.0, mixed, 1.0, input.own[l]);
                                mixed = mix(4.0, mixed, 1.0, input.own[m]);
                                mixed = mix(5.0, mixed, 1.0, input.own[n]);
                                let mut indices = [i, j, k, l, m, n];
                                indices.sort();
                                let (x, y, z, w, v, u) = (indices[0], indices[1], indices[2], indices[3], indices[4], indices[5]);
                                if x == y && y == z && z == w && w == v && v == u {
                                    // 絵の具一種類と同じなのでスキップ 6
                                    continue;
                                }
                                if x == y && y == z && w == v && v == u {
                                    // 絵の具2種類と同じなのでスキップ 3, 3
                                    continue;
                                }
                                if x == y && z == w && w == v && v == u {
                                    // 絵の具2種類と同じなのでスキップ 2, 4
                                    continue;
                                }
                                if x == y && y == z && z == w && v == u {
                                    // 絵の具2種類と同じなのでスキップ 4, 2
                                    continue;
                                }
                                if x == y && z == w && v == u {
                                    // 絵の具3種類と同じなのでスキップ 2, 2, 2
                                    continue;
                                }
                                recipe_map.insert(vec![x, y, z, w, v, u],(mixed, vec![i, j, k, l, m, n]));
                            }
                        }
                    }
                }
            }
        }
    }

    // 7種類の絵の具
    if tube_number_cap == 7 {
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    for l in 0..input.K {
                        for m in 0..input.K {
                            for n in 0..input.K {
                                for o in 0..input.K {
                                    let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                                    mixed = mix(2.0, mixed, 1.0, input.own[k]);
                                    mixed = mix(3.0, mixed, 1.0, input.own[l]);
                                    mixed = mix(4.0, mixed, 1.0, input.own[m]);
                                    mixed = mix(5.0, mixed, 1.0, input.own[n]);
                                    mixed = mix(6.0, mixed, 1.0, input.own[o]);
                                    let mut indices = [i, j, k, l, m, n, o];
                                    indices.sort();
                                    let (x, y, z, w, v, u, t) = (indices[0], indices[1], indices[2], indices[3], indices[4], indices[5], indices[6]);
                                    if x == y && y == z && z == w && w == v && v == u && u == t {
                                        // 絵の具一種類と同じなのでスキップ
                                        continue;
                                    }
                                    recipe_map.insert(vec![x,y,z,w,v,u,t],(mixed, vec![i,j,k,l,m,n,o]));
                                }
                            }
                        }
                    }
                }
            }
        }
    }

    // 8種類の絵の具
    if tube_number_cap == 8 {
        for i in 0..input.K {
            for j in 0..input.K {
                for k in 0..input.K {
                    for l in 0..input.K {
                        for m in 0..input.K {
                            for n in 0..input.K {
                                for o in 0..input.K {
                                    for p in 0..input.K {
                                        let mut mixed = mix(1.0, input.own[i], 1.0, input.own[j]);
                                        mixed = mix(2.0, mixed, 1.0, input.own[k]);
                                        mixed = mix(3.0, mixed, 1.0, input.own[l]);
                                        mixed = mix(4.0, mixed, 1.0, input.own[m]);
                                        mixed = mix(5.0, mixed, 1.0, input.own[n]);
                                        mixed = mix(6.0, mixed, 1.0, input.own[o]);
                                        mixed = mix(7.0, mixed, 1.0, input.own[p]);
                                        let mut indices = [i,j,k,l,m,n,o,p];
                                        indices.sort();
                                        let (x,y,z,w,v,u,t,s) = (indices[0], indices[1], indices[2], indices[3], indices[4], indices[5], indices[6], indices[7]);
                                        // 絵の具一種類と同じなのでスキップ 8
                                        if x == y && y == z && z == w && w == v && v == u && u == t && t == s {
                                            continue;
                                        }
                                        // 絵の具2種類と同じなのでスキップ 4, 4
                                        if x == y && y == z && z == w &&  v == u && u == t && t == s {
                                            continue;
                                        }
                                        // 絵の具2種類と同じなのでスキップ 2, 6
                                        if x == y && z == w && w == v && v == u && u == t && t == s {
                                            continue;
                                        }
                                        // 絵の具2種類と同じなのでスキップ 6, 2
                                        if x == y && y == z && z == w && w == v && v == u && t == s {
                                            continue;
                                        }
                                        // 絵の具3種類と同じなのでスキップ 2, 2, 4
                                        if x == y && z == w && v == u && u == t && t == s {
                                            continue;
                                        }
                                        // 絵の具3種類と同じなのでスキップ 2, 4, 2
                                        if x == y && z == w && w == v &&  v == u && t == s {
                                            continue;
                                        }
                                        // 絵の具3種類と同じなのでスキップ 4, 2, 2
                                        if x == y && y == z && z == w && v == u && t == s {
                                            continue;
                                        }
                                        // 絵の具4種類と同じなのでスキップ 2, 2, 2, 2
                                        if x == y &&  z == w &&  v == u  && t == s {
                                            continue;
                                        }
                                        recipe_map.insert(vec![x,y,z,w,v,u,t,s],(mixed, vec![i,j,k,l,m,n,o,p]));
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    let mut recipes = vec![];
    for (_, (color, tubes)) in recipe_map.iter() {
        recipes.push((color.clone(), tubes.clone()));
    }
    
    let mut kari_map = vec![vec![]; recipes.len()];
    let mut kari: Vec<Vec<((usize, usize), usize)>> = vec![vec![]; input.H];
    let mut ct = 0; // 配達済みor仮決め済みの数

    let mut state = State::new(
        vec![vec![true; input.N - 1]; input.N],
        vec![vec![true; input.N]; input.N - 1],
        input.clone(),
    );

    for i in 0..input.H {
        // 予約済みなら即座に届ける
        if kari[i].len() > 0 {
            let ((i1, j1), recipe_id) = kari[i].pop().unwrap();
            kari_map[recipe_id].retain(|&(_, idx)| idx != i);
            state.apply(&input, Action::Deliver { i: i1, j: j1 });
            continue;
        }

        // recipesの中から最も近い色を探す
        let mut top_recipes = vec![];
        for recipe_id in 0..recipes.len() {
            let (color, tubes) = &recipes[recipe_id];
            if input.H - ct < tubes.len() {
                continue; // 必ず余る量の絵の具を作ることは禁止
            }
            let d = ((color[0] - input.target[i][0]).powi(2)
            + (color[1] - input.target[i][1]).powi(2)
            + (color[2] - input.target[i][2]).powi(2))
            .sqrt();
            top_recipes.push((d, recipe_id));
        }

        // 距離でソート
        top_recipes.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());

        // 最も近い色から順に、パレットに配置できるか試す
        for (_, recipe_id) in top_recipes.iter() {
            // パレットにあるならそれを使う
            if kari_map[*recipe_id].len() > 0 {
                let (pos, target): ((usize, usize), usize) = kari_map[*recipe_id].pop().unwrap();
                // println!("use recipe  {} => {}", target, i);
                // if target <= i {
                //     panic!("kari_mapのtargetがi以下の値を持つことはありえない");
                // }
                kari[target].pop();
                // ct -= 1;
                state.apply(&input, Action::Deliver { i: pos.0, j: pos.1 });
                break;
            }


            let (color, tubes) = &recipes[*recipe_id];

            let positions = state.find_n_size_well(&input, tubes.len());
            if positions.is_none() {
                continue; // パレットに置けない
            }
            ct += tubes.len();

            let positions = positions.unwrap();
            // 隣接するペアを列挙
            let mut pairs = vec![];
            for u in 0..positions.len()-1 {
                for v in u+1..positions.len() {
                    let (i1, j1) = positions[u];
                    let (i2, j2) = positions[v];
                    if i1 == i2 {
                        if (j1 as i32 - j2 as i32).abs() == 1 {
                            pairs.push(((i1, j1), (i2, j2)));
                        }
                    } else if j1 == j2 {
                        if (i1 as i32 - i2 as i32).abs() == 1 {
                            pairs.push(((i1, j1), (i2, j2)));
                        }
                    }
                }
            }
            // 壁を下げる
            for ((i1, j1), (i2, j2)) in pairs.iter() {
                let res = state.apply(&input, Action::Toggle { i1: *i1, j1: *j1, i2: *i2, j2: *j2 });
                if res.is_err() {
                    panic!("壁を下げることができませんでした: {:?}", res);
                }
            }
            // 絵の具を混ぜる
            for tube in tubes.iter() {
                let k = *tube;
                let res = state.apply(&input, Action::Add { i: positions[0].0, j: positions[0].1, k });
                if res.is_err() {
                    panic!("絵の具を混ぜることができませんでした: {:?}", res);

                }
            }

            // 壁を戻す
            for ((i1, j1), (i2, j2)) in pairs.iter() {
                let res = state.apply(&input, Action::Toggle { i1: *i1, j1: *j1, i2: *i2, j2: *j2 });
                if res.is_err() {
                    panic!("壁を戻すことができませんでした: {:?}", res);
                }
            }

            // 絵の具を届ける
            let res = state.apply(&input, Action::Deliver { i: positions[tubes.len()-1].0, j: positions[tubes.len()-1].1 });
            if res.is_err() {
                panic!("絵の具を届けることができませんでした: {:?}", res);
            }

            // 余った絵の具を使う場所を仮決め
            if tubes.len() > 1 {
                // 余った絵の具を使うタイミングを決める
                let mut top_targets = vec![];
                for j in i+1..input.H {
                    if kari[j].len() > 0 {
                        continue;
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
                    let (d, j) = top_targets[i];
                    // チューブの方がマシなら捨てる
                    if input.D < ((d - input.basis_d[j])*10000.0).round() as i32 {
                        let (u, v) = positions[i];
                        let _ = state.apply(&input, Action::Discard { i: u, j: v });
                        ct -= 1;
                        continue;
                    }

                    kari_map[*recipe_id].push((positions[i].clone(), j));
                    kari[j].push((positions[i].clone(), *recipe_id));
                }
            }
            
            break;
        }
    }
    state
}

macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

fn get_ids(
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
    pub basis_d: Vec<f64>,
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
    errors: Vec<f64>,
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
            errors: scores,
        }
    }

    fn apply(&mut self, input: &Input, action: Action) -> Result<(), String> {
        // println!("apply: {:?}", action);
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
                self.errors[self.delivered.len()] = ((color[0] - target[0]).powi(2)
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

    fn get_score(&self, input: &Input) -> i32 {
        1 + input.D * (self.V - input.H as i32) + (self.errors.iter().sum::<f64>() * 10000.0) as i32
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
        let (_, ids, _) = get_ids(&self.wall_v, &self.wall_h);
        let mut seen = vec![vec![false; input.N]; input.N];
        // DFSでn個の空きセルを探す
        for i in 0..input.N {
            for j in 0..input.N {

                if seen[i][j] || self.vols[ids[i][j]] > 0.0 {
                    continue; // すでに訪れたセル、または絵の具があるセルはスキップ
                }
                let mut stack = vec![];
                stack.push((i, j));
                while stack.len() > 0 {
                    let (x, y) = stack.pop().unwrap();
                    if x == input.N - 1 && y == 0 {
                        continue; // 最後のセルは必ず空きにしたい
                    }
                    if seen[x][y] || self.vols[ids[x][y]] > 0.0 {
                        continue; // すでに訪れたセル、または絵の具があるセルはスキップ
                    }
                    seen[x][y] = true;
                    positions.push((x, y));
                    if positions.len() == n {
                        found = true;
                        break;
                    }
                    
                    // 隣接するセルを探索 右>左>上>下 の優先度で探索
                    if x + 1 < input.N && self.vols[ids[x+1][y]] == 0.0 && !seen[x + 1][y] {
                        stack.push((x + 1, y));
                    }
                    if x > 0 && self.vols[ids[x-1][y]] == 0.0 && !seen[x - 1][y] {
                        stack.push((x - 1, y));
                    }
                    if y > 0 && self.vols[ids[x][y-1]] == 0.0 && !seen[x][y - 1] {
                        stack.push((x, y - 1));
                    }
                    if y + 1 < input.N && self.vols[ids[x][y+1]] == 0.0 && !seen[x][y + 1] {
                        stack.push((x, y + 1));
                    }
                }

                if found {
                    return Some(positions);
                } else {
                    positions.clear(); // 位置をクリアして次のセルから再探索
                }
            }
        }

        return None;

    }
}
