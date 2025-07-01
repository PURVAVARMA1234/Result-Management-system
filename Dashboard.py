from tkinter import *
from PIL import Image, ImageTk
from course import CourseClass
from Student import student
from RESULT import Result
from tkinter import messagebox
from REPORT import Report
import os 
import sqlite3
# === IMPORTS ===
class RMS:
        
    def __init__(self,root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
# === ICON===
        self.logo_dash= ImageTk.PhotoImage(file ="image/images/logo_p.png")
#--------title-----
        title = Label(self.root, text="Student Result Management System",padx=20,compound=LEFT ,image = self.logo_dash,font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place( x=0, y=0, relwidth=1, height=50)
   #====MENU BAR====
        M_frame = LabelFrame(self.root,text= "Menu", font=("goudy old style", 15, "bold","italic"), bg="white")
        M_frame.place(x=60, y=50, width=300, height=630)  
        
        #===MENU BUTTONS===
        btn_course = Button(M_frame, text="Course", font=("goudy old style",20 , "bold"), bg="#0b5377", fg="white", cursor="hand2",command = self.add_course).place(x=10, y=40, width=280, height=70)
        btn_student = Button(M_frame, text="Student", font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white", cursor="hand2", command = self.add_student).place(x=10, y=130, width=280, height=70)
        btn_result = Button(M_frame, text="Result", font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white", cursor="hand2", command = self.add_result).place(x=10, y=220, width=280, height=70)
        btn_view = Button(M_frame, text="View Result", font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white", cursor="hand2", command = self.add_report).place(x=10, y=310, width=280, height=70)
        btn_logout = Button(M_frame ,text ="Logout", font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white", cursor="hand2", command = self.logout).place(x=10, y=400, width=280, height=70)
        btn_exit = Button(M_frame, text="Exit", font=("goudy old style", 20, "bold"), bg="#0b5377", fg="white", cursor="hand2", command = self.exit).place(x=10, y=490, width=280, height=70)
        
        #=== Content window=====
        self.bg_img = Image.open("image/images/bg.png")
        self.bg_img = self.bg_img.resize((920,350),Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=400, y=120, width=920, height=350)
        
        #==== update label===
        self.lbl_course = Label(self.root, text="Total Course\n[0]", font=("goudy old style", 20, "bold"), bg="#e43b06", fg="white",cursor="hand2",relief=RIDGE,bd = 10)
        self.lbl_course.place(x = 400,y=500, width=270, height=150)
        self.lbl_student = Label(self.root, text="Total Student\n[0]", font=("goudy old style", 20, "bold"), bg="#0676ad", fg="white",cursor="hand2" ,relief=RIDGE,bd = 10)
        self.lbl_student.place(x = 725,y=500, width=270, height=150)
        self.lbl_result = Label(self.root, text="Total result\n[0]", font=("goudy old style", 20, "bold"), bg="#038074", fg="white",cursor="hand2",relief=RIDGE,bd = 10)
        self.lbl_result.place(x = 1050,y=500, width=270, height=150)
          
        self.update_details()
        
# === ADD COURSE ===
    def add_course(self):
        self.new_window = Toplevel(self.root)
        self.app = CourseClass(self.new_window)
        
# === Add Student ===
    def add_student(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)
        
# === Add Result ===
    def add_result(self):
        self.new_window = Toplevel(self.root)
        self.app = Result(self.new_window)
        
# === Add Report ===
    def add_report(self):
        self.new_window = Toplevel(self.root)
        self.app = Report(self)  
          
# === Footer ===      
        footer = Label(self.root, text=" SRMS-Student Result Management System" ,font=("goudy old style", 12, "bold"), bg="#262626", fg="white").pack( side =BOTTOM, fill = X)
 
    def update_details(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
         cur.execute("SELECT * FROM course")
         cr =cur.fetchall()
         self.lbl_course.config(text = f"Total Course\n[{len(cr)}]")
         self.lbl_student.config(text = f"Total Student\n[{len(cr)}]")
         self.lbl_result.config(text = f"Total Result\n[{len(cr)}]")
         cur.execute("SELECT * FROM student")
         st =cur.fetchall()
         
        except Exception as ex:
            messagebox.showerror("error", f"Error due to {str(ex)}", parent=self.root)
       
 
 # === Add Course Button === 
    def add_course(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = CourseClass(self.new_win) 
        
    def add_student(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = student(self.new_win)     
        
    def add_result(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Result(self.new_win)
        
    def add_report(self):
        self.new_win = Toplevel(self.root)
        self.new_obj = Report(self.new_win)
        
    def logout(self):
        op = messagebox.askyesno("Confirm", "Do you want to logout?")
        if op == True:
            self.root.destroy()
            os.system("python register.py")
            
    def exit(self):
        op = messagebox.askyesno("Confirm", "Do you want to exit?")
        if op == True:
            self.root.destroy()
              
if __name__ == "__main__":
    root = Tk()
    obj = RMS(root)
    root.mainloop()
