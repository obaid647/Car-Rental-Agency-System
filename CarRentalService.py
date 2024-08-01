import mysql.connector
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import simpledialog

#connect to mysql
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="<password>",
    database="car_rental"
)
#create cursor
mycursor = mydb.cursor()

"""
class that includes GUI creation and methods that the buttons will call
"""
class CarRentalService:
    
    """
    Class constuctor. Creates main window for most GUI frames to be placed on
    """
    def __init__(self, root):
        
        #main window
        self.root = root
        self.root.title("Car Rental Service")
        self.root.geometry("1000x600")
        
        #frame of main window
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        #display login page
        self.show_login_page()

    """
    Creates user login frame. Clears frame and then places login frame on window
    """
    def show_login_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #login title
        tk.Label(self.main_frame, text="Login", font=("Arial", 24)).pack(pady=20)
        
        #email entry box
        tk.Label(self.main_frame, text="Email").pack(pady=5)
        self.email_entry = tk.Entry(self.main_frame)
        self.email_entry.pack(pady=5)
        
        #password entry box
        tk.Label(self.main_frame, text="Password").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)
        
        #login button
        tk.Button(self.main_frame, text="Login", command=self.login).pack(pady=20)
        
        #signup button to show user sign up page
        tk.Button(self.main_frame, text="Sign Up", command=self.show_signup_page).pack(pady=5)
        
        #admin login button to show admin login page
        tk.Button(self.main_frame, text="Admin Login", command=self.show_admin_login_page).pack(pady=5)

    """
    After signup button is pressed on user login page. Create signup frame, clear window, and place frame on window
    """
    def show_signup_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #signup title
        tk.Label(self.main_frame, text="Sign Up", font=("Arial", 24)).pack(pady=20)
        
        #name entry box
        tk.Label(self.main_frame, text="Name").pack(pady=5)
        self.signup_name_entry = tk.Entry(self.main_frame)
        self.signup_name_entry.pack(pady=5)
        
        #email entry box
        tk.Label(self.main_frame, text="Email").pack(pady=5)
        self.signup_email_entry = tk.Entry(self.main_frame)
        self.signup_email_entry.pack(pady=5)
        
        #password entry box
        tk.Label(self.main_frame, text="Password").pack(pady=5)
        self.signup_password_entry = tk.Entry(self.main_frame, show="*")
        self.signup_password_entry.pack(pady=5)
        
        #phone number entry box
        tk.Label(self.main_frame, text="Phone").pack(pady=5)
        self.signup_phone_entry = tk.Entry(self.main_frame)
        self.signup_phone_entry.pack(pady=5)
        
        #sign up button to continue sign up and go to user login page
        tk.Button(self.main_frame, text="Sign Up", command=self.signup).pack(pady=20)
        
        #cancel signup and go to login page
        tk.Button(self.main_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)

    """
    After admin login button is pressed on user login page. Create admin login frame, clear window, and place frame 
    """
    def show_admin_login_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #admin login title
        tk.Label(self.main_frame, text="Admin Login", font=("Arial", 24)).pack(pady=20)
        
        #email entry box
        tk.Label(self.main_frame, text="Email").pack(pady=5)
        self.admin_email_entry = tk.Entry(self.main_frame)
        self.admin_email_entry.pack(pady=5)
        
        #password entry box
        tk.Label(self.main_frame, text="Password").pack(pady=5)
        self.admin_password_entry = tk.Entry(self.main_frame, show="*")
        self.admin_password_entry.pack(pady=5)
        
        #login button
        tk.Button(self.main_frame, text="Login", command=self.admin_login).pack(pady=20)
        
        #signup button to go to admin signup page
        tk.Button(self.main_frame, text="Admin Sign Up", command=self.show_admin_signup_page).pack(pady=5)
        
        #back button to go back to user login page
        tk.Button(self.main_frame, text="Back to Login", command=self.show_login_page).pack(pady=5)
    
    """
    After admin signup button is pressed on admin login page. Create admin signup frame, clear window, and place frame 
    """
    def show_admin_signup_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #admin signup title
        tk.Label(self.main_frame, text="Admin Sign Up", font=("Arial", 24)).pack(pady=20)
        
        #name entry box
        tk.Label(self.main_frame, text="Name").pack(pady=5)
        self.admin_signup_name_entry = tk.Entry(self.main_frame)
        self.admin_signup_name_entry.pack(pady=5)
        
        #email entry box
        tk.Label(self.main_frame, text="Email").pack(pady=5)
        self.admin_signup_email_entry = tk.Entry(self.main_frame)
        self.admin_signup_email_entry.pack(pady=5)
        
        #password entry box
        tk.Label(self.main_frame, text="Password").pack(pady=5)
        self.admin_signup_password_entry = tk.Entry(self.main_frame, show="*")
        self.admin_signup_password_entry.pack(pady=5)
        
        #phone number entry box
        tk.Label(self.main_frame, text="Phone").pack(pady=5)
        self.admin_signup_phone_entry = tk.Entry(self.main_frame)
        self.admin_signup_phone_entry.pack(pady=5)
        
        #sign up button to continue signup and go to admin login page
        tk.Button(self.main_frame, text="Sign Up", command=self.admin_signup).pack(pady=20)
        
        #back button to go to admin login page
        tk.Button(self.main_frame, text="Back to Admin Login", command=self.show_admin_login_page).pack(pady=5)
    
    """
    After login button is pressed on user login page. Search for matching email and password.
    Error message if not found. Main page displayed if found
    """
    def login(self):
        
        #get email and password from entry box
        email = self.email_entry.get()
        password = self.password_entry.get()
        
        #search for customer with email and password
        mycursor.execute("SELECT * FROM customers WHERE email=%s AND password=%s", (email, password))
        
        #fetch the user 
        user = mycursor.fetchone()
        
        #if user exists
        if user:
            #get userID and go to user main page
            self.user_id = user[0]
            self.show_user_main_page()
        
        #user does not exist
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    """
    After signup button is pressed on user signup page. Insert customer into database. 
    Show success message and load user login frame
    """
    def signup(self):
        
        #get data from entry boxes
        name = self.signup_name_entry.get()
        email = self.signup_email_entry.get()
        password = self.signup_password_entry.get()
        phone = self.signup_phone_entry.get()
        
        #create customer and insert into database
        mycursor.execute("INSERT INTO customers (name, email, password, phone) VALUES (%s, %s, %s, %s)", 
                         (name, email, password, phone))
        mydb.commit()
        
        #success message and return to user login page
        messagebox.showinfo("Success", "Signup successful")
        self.show_login_page()

    """
    After login button is pressed on admin login page. Search for matching email and password.
    Error message if not found. Main admin page displayed if found
    """
    def admin_login(self):
        
        #get email and password from entry boxes
        email = self.admin_email_entry.get()
        password = self.admin_password_entry.get()
        
        #find admin that has email and password
        mycursor.execute("SELECT * FROM admins WHERE email=%s AND password=%s", (email, password))
        
        #fetch the admin
        admin = mycursor.fetchone()
        
        #if user exists
        if admin:
            #get adminID and go to admin main page
            self.admin_id = admin[0]
            self.show_admin_main_page()
        
        #if user does not exist
        else:
            messagebox.showerror("Error", "Invalid login credentials")

    """
    After signup button is pressed on admin signup page. Insert admin into database. 
    Show success message and load admin login frame
    """
    def admin_signup(self):
        
        #get admin info from entry boxes
        name = self.admin_signup_name_entry.get()
        email = self.admin_signup_email_entry.get()
        password = self.admin_signup_password_entry.get()
        phone = self.admin_signup_phone_entry.get()
        
        #create admin and insert into database
        mycursor.execute("INSERT INTO admins (name, email, password, phone) VALUES (%s, %s, %s, %s)", 
                         (name, email, password, phone))
        mydb.commit()
        
        #success message and return to admin login page
        messagebox.showinfo("Success", "Admin signup successful")
        self.show_admin_login_page()

    """
    Create main frame for user. Clear window and display frame
    """
    def show_user_main_page(self):
        
        #clear frame 
        self.clear_frame()
        
        #display drop down menu
        self.setup_menu(self.show_login_page)
        
        #user main page title
        tk.Label(self.main_frame, text="Available Cars", font=("Arial", 24)).pack(pady=20)
        
        #treeview to display cars 
        self.car_tree = ttk.Treeview(self.main_frame, columns=("car_id", "make", "model", "year", "price"), show="headings")
        
        #treeview headings
        self.car_tree.heading("car_id", text="Car ID")
        self.car_tree.heading("make", text="Make")
        self.car_tree.heading("model", text="Model")
        self.car_tree.heading("year", text="Year")
        self.car_tree.heading("price", text="Price")
        
        #put treeview on main frame
        self.car_tree.pack(pady=20, fill=tk.BOTH, expand=True)
        
        #enter car information into treeview
        self.load_cars()
        
        #frame to hold buttons
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=20)
        
        #book car button to open window to enter booking details for selected car
        tk.Button(btn_frame, text="Book Car", command=self.book_car_page).pack(side=tk.LEFT, padx=10)
        
        #view bookings button to open window to view that users orders
        tk.Button(btn_frame, text="View Bookings", command=self.view_bookings_page).pack(side=tk.LEFT, padx=10)

    """
    Create main frame for admin. Clear window and display frame
    """
    def show_admin_main_page(self):
        
        #clear main frame
        self.clear_frame()
        
        #setup main frame for admin main page
        self.setup_menu(self.show_admin_login_page)
        
        #manage cars title
        tk.Label(self.main_frame, text="Manage Cars", font=("Arial", 24)).pack(pady=20)
        
        #create tree view to view cars
        self.car_tree = ttk.Treeview(self.main_frame, columns=("car_id", "make", "model", "year", "price"), show="headings")
        
        #treeview headings
        self.car_tree.heading("car_id", text="Car ID")
        self.car_tree.heading("make", text="Make")
        self.car_tree.heading("model", text="Model")
        self.car_tree.heading("year", text="Year")
        self.car_tree.heading("price", text="Price")
        
        #put treeview on main frame
        self.car_tree.pack(pady=20, fill=tk.BOTH, expand=True)
        
        #enter car information into treeview
        self.load_cars()
        
        #frame to hold buttons
        btn_frame = tk.Frame(self.main_frame)
        btn_frame.pack(pady=20)
        
        #update car button to open window to update car information
        tk.Button(btn_frame, text="Update Car", command=self.update_car_page).pack(side=tk.LEFT, padx=10)
        
        #view bookings button to open window to view all user bookings
        tk.Button(btn_frame, text="View Bookings", command=self.view_all_bookings_page).pack(side=tk.LEFT, padx=10)
        
        #add car button to add a new car to treeview
        tk.Button(self.main_frame, text="Add Car", command=self.add_car_page).pack(pady=20)

    """
    After book car button is clicked for user. Open window to confirm booking details.
    """
    def book_car_page(self):
        
        #get selected car
        selected_car = self.car_tree.selection()
        
        #if no car selected
        if not selected_car:
            messagebox.showerror("Error", "No car selected")
            return
        
        #get carID
        car_id = self.car_tree.item(selected_car[0])["values"][0]
        
        #create new window
        self.car_booking_window = tk.Toplevel(self.root)
        self.car_booking_window.title("Book Car")
        self.car_booking_window.geometry("400x400")
        
        #from date entry box
        tk.Label(self.car_booking_window, text="From Date (YYYY-MM-DD)").pack(pady=5)
        self.from_date_entry = tk.Entry(self.car_booking_window)
        self.from_date_entry.pack(pady=5)
        
        #to date entry box
        tk.Label(self.car_booking_window, text="To Date (YYYY-MM-DD)").pack(pady=5)
        self.to_date_entry = tk.Entry(self.car_booking_window)
        self.to_date_entry.pack(pady=5)
        
        #cardholder name entry box
        tk.Label(self.car_booking_window, text="Cardholder Name").pack(pady=5)
        self.carholder_name = tk.Entry(self.car_booking_window)
        self.carholder_name.pack(pady=5)
        
        #payment card info entry box
        tk.Label(self.car_booking_window, text="Payment Card Number").pack(pady=5)
        self.card_num = tk.Entry(self.car_booking_window)
        self.card_num.pack(pady=5)
        
        #cvv entry box
        tk.Label(self.car_booking_window, text="CVV Number").pack(pady=5)
        self.cvv_num = tk.Entry(self.car_booking_window)
        self.cvv_num.pack(pady=5)
        
        #book button to create an order
        tk.Button(self.car_booking_window, text="Book", command=lambda: self.book_car(car_id)).pack(pady=20)

    """
    After Book button is clicked on book car window. Insert order into database
    """
    def book_car(self, car_id):
        
        #get from and to date from entry box
        from_date = self.from_date_entry.get()
        to_date = self.to_date_entry.get()
        
        #check for booking conflicts
        mycursor.execute("""
            SELECT * FROM orders
            WHERE car_id = %s
            AND ((from_date <= %s AND to_date >= %s)
            OR (from_date <= %s AND to_date >= %s)
            OR (from_date >= %s AND to_date <= %s))
        """, (car_id, from_date, from_date, to_date, to_date, from_date, to_date))
        
        #fetch conflicts
        conflict = mycursor.fetchall()
        
        #if conflict exists
        if conflict:
            messagebox.showerror("Error", "Car is already booked for the selected dates.")
        
        #no conflict
        else:
            
            #create and insert order
            mycursor.execute("INSERT INTO orders (customer_id, car_id, from_date, to_date, status) VALUES (%s, %s, %s, %s, %s)", 
                            (self.user_id, car_id, from_date, to_date, "Booked"))
            mydb.commit()
            
            #success message and close booking window
            messagebox.showinfo("Success", "Car booked successfully")
            self.car_booking_window.destroy()
    
    """
    After view bookings button is clocked on user main page. Open new window to display orders
    """
    def view_bookings_page(self):
        
        #create new window
        self.bookings_window = tk.Toplevel(self.root)
        self.bookings_window.title("My Bookings")
        self.bookings_window.geometry("1200x400")
        
        #my bookings title
        tk.Label(self.bookings_window, text="My Bookings", font=("Arial", 24)).pack(pady=20)
        
        #create treeview to display order information
        self.bookings_tree = ttk.Treeview(self.bookings_window, columns=("make", "model", "year", "from_date", "to_date", "status"), show="headings")
        
        #treeview headings
        self.bookings_tree.heading("make", text="Make")
        self.bookings_tree.heading("model", text="Model")
        self.bookings_tree.heading("year", text="Year")
        self.bookings_tree.heading("from_date", text="From Date")
        self.bookings_tree.heading("to_date", text="To Date")
        self.bookings_tree.heading("status", text="Status")
        
        #put treeview on window
        self.bookings_tree.pack(pady=20, fill=tk.BOTH, expand=True)
        
        #load orders into treeview
        self.load_bookings()

    """
    After view all bookings button is clocked on admin main page. Open new window to display orders
    """
    def view_all_bookings_page(self):
        
        #create window for bookings page
        self.all_bookings_window = tk.Toplevel(self.root)
        self.all_bookings_window.title("All Bookings")
        self.all_bookings_window.geometry("1200x400")
        
        #all bookings title
        tk.Label(self.all_bookings_window, text="All Bookings", font=("Arial", 24)).pack(pady=20)
        
        #create treeview to display order information
        self.all_bookings_tree = ttk.Treeview(self.all_bookings_window, columns=("order_id", "customer_id", "car_id", "from_date", "to_date", "status"), show="headings")
        
        #treeview headings
        self.all_bookings_tree.heading("order_id", text="Order ID")
        self.all_bookings_tree.heading("customer_id", text="Customer ID")
        self.all_bookings_tree.heading("car_id", text="Car ID")
        self.all_bookings_tree.heading("from_date", text="From Date")
        self.all_bookings_tree.heading("to_date", text="To Date")
        self.all_bookings_tree.heading("status", text="Status")
        
        #put tree view on window
        self.all_bookings_tree.pack(pady=20, fill=tk.BOTH, expand=True)
        
        #load order information onto treeview
        self.load_all_bookings()

    """
    After update car button is selected on admin main page. Open new window for entries of car information
    """
    def update_car_page(self):
        
        #get car selected in treeview
        selected_car = self.car_tree.selection()
        
        #if no car selected
        if not selected_car:
            messagebox.showerror("Error", "No car selected")
            return
        
        #get carID of selection
        car_id = self.car_tree.item(selected_car[0])["values"][0]
        
        #create new window to update car 
        self.car_update_window = tk.Toplevel(self.root)
        self.car_update_window.title("Update Car")
        self.car_update_window.geometry("400x300")
        
        #make entry box
        tk.Label(self.car_update_window, text="Make").pack(pady=5)
        self.update_make_entry = tk.Entry(self.car_update_window)
        self.update_make_entry.pack(pady=5)
        
        #model entry box
        tk.Label(self.car_update_window, text="Model").pack(pady=5)
        self.update_model_entry = tk.Entry(self.car_update_window)
        self.update_model_entry.pack(pady=5)
        
        #year entry box
        tk.Label(self.car_update_window, text="Year (YYYY)").pack(pady=5)
        self.update_year_entry = tk.Entry(self.car_update_window)
        self.update_year_entry.pack(pady=5)
        
        #price entry box
        tk.Label(self.car_update_window, text="Price").pack(pady=5)
        self.update_price_entry = tk.Entry(self.car_update_window)
        self.update_price_entry.pack(pady=5)
        
        #update button to update the car information in db
        tk.Button(self.car_update_window, text="Update", command=lambda: self.update_car(car_id)).pack(pady=20)

    """
    After update button is clicked on update car window. Update car information on database and reload cars on main page
    """
    def update_car(self, car_id):
        
        #get car info
        make = self.update_make_entry.get()
        model = self.update_model_entry.get()
        year = self.update_year_entry.get()
        price = self.update_price_entry.get()
        
        #update car in db
        mycursor.execute("UPDATE cars SET make=%s, model=%s, year=%s, price=%s WHERE car_id=%s", 
                         (make, model, year, price, car_id))
        mydb.commit()
        messagebox.showinfo("Success", "Car updated successfully")
        
        #close update window
        self.car_update_window.destroy()
        
        #reload cars in main treeview
        self.load_cars()

    """
    After add car button is clicked on admin main page. Open new window for entries of car information
    """
    def add_car_page(self):
        
        #create new window
        self.car_add_window = tk.Toplevel(self.root)
        self.car_add_window.title("Add Car")
        self.car_add_window.geometry("400x300")
        
        #make entry box
        tk.Label(self.car_add_window, text="Make").pack(pady=5)
        self.add_make_entry = tk.Entry(self.car_add_window)
        self.add_make_entry.pack(pady=5)
        
        #model entry box
        tk.Label(self.car_add_window, text="Model").pack(pady=5)
        self.add_model_entry = tk.Entry(self.car_add_window)
        self.add_model_entry.pack(pady=5)
        
        #year entry box
        tk.Label(self.car_add_window, text="Year (YYYY)").pack(pady=5)
        self.add_year_entry = tk.Entry(self.car_add_window)
        self.add_year_entry.pack(pady=5)
        
        #price entry box
        tk.Label(self.car_add_window, text="Price").pack(pady=5)
        self.add_price_entry = tk.Entry(self.car_add_window)
        self.add_price_entry.pack(pady=5)
        
        #add button to add car into db
        tk.Button(self.car_add_window, text="Add", command=self.add_car).pack(pady=20)

    """
    After add button is clicked on add car window. Insert new car into database and reload cars on main page.
    """
    def add_car(self):
        
        #get car info
        make = self.add_make_entry.get()
        model = self.add_model_entry.get()
        year = self.add_year_entry.get()
        price = self.add_price_entry.get()
        
        #create car and insert into db
        mycursor.execute("INSERT INTO cars (make, model, year, price) VALUES (%s, %s, %s, %s)", 
                         (make, model, year, price))
        mydb.commit()
        messagebox.showinfo("Success", "Car added successfully")
        
        #close add car window 
        self.car_add_window.destroy()
        
        #reload cars in main treeview
        self.load_cars()
    
    """
    Clear tree view then retrieve car information from database and insert into tree view
    """
    def load_cars(self):
        
        #iterate through treeview
        for i in self.car_tree.get_children():
            
            #delete car
            self.car_tree.delete(i)
            
        #retrieve all cars 
        mycursor.execute("SELECT * FROM cars")
        
        #fetch all car data
        cars = mycursor.fetchall()
        
        #for each car
        for car in cars:
            
            #insert into treeview
            self.car_tree.insert("", "end", values=car)

    """
    Clear tree view then retrieve order information from database and insert into tree view of user booking window
    """
    def load_bookings(self):
        
        #iterate through treeview
        for i in self.bookings_tree.get_children():
            
            #delete order
            self.bookings_tree.delete(i)
        
        #retrieve all orders where order customerID is equal to userID
        mycursor.execute("SELECT c.make, c.model, c.year, o.from_date, o.to_date, o.status FROM orders o JOIN cars c ON o.car_id=c.car_id WHERE o.customer_id=%s", 
                         (self.user_id,))
        
        #fetch all orders
        bookings = mycursor.fetchall()
        
        #iterate through orders
        for booking in bookings:
            
            #insert into treeview
            self.bookings_tree.insert("", "end", values=booking)

    """
    Clear tree view then retrieve order information from database and insert into tree view of admin booking window    
    """
    def load_all_bookings(self):
        
        #iterate through all bookings
        for i in self.all_bookings_tree.get_children():
            
            #delete booking
            self.all_bookings_tree.delete(i)
        
        #retrieve all orders
        mycursor.execute("SELECT * FROM orders")
        
        #fetch all orders
        bookings = mycursor.fetchall()
        
        #iterate through orders
        for booking in bookings:
            
            #insert into treeview
            self.all_bookings_tree.insert("", "end", values=booking)
            
    """
    Create menu bar at top of main pages for logout/exit  
    """
    def setup_menu(self, logout_command):
        
        #create menubar
        menubar = tk.Menu(self.root)

        #create menu in menubar
        filemenu = tk.Menu(menubar, tearoff=0)
        
        #add logout command to return to user/admin login page
        filemenu.add_command(label="Logout", command=logout_command)
        
        #add exit command to exit program
        filemenu.add_command(label="Exit", command=self.root.quit)
        
        #add dropdown in menu
        menubar.add_cascade(label="File", menu=filemenu)
        
        #configure menu of main window
        self.root.config(menu=menubar)

    """
    Wipe window
    """
    def clear_frame(self):
        
        #iterate through main frame
        for widget in self.main_frame.winfo_children():
            
            #delete
            widget.destroy()

def main():
    
    #create root object
    root = tk.Tk()

    #create CarRentalService GUI
    app = CarRentalService(root)

    #run GUI
    root.mainloop()

main()
