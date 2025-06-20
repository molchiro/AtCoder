#![allow(non_snake_case, unused_macros)]

use proconio::input_interactive;
use rand::prelude::*;
use core::panic;
use std::collections::HashSet;
use std::ops::RangeBounds;
use std::time;
use core::cmp::Reverse;

const GRID_SIZE: usize = 10;

fn main() {
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
        .map(|&(lx, rx, ly, ry)| City::new(lx, rx, ly, ry))
        .collect();

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

    // exit(0);

    println!("!");
    
    // // Gの個数だけ何も考えずに先頭から取り出す
    // let mut ans: Vec<Vec<usize>> = vec![vec![]; M];
    // let mut now = 0;
    // for i in 0..M {
    //     for j in 0..G[i] {
    //         ans[i].push(now);
    //         now += 1;
    //     }
    // }

    let mut candidates: HashSet<usize> = HashSet::new();
    let mut now_grid_address = (0, 0);
    for i in 0..M {
        let mut selected: Vec<usize> = vec![];
        let mut roads: Vec<(usize, usize)> = vec![];
        let n = G[i];
        // candidatesの残り個数がnよりも少ない時、gridから取り出して追加する
        while candidates.len() < n {
            if now_grid_address.1 == GRID_SIZE {
                panic!("now_grid_address.1 == GRID_SIZE");
            }
            if now_grid_address.0 == GRID_SIZE {
                panic!("now_grid_address.0 == GRID_SIZE");
            }
            for i in grid[now_grid_address.0][now_grid_address.1].iter() {
                candidates.insert(*i);
            }
            if now_grid_address.1 % 2 == 0 {
                if now_grid_address.0 == GRID_SIZE - 1 {
                    now_grid_address.1 += 1;
                } else {
                    now_grid_address.0 += 1;
                }
            } else {
                if now_grid_address.0 == 0 {
                    now_grid_address.1 += 1;
                } else {
                    now_grid_address.0 -= 1;
                }
            }
        }
        // now_grid_address.1が偶数の時は最も左奇数の時は最も右から取り出す
        let first: usize;
        if now_grid_address.1 % 2 == 0 {
            let leftest = candidates.iter().min_by_key(|&&x| cities[x].estimated_x).unwrap();
            first = *leftest;
        } else {
            let rightest = candidates.iter().max_by_key(|&&x| cities[x].estimated_x).unwrap();
            first = *rightest;
        }
     
        // candidatesの完全グラフを構成
        let mut graph: Vec<Vec<(usize, usize)>> = vec![vec![]; N];
        for i in 0..candidates.len() {
            for j in i + 1..candidates.len() {
            let u = *candidates.iter().nth(i).unwrap();
            let v = *candidates.iter().nth(j).unwrap();
            let d = culc_dist(range[u], range[v]);
            graph[u].push((v, d as usize));
            graph[v].push((u, d as usize));
            }
        }
        // priority_queueを利用して、firstを起点に短い辺を優先的に取り出す
        let mut pq: std::collections::BinaryHeap<Reverse<(usize, usize, usize)>> = std::collections::BinaryHeap::new();
        let mut used: HashSet<usize> = HashSet::new();
        for &(v, d) in &graph[first] {
            pq.push(Reverse((d, first, v)));
        }
        // println!("{:?}", pq);
        used.insert(first);
        selected.push(first);
        while selected.len() < n {
            if let Some(Reverse((_, u, v))) = pq.pop() {
            if used.contains(&v) {
                continue;
            }
            selected.push(v);
            roads.push((u, v));
            used.insert(v);
            for &(w,d) in &graph[v] {
                if used.contains(&w) {
                continue;
                }
                pq.push(Reverse((d, v, w)));
            }
            } else {
            panic!("pq.pop() returns None");
            }
        }

        println!("{}", selected.iter().map(|&x| x.to_string()).collect::<Vec<String>>().join(" "));
        for (u, v) in roads {
            println!("{} {}", u, v);
        }

        // candidatesからselectedを削除
        for i in selected {
            candidates.remove(&i);
        }
    }
}


struct City {
    estimated_x: usize,
    estimated_y: usize,
    lx: usize,
    rx: usize,
    ly: usize,
    ry: usize,
}
impl City {
    fn new(lx: usize, rx: usize, ly: usize, ry: usize) -> Self {
        let estimated_x = (lx + rx) / 2;
        let estimated_y = (ly + ry) / 2;
        Self {
            estimated_x,
            estimated_y,
            lx,
            rx,
            ly,
            ry,
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

pub fn parse_output(_input: &Input, f: &str) -> Result<Output, String> {
    let mut queries = vec![];
    let mut outputs = vec![];
    let mut after_output = false;
    for line in f.lines() {
        let line = line.trim();
        if line.len() == 0 {
            continue;
        } else if after_output {
            outputs.push(line.to_owned());
        } else if line.starts_with('?') {
            // query
            queries.push(line.to_owned());
        } else if line.starts_with('!') {
            // output
            if line != "!" {
                return Err(format!("Illegal output format: {}", line));
            }
            after_output = true;
        } else {
            return Err(format!("Unknown line: {}", line));
        }
    }

    Ok(Output { queries, outputs })
}



pub fn compute_score(input: &Input, outs: &Vec<String>) -> (i64, String) {
    let (mut score, err, _) = compute_score_details(input, &outs);
    if err.len() > 0 {
        score = 0;
    }
    (score, err)
}

pub fn compute_score_details(
    input: &Input,
    outs: &Vec<String>,
) -> (i64, String, (Vec<Vec<usize>>, Vec<Vec<(usize, usize)>>)) {
    let dist = build_dist_matrix(input);
    //各グループについての回答をM回受け取り、バリデーションとスコアの計算を行う
    let mut city_group = vec![-1; input.N];
    let mut city_id = vec![-1; input.N];
    let mut line_ptr = 0;
    let mut score = 0 as i64;
    let mut groups = vec![];
    let mut edges = vec![];
    for g in 0..(input.M) {
        groups.push(vec![]);
        edges.push(vec![]);
        let line = &outs[line_ptr];
        line_ptr += 1;
        let mut tokens = line.split_whitespace();
        for k in 0..input.G[g] {
            let i = read(tokens.next(), 0..input.N);
            let i = match i {
                Ok(i) => i,
                Err(err) => return (0, err, (vec![], vec![])),
            };
            if city_group[i] != -1 {
                return (
                    0,
                    format!("Item {} appears multiple times.", i),
                    (vec![], vec![]),
                );
            }
            city_group[i] = g as i32;
            city_id[i] = k as i32;
            groups[g].push(i);
        }
        if tokens.next().is_some() {
            return (
                0,
                format!("Illegal output format: {}", line),
                (vec![], vec![]),
            );
        }

        let mut dsu = Dsu::new(input.G[g]);
        for _ in 0..(input.G[g] - 1) {
            let line = &outs[line_ptr];
            line_ptr += 1;
            let mut tokens = line.split_whitespace();
            let i = read(tokens.next(), 0..input.N);
            let i = match i {
                Ok(i) => i,
                Err(err) => return (0, err, (vec![], vec![])),
            };
            let j = read(tokens.next(), 0..input.N);
            let j = match j {
                Ok(j) => j,
                Err(err) => return (0, err, (vec![], vec![])),
            };
            if tokens.next().is_some() {
                return (
                    0,
                    format!("Illegal output format: {}", line),
                    (vec![], vec![]),
                );
            }
            if city_group[i] != g as i32 || city_group[j] != g as i32 {
                return (0, format!("Invalid edge: {} {}", i, j), (vec![], vec![]));
            }
            let id_i = city_id[i] as usize;
            let id_j = city_id[j] as usize;
            if dsu.same(id_i, id_j) {
                return (0, format!("Invalid edge: {} {}", i, j), (vec![], vec![]));
            }
            dsu.merge(id_i, id_j);
            score += dist[i][j] as i64;
            edges[g].push((i, j));
        }
    }
    if line_ptr != outs.len() {
        return (0, "Too many outputs".to_owned(), (vec![], vec![]));
    }
    (score, "".to_owned(), (groups, edges))
}

pub fn culc_dist(u: (usize, usize, usize, usize), v: (usize, usize, usize, usize)) -> f64 {
    let ux = (u.0+u.1)/2;
    let uy = (u.2+u.3)/2;
    let vx = (v.0+v.1)/2;
    let vy = (v.2+v.3)/2;
    let dx = (ux as i64 - vx as i64).abs();

    let dy = (uy as i64 - vy as i64).abs();
    let d = (dx.pow(2) + dy.pow(2)) as f64;
    return d;
}

pub fn build_dist_matrix(input: &Input) -> Vec<Vec<usize>> {
    let mut dist = vec![vec![0; input.N]; input.N];
    for i in 0..input.N {
        for j in 0..input.N {
            let mut d = culc_dist(input.range[i], input.range[j]);
            d = d.sqrt();
            //切り捨てて整数とする
            d = d.floor();
            dist[i][j] = d as usize;
        }
    }
    dist
}

