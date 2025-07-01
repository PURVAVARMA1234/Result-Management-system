from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3
import os

class LoginPage:
    def __init__(self, window):
        self.window = window
        self.window.geometry('1166x718')
        self.window.resizable(0, 0)
        self.window.state('zoomed')
        self.window.title('Login Page')

        # Load the background image
        self.bg_frame = Image.open('images\\background1.png')
        self.photo_bg = ImageTk.PhotoImage(self.bg_frame)
        self.bg_panel = Label(self.window, image=self.photo_bg)
        self.bg_panel.image = self.photo_bg
        self.bg_panel.pack(fill='both', expand='yes')

        # Frame tracking
        self.frames = {
            "login": None,
            "register": None,
            "reset_password": None
        }

        self.show_login_frame()

    def show_login_frame(self):
        self.clear_frame()
        self.lgn_frame = Frame(self.window, bg="#F6F6F8")
        self.lgn_frame.place(x=300, y=120, width=950, height=600)
        self.frames['login'] = self.lgn_frame

        # Side image (vector.png)
        side_image = Image.open('images\\vector.png')
        photo1 = ImageTk.PhotoImage(side_image)
        side_image_label = Label(self.lgn_frame, image=photo1, bg='#F6F6F8')
        side_image_label.image = photo1
        side_image_label.place(x=5, y=100)

        # Sign in image (hyy.png)
        sign_in_image = Image.open('images\\hyy.png')
        photo2 = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(self.lgn_frame, image=photo2, bg='#F6F6F8')
        sign_in_image_label.image = photo2
        sign_in_image_label.place(x=620, y=130)

        self.add_login_widgets()

    def add_login_widgets(self):
        self.heading = Label(self.lgn_frame, text="WELCOME", font=('yu gothic ui', 25, "bold"), bg="#F6F6F8", fg='black')
        self.heading.place(x=80, y=30, width=300, height=30)

        # Username
        Label(self.lgn_frame, text="Username", bg="#F6F6F8", fg="#033B72", font=("yu gothic ui", 15, "bold")).place(x=550, y=250)
        self.username_entry = Entry(self.lgn_frame, highlightthickness=0, bg="#A1DDFA", fg="#033B72", font=("yu gothic ui ", 12, "bold"))
        self.username_entry.place(x=580, y=300,  height = 30, width =300)

        # Password
        Label(self.lgn_frame, text="Password", bg="#F6F6F8", fg="#033B72", font=("yu gothic ui", 15, "bold")).place(x=550, y=350)
        self.password_entry = Entry(self.lgn_frame, highlightthickness=0, bg="#A1DDFA", fg="#033B72", font=("yu gothic ui", 12, "bold"), show="*")
        self.password_entry.place(x=580, y=400, height = 30, width =300)

        # Login button
        Button(self.lgn_frame, text='LOGIN', command=self.handle_login, font=("yu gothic ui", 13, "bold"), width=18, bg='#A1DDFA', fg='#033B72').place(x=620, y=450)

        # Forgot Password button
        Button(self.lgn_frame, text="Forgot Password?", command=self.show_reset_password_frame, font=("yu gothic ui", 10, "bold underline"), bg='#A1DDFA', fg='#033B72').place(x=550, y=500)
        
        # Register button
        Button(self.lgn_frame, text="Don't have an account? Register", command=self.show_register_frame, font=("yu gothic ui", 10, "bold"), bg='#A1DDFA', fg='#033B72').place(x=690, y=500)

    def show_register_frame(self):
        self.clear_frame()
        self.reg_frame = Frame(self.window, bg='#F6F6F8')
        self.reg_frame.place(x=300, y=120, width=950, height=600)
        self.frames['register'] = self.reg_frame

        # Side image (vector.png)
        side_image = Image.open('images\\vector.png')
        photo1 = ImageTk.PhotoImage(side_image)
        side_image_label = Label(self.reg_frame, image=photo1, bg='#F6F6F8')
        side_image_label.image = photo1
        side_image_label.place(x=5, y=100)

        title = Label(self.reg_frame, text="Register", font=("yu gothic ui", 25, "bold"), bg="#F6F6F8", fg='#033B72')
        title.pack(pady=20)
        title.place(x=620, y=50)

        Label(self.reg_frame, text="Email", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place(x= 560 ,y=120)
        self.reg_email = Entry(self.reg_frame)
        self.reg_email.pack(pady=5)
        self.reg_email.place( x= 560 , y= 150, height = 30, width =300 )

        Label(self.reg_frame, text="Username", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place (x = 560, y= 200)
        self.reg_username = Entry(self.reg_frame)
        self.reg_username.pack(pady=5)
        self.reg_username.place( x = 560, y = 230, height = 30, width =300 )

        Label(self.reg_frame, text="Password", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place(x = 560, y= 280)
        self.reg_password = Entry(self.reg_frame, show="*")
        self.reg_password.pack(pady=5)
        self.reg_password.place(x = 560 , y = 310 , height = 30, width =300 )

        Label(self.reg_frame, text="Confirm Password", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place(x = 560, y= 370)
        self.reg_confirm = Entry(self.reg_frame, show="*")
        self.reg_confirm.pack(pady=5)
        self.reg_confirm.place(x = 560 , y = 400 , height = 30 , width =300)

        Button(self.reg_frame, text="Register", command=self.handle_register, bg="#A1DDFA", fg="#033B72", font=("yu gothic ui", 15)).place(x=570, y=450, width=130, height=40)
        Button(self.reg_frame, text="Back", command=self.show_login_frame, bg="#A1DDFA", fg="#033B72", font=("yu gothic ui", 15) ).place(x=730, y=450, width=130, height=40)

    def show_reset_password_frame(self):
        self.clear_frame()
        self.reset_frame = Frame(self.window, bg='#F6F6F8')
        self.reset_frame.place(x=300, y=120, width=950, height=600)
        self.frames['reset_password'] = self.reset_frame

        # Side image (vector.png)
        side_image = Image.open('images\\vector.png')
        photo1 = ImageTk.PhotoImage(side_image)
        side_image_label = Label(self.reset_frame, image=photo1, bg='#F6F6F8')
        side_image_label.image = photo1
        side_image_label.place(x=5, y=100)

        # Sign in image (hyy.png)
        sign_in_image = Image.open('images\\reset-removebg-preview.png')
        photo2 = ImageTk.PhotoImage(sign_in_image)
        sign_in_image_label = Label(self.reset_frame, image=photo2, bg='#F6F6F8')
        sign_in_image_label.image = photo2
        sign_in_image_label.place(x=640, y=50)

        title = Label(self.reset_frame, text="Reset Password", font=("yu gothic ui", 25, "bold"), bg="#F6F6F8", fg='#033B72')
        title.pack(pady=20)
        title.place(x=600, y=180)

        Label(self.reset_frame, text="Email", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place(x= 560 ,y=240)
        self.reset_email = Entry(self.reset_frame)
        self.reset_email.pack(pady=5)
        self.reset_email.place(x=560, y=270, height=30, width=300)

        Label(self.reset_frame, text="New Password", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place (x = 560, y= 320)
        self.reset_password = Entry(self.reset_frame, show="*")
        self.reset_password.pack(pady=5)
        self.reset_password.place(x=560, y=350, height=30, width=300)

        Label(self.reset_frame, text="Confirm Password", bg="#A1DDFA", font=("yu gothic ui", 15), fg="#033B72").place(x=560, y=400)
        self.reset_confirm = Entry(self.reset_frame, show="*")
        self.reset_confirm.pack(pady=5)
        self.reset_confirm.place(x=560, y=430, height=30, width=300)

        Button(self.reset_frame, text="Reset Password", command=self.handle_reset_password, font=("yu gothic ui", 15), bg="#A1DDFA", fg="#033B72").place(x=570, y=480, width=150, height=40)
        Button(self.reset_frame, text="Back", command=self.show_login_frame, font=("yu gothic ui", 15), bg="#A1DDFA", fg="#033B72").place(x=730, y=480, width=130, height=40)

    def clear_frame(self):
        if self.frames['login']:
            self.frames['login'].place_forget()
        if self.frames['register']:
            self.frames['register'].place_forget()
        if self.frames['reset_password']:
            self.frames['reset_password'].place_forget()

    import sqlite3
# ...existing code...

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
            row = cur.fetchone()
            con.close()
            if row:
                messagebox.showinfo("Login", "Login successful!")
                os.system("python dashboard.py")
            else:
                messagebox.showerror("Error", "Invalid username or password.")
                
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def handle_register(self):
        email = self.reg_email.get()
        username = self.reg_username.get()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()

        if password != confirm:
            messagebox.showerror("Error", "Passwords don't match.")
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", (username, email, password))
            con.commit()
            con.close()
            messagebox.showinfo("Registration", "Registration successful!")
            self.show_login_frame()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username or Email already exists.")
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

    def handle_reset_password(self):
        email = self.reset_email.get()
        new_password = self.reset_password.get()
        confirm = self.reset_confirm.get()

        if new_password != confirm:
            messagebox.showerror("Error", "Passwords don't match.")
            return

        try:
            con = sqlite3.connect("rms.db")
            cur = con.cursor()
            cur.execute("SELECT * FROM users WHERE email=?", (email,))
            if cur.fetchone():
                cur.execute("UPDATE users SET password=? WHERE email=?", (new_password, email))
                con.commit()
                messagebox.showinfo("Reset Password", "Password reset successful!")
                self.show_login_frame()
            else:
                messagebox.showerror("Error", "Email not found.")
            con.close()
        except Exception as e:
            messagebox.showerror("Error", f"Database error: {e}")

def page():
    window = Tk()
    LoginPage(window)
    window.mainloop()

if __name__ == '__main__':
    page()