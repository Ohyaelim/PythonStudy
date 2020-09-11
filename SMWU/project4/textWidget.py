# 작성일 : 2018. 6. 7


from tkinter import*
from tkinter import messagebox
from tkinter.simpledialog import*
from tkinter.filedialog import askopenfilename

def func_exit() :
    window.quit()
    window.destroy()

def Func1() :

    global filename

    filename = askopenfilename(filetypes =(("Text File", "*.txt"),("All Files","*.*")))
    t = open(filename, 'r', encoding = 'UTF8')
    txt = t.read()
    
    text.config(state=NORMAL)
    text.delete(1.0,END)
    text.insert(END,txt)
    text.config(state=DISABLED)
   
    
def Func2():
    value = askstring('key입력','찾을 문자열 입력')
    files = open(filename, 'r', encoding = 'UTF8')
    txt = files.read()
    a = txt.count(value)


    messagebox.showinfo('문자열 찾기','파일에서 %s를 총%d회 찾음'%(value,a))

window = Tk()
window.title('과제#4')
window.geometry('800x500')

text = Text(window)

text.pack(padx = 10 , pady = 10, expand = 1, fill = BOTH)

mainMenu = Menu(window)
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
mainMenu.add_cascade(label='파일처리',menu=fileMenu)
subMenu=Menu(fileMenu)
fileMenu.add_cascade(label='텍스트파일',menu=subMenu)
fileMenu.add_separator()
fileMenu.add_command(label='종료',command=func_exit)

subMenu.add_command(label='열  기',command=Func1)
subMenu.add_command(label='찾  기',command=Func2)
