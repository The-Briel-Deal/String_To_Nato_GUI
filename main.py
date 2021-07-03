import tkinter
from nato_brain import NatoBrain

natobrain = NatoBrain()


def button_clicked():
    entry_text = entry.get()
    my_text["text"] = natobrain.convert_to_nato(entry_text)


window = tkinter.Tk()
window.title("NATO alphabet converter")

my_label = tkinter.Label()
my_label["text"] = "Put in your text you would like to convert to NATO here"

entry = tkinter.Entry(width=30)


my_text = tkinter.Label(text='Pack', anchor='w', justify="left")
my_text["text"] = ""

button = tkinter.Button(text="Translate", command=button_clicked)

my_label.pack()
entry.pack()
button.pack()
my_text.pack()


tkinter.mainloop()
