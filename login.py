from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox


def main():
    win=Tk()
    app=Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Load background image
        try:
            self.bg = ImageTk.PhotoImage(file=r"c:\Users\user\Downloads\gallery-8-2.jpg")
        except Exception as e:
            messagebox.showerror("Error", f"Error loading background image: {e}")
            print(f"Error loading background image: {e}")
            return

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Load and resize the logo image
        try:
            img1 = Image.open(r"c:\foto\logo.jpg")
            img1 = img1.resize((100, 100), Image.Resampling.LANCZOS)
            self.PhotoImage1 = ImageTk.PhotoImage(img1)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading logo image: {e}")
            print(f"Error loading logo image: {e}")
            return

        lblimg1 = Label(image=self.PhotoImage1, bg="black", borderwidth=0)
        lblimg1.place(x=730, y=175, width=100, height=100)

        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=100)

        # Username Label
        username = Label(frame, text="Username", font=("times new roman", 20, "bold"), fg="white", bg="black")
        username.place(x=70, y=155)

        self.txtuser = ttk.Entry(frame, font=("times new roman", 20, "bold"))
        self.txtuser.place(x=40, y=185, width=270)

        # Password Label
        password = Label(frame, text="Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        password.place(x=70, y=225)

        self.txtpass = ttk.Entry(frame, font=("times new roman", 20, "bold"), show='*')
        self.txtpass.place(x=40, y=255, width=270)

        # Icon Images
        try:
            img2 = Image.open(r"c:\foto\logo.jpg")
            img2 = img2.resize((25, 25), Image.Resampling.LANCZOS)
            self.PhotoImage2 = ImageTk.PhotoImage(img2)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading icon image 2: {e}")
            print(f"Error loading icon image 2: {e}")
            return

        lblimg2 = Label(image=self.PhotoImage2, bg="black", borderwidth=0)
        lblimg2.place(x=650, y=323, width=25, height=25)

        try:
            img3 = Image.open(r"c:\foto\logo.jpg")
            img3 = img3.resize((25, 25), Image.Resampling.LANCZOS)
            self.PhotoImage3 = ImageTk.PhotoImage(img3)
        except Exception as e:
            messagebox.showerror("Error", f"Error loading icon image 3: {e}")
            print(f"Error loading icon image 3: {e}")
            return

        lblimg3 = Label(image=self.PhotoImage3, bg="black", borderwidth=0)
        lblimg3.place(x=650, y=395, width=25, height=25)

        # Login Button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=300, width=120, height=35)

        # Register Button
        registerbtn = Button(frame, text="New User Register",command=self.register_window,font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=350, width=160)

        # Forget Password Button
        forgetbtn = Button(frame, text="Forget Password", font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgetbtn.place(x=10, y=370, width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register( self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to Sukro")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="loginregister")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from register where email=%$ and password=%$",(
                                                                                        self.txtuser.get(),
                                                                                        self.textpass.get()
                                                                                        
                                                                          ))
            row=my_cursor.fetchone()
            if row!=None:
                messagebox.showerror("Error,","Invalid Username & password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.new_window)
                    self.app=


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        # ==================Variables===================
        self.var_faname = StringVar()
        self.var_Iname = StringVar()
        self.var_Contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # =============BG IMAGE=================
        self.bg = ImageTk.PhotoImage(file="wallpaper.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # =============left IMAGE=================
        self.bg1 = ImageTk.PhotoImage(file="leftwallpaper1.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # ==========main frame =====================
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="darkgreen", bg="white")
        register_lbl.place(x=20, y=20)

        # ===============label entry==============

        # --------row1
        fname = Label(frame, text="First Name", font=("times new roman", 20, "bold"), bg="white")
        fname.place(x=50, y=100)

        self.faname_entry = ttk.Entry(frame, textvariable=self.var_faname, font=("times new roman", 15, "bold"))
        self.faname_entry.place(x=50, y=130, width=250)

        l_name = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        l_name.place(x=370, y=100)

        self.txt_lname = ttk.Entry(frame, textvariable=self.var_Iname, font=("times new roman,", 15))
        self.txt_lname.place(x=370, y=130, width=250)

        # ---------row2
        contact = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)

        self.txt_contact = ttk.Entry(frame, textvariable=self.var_Contact, font=("times new roman", 15))
        self.txt_contact.place(x=50, y=200, width=250)

        email = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)

        self.txt_email = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15))
        self.txt_email.place(x=370, y=200, width=250)

        # -----------row3
        security_Q = Label(frame, text="Select Security Questions", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_Q.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state="readonly")
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Girlfriend name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        security_A.place(x=370, y=240)

        self.txt_security = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15))
        self.txt_security.place(x=370, y=270, width=250)

        # ------- row4
        pswd = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        pswd.place(x=50, y=310)

        self.txt_pswd = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15), show='*')
        self.txt_pswd.place(x=50, y=340, width=250)

        confirm_pswd = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confirm_pswd.place(x=370, y=310)

        self.txt_confirm_pswd = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15), show='*')
        self.txt_confirm_pswd.place(x=370, y=340, width=250)

        # ================check button==========
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I Agree The Terms & Conditions", font=("times new roman", 12, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # =============buttons===================
        img = Image.open("register.png")
        img = img.resize((100, 100), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, image=self.photoimage, command=self.register_data, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b1.place(x=10, y=420, width=200)

        img1 = Image.open("login.jpg")
        img1 = img1.resize((200, 50), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2", font=("times new roman", 15, "bold"))
        b2.place(x=330, y=420, width=200)

    # ===========================Function Declaration=========================
    def register_data(self):
        print("Register button clicked")
        if self.var_faname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            print("Some fields are empty")
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            print("Passwords do not match")
            messagebox.showerror("Error", "Password & confirm password must be same")
        elif self.var_check.get() == 0:
            print("Terms and conditions not agreed")
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="", database="loginregister")
                my_cursor = conn.cursor()
                query = ("select * from register where email=%s")
                value = (self.var_email.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row != None:
                    print("User already exists")
                    messagebox.showerror("Error", "User already exists, please try another email")
                else:
                    my_cursor.execute("insert into register values(%s, %s, %s, %s, %s, %s, %s)", (
                        self.var_faname.get(),
                        self.var_Iname.get(),
                        self.var_Contact.get(),
                        self.var_email.get(),
                        self.var_securityQ.get(),
                        self.var_securityA.get(),
                        self.var_pass.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Registered Successfully")
            except Exception as es:
                print(f"Error due to: {str(es)}")
                messagebox.showerror("Error", f"Error due to: {str(es)}")




if __name__ == "__main__":
   main()
