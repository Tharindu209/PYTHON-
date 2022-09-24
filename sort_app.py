import tkinter
import tkinter.messagebox

import sort.bubblesort as bs
import sort.insertionsort as Is
import sort.heapsort as hs
import sort.selectionsort as ss

class GUI:
    def __init__(self):
        # initial GUI
        self.main_window = tkinter.Tk()
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        # create main label
        self.lable = tkinter.Label(self.top_frame,text = 'SORT APPLICATION')
        self.lable.pack(side = 'top')
        
        # selection 
        self.radio = tkinter.IntVar()
        self.radio.set(1)
        
        self.rb1 = tkinter.Radiobutton(self.top_frame,text = 'bubble sort',variable = self.radio,value = 1)
        self.rb2 = tkinter.Radiobutton(self.top_frame,text = 'insertion sort',variable=self.radio,value = 2)
        self.rb3 = tkinter.Radiobutton(self.top_frame,text = 'heap sort',variable=self.radio,value = 3)
        self.rb4 = tkinter.Radiobutton(self.top_frame,text = 'selection sort',variable=self.radio,value = 4)
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        
        # convert button
        self.b1 = tkinter.Button(self.bottom_frame,text = 'convert',command = self.action)
        self.b1.pack(side = 'left')
        
        self.b2 = tkinter.Button(self.bottom_frame,text ='quit',command = self.main_window.destroy)
        self.b2.pack(side = 'right')
        self.top_frame.pack()
        self.bottom_frame.pack()
        
        self.main_window.mainloop()
        
    
    def action(self):
        value = self.radio.get()
        
        if value == 1:
            tkinter.messagebox.showinfo("sorted: {} ",format(str(bs.main())))
        
        if value == 2:
            tkinter.messagebox.showinfo("sorted: {} ",format(str(Is.main())))
        
        if value == 3:
            tkinter.messagebox.showinfo("sorted: {} ",format(str(hs.main())))
        
        if value == 4:
            tkinter.messagebox.showinfo("sorted: {} ",format(str(ss.main())))
            
            
    
        
        
new_window = GUI()