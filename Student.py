from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import sqlite3

class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Result Management System")
        self.root.geometry("1200x480+80+170")
        self.root.config(bg="white")
        self.root.focus_force()
        
        title = Label(self.root, text="Manage Student Details", font=("goudy old style", 20, "bold"), bg="#033054", fg="white").place(x=0, y=0, relwidth=1, height=50)

        # Variables
        self.var_name = StringVar()
        self.var_rollno = StringVar()
        self.var_email = StringVar()
        self.var_state = StringVar()
        self.var_city = StringVar()
        self.var_pincode = StringVar()
        self.var_contact = StringVar()
        self.var_DOB = StringVar()
        self.var_date = StringVar()
        self.var_gender = StringVar()
        self.var_course = StringVar()
        self.course_list = []
        self.load_data()

        # Widgets
        lbl_name = Label(self.root, text=" Name", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=60)
        lbl_rollno = Label(self.root, text="Roll No", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=110)
        lbl_email = Label(self.root, text="Email", font=("goudy old style", 20, "bold"), bg="white").place(x=400, y=110)
        lbl_state = Label(self.root, text="State", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=160)
        lbl_city = Label(self.root, text="City", font=("goudy old style", 20, "bold"), bg="white").place(x=250, y=160)
        lbl_pincode = Label(self.root, text="Pincode", font=("goudy old style", 20, "bold"), bg="white").place(x=470, y=160)
        lbl_contact = Label(self.root, text="Contact", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=260)
        lbl_DOB = Label(self.root, text="DOB", font=("goudy old style", 20, "bold"), bg="white").place(x=400, y=60)
        lbl_address = Label(self.root, text="Address", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=310)
        lbl_date = Label(self.root, text="Admission date", font=("goudy old style", 20, "bold"), bg="white").place(x=320, y=260)
        lbl_gender = Label(self.root, text="Gender", font=("goudy old style", 20, "bold"), bg="white").place(x=10, y=210)
        lbl_course = Label(self.root, text="Course", font=("goudy old style", 20, "bold"), bg="white").place(x=370, y=210)

       
        self.txt_name = Entry(self.root, textvariable=self.var_name, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_name.place(x=120, y=60, width=200)
        self.txt_DOB = Entry(self.root, textvariable=self.var_DOB, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_DOB.place(x=500, y=60, width=200)
        self.txt_rollno = Entry(self.root, textvariable=self.var_rollno, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_rollno.place(x=180, y=110, width=200)
        txt_gender = ttk.Combobox(self.root, textvariable=self.var_gender, font=("goudy old style", 20, "bold"))
        txt_gender["values"] = ("Male", "Female", "Other")
        txt_gender.place(x=120, y=210, width=200)
        txt_gender.current(0)
        self.txt_email = Entry(self.root, textvariable=self.var_email, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_email.place(x=500, y=110, width=200)
        self.txt_state = Entry(self.root, textvariable=self.var_state, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_state.place(x=100, y=160, width=120)
        txt_course = ttk.Combobox(self.root, textvariable=self.var_course, values=self.course_list, font=("goudy old style", 20, "bold"))
        txt_course.place(x=500, y=210, width=200)
        self.txt_city = Entry(self.root, textvariable=self.var_city, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_city.place(x=330, y=160, width=120)
        self.txt_pincode = Entry(self.root, textvariable=self.var_pincode, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_pincode.place(x=580, y=160, width=120)
        self.txt_contact = Entry(self.root, textvariable=self.var_contact, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_contact.place(x=120, y=260, width=200)
        self.txt_date = Entry(self.root, textvariable=self.var_date, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_date.place(x=500, y=260, width=200)

        self.txt_address = Text(self.root, font=("goudy old style", 20, "bold"), bg="light yellow")
        self.txt_address.place(x=150, y=310, width=550, height=70)

        # Buttons
        btn_add = Button(self.root, text="Save", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.add).place(x=150, y=400, width=110, height=40)
        btn_update = Button(self.root, text="Update", font=("goudy old style", 15, "bold"), bg="#4caf50", fg="white", cursor="hand2", command=self.update).place(x=270, y=400, width=110, height=40)
        btn_delete = Button(self.root, text="Delete", font=("goudy old style", 15, "bold"), bg="#f44336", fg="white", cursor="hand2", command=self.delete).place(x=390, y=400, width=110, height=40)
        btn_clear = Button(self.root, text="Clear", font=("goudy old style", 15, "bold"), bg="#607d8b", fg="white", cursor="hand2", command=self.clear).place(x=510, y=400, width=110, height=40)

        # Search bar
        lbl_search = Label(self.root, text="Search Roll no", font=("goudy old style", 20, "bold"), bg="white").place(x=720, y=60)
        self.var_search = StringVar()
        txt_search = Entry(self.root, textvariable=self.var_search, font=("goudy old style", 20, "bold"), bg="light yellow").place(x=800, y=60, width=180)
        btn_search = Button(self.root, text="Search", font=("goudy old style", 15, "bold"), bg="#2196f3", fg="white", cursor="hand2", command=self.search).place(x=1050, y=60, width=80)

        # Table
        course_frame = Frame(self.root, bd=3, relief=RIDGE)
        course_frame.place(x=720, y=100, width=470, height=340)
        scroll_x = Scrollbar(course_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(course_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(course_frame, columns=("rollno", "name", "email", "state", "city", "DOB", "pincode", "gender", "course", "address", "date", "contact"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("name", text="Name")
        self.student_table.heading("rollno", text="Roll no")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("state", text="State")
        self.student_table.heading("city", text="City")
        self.student_table.heading("DOB", text="DOB")
        self.student_table.heading("pincode", text="Pincode")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("date", text="Admission date")
        self.student_table.heading("contact", text="Contact")

        self.student_table["show"] = "headings"
        self.student_table.column("rollno", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("email", width=100)
        self.student_table.column("DOB", width=100)
        self.student_table.column("state", width=100)
        self.student_table.column("city", width=100)
        self.student_table.column("pincode", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("address", width=200)
        self.student_table.column("date", width=100)
        self.student_table.column("contact", width=100)
        self.student_table.bind("<ButtonRelease-1>", self.get_data)
        self.student_table.pack(fill=BOTH, expand=1)

        self.show()

    def clear(self):
        self.var_name.set("")
        self.var_rollno.set("")
        self.var_email.set("")
        self.var_state.set("")
        self.var_city.set("")
        self.var_pincode.set("")
        self.var_contact.set("")
        self.var_DOB.set("")
        self.var_date.set("")
        self.var_gender.set("")
        self.var_course.set("")
        self.txt_address.delete("1.0", END)
        self.show()

    def delete(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll No should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select a roll no from the list", parent=self.root)
                else:
                    op = messagebox.askyesno("Confirm", "Do you really want to delete?", parent=self.root)
                    if op:
                        cur.execute("DELETE FROM student WHERE rollno=?", (self.var_rollno.get(),))
                        con.commit()
                        messagebox.showinfo("Delete", "Student details deleted successfully", parent=self.root)
                        self.clear()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def get_data(self, ev):
        r = self.student_table.focus()
        content = self.student_table.item(r)
        row = content["values"]
        if not row:
            return
        # Set values using correct indexes
        self.var_rollno.set(row[0])
        self.var_name.set(row[1])
        self.var_email.set(row[2])
        self.var_state.set(row[3])
        self.var_city.set(row[4])
        self.var_DOB.set(row[5])
        self.var_pincode.set(row[6])
        self.var_gender.set(row[7])
        self.var_course.set(row[8])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[9])
        self.var_date.set(row[10])
        self.var_contact.set(row[11])
        # Make rollno readonly
        self.txt_rollno.config(state="readonly")

    def add(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll number should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
                row = cur.fetchone()
                if row is not None:
                    messagebox.showerror("Error", "This roll number already exists, try another", parent=self.root)
                else:
                    cur.execute(
                        "INSERT INTO student (rollno, name, email, state, city, DOB, pincode, gender, course, address, date, contact) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                        (
                            self.var_rollno.get(),
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_DOB.get(),
                            self.var_pincode.get(),
                            self.var_gender.get(),
                            self.var_course.get(),
                            self.txt_address.get("1.0", END).strip(),
                            self.var_date.get(),
                            self.var_contact.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def update(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            if self.var_rollno.get() == "":
                messagebox.showerror("Error", "Roll no should be required", parent=self.root)
            else:
                cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_rollno.get(),))
                row = cur.fetchone()
                if row is None:
                    messagebox.showerror("Error", "Please select a roll no from the list", parent=self.root)
                else:
                    cur.execute(
                        "UPDATE student SET name=?, email=?, state=?, city=?, DOB=?, pincode=?, gender=?, course=?, address=?, date=?, contact=? WHERE rollno=?",
                        (
                            self.var_name.get(),
                            self.var_email.get(),
                            self.var_state.get(),
                            self.var_city.get(),
                            self.var_DOB.get(),
                            self.var_pincode.get(),
                            self.var_gender.get(),
                            self.var_course.get(),
                            self.txt_address.get("1.0", END).strip(),
                            self.var_date.get(),
                            self.var_contact.get(),
                            self.var_rollno.get()
                        )
                    )
                    con.commit()
                    messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
                    self.show()
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def search(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student WHERE rollno=?", (self.var_search.get(),))
            row = cur.fetchone()
            self.student_table.delete(*self.student_table.get_children())
            if row:
                self.student_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()

    def show(self):
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT * FROM student")
            rows = cur.fetchall()
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
        except Exception as e:
            messagebox.showerror("Error", f"Error due to : {str(e)}")
        finally:
            con.close()
            
    def load_data(self):
        self.course_list.clear()
        con = sqlite3.connect(database="rms.db")
        cur = con.cursor()
        try:
            cur.execute("SELECT name FROM course")
            rows = cur.fetchall()
            if len(rows) > 0:
                for row in rows:
                    self.course_list.append(row[0])
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to {str(ex)}", parent=self.root)
        finally:
            con.close()

if __name__ == "__main__":
    root = Tk()
    obj = student(root)
    root.mainloop()