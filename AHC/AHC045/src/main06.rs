#![allow(non_snake_case, unused_macros)]

use core::panic;
use std::collections::HashMap;
use itertools::Itertools;
use proconio::input_interactive;
use std::ops::RangeBounds;
use std::{clone, collections::HashSet};
// use std::time;
use core::cmp::Reverse;

const GRID_SIZE: usize = 4;

fn main() {
    // let start_time = time::Instant::now();
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
    let mut cities: Vec<City> = input
        .range
        .iter()
        .enumerate()
        .map(|(i, &(lx, rx, ly, ry))| City::new(i, lx, rx, ly, ry))
        .collect();

    let last_query = G.iter().filter(|&n| 3 <= *n && *n <= L).count();

    let x_max = cities.iter().map(|c| c.rx).max().unwrap();
    let y_max = cities.iter().map(|c| c.ry).max().unwrap();

    // rangeの中心座標に基づき、G×Gのグリッドに分割する
    let mut grid: Vec<Vec<Vec<usize>>> = vec![vec![vec![]; GRID_SIZE]; GRID_SIZE];
    for i in 0..N {
        let gx = (cities[i].estimated_x * GRID_SIZE) / x_max;
        let gy = (cities[i].estimated_y * GRID_SIZE) / y_max;
        // println!("{} {} {} {}", cities[i].estimated_x, cities[i].estimated_y, gx, gy);
        grid[gx][gy].push(i);
    }

    let mut q_count = last_query+1;

    // 3つの位置関係からrangeを修正する
    for i in 0..N {
        let a = cities[i].clone();
        let gx = (cities[i].estimated_x * GRID_SIZE) / x_max;
        let gy = (cities[i].estimated_y * GRID_SIZE) / y_max;
        let c: City;
        if gx < GRID_SIZE / 2 {
            c = cities[grid[GRID_SIZE - 1][gy][0]].clone();
        } else {
            c = cities[grid[0][gy][0]].clone();
        }

        let d: City;
        if gy < GRID_SIZE / 2 {
            d = cities[grid[gx][GRID_SIZE - 1][0]].clone();
        } else {
            d = cities[grid[gx][0][0]].clone();
        }

        for j in i..N {
            if q_count >= Q {
                continue;
            }

            if i == j {
                continue;
            }
            let b = cities[j].clone();
            if a.is_inside_of(&b) {
                q_count += 2;

                println!("? 3 {} {} {}", i, j, c.id);
                input_interactive! {
                    roads: [(usize, usize); 2],
                }
                if (roads.iter().filter(|&(u, v)| *u == j || *v == j).count() == 2)
                    ^ (gx < GRID_SIZE / 2)
                {
                    cities[j].update(b.lx, a.rx, b.ly, b.ry);
                } else {
                    cities[j].update(a.lx, b.rx, b.ly, b.ry);
                }

                println!("? 3 {} {} {}", i, j, d.id);
                input_interactive! {
                    roads: [(usize, usize); 2],
                }
                if (roads.iter().filter(|&(u, v)| *u == j || *v == j).count() == 2)
                    ^ (gy < GRID_SIZE / 2)
                {
                    cities[j].update(b.lx, b.rx, b.ly, a.ry);
                } else {
                    cities[j].update(b.lx, b.rx, a.ly, b.ry);
                }
                // a = cities[j].clone();
            }
        }
    }

    // グリッド分けをやり直す
    let x_max = cities.iter().map(|c| c.rx).max().unwrap();
    let y_max = cities.iter().map(|c| c.ry).max().unwrap();

    // rangeの中心座標に基づき、G×Gのグリッドに分割する
    let mut grid: Vec<Vec<Vec<usize>>> = vec![vec![vec![]; GRID_SIZE]; GRID_SIZE];
    for i in 0..N {
        let gx = (cities[i].estimated_x * GRID_SIZE) / x_max;
        let gy = (cities[i].estimated_y * GRID_SIZE) / y_max;
        // println!("{} {} {} {}", cities[i].estimated_x, cities[i].estimated_y, gx, gy);
        grid[gx][gy].push(i);
    }

    let mut districts: Vec<District> = vec![District::new(); M];
    let mut candidates: HashSet<City> = HashSet::new();
    let mut now_grid = 0;
    for i in 0..M {
        let n = G[i];
        // candidatesの残り個数がnよりも少ない時、gridから取り出して追加する
        // ある程度余裕を持って取り出す
        while candidates.len() < n + 150  && now_grid < GRID_SIZE*2 {
            for x in 0..now_grid*2 + 1 {
                if x < GRID_SIZE && now_grid - x < GRID_SIZE {
                    let now_grid_address = (x, now_grid - x);
                    for i in grid[now_grid_address.0][now_grid_address.1].iter() {
                        candidates.insert(cities[*i].clone());
                    }
                }
            }

            now_grid += 1;
        }

        let district = build_roads_pq(n, candidates.clone());
        districts[i] = district.clone();

        // candidatesからselectedを削除
        for i in district.clone().cities.iter() {
            candidates.remove(&i);
        }
    }

    for i in 0..M {
        let mut district = districts[i].clone();
        if 3 <= district.len() && district.len() <= L {
            println!(
                "? {} {}",
                district.len(),
                district.cities
                    .iter()
                    .map(|city| city.id.to_string())
                    .collect::<Vec<String>>()
                    .join(" ")
            );
            input_interactive! {
                roads: [(usize, usize); district.len() - 1],
            }
            district.replace_roads(roads);
            districts[i] = district.clone();
        }
    }

    println!("!");
    for i in 0..M {
        districts[i].echo();
    }
}

fn build_roads_pq(n: usize, candidates: HashSet<City>) -> District {
    let mut candidates: Vec<City> = candidates.into_iter().collect();
    candidates.sort_by_key(|city| city.estimated_x + city.estimated_y);

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
            district.add_road((candidates[u].id, candidates[v].id));
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
    return  district;
    
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
        Self {
            id: i,
            estimated_x,
            estimated_y,
            lx,
            rx,
            ly,
            ry,
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
    }
}

#[derive(Clone)]
struct District {
    cities: HashSet<City>,
    roads: Vec<(usize, usize)>,
}

impl District {
    fn new() -> Self {
        let cities = HashSet::new();
        let roads = vec![];
        Self {
            cities,
            roads
        }
    }

    fn add_city(&mut self, city: City) {
        self.cities.insert(city);
    }

    fn add_road(&mut self, road: (usize, usize)) {
        self.roads.push(road);
    }

    fn replace_roads(&mut self, roads: Vec<(usize, usize)>) {
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
            println!("{} {}", road.0, road.1);
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

impl std::fmt::Display for Input {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        writeln!(f, "{} {} {} {} {}", self.N, self.M, self.Q, self.L, self.W)?;
        for i in 0..self.M {
            write!(f, "{}", self.G[i])?;
            if i < self.M - 1 {
                write!(f, " ")?;
            } else {
                writeln!(f)?;
            }
        }
        for i in 0..self.N {
            writeln!(
                f,
                "{} {} {} {}",
                self.range[i].0, self.range[i].1, self.range[i].2, self.range[i].3
            )?;
        }
        Ok(())
    }
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
    pub queries: Vec<String>,
    pub outputs: Vec<String>,
}

fn culc_dist(u: &City, v: &City) -> f64 {
    let dx = (u.estimated_x as i64 - v.estimated_x as i64).abs();
    let dy = (u.estimated_y as i64 - v.estimated_y as i64).abs();

    let d = (dx.pow(2) + dy.pow(2)) as f64;
    return d;
}
