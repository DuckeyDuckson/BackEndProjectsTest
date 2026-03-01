
import tkinter as tk

# 1. Create the main window
root = tk.Tk()
root.title("My Python Window")
root.geometry("400x300")  # Set width and height

# 2. Add a label (text)
Number = 0
label = tk.Label(root, text="When You press the button it should add 1 to", font=("Arial", 14))
label.pack(pady=20)  # 'pack' puts it in the window with some padding
label2 = tk.Label(root, text=str(Number), font=("Arial", 14))
label2.pack(pady=30)
# 3. Add a close button
def AddOne():
    global Number #this gets the number variable(global is a getter)
    Number += 1
    label2.config(text=f"{Number}")
def AddSetAmount(amount):
    global Number
    Number += amount
    label2.config(text=f"{Number}")

def only_numbers(char):
    # Returns True if the character is a digit, False otherwise
    return char.isdigit() or char == ""

# 2. Register the function with Tkinter
validation = root.register(only_numbers)

button_text = tk.StringVar()
TargetNumber = 5
button_text.set(f"Add {TargetNumber}")
button = tk.Button(root, text="Add", command=AddOne)
button.pack()
button2 = tk.Button(root, textvariable=button_text , command=lambda: AddSetAmount(TargetNumber)) #runs only when button is pressed cuz lambda, also f means formatted string
button2.pack()

def AddFromInput(amount):
    global TargetNumber
    TargetNumber = amount
    button_text.set(f"Add {TargetNumber}")
input_box = tk.Entry(root, 
                     validate="key", 
                     validatecommand=(validation, '%S')) 
input_box.pack(pady=10)
input_box.bind("<Return>", lambda event: AddFromInput(int(input_box.get())))

def make_draggable(widget):
    """Makes a Tkinter widget draggable."""
    widget.bind("<Button-1>", lambda e: (setattr(e.widget, '_drag_start_x', e.x), 
                                         setattr(e.widget, '_drag_start_y', e.y)))
    widget.bind("<B1-Motion>", lambda e: e.widget.place(
        x=e.widget.winfo_x() - e.widget._drag_start_x + e.x,
        y=e.widget.winfo_y() - e.widget._drag_start_y + e.y))

# Example Usage
frame = tk.Frame(root, bg="grey", width=50, height=50)
frame.place(x=10, y=10)
make_draggable(frame)

# 4. Start the application
root.mainloop()
