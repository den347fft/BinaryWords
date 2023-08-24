from tkinter import *
from tkinter import messagebox
import pyperclip
from pyfiglet import Figlet

def string_to_binary(string):
  binary = ""
  for char in string:
    ascii_code = ord(char)
    binary_code = bin(ascii_code)[2:]
    binary_code = binary_code.zfill(8)
    binary += binary_code
  return binary

def binary_to_string(binary):
  string = ""
  chunks = [binary[i:i+8] for i in range(0, len(binary), 8)]
  for chunk in chunks:
    decimal = int(chunk, 2)
    char = chr(decimal)
    string += char
  return string

def shifr():
  if value_m.get() == "shifr":
    bin_ = string_to_binary(text_value.get())
    text["text"] = bin_
  elif value_m.get() == "unshifr":
    word = binary_to_string(text_value.get())
    text["text"] = word
def copy():
    pyperclip.copy(text['text'])
    messagebox.showinfo("INFO", "Text copied to clipboard")
root = Tk()
root["bg"] = "white"
root.title("binarywords by _sineD_0")

value_m = StringVar()
value_m.set("shifr")
text_value = StringVar()

h1 = Label(text=f"{Figlet(font='big').renderText(text='BinaryWords')}").pack()
choose_ = OptionMenu(root,value_m,"shifr","unshifr")
choose_.pack()
input_text = Entry(textvariable=text_value)
input_text.pack()
okbtn = Button(command=shifr,text="Ok").pack()
text = Label(text="")
text.pack()
copy_btn = Button(text="copy",command=copy).pack()

root.mainloop()