import tkinter as tk
import math, random

# --- Game State ---
current_player = 'X'
board = [''] * 9
buttons = []
game_over = False

# --- Logic Functions ---
def check_win(b, p):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    for a,b_,c in wins:
        if b[a] == b[b_] == b[c] == p:
            return True, (a,b_,c)
    return False, None

def check_draw(b):
    return '' not in b

def get_empty(b):
    return [i for i, v in enumerate(b) if v == '']

def minimax(b, depth, is_max):
    if check_win(b, 'O')[0]: return 10 - depth
    if check_win(b, 'X')[0]: return -10 + depth
    if check_draw(b): return 0

    if is_max:
        best = -math.inf
        for i in get_empty(b):
            b[i] = 'O'
            best = max(best, minimax(b, depth + 1, False))
            b[i] = ''
        return best
    else:
        best = math.inf
        for i in get_empty(b):
            b[i] = 'X'
            best = min(best, minimax(b, depth + 1, True))
            b[i] = ''
        return best

def best_move(b):
    # Add randomness: sometimes AI doesn't play the best move
    if random.random() < 0.3:  # 30% chance of "mistake"
        return random.choice(get_empty(b))

    best = -math.inf
    move = -1
    for i in get_empty(b):
        b[i] = 'O'
        score = minimax(b, 0, False)
        b[i] = ''
        if score > best:
            best = score
            move = i
    return move

# --- GUI Functions ---
def update_status(msg):
    status_label.config(text=msg)

def check_state():
    global game_over
    win, combo = check_win(board, 'X')
    if win:
        update_status("🎉 Player X Wins!")
        for i in combo: buttons[i].config(bg='green')
        game_over = True
        return
    win, combo = check_win(board, 'O')
    if win:
        update_status("🤖 AI O Wins!")
        for i in combo: buttons[i].config(bg='orange')
        game_over = True
        return
    if check_draw(board):
        update_status("😐 It's a Draw!")
        game_over = True
        return
    update_status("Your turn! You are X")

def ai_play():
    global current_player
    if game_over: return
    root.after(400, do_ai)

def do_ai():
    global current_player
    idx = best_move(board)
    if idx != -1:
        board[idx] = 'O'
        buttons[idx].config(text='O', state=tk.DISABLED, fg='blue', font=('Arial', 24, 'bold'))
    check_state()
    if not game_over:
        current_player = 'X'
        update_status("Your turn! You are X")

def click_btn(idx):
    global current_player
    if board[idx] == '' and current_player == 'X' and not game_over:
        board[idx] = 'X'
        buttons[idx].config(text='X', state=tk.DISABLED, fg='red', font=('Arial', 24, 'bold'))
        check_state()
        if not game_over:
            current_player = 'O'
            update_status("AI's turn...")
            ai_play()

def reset():
    global board, current_player, game_over
    board = [''] * 9
    current_player = 'X'
    game_over = False
    for b in buttons:
        b.config(text='', state=tk.NORMAL, bg='SystemButtonFace')
    update_status("New Game! You are X")

# --- GUI Setup ---
root = tk.Tk()
root.title("Tic-Tac-Toe (Easy Minimax)")
root.resizable(False, False)

status_label = tk.Label(root, text="New Game! You are X", font=('Arial', 14, 'bold'))
status_label.grid(row=0, column=0, columnspan=3, pady=10)

frame = tk.Frame(root)
frame.grid(row=1, column=0, columnspan=3)

for i in range(9):
    btn = tk.Button(frame, text='', width=5, height=2,
                    font=('Arial', 24, 'bold'),
                    command=lambda i=i: click_btn(i))
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    buttons.append(btn)

reset_btn = tk.Button(root, text="New Game", font=('Arial', 12, 'bold'),
                      bg='lightblue', command=reset)
reset_btn.grid(row=2, column=0, columnspan=3, pady=10)

root.mainloop()
