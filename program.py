import schedule
import time 
import tkinter as tk
from tkinter import ttk


root = tk.Tk()
menu = ttk.Frame(root)
menu.pack(side="top", fill="x")
root.title("balls")
root.geometry("500x200")
root.resizable(height = False, width = False)
ttk.Style().configure("my.TButton", font=("Arial",16,"bold"))
button1 = ttk.Button(menu, text ="click now", style="my.TButton")
button1.pack(fill="x" ,side="left")
button2 = ttk.Button(menu, text = "place holder" , style="my.TButton") 
button2.pack(fill="x",)

root.mainloop()






# def call():
#     print("good luck programmer")

# schedule.every(5).seconds.do(call)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


