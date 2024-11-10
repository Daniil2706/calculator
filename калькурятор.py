import tkinter as tk
def polo():
    num1 = int(nnmber1_entry.get())
    num2 = int(nnmber2_entry.get())
    return num1, num2

def instirt_valet(valet):
    nnmber3_entry.delete(0, "end")
    nnmber3_entry.insert(0, valet)

def add():
    num1, num2 = polo()
    ras = num1 + num2
    instirt_valet(ras)

def sub():
    num1, num2 = polo()
    ras = num1 - num2
    instirt_valet(ras)

def mul():
    num1, num2 = polo()
    ras = num1 * num2
    instirt_valet(ras)

def div():
    num1, num2 = polo()
    ras = num1 / num2
    instirt_valet(ras)

window = tk.Tk()
window.title("калькулятор")
window.geometry("350x350")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=6, height=10, command=add)
button_add.place(x=0, y=200)
button_sud = tk.Button(window, text="-", width=6, height=10, command=sub)
button_sud.place(x=50, y=200)
button_pol = tk.Button(window, text="*", width=6, height=10, command=mul)
button_pol.place(x=100, y=200)
button_poi = tk.Button(window, text=":", width=6, height=10, command=div)
button_poi.place(x=150, y=200)
nnmber1_entry = tk.Entry(window, width=60)
nnmber1_entry.place(x=0, y=50)
nnmber2_entry = tk.Entry(window, width=60)
nnmber2_entry.place(x=0, y=100)
nnmber3_entry = tk.Entry(window, width=60)
nnmber3_entry.place(x=0, y=150)
nnmber1 = tk.Label(window, text="Ведите первое число:")
nnmber1.place(x=0, y=30)
nnmber2 = tk.Label(window, text="Ведите второе число:")
nnmber2.place(x=0, y=80)
nnmber3 = tk.Label(window, text="Ответ:")
nnmber3.place(x=0, y=130)
window.mainloop()
