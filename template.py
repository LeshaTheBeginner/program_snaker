import tkinter as tk


root = tk.Tk()
root.geometry("400x300")

frame1 = tk.Frame(root, bg="lightblue")
frame1.pack(fill="both", expand=True, padx=10, pady=10)

frame2 = tk.Frame(root, bg="lightgreen")
frame2.pack(fill="both", expand=True, padx=10, pady=10)

label1 = tk.Label(frame1, text="Frame 1")
label1.pack(pady=20)

label2 = tk.Label(frame2, text="Frame 2")
label2.pack(pady=20)

button1 = tk.Button(frame1, text="Click Me")
button1.pack()

button2 = tk.Button(frame2, text="Press Me")
button2.pack()

root.mainloop()