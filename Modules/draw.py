import tkinter as tk
import tkinter.font as tkfont

window = tk.Tk()
window.title("Drawn Window")
window.config(bg="lightblue")  # Add a background color

my_font = tkfont.Font(family="Helvetica", size=12, weight="bold")  # Adjust as needed

label = tk.Label(window, text="This is a drawn window", font=my_font, bg="lightblue")
label.pack()

button = tk.Button(window, text="Close", command=window.destroy)  # Example button
button.pack()

window.mainloop()
