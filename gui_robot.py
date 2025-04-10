from robot import Robot
import tkinter
from tkinter import messagebox

class GUI(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.geometry("800x500")
        self.title("ROBOTIK")
        self.robot = Robot("Jozo", 50)
        self.prostredie()
        self.canvas = tkinter.Canvas(self, width=200, height=200, background="lightblue") # veľkost canvasu
        self.canvas.place(x=300, y=200)
        self.mainloop()



    def prostredie(self):
        tkinter.Button(self, text="Predstav sa", font=("Arial", 18), background="lightblue", command=lambda: (self.zobraz_obrazok(), self.predstavenie())).place(x=0, y=0)
        self.text_predstav_sa = tkinter.StringVar() # specialna stringvarova premenna pre gui
        tkinter.Entry(self, textvariable=self.text_predstav_sa, font=("Arial", 18), background="lightgreen", width=40).place(x=150, y=15)
        tkinter.Button(self, text="Vymaž", font=("Arial", 15), background="red", foreground="white", command=self.vymazanie).place(x=680, y=5)    # nastavenie commandu pomocou lambdy: lambda: self.text_predstav_sa.set("")
        tkinter.Label(self, text="Zadajte meno:", font=("Arial", 15)).place(x=0, y=60)

        self.meno_robota = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.meno_robota, font=("Arial", 15)).place(x=150, y=60)
        tkinter.Button(self, text="Zmen", font=("Arial", 15), command=self.zmen_meno).place(x=400, y=60)


    def predstavenie(self):
        self.text_predstav_sa.set(self.robot.predstav_sa())

    def vymazanie(self):
        self.text_predstav_sa.set("")

    def zmen_meno(self):
        try:
            self.robot.meno = self.meno_robota.get()
        except ValueError as chyba:
            messagebox.showerror("chyba", chyba)

    def zobraz_obrazok(self):
        self.obrazok = tkinter.PhotoImage(file="robotik.png")
        self.canvas.create_image(50, 50, anchor=tkinter.CENTER, image=self.obrazok)


GUI()