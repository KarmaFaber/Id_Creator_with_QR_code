#python libraries
from tkinter import *
import datetime
from tkinter import messagebox

from PIL import Image, ImageDraw, ImageFont
image = Image.new('RGB', (1000,900), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)
import random
import qrcode

#root---
root=Tk()
root.title("ID card generator with QR Code")
root.geometry("700x500")
root.config(bg="#EFD2BC")

#my variables:---
name=StringVar()
lastname=StringVar()
passport=StringVar()

d_date=datetime.datetime.now()
reg_format_date = d_date.strftime(" date: %d-%m-%Y \t time: %I:%M:%S %p")


#my Labels:---
dateLabel=Label(root, text=reg_format_date, bg="#EFD2BC")
dateLabel.config(font=("Courier", 12))
dateLabel.grid(row=0, column=0, padx=10, pady=10)

nameLabel=Label(root, text="your name: ", bg="#EFD2BC")
nameLabel.config(font=("Courier", 12))
nameLabel.grid(row=1, column=0, padx=10, pady=10)

lastnameLabel=Label(root, text="lastname: ", bg="#EFD2BC")
lastnameLabel.config(font=("Courier", 12))
lastnameLabel.grid(row=2, column=0, padx=10, pady=10)

passportLabel=Label(root, text="passport: ", bg="#EFD2BC")
passportLabel.config(font=("Courier", 12))
passportLabel.grid(row=3, column=0, padx=10, pady=10)

companyLabel=Label(root, text="company: ", bg="#EFD2BC")
companyLabel.config(font=("Courier", 12))
companyLabel.grid(row=4, column=0, padx=10, pady=10)

textLabel=Label(root, text="All Fields are Mandatory \nAvoid any kind of Spelling Mistakes\n Write Everything in uppercase letters", bg="#EFD2BC")
textLabel.config(font=("Courier", 10))
textLabel.grid(row=8, column=0, padx=10, pady=10)

#my entry boxes:---
nameBox=Entry(root, bg="#EFD2BC", fg="#2c2627")
nameBox.config(font=("Courier", 12))
nameBox.grid(row=1, column=1, padx=10, pady=10)
nameBox.focus()

lastnameBox=Entry(root, bg="#EFD2BC", fg="#2c2627")
lastnameBox.config(font=("Courier", 12))
lastnameBox.grid(row=2, column=1, padx=10, pady=10)
lastnameBox.focus()

passportBox=Entry(root, bg="#EFD2BC", fg="#2c2627")
passportBox.config(font=("Courier", 12))
passportBox.grid(row=3, column=1, padx=10, pady=10)
passportBox.focus()

companyBox=Entry(root, bg="#EFD2BC", fg="#2c2627")
companyBox.config(font=("Courier", 12))
companyBox.grid(row=4, column=1, padx=10, pady=10)
companyBox.focus()
#----def
def create_qr():
    (x,y)=(50,50)
    message=nameBox.get()
    name=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=80)
    draw.text((x, y), message, fill=color, font=font)

    (x,y)=(600,75)
    idno=random.randint(10000000,90000000)
    message = str('ID '+str(idno))
    color = 'rgb(0, 0, 0)' # black color
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x,y)=(50, 250)
    message=lastnameBox.get()
    lastname=message
    color = 'rgb(0, 0, 0)' # black color 
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x,y)=(50, 350)
    message=passportBox.get()
    passport=message
    color = 'rgb(0, 0, 0)' # black color 
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)

    (x, y) = (50, 450)
    message = companyBox.get()
    company=message
    color = 'rgb(0, 0, 0)'
    font = ImageFont.truetype('arial.ttf', size=60)
    draw.text((x, y), message, fill=color, font=font)
    
    # save the edited image
    image.save(str(name)+'.png')

    img = qrcode.make(str(company)+str(idno))   # this info. is added in QR code, also add other things
    img.save(str(idno)+'.bmp')

    til = Image.open(name+'.png')
    im = Image.open(str(idno)+'.bmp') #25x25
    til.paste(im,(600,350))
    til.save(name+'.png')

    messagebox.showinfo(message="Your ID Card Successfully created in a PNG file "+name+".png", title=None)


    #clear EntryBoxes:---
    nameBox.delete(0,END)
    lastnameBox.delete(0,END)
    passportBox.delete(0,END)
    companyBox.delete(0,END)


#btn---------------
btn=Button(root, text="Create QR", command=create_qr, bg="#bc2c3d", fg="#2c2627")
btn.grid(row=5, column=0, padx=20, pady=20)
btn.config(font=("Courier", 12))

#close root----
root.mainloop()