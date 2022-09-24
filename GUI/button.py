import tkinter as t
import tkinter.messagebox

class gui:
    def __init__(self):
        self.window = t.Tk()
        
        self.top_frame = t.Frame(self.window)
        self.bottom_frame = t.Frame(self.window)
        
        self.label = t.Label(self.window,text = 'hello world')
        self.label.pack(side = 'top')
        self.radio_var = t.IntVar()
        self.radio_var.set(1)
        
        self.rb1 = t.Radiobutton(self.top_frame,text = 'option1',variable = self.radio_var,value =1 )
        self.rb2 = t.Radiobutton(self.top_frame,text = 'option2',variable = self.radio_var,value =2 )
        self.rb3 = t.Radiobutton(self.top_frame ,text = 'option3',variable = self.radio_var,value =3 )
        self.rb4 = t.Radiobutton(self.top_frame,text = 'option4',variable = self.radio_var,value =4 )
        
        self.rb1.pack()
        self.rb2.pack()
        self.rb3.pack()
        self.rb4.pack()
        
        self.button1 = t.Button(self.bottom_frame,text= 'ok',command =self.your_choice)
        self.button2 = t.Button(self.bottom_frame,text= 'quit',command =self.window.destroy)
        self.button1.pack(side = 'left')
        self.button2.pack(side = 'left')
        
        self.top_frame.pack() 
        self.bottom_frame.pack()

        t.mainloop()
         
         
    def your_choice(self):
        t.messagebox.showinfo('Selection', 'You selected option ' + str(self.radio_var.get()))
         
my_gui = gui()