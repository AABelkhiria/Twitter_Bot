import sys
import os
from tkinter import Tk, StringVar, GROOVE, Message, Text, LEFT, WORD
from tkinter.ttk import Style, Combobox, Button, Radiobutton, Frame
from time import sleep
from gensen import *

def co():
    try:
        text = "python twit.py " + TCombobox1.get().split()[0]
        os.popen(text)
        Text1.configure(state="normal")
        Text1.insert('1.0', "Connecting as "+TCombobox1.get().split()[0]+"\n" )
        Text1.configure(state="disabled")
    except:
        Text1.configure(state="normal")
        Text1.insert('1.0', "Please select an account to connect\n" )
        Text1.configure(state="disabled")

def dele():
    try:
        TCombobox2.get().split()
        Text1.configure(state="normal")
        Text1.insert('1.0', "Deleting "+TCombobox2.get().split()[0]+"\n" )
        Text1.configure(state="disabled")
        with open('Accounts\Twitter\mail.txt','w') as f :
            for m in mails:
                if m!=TCombobox2.get():
                     f.write(m)
    except:
        Text1.configure(state="normal")
        Text1.insert('1.0', "Please select an account to delete\n" )
        Text1.configure(state="disabled")
    with open('Accounts\Twitter\deleted_mail.txt','a') as f :
        f.write(TCombobox2.get())
    TCombobox2.set("")
    ref(0)

def ref(t):
    with open('Accounts\Twitter\mail.txt','r') as f :
        mails = f.readlines()
    TCombobox1['values'] = mails
    TCombobox2['values'] = mails
    if t:
        Text1.configure(state="normal")
        Text1.insert('1.0', "Refreshing\n" )
        Text1.configure(state="disabled")
        TCombobox1.set("")
        TCombobox2.set("")

def creat():
    browser = init("mobile")
    geturl(browser,'https://mobile.twitter.com/signup?type=email')

    browser.execute_script("window.open('');")
    browser.switch_to_window(browser.window_handles[1])
    geturl(browser,'https://www.minuteinbox.com/')

    mail = browser.find_element_by_id("email").get_attribute("innerHTML")
    Text1.configure(state="normal")
    Text1.insert('1.0', "Mail generated "+mail+"\n" )
    Text1.configure(state="disabled")
    
    browser.switch_to_window(browser.window_handles[0])

    with open('Contents\\Names\\name_sur.txt','r') as f :
        names = f.readlines()
        num = random.randint(1, len(names) )
        name = names[num].split()[0]+" "+names[num].split()[1]
        
    Text1.configure(state="normal")
    Text1.insert('1.0', "Name generated "+name+"\n" )
    Text1.configure(state="disabled")

    champ = browser.find_element_by_id("oauth_signup_client_fullname")
    champ.send_keys(name)
    champ = browser.find_element_by_id("oauth_signup_client_phone_number")
    champ.send_keys(mail)
    browser.find_element_by_name("commit").click()

    while(1):
        sleep(2)
        stop=0
        if 'Add a phone number.' in browser.page_source :
            Text1.configure(state="normal")
            Text1.insert('1.0', "You can not anymore create accounts\n" )
            Text1.configure(state="disabled")
            stop=1
            break

    if stop:
        browser.quit()
        return
    print("haha")
            
        
    
def end():
    try:
        browser.quit()
    except:
        Text1.configure(state="normal")
        Text1.insert('1.0', "Exiting now\n" )
        Text1.configure(state="disabled")
    root.destroy()

root = Tk() 
root.title("Twitter Bot")
root.geometry("990x254+13+25")
root.configure(background="#d9d9d9")
root.configure(highlightbackground="#d9d9d9")
root.configure(highlightcolor="black")
root.resizable(False, False)

combobox1 = StringVar()
combobox2 = StringVar()
with open('Accounts\Twitter\mail.txt','r') as f :
    mails = f.readlines()

_bgcolor = '#d9d9d9'  # X11 color: 'gray85'
_fgcolor = '#000000'  # X11 color: 'black'
_compcolor = '#d9d9d9' # X11 color: 'gray85'
_ana1color = '#d9d9d9' # X11 color: 'gray85' 
_ana2color = '#d9d9d9' # X11 color: 'gray85' 
style = Style()
style.theme_use('clam')
style.configure('.',background=_bgcolor)
style.configure('.',foreground=_fgcolor)
style.configure('.',font="TkDefaultFont")
style.map('.',background=
    [('selected', _compcolor), ('active',_ana2color)])


Connect = Frame(root)
Connect.place(relx=0.01, rely=0.04, relheight=0.53, relwidth=0.34)
Connect.configure(relief=GROOVE)
Connect.configure(borderwidth="2")
Connect.configure(relief=GROOVE)
Connect.configure(width=335)

Message1 = Message(Connect)
Message1.place(relx=0.03, rely=-0.04, relheight=0.17, relwidth=0.18)
Message1.configure(background="#d9d9d9")
Message1.configure(foreground="#000000")
Message1.configure(highlightbackground="#d9d9d9")
Message1.configure(highlightcolor="black")
Message1.configure(text='''Connect''')
Message1.configure(width=60)

TCombobox1 = Combobox(Connect)
TCombobox1.place(relx=0.12, rely=0.3, relheight=0.16, relwidth=0.76)
TCombobox1.configure(textvariable=combobox1)
TCombobox1.configure(takefocus="")
TCombobox1.configure(state="readonly")
TCombobox1['values'] = mails

Button1 = Button(Connect)
Button1.place(relx=0.72, rely=0.59, height=24, width=67)
Button1.configure(padding=(2,0,0,0))
Button1.configure(text='''Connect''')
Button1.configure(command=co)

Connect1 = Frame(root)
Connect1.place(relx=0.37, rely=0.04, relheight=0.53, relwidth=0.34)
Connect1.configure(relief=GROOVE)
Connect1.configure(borderwidth="2")
Connect1.configure(relief=GROOVE)
Connect1.configure(width=335)

Message2 = Message(Connect1)
Message2.place(relx=0.03, rely=-0.04, relheight=0.17, relwidth=0.18)
Message2.configure(background="#d9d9d9")
Message2.configure(foreground="#000000")
Message2.configure(highlightbackground="#d9d9d9")
Message2.configure(highlightcolor="black")
Message2.configure(text='''Delete''')
Message2.configure(width=60)

TCombobox2 = Combobox(Connect1)
TCombobox2.place(relx=0.12, rely=0.3, relheight=0.16, relwidth=0.76)
TCombobox2.configure(textvariable=combobox2)
TCombobox2.configure(state="readonly")
TCombobox2.configure(takefocus="")
TCombobox2['values'] = mails

Button2 = Button(Connect1)
Button2.place(relx=0.72, rely=0.59, height=24, width=67)
Button2.configure(padding=(2,0,0,0))
Button2.configure(text='''Delete''')
Button2.configure(command=dele)

Connect3 = Frame(root)
Connect3.place(relx=0.74, rely=0.04, relheight=0.53, relwidth=0.24)
Connect3.configure(relief=GROOVE)
Connect3.configure(borderwidth="2")
Connect3.configure(relief=GROOVE)
Connect3.configure(width=235)

Message4 = Message(Connect3)
Message4.place(relx=0.04, rely=-0.04, relheight=0.17, relwidth=0.25)
Message4.configure(background="#d9d9d9")
Message4.configure(foreground="#000000")
Message4.configure(highlightbackground="#d9d9d9")
Message4.configure(highlightcolor="black")
Message4.configure(text='''Create''')
Message4.configure(width=60)

Button4 = Button(Connect3)
Button4.place(relx=0.6, rely=0.67, height=24, width=67)
Button4.configure(padding=(2,0,0,0))
Button4.configure(text='''Create''')
Button4.configure(command=creat)

Radiobutton1 = Radiobutton(Connect3)
Radiobutton1.place(relx=0.09, rely=0.22, relheight=0.19, relwidth=0.5)
Radiobutton1.configure(text='''Create 1 account''')
Radiobutton1.configure(value="1")
Radiobutton1.invoke()

Radiobutton2 = Radiobutton(Connect3)
Radiobutton2.place(relx=0.09, rely=0.44, relheight=0.19, relwidth=0.45)
Radiobutton2.configure(text='''Create in Loop''')
Radiobutton2.configure(value="2")

Connect6 = Frame(root)
Connect6.place(relx=0.01, rely=0.63, relheight=0.3, relwidth=0.96)
Connect6.configure(relief=GROOVE)
Connect6.configure(borderwidth="2")
Connect6.configure(relief=GROOVE)
Connect6.configure(width=955)

Message7 = Message(Connect6)
Message7.place(relx=0.01, rely=-0.08, relheight=0.31, relwidth=0.06)
Message7.configure(background="#d9d9d9")
Message7.configure(foreground="#000000")
Message7.configure(highlightbackground="#d9d9d9")
Message7.configure(highlightcolor="black")
Message7.configure(text='''Statut''')
Message7.configure(width=60)

Button7 = Button(Connect6)
Button7.place(relx=0.91, rely=0.27, height=24, width=67)
Button7.configure(padding=(2,0,0,0))
Button7.configure(text='''Refresh''')
Button7.configure(command=lambda: ref(1))

Text1 = Text(Connect6)
Text1.place(relx=0.02, rely=0.27, relheight=0.59, relwidth=0.86)
Text1.configure(background="white")
Text1.configure(font="TkTextFont")
Text1.configure(foreground="black")
Text1.configure(highlightbackground="#d9d9d9")
Text1.configure(highlightcolor="black")
Text1.configure(insertbackground="black")
Text1.configure(selectbackground="#c4c4c4")
Text1.configure(selectforeground="black")
Text1.configure(undo="1")
Text1.configure(width=824)
Text1.configure(wrap=WORD)
Text1.configure(state="disabled")

##menubar = Menu(root,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
##root.configure(menu = menubar)
root.protocol("WM_DELETE_WINDOW", end)
root.mainloop()
