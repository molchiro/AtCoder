#![allow(non_snake_case, unused_macros)]

use core::panic;
use itertools::Itertools;
use proconio::input;
use rand::prelude::*;
use std::collections::VecDeque;
use std::collections::{HashMap, HashSet};

const TIME_LIMIT: u128 = 1950; // ミリ秒
const SEED: u64 = 123456789;

fn main() {
    let start_time = std::time::Instant::now();
    let mut rng = rand_chacha::ChaCha20Rng::seed_from_u64(SEED);

    input! {
        N: usize, M: usize, K: usize,
        pos: [(i64, i64); N + M],
        ps: [[f64; N]; K],
    }

    let input = Input {
        N,
        M,
        K,
        pos: pos.clone(),
        ps: ps.clone(),
    };

    // 一番左端の点から始める
    let s = pos
        .iter()
        .enumerate()
        .filter(|&(i, _)| i >= N)
        .min_by_key(|&(_, &(x, _))| x)
        .map(|(i, _)| i)
        .unwrap();

    let mut mask = vec![false; N + M];
    // 最大500個になるようランダムなソーターをマスク
    let mask_lim = 120;
    let num_to_mask = if M > mask_lim { M - mask_lim } else { 0 };
    for v in (N..(M + N)).choose_multiple(&mut rng, num_to_mask) {
        if v == s {
            continue; // 始点はマスクしない
        }
        mask[v] = true;
    }

    let edges = delaunay_edges(&pos, &mask);
    let mut graph = vec![vec![]; N + M];
    for (u, v) in edges {
        if u < N {
            graph[v].push(u);
        } else if v < N {
            graph[u].push(v);
        } else {
            graph[u].push(v);
            graph[v].push(u);
        }
    }

    if graph[s].is_empty() {
        // 始点が孤立している場合は異常
        panic!("始点が孤立している");
    }

    let mut ans = vec![vec![]; M];
    let mut visited = vec![false; N + M];
    let mut queue = VecDeque::new();
    let mut ct = 0;
    queue.push_back(s);
    while let Some(u) = queue.pop_front() {
        ct += 1;
        if u < N {
            continue; // 終点は無視
        }
        if visited[u] {
            continue;
        }
        visited[u] = true;

        let mut to = vec![];
        if !queue.is_empty() {
            // 端点がもう一つあるなら一つはそこを使う
            if graph[u].contains(queue.back().unwrap()) {
                to.push(*queue.back().unwrap());
            }
        }
        // let graph_u = graph[u].clone();

        for &v in &graph[u] {
            if to.len() >= 2 {
                break; // 2つ以上の隣接点があれば十分
            }
            if !visited[v] {
                if to.contains(&v) {
                    continue; // 既に追加済みの隣接点はスキップ
                }
                if ct < N * 1 && v < N {
                    continue; // 序盤なら端点はスキップ
                }
                to.push(v);
            }
        }

        if to.is_empty() {
            continue; // 隣接点がない場合はスキップ
        }
        if to.len() == 1 {
            let v1 = to[0];
            ans[u - N] = [0, v1, v1].to_vec();
            if v1 >= N {
                queue.push_back(v1);
            } else {
                visited[v1] = true; // 端点は訪問済みにする
            }
        } else {
            let v1 = to[0];
            let v2 = to[1];
            ans[u - N] = [0, v1, v2].to_vec();
            if v1 >= N {
                queue.push_back(v1);
            } else {
                visited[v1] = true; // 端点は訪問済みにする
            }
            if v2 >= N {
                queue.push_back(v2);
            } else {
                visited[v2] = true; // 端点は訪問済みにする
            }
        }
    }

    // 枝刈り
    let mut done = false;
    while !done {
        done = true;
        for i in 0..M {
            if ans[i].is_empty() {
                continue;
            }
            if let [s, v1, v2] = ans[i].as_slice() {
                if v1 == v2 {
                    if *v1 >= N && ans[*v1 - N].is_empty() {
                        ans[i].clear();
                        done = false; // 変更があったので再度チェック
                    }
                } else {
                    if *v1 >= N && ans[*v1 - N].is_empty() {
                        ans[i] = [*s, *v2, *v2].to_vec();
                        done = false; // 変更があったので再度チェック
                    } else if *v2 >= N && ans[*v2 - N].is_empty() {
                        ans[i] = [*s, *v1, *v1].to_vec();
                        done = false; // 変更があったので再度チェック
                    }
                }
            }
        }
    }

    let mut init_output = Output {
        ds: (0..N).collect(),
        s,
        cs: ans
            .iter()
            .enumerate()
            .map(|(_, v)| {
                if v.is_empty() {
                    (!0, !0, !0)
                } else {
                    (0, v[1], v[2])
                }
            })
            .collect(),
    };

    // sorterの番号をランダムに入れ替える
    // for i in 0..M {
    //     if output.cs[i].0 == !0 {
    //         continue;
    //     }
    //     output.cs[i].0 = rng.gen_range(0..K);
    // }

    let mut best_score = compute_score_details(&input, &init_output);
    let mut best_output = init_output.clone();

    // 時間の許す限りprocessorの入れ替え順列を総当たりで試す
    for perm in (0..N).permutations(N) {
        if start_time.elapsed().as_millis() >= TIME_LIMIT {
            break; // 2秒経過したら終了
        }
        let mut inner_best_output = init_output.clone();
        inner_best_output.ds = perm;
        let mut inner_best_score = compute_score_details(&input, &inner_best_output);
        // 時間の許す限りsorterの番号、v1とv2の入れ替えを試す
        let mut visited = vec![false; N + M];
        let mut queue = VecDeque::new();
        queue.push_back(init_output.s);
        while let Some(u) = queue.pop_front() {
            if start_time.elapsed().as_millis() >= TIME_LIMIT {
                break; // 2秒経過したら終了
            }
            if u < N {
                continue; // 終点は無視
            }
            if visited[u] {
                continue;
            }
            visited[u] = true;
            for i in 0..K {
                let current_sorter = inner_best_output.cs[u - N].0;
                let current_v1 = inner_best_output.cs[u - N].1;
                let current_v2 = inner_best_output.cs[u - N].2;
                let mut best_pattern = 0;
                if !visited[current_v1] {
                    queue.push_back(current_v1);
                }
                if !visited[current_v2] {
                    queue.push_back(current_v2);
                }

                // v1とv2の入れ替え
                inner_best_output.cs[u - N].1 = current_v2;
                inner_best_output.cs[u - N].2 = current_v1;
                let score = compute_score_details(&input, &inner_best_output);
                if score.0 == inner_best_score.0 {
                    break;
                }
                if score.0 < inner_best_score.0 {
                    inner_best_score = score;
                    best_pattern = 1;
                }

                // sorterの番号を入れ替える
                if current_sorter != i {
                    inner_best_output.cs[u - N].0 = i;
                    inner_best_output.cs[u - N].1 = current_v1;
                    inner_best_output.cs[u - N].2 = current_v2;
                    let score = compute_score_details(&input, &inner_best_output);
                    if score.0 < inner_best_score.0 {
                        inner_best_score = score;
                        best_pattern = 2;
                    }
    
                    // sorterの入れ替え+v1とv2の入れ替え
                    inner_best_output.cs[u - N].0 = i;
                    inner_best_output.cs[u - N].1 = current_v2;
                    inner_best_output.cs[u - N].2 = current_v1;
                    let score = compute_score_details(&input, &inner_best_output);
                    if score.0 < inner_best_score.0 {
                        inner_best_score = score;
                        best_pattern = 3;
                    }
                }

                if best_pattern == 0 {
                    inner_best_output.cs[u - N].0 = current_sorter;
                    inner_best_output.cs[u - N].1 = current_v1;
                    inner_best_output.cs[u - N].2 = current_v2;
                } else if best_pattern == 1 {
                    inner_best_output.cs[u - N].0 = current_sorter;
                    inner_best_output.cs[u - N].1 = current_v2;
                    inner_best_output.cs[u - N].2 = current_v1;
                } else if best_pattern == 2 {
                    inner_best_output.cs[u - N].0 = i;
                    inner_best_output.cs[u - N].1 = current_v1;
                    inner_best_output.cs[u - N].2 = current_v2;
                } else if best_pattern == 3 {
                    inner_best_output.cs[u - N].0 = i;
                    inner_best_output.cs[u - N].1 = current_v2;
                    inner_best_output.cs[u - N].2 = current_v1;
                }
            }
        }
        if inner_best_score.0 < best_score.0 {
            best_score = inner_best_score;
            best_output = inner_best_output;
        }
    }

    best_output.print();
}

type Edge = (usize, usize);

fn canonical_edge(a: usize, b: usize) -> Edge {
    if a < b {
        (a, b)
    } else {
        (b, a)
    }
}

/// orient を i128 で計算（>0 が CCW）
fn orient_i128(a: (i64, i64), b: (i64, i64), c: (i64, i64)) -> i128 {
    let (ax, ay) = a;
    let (bx, by) = b;
    let (cx, cy) = c;
    let v1x = bx as i128 - ax as i128;
    let v1y = by as i128 - ay as i128;
    let v2x = cx as i128 - ax as i128;
    let v2y = cy as i128 - ay as i128;
    v1x * v2y - v1y * v2x
}

/// 外接円判定（すべて i128 で計算）
/// 前提：引数の (a,b,c) が CCW になっていること
fn in_circumcircle_i128(p: (i64, i64), a: (i64, i64), b: (i64, i64), c: (i64, i64)) -> bool {
    let (px, py) = p;
    let (ax, ay) = a;
    let (bx, by) = b;
    let (cx, cy) = c;

    let ax = ax as i128 - px as i128;
    let ay = ay as i128 - py as i128;
    let bx = bx as i128 - px as i128;
    let by = by as i128 - py as i128;
    let cx = cx as i128 - px as i128;
    let cy = cy as i128 - py as i128;

    let a2 = ax * ax + ay * ay;
    let b2 = bx * bx + by * by;
    let c2 = cx * cx + cy * cy;

    // det = a2 * (bx*cy - cx*by) - b2 * (ax*cy - cx*ay) + c2 * (ax*by - bx*ay)
    let det = a2 * (bx * cy - cx * by) - b2 * (ax * cy - cx * ay) + c2 * (ax * by - bx * ay);

    det > 0 // 厳密に内側なら true。境界を含めたいなら det >= 0 に変更
}

/// ドロネー三角分割の辺集合を返す（整数版）
pub fn delaunay_edges(points: &Vec<(i64, i64)>, mask: &Vec<bool>) -> Vec<Edge> {
    let mut pts: Vec<(i64, i64)> = points.clone();
    let p0 = (0_i64, 5000_i64);
    let p0_idx = pts.len();
    pts.push(p0);

    // スーパー三角形（十分大きく固定）
    let p1 = (-1_i64, -1_i64);
    let p2 = (-1_i64, 1_000_000_i64);
    let p3 = (1_000_000_i64, -1_i64);
    let p1_idx = pts.len();
    let p2_idx = pts.len() + 1;
    let p3_idx = pts.len() + 2;

    let mut all_pts = pts.clone();
    all_pts.push(p1);
    all_pts.push(p2);
    all_pts.push(p3);

    let mut triangles: Vec<(usize, usize, usize)> = vec![(p1_idx, p2_idx, p3_idx)];

    for (pi, &p) in pts.iter().enumerate() {
        if pi < pts.len() - 1 && mask[pi] {
            continue; // マスクされている点は無視
        }
        let mut bad_triangles = Vec::new();
        for &(a, b, c) in &triangles {
            // 三角形の向きを i128 で判定し、CCW に合わせる
            let pa = all_pts[a];
            let pb = all_pts[b];
            let pc = all_pts[c];
            let cross = orient_i128(pa, pb, pc);
            let (a1, b1, c1) = if cross > 0 { (a, b, c) } else { (a, c, b) };

            if in_circumcircle_i128(p, all_pts[a1], all_pts[b1], all_pts[c1]) {
                bad_triangles.push((a, b, c));
            }
        }

        let mut edge_count: HashMap<Edge, usize> = HashMap::new();
        for &(a, b, c) in &bad_triangles {
            for &(u, v) in &[(a, b), (b, c), (c, a)] {
                let e = canonical_edge(u, v);
                *edge_count.entry(e).or_insert(0) += 1;
            }
        }

        let polygon: Vec<Edge> = edge_count
            .into_iter()
            .filter(|&(_, cnt)| cnt == 1)
            .map(|(e, _)| e)
            .collect();

        triangles.retain(|t| !bad_triangles.contains(t));

        for (u, v) in polygon {
            let a = all_pts[u];
            let b = all_pts[v];
            let c = all_pts[pi];
            // 反時計回りに揃えて追加
            let cross = orient_i128(a, b, c);
            if cross > 0 {
                triangles.push((u, v, pi));
            } else {
                triangles.push((v, u, pi));
            }
        }
    }

    let super_ids: HashSet<usize> = [p1_idx, p2_idx, p3_idx, p0_idx].into_iter().collect();
    triangles.retain(|&(a, b, c)| {
        !super_ids.contains(&a) && !super_ids.contains(&b) && !super_ids.contains(&c)
    });

    let mut edge_set = HashSet::new();
    for &(a, b, c) in &triangles {
        edge_set.insert(canonical_edge(a, b));
        edge_set.insert(canonical_edge(b, c));
        edge_set.insert(canonical_edge(c, a));
    }

    let mut edges: Vec<Edge> = edge_set.into_iter().collect();

    // ソートキー：中心(5000,5000) に対する距離（i128）
    // let center = (5000_i64, 5000_i64);
    // edges.sort_unstable_by_key(|&(u, v)| {
    //     let dux = all_pts[u].0 as i128 - center.0 as i128;
    //     let duy = all_pts[u].1 as i128 - center.1 as i128;
    //     let dvx = all_pts[v].0 as i128 - center.0 as i128;
    //     let dvy = all_pts[v].1 as i128 - center.1 as i128;
    //     let dist_u = dux*dux + duy*duy;
    //     let dist_v = dvx*dvx + dvy*dvy;
    //     (dist_u, dist_v)
    // });

    // x座標でソート
    edges.sort_by_key(|&(u, v)| {
        let (x1, _) = all_pts[u];
        let (x2, _) = all_pts[v];
        (x1, x2)
    });

    // (0, 0)に近い順にソート
    // edges.sort_unstable_by_key(|&(u, v)| {
    //     let (x1, y1) = all_pts[u];
    //     let (x2, y2) = all_pts[v];
    //     let dist1 = (x1 * x1 + y1 * y1) as
    //     i128;
    //     let dist2 = (x2 * x2 + y2 * y2) as
    //     i128;
    //     (dist1, dist2)
    // });

    edges
}

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
    pub K: usize,
    pub pos: Vec<(i64, i64)>,
    pub ps: Vec<Vec<f64>>,
}

#[derive(Clone)]
pub struct Output {
    pub ds: Vec<usize>,
    pub s: usize,
    pub cs: Vec<(usize, usize, usize)>,
}

impl Output {
    fn print(&self) {
        println!(
            "{}",
            self.ds
                .iter()
                .map(|x| x.to_string())
                .collect::<Vec<_>>()
                .join(" ")
        );
        println!("{}", self.s);
        for (_, &(s, v1, v2)) in self.cs.iter().enumerate() {
            if s == !0 {
                println!("-1");
            } else {
                println!("{} {} {}", s, v1, v2);
            }
        }
    }
}

pub fn compute_score_details(input: &Input, out: &Output) -> (i64, String, Vec<Vec<f64>>) {
    let mut probs = mat![0.0; input.N + input.M; input.N];
    let mut tmp = out.ds.clone();
    tmp.sort();
    tmp.dedup();
    let mut segs = vec![((0, 5000), input.pos[out.s])];
    let mut g = vec![vec![]; input.N + input.M];
    for i in 0..input.M {
        if out.cs[i].0 == !0 {
            continue;
        }
        segs.push((input.pos[input.N + i], input.pos[out.cs[i].1]));
        segs.push((input.pos[input.N + i], input.pos[out.cs[i].2]));
        g[input.N + i].push(out.cs[i].1);
        g[input.N + i].push(out.cs[i].2);
    }
    for i in 0..segs.len() {
        for j in 0..i {
            if segs[i].0 == segs[j].0
                || segs[i].0 == segs[j].1
                || segs[i].1 == segs[j].0
                || segs[i].1 == segs[j].1
            {
                continue;
            }
        }
    }
    let Some(order) = topological_sort(&g) else {
        return (0, "Graph contains a cycle".to_owned(), probs);
    };
    probs[out.s].fill(1.0);
    for u in order {
        if u >= input.N {
            let u = u - input.N;
            let k = out.cs[u].0;
            if k == !0 {
                continue;
            }
            let (v1, v2) = (out.cs[u].1, out.cs[u].2);
            for i in 0..input.N {
                probs[v1][i] += probs[u + input.N][i] * input.ps[k][i];
                probs[v2][i] += probs[u + input.N][i] * (1.0 - input.ps[k][i]);
            }
        }
    }
    let mut score = 0.0;
    for i in 0..input.N {
        let d = out.ds[i];
        let q = probs[i][d];
        score += 1.0 - q;
    }
    score /= input.N as f64;
    let score = (1e9 * score).round() as i64;
    (score, String::new(), probs)
}

pub fn topological_sort(adj: &Vec<Vec<usize>>) -> Option<Vec<usize>> {
    let n = adj.len();
    let mut in_deg = vec![0; n];
    for u in 0..n {
        for &v in &adj[u] {
            in_deg[v] += 1;
        }
    }
    let mut queue = VecDeque::new();
    for u in 0..n {
        if in_deg[u] == 0 {
            queue.push_back(u);
        }
    }
    let mut order = Vec::with_capacity(n);
    while let Some(u) = queue.pop_front() {
        order.push(u);
        for &v in &adj[u] {
            in_deg[v] -= 1;
            if in_deg[v] == 0 {
                queue.push_back(v);
            }
        }
    }
    if order.len() == n {
        Some(order)
    } else {
        None
    }
}
