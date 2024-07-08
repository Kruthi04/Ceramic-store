import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk

class FirstPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image = photo)
        label.image=photo
        label.place(x=0,y=0)

        border=tk.LabelFrame(self,text="Login",bg="ivory", bd=10, font=("Arial",20))
        border.pack(fill="both",expand="yes",padx=150,pady=150)

        L1=tk.Label(border,text="Username",bg="ivory",font=("Arial Bold",15))
        L1.place(x=50,y=20)
        T1= tk.Entry(border,width=30,bd=5)
        T1.place(x=180, y=20)

        L1 = tk.Label(border, text="password",bg="ivory", font=("Arial Bold", 15))
        L1.place(x=50, y=80)
        T2 = tk.Entry(border, width=30,show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:
                with open("credential.txt","r") as f:
                    info= f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get(): # .strip will remove the space provided before and after the username and passwword
                            controller.show_frame(HomePage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)

        def register():
            window=tk.Tk()
            window.resizable(0,0)    # to remove maximizze button
            window.configure(bg="ivory")  #background color of the window
            window.title("Register to BookEasy")
            #p2 = tk.PhotoImage(file='vase.png')
            #window.iconphoto(False, p2)
            tk.Label(window, text="Fill details for registration", bg="ivory", fg="black", font=90).place(x=100,y=6)
            l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="ivory")
            l1.place(x=10, y=50)
            t1 = tk.Entry(window,width=30,bd=5)
            t1.place(x=200,y=50)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15),bg="ivory")
            l2.place(x=10, y=100)
            t2 = tk.Entry(window, width=30, show="*",bd=5)
            t2.place(x=200, y=100)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="ivory")
            l3.place(x=10,y=150)
            t3 = tk.Entry(window, width=30,show="*", bd=5)
            t3.place(x=200, y=150)

            def check():
                 if t1.get()!="" or t2.get()!="" or t3.get()!="":
                     if t2.get()== t3.get():
                         with open("credential.txt","a") as f:
                             f.write(t1.get()+","+t2.get()+"\n")
                             messagebox.showinfo("Welcome","You have registered successfully!")
                     else:
                         messagebox.showinfo("Error","Your password didnt match")
                 else:
                     messagebox.showinfo("Error","Please fill the complete field")
            b1=tk.Button(window, text="Register to BookEasy",bg="dark orange", font=("Arial" , 15), command=check)
            b1.place(x=170,y=200)
            window.geometry("470x270")   #for entry to execute
            window.mainloop()

        B2 = tk.Button(self, text="Register",bg="dark orange", font=("Arial", 15),command=register)
        B2.place(x=670, y=50)
        lb1 = tk.Label(self, text="Welcome to AtoZ Ceramics", bg="light yellow", fg="black", font=("Arial", 20),
                    height=2, width=30)
        lb1.place(x=155,y=40)

class HomePage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)

        load = Image.open("wallpaper.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        tk.Label(self, text="Welcome to AtoZ Ceramics", bg="light yellow", fg="black", font=("Arial",20), height=2, width=30).place(x=145, y=60)
        tk.Button(self, text="Home", bg="light gray", fg="black", font=("Arial",15), height=2, width=10,command=lambda: controller.show_frame(HomePage)).place(x=80,y=180)
        tk.Button(self, text="About us", bg="lightgray", fg="black", font=("Arial",15), height=2, width=10,command=lambda: controller.show_frame(AboutUsPage)).place(x=250,y=180)
        tk.Button(self, text="Shop All", bg="light gray", fg="black", font=("Arial",15), height=2, width=10,command=lambda: controller.show_frame(ShopAllPage)).place(x=420,y=180)
        tk.Button(self, text="Category", bg="lightgray", fg="black", font=("Arial",15), height=2, width=10,command=lambda: controller.show_frame(CategoryPage)).place(x=590, y=180)


       # Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        #Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)

class CategoryPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="beige")

        load = Image.open("category.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)


        lb1 = tk.Label(self, text="Category", fg="black", font=("Arial", 30), height=2)
        lb1.place(x=270, y=2)

        load = Image.open("bathroomCeramics2.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=70, y=80)
        bathButton = tk.Button(self, text="Bathroom ceramics",bg="ivory", width=30, height=1, )
        bathButton.place(x=80, y=240)
        HomeButton = tk.Button(self, text="Home",bg="ivory", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        HomeButton.place(x=70, y=10)

        load = Image.open("home_decor.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=400, y=85)
        homeDecorButton = tk.Button(self, text="Home decor",bg="ivory", width=28, height=1)
        homeDecorButton.place(x=480, y=240)

        load = Image.open("kitchen11.png")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=290, y=290)
        tk.Button(self, text="Kitchen ceramics",bg="ivory", width=28, height=1).place(x=275, y=450)

        #Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        #Button.place(x=100, y=450)

class AboutUsPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="ivory")

        l2 = tk.Label(self, text="About us", font=("Arial", 15), bg="ivory")
        l2.place(x=10, y=100)

        Button = tk.Button(self, text="Home",bg="ivory", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=650, y=450)

class ShopAllPage(tk.Frame):
    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.configure(bg="ivory")
        l2 = tk.Label(self, text="Shop all", font=("Arial", 15), bg="ivory")
        l2.place(x=10, y=100)

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(HomePage))
        Button.place(x=650, y=450)

class Application(tk.Tk):
    def __init__(self,*args, **kwargs):
        tk.Tk.__init__(self,*args,**kwargs)
        window=tk.Frame(self)
        window.pack()
       # p1 = tk.PhotoImage(file='vase.png')
        #screen1.iconphoto(False, p1)

        window.grid_rowconfigure(0,minsize=500)
        window.grid_columnconfigure(0,minsize=800)

        self.frames= {}
        for F in (FirstPage,HomePage,CategoryPage,AboutUsPage,ShopAllPage):
            frame= F(window, self)
            self.frames[F]=frame
            frame.grid(row=0,column=0, sticky="nsew")
            self.title('BookEasy')
            p1 = tk.PhotoImage(file='vase.png')
            self.iconphoto(False, p1)

        self.show_frame(FirstPage)

    def show_frame(self,page):
            frame = self.frames[page]
            frame.tkraise()
app= Application()
app.maxsize(850,550)
app.mainloop()

