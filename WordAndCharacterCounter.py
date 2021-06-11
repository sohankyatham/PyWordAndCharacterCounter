# Imports
from tkinter import *



# Screen
root = Tk()
root.geometry("600x600")
root.title("Word and Character Counter")



# Declare Word Count and Character Count Function
def DeclareWord_CharCountFunc():
    # Get Content from the TextBox
    TextContent = TextBox.get("1.0", END)
    # Turn The Contents (String) to a Number Value
    CharactersInTextBox = len(TextContent)
    WordsInTextBox = len(TextContent.split())
    # Update the Display Label to Show Number of Characters the Words in TextBox
    DisplayLabel.config(text=str(CharactersInTextBox - 1) + " Characters, " + str(WordsInTextBox) + " Words")



# Intitialize Word and Character Count Function
def InitWord_CharCount():
    DeclareWord_CharCountFunc()
    DisplayLabel.after(1000, InitWord_CharCount)



# Text Box
TextBox = Text(root, width=50, height=20, font=("Arial", 16), wrap="word", undo=True)
TextBox.pack()



# Display Label
DisplayLabel = Label(root, text="", font=("Arial", 16))
DisplayLabel.pack(pady=20)



# Mainloop
InitWord_CharCount()
root.mainloop()
