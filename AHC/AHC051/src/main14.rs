#![allow(non_snake_case, unused_macros)]

use itertools::Itertools;
use proconio::input;
use rand::prelude::*;
use std::collections::VecDeque;
use std::collections::{HashMap, HashSet};

const TIME_LIMIT: u128 = 1980; // ミリ秒
const SEED: u64 = 123456789;
const MASK_LIMIT: usize = 120;

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

    let (mut best_score, mut best_output, best_sorters, mut order) = create_init_output(&input, &mut rng);

    // 時間が大量に余っていれば繰り返す
    while start_time.elapsed().as_millis() < TIME_LIMIT*5 / 7 {
        let (score, output, _, new_order) = create_init_output(&input, &mut rng);
        if score < best_score {
            best_score = score;
            best_output = output;
            order = new_order;
            // best_sorters = sorters; // ソーターの入れ替えはしない
        }
    }

    let init_output = best_output.clone();

    // init_output.print();

    // 時間の許す限りprocessorの入れ替え順列を総当たりで試す
    if input.N <= 5 {
        for (i, perm) in (0..N).permutations(N).enumerate() {
            // break;
            if i == 0 {
                continue; // 最初の順列は初期状態なのでスキップ
            }
            if start_time.elapsed().as_millis() >= TIME_LIMIT {
                break; // 2秒経過したら終了
            }
            let mut inner_best_output = init_output.clone();
            inner_best_output.ds = perm;
            let mut inner_best_score = compute_score_details(&input, &inner_best_output, &order);
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
                for sorter_i in best_sorters.iter() {
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
                    let score = compute_score_details(&input, &inner_best_output, &order);
                    if score == inner_best_score {
                        break;
                    }
                    if score < inner_best_score {
                        inner_best_score = score;
                        best_pattern = 1;
                    }

                    // sorterの番号を入れ替える
                    if current_sorter != *sorter_i {
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v1;
                        inner_best_output.cs[u - N].2 = current_v2;
                        let score = compute_score_details(&input, &inner_best_output, &order);
                        if score < inner_best_score {
                            inner_best_score = score;
                            best_pattern = 2;
                        }

                        // sorterの入れ替え+v1とv2の入れ替え
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v2;
                        inner_best_output.cs[u - N].2 = current_v1;
                        let score = compute_score_details(&input, &inner_best_output, &order);
                        if score < inner_best_score {
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
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v1;
                        inner_best_output.cs[u - N].2 = current_v2;
                    } else if best_pattern == 3 {
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v2;
                        inner_best_output.cs[u - N].2 = current_v1;
                    }
                }
            }
            if inner_best_score < best_score {
                best_score = inner_best_score;
                best_output = inner_best_output;
            }
            // break;
        }
    } else {
        let mut seen = Vec::new();
        seen.push(init_output.ds.clone());
        loop {
            // break;
            if start_time.elapsed().as_millis() >= TIME_LIMIT {
                break; // 2秒経過したら終了
            }
            let mut inner_best_output = init_output.clone();
            // ２箇所ランダムに選んでスワップ
            let chosen = (0..N).choose_multiple(&mut rng, 2);
            inner_best_output.ds.swap(chosen[0], chosen[1]);
            if seen.contains(&inner_best_output.ds) {
                continue; // 既に試した順列はスキップ
            }
            seen.push(inner_best_output.ds.clone());
            let mut inner_best_score = compute_score_details(&input, &inner_best_output, &order);
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
                for sorter_i in best_sorters.iter() {
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
                    let score = compute_score_details(&input, &inner_best_output, &order);
                    if score == inner_best_score {
                        break;
                    }
                    if score < inner_best_score {
                        inner_best_score = score;
                        best_pattern = 1;
                    }

                    // sorterの番号を入れ替える
                    if current_sorter != *sorter_i {
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v1;
                        inner_best_output.cs[u - N].2 = current_v2;
                        let score = compute_score_details(&input, &inner_best_output, &order);
                        if score < inner_best_score {
                            inner_best_score = score;
                            best_pattern = 2;
                        }

                        // sorterの入れ替え+v1とv2の入れ替え
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v2;
                        inner_best_output.cs[u - N].2 = current_v1;
                        let score = compute_score_details(&input, &inner_best_output, &order);
                        if score < inner_best_score {
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
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v1;
                        inner_best_output.cs[u - N].2 = current_v2;
                    } else if best_pattern == 3 {
                        inner_best_output.cs[u - N].0 = *sorter_i;
                        inner_best_output.cs[u - N].1 = current_v2;
                        inner_best_output.cs[u - N].2 = current_v1;
                    }
                }
            }
            if inner_best_score < best_score {
                best_score = inner_best_score;
                best_output = inner_best_output;
            }
            // break;
        }
    }

    best_output.print();
}

fn create_init_output(input: &Input, rng: &mut impl Rng) -> (i64, Output, Vec<usize>, Vec<usize>) {
    let mut best_sorters = vec![];

    let mut sorters = vec![];
    for i in 0..input.K {
        // 分散が大きいほど良いソーターとする

        let mut sum = 0.0;
        for j in 0..input.N {
            sum += (input.ps[i][j] - 0.5).powi(2);
        }
        sorters.push((sum, i));
    }
    sorters.sort_by(|a, b| a.0.partial_cmp(&b.0).unwrap());
    sorters.reverse();

    //　被らないように最大25個まで選ぶ
    for (_, i) in sorters {
        if best_sorters.contains(&i) {
            continue; // 既に選ばれているソーターはスキップ
        }
        best_sorters.push(i);
        if best_sorters.len() >= 25 {
            break;
        }
    }

    let mut mask = vec![false; input.N + input.M + 1];
    // ランダムなソーターをマスク
    // マスクしないソーターの最大数
    let mask_lim = MASK_LIMIT;
    let num_to_mask = if input.M > mask_lim {
        input.M - mask_lim
    } else {
        0
    };
    for v in (input.N..(input.M + input.N + 1)).choose_multiple(rng, num_to_mask) {
        if v == input.N + input.M {
            continue; // 始点はマスクしない
        }
        mask[v] = true;
    }

    let pos_with_start = [input.pos.clone(), vec![(0, 5000)]].concat();

    let edges = delaunay_edges(&pos_with_start, &mask);
    let mut graph = vec![vec![]; pos_with_start.len()];
    for (u, v) in edges {
        if u == input.N + input.M {
            graph[u].push(v);
        } else if v == input.N + input.M {
            graph[v].push(u);
        } else if u < input.N {
            graph[v].push(u);
        } else if v < input.N {
            graph[u].push(v);
        } else {
            graph[u].push(v);
            graph[v].push(u);
        }
    }

    // println!("graph: {:?}", graph);

    let mut best_score = i64::MAX;
    let mut best_output = Output::default();
    let mut order = vec![];
    // 4回までの初期解を試す
    let mut ct = 0;
    for s in graph[input.N + input.M].iter() {
        if s < &input.N {
            continue; // 始点は無視
        }
        let (score, output, new_order) = _create_init_output(input, &best_sorters, &graph, *s);
        if score < best_score {
            best_score = score;
            best_output = output;
            order = new_order;
        }
        ct += 1;
        if ct >= 5 {
            break;
        }
    }

    (best_score, best_output, best_sorters, order)
}

fn _create_init_output(
    input: &Input,
    sorters: &Vec<usize>,
    graph: &Vec<Vec<usize>>,
    s: usize,
) -> (i64, Output, Vec<usize>) {
    let mut ans = vec![vec![]; input.M];
    let mut visited = vec![false; input.N + input.M];
    let mut queue = VecDeque::new();
    let mut ct = 0;
    queue.push_back(s);
    while let Some(u) = queue.pop_front() {
        ct += 1;
        if u < input.N {
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
                if ct < (input.N).max(10) && v < input.N {
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
            ans[u - input.N] = [0, v1, v1].to_vec();
            if v1 >= input.N {
                queue.push_back(v1);
            } else {
                visited[v1] = true; // 端点は訪問済みにする
            }
        } else {
            let v1 = to[0];
            let v2 = to[1];
            ans[u - input.N] = [0, v1, v2].to_vec();
            if v1 >= input.N {
                queue.push_back(v1);
            } else {
                visited[v1] = true; // 端点は訪問済みにする
            }
            if v2 >= input.N {
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
        for i in 0..input.M {
            if ans[i].is_empty() {
                continue;
            }
            if let [s, v1, v2] = ans[i].as_slice() {
                if v1 == v2 {
                    if *v1 >= input.N && ans[*v1 - input.N].is_empty() {
                        ans[i].clear();
                        done = false; // 変更があったので再度チェック
                    }
                } else {
                    if *v1 >= input.N && ans[*v1 - input.N].is_empty() {
                        ans[i] = [*s, *v2, *v2].to_vec();
                        done = false; // 変更があったので再度チェック
                    } else if *v2 >= input.N && ans[*v2 - input.N].is_empty() {
                        ans[i] = [*s, *v1, *v1].to_vec();
                        done = false; // 変更があったので再度チェック
                    }
                }
            }
        }
    }

    let init_output = Output {
        ds: (0..input.N).collect(),
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

    if init_output.cs[s - input.N] == (!0, !0, !0) {
        return (i64::MAX, init_output, vec![]);
    }

    let order = calc_order(&input, &init_output);

    let mut best_score = compute_score_details(&input, &init_output, &order);
    let mut best_output = init_output.clone();

    let mut inner_best_output = init_output.clone();
    let mut inner_best_score = compute_score_details(&input, &inner_best_output, &order);
    // 時間の許す限りsorterの番号、v1とv2の入れ替えを試す
    let mut visited = vec![false; input.N + input.M];
    let mut queue = VecDeque::new();
    queue.push_back(init_output.s);
    while let Some(u) = queue.pop_front() {
        if u < input.N {
            continue; // 終点は無視
        }
        if visited[u] {
            continue;
        }
        visited[u] = true;
        for sorter_i in sorters.iter() {
            let current_sorter = inner_best_output.cs[u - input.N].0;
            let current_v1 = inner_best_output.cs[u - input.N].1;
            let current_v2 = inner_best_output.cs[u - input.N].2;
            let mut best_pattern = 0;
            if !visited[current_v1] {
                queue.push_back(current_v1);
            }
            if !visited[current_v2] {
                queue.push_back(current_v2);
            }

            // v1とv2の入れ替え
            inner_best_output.cs[u - input.N].1 = current_v2;
            inner_best_output.cs[u - input.N].2 = current_v1;
            let score = compute_score_details(&input, &inner_best_output, &order);
            if score == inner_best_score {
                break;
            }
            if score < inner_best_score {
                inner_best_score = score;
                best_pattern = 1;
            }

            // sorterの番号を入れ替える
            if current_sorter != *sorter_i {
                inner_best_output.cs[u - input.N].0 = *sorter_i;
                inner_best_output.cs[u - input.N].1 = current_v1;
                inner_best_output.cs[u - input.N].2 = current_v2;
                let score = compute_score_details(&input, &inner_best_output, &order);
                if score < inner_best_score {
                    inner_best_score = score;
                    best_pattern = 2;
                }

                // sorterの入れ替え+v1とv2の入れ替え
                inner_best_output.cs[u - input.N].0 = *sorter_i;
                inner_best_output.cs[u - input.N].1 = current_v2;
                inner_best_output.cs[u - input.N].2 = current_v1;
                let score = compute_score_details(&input, &inner_best_output, &order);
                if score < inner_best_score {
                    inner_best_score = score;
                    best_pattern = 3;
                }
            }

            if best_pattern == 0 {
                inner_best_output.cs[u - input.N].0 = current_sorter;
                inner_best_output.cs[u - input.N].1 = current_v1;
                inner_best_output.cs[u - input.N].2 = current_v2;
            } else if best_pattern == 1 {
                inner_best_output.cs[u - input.N].0 = current_sorter;
                inner_best_output.cs[u - input.N].1 = current_v2;
                inner_best_output.cs[u - input.N].2 = current_v1;
            } else if best_pattern == 2 {
                inner_best_output.cs[u - input.N].0 = *sorter_i;
                inner_best_output.cs[u - input.N].1 = current_v1;
                inner_best_output.cs[u - input.N].2 = current_v2;
            } else if best_pattern == 3 {
                inner_best_output.cs[u - input.N].0 = *sorter_i;
                inner_best_output.cs[u - input.N].1 = current_v2;
                inner_best_output.cs[u - input.N].2 = current_v1;
            }
        }
    }
    if inner_best_score < best_score {
        best_score = inner_best_score;
        best_output = inner_best_output;
    }
    (best_score, best_output, order)
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
pub fn delaunay_edges(pts: &Vec<(i64, i64)>, mask: &Vec<bool>) -> Vec<Edge> {
    // スーパー三角形（十分大きく固定）
    let p1 = (-1_i64, -1_i64);
    let p2 = (-1_i64, 1_000_000_i64);
    let p3 = (1_000_000_i64, -1_i64);
    let p1_idx = pts.len();
    let p2_idx = pts.len() + 1;
    let p3_idx = pts.len() + 2;

    let mut pts_with_super = pts.clone();
    pts_with_super.push(p1);
    pts_with_super.push(p2);
    pts_with_super.push(p3);

    let mut triangles: Vec<(usize, usize, usize)> = vec![(p1_idx, p2_idx, p3_idx)];

    for (pi, &p) in pts.iter().enumerate() {
        if mask[pi] {
            continue; // マスクされている点は無視
        }
        let mut bad_triangles = Vec::new();
        for &(a, b, c) in &triangles {
            // 三角形の向きを i128 で判定し、CCW に合わせる
            let pa = pts_with_super[a];
            let pb = pts_with_super[b];
            let pc = pts_with_super[c];
            let cross = orient_i128(pa, pb, pc);
            let (a1, b1, c1) = if cross > 0 { (a, b, c) } else { (a, c, b) };

            if in_circumcircle_i128(
                p,
                pts_with_super[a1],
                pts_with_super[b1],
                pts_with_super[c1],
            ) {
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
            let a = pts_with_super[u];
            let b = pts_with_super[v];
            let c = pts_with_super[pi];
            // 反時計回りに揃えて追加
            let cross = orient_i128(a, b, c);
            if cross > 0 {
                triangles.push((u, v, pi));
            } else {
                triangles.push((v, u, pi));
            }
        }
    }

    let super_ids: HashSet<usize> = [p1_idx, p2_idx, p3_idx].into_iter().collect();
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

    // x座標でソート
    edges.sort_by_key(|&(u, v)| {
        let (x1, _) = pts_with_super[u];
        let (x2, _) = pts_with_super[v];
        (x1, x2)
    });

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

impl Default for Output {
    fn default() -> Self {
        Output {
            ds: Vec::new(),
            s: 0,
            cs: Vec::new(),
        }
    }
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

pub fn calc_order(input: &Input, out: &Output) -> Vec<usize> {
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

    let Some(order) = topological_sort(&g) else {
        return vec![];
    };
    order
}

pub fn compute_score_details(input: &Input, out: &Output, order: &[usize]) -> i64 {
    let n = input.N;
    let m = input.M;
    let mut probs = vec![0.0; (n + m) * n];

    // 初期化
    for i in 0..n {
        unsafe {
            *probs.get_unchecked_mut(out.s * n + i) = 1.0;
        }
    }

    for &u in order {
        if u >= n {
            let comp_idx = u - n;
            let k = out.cs[comp_idx].0;
            if k == !0 {
                continue;
            }
            let (v1, v2) = (out.cs[comp_idx].1, out.cs[comp_idx].2);

            let src_base = u * n;
            let dst1_base = v1 * n;
            let dst2_base = v2 * n;
            let ps_row = unsafe { input.ps.get_unchecked(k) };

            for i in 0..n {
                unsafe {
                    let p = *probs.get_unchecked(src_base + i);
                    let pk = *ps_row.get_unchecked(i);
                    *probs.get_unchecked_mut(dst1_base + i) += p * pk;
                    *probs.get_unchecked_mut(dst2_base + i) += p * (1.0 - pk);
                }
            }
        }
    }

    let mut score = 0.0;
    for i in 0..n {
        unsafe {
            let d = *out.ds.get_unchecked(i);
            score += 1.0 - *probs.get_unchecked(i * n + d);
        }
    }

    ((1e9 * (score / n as f64)).round()) as i64
}



pub fn topological_sort(adj: &[Vec<usize>]) -> Option<Vec<usize>> {
    let n = adj.len();
    let mut in_deg = vec![0usize; n];

    // 入次数カウント
    for edges in adj {
        for &v in edges {
            in_deg[v] += 1;
        }
    }

    // スタック方式（VecDequeより速い）
    let mut stack = Vec::with_capacity(n);
    for (u, &deg) in in_deg.iter().enumerate() {
        if deg == 0 {
            stack.push(u);
        }
    }

    let mut order = Vec::with_capacity(n);
    while let Some(u) = stack.pop() {
        order.push(u);
        for &v in &adj[u] {
            in_deg[v] -= 1;
            if in_deg[v] == 0 {
                stack.push(v);
            }
        }
    }

    if order.len() == n {
        Some(order)
    } else {
        None
    }
}
