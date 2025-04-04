from robot import Robot
import tkinter

class GUI(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("ROBOTIK")
        self.prostredie()
        self.canvas = tkinter.Canvas(self, width=200, height=200) # veľkost canvasu
        self.canvas.place(x=300, y=200)
        self.mainloop()



    def prostredie(self):
        tkinter.Button(self, text="Prestav sa", font=("Arial", 18), background="lightblue", command=self.predstavenie).place(x=0, y=0)
        self.text_predstav_sa = tkinter.StringVar() # specialna stringvarova premenna pre gui
        tkinter.Entry(self, textvariable=self.text_predstav_sa, font=("Arial", 18), background="lightgreen", width=40).place(x=150, y=15)
        tkinter.Button(self, text="Vymaž", font=("Arial", 15), background="red", foreground="white", command=self.vymazanie).place(x=680, y=5)    # nastavenie commandu pomocou lambdy: lambda: self.text_predstav_sa.set("")


    def predstavenie(self):
        self.robot = Robot("Jano", 60)
        self.text_predstav_sa.set(self.robot.predstav_sa())

    def vymazanie(self):
        self.text_predstav_sa.set("")


GUI()