import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3

class RepairShopApp:
    def __init__(self, root):
        self.root = root
        self.root.title("DEBREMARKOS UNIVERSITY ONLINE STUDENT DEPARTMENT SELECTION SYSTEM")

        # Create database and tables
        self.create_database()

        # Create UI
        self.create_ui()

    def create_database(self):
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()

        # Create tables
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS student(
                studentId INTEGER PRIMARY KEY,
                FirstName VARCHAR(50) NOT NULL,
                LastName VARCHAR(50) NOT NULL,
                Email VARCHAR(30),
                Phone INT,
                Address VARCHAR(50)
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS department (
                departmentId INTEGER PRIMARY KEY,
                department_name VARCHAR(50) NOT NULL,
                stream VARCHAR(50) NOT NULL,
                hof VARCHAR(50) NOT NULL
            )
        ''')
        
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS course (
                courseId INTEGER PRIMARY KEY,
                title VARCHAR(56),
                RegistrationNo VARCHAR(45) NOT NULL,
                Year INTEGER,
                grade VARCHAR(34) NOT NULL,
                gpa VARCHAR(90) NOT NULL
            )
        ''')

        conn.commit()
        conn.close()

    def create_ui(self):
        # Create tabs
        self.tabControl = ttk.Notebook(self.root)
        self.student_tab = ttk.Frame(self.tabControl)
        self.department_tab = ttk.Frame(self.tabControl)
        self.course_tab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.student_tab, text='Student')
        self.tabControl.add(self.department_tab, text='Department')
        self.tabControl.add(self.course_tab, text='Course')
        self.tabControl.pack(expand=1, fill="both")

        # Create UI for each tab
        self.create_student_ui()
        self.create_department_ui()
        self.create_course_ui()

    def create_student_ui(self):
        # Student UI
        ttk.Label(self.student_tab, text="First Name:").grid(row=0, column=0)
        self.student_first_name_entry = ttk.Entry(self.student_tab)
        self.student_first_name_entry.grid(row=0, column=1)

        ttk.Label(self.student_tab, text="Last Name:").grid(row=1, column=0)
        self.student_last_name_entry = ttk.Entry(self.student_tab)
        self.student_last_name_entry.grid(row=1, column=1)

        ttk.Label(self.student_tab, text="Email:").grid(row=2, column=0)
        self.student_email_entry = ttk.Entry(self.student_tab)
        self.student_email_entry.grid(row=2, column=1)

        ttk.Label(self.student_tab, text="Phone:").grid(row=3, column=0)
        self.student_phone_entry = ttk.Entry(self.student_tab)
        self.student_phone_entry.grid(row=3, column=1)

        ttk.Label(self.student_tab, text="Address:").grid(row=4, column=0)
        self.student_address_entry = ttk.Entry(self.student_tab)
        self.student_address_entry.grid(row=4, column=1)

        ttk.Button(self.student_tab, text="Add Student", command=self.add_student).grid(row=10, column=0, columnspan=2)
        ttk.Button(self.student_tab, text="Update Student", command=self.update_student).grid(row=10, column=2, columnspan=2)
        ttk.Button(self.student_tab, text="Delete Student", command=self.delete_student).grid(row=10, column=4, columnspan=2)
        ttk.Button(self.student_tab, text="Clear Fields", command=self.clear_student_fields).grid(row=10, column=6, columnspan=2)
        ttk.Button(self.student_tab, text="View Student", command=self.view_student).grid(row=10, column=8, columnspan=2)

        self.student_tree = ttk.Treeview(self.student_tab, columns=("studentId", "FirstName", "LastName", "Email", "Phone", "Address"), show="headings")
        self.student_tree.heading("studentId", text="ID")
        self.student_tree.heading("FirstName", text="First Name")
        self.student_tree.heading("LastName", text="Last Name")
        self.student_tree.heading("Email", text="Email")
        self.student_tree.heading("Phone", text="Phone")
        self.student_tree.heading("Address", text="Address")
        self.student_tree.grid(row=12, column=0, columnspan=10)

        self.student_tree.bind("<Double-1>", self.on_student_select)

    def create_department_ui(self):
        # Department UI
        #department is one intity in the online department selection system
        ttk.Label(self.department_tab, text="Department Name:").grid(row=0, column=0)
        self.department_name_entry = ttk.Entry(self.department_tab)
        self.department_name_entry.grid(row=0, column=1)

        ttk.Label(self.department_tab, text="Stream:").grid(row=1, column=0)
        self.department_stream_entry = ttk.Entry(self.department_tab)
        self.department_stream_entry.grid(row=1, column=1)

        ttk.Label(self.department_tab, text="HOF:").grid(row=2, column=0)
        self.department_hof_entry = ttk.Entry(self.department_tab)
        self.department_hof_entry.grid(row=2, column=1)

        ttk.Button(self.department_tab, text="Add Department", command=self.add_department).grid(row=6, column=0, columnspan=2)
        ttk.Button(self.department_tab, text="Update Department", command=self.update_department).grid(row=6, column=2, columnspan=2)
        ttk.Button(self.department_tab, text="Delete Department", command=self.delete_department).grid(row=6, column=4, columnspan=2)
        ttk.Button(self.department_tab, text="Clear Fields", command=self.clear_department_fields).grid(row=6, column=6, columnspan=2)
        ttk.Button(self.department_tab, text="View Departments", command=self.view_department).grid(row=6, column=8, columnspan=2)

        self.department_tree = ttk.Treeview(self.department_tab, columns=("departmentId", "department_name", "stream", "hof"), show="headings")
        self.department_tree.heading("departmentId", text="ID")
        self.department_tree.heading("department_name", text="Department Name")
        self.department_tree.heading("stream", text="Stream")
        self.department_tree.heading("hof", text="HOF")
        self.department_tree.grid(row=10, column=0, columnspan=10)

        self.department_tree.bind("<Double-1>", self.on_department_select)

    def create_course_ui(self):
        # Course UI
        ttk.Label(self.course_tab, text="Title:").grid(row=0, column=0)
        self.course_title_entry = ttk.Entry(self.course_tab)
        self.course_title_entry.grid(row=0, column=1)

        ttk.Label(self.course_tab, text="Registration No:").grid(row=1, column=0)
        self.course_registration_no_entry = ttk.Entry(self.course_tab)
        self.course_registration_no_entry.grid(row=1, column=1)

        ttk.Label(self.course_tab, text="Year:").grid(row=2, column=0)
        self.course_year_entry = ttk.Entry(self.course_tab)
        self.course_year_entry.grid(row=2, column=1)

        ttk.Label(self.course_tab, text="Grade:").grid(row=3, column=0)
        self.course_grade_entry = ttk.Entry(self.course_tab)
        self.course_grade_entry.grid(row=3, column=1)

        ttk.Label(self.course_tab, text="GPA:").grid(row=4, column=0)
        self.course_gpa_entry = ttk.Entry(self.course_tab)
        self.course_gpa_entry.grid(row=4, column=1)

        ttk.Button(self.course_tab, text="Add Course", command=self.add_course).grid(row=6, column=0, columnspan=2)
        ttk.Button(self.course_tab, text="Update Course", command=self.update_course).grid(row=6, column=2, columnspan=2)
        ttk.Button(self.course_tab, text="Delete Course", command=self.delete_course).grid(row=6, column=4, columnspan=2)
        ttk.Button(self.course_tab, text="Clear Fields", command=self.clear_course_fields).grid(row=6, column=6, columnspan=2)
        ttk.Button(self.course_tab, text="View Courses", command=self.view_course).grid(row=6, column=8, columnspan=2)

        self.course_tree = ttk.Treeview(self.course_tab, columns=("courseId", "title", "RegistrationNo", "Year", "grade", "gpa"), show="headings")
        self.course_tree.heading("courseId", text="ID")
        self.course_tree.heading("title", text="Title")
        self.course_tree.heading("RegistrationNo", text="Registration No")
        self.course_tree.heading("Year", text="Year")
        self.course_tree.heading("grade", text="Grade")
        self.course_tree.heading("gpa", text="GPA")
        self.course_tree.grid(row=11, column=0, columnspan=10)
        self.course_tree.bind("<Double-1>", self.on_course_select)

    # CRUD Operations for Student

    '''CRUD Operations in Databases
CRUD is an acronym that stands for the four basic operations you can perform on data in a database:

Create - Adding new records to the database

Read - Retrieving or viewing existing records

Update - Modifying existing records

Delete - Removing records from the database

These operations form the foundation of most database interactions in applications. Here's a more detailed breakdown:

Create (Insert)
Adds new data to the database

In SQL: INSERT INTO table_name (column1, column2) VALUES (value1, value2);

Example: Adding a new user to a users table

Read (Select)
Retrieves data from the database

In SQL: SELECT column1, column2 FROM table_name WHERE condition;

Example: Getting a list of all active users

Update (Modify)
Changes existing data in the database

In SQL: UPDATE table_name SET column1 = value1 WHERE condition;

Example: Changing a user's email address

Delete (Remove)
Removes data from the database

In SQL: DELETE FROM table_name WHERE condition;

Example: Removing an inactive user account

CRUD operations are implemented in all types of databases (relational like MySQL, PostgreSQL, and non-relational like MongoDB) though the specific syntax may vary. They are essential for any application that needs to persistently store and manage data.

        // Sample product CRUD operations
const Product = require('./models/Product');

// CREATE
router.post('/products', async (req, res) => {
  const product = new Product(req.body);
  await product.save();
  res.status(201).send(product);
});

// READ
router.get('/products', async (req, res) => {
  const products = await Product.find({});
  res.send(products);
});

// UPDATE
router.patch('/products/:id', async (req, res) => {
  const product = await Product.findByIdAndUpdate(req.params.id, req.body);
  res.send(product);
});

// DELETE
router.delete('/products/:id', async (req, res) => {
  await Product.findByIdAndDelete(req.params.id);
  res.status(204).send();
});'''
    def add_student(self):
        first_name = self.student_first_name_entry.get()
        last_name = self.student_last_name_entry.get()
        email = self.student_email_entry.get()
        phone = self.student_phone_entry.get()
        address = self.student_address_entry.get()
        
        if first_name and last_name:
            conn = sqlite3.connect('departement_selection_system.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO student(FirstName, LastName, Email, Phone, Address) VALUES (?, ?, ?, ?, ?)",
                        (first_name, last_name, email, phone, address))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Student registered successfully.")
            self.view_student()
        else:
            messagebox.showwarning("Input Error", "Please enter first and last name.")

    def update_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to update.")
            return

        student_id = self.student_tree.item(selected_item)['values'][0]
        first_name = self.student_first_name_entry.get()
        last_name = self.student_last_name_entry.get()
        email = self.student_email_entry.get()
        phone = self.student_phone_entry.get()
        address = self.student_address_entry.get()
        
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE student SET FirstName=?, LastName=?, Email=?, Phone=?, Address=? WHERE studentId=?",
                    (first_name, last_name, email, phone, address, student_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student updated successfully.")
        self.view_student()

    def delete_student(self):
        selected_item = self.student_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a student to delete.")
            return

        student_id = self.student_tree.item(selected_item)['values'][0]
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM student WHERE studentId=?", (student_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Student deleted successfully.")
        self.view_student()

    def clear_student_fields(self):
        self.student_first_name_entry.delete(0, tk.END)
        self.student_last_name_entry.delete(0, tk.END)
        self.student_email_entry.delete(0, tk.END)
        self.student_phone_entry.delete(0, tk.END)
        self.student_address_entry.delete(0, tk.END)

    def view_student(self):
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        self.student_tree.delete(*self.student_tree.get_children())
        cursor.execute("SELECT * FROM student")
        for row in cursor.fetchall():
            self.student_tree.insert("", "end", values=row)
        conn.close()

    def on_student_select(self, event):
        selected_item = self.student_tree.selection()
        if selected_item:
            student = self.student_tree.item(selected_item)['values']
            self.student_first_name_entry.delete(0, tk.END)
            self.student_first_name_entry.insert(0, student[1])
            self.student_last_name_entry.delete(0, tk.END)
            self.student_last_name_entry.insert(0, student[2])
            self.student_email_entry.delete(0, tk.END)
            self.student_email_entry.insert(0, student[3])
            self.student_phone_entry.delete(0, tk.END)
            self.student_phone_entry.insert(0, student[4])
            self.student_address_entry.delete(0, tk.END)
            self.student_address_entry.insert(0, student[5])

    # CRUD Operations for Department
    def add_department(self):
        department_name = self.department_name_entry.get()
        stream = self.department_stream_entry.get()
        hof = self.department_hof_entry.get()
        
        if department_name and stream and hof:
            conn = sqlite3.connect('departement_selection_system.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO department (department_name, stream, hof) VALUES (?, ?, ?)",
                        (department_name, stream, hof))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Department added successfully.")
            self.view_department()
        else:
            messagebox.showwarning("Input Error", "Please enter all department information.")

    def update_department(self):
        selected_item = self.department_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a department to update.")
            return

        department_id = self.department_tree.item(selected_item)['values'][0]
        department_name = self.department_name_entry.get()
        stream = self.department_stream_entry.get()
        hof = self.department_hof_entry.get()
        
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE department SET department_name=?, stream=?, hof=? WHERE departmentId=?",
                    (department_name, stream, hof, department_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Department updated successfully.")
        self.view_department()

    def delete_department(self):
        selected_item = self.department_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a department to delete.")
            return

        department_id = self.department_tree.item(selected_item)['values'][0]
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM department WHERE departmentId=?", (department_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Department deleted successfully.")
        self.view_department()

    def clear_department_fields(self):
        self.department_name_entry.delete(0, tk.END)
        self.department_stream_entry.delete(0, tk.END)
        self.department_hof_entry.delete(0, tk.END)

    def view_department(self):
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        self.department_tree.delete(*self.department_tree.get_children())
        cursor.execute("SELECT * FROM department")
        for row in cursor.fetchall():
            self.department_tree.insert("", "end", values=row)
        conn.close()

    def on_department_select(self, event):
        selected_item = self.department_tree.selection()
        if selected_item:
            department = self.department_tree.item(selected_item)['values']
            self.department_name_entry.delete(0, tk.END)
            self.department_name_entry.insert(0, department[1])
            self.department_stream_entry.delete(0, tk.END)
            self.department_stream_entry.insert(0, department[2])
            self.department_hof_entry.delete(0, tk.END)
            self.department_hof_entry.insert(0, department[3])

    # CRUD Operations for course
    def add_course(self):
        title = self.course_title_entry.get()
        registration_no = self.course_registration_no_entry.get()
        year = self.course_year_entry.get()
        grade = self.course_grade_entry.get()
        gpa = self.course_gpa_entry.get()
        
        if title and registration_no:
            conn = sqlite3.connect('departement_selection_system.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO course (title, RegistrationNo, Year, grade, gpa) VALUES (?, ?, ?, ?, ?)",
                        (title, registration_no, year, grade, gpa))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success", "Course added successfully.")
            self.view_course()
        else:
            messagebox.showwarning("Input Error", "Please enter title and registration number.")

    def update_course(self):
        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a course to update.")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]
        title = self.course_title_entry.get()
        registration_no = self.course_registration_no_entry.get()
        year = self.course_year_entry.get()
        grade = self.course_grade_entry.get()
        gpa = self.course_gpa_entry.get()
        
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("UPDATE course SET title=?, RegistrationNo=?, Year=?, grade=?, gpa=? WHERE courseId=?",
                    (title, registration_no, year, grade, gpa, course_id))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course updated successfully.")
        self.view_course()

    def delete_course(self):
        selected_item = self.course_tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select a course to delete.")
            return

        course_id = self.course_tree.item(selected_item)['values'][0]
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        cursor.execute("DELETE FROM course WHERE courseId=?", (course_id,))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Course deleted successfully.")
        self.view_course()

    def clear_course_fields(self):
        self.course_title_entry.delete(0, tk.END)
        self.course_registration_no_entry.delete(0, tk.END)
        self.course_year_entry.delete(0, tk.END)
        self.course_grade_entry.delete(0, tk.END)
        self.course_gpa_entry.delete(0, tk.END)
        
    def view_course(self):
        conn = sqlite3.connect('departement_selection_system.db')
        cursor = conn.cursor()
        self.course_tree.delete(*self.course_tree.get_children())
        cursor.execute("SELECT * FROM course")
        for row in cursor.fetchall():
            self.course_tree.insert("", "end", values=row)
        conn.close()

    def on_course_select(self, event):
        selected_item = self.course_tree.selection()
        if selected_item:
            course = self.course_tree.item(selected_item)['values']
            self.course_title_entry.delete(0, tk.END)
            self.course_title_entry.insert(0, course[1])
            self.course_registration_no_entry.delete(0, tk.END)
            self.course_registration_no_entry.insert(0, course[2])
            self.course_year_entry.delete(0, tk.END)
            self.course_year_entry.insert(0, course[3])
            self.course_grade_entry.delete(0, tk.END)
            self.course_grade_entry.insert(0, course[4])
            self.course_gpa_entry.delete(0, tk.END)
            self.course_gpa_entry.insert(0, course[5])

# Login Window
def create_login_window():
    def toggle_password_visibility():
        if entry_password['show'] == '*':
            entry_password.config(show='')
            eye_button.config(text="👁")
            # Hide password after 2 seconds
            entry_password.after(500, lambda: [entry_password.config(show='*'), eye_button.config(text="👁")])
        else:
            entry_password.config(show='*')
            eye_button.config(text="👁")

    def log():
        txtu = entry_username.get()
        txtp = entry_password.get()
        if txtu == 'dmu' and txtp == "dmu1221":
            rw.destroy()
            root = tk.Tk()
            app = RepairShopApp(root)
            root.mainloop()
        elif txtu != "dmu" and txtp != "dmu1221":
            messagebox.showerror("Error", "Please enter correct username and password") 
        elif txtu != "dmu":
            messagebox.showerror("Error", "Invalid username") 
        elif txtp != "dmu1221":
            messagebox.showerror("Error", "Invalid password")

    rw = tk.Tk()
    rw.title("Login User Interface")
    rw.geometry('600x600')
    rw.resizable(True, True)
    rw.configure(bg="#2c3e50")

    # Frame for the Login Form
    frame = tk.Frame(rw, bg="#ecf0f1", bd=5, relief=tk.RIDGE)
    frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=1100, height=280)

    title_label = tk.Label(frame, text="WELLCOME TO DEBREMARKOS UNIVERSITY\nONLINE STUDENT DEPARTMENT SELECTION SYSTEM", 
                         font=("Arial", 12, "bold"), bg="#ecf0f1", fg="#2c3e50")
    title_label.pack(pady=10)

    # Username Entry
    '''
    label_username = tk.Label(frame, text="Username:", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
    label_username.pack()
    entry_username = ttk.Entry(frame, font=("Arial", 12))
    entry_username.pack(pady=5, ipady=3)'''
    username_frame = tk.Frame(frame, bg="#ecf0f1")
    username_frame.pack(pady=10)
    tk.Label(username_frame, text="Username:", font=("Arial", 12), bg="#ecf0f1").pack(side=tk.LEFT)
    entry_username = ttk.Entry(username_frame, font=("Arial", 12), width=25)
    entry_username.pack(side=tk.LEFT, padx=10)

    # Password Entry
    password_frame = tk.Frame(frame, bg="#ecf0f1")
    password_frame.pack(pady=10)
    tk.Label(password_frame, text="Password:", font=("Arial", 12), bg="#ecf0f1").pack(side=tk.LEFT)

    entry_password = ttk.Entry(password_frame, font=("Arial", 12), show="*", width=25)
    entry_password.pack(side=tk.LEFT)

    eye_button = tk.Button(password_frame, text="👁", font=("Arial", 12), 
                         bg="#ecf0f1", relief=tk.FLAT, command=toggle_password_visibility)
    eye_button.pack(side=tk.LEFT, padx=5)

    # Login Button
    login_button = tk.Button(frame, text="Login", font=("Arial", 12, "bold"), 
                           bg="#2c3e50", fg="white", command=log)
    login_button.pack(pady=20, ipadx=50, ipady=5)

    rw.mainloop()

if __name__ == "__main__":
    create_login_window()