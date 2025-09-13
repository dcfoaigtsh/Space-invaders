# 🎮 Space Invaders - 太空侵略者

一款使用 **Python** 製作的 8-bit 風格射擊遊戲，靈感來自經典的《Space Invaders》。  
玩家將操控太空船，閃避並擊退來襲的外星人，挑戰三個逐漸升級的關卡。  

影片展示：[YouTube Demo](https://youtu.be/eTSU0HEgVzI)

---

## ✨ 遊戲特色
- 經典 **像素風格** 設計
- 三大關卡挑戰，難度逐步提升
- **方向鍵**控制移動，**空白鍵**發射雷射
- **P 鍵 / 按鈕**可暫停與繼續遊戲
- **R 鍵**重新開始
- 介面包含血量條、分數與最高分紀錄
- 遊戲結束或勝利畫面附有重新遊玩提示

---

## 🎮 遊戲玩法
1. 啟動遊戲 → 封面畫面（點擊 **START** 開始）
2. 進入遊戲說明頁面，了解操作方式
3. 倒數 3 秒後正式開始
4. 擊退外星人並避免被擊中（共 3 條命）
5. 三關全數通關則獲勝，失敗則會顯示 **You Lose**

---

## 🛠️ 系統架構

專案主要程式檔案：
- **Main.py**：遊戲主程式（初始化、UI、流程控制）
- **Game.py**：遊戲主邏輯（關卡、事件、碰撞檢測）
- **Alien.py**：定義外星人與神秘飛船
- **Obstacle.py**：定義障礙物
- **Spaceship.py**：定義玩家太空船
- **Laser.py**：定義雷射物件

---

## 🚀 安裝與執行
1. 下載或 clone 專案：
   ```bash
   git clone https://github.com/你的帳號/Space-invaders.git
   cd Space-invaders
2. 建立虛擬環境(建議)
   python -m venv venv
   source venv/bin/activate   # macOS/Linux
   venv\Scripts\activate      # Windows
3. 執行遊戲：
   python main.py
