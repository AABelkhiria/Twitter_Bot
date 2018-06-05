import sys
import os
from tkinter import Tk, StringVar, GROOVE, Message, Text, LEFT, WORD, END, INSERT
from tkinter.ttk import Style, Combobox, Button, Radiobutton, Frame, Checkbutton, Label, Scale, Entry
from time import sleep
from gensen import *

def struc1(s):
    slider1.set('%d' % float(s))
    val1.place(relx=0.1+(int(slider1.get())*0.00048), rely=0.52)

def struc2(s):
    slider2.set('%d' % float(s))
    val2.place(relx=0.1+(int(slider2.get())*0.007), rely=0.665)

def up():
    try:
        combobox1.get().split()[0]
        if (int(check1.get()) or int(check2.get())):
            geturl(browser,"https://mobile.twitter.com/settings/profile")
            while(1):
                pas = 0
                try:
                    browser.find_element_by_css_selector('input[type="file"]')
                    pas = 1
                except:
                    sleep(2)
                if pas == 1:
                    break
            sleep(1)
            if int(check1.get()):
                browser.find_elements_by_css_selector('input[type="file"]')[1].clear()
                browser.find_elements_by_css_selector('input[type="file"]')[1].send_keys(os.path.dirname(os.path.abspath(__file__))+"\Contents\Photos\\"+combobox1.get())
                sleep(1)
            if int(check2.get()):
                browser.find_elements_by_css_selector('input[type="file"]')[0].clear()
                browser.find_elements_by_css_selector('input[type="file"]')[0].send_keys(os.path.dirname(os.path.abspath(__file__))+"\Contents\Photos\\"+combobox1.get())
                sleep(1)
            sleep(2)
            clickelem(browser,"/html/body/div/div/main/div/div[7]/div[2]/div","no verif")
            waitelem(browser,"/html/body/div/div[1]/main/div/div/div/div/div/div/div[1]/div[2]/div[1]/a/div/div")
    except:
        pass

def fo(has):
    url = 'https://twitter.com/hashtag/'+has+'?f=users'
    geturl(browser,url)
    sleep(2)
    for i in range(1,int(slider1.get())+1):
        try:
            browser.find_elements_by_css_selector('div > span:nth-child(2) > button:nth-child(1)')[i].click()
        except:
            pass
        sleep(int(slider2.get()))
        

def follow():
    try:
        if int(radio.get()) == 1:
            combobox2.get().split()[0]
            fo(combobox2.get().split()[0])
        else :
            with open('Contents\Hashtags\hashtags.txt','r') as f :
                hashes = f.readlines()
            for hashe in hashes:
                fo(hashe.split()[0])
    except:
        pass

def test():
    print(os.path.dirname(os.path.abspath(__file__)))

def end():
    try:
        browser.quit()
    except:
        pass
    root.destroy()
    
root = Tk()
root.title("Connecting as "+sys.argv[1])
root.geometry("623x423+56+82")
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")
root.resizable(False, False)

combobox1 = StringVar()
combobox2 = StringVar()
combobox3 = StringVar()
combobox4 = StringVar()
slider1 = StringVar()
slider2 = StringVar()
check1 = StringVar()
check2 = StringVar()
radio= StringVar()

slider1.set('1')
slider2.set('1')
check1.set('0')
check2.set('0')

photos = []
for (dirpath, dirnames, filenames) in os.walk("Contents\Photos"):
    photos.extend(filenames)
    break

with open('Contents\Hashtags\hashtags.txt','r') as f :
    hashtags = f.readlines()

## GUI Tkinter

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#d9d9d9' # X11 color: 'gray85' 
styl = Style()
styl.theme_use('clam')
styl.configure('.',background=_bgcolor)
styl.configure('.',foreground=_fgcolor)
styl.configure('.',sliderthickness='20')
styl.configure('.',font="TkDefaultFont")
styl.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])

Frame1 = Frame(root)
Frame1.place(relx=0.02, rely=0.02, relheight=0.27, relwidth=0.46)
Frame1.configure(relief=GROOVE)
Frame1.configure(borderwidth="2")
Frame1.configure(relief=GROOVE)
Frame1.configure(width=285)

Checkbutton1 = Checkbutton(Frame1)
Checkbutton1.place(relx=0.07, rely=0.43, relheight=0.22, relwidth=0.34)
Checkbutton1.configure(text='''Profile photo''')
Checkbutton1.configure(variable=check1)

Checkbutton3 = Checkbutton(Frame1)
Checkbutton3.place(relx=0.07, rely=0.7, relheight=0.22, relwidth=0.35)
Checkbutton3.configure(text='''Header photo''')
Checkbutton3.configure(variable=check2)

Label1 = Label(Frame1)
Label1.place(relx=0.04, rely=-0.04)
Label1.configure(text='''Upload''')

Button1 = Button(Frame1)
Button1.place(relx=0.74, rely=0.7, height=25, width=60)
Button1.configure(padding=(2,0,0,0))
Button1.configure(text='''Upload''')
Button1.configure(command=up)

TCombobox1 = Combobox(Frame1)
TCombobox1.place(relx=0.09, rely=0.22, relheight=0.18, relwidth=0.61)
TCombobox1.configure(textvariable=combobox1)
TCombobox1.configure(width=173)
TCombobox1.configure(takefocus="")
TCombobox1.configure(state="readonly")
TCombobox1['values'] = photos


Frame3 = Frame(root)
Frame3.place(relx=0.02, rely=0.33, relheight=0.63, relwidth=0.46)
Frame3.configure(relief=GROOVE)
Frame3.configure(borderwidth="2")
Frame3.configure(relief=GROOVE)
Frame3.configure(width=285)

Label4 = Label(Frame3)
Label4.place(relx=0.04, rely=-0.04, height=21, width=44)
Label4.configure(text='''Follow''')

Radiobutton1 = Radiobutton(Frame3)
Radiobutton1.place(relx=0.07, rely=0.08, relheight=0.09, relwidth=0.38)
Radiobutton1.configure(text='''Single Hashtag''')
Radiobutton1.configure(variable=radio)
Radiobutton1.configure(value="1")
Radiobutton1.invoke()

TCombobox3 = Combobox(Frame3)
TCombobox3.place(relx=0.11, rely=0.19, relheight=0.08, relwidth=0.6)
TCombobox3.configure(textvariable=combobox2)
TCombobox3.configure(width=173)
TCombobox3.configure(takefocus="")
TCombobox3['values'] = hashtags

Radiobutton2 = Radiobutton(Frame3)
Radiobutton2.place(relx=0.07, rely=0.3, relheight=0.09, relwidth=0.44)
Radiobutton2.configure(text='''Multiple Hashtags''')
Radiobutton2.configure(value="2")
Radiobutton2.configure(variable=radio)

Entry1 = Entry(Frame3)
Entry1.place(relx=0.11, rely=0.42, relheight=0.08, relwidth=0.51)
Entry1.configure(width=144)

Button2 = Button(Frame3)
Button2.place(relx=0.63, rely=0.42, height=20, width=20)
Button2.configure(padding=(2,0,0,0))
Button2.configure(text='''+''')

Button3 = Button(Frame3)
Button3.place(relx=0.74, rely=0.87, height=25, width=60)
Button3.configure(padding=(2,0,0,0))
Button3.configure(text='''Follow''')
Button3.configure(command=follow)
Button3.configure(width=56)

Scale1 = Scale(Frame3, command=lambda s:struc1(s))
Scale1.place(relx=0.07, rely=0.59)
Scale1.configure(length="172")
Scale1.configure(orient="horizontal")
Scale1.configure(from_=1)
Scale1.configure(to_=1000)

val1 = Label(Frame3, textvariable=slider1)
val1.place(relx=0.105, rely=0.52)

Scale2 = Scale(Frame3, command=lambda s:struc2(s))
Scale2.place(relx=0.07, rely=0.735)
Scale2.configure(length="150")
Scale2.configure(orient="horizontal")
Scale2.configure(from_=1)
Scale2.configure(to_=60)

val2 = Label(Frame3, textvariable=slider2)
val2.place(relx=0.105, rely=0.665)

Label5 = Label(Frame3)
Label5.place(relx=0.7, rely=0.58, height=21, width=64)
Label5.configure(text='''to follow''')
Label5.configure(width=64)

Label6 = Label(Frame3)
Label6.place(relx=0.63, rely=0.72, height=21, width=94)
Label6.configure(text='''latency of follow''')
Label6.configure(width=94)

Frame2 = Frame(root)
Frame2.place(relx=0.5, rely=0.02, relheight=0.27, relwidth=0.47)
Frame2.configure(relief=GROOVE)
Frame2.configure(borderwidth="2")
Frame2.configure(relief=GROOVE)
Frame2.configure(width=295)

Label2 = Label(Frame2)
Label2.place(relx=0.03, rely=-0.04, height=21, width=44)
Label2.configure(text='''Like''')

Scale3 = Scale(Frame2)
Scale3.place(relx=0.03, rely=0.19)
Scale3.configure(length="220")
Scale3.configure(orient="horizontal")

Label7 = Label(Frame2)
Label7.place(relx=0.68, rely=0.37, height=21, width=64)
Label7.configure(text='''to like''')

Button4 = Button(Frame2)
Button4.place(relx=0.73, rely=0.71, height=25, width=60)
Button4.configure(padding=(2,0,0,0))
Button4.configure(text='''Like''')

Frame4 = Frame(root)
Frame4.place(relx=0.5, rely=0.33, relheight=0.48, relwidth=0.47)
Frame4.configure(relief=GROOVE)
Frame4.configure(borderwidth="2")
Frame4.configure(relief=GROOVE)
Frame4.configure(width=295)

Label3 = Label(Frame4)
Label3.place(relx=0.03, rely=-0.04, height=21, width=44)
Label3.configure(text='''Tweet''')

TCombobox2 = Combobox(Frame4)
TCombobox2.place(relx=0.07, rely=0.32, relheight=0.1, relwidth=0.76)
TCombobox2.configure(textvariable=combobox3)
TCombobox2.configure(width=223)
TCombobox2.configure(takefocus="")
TCombobox2.configure(state="readonly")

Label8 = Label(Frame4)
Label8.place(relx=0.07, rely=0.2, height=21, width=80)
Label8.configure(text='''Text to tweet''')

Label9 = Label(Frame4)
Label9.place(relx=0.07, rely=0.5, height=21, width=90)
Label9.configure(text='''Image to tweet''')

TCombobox4 = Combobox(Frame4)
TCombobox4.place(relx=0.07, rely=0.62, relheight=0.1, relwidth=0.76)
TCombobox4.configure(textvariable=combobox4)
TCombobox4.configure(takefocus="")

Button7 = Button(Frame4)
Button7.place(relx=0.73, rely=0.83, height=25, width=60)
Button7.configure(padding=(2,0,0,0))
Button7.configure(text='''Tweet''')

Button5 = Button(root)
Button5.place(relx=0.75, rely=0.9, height=25, width=120)
Button5.configure(padding=(2,0,0,0))
Button5.configure(text='''Quit''')
Button5.configure(width=120)

Button6 = Button(root)
Button6.place(relx=0.52, rely=0.9, height=25, width=120)
Button6.configure(padding=(2,0,0,0))
Button6.configure(text='''Refresh''')
Button6.configure(width=120)

Button8 = Button(root)
Button8.place(relx=0.63, rely=0.83, height=24, width=137)
Button8.configure(padding=(2,0,0,0))
Button8.configure(text='''Open folder''')
Button8.configure(width=137)
Button8.configure(command=test)

root.update()
browser = connect(str(sys.argv[1]) , "pc")
root.title("Connected as "+sys.argv[1])

root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()

