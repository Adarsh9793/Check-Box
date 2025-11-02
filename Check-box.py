# step1: import tkinter
from tkinter import *

# step2: gui interaction
window = Tk()

#step3: adding inputs

window.geometry("400x400")

check_box_1 = IntVar()
check_box_2 = IntVar()
check_box_3 = IntVar()

chk_btn_1 = Checkbutton(window,text= "adarsh",onvalue=1, offvalue=2, height = 2, width = 10)
chk_btn_2 = Checkbutton(window, text="tripathi", onvalue=1, offvalue=0, height=2, width=10)
chk_btn_3 = Checkbutton(window, text="Raj", onvalue=1, offvalue=0, height=2, width=10)

chk_btn_1.pack()
chk_btn_2.pack()    
chk_btn_3.pack()

# step 4: mainloop
window.mainloop()