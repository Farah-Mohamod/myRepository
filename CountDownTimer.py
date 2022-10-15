#Importing needful modules

import tkinter as tk
import datetime
import winsound as ws

#creating the countdown class

class Countdown(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.create_widgets()
        self.show_widgets()
        self.seconds_left=0
        self._timer_on=False

        
#Declaring the widgets
    def show_widgets(self):
        self.label.pack() #label creates the top widget of the screean
        self.entry.pack() #Entry creates the text boxes that we'll type something
        self.start.pack() #Start botton is basically starts the timing
        self.stop.pack()  #stop botton is basically stops the timing
        self.reset.pack() #reset botton is basically resets the time
        
#Creating the widgets that we've declared
    def create_widgets(self):
        self.label=tk.Label(self,text="Seconds: ")
        self.entry=tk.Entry(self,justify="center")
        self.entry.focus_set()
        self.reset=tk.Button(self,text="Reset",command=self.reset_button) #command=self.reset_buttom will reset the button
        self.stop=tk.Button(self,text="Pause",command=self.stop_button)
        self.start=tk.Button(self,text="Start",command=self.start_button)


    def countdown(self):
        self.label["text"]=self.conver_seconds_left_to_time()


        if self.seconds_left:
            self.seconds_left-=1
            self.timer_on=self.after(1000,self.countdown)
        else:
            self.timer_on=False
            ws.PlaySound("Alarm Clock Sound",ws.SND_FILENAME)

    def reset_button(self):
        self.seconds_left=0
        self.stop_timer()
        self._timer_on=False
        self.label["text"]="Seconds."
        self.start.forget()
        self.stop.forget()      #replacing the buttons
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()


    def stop_button(self):
        self.stop_timer()
        self.seconds_left=int(self.entry.get())

    def start_button(self):
        self.seconds_left=int(self.entry.get())
        self.stop_timer()
        self.countdown()
        self.start.forget()
        self.stop.forget()
        self.reset.forget()
        self.start.pack()
        self.stop.pack()
        self.reset.pack()


    def stop_timer(self):
        if self._timer_on:
            self.after_cancel(self._timer_on)
            self._timer_on=False

    def conver_seconds_left_to_time(self):
        return datetime.timedelta(seconds=self.seconds_left)



    
            

# MAIN LOOP

if __name__=="__main__":
    root=tk.Tk()
    root.resizable(False,False)


    
    countdown=Countdown(root)
    countdown.pack() #
    root.mainloop() #this will keep the screen open
    















    
