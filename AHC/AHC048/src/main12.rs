#![allow(non_snake_case, unused_macros)]

use core::panic;

use im_rc::HashMap;
use proconio::input;


const RECIPE_N_CAP: usize = 12000; // レシピの数の上限

fn main() {
    input! {
        N: usize, K: usize, H: usize, T: usize, D: i32,
        own: [[f64; 3]; K],
        target: [[f64; 3]; H],
    }
    
    let mut basis_d = vec![];
    for (_, colors) in target.iter().enumerate() {
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
    let mut iterations = 3;
    if input.K < 21 {
        iterations += 1

    }
    if input.K < 13 {
        iterations += 1

    }
    if input.K < 10 {
        iterations += 1
    }
    if input.K < 8 {
        iterations += 1
    }
    if input.K < 6 {
        iterations += 1
    }

    create_recipe_map(input.clone(), iterations, &mut recipe_map);
        
    // 必ず全ての壁を上げた状態からスタート
    for _ in 0..N {
        println!("{}", "1 ".repeat(N - 1).trim());
    }
    for _ in 0..N-1 {
        println!("{}", "1 ".repeat(N).trim());
    }

    let best_state = solve(input.clone(), recipe_map, iterations);

    // 最高のスコアだった時のactionsを出力
    for action in best_state.actions.iter() {
        match action {
            Action::Add { i, j, k } => println!("1 {} {} {}", i, j, k),
            Action::Deliver { i, j , color: _} => println!("2 {} {}", i, j),
            Action::Discard { i, j } => println!("3 {} {}", i, j),
            Action::Toggle { i1, j1, i2, j2 } => println!("4 {} {} {} {}", i1, j1, i2, j2),
        }
    }

}

fn create_recipe_map(input: Input, tube_number_cap: usize, recipe_map: &mut HashMap<Vec<usize>, ([f64; 3], Vec<usize>)>) {
    if tube_number_cap >= 1 {
        // 1種類の絵の具
        for i in 0..input.K {
            recipe_map.insert(vec![i], (input.own[i], vec![i]));

        }
    }
    if tube_number_cap >= 2 {
        // 2種類の絵の具
        for i in 0..input.K {
            for j in i + 1..input.K {
                recipe_map.insert(vec![i,j],(mix(1.0, input.own[i], 1.0, input.own[j]), vec![i, j]));
            }
        }
    }

    if tube_number_cap >= 3 {
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

    if tube_number_cap >= 4 {
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

    if tube_number_cap >= 5 {
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

    if tube_number_cap >= 6 {
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
    if tube_number_cap >= 7 {
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
    if tube_number_cap >= 8 {
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
}

fn solve(input: Input, recipe_map: HashMap<Vec<usize>, ([f64; 3], Vec<usize>)>, tube_number_cap: usize) -> State {
    let mut beam_width_1: usize = 7;
    // const BEAM2: usize = 4;

    
    let mut recipes = vec![];
    for (recipe_id, (_, (color,tubes))) in recipe_map.iter().enumerate() {
        recipes.push(Recipe::new(recipe_id, color.clone(), tubes.clone()));
    }
    recipes.truncate(RECIPE_N_CAP);
    // println!("{} recipes available", recipes.len());

    if recipes.len() < 1000 {
        beam_width_1 += 4
    }
    if recipes.len() < 1500 {
        beam_width_1 += 2
    }
    if recipes.len() < 2000 {
        beam_width_1 += 4
    }
    if recipes.len() < 2500 {
        beam_width_1 += 1
    }
    if recipes.len() < 3000 {
        beam_width_1 += 3
    }
    if recipes.len() < 4000 {
        beam_width_1 += 1
    }
    // if recipes.len() < 7500 {
    //     beam_width_1 += 1
    // }

    let init_state = State::new(
        vec![vec![true; input.N - 1]; input.N],
        vec![vec![true; input.N]; input.N - 1],
        input.clone(),
        recipes.len(),
    );

    let mut states = vec![];
    states.push(init_state.clone());

    for i in 0..input.H {
        // println!("Processing delivery {}", i + 1);
        let mut  next_states = vec![];
        for current_state in states.iter() {
            
            // 予約済みなら即座に届ける
            if current_state.kari[i].len() > 0 {
                let mut state = current_state.clone();
                let res = state.deliver_reserved(&input, i);
                if res.is_err() {
                    continue;
                }
                next_states.push(state);
                continue;
            } else {

                // recipesの中から最も近い色を探す
                let mut top_recipes = vec![];
                for recipe_id in 0..recipes.len() {
                    let color = &recipes[recipe_id].color;
                    let tubes = &recipes[recipe_id].tubes;
                    if input.H - current_state.ct < tubes.len() {
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
    
                if top_recipes.len() == 0 {
                    panic!("No recipes available for delivery at index {}", i);
                }

    
                // 最も近い色から順に試す
                let mut beam_count = 0;
                for (_, recipe_id) in top_recipes.iter() {
                    // if i < 200 {
                    //     if beam_count >= BEAM2 {
                    //         break; 
                    //     }
                    // } else {
                    //     if beam_count >= BEAM2 / 2 {
                    //         break; // 後半はBEAMを半分にする
                    //     }
                    // }
                    if next_states.len() >= beam_width_1 {
                        break; // BEAM数以上の状態は保持しない
                    }
                    let mut state = current_state.clone();
                    if state.is_in_palette(*recipe_id) {
                        let res = state.deliver_from_palette(&input, &recipes[*recipe_id]);
                        if res.is_err() {
                            panic!("絵の具を届けることができませんでした: {:?}", res);
                        }
                    } else {
                        let res = state.create_recipe_and_deliver(&input, &recipes[*recipe_id]);
                        if res.is_err() {
                            // 作れなかったら次のレシピを試す
                            continue;
                        }
                    }
                    beam_count += 1;
                    next_states.push(state);
                }
            }

        }
        next_states.sort_by(|a, b| {
            (a.penalty_cumsum / a.ct as f64)
                .partial_cmp(&(b.penalty_cumsum / b.ct as f64))
                .unwrap()
        });
        next_states.truncate(beam_width_1);
        states = next_states;
    }
    // 最終スコアでソート
    states.sort_by(|a, b| {
        (a.get_score(&input))
            .partial_cmp(&(b.get_score(&input)))
            .unwrap()
    });
    states[0].clone() // 最も良い状態を返す
}

macro_rules! mat {
	($($e:expr),*) => { Vec::from(vec![$($e),*]) };
	($($e:expr,)*) => { Vec::from(vec![$($e),*]) };
	($e:expr; $d:expr) => { Vec::from(vec![$e; $d]) };
	($e:expr; $d:expr $(; $ds:expr)+) => { Vec::from(vec![mat![$e $(; $ds)*]; $d]) };
}

#[derive(Clone)]
struct Recipe {
    recipe_id: usize,
    color: [f64; 3],
    tubes: Vec<usize>,
}

impl Recipe {
    fn new(recipe_id: usize, color: [f64; 3], tubes: Vec<usize>) -> Self {
        Recipe { recipe_id, color, tubes }
    }
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
        color: [f64; 3],
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
    vols: Vec<Vec<f64>>,
    delivered: Vec<[f64; 3]>,
    V: i32,
    actions: Vec<Action>,
    errors: Vec<f64>,
    kari_map: Vec<Vec<((usize, usize), usize)>>,
    kari: Vec<Vec<((usize, usize), Recipe)>>,
    ct: usize, // 配達済みor仮決め済みの数
    penalty_cumsum: f64,
}

impl State {
    fn new(wall_v: Vec<Vec<bool>>, wall_h: Vec<Vec<bool>>, input: Input, recipe_n: usize) -> Self {
        let vols = vec![vec![0.0; input.N]; input.N];
        let errors = vec![1.0; input.H];
        let kari_map = vec![vec![]; recipe_n];
        let kari = vec![vec![]; input.H];
        Self {
            wall_v: wall_v.clone(),
            wall_h: wall_h.clone(),
            vols,
            delivered: vec![],
            V: 0,
            actions: vec![],
            errors,
            kari_map,
            kari,
            ct: 0,
            penalty_cumsum: 0.0,
        }
    }

    fn apply(&mut self, input: &Input, action: Action) -> Result<(), String> {
        // println!("apply: {:?}", action);
        match action {
            Action::Add { i, j, k } => {
                self.V += 1;
                self.vols[i][j] += 1.0;
            }
            Action::Deliver { i, j , color} => {
                let target = input.target[self.delivered.len()];
                self.errors[self.delivered.len()] = ((color[0] - target[0]).powi(2)
                    + (color[1] - target[1]).powi(2)
                    + (color[2] - target[2]).powi(2))
                .sqrt();
                self.vols[i][j] = 0.0;
                self.delivered.push(color);
            }
            Action::Discard { i, j } => {
                self.vols[i][j] = 0.0;
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
            }
        }
        self.actions.push(action);
        Ok(())
    }

    fn deliver_reserved(&mut self, input: &Input, u: usize) -> Result<(), String> {
        let ((i1, j1), recipe) = self.kari[u].pop().unwrap();
        self.kari_map[recipe.recipe_id].retain(|&(_, idx)| idx != u);
        let res = self.apply(input, Action::Deliver { i: i1, j: j1, color: recipe.color });
        if res.is_err() {
            return Err(format!("Failed to deliver reserved paint: {:?}", res));
        }
        Ok(())
    }

    fn is_in_palette(&self, recipe_id: usize) -> bool {
        self.kari_map[recipe_id].len() > 0
    }

    fn deliver_from_palette(
        &mut self,
        input: &Input,
        recipe: &Recipe,
    ) -> Result<(), String> {
        if !self.is_in_palette(recipe.recipe_id) {
            return Err("Recipe not in palette".to_owned());
        }
        let ((i, j), target) = self.kari_map[recipe.recipe_id].pop().unwrap();
        self.kari[target].pop();

        let d1 = ((recipe.color[0] - input.target[target][0]).powi(2)
            + (recipe.color[1] - input.target[target][1]).powi(2)
            + (recipe.color[2] - input.target[target][2]).powi(2))
            .sqrt();
        self.penalty_cumsum -= d1 * 10000.0;
        let d2 = ((recipe.color[0] - input.target[self.delivered.len()][0]).powi(2)
        + (recipe.color[1] - input.target[self.delivered.len()][1]).powi(2)
        + (recipe.color[2] - input.target[self.delivered.len()][2]).powi(2))
        .sqrt();
        self.penalty_cumsum += d2 * 10000.0;

        self.apply(input, Action::Deliver { i, j , color: recipe.color })
    }

    fn create_recipe_and_deliver(&mut self, input: &Input, recipe: &Recipe) -> Result<(), String> {

        let positions = self.find_n_size_well(&input, recipe.tubes.len());
        if positions.is_none() {
            return Err("No suitable positions found for the recipe".to_owned());
        }

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
            let res = self.apply(&input, Action::Toggle { i1: *i1, j1: *j1, i2: *i2, j2: *j2 });
            if res.is_err() {
                panic!("壁を下げることができませんでした: {:?}", res);
            }
        }
        // 絵の具を混ぜる
        for (tube, (i, j)) in recipe.tubes.iter().zip(positions.iter()) {
            let k = *tube;
            let res = self.apply(&input, Action::Add { i: *i, j: *j, k });
            if res.is_err() {
                panic!("絵の具を混ぜることができませんでした: {:?}", res);

            }
        }

        // 壁を戻す
        for ((i1, j1), (i2, j2)) in pairs.iter() {
            let res = self.apply(&input, Action::Toggle { i1: *i1, j1: *j1, i2: *i2, j2: *j2 });
            if res.is_err() {
                panic!("壁を戻すことができませんでした: {:?}", res);
            }
        }

        // 絵の具を届ける
        let d = ((recipe.color[0] - input.target[self.delivered.len()][0]).powi(2)
        + (recipe.color[1] - input.target[self.delivered.len()][1]).powi(2)
        + (recipe.color[2] - input.target[self.delivered.len()][2]).powi(2))
        .sqrt();
        let res = self.apply(&input, Action::Deliver { i: positions[recipe.tubes.len()-1].0, j: positions[recipe.tubes.len()-1].1 , color: recipe.color });
        if res.is_err() {
            panic!("絵の具を届けることができませんでした: {:?}", res);
        }
        self.penalty_cumsum += d * 10000.0;

        self.ct += recipe.tubes.len();
        // 余った絵の具を使う場所を仮決め
        if recipe.tubes.len() > 1 {
            // 余った絵の具を使うタイミングを決める
            let mut top_targets = vec![];
            for j in self.delivered.len()..input.H {
                if self.kari[j].len() > 0 {
                    continue;
                }
                let d = ((recipe.color[0] - input.target[j][0]).powi(2)
                    + (recipe.color[1] - input.target[j][1]).powi(2)
                    + (recipe.color[2] - input.target[j][2]).powi(2))
                    .sqrt();
                top_targets.push((d, j));
            }
            // 距離でソート
            top_targets.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
            for i in 0..recipe.tubes.len() - 1 {
                let (d, target) = top_targets[i];
                // チューブ直の方がマシなら捨てる
                if input.D < ((d - input.basis_d[target])*10000.0).round() as i32 {
                    let (u, v) = positions[i];
                    let _ = self.apply(&input, Action::Discard { i: u, j: v });
                    self.penalty_cumsum += input.D as f64;
                    self.ct -= 1;
                    continue;
                }

                self.kari_map[recipe.recipe_id].push((positions[i].clone(), target));
                self.kari[target].push((positions[i].clone(), recipe.clone()));
                self.penalty_cumsum += d * 10000.0;
            }
        }
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
            return Some(vec![(input.N - 1, input.N - 1)]);
        }

        let mut found = false;
        let mut positions = vec![];
        let mut seen = vec![vec![false; input.N]; input.N];
        // DFSでn個の空きセルを探す
        for i in 0..input.N {
            for j in 0..input.N {

                if seen[i][j] || self.vols[i][j] > 0.0 {
                    continue; // すでに訪れたセル、または絵の具があるセルはスキップ
                }
                let mut stack = vec![];
                stack.push((i, j));
                while stack.len() > 0 {
                    let (x, y) = stack.pop().unwrap();
                    if x == input.N-1 && y == input.N-1 {
                        continue; // 最後のセルは必ず空きにしたい
                    }
                    if seen[x][y] || self.vols[i][j] > 0.0 {
                        continue; // すでに訪れたセル、または絵の具があるセルはスキップ
                    }
                    seen[x][y] = true;
                    positions.push((x, y));
                    if positions.len() == n {
                        found = true;
                        break;
                    }
                    
                    
                    // 隣接するセルを探索 右>左>上>下 の優先度で探索
                    if x + 1 < input.N && self.vols[x+1][y] == 0.0 && !seen[x + 1][y] {
                        stack.push((x + 1, y));
                    }
                    if x > 0 && self.vols[x-1][y] == 0.0 && !seen[x - 1][y] {
                        stack.push((x - 1, y));
                    }
                    if y > 0 && self.vols[x][y-1] == 0.0 && !seen[x][y - 1] {
                        stack.push((x, y - 1));
                    }
                    if y + 1 < input.N && self.vols[x][y+1] == 0.0 && !seen[x][y + 1] {
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
