import sqlite3
from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

# Connect to SQLite database (it will create a new database if it doesn't exist)
conn = sqlite3.connect('fitness_tracker.db')
cursor = conn.cursor()

# Create tables for storing exercise and meal data
cursor.execute('''CREATE TABLE IF NOT EXISTS exercises (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    exercise TEXT,
                    duration INTEGER,
                    calories_burned INTEGER
                  )''')

cursor.execute('''CREATE TABLE IF NOT EXISTS meals (
                    id INTEGER PRIMARY KEY,
                    date TEXT,
                    meal TEXT,
                    calories INTEGER
                  )''')
conn.commit()

# Function to add an exercise entry
def add_exercise():
    date = entry_date.get()
    exercise = entry_exercise.get()
    duration = int(entry_duration.get())
    calories_burned = int(entry_calories_burned.get())

    cursor.execute("INSERT INTO exercises (date, exercise, duration, calories_burned) VALUES (?, ?, ?, ?)",
                   (date, exercise, duration, calories_burned))
    conn.commit()
    messagebox.showinfo("Success", "Exercise entry added successfully!")

# Function to add a meal entry
def add_meal():
    date = entry_date.get()
    meal = entry_meal.get()
    calories = int(entry_calories.get())

    cursor.execute("INSERT INTO meals (date, meal, calories) VALUES (?, ?, ?)",
                   (date, meal, calories))
    conn.commit()
    messagebox.showinfo("Success", "Meal entry added successfully!")

# Function to generate a report of total calories burned and consumed
def generate_report():
    cursor.execute("SELECT SUM(calories_burned) FROM exercises")
    total_burned = cursor.fetchone()[0]
    cursor.execute("SELECT SUM(calories) FROM meals")
    total_consumed = cursor.fetchone()[0]

    total_burned = total_burned if total_burned else 0
    total_consumed = total_consumed if total_consumed else 0

    messagebox.showinfo("Report", f"Total Calories Burned: {total_burned}\nTotal Calories Consumed: {total_consumed}")

    # Plotting data visualization
    labels = ['Calories Burned', 'Calories Consumed']
    values = [total_burned, total_consumed]

    plt.bar(labels, values, color=['blue', 'red'])
    plt.title("Calories Burned vs. Consumed")
    plt.ylabel("Calories")
    plt.show()

# GUI Setup
root = Tk()
root.title("Health and Fitness Tracker")

# Date input
label_date = Label(root, text="Date (YYYY-MM-DD):")
label_date.grid(row=0, column=0)
entry_date = Entry(root)
entry_date.grid(row=0, column=1)

# Exercise input
label_exercise = Label(root, text="Exercise:")
label_exercise.grid(row=1, column=0)
entry_exercise = Entry(root)
entry_exercise.grid(row=1, column=1)

# Duration input
label_duration = Label(root, text="Duration (minutes):")
label_duration.grid(row=2, column=0)
entry_duration = Entry(root)
entry_duration.grid(row=2, column=1)

# Calories burned input
label_calories_burned = Label(root, text="Calories Burned:")
label_calories_burned.grid(row=3, column=0)
entry_calories_burned = Entry(root)
entry_calories_burned.grid(row=3, column=1)

# Meal input
label_meal = Label(root, text="Meal:")
label_meal.grid(row=4, column=0)
entry_meal = Entry(root)
entry_meal.grid(row=4, column=1)

# Calories input for meal
label_calories = Label(root, text="Calories (Meal):")
label_calories.grid(row=5, column=0)
entry_calories = Entry(root)
entry_calories.grid(row=5, column=1)

# Add Exercise Button
button_add_exercise = Button(root, text="Add Exercise", command=add_exercise)
button_add_exercise.grid(row=6, column=0)

# Add Meal Button
button_add_meal = Button(root, text="Add Meal", command=add_meal)
button_add_meal.grid(row=6, column=1)

# Generate Report Button
button_generate_report = Button(root, text="Generate Report", command=generate_report)
button_generate_report.grid(row=7, column=0, columnspan=2)

root.mainloop()

# Close the connection when the application is closed
conn.close()
