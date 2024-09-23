import tkinter as tk

# Create a root window
root = tk.Tk()

# Set window title and size
root.title("My Tkinter App")
root.geometry("300x200")

# Add a label
label = tk.Label(root, text="Hello, Tkinter!")
label.pack(pady=20)

# Add a button to close the window
button = tk.Button(root, text="Close", command=root.quit)
button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()