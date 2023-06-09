from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('800x500')
root.configure(bg='Black')
root.title('Youtube downloader')
root.resizable(0, 0)

label = Label(root, text="YouTube Video Downloader",font="Helvatica 24",fg='white', relief=RIDGE,bg='black',borderwidth=0)
root.wm_attributes("-transparentcolor", 'grey')
label.pack()

Label(text="Paste Link Here",fg='white',font="Helvatica 15",borderwidth=0,bg='black').place(x=350,y=50)

link = StringVar()
link_enter = Entry(root, width = 70,textvariable = link)
link_enter.place(x = 200, y = 90)

def Download():
    url = YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text='DOWNLOADED', font='arial 10', bg='black', fg='white').place(x=375, y=250)

Button(root,text="DOWNLOAD",font="Helvatica 10",command=Download).place(x=380,y=150)


root.mainloop()
