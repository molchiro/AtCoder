use std::isize;
use std::time;
use proconio::input;
use rand;
use rand::prelude::*;


const N: usize = 20;
const M: usize = 40;

fn main() {
    let start_time = time::Instant::now();
    let mut rng: rand::rngs::StdRng = rand::SeedableRng::from_seed([123 as u8; 32]);


    input! {
        _: usize, m: usize,
        destinations: [(usize, usize); m],
    }
    let init_game = Game::new(destinations[0], destinations[1..].to_vec());
    // 初期解
    let mut init_ans = init_game.clone();
    while !init_ans.finished() {
        // println!("{} ({:?})", game.target_index, game.targets[game.target_index]);
        init_ans.go_next_target();
    }

    // 手順のどこかにalterを挿入して解き直して改善するか見る
    let mut best_ans = init_ans.clone();
    while start_time.elapsed().as_millis() < 1950 {

        let alter_index;
        if start_time.elapsed().as_millis() < 800 {
            alter_index = rng.gen_range(0..best_ans.actions.len()/4);
        } else if start_time.elapsed().as_millis() < 1200 {
            alter_index = rng.gen_range(best_ans.actions.len()/4..best_ans.actions.len()/2);
        } else if start_time.elapsed().as_millis() < 1600 {
            alter_index = rng.gen_range(best_ans.actions.len()/2..best_ans.actions.len()*3/4);
        } else {
            alter_index = rng.gen_range(best_ans.actions.len()*3/4..best_ans.actions.len());
        }

        let alter_direction = match rng.gen_range(0..4) {
            0 => Direction::Up,
            1 => Direction::Down,
            2 => Direction::Left,
            _ => Direction::Right,
        };
        let mut new_ans = init_game.clone();
        // alter_indexまでの行動を再現
        for i in 0..alter_index {
            new_ans.act(&best_ans.actions[i]);
        }
        // alterを挿入
        new_ans.act(&Action::Alter(alter_direction));
        
        // 以降alterなしで最適な行動をシミュレーション
        while !new_ans.finished() {
            new_ans.go_next_target();
        }
        if new_ans.score() > best_ans.score() {
            best_ans = new_ans;
        }
    }


    // println!("score: {}", game.score());
    // println!("turn: {}", game.turn);
    // println!("actions: {}", game.actions.len());

    for i in 0..best_ans.actions.len() {
        println!("{}", best_ans.actions[i].to_string());
    }
}

#[derive(Clone)]
struct Game {
    targets: Vec<(usize, usize)>,
    grid: [[bool; N]; N],
    target_index: usize,
    now: (usize, usize),
    actions: Vec<Action>,
    turn: usize,
}

impl Game {
    fn new(now: (usize, usize), targets: Vec<(usize, usize)>) -> Self {
        let grid = [[false; N]; N];
        let target_index = 0;
        let actions = vec![];
        let turn = 0;

        Game {
            targets,
            grid,
            target_index,
            now,
            actions,
            turn,
        }
    }

    fn act(&mut self, action: &Action) {
        match action {
            Action::Move(direction) => {
                self.move_player(direction);
            }
            Action::Skate(direction) => {
                self.skate(direction);
            }
            Action::Alter(direction) => {
                self.alter(direction);
            }
        }
        self.actions.push(action.clone());
        if self.now == self.targets[self.target_index] {
            self.target_index += 1;
        }
        self.turn += 1;
    }

    fn move_player(&mut self, direction: &Direction) {
        let (h, w) = self.now;
        match direction {
            Direction::Up => {
                if h > 0 && !self.grid[h-1][w] {
                    self.now.0 -= 1;
                }
            }
            Direction::Down => {
                if h < N-1 && !self.grid[h+1][w] {
                    self.now.0 += 1;
                }
            }
            Direction::Left => {
                if w > 0 && !self.grid[h][w-1] {
                    self.now.1 -= 1;
                }
            }
            Direction::Right => {
                if w < N-1 && !self.grid[h][w+1] {
                    self.now.1 += 1;
                }
            }
        }

    }
        
    fn skate(&mut self, direction: &Direction) {
        let (h, w) = self.now;
        match direction {
            Direction::Up => {
                while self.now.0 > 0 && !self.grid[self.now.0-1][w] {
                    self.now.0 -= 1;
                }
            }
            Direction::Down => {
                while self.now.0 < N-1 && !self.grid[self.now.0+1][w] {
                    self.now.0 += 1;
                }
            }
            Direction::Left => {
                while self.now.1 > 0 && !self.grid[h][self.now.1-1] {
                    self.now.1 -= 1;
                }
            }
            Direction::Right => {
                while self.now.1 < N-1 && !self.grid[h][self.now.1+1] {
                    self.now.1 += 1;
                }
            }
        }

    }

    fn alter(&mut self, direction: &Direction) {
        let (h, w) = self.now;
        match direction {
            Direction::Up => {
                if h > 0 {
                    self.grid[h-1][w] = !self.grid[h-1][w];
                }
            }
            Direction::Down => {
                if h < N-1 {
                    self.grid[h+1][w] = !self.grid[h+1][w];
                }
            }
            Direction::Left => {
                if w > 0 {
                    self.grid[h][w-1] = !self.grid[h][w-1];
                }
            }
            Direction::Right => {
                if w < N-1 {
                    self.grid[h][w+1] = !self.grid[h][w+1];
                }
            }
        }

    }

    fn go_next_target(&mut self) {
        if self.finished() {
            return;
        }
        // println!("now: {:?}", self.now);
        // bfsで次のターゲットまでの最短経路を探索する
        let mut queue = vec![(self.now)];
        let mut visited = vec![vec![false; N]; N];
        let mut prev: Vec<Vec<Vec<(usize, usize, Action)>>> = vec![vec![vec![]; N]; N];
        visited[self.now.0][self.now.1] = true;
        let next_target = self.targets[self.target_index];
        let mut found = false;
        while !queue.is_empty() {
            let (h, w) = queue.remove(0);
            if (h, w) == next_target {
                found = true;
                break;
            }
            // 上下左右にスケート
            for direction in [Direction::Up, Direction::Down, Direction::Left, Direction::Right] {
                let mut nh = h as isize;
                let mut nw = w as isize;

                match direction {
                    Direction::Up => {
                        while nh > 0 && !self.grid[nh as usize - 1][nw as usize] {
                            nh -= 1;
                        }
                    }
                    Direction::Down => {
                        while nh < N as isize - 1 && !self.grid[nh as usize + 1][nw as usize] {
                            nh += 1;
                        }
                    }
                    Direction::Left => {
                        while nw > 0 && !self.grid[nh as usize][nw as usize - 1] {
                            nw -= 1;
                        }
                    }
                    Direction::Right => {
                        while nw < N as isize - 1 && !self.grid[nh as usize][nw as usize + 1] {
                            nw += 1;
                        }
                    }
                    
                }

                let nh = nh as usize;
                let nw = nw as usize;
                if !visited[nh][nw]{
                    visited[nh][nw] = true;
                    prev[nh][nw].push((h, w, Action::Skate(direction)));
                    queue.push((nh, nw));
                }
            }
            // 上下左右に一歩移動
            for direction in [Direction::Up, Direction::Down, Direction::Left, Direction::Right] {
                let mut nh = h as isize;
                let mut nw = w as isize;

                match direction {
                    Direction::Up => {
                        nh -= 1;
                    }
                    Direction::Down => {
                        nh += 1;
                    }
                    Direction::Left => {
                        nw -= 1;
                    }
                    Direction::Right => {
                        nw += 1;
                    }
                    
                }
                if nh < 0 || nh >= N as isize || nw < 0 || nw >= N as isize {
                    continue;
                }
                let nh = nh as usize;
                let nw = nw as usize;
                if !visited[nh][nw] && !self.grid[nh][nw] {
                    visited[nh][nw] = true;
                    prev[nh][nw].push((h, w, Action::Move(direction)));
                    queue.push((nh, nw));
                }
            }
            
            
        }

        // 解がなかった場合は袋小路にいるので、tunrを無理やり進める
        if !found {
            self.turn = 2*N*M;
        } else {

            // 経路復元
            let mut actions = vec![];
            let mut now = next_target;
            while now != self.now {
                let (h, w, action) = prev[now.0][now.1].pop().unwrap();
                actions.push(action);
                now = (h, w);
            }
    
            // println!("actions: {:?}", actions);
    
            // 行動を再現
            while actions.len() > 0 {
                let action = actions.pop().unwrap();
                self.act(&action);
            }
        }
        

    }
    fn finished(&self) -> bool {
        self.target_index >= self.targets.len() || self.turn >= 2*N*M
    }

    fn score(&self) -> usize {
        if self.target_index < M-1 {
            return self.target_index + 1;
        } else {
            return M+2*N*M-self.turn;
        }
    }
    
}

#[derive(Clone, Debug)]
enum Action {
    Move(Direction),
    Skate(Direction),
    Alter(Direction)
}

impl Action {
    fn to_string(&self) -> String {
        match self {
            Action::Move(direction) => format!("M {}", direction.to_string()),
            Action::Skate(direction) => format!("S {}", direction.to_string()),
            Action::Alter(direction) => format!("A {}", direction.to_string()),
        }
    }
}

#[derive(Clone, PartialEq, Debug)]
enum Direction {
    Up,
    Down,
    Left,
    Right,
}

impl Direction {
    fn to_string(&self) -> String {
        match self {
            Direction::Up => "U".to_string(),
            Direction::Down => "D".to_string(),
            Direction::Left => "L".to_string(),
            Direction::Right => "R".to_string(),
        }
    }
}