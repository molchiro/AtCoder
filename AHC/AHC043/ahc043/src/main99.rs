use im_rc::HashSet;
use proconio;
use std::time;
use std::fmt;
use std::collections::VecDeque;

const T: usize = 800;
const STATION_COST: i64 = 5000;
const RAIL_COST: i64 = 100;


fn main() {



    let start_time = time::Instant::now();




    proconio::input! {
        n: usize, m: usize, k: i64, t: usize,
        srcdst: [(usize, usize, usize, usize); m]
    }
    let src: Vec<(usize, usize)> = srcdst.iter().map(|&(a, b, _, _)| (a, b)).collect();
    let dst: Vec<(usize, usize)> = srcdst.iter().map(|&(_, _, c, d)| (c, d)).collect();
    
    let input = Input {
        n,
        m,
        k,
        t,
        src,
        dst
    };
    let mut initial_state = State::new(&input);
    
    // 最初に建てる駅を決める
    let srcdst_to_dicide_first_station: Vec<(usize, usize, usize, usize)> = srcdst.iter()
        .filter(|&(a, b, c, d)| {
            let cost = ((*a as i64 - *c as i64).abs() + (*b as i64 - *d as i64).abs()) * RAIL_COST + STATION_COST*2;
            cost <= k
        })
        .cloned()
        .collect();
    let src_to_dicide_first_station: Vec<(usize, usize)> = srcdst_to_dicide_first_station.iter().map(|&(a, b, _, _)| (a, b)).collect();
    let dst_to_dicide_first_station: Vec<(usize, usize)> = srcdst_to_dicide_first_station.iter().map(|&(_, _, c, d)| (c, d)).collect();
    // 建てられる駅の組み合わせが１つもない場合は終了
    if src_to_dicide_first_station.len() == 0 {
        initial_state.operations.print();
        return;
    }
    let input_to_dicide_first_station = Input {
        n,
        m: src_to_dicide_first_station.len(),
        k,
        t: 0,
        src: src_to_dicide_first_station,
        dst: dst_to_dicide_first_station
    };
    let state_to_dicide_first_station = State::new(&input_to_dicide_first_station);
    let mut candidates = state_to_dicide_first_station.get_candidates();
    candidates.sort_by_key(|&(_, _, current, future, is_rail)| (current, is_rail, future));
    let (r_f, c_f, _, _, _) = candidates.pop().unwrap();
    
    initial_state.action((r_f, c_f));
    let init_res = solve(&initial_state.clone());


    let mut max_final_money = 0;
    let mut best_state = init_res.clone();

    let mut ct = 1;
    let mut i = 1;

    while start_time.elapsed().as_millis() < 2850 {
        println!("# ct: {}", ct);

        let mut actions = best_state.actions.clone();
        
        if i+1 >= actions.len() {
            break;
        }
        
        // iとi+1を入れ替えて、i以降を再計算
        actions.swap(i, i+1);
        let mut new_state = initial_state.clone();
        for j in i..actions.len() {
            new_state.action(actions[j]);
        } 

        // 改善するなら更新
        if new_state.final_money > max_final_money {
            max_final_money = new_state.final_money;
            best_state = new_state.clone();

            // i番目のアクションを行なったのちにソルバで解かせた時に改善するか確認
            new_state = solve(& initial_state);
            if new_state.final_money > max_final_money {
                max_final_money = new_state.final_money;
                best_state = new_state.clone();
            } else {
                initial_state.action(actions[i]);
                i += 1;
            }

        } else {
            initial_state.action(actions[i]);
            i += 1;
        }

        ct += 1;
    }



    best_state.operations.print();

    // println!("{}", state.money)

}

fn solve(state: &State) -> State {
    let mut state = state.clone();
    let mut max_final_money = 0;
    let mut best_state = state.clone();
        
    while state.operations.len() < 800 {
        let mut candidates = state.get_candidates();
        candidates.sort_by_key(|&(_, _, current, future, is_rail)| (current, is_rail, future));

        // 駅を建てる意味のある場所がもう無ければ終了
        match candidates.last() {
            Some((_, _, current, future, _)) => {
                if current + future <= 0 {
                    break;
                }
            },
            None => {
                break;
            }
        }

    
        while let Some((r, c, _, _, _)) = candidates.pop() {
            let res = state.action((r, c));
            if res {
                break;
            }
        }
        // println!("{}", state.income);
        if state.final_money > max_final_money {
            max_final_money = state.final_money;
            best_state = state.clone();
        }
    }
    best_state
}

#[derive(Clone)]
pub struct Input {
    n: usize,
    m: usize,
    k: i64,
    t: usize,
    src: Vec<(usize, usize)>,
    dst: Vec<(usize, usize)>,
}

impl Input {
    pub fn new() -> Self {
        Input {
            n: 0,
            m: 0,
            k: 0,
            t: 0,
            src: vec![],
            dst: vec![],
        }
    }
}


#[derive(PartialEq, Eq, Clone, Copy, Debug)]
pub enum Kind {
    Left,
    Right,
    Up,
    Down,
}

fn culc_kind_v(s: &(i64, i64), t: &(i64, i64), u: &(i64, i64)) -> Vec<Kind> {
    let mut res = Vec::new();
    if (t.0, t.1 - 1) == *s || (t.0, t.1 - 1) == *u {
        res.push(Kind::Left);
    }

    if (t.0, t.1 + 1) == *s || (t.0, t.1 + 1) == *u {
        res.push(Kind::Right);
    }

    if (t.0 - 1, t.1) == *s || (t.0 - 1, t.1) == *u {
        res.push(Kind::Up);
    }

    if (t.0 + 1, t.1) == *s || (t.0 + 1, t.1) == *u {
        res.push(Kind::Down);
    }
    res
}

fn kind_v_to_usize(kind_v: &Vec<Kind>) -> usize {
    let mut dir = [false; 4]; // [Left, Right, Up, Down]
    if kind_v.contains(&Kind::Left) {
        dir[0] = true;
    }
    if kind_v.contains(&Kind::Right) {
        dir[1] = true;
    }
    if kind_v.contains(&Kind::Up) {
        dir[2] = true;
    }
    if kind_v.contains(&Kind::Down) {
        dir[3] = true;
    }
    match dir {
        [false, false, false, false] => usize::MAX,
        [true, true, true, true] => 0,
        [true, true, false, false] => 1,
        [false, false, true, true] => 2,
        [true, false, false, true] => 3,
        [true, false, true, false] => 4,
        [false, true, true, false] => 5,
        [false, true, false, true] => 6,
        _ => unreachable!(),
    }
}

fn is_rail(kind_v: &Vec<Kind>) -> bool {
    kind_v.len() == 2
}

#[derive(Clone)]
pub struct Rail {
    // 1: Left, Right
    // 2: Up, Down
    // 3: Left, Down
    // 4: Left, Up
    // 5: Right, Up
    // 6: Right, Down
    pub kind_v: Vec<Kind>,
    pub r: usize,
    pub c: usize,
}

impl Rail {
    fn new(kind: usize, r: usize, c: usize) -> Self {
        let kind_v = match kind {
            1 => vec![Kind::Left, Kind::Right],
            2 => vec![Kind::Up, Kind::Down],
            3 => vec![Kind::Left, Kind::Down],
            4 => vec![Kind::Left, Kind::Up],
            5 => vec![Kind::Right, Kind::Up],
            6 => vec![Kind::Right, Kind::Down],
            _ => unreachable!(),
        };
        Rail { kind_v, r, c }
    }
}

#[derive(Clone)]
pub struct Station {
    pub kind_v: Vec<Kind>,
    pub r: usize,
    pub c: usize,
}

impl Station {
    fn new(r: usize, c: usize) -> Self {
        Station {
            kind_v: vec![Kind::Left, Kind::Right, Kind::Up, Kind::Down],
            r,
            c,
        }
    }
}

#[derive(Clone)]
enum Op {
    None,
    Rail(Rail),
    Station(Station),
}

impl fmt::Display for Op {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        match self {
            Op::None => writeln!(f, "-1")?,
            Op::Rail(r) => writeln!(f, "{} {} {}", kind_v_to_usize(&r.kind_v), r.r, r.c)?,
            Op::Station(t) => writeln!(f, "0 {} {}", t.r, t.c)?,
        }
        Ok(())
    }
}



#[derive(Clone)]
struct Operations {
    ops: Vec<Op>,
}

impl Operations {
    fn new() -> Self {
        Operations {
            ops: Vec::new(),
        }
    }

    fn print(&self) {
        let mut ops = self.ops.clone();
        if ops.len() < T {
            ops.resize(T, Op::None);
        } else if ops.len() > T {
            ops.truncate(T);
        }
        for op in &ops {
            print!("{}", op);
        }
    }

    fn push(&mut self, op: Op) {
        self.ops.push(op);
    }

    fn len(&self) -> usize {
        return self.ops.len();
    }
}


#[derive(Clone)]
struct State {
    money: i64,
    income: i64,
    final_money: i64,
    operations: Operations,
    actions: Vec<(usize, usize)>,
    grid_state: Vec<Vec<Vec<Kind>>>,
    grid_scope_src: Vec<Vec<HashSet<usize>>>,
    grid_scope_dst: Vec<Vec<HashSet<usize>>>,
    src_waiting: HashSet<usize>,
    dst_waiting: HashSet<usize>,
    src: Vec<(usize, usize)>,
    dst: Vec<(usize, usize)>,
    potential: Vec<i64>,
    grid_potential_current: Vec<Vec<i64>>,
    grid_potential_future: Vec<Vec<i64>>,
    n: usize,
    t: usize,
}

impl State {
    fn new(input: &Input) -> State {
        // 初期値
        let mut state = State {
            money: input.k,
            final_money: input.k,
            income: 0,
            n: input.n,
            t: input.t,
            operations: Operations::new(),
            actions: vec![],
            src: input.src.clone(),
            dst: input.dst.clone(),
            potential: vec![0; input.m],
            grid_potential_current: vec![vec![0; input.n]; input.n],
            grid_potential_future: vec![vec![0; input.n]; input.n],
            grid_state: vec![vec![vec![]; input.n]; input.n],
            grid_scope_src: vec![vec![HashSet::new(); input.n]; input.n],
            grid_scope_dst: vec![vec![HashSet::new(); input.n]; input.n],
            src_waiting: HashSet::new(),
            dst_waiting: HashSet::new(),
        };

        // potentialを初期化
        for i in 0..input.m {
            let (r_src, c_src) = state.src[i];
            let (r_dst, c_dst) = state.dst[i];
            let r_src = r_src as i64;
            let c_src = c_src as i64;
            let r_dst = r_dst as i64;
            let c_dst = c_dst as i64;
            state.potential[i] = (r_src - r_dst).abs() + (c_src - c_dst).abs();
        }

        // grid_scope_srcを初期化
        for i in 0..input.m {
            let (r, c) = input.src[i];
            let r = r as i64;
            let c = c as i64;

            for dr in -2..=2 {
                let rx = r + dr;
                if !(0 <= rx && rx < input.n as i64) {
                    continue;
                }
                for dc in -2..=2 {
                    let cx = c + dc;
                    if !(0 <= cx && cx < input.n as i64)
                        || (dr).abs() + (dc).abs() > 2
                    {
                        continue;
                    }
                    state.grid_scope_src[rx as usize][cx as usize].insert(i);
                }
            }
        }

        // grid_scope_dstを初期化
        for i in 0..input.m {
            let (r, c) = input.dst[i];
            let r = r as i64;
            let c = c as i64;

            for dr in -2..=2 {
                let rx = r + dr;
                if !(0 <= rx && rx < input.n as i64) {
                    continue;
                }
                for dc in -2..=2 {
                    let cx = c + dc;
                    if !(0 <= cx && cx < input.n as i64)
                        || (dr).abs() + (dc).abs() > 2
                    {
                        continue;
                    }
                    state.grid_scope_dst[rx as usize][cx as usize].insert(i);
                }
            }
        }

        // grid_potential_futureを初期化
        for r in 0..state.n {
            for c in 0..state.n {
                for i in state.grid_scope_src[r][c].clone() {
                    state.grid_potential_future[r][c] += state.potential[i];
                }
                for i in state.grid_scope_dst[r][c].clone() {
                    state.grid_potential_future[r][c] += state.potential[i];
                }
            }
        }
        state
    }


    fn action(&mut self, station: (usize, usize)) -> bool {
        self.actions.push(station);
        if self.actions.len() == 1 {
            self.build_station(station)
        } else {
            self.build_station_and_rail(station)
        }
    }

    fn build_station(&mut self, (r, c): (usize, usize)) -> bool  {
        // お金がなければ待ち、駅だけを建てる
        while self.money < STATION_COST {
            self.operate(&Op::None);
        }
        self.operate(&Op::Station(Station::new(r, c)));
        return true;
    }

    fn build_station_and_rail(&mut self, station: (usize, usize)) -> bool {
        let (station_r, station_c) = station;
        if kind_v_to_usize(&self.grid_state[station_r][station_c]) == usize::MAX {
            // BFSで一番近駅までの経路を探索し、そのルートにレールを建築する
            let start = (station_r, station_c);
            let mut goal:(usize, usize) = (usize::MAX, usize::MAX);
            let mut queue = VecDeque::new();
            let mut visited = vec![vec![false; self.n]; self.n];
            let mut prev = vec![vec![(usize::MAX, usize::MAX); self.n]; self.n];
            let mut rail:(usize, usize) = (usize::MAX, usize::MAX);

            queue.push_back(start);
            visited[start.0][start.1] = true;
            
            'bfs: while let Some((r, c)) = queue.pop_front() {
                for dr in -1..=1 {
                    for dc in -1..=1 {
                        if (dr as i64).abs() + (dc as i64).abs()  != 1 {
                            continue;
                        }
                        let nr = r as i64 + dr;
                        let nc = c as i64 + dc;
                
                        if nr >= 0 && nr < self.n as i64 && nc >= 0 && nc < self.n as i64 {
                            let nr = nr as usize;
                            let nc = nc as usize;
                            let num = kind_v_to_usize(&self.grid_state[nr][nc]);

                            // 駅を発見したら終了
                            if num == 0 {
                                prev[nr][nc] = (r, c);
                                goal = (nr, nc);
                                break 'bfs;
                            }

                            // railも第二候補として記憶しておく
                            if num > 0 && num <= 6 && rail == (usize::MAX, usize::MAX) {
                                rail = (nr, nc)
                            }
                
                            if !visited[nr][nc] {
                                visited[nr][nc] = true;
                                prev[nr][nc] = (r, c);
                                if num == usize::MAX {
                                    queue.push_back((nr, nc));
                                }
                            }
                        }
                    }
                }
            }

            if goal == (usize::MAX, usize::MAX) {
                goal = rail;
            }
            
            if goal == (usize::MAX, usize::MAX) {
                panic!("no place to connect.");
            }

            // 建築費用が足りるか確認
            let mut cost = STATION_COST;
            let (r_s, c_s) = start;
            let (r_g, c_g) = goal;
            let r_s = r_s as i64;
            let c_s = c_s as i64;
            let r_g = r_g as i64;
            let c_g = c_g as i64;
            cost += ((r_s - r_g).abs() + (c_s - c_g).abs()) * RAIL_COST;
            if goal == rail {
                cost += STATION_COST;
            }
            if self.income == 0 && cost > self.money {
                return false;
            }

            // 経路復元しながらレールを建築
            let mut current = goal;

            // for row in prev.clone() {
            //     println!("{:?}", row);
            // }

            while prev[current.0][current.1] != start {
                let nxt = current.clone();
                current = prev[current.0][current.1];
                let prv = prev[current.0][current.1];
                // お金がなければ貯まるまで待つ
                while self.money < RAIL_COST {
                    self.operate(&Op::None);
                }

                // レールを建築
                let kind_v = culc_kind_v(&(prv.0 as i64, prv.1 as i64), &(current.0 as i64, current.1 as i64), &(nxt.0 as i64, nxt.1 as i64));
                self.operate(&Op::Rail(Rail::new(kind_v_to_usize(&kind_v), current.0, current.1)));
            }

            // 終点が線路だったなら駅を建築
            if goal == rail {
                while self.money < STATION_COST {
                    self.operate(&Op::None);
                }
                self.operate(&Op::Station(Station::new(goal.0, goal.1)));
            }

        }
        
        // 駅を建築
        while self.money < STATION_COST {
            self.operate(&Op::None);
        }
        self.operate(&Op::Station(Station::new(station_r, station_c)));
        
        return true;
    }

    fn operate(&mut self, op: &Op)  {
        self.operations.push(op.clone());
        match op {
            Op::None => {},
            Op::Rail(rail) => self.rail(rail.clone()),
            Op::Station(station) => self.station(station.clone()),
        }
        self.money += self.income;
        if self.operations.len() > 2000 {
            // self.operations.print();
            panic!("waiting forever...")
        }
    }


    fn rail(&mut self, rail: Rail)  {
        if self.money < RAIL_COST {
            panic!("Not enough money");
        }
        self.money -= RAIL_COST;
        self.final_money -= RAIL_COST;
        if self.grid_state[rail.r][rail.c] != vec![] {
            panic!("Rail or Station already exists");
        }
        self.grid_state[rail.r][rail.c] = rail.kind_v.clone();


    }
    
    fn update_grid_potential(&mut self, i: usize, is_source: bool, add_waiting: bool) {
        if add_waiting {
            // 自身を処理
            let (r, c) = if is_source { self.src[i] } else { self.dst[i] };
            let (r, c) = (r as i64, c as i64);
            let value = self.potential[i];
            for dr in -2..=2 {
                let rx = r + dr;
                if !(0 <= rx && rx < self.n as i64) {
                    continue;
                }
                for dc in -2..=2 {
                    let cx = c + dc;
                    if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                        continue;
                    }
                    self.grid_potential_future[rx as usize][cx as usize] -= value;
                }
            }

            // 相方を処理
            let (r, c) = if !is_source { self.src[i] } else { self.dst[i] };
            let (r, c) = (r as i64, c as i64);
            let value = self.potential[i];
            for dr in -2..=2 {
                let rx = r + dr;
                if !(0 <= rx && rx < self.n as i64) {
                    continue;
                }
                for dc in -2..=2 {
                    let cx = c + dc;
                    if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                        continue;
                    }
                    self.grid_potential_future[rx as usize][cx as usize] -= value;
                    self.grid_potential_current[rx as usize][cx as usize] += value;
                }
            }
        } else {
            // 自身を処理
            let (r, c) = if is_source { self.src[i] } else { self.dst[i] };
            let (r, c) = (r as i64, c as i64);
            let value = self.potential[i];
            for dr in -2..=2 {
                let rx = r + dr;
                if !(0 <= rx && rx < self.n as i64) {
                    continue;
                }
                for dc in -2..=2 {
                    let cx = c + dc;
                    if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                        continue;
                    }
                    self.grid_potential_current[rx as usize][cx as usize] -= value;
                }
            }

        }


    }

    fn process_new_entries(&mut self, new_entries: Vec<usize>, is_source: bool) {
        for i in new_entries {
            let (r, c) = if is_source { self.src[i] } else { self.dst[i] };
            let (r, c) = (r as i64, c as i64);


            if (is_source && self.dst_waiting.contains(&i)) || (!is_source && self.src_waiting.contains(&i)) {
                // ペアが成立
                self.income += self.potential[i];
                self.final_money += self.potential[i] * (self.t as i64 - self.operations.len() as i64 + 1);
                
                if is_source {
                    self.dst_waiting.remove(&i);
                    for dr in -2..=2 {
                        let rx = r + dr;
                        if !(0 <= rx && rx < self.n as i64) {
                            continue;
                        }
                        for dc in -2..=2 {
                            let cx = c + dc;
                            if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                                continue;
                            }
                            self.grid_scope_src[rx as usize][cx as usize].remove(&i);
                        }
                    }
                } else {
                    self.src_waiting.remove(&i);
                    for dr in -2..=2 {
                        let rx = r + dr;
                        if !(0 <= rx && rx < self.n as i64) {
                            continue;
                        }
                        for dc in -2..=2 {
                            let cx = c + dc;
                            if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                                continue;
                            }
                            self.grid_scope_dst[rx as usize][cx as usize].remove(&i);
                        }
                    }
                }

                self.update_grid_potential(i, is_source, false);
            } else {
                if is_source {
                    self.src_waiting.insert(i);

                    for dr in -2..=2 {
                        let rx = r + dr;
                        if !(0 <= rx && rx < self.n as i64) {
                            continue;
                        }
                        for dc in -2..=2 {
                            let cx = c + dc;
                            if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                                continue;
                            }
                            self.grid_scope_src[rx as usize][cx as usize].remove(&i);
                        }
                    }
                } else {
                    self.dst_waiting.insert(i);
                    for dr in -2..=2 {
                        let rx = r + dr;
                        if !(0 <= rx && rx < self.n as i64) {
                            continue;
                        }
                        for dc in -2..=2 {
                            let cx = c + dc;
                            if !(0 <= cx && cx < self.n as i64) || dr.abs() + dc.abs() > 2 {
                                continue;
                            }
                            self.grid_scope_dst[rx as usize][cx as usize].remove(&i);
                        }
                    }
                }
                // for row in &self.grid_scope_src {
                //     println!("{:?}", row);
                // }
                // 相方のポテンシャルを処理
                self.update_grid_potential(i, is_source, true);
            }
        }
    }

    // 駅と駅の間に線路が引かれている前提でコードを書くのでバグに注意
    fn station(&mut self, station: Station)  {
        if self.money < STATION_COST {
            panic!("Not enough money");
        }
        self.money -= STATION_COST;
        self.final_money -= STATION_COST;


        if self.grid_state[station.r][station.c].len() == 4 {
            panic!("Station already exists");
        }

        self.grid_state[station.r][station.c] = station.kind_v.clone();

        let new_srcs: Vec<_> = self.grid_scope_src[station.r][station.c]
        .iter()
        .filter(|&&src| !self.src_waiting.contains(&src))
        .copied()
        .collect();

        let new_dsts: Vec<_> = self.grid_scope_dst[station.r][station.c]
            .iter()
            .filter(|&&dst| !self.dst_waiting.contains(&dst))
            .copied()
            .collect();

        // println!("{:?}", &new_srcs);
        
        self.process_new_entries(new_srcs, true);
        self.process_new_entries(new_dsts, false);
                    
        
    }

    fn get_candidates(&self) -> Vec<(usize, usize, i64, i64, bool)> {
        let candidates: Vec<(usize, usize, i64, i64, bool)> = (0..self.n)
            .flat_map(|r| (0..self.n).map(move |c| (r, c)))
            .map(|(r, c)| (r, c, self.grid_potential_current[r][c], self.grid_potential_future[r][c], is_rail(&self.grid_state[r][c])))
            .collect();
        
        candidates
    }
}
