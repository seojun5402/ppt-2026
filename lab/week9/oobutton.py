import tkinter as tk

root = tk.Tk()
root.title("oobutton")
root.geometry("600x400")

def on_label_clicked(event):
    print(f"라벨이 클릭되었습니다: {event}")

label = tk.Label(root, text="객체지원윈도우프로그래밍")
label.bind("<Double-1>", on_label_clicked)
label.pack()

def on_bin1_clicked(event):
    print(f"버튼이 클릭되었습니다: {event}")
    label.config(text = f"버튼이 클릭되었습니다: {event}")

bin1 = tk.Button(root, text = "클릭해볼까요?", width = "100" , height = 50 , fg = "red")
bin1.bind("<Button-1>", on_bin1_clicked)
bin1.pack()

root.mainloop()