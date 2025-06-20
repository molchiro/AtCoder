// 手動モードのフラグ
let manualMode = false;
let selectedAction = null; // 選択されたアクション（"rail", "station", "wait"）

// 手動モードの切り替え
function toggleManualMode() {
  manualMode = !manualMode;
  document.getElementById("manual_mode").innerText = manualMode ? "手動モード: ON" : "手動モード: OFF";
}
window.toggleManualMode = toggleManualMode;

// 行動の選択
function selectAction(action) {
  selectedAction = action;
  document.getElementById("selected_action").innerText = `選択中: ${action}`;
}
window.selectAction = selectAction;

// ゲームエリアのクリックイベント
function handleGridClick(event) {
  if (!manualMode || !selectedAction) return;
  
  const target = event.target;
  if (!target.classList.contains("grid-cell")) return;
  
  const x = target.dataset.x;
  const y = target.dataset.y;
  
  if (selectedAction === "rail") {
    placeRail(x, y);
  } else if (selectedAction === "station") {
    placeStation(x, y);
  } else if (selectedAction === "wait") {
    advanceTurn();
  }
}
document.getElementById("game_area").addEventListener("click", handleGridClick);

// 線路を配置
function placeRail(x, y) {
  if (money < 100) {
    alert("資金不足: 線路を配置できません");
    return;
  }
  // 実際に線路を配置するロジック（仮）
  document.querySelector(`[data-x='${x}'][data-y='${y}']`).classList.add("rail");
  money -= 100;
  advanceTurn();
}

// 駅を配置
function placeStation(x, y) {
  if (money < 5000) {
    alert("資金不足: 駅を配置できません");
    return;
  }
  // 実際に駅を配置するロジック（仮）
  document.querySelector(`[data-x='${x}'][data-y='${y}']`).classList.add("station");
  money -= 5000;
  advanceTurn();
}

// ターンを進める（集金フェーズ）
function advanceTurn() {
  turn++;
  document.getElementById("turn").innerText = `ターン: ${turn}`;
  collectIncome();
}

// 集金フェーズ
function collectIncome() {
  // 収益計算のロジック（仮）
  let income = Math.floor(Math.random() * 1000); // ここを適切な通勤計算に変更
  money += income;
  document.getElementById("money").innerText = `資金: ${money}`;
}

// UI要素の追加（HTMLに追加する必要あり）
document.body.insertAdjacentHTML("beforeend", `
  <button id="manual_mode" onclick="toggleManualMode()">手動モード: OFF</button>
  <button onclick="selectAction('rail')">線路配置</button>
  <button onclick="selectAction('station')">駅配置</button>
  <button onclick="selectAction('wait')">待機</button>
  <p id="selected_action">選択中: なし</p>
  <p id="turn">ターン: 0</p>
  <p id="money">資金: 0</p>
  <div id="game_area"></div>
`);
