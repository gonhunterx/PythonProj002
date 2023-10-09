import tkinter as tk


window = tk.Tk()
window.geometry("600x450")
window.title("My first GUI")


label = tk.Label(window, text="Hello World", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(window, height=4, font=("Arial", 16))
textbox.pack(padx=15)

# myentry = tk.Entry(window)
# myentry.pack()\

button = tk.Button(window, text="Click me", font=("Arial", 18))
button.pack(padx=10, pady=10)


window.mainloop()
