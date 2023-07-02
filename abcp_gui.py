import tkinter as tk
import tkinter.font as tkFont
from PIL import ImageTk, Image


# Army body fat; one touch tape test
def body_fat_men(waist, weight):
    return -26.97 - (0.12 * weight) + (1.99 * waist)


def body_fat_female(waist, weight):
    return -9.15 - (0.015 * weight) + (1.27 * waist)


class App:
    def __init__(self, root):
        # setting title
        root.title("U.S. Army One-Touch Tape Test Calculator")

        # setting window size
        width = 600
        height = 250
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        # army logo
        image = Image.open("abc_exec/logo.png")  # Replace "army_logo.png" with the actual image path
        image = image.resize((120, 101))  # Adjust the image size as needed
        self.photo = ImageTk.PhotoImage(image)

        GLabel_914 = tk.Label(root, image=self.photo, compound="center")
        GLabel_914.place(x=10, y=10, width=120, height=101)

        # male radio button
        self.gender = tk.StringVar()
        GRadio_682 = tk.Radiobutton(root, variable=self.gender, value="male")
        ft = tkFont.Font(family='Arial', size=10)
        GRadio_682["font"] = ft
        GRadio_682["fg"] = "#fad400"
        GRadio_682["justify"] = "center"
        GRadio_682["text"] = " Male"
        GRadio_682.place(x=220, y=60, width=85, height=25)
        GRadio_682["command"] = self.GRadio_682_command

        # female radio button
        GRadio_467 = tk.Radiobutton(root, variable=self.gender, value="female")
        ft = tkFont.Font(family='Arial', size=10)
        GRadio_467["font"] = ft
        GRadio_467["fg"] = "#fad400"
        GRadio_467["justify"] = "center"
        GRadio_467["text"] = "Female"
        GRadio_467.place(x=310, y=60, width=85, height=25)
        GRadio_467["command"] = self.GRadio_467_command

        # inches entry box
        self.waist_entry = tk.Entry(root)
        self.waist_entry["bg"] = "#ffffff"
        self.waist_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=10)
        self.waist_entry["font"] = ft
        self.waist_entry["fg"] = "#000000"
        self.waist_entry["justify"] = "center"
        self.waist_entry.place(x=310, y=90, width=160, height=30)

        # waist size label
        GLabel_576 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_576["font"] = ft
        GLabel_576["fg"] = "#fad400"
        GLabel_576["justify"] = "center"
        GLabel_576["text"] = "Enter waist size (inches):"
        GLabel_576.place(x=140, y=90, width=176, height=30)

        # weight pounds label
        GLabel_433 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_433["font"] = ft
        GLabel_433["fg"] = "#fad400"
        GLabel_433["justify"] = "center"
        GLabel_433["text"] = "Enter weight (lbs):"
        GLabel_433.place(x=160, y=130, width=135, height=30)

        # pounds entry box
        self.weight_entry = tk.Entry(root)
        self.weight_entry["bg"] = "#ffffff"
        self.weight_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=10)
        self.weight_entry["font"] = ft
        self.weight_entry["fg"] = "#000000"
        self.weight_entry["justify"] = "center"
        self.weight_entry.place(x=310, y=130, width=160, height=30)

        # output percentage
        self.bodyfat_output = tk.Entry(root)
        self.bodyfat_output["bg"] = "#ffffff"
        self.bodyfat_output["borderwidth"] = "1px"
        ft = tkFont.Font(family='Arial', size=10)
        self.bodyfat_output["font"] = ft
        self.bodyfat_output["fg"] = "#333333"
        self.bodyfat_output["justify"] = "center"
        self.bodyfat_output.place(x=310, y=210, width=160, height=30)

        # body fat label
        GLabel_121 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_121["font"] = ft
        GLabel_121["fg"] = "#fad400"
        GLabel_121["justify"] = "center"
        GLabel_121["text"] = "Body-Fat Percentage: "
        GLabel_121.place(x=130, y=210, width=199, height=34)

        # calculate button
        GButton_252 = tk.Button(root)
        GButton_252["bg"] = "#525252"
        ft = tkFont.Font(family='Arial', size=10)
        GButton_252["font"] = ft
        GButton_252["fg"] = "#000000"
        GButton_252["justify"] = "center"
        GButton_252["text"] = "CALCULATE"
        GButton_252["relief"] = "raised"
        GButton_252.place(x=260, y=170, width=91, height=30)
        GButton_252["command"] = self.GButton_252_command

        # m/f label
        GLabel_850 = tk.Label(root)
        ft = tkFont.Font(family='Arial', size=10)
        GLabel_850["font"] = ft
        GLabel_850["fg"] = "#fad400"
        GLabel_850["justify"] = "center"
        GLabel_850["text"] = "Select Male or Female"
        GLabel_850.place(x=180, y=20, width=256, height=30)

    def GRadio_682_command(self):
        self.gender = "male"

    def GRadio_467_command(self):
        self.gender = "female"

    def GButton_252_command(self):
        waist = int(self.waist_entry.get())
        weight = int(self.weight_entry.get())

        if self.gender == "male":
            bodyfat = body_fat_men(waist, weight)
        elif self.gender == "female":
            bodyfat = body_fat_female(waist, weight)
        else:
            bodyfat = None

        if bodyfat is not None:
            self.bodyfat_output.delete(0, tk.END)
            self.bodyfat_output.insert(0, f"{bodyfat:.2f}%")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
