from tkinter import *
import random
class RockPaper:

    def __init__(self):
        self.root=Tk()
        self.root.title("Rock Paper Scissor")
        self.root.geometry("600x650")
        try:
            self.root.iconbitmap(r"rcp.ico")
        except:
            pass
        self.wel()
        try:
            self.pic = PhotoImage(file=r"rrr.png")   
        except:
            print("Wrong image address")  
        self.picl = [PhotoImage(file = r"rockl.png"),PhotoImage(file=r"scissorsl.png"),PhotoImage(file=r"paperl.png")]
        self.picr=[PhotoImage(file = r"rock.png"),PhotoImage(file=r"scissorsr.png"),PhotoImage(file=r"paperr.png")]
        self.pscore,self.cscore=0,0
        self.root.resizable(0,0)

    def wel(self):
            Label(self.root,text="WELCOME",bg="#FFF8DC",fg="#080808",font="Times 25",pady=25).pack()
            Button(self.root,text="Start",bg="green",fg="white",activebackground="yellow",bd=4,pady=8,padx=10,command=self.Start).place(x=275,y=150)
            Button(self.root,text="Exit",bg="red",fg="white",activebackground="yellow",bd=4,pady=8,padx=12,command=exit).place(x=275,y=220)
    

    def draw(self):
        c = Canvas(self.root,height=400,width=400)
        c.place(x=150,y=320)
        c.create_line(50,10,200,10,fill="black",width=7)
        c.create_line(196,10,196,175,width=7)
        c.create_rectangle(170,160,220,180,fill="black")
        if (self.cscore>=1):
            c.create_line(75,10,75,30,fill="black",width=2)
        if (self.cscore>=2):
            c.create_oval(60,30,90,60,width=0,fill="black")
        if self.cscore>=3:
            c.create_line(75,60,75,109,fill="black",width=4)
        if self.cscore>=4:
            c.create_line(75,72,55,92,width=2)
            c.create_line(75,72,95,92,width=2)
        if self.cscore==5:
            c.create_line(75,107,50,139,width=2)
            c.create_line(75,106,100,139,width=2)
        if self.cscore==6:
            self.pscore,self.cscore=0,0
            for widgets in self.root.winfo_children():

                widgets.destroy()
            Label(self.root,text="You Loose!",fg="red",font="Times 30").pack()
            Button(self.root,text="Play Again!",bg="green",fg="white",activebackground="yellow",bd=3,pady=4,padx=10,command=self.game).pack(expand=True)
            Button(self.root,text="Exit",bg="red",fg="white",activebackground="yellow",bd=3,pady=4,padx=10,command=exit).pack(expand=True)
        elif self.pscore==6:
            self.pscore,self.cscore=0,0
            for widget in self.root.winfo_children():
                widget.destroy()
            Label(self.root,text="You Win!",fg="green",font="Times 30").pack()
            Button(self.root,text="Play Again!",bg="green",fg="white",activebackground="yellow",bd=3,pady=4,padx=10,command=self.game).pack(expand=True)
            Button(self.root,text="Exit",bg="red",fg="white",activebackground="yellow",bd=3,pady=4,padx=10,command=exit).pack(expand=True)

        
        


    def Start(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
        try:
            Label(self.root,image=self.pic,bg="yellow").pack(fill=X)
        except:
            print("Wrong Image address")
        v = IntVar()
        Label(self.root,text="Enter your Name",fg="red",bd=4,pady=8,padx=50,font="Algerian 16").pack()
        global name_var
        name_var = StringVar()
        Entry(self.root,bg="pink",fg="blue",bd=5,width=25,textvariable = name_var,selectbackground="yellow",selectforeground="red").pack()
        Label(self.root,text=" ",padx=20,pady=20).pack()
        Button(self.root,text="Submit",bg="red",fg="white",activebackground="yellow",bd=3,pady=4,padx=10,command=self.game).pack()
         
    
    def game(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
        Label(self.root,text="Let's Play!",fg="green",font="Times 14").place(x=250,y=10)
        Label(self.root,text=name_var.get(),fg="white",bg="#0000FF",relief=GROOVE,padx=25,pady=10,font=" 15").place(x=135,y=60)
        Label(self.root,text="v/s",fg="red",font="Times 22").place(x=280,y=230)
        Label(self.root,text="Computer",fg="white",bg="#53868B",relief=GROOVE,pady=10,padx=20,font=" 16").place(x=360,y=60)
        Label(self.root,text="Score : " + str(self.cscore),fg="green",font="Times 24").place(x=360,y=430)
        Label(self.root,text="Score : " + str(self.pscore),fg="green",font="Times 24").place(x=120,y=430)
        
        yy=50
        global var
        var=IntVar()
        for i in range(3):
            yy+=90
            Radiobutton(self.root,image=self.picl[i],bg="blue",relief=GROOVE,variable=var,value=i+1,command=self.winorloose).place(x=90,y=yy)
        yy=50
        for i in self.picr:
            yy+=90
            Label(self.root,image=i,relief=GROOVE,bg="#53868B").place(x=350,y=yy)
    
    def winorloose(self):
        for widgets in self.root.winfo_children():
            widgets.destroy()
        Label(self.root,text=name_var.get(),fg="white",bg="#0000FF",relief=GROOVE,padx=25,pady=10,font=" 15").place(x=135,y=60)
        Label(self.root,text="v/s",fg="red",font="Times 22").place(x=280,y=180)
        Label(self.root,text="Computer",fg="white",bg="#53868B",relief=GROOVE,pady=10,padx=20,font=" 16").place(x=360,y=60)
        val = var.get()
        Label(self.root,image=self.picl[val-1],bg="blue",relief=GROOVE).place(x=90,y=170)
        ran = random.choice(range(0,3))
        Label(self.root,image=self.picr[ran],relief=GROOVE,bg="#53868B").place(x=350,y=170)
        Button(self.root,text="Next round",bg="Pink",fg="black",activebackground="yellow",bd=4,pady=8,padx=12,command=self.game).place(x=255,y=270)
        if val==1 and ran==0:
            Label(self.root,text="Draw!",fg="green",font="Times 14").place(x=250,y=10)
        elif val==1 and ran ==1:
            Label(self.root,text="You win!",fg="green",font="Times 14").place(x=250,y=10)
            self.pscore+=1
        elif val==1 and ran==2:
            Label(self.root,text="You Loose!",fg="red",font="Times 14").place(x=250,y=10)
            self.cscore+=1
        elif val==2 and ran==0:
            Label(self.root,text="You Loose!",fg="red",font="Times 14").place(x=250,y=10)
            self.cscore+=1
        elif val==2 and ran==1:
            Label(self.root,text="Draw!",fg="green",font="Times 14").place(x=250,y=10)
        elif val==2 and ran==2:
            Label(self.root,text="You win!",fg="green",font="Times 14").place(x=250,y=10)
            self.pscore+=1
        elif val==3 and ran==0:  
            Label(self.root,text="You win!",fg="green",font="Times 14").place(x=250,y=10)
            self.pscore+=1
        elif val==3 and ran==1:
            Label(self.root,text="You Loose!",fg="red",font="Times 14").place(x=250,y=10)
            self.cscore+=1
        elif val==3 and ran==2:
            Label(self.root,text="Draw!",fg="green",font="Times 14").place(x=250,y=10)  
        self.draw()
        


    def mainloop(self):
        self.root.mainloop()
game = RockPaper()
game.mainloop()