import tkinter as tk
from datetime import datetime
import pytz

# Set your time zone
timezone = pytz.timezone('Asia/Kolkata')  # Replace with your timezone

# Function to update the time and date
def update_time():
    now = datetime.now(timezone)
    current_time = now.strftime('%H:%M:%S %p')  # Time in HH:MM:SS AM/PM format
    current_date = now.strftime('%A, %d %B %Y')  # Date in Day, DD Month YYYY format
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)  # Update every second

# Create the main window
root = tk.Tk()
root.title("Digital Clock by Anees")

# Configure the window background
root.configure(background='lightcyan')

# Create and configure the date label
date_label = tk.Label(root, font=('calibri', 20), background='lightcyan', foreground='black')
date_label.pack(anchor='n', pady=10)

# Create and configure the time label
time_label = tk.Label(root, font=('calibri', 40, 'bold'), background='lightcyan', foreground='darkblue')
time_label.pack(anchor='center', pady=20)

# Initial call to display time and date
update_time()

# Run the application
root.mainloop()
