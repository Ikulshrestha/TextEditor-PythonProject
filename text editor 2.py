from tkinter import *
from tkinter import Tk,Menu, filedialog,messagebox
import tkinter.scrolledtext as ScrolledText
import tkinter.colorchooser
#main window
 root = Tk(className=' MyEditor')
textarea = ScrolledText.ScrolledText(root, width=800, height=500)
textarea.pack()
root.iconbitmap('icons/pypad_BNi_icon.ico')
 #FUNCTIONS
 ###################################
 #NEW
def new():
    if len(textarea.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno('SAVE', 'Do you want to save the file?'):
            save()
        else:
            textarea.delete('1.0', END)
     #OPEN
def open():
    file = filedialog.askopenfile(parent=root, title='Select a text file',filetype=(('Text file','*.txt'), ('All files','*.*')))
    root.title(os.path.basename(file.name) + ' -  MyEditor')
     if file != None:
        contents=file.read()
        textarea.insert('1.0',contents)
        file.close()
#SAVE
def save():
    file = filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if file != None :
        data=textarea.get('1.0',END+'-1c')
        file.write(data)
        file.close()
#EXIT
def exit():
    if messagebox.askyesno('QUIT','Are you sure you want to quit?'):
        root.destroy()
 ##################################
 #UNDO
def undo():
    text.event_generate("<<Undo>>")
    return
#REDO
def redo():
    text.event_generate("<<Redo>>")
    return
#CUT
def cut():
    text.event_generate("<<Cut>>")
    return
#COPY
def copy():
    text.event_generate("<<Copy>>")
    return
#PASTE
def paste():
    text.event_generate("<<Paste>>")
    return
 ####################################
 #about
def about():
    label=messagebox.showinfo("About", "An Editor using Tkinter by Ishan Kulshrestha")
#help
def help():
    label=messagebox.showinfo("Help", "For help drop an email at kulshresthaishan.com")
 ####################################
 #def theme():
    #Thinking.......
 #defining icons
newicon = PhotoImage(file='icons/new_file.gif')
openicon = PhotoImage(file='icons/open_file.gif')
saveicon = PhotoImage(file='icons/Save.gif')
cuticon = PhotoImage(file='icons/Cut.gif')
copyicon = PhotoImage(file='icons/Copy.gif')
pasteicon = PhotoImage(file='icons/Paste.gif')
undoicon = PhotoImage(file='icons/Undo.gif')
redoicon = PhotoImage(file='icons/Redo.gif')
 #MENUBAR
 #meneu
my_menu=Menu(root)
root.config(menu=my_menu)
 #file Menu
filemenu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New',command=new)
filemenu.add_command(label='Open',command=open)
filemenu.add_command(label='Save',command=save)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=exit)
 #Edit menu
editmenu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Edit',menu=editmenu)
editmenu.add_command(label='Undo', accelerator='Ctrl+Z', command=undo, image=undoicon)
editmenu.add_command(label='Redo', accelerator='Ctrl+Y',command=redo, image=redoicon)
editmenu.add_separator()
editmenu.add_command(label='Cut', accelerator='Ctrl+X', command=cut, image=cuticon)
editmenu.add_command(label='Copy', accelerator='Ctrl+C', command=copy, image=copyicon)
editmenu.add_command(label='Paste', accelerator='Ctrl+V', command=paste, image=pasteicon)
 #config menu
configmenu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Config', menu=configmenu)
fontmenu = Menu(configmenu,tearoff=0)#, command=Font)
configmenu.add_cascade(label='Font',menu=fontmenu)
fontsubmenu = Menu(fontmenu, tearoff=0)
fontmenu.add_cascade(label='Font Style',menu=fontsubmenu)
for item in ('Roman', 'Bold', 'Italic'):
    fontsubmenu.add_radiobutton(label=item, variable='font')
fontsize = Menu(fontmenu, tearoff=0)
fontmenu.add_cascade(label='Font Size', menu=fontsize)
for size in range(8 , 26 , 2):
    fontsize.add_radiobutton(label='{} px'.format(size), variable='font_size')
themesmenu = Menu(configmenu, tearoff=0)
configmenu.add_cascade(label='Themes',menu=themesmenu)
clrschms = {
'1. Default White': '000000.FFFFFF',
'2. Greygarious Grey':'83406A.D1D4D1',
'3. Lovely Lavender':'202B4B.E1E1FF',
'4. Aquamarine': '5B8340.D1E7E0',
'5. Bold Beige': '4B4620.FFF0E1',
'6. Cobalt Blue':'ffffBB.3333aa',
'7. Olive Green': 'D1E7E0.5B8340',
}
themechoice= StringVar()
themechoice.set('1. Default White')
for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice)#, command=theme)
 #Help menu
helpmenu=Menu(root, tearoff=0)
my_menu.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='Help',command=help)#, command=helpbox)
helpmenu.add_command(label='About',command=about)#, command=aboutbox)
 #shortcut bar and line number
#shortcutbar = Frame(root, height=25)
#icons = ['new_file', 'open_file', 'save', 'cut', 'copy', 'paste', 'undo', 'redo']
#for i, icon in enumerate(icons):
#    tbicon = PhotoImage(file='icons/'+icon+'.gif')
#    cmd = eval(icon)
#    toolbar.pack(side=LEFT)
#shortcutbar.pack(expand=NO, fill=X)
 root.mainloop()
