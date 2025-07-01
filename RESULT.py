import sqlite3
from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk

class Result:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        # Initialize database (fixes missing columns)
        self.setup_database()

        #--------title-----
        title = Label(self.root, text="Manage Result Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #=====Variables=====
        self.var_student = StringVar()
        self.var_name = StringVar()
        self.var_course = StringVar()
        self.var_marks = StringVar()
        self.var_fullmark = StringVar()
        self.roll_list = []
        self.load_roll_numbers()

        #===Widgets===  
        lbl_student = Label(self.root, text=" Select Student", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=70)
        lbl_name = Label(self.root, text="Name", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=130)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=190)
        lbl_marks = Label(self.root, text="Marks Obtained", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=250)
        lbl_fullmark = Label(self.root, text="Full Marks", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=310)

        txt_student = ttk.Combobox(self.root, textvariable=self.var_student, values=self.roll_list, font=("goudy old style", 20, "bold"))
        txt_student.place(x=200, y=70, width=200)
        txt_student.set("Select ")
        txt_student.bind("<<ComboboxSelected>>", self.search)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_name.place(x=200, y=130, width=200)
        self.txt_course = Entry(self.root, textvariable=self.var_course, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_course.place(x=200, y=190, width=200)
        self.txt_marks = Entry(self.root, textvariable=self.var_marks, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_marks.place(x=200, y=250, width=200)
        self.txt_fullmark = Entry(self.root, textvariable=self.var_fullmark, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_fullmark.place(x=200, y=310, width=200)

        #===Buttons===
        btn_submit = Button(self.root, text="Submit", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=350, y=400, width=110, height=40)

        self.bg_img = Image.open("image/images/result.jpg")
        self.bg_img = self.bg_img.resize((550, 450), Image.Resampling.LANCZOS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)
        self.lbl_bg = Label(self.root, image=self.bg_img).place(x=600, y=70, width=550, height=390)

    def setup_database(self):
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        try:
            # Check if 'fullmark' column exists in the 'result' table
            cursor.execute("PRAGMA table_info(result)")
            columns = [column[1] for column in cursor.fetchall()]
            
            if "fullmark" not in columns:
                cursor.execute("ALTER TABLE result ADD COLUMN fullmark INTEGER")
                conn.commit()
                messagebox.showinfo("Database Update", "Added 'fullmark' column to the result table.")
        except Exception as e:
            messagebox.showerror("Database Error", f"Error checking/updating table: {e}")
        finally:
            conn.close()

    def clear(self):
        self.var_student.set("Select ")
        self.var_name.set("")
        self.var_course.set("")
        self.var_marks.set("")
        self.var_fullmark.set("")

    def add(self):
        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        try:
            if not all([
                self.var_student.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_marks.get(),
                self.var_fullmark.get()
            ]):
                messagebox.showerror("Error", "All fields are required!", parent=self.root)
                return

            # Calculate percentage
            per = (int(self.var_marks.get()) / int(self.var_fullmark.get())) * 100

            cursor.execute("""
                INSERT INTO result 
                (student, name, course, marks, fullmark, per) 
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                self.var_student.get(),
                self.var_name.get(),
                self.var_course.get(),
                self.var_marks.get(),
                self.var_fullmark.get(),
                per
            ))
            
            conn.commit()
            messagebox.showinfo("Success", "Result added successfully!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)
        finally:
            conn.close()

    def search(self, event=None):
        rollno = self.var_student.get()
        if not rollno or rollno == "Select ":
            return

        conn = sqlite3.connect("rms.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT name, course FROM student WHERE rollno=?", (rollno,))
            row = cursor.fetchone()
            if row:
                self.var_name.set(row[0])
                self.var_course.set(row[1])
            else:
                messagebox.showerror("Error", "Student not found!", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Database Error: {e}", parent=self.root)
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

if __name__ == "__main__":
    root = Tk()
    obj = Result(root)
    root.mainloop()
