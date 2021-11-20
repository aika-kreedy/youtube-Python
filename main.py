from tkinter import *
from pytube import YouTube

root = Tk()
root.geometry('500x300')

root.title(" AIKA youtube video downloader")
root.iconbitmap(r"youtube_logo_2017_svg_S4b_icon.ico")

link = StringVar()

Label(root, text = 'Paste Link Here Below', font = 'arial 15 bold').place(x= 45 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

def Downloader():
    url =YouTube(str(link.get()))
    video = url.streams.first()
    video.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 100)

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'red', padx = 2, command = Downloader).place(x=310 ,y = 150)

root.mainloop()

