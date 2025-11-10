import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
rw=tk.Tk()
rw.title("login user interface")
rw.geometry('600x600')
rw.resizable("true","true")
def log():
    txtu=entry_username.get()
    txtp=entry_password.get()
    if txtu=='zoom'and txtp=="zoom2030":
        rw.destroy()
        import tkinter as tk
        from tkinter import ttk, messagebox
        import sqlite3

        class RepairShopApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Repair Shop Management System")

                # Create database and tables
                self.create_database()

                # Create UI
                self.create_ui()

            def create_database(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()

                # Create tables
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Customers (
                        CustomerId INTEGER PRIMARY KEY,
                        FirstName VARCHAR(50) NOT NULL,
                        LastName VARCHAR(50) NOT NULL,
                        Email VARCHAR(30),
                        Phone INT,
                        Address VARCHAR(50),
                        DepositAmount DECIMAL(10,2),
                        DateOfDeposit DATE
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Computers (
                        ComputerId INTEGER PRIMARY KEY,
                        SerialNum VARCHAR(50) NOT NULL,
                        Make VARCHAR(50) NOT NULL,
                        Model VARCHAR(50) NOT NULL,
                        ComputerDescription TEXT,
                        CustomerId INTEGER,
                        FOREIGN KEY (CustomerId) REFERENCES Customers(CustomerId)
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS RepairJobs (
                        JobNum INTEGER PRIMARY KEY,
                        DateReceived DATE,
                        DateToReturn DATE,
                        DateReturned DATE,
                        DateStarted DATE,
                        DateEnded DATE,
                        RepairDetails TEXT,
                        LaborDetails TEXT,
                        LaborCost DECIMAL(10,2),
                        TotalCost DECIMAL(10,2),
                        PaidInFull VARCHAR(78),
                        AdditionalComments TEXT,
                        ComputerId INTEGER,
                        FOREIGN KEY (ComputerId) REFERENCES Computers(ComputerId)
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Vehicles (
                        VehicleId INTEGER PRIMARY KEY,
                        VIN VARCHAR(56),
                        RegistrationNo VARCHAR(45)NOT NULL,
                        Year INTEGER,
                        Make VARCHAR(34)NOT NULL,
                        Model VARCHAR(90) NOT NULL,
                        Color VARCHAR(45) NOT NULL
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Items (
                        ItemId INTEGER PRIMARY KEY,
                        PartNum TEXT NOT NULL,
                        ShortName TEXT NOT NULL,
                        ItemDescription TEXT,
                        Cost REAL,
                        NumInStock INTEGER,
                        ReorderLow INTEGER
                    )
                ''')
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS Repairmen (
                        RepairmenId INTEGER PRIMARY KEY,
                        LastName TEXT NOT NULL,
                        FirstName TEXT NOT NULL,
                        MI TEXT,
                        Email TEXT,
                        Mobile TEXT,
                        HTel TEXT,
                        Extension TEXT
                    )
                ''')

                conn.commit()
                conn.close()

            def create_ui(self):
                # Create tabs
                self.tabControl = ttk.Notebook(self.root)
                self.customers_tab = ttk.Frame(self.tabControl)
                self.computers_tab = ttk.Frame(self.tabControl)
                self.repair_jobs_tab = ttk.Frame(self.tabControl)
                self.vehicles_tab = ttk.Frame(self.tabControl)
                self.items_tab = ttk.Frame(self.tabControl)
                self.repairmen_tab = ttk.Frame(self.tabControl)

                self.tabControl.add(self.customers_tab, text='Customers')
                self.tabControl.add(self.computers_tab, text='Computers')
                self.tabControl.add(self.repair_jobs_tab, text='Repair Jobs')
                self.tabControl.add(self.vehicles_tab, text='Vehicles')
                self.tabControl.add(self.items_tab, text='Items')
                self.tabControl.add(self.repairmen_tab, text='Repairmen')
                self.tabControl.pack(expand=1, fill="both")

                # Create UI for each tab
                self.create_customers_ui()
                self.create_computers_ui()
                self.create_repair_jobs_ui()
                self.create_vehicles_ui()
                self.create_items_ui()
                self.create_repairmen_ui()

            def create_customers_ui(self):
                # Customer UI
                ttk.Label(self.customers_tab, text="First Name:").grid(row=0, column=0)
                self.customer_first_name_entry = ttk.Entry(self.customers_tab)
                self.customer_first_name_entry.grid(row=0, column=1)

                ttk.Label(self.customers_tab, text="Last Name:").grid(row=1, column=0)
                self.customer_last_name_entry = ttk.Entry(self.customers_tab)
                self.customer_last_name_entry.grid(row=1, column=1)

                ttk.Label(self.customers_tab, text="Email:").grid(row=2, column=0)
                self.customer_email_entry = ttk.Entry(self.customers_tab)
                self.customer_email_entry.grid(row=2, column=1)

                ttk.Label(self.customers_tab, text="Phone:").grid(row=3, column=0)
                self.customer_phone_entry = ttk.Entry(self.customers_tab)
                self.customer_phone_entry.grid(row=3, column=1)

                ttk.Label(self.customers_tab, text="Address:").grid(row=4, column=0)
                self.customer_address_entry = ttk.Entry(self.customers_tab)
                self.customer_address_entry.grid(row=4, column=1)

                ttk.Label(self.customers_tab, text="Deposit Amount:").grid(row=5, column=0)
                self.customer_deposit_entry = ttk.Entry(self.customers_tab)
                self.customer_deposit_entry.grid(row=5, column=1)

                ttk.Label(self.customers_tab, text="Date of Deposit:").grid(row=6, column=0)
                self.customer_date_of_deposit_entry = ttk.Entry(self.customers_tab)
                self.customer_date_of_deposit_entry.grid(row=6, column=1)

                ttk.Button(self.customers_tab, text="Add Customer", command=self.add_customer).grid(row=10, column=0, columnspan=2)
                ttk.Button(self.customers_tab, text="Update Customer", command=self.update_customer).grid(row=10, column=1, columnspan=2)
                ttk.Button(self.customers_tab, text="Delete Customer", command=self.delete_customer).grid(row=10, column=2, columnspan=2)
                ttk.Button(self.customers_tab, text="Clear Fields", command=self.clear_customer_fields).grid(row=10, column=4, columnspan=2)
                ttk.Button(self.customers_tab, text="View Customers", command=self.view_customers).grid(row=10, column=6, columnspan=2)

                self.customers_tree = ttk.Treeview(self.customers_tab, columns=("CustomerId", "FirstName", "LastName", "Email", "Phone", "Address", "DepositAmount", "DateOfDeposit"), show="headings")
                self.customers_tree.heading("CustomerId", text="ID")
                self.customers_tree.heading("FirstName", text="First Name")
                self.customers_tree.heading("LastName", text="Last Name")
                self.customers_tree.heading("Email", text="Email")
                self.customers_tree.heading("Phone", text="Phone")
                self.customers_tree.heading("Address", text="Address")
                self.customers_tree.heading("DepositAmount", text="Deposit Amount")
                self.customers_tree.heading("DateOfDeposit", text="Date of Deposit")
                self.customers_tree.grid(row=12, column=0, columnspan=20)

                self.customers_tree.bind("<Double-1>", self.on_customer_select)

            def create_computers_ui(self):
                # Computer UI
                ttk.Label(self.computers_tab, text="Serial Number:").grid(row=0, column=0)
                self.computer_serial_num_entry = ttk.Entry(self.computers_tab)
                self.computer_serial_num_entry.grid(row=0, column=1)

                ttk.Label(self.computers_tab, text="Make:").grid(row=1, column=0)
                self.computer_make_entry = ttk.Entry(self.computers_tab)
                self.computer_make_entry.grid(row=1, column=1)

                ttk.Label(self.computers_tab, text="Model:").grid(row=2, column=0)
                self.computer_model_entry = ttk.Entry(self.computers_tab)
                self.computer_model_entry.grid(row=2, column=1)

                ttk.Label(self.computers_tab, text="Description:").grid(row=3, column=0)
                self.computer_description_entry = ttk.Entry(self.computers_tab)
                self.computer_description_entry.grid(row=3, column=1)

                ttk.Label(self.computers_tab, text="Customer ID:").grid(row=4, column=0)
                self.computer_customer_id_entry = ttk.Entry(self.computers_tab)
                self.computer_customer_id_entry.grid(row=4, column=1)

                ttk.Button(self.computers_tab, text="Add Computer", command=self.add_computer).grid(row=6, column=0, columnspan=2)
                ttk.Button(self.computers_tab, text="Update Computer", command=self.update_computer).grid(row=6, column=2, columnspan=2)
                ttk.Button(self.computers_tab, text="Delete Computer", command=self.delete_computer).grid(row=6, column=4, columnspan=2)
                ttk.Button(self.computers_tab, text="Clear Fields", command=self.clear_computer_fields).grid(row=6, column=6, columnspan=2)
                ttk.Button(self.computers_tab, text="View Computers", command=self.view_computers).grid(row=6, column=8, columnspan=2)

                self.computers_tree = ttk.Treeview(self.computers_tab, columns=("ComputerId", "SerialNum", "Make", "Model", "Description", "CustomerId"), show="headings")
                self.computers_tree.heading("ComputerId", text="ID")
                self.computers_tree.heading("SerialNum", text="Serial Number")
                self.computers_tree.heading("Make", text="Make")
                self.computers_tree.heading("Model", text="Model")
                self.computers_tree.heading("Description", text="Description")
                self.computers_tree.heading("CustomerId", text="Customer ID")
                self.computers_tree.grid(row=10, column=0,columnspan=20)

                self.computers_tree.bind("<Double-1>", self.on_computer_select)

            def create_repair_jobs_ui(self):
                # Repair Job UI
                ttk.Label(self.repair_jobs_tab, text="Job Number:").grid(row=0, column=0)
                self.repair_job_num_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_num_entry.grid(row=0, column=1)

                ttk.Label(self.repair_jobs_tab, text="Date Received:").grid(row=1, column=0)
                self.repair_job_date_received_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_date_received_entry.grid(row=1, column=1)

                ttk.Label(self.repair_jobs_tab, text="Date To Return:").grid(row=2, column=0)
                self.repair_job_date_to_return_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_date_to_return_entry.grid(row=2, column=1)

                ttk.Label(self.repair_jobs_tab, text="Date Returned:").grid(row=3, column=0)
                self.repair_job_date_returned_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_date_returned_entry.grid(row=3, column=1)

                ttk.Label(self.repair_jobs_tab, text="Date Started:").grid(row=4, column=0)
                self.repair_job_date_started_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_date_started_entry.grid(row=4, column=1)

                ttk.Label(self.repair_jobs_tab, text="Date Ended:").grid(row=5, column=0)
                self.repair_job_date_ended_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_date_ended_entry.grid(row=5, column=1)

                ttk.Label(self.repair_jobs_tab, text="Repair Details:").grid(row=6, column=0)
                self.repair_job_repair_details_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_repair_details_entry.grid(row=6, column=1)

                ttk.Label(self.repair_jobs_tab, text="Labor Details:").grid(row=7, column=0)
                self.repair_job_labor_details_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_labor_details_entry.grid(row=7, column=1)

                ttk.Label(self.repair_jobs_tab, text="Labor Cost:").grid(row=8, column=0)
                self.repair_job_labor_cost_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_labor_cost_entry.grid(row=8, column=1)

                ttk.Label(self.repair_jobs_tab, text="Total Cost:").grid(row=9, column=0)
                self.repair_job_total_cost_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_total_cost_entry.grid(row=9, column=1)

                ttk.Label(self.repair_jobs_tab, text="Paid In Full (1/0):").grid(row=10, column=0)
                self.repair_job_paid_in_full_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_paid_in_full_entry.grid(row=10, column=1)

                ttk.Label(self.repair_jobs_tab, text="Additional Comments:").grid(row=11, column=0)
                self.repair_job_additional_comments_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_additional_comments_entry.grid(row=11, column=1)

                ttk.Label(self.repair_jobs_tab, text="Computer ID:").grid(row=12, column=0)
                self.repair_job_computer_id_entry = ttk.Entry(self.repair_jobs_tab)
                self.repair_job_computer_id_entry.grid(row=12, column=1)

                ttk.Button(self.repair_jobs_tab, text="Add Repair Job", command=self.add_repair_job).grid(row=15, column=0, columnspan=2)
                ttk.Button(self.repair_jobs_tab, text="Update Repair Job", command=self.update_repair_job).grid(row=15, column=1, columnspan=2)
                ttk.Button(self.repair_jobs_tab, text="Delete Repair Job", command=self.delete_repair_job).grid(row=15, column=3, columnspan=2)
                ttk.Button(self.repair_jobs_tab, text="Clear Fields", command=self.clear_repair_job_fields).grid(row=15, column=5, columnspan=2)
                ttk.Button(self.repair_jobs_tab, text="View Repair Jobs", command=self.view_repair_jobs).grid(row=15, column=7, columnspan=2)

                self.repair_jobs_tree = ttk.Treeview(self.repair_jobs_tab, columns=("JobNum", "DateReceived", "DateToReturn", "DateReturned", "DateStarted", "DateEnded", "RepairDetails", "LaborDetails", "LaborCost", "TotalCost", "PaidInFull", "AdditionalComments", "ComputerId"), show="headings")
                self.repair_jobs_tree.column("JobNum", width=90)
                self.repair_jobs_tree.heading("JobNum", text="Job Number")
                self.repair_jobs_tree.column("DateReceived",width=90 )
                self.repair_jobs_tree.heading("DateReceived", text="Date Received")
                self.repair_jobs_tree.column("DateToReturn",width=90 )
                self.repair_jobs_tree.heading("DateToReturn", text="Date To Return")
                self.repair_jobs_tree.column("DateReturned", width=90)
                self.repair_jobs_tree.heading("DateReturned", text="Date Returned")
                self.repair_jobs_tree.column("DateStarted", width=90)
                self.repair_jobs_tree.heading("DateStarted", text="Date Started")
                self.repair_jobs_tree.column("DateEnded", width=90)
                self.repair_jobs_tree.heading("DateEnded", text="Date Ended")
                self.repair_jobs_tree.column("RepairDetails", width=90)
                self.repair_jobs_tree.heading("RepairDetails", text="Repair Details")
                self.repair_jobs_tree.column("LaborDetails", width=90)
                self.repair_jobs_tree.heading("LaborDetails", text="Labor Details")
                self.repair_jobs_tree.column("LaborCost", width=90)
                self.repair_jobs_tree.heading("LaborCost", text="Labor Cost")
                self.repair_jobs_tree.column("TotalCost", width=90)
                self.repair_jobs_tree.heading("TotalCost", text="Total Cost")
                self.repair_jobs_tree.column("PaidInFull", width=90)
                self.repair_jobs_tree.heading("PaidInFull", text="Paid In Full")
                self.repair_jobs_tree.heading("AdditionalComments", text="Additional Comments")
                self.repair_jobs_tree.column("AdditionalComments",width=90 )
                self.repair_jobs_tree.heading("ComputerId", text="Computer ID")
                self.repair_jobs_tree.grid(row=18, column=0, columnspan=20)

                self.repair_jobs_tree.bind("<Double-1>", self.on_repair_job_select)

            def create_vehicles_ui(self):
                # Vehicle UI
                ttk.Label(self.vehicles_tab, text="VIN:").grid(row=0, column=0)
                self.vehicle_vin_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_vin_entry.grid(row=0, column=1)

                ttk.Label(self.vehicles_tab, text="Registration No:").grid(row=1, column=0)
                self.vehicle_registration_no_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_registration_no_entry.grid(row=1, column=1)

                ttk.Label(self.vehicles_tab, text="Year:").grid(row=2, column=0)
                self.vehicle_year_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_year_entry.grid(row=2, column=1)

                ttk.Label(self.vehicles_tab, text="Make:").grid(row=3, column=0)
                self.vehicle_make_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_make_entry.grid(row=3, column=1)

                ttk.Label(self.vehicles_tab, text="Model:").grid(row=4, column=0)
                self.vehicle_model_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_model_entry.grid(row=4, column=1)

                ttk.Label(self.vehicles_tab, text="Color:").grid(row=5, column=0)
                self.vehicle_color_entry = ttk.Entry(self.vehicles_tab)
                self.vehicle_color_entry.grid(row=5, column=1)

                ttk.Button(self.vehicles_tab, text="Add Vehicle", command=self.add_vehicle).grid(row=6, column=0, columnspan=2)
                ttk.Button(self.vehicles_tab, text="Update Vehicle", command=self.update_vehicle).grid(row=6, column=1, columnspan=2)
                ttk.Button(self.vehicles_tab, text="Delete Vehicle", command=self.delete_vehicle).grid(row=6, column=2, columnspan=2)
                ttk.Button(self.vehicles_tab, text="Clear Fields", command=self.clear_vehicle_fields).grid(row=6, column=4, columnspan=2)
                ttk.Button(self.vehicles_tab, text="View Vehicles", command=self.view_vehicles).grid(row=6, column=6, columnspan=2)

                self.vehicles_tree = ttk.Treeview(self.vehicles_tab, columns=("VehicleId", "VIN", "RegistrationNo", "Year", "Make", "Model", "Color"), show="headings")
                self.vehicles_tree.heading("VehicleId", text="ID")
                self.vehicles_tree.heading("VIN", text="VIN")
                self.vehicles_tree.heading("RegistrationNo", text="Registration No")
                self.vehicles_tree.heading("Year", text="Year")
                self.vehicles_tree.heading("Make", text="Make")
                self.vehicles_tree.heading("Model", text="Model")
                self.vehicles_tree.heading("Color", text="Color")
                self.vehicles_tree.grid(row=11, column=0, columnspan=20)

                self.vehicles_tree.bind("<Double-1>", self.on_vehicle_select)

            def create_items_ui(self):
                # Item UI
                ttk.Label(self.items_tab, text="Part Number:").grid(row=0, column=0)
                self.item_part_num_entry = ttk.Entry(self.items_tab)
                self.item_part_num_entry.grid(row=0, column=1)

                ttk.Label(self.items_tab, text="Short Name:").grid(row=1, column=0)
                self.item_short_name_entry = ttk.Entry(self.items_tab)
                self.item_short_name_entry.grid(row=1, column=1)

                ttk.Label(self.items_tab, text="Description:").grid(row=2, column=0)
                self.item_description_entry = ttk.Entry(self.items_tab)
                self.item_description_entry.grid(row=2, column=1)

                ttk.Label(self.items_tab, text="Cost:").grid(row=3, column=0)
                self.item_cost_entry = ttk.Entry(self.items_tab)
                self.item_cost_entry.grid(row=3, column=1)

                ttk.Label(self.items_tab, text="Number In Stock:").grid(row=4, column=0)
                self.item_num_in_stock_entry = ttk.Entry(self.items_tab)
                self.item_num_in_stock_entry.grid(row=4, column=1)

                ttk.Label(self.items_tab, text="Reorder Low:").grid(row=5, column=0)
                self.item_reorder_low_entry = ttk.Entry(self.items_tab)
                self.item_reorder_low_entry.grid(row=5, column=1)

                ttk.Button(self.items_tab, text="Add Item", command=self.add_item).grid(row=6, column=0, columnspan=2)
                ttk.Button(self.items_tab, text="Update Item", command=self.update_item).grid(row=6, column=1, columnspan=2)
                ttk.Button(self.items_tab, text="Delete Item", command=self.delete_item).grid(row=6, column=2, columnspan=2)
                ttk.Button(self.items_tab, text="Clear Fields", command=self.clear_item_fields).grid(row=6, column=4, columnspan=2)
                ttk.Button(self.items_tab, text="View Items", command=self.view_items).grid(row=6, column=6, columnspan=2)

                self.items_tree = ttk.Treeview(self.items_tab, columns=("ItemId", "PartNum", "ShortName", "ItemDescription", "Cost", "NumInStock", "ReorderLow"), show="headings")
                self.items_tree.heading("ItemId", text="ID")
                self.items_tree.heading("PartNum", text="Part Number")
                self.items_tree.heading("ShortName", text="Short Name")
                self.items_tree.heading("ItemDescription", text="Description")
                self.items_tree.heading("Cost", text="Cost")
                self.items_tree.heading("NumInStock", text="Number In Stock")
                self.items_tree.heading("ReorderLow", text="Reorder Low")
                self.items_tree.grid(row=11, column=0, columnspan=20)

                self.items_tree.bind("<Double-1>", self.on_item_select)

            def create_repairmen_ui(self):
                # Repairman UI
                ttk.Label(self.repairmen_tab, text="First Name:").grid(row=0, column=0)
                self.repairman_first_name_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_first_name_entry.grid(row=0, column=1)

                ttk.Label(self.repairmen_tab, text="Last Name:").grid(row=1, column=0)
                self.repairman_last_name_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_last_name_entry.grid(row=1, column=1)

                ttk.Label(self.repairmen_tab, text="Middle Initial:").grid(row=2, column=0)
                self.repairman_mi_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_mi_entry.grid(row=2, column=1)

                ttk.Label(self.repairmen_tab, text="Email:").grid(row=3, column=0)
                self.repairman_email_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_email_entry.grid(row=3, column=1)
                ttk.Label(self.repairmen_tab, text="Mobile:").grid(row=4, column=0)
                self.repairman_mobile_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_mobile_entry.grid(row=4, column=1)

                ttk.Label(self.repairmen_tab, text="Home Telephone:").grid(row=5, column=0)
                self.repairman_h_tel_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_h_tel_entry.grid(row=5, column=1)

                ttk.Label(self.repairmen_tab, text="Extension:").grid(row=6, column=0)
                self.repairman_extension_entry = ttk.Entry(self.repairmen_tab)
                self.repairman_extension_entry.grid(row=6, column=1)

                ttk.Button(self.repairmen_tab, text="Add Repairman", command=self.add_repairman).grid(row=7, column=0, columnspan=2)
                ttk.Button(self.repairmen_tab, text="Update Repairman", command=self.update_repairman).grid(row=7, column=1, columnspan=2)
                ttk.Button(self.repairmen_tab, text="Delete Repairman", command=self.delete_repairman).grid(row=7, column=2, columnspan=2)
                ttk.Button(self.repairmen_tab, text="Clear Fields", command=self.clear_repairman_fields).grid(row=7, column=4, columnspan=2)
                ttk.Button(self.repairmen_tab, text="View Repairmen", command=self.view_repairmen).grid(row=7, column=6, columnspan=2)

                self.repairmen_tree = ttk.Treeview(self.repairmen_tab, columns=("RepairmenId", "FirstName", "LastName", "MI", "Email", "Mobile", "HTel", "Extension"), show="headings")
                self.repairmen_tree.heading("RepairmenId", text="ID")
                self.repairmen_tree.heading("FirstName", text="First Name")
                self.repairmen_tree.heading("LastName", text="Last Name")
                self.repairmen_tree.heading("MI", text="Middle Initial")
                self.repairmen_tree.heading("Email", text="Email")
                self.repairmen_tree.heading("Mobile", text="Mobile")
                self.repairmen_tree.heading("HTel", text="Home Telephone")
                self.repairmen_tree.heading("Extension", text="Extension")
                self.repairmen_tree.grid(row=12, column=0, columnspan=20)

                self.repairmen_tree.bind("<Double-1>", self.on_repairman_select)

            # CRUD Operations
            def add_customer(self):
                first_name = self.customer_first_name_entry.get()
                last_name = self.customer_last_name_entry.get()
                email = self.customer_email_entry.get()
                phone = self.customer_phone_entry.get()
                address = self.customer_address_entry.get()
                deposit_amount = self.customer_deposit_entry.get()
                date_of_deposit = self.customer_date_of_deposit_entry.get()

                if first_name and last_name:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Customers (FirstName, LastName, Email, Phone, Address, DepositAmount, DateOfDeposit) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (first_name, last_name, email, phone, address, deposit_amount, date_of_deposit))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Customer added successfully.")
                    self.view_customers()
                else:
                    messagebox.showwarning("Input Error", "Please enter first and last name.")

            def update_customer(self):
                selected_item = self.customers_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a customer to update.")
                    return

                customer_id = self.customers_tree.item(selected_item)['values'][0]
                first_name = self.customer_first_name_entry.get()
                last_name = self.customer_last_name_entry.get()
                email = self.customer_email_entry.get()
                phone = self.customer_phone_entry.get()
                address = self.customer_address_entry.get()
                deposit_amount = self.customer_deposit_entry.get()
                date_of_deposit = self.customer_date_of_deposit_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Customers SET FirstName=?, LastName=?, Email=?, Phone=?, Address=?, DepositAmount=?, DateOfDeposit=? WHERE CustomerId=?",
                            (first_name, last_name, email, phone, address, deposit_amount, date_of_deposit, customer_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Customer updated successfully.")
                self.view_customers()

            def delete_customer(self):
                selected_item = self.customers_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a customer to delete.")
                    return

                customer_id = self.customers_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Customers WHERE CustomerId=?", (customer_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Customer deleted successfully.")
                self.view_customers()

            def clear_customer_fields(self):
                self.customer_first_name_entry.delete(0, tk.END)
                self.customer_last_name_entry.delete(0, tk.END)
                self.customer_email_entry.delete(0, tk.END)
                self.customer_phone_entry.delete(0, tk.END)
                self.customer_address_entry.delete(0, tk.END)
                self.customer_deposit_entry.delete(0, tk.END)
                self.customer_date_of_deposit_entry.delete(0, tk.END)

            def view_customers(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.customers_tree.delete(*self.customers_tree.get_children())
                cursor.execute("SELECT * FROM Customers")
                for row in cursor.fetchall():
                    self.customers_tree.insert("", "end", values=row)
                conn.close()

            def on_customer_select(self, event):
                selected_item = self.customers_tree.selection()
                if selected_item:
                    customer = self.customers_tree.item(selected_item)['values']
                    self.customer_first_name_entry.delete(0, tk.END)
                    self.customer_first_name_entry.insert(0, customer[1])
                    self.customer_last_name_entry.delete(0, tk.END)
                    self.customer_last_name_entry.insert(0, customer[2])
                    self.customer_email_entry.delete(0, tk.END)
                    self.customer_email_entry.insert(0, customer[3])
                    self.customer_phone_entry.delete(0, tk.END)
                    self.customer_phone_entry.insert(0, customer[4])
                    self.customer_address_entry.delete(0, tk.END)
                    self.customer_address_entry.insert(0, customer[5])
                    self.customer_deposit_entry.delete(0, tk.END)
                    self.customer_deposit_entry.insert(0, customer[6])
                    self.customer_date_of_deposit_entry.delete(0, tk.END)
                    self.customer_date_of_deposit_entry.insert(0, customer[7])

            # Similar CRUD methods for Computers, Repair Jobs, Vehicles, Items, and Repairmen
            # ...

            def add_computer(self):
                serial_num = self.computer_serial_num_entry.get()
                make = self.computer_make_entry.get()
                model = self.computer_model_entry.get()
                description = self.computer_description_entry.get()
                customer_id = self.computer_customer_id_entry.get()

                if serial_num and make and model:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Computers (SerialNum, Make, Model, ComputerDescription, CustomerId) VALUES (?, ?, ?, ?, ?)",
                                (serial_num, make, model, description, customer_id))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Computer added successfully.")
                    self.view_computers()
                else:
                    messagebox.showwarning("Input Error", "Please enter serial number, make, and model.")

            def update_computer(self):
                selected_item = self.computers_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a computer to update.")
                    return

                computer_id = self.computers_tree.item(selected_item)['values'][0]
                serial_num = self.computer_serial_num_entry.get()
                make = self.computer_make_entry.get()
                model = self.computer_model_entry.get()
                description = self.computer_description_entry.get()
                customer_id = self.computer_customer_id_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Computers SET SerialNum=?, Make=?, Model=?, ComputerDescription=?, CustomerId=? WHERE ComputerId=?",
                            (serial_num, make, model, description, customer_id, computer_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Computer updated successfully.")
                self.view_computers()

            def delete_computer(self):
                selected_item = self.computers_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a computer to delete.")
                    return

                computer_id = self.computers_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Computers WHERE ComputerId=?", (computer_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Computer deleted successfully.")
                self.view_computers()

            def clear_computer_fields(self):
                self.computer_serial_num_entry.delete(0, tk.END)
                self.computer_make_entry.delete(0, tk.END)
                self.computer_model_entry.delete(0, tk.END)
                self.computer_description_entry.delete(0, tk.END)
                self.computer_customer_id_entry.delete(0, tk.END)

            def view_computers(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.computers_tree.delete(*self.computers_tree.get_children())
                cursor.execute("SELECT * FROM Computers")
                for row in cursor.fetchall():
                    self.computers_tree.insert("", "end", values=row)
                conn.close()

            def on_computer_select(self, event):
                selected_item = self.computers_tree.selection()
                if selected_item:
                    computer = self.computers_tree.item(selected_item)['values']
                    self.computer_serial_num_entry.delete(0, tk.END)
                    self.computer_serial_num_entry.insert(0, computer[1])
                    self.computer_make_entry.delete(0, tk.END)
                    self.computer_make_entry.insert(0, computer[2])
                    self.computer_model_entry.delete(0, tk.END)
                    self.computer_model_entry.insert(0, computer[3])
                    self.computer_description_entry.delete(0, tk.END)
                    self.computer_description_entry.insert(0, computer[4])
                    self.computer_customer_id_entry.delete(0, tk.END)
                    self.computer_customer_id_entry.insert(0, computer[5])

            # Similar CRUD methods for Repair Jobs, Vehicles, Items, and Repairmen
            # ...

            def add_repair_job(self):
                job_num = self.repair_job_num_entry.get()
                date_received = self.repair_job_date_received_entry.get()
                date_to_return = self.repair_job_date_to_return_entry.get()
                date_returned = self.repair_job_date_returned_entry.get()
                date_started = self.repair_job_date_started_entry.get()
                date_ended = self.repair_job_date_ended_entry.get()
                repair_details = self.repair_job_repair_details_entry.get()
                labor_details = self.repair_job_labor_details_entry.get()
                labor_cost = self.repair_job_labor_cost_entry.get()
                total_cost = self.repair_job_total_cost_entry.get()
                paid_in_full = self.repair_job_paid_in_full_entry.get()
                additional_comments = self.repair_job_additional_comments_entry.get()
                computer_id = self.repair_job_computer_id_entry.get()

                if job_num and date_received:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO RepairJobs (JobNum, DateReceived, DateToReturn, DateReturned, DateStarted, DateEnded, RepairDetails, LaborDetails, LaborCost, TotalCost, PaidInFull, AdditionalComments, ComputerId) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                                (job_num, date_received, date_to_return, date_returned, date_started, date_ended, repair_details, labor_details, labor_cost, total_cost, paid_in_full, additional_comments, computer_id))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Repair job added successfully.")
                    self.view_repair_jobs()
                else:
                    messagebox.showwarning("Input Error", "Please enter job number and date received.")

            def update_repair_job(self):
                selected_item = self.repair_jobs_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a repair job to update.")
                    return

                job_num = self.repair_jobs_tree.item(selected_item)['values'][0]
                date_received = self.repair_job_date_received_entry.get()
                date_to_return = self.repair_job_date_to_return_entry.get()
                date_returned = self.repair_job_date_returned_entry.get()
                date_started = self.repair_job_date_started_entry.get()
                date_ended = self.repair_job_date_ended_entry.get()
                repair_details = self.repair_job_repair_details_entry.get()
                labor_details = self.repair_job_labor_details_entry.get()
                labor_cost = self.repair_job_labor_cost_entry.get()
                total_cost = self.repair_job_total_cost_entry.get()
                paid_in_full = self.repair_job_paid_in_full_entry.get()
                additional_comments = self.repair_job_additional_comments_entry.get()
                computer_id = self.repair_job_computer_id_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE RepairJobs SET DateReceived=?, DateToReturn=?, DateReturned=?, DateStarted=?, DateEnded=?, RepairDetails=?, LaborDetails=?, LaborCost=?, TotalCost=?, PaidInFull=?, AdditionalComments=?, ComputerId=? WHERE JobNum=?",
                            (date_received, date_to_return, date_returned, date_started, date_ended, repair_details, labor_details, labor_cost, total_cost, paid_in_full, additional_comments, computer_id, job_num))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Repair job updated successfully.")
                self.view_repair_jobs()

            def delete_repair_job(self):
                selected_item = self.repair_jobs_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a repair job to delete.")
                    return

                job_num = self.repair_jobs_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM RepairJobs WHERE JobNum=?", (job_num,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Repair job deleted successfully.")
                self.view_repair_jobs()

            def clear_repair_job_fields(self):
                self.repair_job_num_entry.delete(0, tk.END)
                self.repair_job_date_received_entry.delete(0, tk.END)
                self.repair_job_date_to_return_entry.delete(0, tk.END)
                self.repair_job_date_returned_entry.delete(0, tk.END)
                self.repair_job_date_started_entry.delete(0, tk.END)
                self.repair_job_date_ended_entry.delete(0, tk.END)
                self.repair_job_repair_details_entry.delete(0, tk.END)
                self.repair_job_labor_details_entry.delete(0, tk.END)
                self.repair_job_labor_cost_entry.delete(0, tk.END)
                self.repair_job_total_cost_entry.delete(0, tk.END)
                self.repair_job_paid_in_full_entry.delete(0, tk.END)
                self.repair_job_additional_comments_entry.delete(0, tk.END)
                self.repair_job_computer_id_entry.delete(0, tk.END)

            def view_repair_jobs(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.repair_jobs_tree.delete(*self.repair_jobs_tree.get_children())
                cursor.execute("SELECT * FROM RepairJobs")
                for row in cursor.fetchall():
                    self.repair_jobs_tree.insert("", "end", values=row)
                conn.close()

            def on_repair_job_select(self, event):
                selected_item = self.repair_jobs_tree.selection()
                if selected_item:
                    job = self.repair_jobs_tree.item(selected_item)['values']
                    self.repair_job_num_entry.delete(0, tk.END)
                    self.repair_job_num_entry.insert(0, job[0])
                    self.repair_job_date_received_entry.delete(0, tk.END)
                    self.repair_job_date_received_entry.insert(0, job[1])
                    self.repair_job_date_to_return_entry.delete(0, tk.END)
                    self.repair_job_date_to_return_entry.insert(0, job[2])
                    self.repair_job_date_returned_entry.delete(0, tk.END)
                    self.repair_job_date_returned_entry.insert(0, job[3])
                    self.repair_job_date_started_entry.delete(0, tk.END)
                    self.repair_job_date_started_entry.insert(0, job[4])
                    self.repair_job_date_ended_entry.delete(0, tk.END)
                    self.repair_job_date_ended_entry.insert(0, job[5])
                    self.repair_job_repair_details_entry.delete(0, tk.END)
                    self.repair_job_repair_details_entry.insert(0, job[6])
                    self.repair_job_labor_details_entry.delete(0, tk.END)
                    self.repair_job_labor_details_entry.insert(0, job[7])
                    self.repair_job_labor_cost_entry.delete(0, tk.END)
                    self.repair_job_labor_cost_entry.insert(0, job[8])
                    self.repair_job_total_cost_entry.delete(0, tk.END)
                    self.repair_job_total_cost_entry.insert(0, job[9])
                    self.repair_job_paid_in_full_entry.delete(0, tk.END)
                    self.repair_job_paid_in_full_entry.insert(0, job[10])
                    self.repair_job_additional_comments_entry.delete(0, tk.END)
                    self.repair_job_additional_comments_entry.insert(0, job[11])
                    self.repair_job_computer_id_entry.delete(0, tk.END)
                    self.repair_job_computer_id_entry.insert(0, job[12])

            # Similar CRUD methods for Vehicles, Items, and Repairmen
            # ...

            def add_vehicle(self):
                vin = self.vehicle_vin_entry.get()
                registration_no = self.vehicle_registration_no_entry.get()
                year = self.vehicle_year_entry.get()
                make = self.vehicle_make_entry.get()
                model = self.vehicle_model_entry.get()
                color = self.vehicle_color_entry.get()

                if vin and registration_no:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Vehicles (VIN, RegistrationNo, Year, Make, Model, Color) VALUES (?, ?, ?, ?, ?, ?)",
                                (vin, registration_no, year, make, model, color))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Vehicle added successfully.")
                    self.view_vehicles()
                else:
                    messagebox.showwarning("Input Error", "Please enter VIN and registration number.")

            def update_vehicle(self):
                selected_item = self.vehicles_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a vehicle to update.")
                    return

                vehicle_id = self.vehicles_tree.item(selected_item)['values'][0]
                vin = self.vehicle_vin_entry.get()
                registration_no = self.vehicle_registration_no_entry.get()
                year = self.vehicle_year_entry.get()
                make = self.vehicle_make_entry.get()
                model = self.vehicle_model_entry.get()
                color = self.vehicle_color_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Vehicles SET VIN=?, RegistrationNo=?, Year=?, Make=?, Model=?, Color=? WHERE VehicleId=?",
                            (vin, registration_no, year, make, model, color, vehicle_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Vehicle updated successfully.")
                self.view_vehicles()

            def delete_vehicle(self):
                selected_item = self.vehicles_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a vehicle to delete.")
                    return

                vehicle_id = self.vehicles_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Vehicles WHERE VehicleId=?", (vehicle_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Vehicle deleted successfully.")
                self.view_vehicles()

            def clear_vehicle_fields(self):
                self.vehicle_vin_entry.delete(0, tk.END)
                self.vehicle_registration_no_entry.delete(0, tk.END)
                self.vehicle_year_entry.delete(0, tk.END)
                self.vehicle_make_entry.delete(0, tk.END)
                self.vehicle_model_entry.delete(0, tk.END)
                self.vehicle_color_entry.delete(0, tk.END)

            def view_vehicles(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.vehicles_tree.delete(*self.vehicles_tree.get_children())
                cursor.execute("SELECT * FROM Vehicles")
                for row in cursor.fetchall():
                    self.vehicles_tree.insert("", "end", values=row)
                conn.close()

            def on_vehicle_select(self, event):
                selected_item = self.vehicles_tree.selection()
                if selected_item:
                    vehicle = self.vehicles_tree.item(selected_item)['values']
                    self.vehicle_vin_entry.delete(0, tk.END)
                    self.vehicle_vin_entry.insert(0, vehicle[1])
                    self.vehicle_registration_no_entry.delete(0, tk.END)
                    self.vehicle_registration_no_entry.insert(0, vehicle[2])
                    self.vehicle_year_entry.delete(0, tk.END)
                    self.vehicle_year_entry.insert(0, vehicle[3])
                    self.vehicle_make_entry.delete(0, tk.END)
                    self.vehicle_make_entry.insert(0, vehicle[4])
                    self.vehicle_model_entry.delete(0, tk.END)
                    self.vehicle_model_entry.insert(0, vehicle[5])
                    self.vehicle_color_entry.delete(0, tk.END)
                    self.vehicle_color_entry.insert(0, vehicle[6])

            def add_item(self):
                part_num = self.item_part_num_entry.get()
                short_name = self.item_short_name_entry.get()
                description = self.item_description_entry.get()
                cost = self.item_cost_entry.get()
                num_in_stock = self.item_num_in_stock_entry.get()
                reorder_low = self.item_reorder_low_entry.get()

                if part_num and short_name:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Items (PartNum, ShortName, ItemDescription, Cost, NumInStock, ReorderLow) VALUES (?, ?, ?, ?, ?, ?)",
                                (part_num, short_name, description, cost, num_in_stock, reorder_low))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Item added successfully.")
                    self.view_items()
                else:
                    messagebox.showwarning("Input Error", "Please enter part number and short name.")

            def update_item(self):
                selected_item = self.items_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select an item to update.")
                    return

                item_id = self.items_tree.item(selected_item)['values'][0]
                part_num = self.item_part_num_entry.get()
                short_name = self.item_short_name_entry.get()
                description = self.item_description_entry.get()
                cost = self.item_cost_entry.get()
                num_in_stock = self.item_num_in_stock_entry.get()
                reorder_low = self.item_reorder_low_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Items SET PartNum=?, ShortName=?, ItemDescription=?, Cost=?, NumInStock=?, ReorderLow=? WHERE ItemId=?",
                            (part_num, short_name, description, cost, num_in_stock, reorder_low, item_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item updated successfully.")
                self.view_items()

            def delete_item(self):
                selected_item = self.items_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select an item to delete.")
                    return

                item_id = self.items_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Items WHERE ItemId=?", (item_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Item deleted successfully.")
                self.view_items()

            def clear_item_fields(self):
                self.item_part_num_entry.delete(0, tk.END)
                self.item_short_name_entry.delete(0, tk.END)
                self.item_description_entry.delete(0, tk.END)
                self.item_cost_entry.delete(0, tk.END)
                self.item_num_in_stock_entry.delete(0, tk.END)
                self.item_reorder_low_entry.delete(0, tk.END)

            def view_items(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.items_tree.delete(*self.items_tree.get_children())
                cursor.execute("SELECT * FROM Items")
                for row in cursor.fetchall():
                    self.items_tree.insert("", "end", values=row)
                conn.close()

            def on_item_select(self, event):
                selected_item = self.items_tree.selection()
                if selected_item:
                    item = self.items_tree.item(selected_item)['values']
                    self.item_part_num_entry.delete(0, tk.END)
                    self.item_part_num_entry.insert(0, item[1])
                    self.item_short_name_entry.delete(0, tk.END)
                    self.item_short_name_entry.insert(0, item[2])
                    self.item_description_entry.delete(0, tk.END)
                    self.item_description_entry.insert(0, item[3])
                    self.item_cost_entry.delete(0, tk.END)
                    self.item_cost_entry.insert(0, item[4])
                    self.item_num_in_stock_entry.delete(0, tk.END)
                    self.item_num_in_stock_entry.insert(0, item[5])
                    self.item_reorder_low_entry.delete(0, tk.END)
                    self.item_reorder_low_entry.insert(0, item[6])

            def add_repairman(self):
                first_name = self.repairman_first_name_entry.get()
                last_name = self.repairman_last_name_entry.get()
                mi = self.repairman_mi_entry.get()
                email = self.repairman_email_entry.get()
                mobile = self.repairman_mobile_entry.get()
                h_tel = self.repairman_h_tel_entry.get()
                extension = self.repairman_extension_entry.get()

                if first_name and last_name:
                    conn = sqlite3.connect('repair_shop.db')
                    cursor = conn.cursor()
                    cursor.execute("INSERT INTO Repairmen (FirstName, LastName, MI, Email, Mobile, HTel, Extension) VALUES (?, ?, ?, ?, ?, ?, ?)",
                                (first_name, last_name, mi, email, mobile, h_tel, extension))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("Success", "Repairman added successfully.")
                    self.view_repairmen()
                else:
                    messagebox.showwarning("Input Error", "Please enter first and last name.")

            def update_repairman(self):
                selected_item = self.repairmen_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a repairman to update.")
                    return

                repairman_id = self.repairmen_tree.item(selected_item)['values'][0]
                first_name = self.repairman_first_name_entry.get()
                last_name = self.repairman_last_name_entry.get()
                mi = self.repairman_mi_entry.get()
                email = self.repairman_email_entry.get()
                mobile = self.repairman_mobile_entry.get()
                h_tel = self.repairman_h_tel_entry.get()
                extension = self.repairman_extension_entry.get()

                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("UPDATE Repairmen SET FirstName=?, LastName=?, MI=?, Email=?, Mobile=?, HTel=?, Extension=? WHERE RepairmenId=?",
                            (first_name, last_name, mi, email, mobile, h_tel, extension, repairman_id))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Repairman updated successfully.")
                self.view_repairmen()

            def delete_repairman(self):
                selected_item = self.repairmen_tree.selection()
                if not selected_item:
                    messagebox.showwarning("Selection Error", "Please select a repairman to delete.")
                    return

                repairman_id = self.repairmen_tree.item(selected_item)['values'][0]
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM Repairmen WHERE RepairmenId=?", (repairman_id,))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Repairman deleted successfully.")
                self.view_repairmen()

            def clear_repairman_fields(self):
                self.repairman_first_name_entry.delete(0, tk.END)
                self.repairman_last_name_entry.delete(0, tk.END)
                self.repairman_mi_entry.delete(0, tk.END)
                self.repairman_email_entry.delete(0, tk.END)
                self.repairman_mobile_entry.delete(0, tk.END)
                self.repairman_h_tel_entry.delete(0, tk.END)
                self.repairman_extension_entry.delete(0, tk.END)

            def view_repairmen(self):
                conn = sqlite3.connect('repair_shop.db')
                cursor = conn.cursor()
                self.repairmen_tree.delete(*self.repairmen_tree.get_children())
                cursor.execute("SELECT * FROM Repairmen")
                for row in cursor.fetchall():
                    self.repairmen_tree.insert("", "end", values=row)
                conn.close()

            def on_repairman_select(self, event):
                selected_item = self.repairmen_tree.selection()
                if selected_item:
                    repairman = self.repairmen_tree.item(selected_item)['values']
                    self.repairman_first_name_entry.delete(0, tk.END)
                    self.repairman_first_name_entry.insert(0, repairman[1])
                    self.repairman_last_name_entry.delete(0, tk.END)
                    self.repairman_last_name_entry.insert(0, repairman[2])
                    self.repairman_mi_entry.delete(0, tk.END)
                    self.repairman_mi_entry.insert(0, repairman[3])
                    self.repairman_email_entry.delete(0, tk.END)
                    self.repairman_email_entry.insert(0, repairman[4])
                    self.repairman_mobile_entry.delete(0, tk.END)
                    self.repairman_mobile_entry.insert(0, repairman[5])
                    self.repairman_h_tel_entry.delete(0, tk.END)
                    self.repairman_h_tel_entry.insert(0, repairman[6])
                    self.repairman_extension_entry.delete(0, tk.END)
                    self.repairman_extension_entry.insert(0, repairman[7])

        if __name__ == "__main__":
            root = tk.Tk()
            app = RepairShopApp(root)
            root.mainloop()
    elif txtu!="zoom"and txtp!="zoom2030":
        messagebox.showerror("error","please insert correct user name and password") 
    elif txtu!="zoom":
        messagebox.showerror("error","invalid user name") 
    elif txtp!="zoom2030":
        messagebox.showerror("error","invalid password")
rw.configure(bg="#2c3e50")
# Frame for the Login Form
frame = tk.Frame(rw, bg="#ecf0f1", bd=5, relief=tk.RIDGE)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=320, height=280)

title_label = tk.Label(frame, text="Login page!!!", font=("Arial", 18, "bold"), bg="#ecf0f1", fg="#2c3e50")
title_label.pack(pady=10)

# Username Entry
label_username = tk.Label(frame, text="Username", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
label_username.pack()
entry_username = ttk.Entry(frame, font=("Arial", 12))
entry_username.pack(pady=5, ipady=3)

# Password Entry
label_password = tk.Label(frame, text="Password", font=("Arial", 12), bg="#ecf0f1", fg="#2c3e50")
label_password.pack()
entry_password = ttk.Entry(frame, font=("Arial", 12), show="*")
entry_password.pack(pady=5, ipady=3)

# Login Button
login_button = tk.Button(frame, text="Login", font=("Arial", 12, "bold"), bg="#2c3e50", fg="white", command=log)
login_button.pack(pady=20, ipadx=50, ipady=5)

# Run the application
rw.mainloop()

