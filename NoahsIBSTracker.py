from customtkinter import *
import tkinter as tk
import sqlite3
from datetime import datetime
from datetime import datetime, timedelta




app = CTk()
app.geometry("500x500")

def login_page():

  for widget in app.winfo_children():
    widget.destroy()

  title = CTkLabel(master=app, text="Login Page", font=("Arial", 24))
  title.pack(pady=10, padx=10)
  
  login_frame = CTkFrame(master=app, fg_color="grey")
  login_frame.pack(expand=True)

  login_textbox = CTkEntry(master=login_frame, placeholder_text="Username")
  password1_textbox = CTkEntry(master=login_frame, placeholder_text="Password")
  login_btn = CTkButton(master=login_frame, text="Login",command=lambda: check_login_details(login_textbox, password1_textbox))
  create_acc_btn = CTkButton(master=login_frame, text="Create account",command=create_account_page)


  login_textbox.pack(padx=20, pady=30)
  password1_textbox.pack(padx=20, pady=0)
  login_btn.pack(padx=20, pady=10, anchor="center")
  create_acc_btn.pack(padx=20, pady=20, anchor="center")



  def track_meal(username):
    for widget in app.winfo_children():
      widget.destroy()
      
    meal_date = datetime.today().strftime('%Y-%m-%d')

    track_meal_frame = CTkFrame(master=app, fg_color="grey")
    track_meal_frame.pack(expand=True)

    
    title = CTkLabel(master=track_meal_frame, text="Does your meal have the following content:", font=("Arial", 12))
    
    checkbutton1 = CTkCheckBox(master=track_meal_frame, text="Apples")
    checkbutton2 = CTkCheckBox(master=track_meal_frame, text="Beans")
    checkbutton3 = CTkCheckBox(master=track_meal_frame, text="Broccoli")
    checkbutton4 = CTkCheckBox(master=track_meal_frame, text="Cabbage")
    checkbutton5 = CTkCheckBox(master=track_meal_frame, text="Caffeine")
    checkbutton6 = CTkCheckBox(master=track_meal_frame, text="Cauliflower")
    checkbutton7 = CTkCheckBox(master=track_meal_frame, text="Gum")
    checkbutton8 = CTkCheckBox(master=track_meal_frame, text="Chocolates")
    checkbutton9 = CTkCheckBox(master=track_meal_frame, text="Diary products")
    checkbutton10 = CTkCheckBox(master=track_meal_frame, text="Fatty foods")
    checkbutton11 = CTkCheckBox(master=track_meal_frame, text="Margarine")
    checkbutton12 = CTkCheckBox(master=track_meal_frame, text="Nuts")
    checkbutton13 = CTkCheckBox(master=track_meal_frame, text="Orange & Grapefruit juices")
    checkbutton14 = CTkCheckBox(master=track_meal_frame, text="Wheat products")
    checkbutton15 = CTkCheckBox(master=track_meal_frame, text="None of the above")
    confirm_meal_btn = CTkButton(master=track_meal_frame, text="Confirm",command=lambda: confirm_meal(username))
    back_btn = CTkButton(master=track_meal_frame, text="Back",command=lambda: home_page(username))
    
    title.pack(pady=10, padx=10)
    checkbutton1.pack()
    checkbutton2.pack()
    checkbutton3.pack()
    checkbutton4.pack()
    checkbutton5.pack()
    checkbutton6.pack()
    checkbutton7.pack()
    checkbutton8.pack()
    checkbutton9.pack()
    checkbutton10.pack()
    checkbutton11.pack()
    checkbutton12.pack()
    checkbutton13.pack()
    checkbutton14.pack()
    checkbutton15.pack()
    confirm_meal_btn.pack(padx=20, pady=10)
    back_btn.pack(padx=20, pady=10)


    def confirm_meal(username):

      
      file_name = username + "_meal_data"
      date = datetime.today().strftime('%Y-%m-%d')
      
      food1 = int(checkbutton1.get())
      food2 = int(checkbutton2.get())
      food3 = int(checkbutton3.get())
      food4 = int(checkbutton4.get())
      food5 = int(checkbutton5.get())
      food6 = int(checkbutton6.get())
      food7 = int(checkbutton7.get())
      food8 = int(checkbutton8.get())
      food9 = int(checkbutton9.get())
      food10 = int(checkbutton10.get())
      food11 = int(checkbutton11.get())
      food12 = int(checkbutton12.get())
      food13 = int(checkbutton13.get())
      food14 = int(checkbutton14.get())
      none = int(checkbutton15.get())

      conn = sqlite3.connect(file_name)
      cursor = conn.cursor()

      cursor.execute('''
          CREATE TABLE IF NOT EXISTS meals (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              meal_content TEXT UNIQUE NOT NULL,
              date DATE
          )
      ''')
      

      if none == 1:
        home_page(username)

      else:

        if food1 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Apples", date))
          conn.commit()
          
        if food2 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Beans", date))
          conn.commit()

        if food3 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Broccoli", date))
          conn.commit()
      
        if food4 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Cabbage", date))
          conn.commit()
        
        if food5 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Caffeine", date))
          conn.commit()

        if food6 == 1:
           cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Cauliflower", date))
           conn.commit()

        if food7 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Gum", date))
          conn.commit()

        if food8 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Chocolate", date))
          conn.commit()

        if food9 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Diary products", date))
          conn.commit()

        if food10 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Fatty foods", date))
          conn.commit()

        if food11 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Margarine", date))
          conn.commit()

        if food12 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Nuts", date))
          conn.commit()

        if food13 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Orange & Grapefruit", date))
          conn.commit()

        if food14 == 1:
          cursor.execute("INSERT INTO meals (meal_content, date) VALUES (?, ?)", ("Wheat products", date))
          conn.commit()

        cursor.execute("SELECT * FROM meals")
        rows = cursor.fetchall()
        for row in rows:
          print(row)

          
        conn.commit()
        conn.close()
      

        print("meal confirmed")
        home_page(username)

  def track_pain(username):

    for widget in app.winfo_children():
      widget.destroy()

    pain_frame = CTkFrame(master=app, fg_color="grey")
    pain_frame.pack(expand=True)

    title = CTkLabel(master=pain_frame, text="Having stomach pain?", font=("Arial", 24))
    warning1 = CTkLabel(master=pain_frame, text="Can only track every 30 minutes", font=("Arial", 10))
    warning2 = CTkLabel(master=pain_frame, text="Track your level of pain:", font=("Arial", 15))
    level_of_pain_btn1 = CTkButton(master=pain_frame, text="Moderate",command=lambda: record_pain(username,pain_frame,"Moderate"))
    level_of_pain_btn2 = CTkButton(master=pain_frame, text="Extreme",command=lambda: record_pain(username,pain_frame,"Extreme"))
    back_btn = CTkButton(master=pain_frame, text="Back",command=lambda: home_page(username))

    title.pack(padx=20, pady=20, anchor="center")
    warning1.pack()
    warning2.pack()
    level_of_pain_btn1.pack(padx=20, pady=20, anchor="center")
    level_of_pain_btn2.pack(padx=20, pady=20, anchor="center")
    back_btn.pack()

    def record_pain(username,pain_frame,pain_level):
    
      file_name = username + "_pain_data"
    
      # Get current date and time
      pain_date = datetime.today().strftime('%Y-%m-%d')
      now = datetime.now()
      current_hour = now.hour
      current_minute = now.minute

    # Connect to the SQLite database
      conn = sqlite3.connect(file_name)
      cursor = conn.cursor()

    # Create the table if it doesn't exist
      cursor.execute('''
          CREATE TABLE IF NOT EXISTS pain (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              level TEXT UNIQUE NOT NULL,
              date DATE,
              hours INTEGER,
              minutes INTEGER
          )
      ''')

      cursor.execute("SELECT date, hours, minutes FROM pain ORDER BY id DESC LIMIT 1")
      last_entry = cursor.fetchone()

      if last_entry:
          last_date, last_hour, last_minute = last_entry
        
          last_recorded_time = datetime.strptime(last_date, '%Y-%m-%d').replace(hour=last_hour, minute=last_minute)
        
          time_difference = now - last_recorded_time

          if time_difference <= timedelta(minutes=30):
            warning_message = (f"Last record was at {last_hour}:{last_minute}")
            warning2 = CTkLabel(master=pain_frame, text=warning_message, font=("Arial", 10))
            warning2.pack()
            conn.close()
            return
          else:
            print(f"Last record was {time_difference} ago. Recording new data...")
    
    # Insert new pain tracking record
      cursor.execute("INSERT INTO pain (date, hours, minutes, level) VALUES (?, ?, ?, ?)", (pain_date, current_hour, current_minute, pain_level))

    # Commit the changes and close the connection
      conn.commit()
      conn.close()

      print("New symptoms tracked.")
    

  
    

  def home_page(username):
    for widget in app.winfo_children():
      widget.destroy()

    home_frame = CTkFrame(master=app, fg_color="grey")
    

    title = CTkLabel(master=app, text="Home Page", font=("Arial", 24))
    meal_btn = CTkButton(master=home_frame, text="Track meal",command=lambda: track_meal(username))
    pain_btn = CTkButton(master=home_frame, text="Record symptoms",command=lambda: track_pain(username))
    view_btn = CTkButton(master=home_frame, text="view data",command=lambda: track_pain(username))
    


    title.pack(padx=20, pady=20, anchor="center")
    home_frame.pack(expand=True)
    meal_btn.pack(padx=20, pady=20, anchor="center")
    pain_btn.pack(padx=20, pady=5, anchor="center")
    view_btn.pack(padx=20, pady=5, anchor="center")
    
    

  
  def check_login_details(login_textbox, password1_textbox):
    username = login_textbox.get()
    password = password1_textbox.get()
    
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM logins WHERE username = ? AND password = ?", (username, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        print("Login successful!")
        home_page(username)
          
    else:
        print("Invalid username or password.")
        



def create_account_page():
  
  for widget in app.winfo_children():
    widget.destroy()

  title = CTkLabel(master=app, text="Create account", font=("Arial", 24))
  title.pack(pady=20, padx=20)
  
  createaccount_frame = CTkFrame(master=app, fg_color="grey")
  createaccount_frame.pack(expand=True)

  user_textbox = CTkEntry(master=createaccount_frame, placeholder_text="Username")
  password_textbox = CTkEntry(master=createaccount_frame, placeholder_text="Password")
  
  create_acc_btn = CTkButton(master=createaccount_frame, text="Create account",command=lambda: create_account(user_textbox,password_textbox,createaccount_frame))
  back_btn = CTkButton(master=createaccount_frame, text="Back",command=login_page)

  user_textbox.pack(padx=20, pady=30)
  password_textbox.pack(padx=20, pady=0)
  create_acc_btn.pack(padx=20, pady=30, anchor="center")
  back_btn.pack(padx=20, pady=30)
  
def create_account(user_textbox,password_textbox,createaccount_frame):
  global username 
  username = user_textbox.get()
  password = password_textbox.get()

  conn = sqlite3.connect('users.db')
  cursor = conn.cursor()
  
  cursor.execute('''
      CREATE TABLE IF NOT EXISTS logins (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          username TEXT UNIQUE NOT NULL,
          password TEXT NOT NULL,
          date DATE
      )
  ''')
  
  conn.commit()
  conn.close()

  def check_username_exists(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("SELECT 1 FROM logins WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    return bool(result)  # Return True if a row was found, False otherwise

  start_date = datetime.today().strftime('%Y-%m-%d')
  
  username_to_check = username
  if check_username_exists(username_to_check):
    username_exists_label = CTkLabel(master=createaccount_frame, text="username exists", font=("Arial", 8))
    username_exists_label.pack(pady=20, padx=20)
    user_textbox.delete(0, tk.END)
    password_textbox.delete(0, tk.END)
  
  else:
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO logins (username, password, date) VALUES (?, ?, ?)", (username, password, start_date))
    
    print("Account created successfully!")

    account_created_label = CTkLabel(master=createaccount_frame, text="Account created", font=("Arial", 8))
    account_created_label.pack(pady=20, padx=20)

    cursor.execute("SELECT * FROM logins")
    rows = cursor.fetchall()
    for row in rows:
      print(row)
      
    conn.commit()
    conn.close()


login_page()


app.mainloop()



  