import tkinter as tk
from turtle import RawTurtle, ScrolledCanvas

# ===========================
# Tkinter 윈도우 + Turtle 캔버스 설정
# ===========================
root = tk.Tk()
root.title("유치원 코딩 앱")
root.geometry("600x400")

canvas = ScrolledCanvas(root, width=400, height=300)
canvas.pack(side=tk.LEFT)
t = RawTurtle(canvas)
t.speed(1)

# 명령어 리스트
commands = []

# ===========================
# 명령 추가 함수
# ===========================
def add_command(cmd):
    commands.append(cmd)
    update_command_list()

# 명령 리스트 표시
def update_command_list():
    text = "\n".join(commands)
    label_commands.config(text=text)

# ===========================
# 명령 실행 함수
# ===========================
def run_commands():
    for cmd in commands:
        if cmd == "앞으로":
            t.forward(50)
        elif cmd == "왼쪽":
            t.left(90)
        elif cmd == "오른쪽":
            t.right(90)
        elif cmd == "뒤로":
            t.backward(50)

# ===========================
# GUI 버튼
# ===========================
frame = tk.Frame(root)
frame.pack(side=tk.RIGHT, padx=10)

btn_forward = tk.Button(frame, text="앞으로", width=10, command=lambda: add_command("앞으로"))
btn_left = tk.Button(frame, text="왼쪽", width=10, command=lambda: add_command("왼쪽"))
btn_right = tk.Button(frame, text="오른쪽", width=10, command=lambda: add_command("오른쪽"))
btn_back = tk.Button(frame, text="뒤로", width=10, command=lambda: add_command("뒤로"))
btn_run = tk.Button(frame, text="실행!", width=10, bg="green", fg="white", command=run_commands)

btn_forward.pack(pady=5)
btn_left.pack(pady=5)
btn_right.pack(pady=5)
btn_back.pack(pady=5)
btn_run.pack(pady=20)

# 명령 리스트 표시 라벨
label_commands = tk.Label(frame, text="", justify="left", font=("Arial", 12))
label_commands.pack()

root.mainloop()
