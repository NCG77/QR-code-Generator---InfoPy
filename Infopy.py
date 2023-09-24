from tkinter import *              #For GUI
import pyqrcode                    #For QR code generation
from PIL import ImageTk, Image     #For Image and file creation
import os                          #For Saving of image on desktop
from tkinter import filedialog     #For Opening File manager to store png image

#Defining main function
def main():
    construct()

#Defining Construct: Creates Sturuture of GUI elements
def construct():
    """ Main Screen creation"""

    a= Tk()
    a.title('Infopy')
    a.geometry('400x600')
    a.minsize(400,600)
    a.maxsize(400,600)

    """ Screen Contents"""

    Label(a,text='Content:',font=('Arial',13)).place(x=20,y=20)
    Details=Text(a,height=12,width=44)
    Details.place(x=20,y=50)
    Label(a,text='Preview:',font=('Arial',13)).place(x=20,y=320)
    Button(a,text="Generate QR",command=lambda:Process(Details.get("1.0",END),a),height=2,width=20).place(x=50,y=260)
    Button(a,text="Save Image",command=lambda:Save(),height=2,width=20).place(x=200,y=260)
    a.mainloop()

#Defining Generate QR: Generates a QR Code from the inputed text
def Generate_QR(text):
    """Generating QR Code"""

    qr_code = pyqrcode.create(text)
    qr_code.png('qr.png', scale=6)
    return True

#Defining Process: Gets Data and generates qr code and png image for the same
def Process(TxT,a):
    """Geting text and creating qr png image of text called qr.png"""

    text = TxT
    Generate_QR(text)

    """Printing generated image on the screen"""

    img = Image.open("qr.png")
    img= img.resize((200,200))
    img = ImageTk.PhotoImage(img)
    Label(a,image=img).place(x=100,y=350)
    Label.image = img
    return True

#Saves the image in the specified path
def saving(file_path):
    """Stores the file in the specified location and returns confirmation"""
    try:
        image = Image.open('qr.png')
        image.save(file_path)
        return f"Image saved as {file_path}"
    except Exception as e:
        return f"Error saving image: {e}"

#Defining Save function: functions to Save the generated png 
def Save():
    try:
        """Finds and opens file managers defalt path"""

        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        file_path = filedialog.asksaveasfilename(
            initialdir=desktop_path,
            defaultextension=".png",
            filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        
        if file_path:
            """ Opens png file and stores it into the specified location"""

            result = saving(file_path)
            print(result)
            return True
        else:
            print("Save operation canceled.")
    except Exception as e:
        print(f"Error saving image: {e}")

#Calling main Function
if __name__ == "__main__": 
    main()