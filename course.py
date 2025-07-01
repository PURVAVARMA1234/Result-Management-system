from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class CourseClass:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()

        #--------title-----
        title = Label(self.root, text="Manage Course Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        #=====Variables=====
        self.var_name = StringVar()
        self.var_duration = StringVar()
        self.var_charge = StringVar()

        #===Widgets===  
        lbl_name = Label(self.root, text="Course Name", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=60)
        lbl_duration = Label(self.root, text="Duration", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=100)
        lbl_charge = Label(self.root, text="Course Fee", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=140)
        lbl_description = Label(self.root, text="Description", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=180)

        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_name.place(x=180, y=60, width=200)
        self.txt_duration = Entry(self.root, textvariable=self.var_duration, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_duration.place(x=180, y=100, width=200)
        self.txt_charge = Entry(self.root, textvariable=self.var_charge, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_charge.place(x=180, y=140, width=200)
        self.txt_description = Text(self.root, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_description.place(x=180, y=180, width=400, height=70)

        #===Buttons===
        btn_submit = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add).place(x=100, y=400, width=110, height=40)
        btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update).place(x=220, y=400, width=110, height=40)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete).place(x=340, y=400, width=110, height=40)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=460, y=400, width=110, height=40)

        #=== search bar ===
        lbl_search = Label(self.root, text="Search Course", font=("goudy old style", 20, "bold"), bg="white").place(x=720, y=60)
        self.var_search = StringVar()
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20, "bold"), bg="light yellow").place(x=900, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search).place(x=1100, y=60, width=80)

        # === Course Table ===
        course_frame = Frame(self.root, bd=3, relief=RIDGE)
        course_frame.place(x=720, y=100, width=470, height=340)

        scroll_x = Scrollbar(course_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(course_frame, orient=VERTICAL)

        self.course_table = ttk.Treeview(course_frame, columns=("cid", "name", "duration", "charge", "description"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.course_table.xview)
        scroll_y.config(command=self.course_table.yview)

        self.course_table.heading("cid", text="Course ID")
        self.course_table.heading("name", text="Name")
        self.course_table.heading("duration", text="Duration")
        self.course_table.heading("charge", text="Course Fee")
        self.course_table.heading("description", text="Description")

        self.course_table["show"] = "headings"
        self.course_table.column("cid", width=100)
        self.course_table.column("name", width=150)
        self.course_table.column("duration", width=100)
        self.course_table.column("charge", width=100)
        self.course_table.column("description", width=200)
        self.course_table.bind("<ButtonRelease-1>", self.get_data)
        self.course_table.pack(fill=BOTH, expand=1)
        self.show()

    #==========================================
    def clear(self):
        self.var_name.set("")
        self.var_duration.set("")
        self.var_charge.set("")
        self.txt_description.delete("1.0", END)
        self.txt_name.config(state="normal")
        self.show()

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select a course from the list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM course WHERE name=?", (self.var_name.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Course deleted successfully", parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def get_data(self, ev):
        r = self.course_table.focus()
        content = self.course_table.item(r)
        row = content["values"]
        if not row:
            return
        self.var_name.set(row[1])
        self.var_duration.set(row[2])
        self.var_charge.set(row[3])
        self.txt_description.delete("1.0", END)
        self.txt_description.insert(END, row[4])
        self.txt_name.config(state="readonly")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This course already exists, try another", parent=self.root)
                else:
                    cur.execute("INSERT INTO course (name, duration, charge, description) VALUES (?, ?, ?, ?)",
                                (self.var_name.get(),
                                 self.var_duration.get(),
                                 self.var_charge.get(),
                                 self.txt_description.get("1.0", END).strip()))
                    con.commit()
                    messagebox.showinfo("Success", "Course added successfully", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_name.get() == "":
                messagebox.showerror("Error", "Course name should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM course WHERE name=?", (self.var_name.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Select course from list", parent=self.root)
                else:
                    cur.execute("UPDATE course SET duration=?, charge=?, description=? WHERE name=?",
                                (self.var_duration.get(),
                                 self.var_charge.get(),
                                 self.txt_description.get("1.0", END).strip(),
                                 self.var_name.get()))
                    con.commit()
                    messagebox.showinfo("Success", "Course updated successfully", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course WHERE name LIKE ?", ('%' + self.var_search.get() + '%',))
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM course")
            rows = cur.fetchall()
            self.course_table.delete(*self.course_table.get_children())
            for row in rows:
                self.course_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()
            
    import sqlite3

con = sqlite3.connect("rms.db")
cur = con.cursor()
try:
    cur.execute("ALTER TABLE course ADD COLUMN charge INTEGER")
    con.commit()
    print("Column 'charge' added successfully.")
except Exception as e:
    print(f"Error: {e}")
finally:
    con.close()

if __name__ == "__main__":
    root = Tk()
    obj = CourseClass(root)
    root.mainloop()