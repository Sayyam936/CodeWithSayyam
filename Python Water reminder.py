
import schedule
import time
import tkinter
import tkinter.messagebox

def drinkwater():
    tkinter.messagebox.showinfo("Drink water", "Drink 1 glass of water ")

schedule.every(10).seconds.do(drinkwater)

while True:
    schedule.run_pending()
    time.sleep(1)
