from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class Report:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        #--------title-----
        title = Label(self.root, text="Display Result Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)
        
        self.setup_database()
        
        self.var_student = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmark = StringVar()
        self.var_per = StringVar()
        self.var_search = StringVar()
        self.roll_list = []
        self.load_roll_numbers()
        
        lbl_search = Label(self.root, text="Search Roll no", font=("goudy old style", 20, "bold"), bg="white").place(x=300, y=60)
        txt_student = ttk.Combobox(self.root, textvariable=self.var_student, values=self.roll_list, font=("goudy old style", 20, "bold"))
        txt_student.place(x=550, y=60, width=200)
        txt_student.set("Select ")
        txt_student.bind("<<ComboboxSelected>>", self.search)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=840, y=60, width=100, height=35)
        
        lbl_rollno = Label(self.root, text="Roll no", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=20, y=150, width=200, height=50)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=210, y=150, width=200, height=50)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=400, y=150, width=200, height=50)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=590, y=150, width=200, height=50)
        lbl_fullmark = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=780, y=150, width=200, height=50)
        lbl_per = Label(self.root, text="Percentage", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE).place(x=970, y=150, width=200, height=50)

        self.rollno = Label(self.root, text="", font=("goudy old style", 20, "bold"), bg="white", bd=2, relief=GROOVE)
        self.rollno.place(y=190, x=20, width=200, height=50)
        self.name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bd=2, relief=GROOVE)
        self.name.place(y=190, x=210, width=200, height=50)
        self.course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bd=2, relief=GROOVE)
        self.course.place(y=190, x=400, width=200, height=50)
        self.marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), bd=2, relief=GROOVE)
        self.marks.place(y=190, x=590, width=200, height=50)
        self.fullmark = Entry(self.root, textvariable=self.var_fullmark, font=("goudy old style", 20, "bold"), bd=2, relief=GROOVE)
        self.fullmark.place(y=190, x=780, width=200, height=50)
        self.per = Entry(self.root, textvariable=self.var_per, font=("goudy old style", 20, "bold"), bd=2, relief=GROOVE)
        self.per.place(y=190, x=970, width=200, height=50)

    def search(self, event=None):
      con = sqlite3.connect(database="rms.db")
      cur = con.cursor()
      try:
        search_roll = self.var_student.get().strip()
        print("Searching for roll:", search_roll)
        if search_roll == "" or search_roll == "Select ":
            messagebox.showerror("Error", "Roll no must be required")
            return
        cur.execute("SELECT * FROM result WHERE student=?", (search_roll,))
        row = cur.fetchone()
        print("DB row:", row)
        if row:
            self.rollno.config(text=self.var_student.get())  # Always show selected roll
            self.var_name.set(row[2])       # name
            self.var_course.set(row[3])     # course
            self.var_marks.set(row[4])      # marks
            self.var_fullmark.set(row[7])   # fullmark
            self.var_per.set(row[6])        # per
        else:
            messagebox.showerror("Error", "No record found")
      except Exception as e:
        messagebox.showerror("Error", f"Error due to : {str(e)}")
      finally:
        con.close()
    
    def setup_database(self):
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        try:
            # Check if 'fullmark' row exists in the 'Report' table
            cursor.execute("PRAGMA table_info(Report)")
            rows = [row[1] for row in cursor.fetchall()]
            
            if "fullmark" not in rows:
                cursor.execute("ALTER TABLE Report ADD row fullmark INTEGER")
                conn.commit()
                messagebox.showinfo("Database Update", "Added 'fullmark' row to the result table.")
        except Exception as e:
            messagebox.showerror("Database Error", f"Error checking/updating table: {e}")
        finally:
            conn.close()
        
    def load_roll_numbers(self):
        self.roll_list = ["Select "]
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT rollno FROM student")
            self.roll_list.extend([row[0] for row in cursor.fetchall()])
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load roll numbers: {e}")
        finally:
            conn.close()


          
    def clear(self):
        self.var_name.set("")
        self.var_student.set("")
        self.var_marks.set("")
        self.var_fullmark.set("")
        self.var_per.set("")
        self.var_course.set("")
        self.rollno.config(text="")

if __name__ == "__main__":
    root = Tk()
    obj = Report(root)
    root.mainloop()