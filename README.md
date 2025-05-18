# 🎮 Tic Tac Toe Game in Python (2-Player & AI Mode)

This is a terminal-based implementation of the classic **Tic Tac Toe** game written in Python.  
The game offers **two modes**:
- **2-Player Mode**: Two human players take turns.
- **Player vs Computer Mode**: Play against a smart AI opponent powered by the **Minimax algorithm**.

This project is perfect for beginners to practice Python fundamentals and for those looking to understand basic **game AI logic**.

---

## 📌 Features

✅ 3x3 Tic Tac Toe board displayed in the terminal  
✅ Supports **Two Player Mode**  
✅ Supports **Player vs Computer Mode** (unbeatable AI using Minimax)  
✅ Win and Draw detection logic  
✅ Clean and interactive command-line interface  
✅ Input validation for incorrect or taken cells
✅ Adjustable AI difficulty (easy, medium, hard)  

---

## 🧰 Technologies Used

- **Language**: Python 3
- **Libraries**: Only built-in Python modules (no external dependencies)

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/tic-tac-toe-python.git
cd tic-tac-toe-python
```

### 2. Run the Game
```bash
python tic_tac_toe.py
```

> Make sure Python 3 is installed on your machine.

---

## 🕹️ Gameplay Instructions

- At the start, select game mode:
  - `1` → Player vs Player
    - `2` → Player vs Computer
- Players take turns entering their moves by specifying the cell number
- The computer AI uses the Minimax algorithm to play optimally

---

## 🤖 Minimax Algorithm

In **Player vs Computer Mode**, the AI uses the **Minimax algorithm**, which recursively evaluates all possible future moves and selects the optimal one that maximizes its chance of winning while minimizing the opponent's.

This makes the computer **unbeatable** – it will either win or force a draw!

---

## 🖥️ Sample Output

```
Welcome to Tic Tac Toe!
Choose Game Mode:
1 - Player vs Player
2 - Player vs Computer

Enter your choice: 2

You are X. Computer is O.
  1   2   3
1   |   |  
 ---+---+---
2   |   |  
 ---+---+---
3   |   |  

Your move (row and column): 1 1
```

---

## 🧠 Future Enhancements

- GUI version using Tkinter or Pygame  
- Score tracking and leaderboard  
- Game replay option

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🤝 Contributing

Contributions are welcome!  
Feel free to fork this repo, add features, improve performance, or refactor the code.

