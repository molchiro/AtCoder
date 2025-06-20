#![allow(non_snake_case, unused_macros)]

use core::cmp::Reverse;
use core::panic;
use itertools::Itertools;
use proconio::input_interactive;
use rand::seq::SliceRandom;
use rand::Rng;
use std::collections::{HashSet, VecDeque};
use std::time;

const GRID_SIZE: usize = 6;

fn main() {
    let mut rng: rand::rngs::StdRng = rand::SeedableRng::from_seed([123 as u8; 32]);
    let start_time = time::Instant::now();
    input_interactive! {
        N: usize, M: usize, Q: usize, L: usize, W: usize,
        G: [usize; M],
        range: [(usize, usize, usize, usize); N],
    }
    // println!("# here");

    let input = Input {
        N,
        M,
        Q,
        L,
        W,
        G: G.clone(),
        range: range.clone(),
    };
    let cities: Vec<City> = input
        .range
        .iter()
        .enumerate()
        .map(|(i, &(lx, rx, ly, ry))| City::new(i, lx, rx, ly, ry))
        .collect();

    let mut last_query = 0;
    for n in G.iter() {
        if n < &3 {
            continue;
        }
        last_query += n / (L-1);
        if n % (L-1) >= 3 {
            last_query += 1;
        }
    }

    let x_max = cities.iter().map(|c| c.rx).max().unwrap();
    let y_max = cities.iter().map(|c| c.ry).max().unwrap();

    // rangeの中心座標に基づき、G×Gのグリッドに分割する
    let mut grid: Vec<Vec<Vec<City>>> = vec![vec![vec![]; GRID_SIZE]; GRID_SIZE];
    for i in 0..N {
        let u = cities[i].clone();
        let gx = (u.estimated_x * GRID_SIZE) / x_max;
        let gy = (u.estimated_y * GRID_SIZE) / y_max;
        // println!("{} {} {} {}", cities[i].estimated_x, cities[i].estimated_y, gx, gy);
        grid[gx][gy].push(u);
    }

    let mut q_count = last_query + 1;

    // 3つの位置関係からrangeを修正する
    for u_id in cities.iter().sorted_by(|a, b| a.s.cmp(&b.s)).rev().map(|city| city.id) {
        let mut a = cities[u_id].clone();
        let gx_u = (&a.estimated_x * GRID_SIZE) / x_max;
        let gy_u = (&a.estimated_y * GRID_SIZE) / y_max;
        let c: City;
        if gx_u < GRID_SIZE / 2 {
            c = grid[GRID_SIZE - 1][gy_u][0].clone();
        } else {
            c = grid[0][gy_u][0].clone();
        }

        let d: City;
        if gy_u < GRID_SIZE / 2 {
            d = grid[gx_u][GRID_SIZE - 1][0].clone();
        } else {
            d = grid[gx_u][0][0].clone();
        }

        for v_id in grid[gx_u][gy_u].iter().sorted_by(|a, b| a.s.cmp(&b.s)).map(|c| c.id) {
            if q_count >= Q {
                continue;
            }

            if u_id == v_id {
                continue;
            }
            let b = cities[v_id].clone();
            if b.is_inside_of(&a) {

                q_count += 2;

                println!("? 3 {} {} {}", a.id, b.id, c.id);
                input_interactive! {
                    roads: [(usize, usize); 2],
                }
                if (roads.iter().filter(|&(u, v)| *u == a.id || *v == a.id).count() == 2)
                    ^ (gx_u < GRID_SIZE / 2)
                {
                    a.update(a.lx, b.estimated_x, a.ly, a.ry);
                } else {
                    a.update(b.estimated_x, a.rx, a.ly, a.ry);
                }

                println!("? 3 {} {} {}", a.id, b.id, d.id);
                input_interactive! {
                    roads: [(usize, usize); 2],
                }
                if (roads.iter().filter(|&(u, v)| *u == a.id || *v == a.id).count() == 2)
                    ^ (gy_u < GRID_SIZE / 2)
                {
                    a.update(a.lx, a.rx, a.ly, b.estimated_y);
                } else {
                    a.update(a.lx, a.rx, b.estimated_y, a.ry);
                }
                break;
            }
        }
        // gridから古いaを削除
        grid[gx_u][gy_u].retain(|x| x.id != a.id);
        // gridに更新後のaを追加
        let gx_j = (a.estimated_x * GRID_SIZE) / x_max;
        let gy_j = (a.estimated_y * GRID_SIZE) / y_max;
        grid[gx_j][gy_j].push(a.clone());
    }

    let mut best_score = f64::MAX;
    let mut best_districts: Vec<District> = vec![];
    while start_time.elapsed().as_millis() < 1800 {
        let districts = solve_rnd(&grid, &G, M, &mut rng);
        let mut score = 0.0;
        for i in 0..M {
            score += districts[i].size;
        }
        if score < best_score {
            best_score = score;
            best_districts = districts.clone();
        }
    }

    for i in 0..M {
        let mut district = best_districts[i].clone();
        if 3 <= district.len() && district.len() <= L {
            println!(
                "? {} {}",
                district.len(),
                district
                    .cities
                    .iter()
                    .map(|city| city.id.to_string())
                    .collect::<Vec<String>>()
                    .join(" ")
            );
            input_interactive! {
                roads_raw: [(usize, usize); district.len() - 1],
            }
            let mut roads: Vec<(City, City)> = vec![];
            for (u, v) in roads_raw.iter() {
                roads.push((cities[*u].clone(), cities[*v].clone()));
            }

            district.replace_roads(roads);
            best_districts[i] = district.clone();
        } else if district.len() > L {
            // グラフの構築
            let root = district.roads[0].0.clone().id;
            let mut parent: Vec<usize> = vec![usize::MAX; N];
            let mut children: Vec<Vec<usize>> = vec![vec![]; N];
            for (u, v) in district.roads.clone() {
                children[u.id].push(v.id);
                parent[v.id] = u.id;
            }

            
            // 最大クエリ回数を決定
            let n = G[i];
            let mut q = 0;
            q += n / (L-1);
            if n % (L-1) >= 3 {
                q += 1;
            }
            let 
            mut finished: HashSet<usize> = HashSet::new();
            let mut new_roads: Vec<(City, City)> = vec![];
            let mut dsu = Dsu::new(N);
            let mut outer_dq: VecDeque<usize> = VecDeque::new();
            let mut outer_selected: HashSet<usize> = HashSet::new();
            let mut queries: HashSet<Vec<usize>> = HashSet::new();
            // let mut queried: HashSet<usize> = HashSet::new();
            // rootを始点にしてBFSしながらクエリしてdistrictを再構築する
            outer_dq.push_back(root);
            while q > 0 && outer_dq.len() > 0 {
                let u = outer_dq.pop_front().unwrap();
                if finished.contains(&u) {
                    continue;
                }
                // uを基準に子、親の順で幅優先探索し、クエリに含めるcityを選ぶ
                let mut inner_dq: VecDeque<usize> = VecDeque::new();
                let mut inner_selected: HashSet<usize> = HashSet::new();
                inner_dq.push_back(u);
                'inner_loop: while inner_dq.len() > 0 && inner_selected.len() < L {
                    let v = inner_dq.pop_front().unwrap();
                    if finished.contains(&v) {
                        continue;
                    }
                    if inner_selected.contains(&v) {
                        continue;
                    }
                    inner_selected.insert(v);
                    outer_selected.insert(v);
                    let mut f = true;
                    for &child in children[v].iter() {
                        if !inner_selected.contains(&child) {
                            inner_dq.push_back(child);
                            if !outer_selected.contains(&child) {
                                outer_dq.push_back(child);
                                f = false;
                            }
                        }
                        if inner_selected.len() >= L {
                            break 'inner_loop;
                        }
                    }
                    let p = parent[v];
                    if !p.eq(&usize::MAX) {
                        if !inner_selected.contains(&p) {
                            inner_dq.push_back(p);
                            // f = false;
                        }
                        if inner_selected.len() >= L {
                            break 'inner_loop;
                        }
                    }
                    if f {
                        finished.insert(v);
                    }
                }
                if inner_selected.len() < 3 {
                    continue;
                }
                // inner_selectedに含まれるcityクエリしdsuを更新する
                let inner_selected_vec: Vec<usize> = inner_selected.iter().map(|&x| x).sorted().collect();
                if queries.contains(&inner_selected_vec.clone()) {
                    continue;
                }
                println!(
                    "? {} {}",
                    inner_selected.len(),
                    inner_selected
                        .iter()
                        .map(|&city| city.to_string())
                        .collect::<Vec<String>>()
                        .join(" ")
                );
                input_interactive! {
                    roads_raw: [(usize, usize); inner_selected.len() - 1],
                }
                for (i, j) in roads_raw.iter() {
                    if dsu.same(*i, *j) {
                        continue;
                    }
                    new_roads.push((cities[*i].clone(), cities[*j].clone()));
                    dsu.merge(*i, *j);
                }
                q -= 1;
                queries.insert(inner_selected_vec);
                // queried.extend(inner_selected.iter());
            }
            // 構築漏れの点を連結させる
            // let not_queried: Vec<City> = district
            //     .cities
            //     .iter()
            //     .filter(|&city| !queried.contains(&city.id))
            //     .map(|city| city.clone())
            //     .collect();
            // if not_queried.len() > 0 {
                let mut edges: Vec<(f64, usize, usize)> = vec![];
                // for u in not_queried.iter() {
                for u in district.cities.iter() {
                    for v in district.cities.iter() {
                        if u.id == v.id {
                            continue;
                        }
                        let d = culc_dist(u, v);
                        edges.push((d, u.id, v.id));
                    }
                }
                edges.sort_by(|a, b| a.partial_cmp(b).unwrap());
                for &(_, u, v) in edges.iter() {
                    if dsu.same(u, v) {
                        continue;
                    }
                    new_roads.push((cities[u].clone(), cities[v].clone()));
                    dsu.merge(u, v);
                }
            // }
            // 再構築したroadでdistrictを更新する
            district.replace_roads(new_roads.clone());
            best_districts[i] = district.clone();
        }

    }
    println!("!");
    for i in 0..M {
        best_districts[i].echo();
    }
}

fn build_roads(n: usize, candidates: HashSet<City>, rot: usize) -> District {
    let mut candidates: Vec<City> = candidates.into_iter().collect();
    if rot == 0 {
        // 左上
        candidates.sort_by_key(|city| city.estimated_x + city.estimated_y);
    } else if rot == 1 {
        // 左 
        candidates.sort_by_key(|city| city.estimated_x);
    } else if rot == 2 {
        // 上
        candidates.sort_by_key(|city| city.estimated_y);
    } else if rot == 3 {
        // 左下
        candidates.sort_by_key(|city| city.estimated_x + 10000 - city.estimated_y);
    } else if rot == 4 {
        // 右上
        candidates.sort_by_key(|city| 10000 - city.estimated_x + city.estimated_y);
    } else if rot == 5 {
        // 右
        candidates.sort_by_key(|city| 10000 - city.estimated_x);
    } else if rot == 6 {
        // 下
        candidates.sort_by_key(|city| 10000 - city.estimated_y);
    } else if rot == 7 {
        // 右下
        candidates.sort_by_key(|city| 10000 - city.estimated_x + 10000 - city.estimated_y);
    } else {
        panic!("rot is out of range");
    }

    // candidatesの完全グラフを構成
    let mut graph: Vec<Vec<(usize, usize)>> = vec![vec![]; candidates.len()];
    for i in 0..candidates.len() {
        for j in i + 1..candidates.len() {
            let u = &candidates[i];
            let v = &candidates[j];
            let d = culc_dist(u, v);
            graph[i].push((j, d as usize));
            graph[j].push((i, d as usize));
        }
    }
    // priority_queueを利用して、firstを起点に短い辺を優先的に取り出す
    let mut pq: std::collections::BinaryHeap<Reverse<(usize, usize, usize)>> =
        std::collections::BinaryHeap::new();
    for &(v, d) in &graph[0] {
        pq.push(Reverse((d, 0, v)));
    }
    // println!("{:?}", pq);
    let mut district = District::new();
    district.add_city(candidates[0].clone());
    while district.cities.len() < n {
        if let Some(Reverse((_, u, v))) = pq.pop() {
            if district.contains(&candidates[v]) {
                continue;
            }
            district.add_city(candidates[v].clone());
            district.add_road((candidates[u].clone(), candidates[v].clone()));
            for &(w, d) in &graph[v] {
                if district.contains(&candidates[w]) {
                    continue;
                }
                pq.push(Reverse((d, v, w)));
            }
        } else {
            panic!("pq.pop() returns None");
        }
    }
    return district;
}

use std::hash::{Hash, Hasher};

#[derive(Eq, Clone)]
struct City {
    id: usize,
    estimated_x: usize,
    estimated_y: usize,
    lx: usize,
    rx: usize,
    ly: usize,
    ry: usize,
    s: usize,
}

impl PartialEq for City {
    fn eq(&self, other: &Self) -> bool {
        self.id == other.id
    }
}

impl Hash for City {
    fn hash<H: Hasher>(&self, state: &mut H) {
        self.id.hash(state);
    }
}
impl City {
    fn new(i: usize, lx: usize, rx: usize, ly: usize, ry: usize) -> Self {
        let estimated_x = (lx + rx) / 2;
        let estimated_y = (ly + ry) / 2;
        let s = (rx - lx) * (ry - ly);
        Self {
            id: i,
            estimated_x,
            estimated_y,
            lx,
            rx,
            ly,
            ry,
            s
        }
    }

    fn is_inside_of(&self, other_city: &City) -> bool {
        other_city.lx <= self.lx
            && self.rx <= other_city.rx
            && other_city.ly <= self.ly
            && self.ry <= other_city.ry
    }

    fn update(&mut self, lx: usize, rx: usize, ly: usize, ry: usize) {
        self.lx = lx;
        self.rx = rx;
        self.ly = ly;
        self.ry = ry;
        self.estimated_x = (lx + rx) / 2;
        self.estimated_y = (ly + ry) / 2;
        self.s = (rx - lx) * (ry - ly);
    }
}

#[derive(Clone)]
struct District {
    cities: HashSet<City>,
    roads: Vec<(City, City)>,
    size: f64,
}

impl District {
    fn new() -> Self {
        let cities = HashSet::new();
        let roads = vec![];
        let size = 0.0;
        Self {
            cities,
            roads,
            size,
        }
    }

    fn add_city(&mut self, city: City) {
        self.cities.insert(city);
    }

    fn add_road(&mut self, road: (City, City)) {
        self.size += culc_dist(&road.0, &road.1);
        self.roads.push(road);
    }

    fn replace_roads(&mut self, roads: Vec<(City, City)>) {
        self.size = 0.0;
        for (u, v) in roads.iter() {
            self.size += culc_dist(u, v);
        }
        self.roads = roads;
    }

    fn contains(&self, city: &City) -> bool {
        self.cities.contains(city)
    }

    fn len(&self) -> usize {
        self.cities.len()
    }

    fn echo(&self) {
        println!(
            "{}",
            self.cities
                .iter()
                .map(|city| city.id.to_string())
                .collect::<Vec<String>>()
                .join(" ")
        );
        for road in self.roads.iter() {
            println!("{} {}", road.0.id, road.1.id);
        }
    }
}

// https://github.com/rust-lang-ja/ac-library-rs/blob/master/src/dsu.rs

/// A Disjoint set union (DSU) with union by size and path compression.
///
/// See: [Zvi Galil and Giuseppe F. Italiano, Data structures and algorithms for disjoint set union problems](https://core.ac.uk/download/pdf/161439519.pdf)
///
/// In the following documentation, let $n$ be the size of the DSU.
///
/// # Example
///
/// ```
/// use ac_library::Dsu;
/// use proconio::{input, source::once::OnceSource};
///
/// input! {
///     from OnceSource::from(
///         "5\n\
///          3\n\
///          0 1\n\
///          2 3\n\
///          3 4\n",
///     ),
///     n: usize,
///     abs: [(usize, usize)],
/// }
///
/// let mut dsu = Dsu::new(n);
/// for (a, b) in abs {
///     dsu.merge(a, b);
/// }
///
/// assert!(dsu.same(0, 1));
/// assert!(!dsu.same(1, 2));
/// assert!(dsu.same(2, 4));
///
/// assert_eq!(
///     dsu.groups()
///         .into_iter()
///         .map(|mut group| {
///             group.sort_unstable();
///             group
///         })
///         .collect::<Vec<_>>(),
///     [&[0, 1][..], &[2, 3, 4][..]],
/// );
/// ```
pub struct Dsu {
    n: usize,
    // root node: -1 * component size
    // otherwise: parent
    parent_or_size: Vec<i32>,
}

impl Dsu {
    /// Creates a new `Dsu`.
    ///
    /// # Constraints
    ///
    /// - $0 \leq n \leq 10^8$
    ///
    /// # Complexity
    ///
    /// - $O(n)$
    pub fn new(size: usize) -> Self {
        Self {
            n: size,
            parent_or_size: vec![-1; size],
        }
    }

    // `\textsc` does not work in KaTeX
    /// Performs the Uɴɪᴏɴ operation.
    ///
    /// # Constraints
    ///
    /// - $0 \leq a < n$
    /// - $0 \leq b < n$
    ///
    /// # Panics
    ///
    /// Panics if the above constraints are not satisfied.
    ///
    /// # Complexity
    ///
    /// - $O(\alpha(n))$ amortized
    pub fn merge(&mut self, a: usize, b: usize) -> usize {
        assert!(a < self.n);
        assert!(b < self.n);
        let (mut x, mut y) = (self.leader(a), self.leader(b));
        if x == y {
            return x;
        }
        if -self.parent_or_size[x] < -self.parent_or_size[y] {
            std::mem::swap(&mut x, &mut y);
        }
        self.parent_or_size[x] += self.parent_or_size[y];
        self.parent_or_size[y] = x as i32;
        x
    }

    /// Returns whether the vertices $a$ and $b$ are in the same connected component.
    ///
    /// # Constraints
    ///
    /// - $0 \leq a < n$
    /// - $0 \leq b < n$
    ///
    /// # Panics
    ///
    /// Panics if the above constraint is not satisfied.
    ///
    /// # Complexity
    ///
    /// - $O(\alpha(n))$ amortized
    pub fn same(&mut self, a: usize, b: usize) -> bool {
        assert!(a < self.n);
        assert!(b < self.n);
        self.leader(a) == self.leader(b)
    }

    /// Performs the Fɪɴᴅ operation.
    ///
    /// # Constraints
    ///
    /// - $0 \leq a < n$
    ///
    /// # Panics
    ///
    /// Panics if the above constraint is not satisfied.
    ///
    /// # Complexity
    ///
    /// - $O(\alpha(n))$ amortized
    pub fn leader(&mut self, a: usize) -> usize {
        assert!(a < self.n);
        if self.parent_or_size[a] < 0 {
            return a;
        }
        self.parent_or_size[a] = self.leader(self.parent_or_size[a] as usize) as i32;
        self.parent_or_size[a] as usize
    }

    /// Returns the size of the connected component that contains the vertex $a$.
    ///
    /// # Constraints
    ///
    /// - $0 \leq a < n$
    ///
    /// # Panics
    ///
    /// Panics if the above constraint is not satisfied.
    ///
    /// # Complexity
    ///
    /// - $O(\alpha(n))$ amortized
    pub fn size(&mut self, a: usize) -> usize {
        assert!(a < self.n);
        let x = self.leader(a);
        -self.parent_or_size[x] as usize
    }

    /// Divides the graph into connected components.
    ///
    /// The result may not be ordered.
    ///
    /// # Complexity
    ///
    /// - $O(n)$
    pub fn groups(&mut self) -> Vec<Vec<usize>> {
        let mut leader_buf = vec![0; self.n];
        let mut group_size = vec![0; self.n];
        for i in 0..self.n {
            leader_buf[i] = self.leader(i);
            group_size[leader_buf[i]] += 1;
        }
        let mut result = vec![Vec::new(); self.n];
        for i in 0..self.n {
            result[i].reserve(group_size[i]);
        }
        for i in 0..self.n {
            result[leader_buf[i]].push(i);
        }
        result
            .into_iter()
            .filter(|x| !x.is_empty())
            .collect::<Vec<Vec<usize>>>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn dsu_works() {
        let mut d = Dsu::new(4);
        d.merge(0, 1);
        assert!(d.same(0, 1));
        d.merge(1, 2);
        assert!(d.same(0, 2));
        assert_eq!(d.size(0), 3);
        assert!(!d.same(0, 3));
        assert_eq!(d.groups(), vec![vec![0, 1, 2], vec![3]]);
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
    pub Q: usize,
    pub L: usize,
    pub W: usize,
    pub G: Vec<usize>,
    pub range: Vec<(usize, usize, usize, usize)>,
}

fn culc_dist(u: &City, v: &City) -> f64 {
    let dx = (u.estimated_x as i64 - v.estimated_x as i64).abs();
    let dy = (u.estimated_y as i64 - v.estimated_y as i64).abs();

    let d = (dx.pow(2) + dy.pow(2)) as f64;
    return d;
}

fn solve_rnd(
    grid: &Vec<Vec<Vec<City>>>,
    G: &Vec<usize>,
    M: usize,
    rng: &mut rand::rngs::StdRng,
) -> Vec<District> {
    let mut shuffled_G: Vec<(usize, &usize)> = G.iter().enumerate().collect();
    shuffled_G.shuffle(rng);
    let mut districts: Vec<District> = vec![District::new(); M];
    let mut candidates: HashSet<City> = HashSet::new();
    let mut now_grid = 0;
    // let rng_range: usize;
    // if M < 3 {
    //     rng_range = 8;
    // } else if M < 4 {
    //     rng_range = 7;
    // } else if M < 5 {
    //     rng_range = 6;
    // } else if M < 8 {
    //     rng_range = 5;
    // } else if M < 10 {
    //     rng_range = 4;
    // } else if M < 12 {
    //     rng_range = 3;
    // } else if M < 15 {
    //     rng_range = 2;
    // } else {
    //     rng_range = 1;
    // }
    for i in 0..M {
        let (idx, n) = shuffled_G[i];
        // candidatesの残り個数がnよりも少ない時、gridから取り出して追加する
        // ある程度余裕を持って取り出す
        while candidates.len() < n + rng.gen_range(75..150) && now_grid < GRID_SIZE * 2 {
            for x in 0..now_grid * 2 + 1 {
                if x < GRID_SIZE && now_grid - x < GRID_SIZE {
                    let now_grid_address: (usize, usize) = (x, now_grid - x);
                    for city in grid[now_grid_address.0][now_grid_address.1].iter() {
                        candidates.insert(city.clone());
                    }
                }
            }

            now_grid += 1;
        }

        let district = build_roads(*n, candidates.clone(), 0);
        districts[idx] = district.clone();

        // candidatesからselectedを削除
        for i in district.clone().cities.iter() {
            candidates.remove(&i);
        }
    }
    districts
}
