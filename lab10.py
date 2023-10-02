
from tkinter import *
from random import choice

root = Tk()
root.attributes("-topmost", True)
root.title("Крестики нолики")
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
wh = (w//2)-200
hh = (h//2)-200
root.geometry(f"350x230+{wh}+{hh}")
canvas = Canvas(root,bg="#00868B", width=400, height=300)
canvas.pack(anchor=CENTER, expand=1)
por = [0,1,2,3,4,5,6,7,8,9]
win = [[1,2,3],
       [3,6,9],
       [7,8,9],
       [1,4,7],
       [1,5,9],
       [3,5,7],
       [2,5,8],
       [4,5,6]]
yup = [1,2,3,4,5,6,7,8,9]
x = []
o = []
clet =''
l=0;comb = 0; col = 0
n = 10;w = 75;g = 20;h = 85
pav = []
clet1 = 0;clet2 = 0;clet3 = 0;clet4 = 0;
clet5 = 0;clet6 = 0;clet7 = 0;clet8 = 0;clet9 = 0
check = 0;suma = 0;l = 0;
u = 0
ft  = 0
def close(ud):
    exit()
def bot(yue):
    global u
    u += 1
    checki = []
    pro = []
    ft = 0
    if len(x) >= 2:
        for i in range(len(win)):
            if (win[i].count('x') == 2 and win[i].count('o') != 1) or (win[i].count('o') == 2 and win[i].count('x') != 1):
                pro = win[i]
        for j in pro:
            if j != 'x' and j != 'o':
                por[j] = 'o'
                yue = eval(f'clet{j}')
                x1, y1, x2, y2 = canvas.coords(yue)
                canvas.create_text(x1 + 32, y1 + 34, text="O", font="System 50", fill="#282828")
                o.append(yue)
                ft += 1
                print('1')
                pro = []
                break
            elif j != 'x' and j != 'o':
                por[j] = 'o'
                yue = eval(f'clet{j}')
                x1, y1, x2, y2 = canvas.coords(yue)
                canvas.create_text(x1 + 32, y1 + 34, text="O", font="System 50", fill="#282828")
                o.append(yue)
                ft += 1
                print('1')
                break
        if len(pro) == 0 and ft == 0:
            for b in por:
                if b in yup:
                    checki.append(b)
            print('2')
            print(checki)
            p = choice(checki)
            print(p)
            yue = eval(f'clet{p}')
            x1, y1, x2, y2 = canvas.coords(yue)
            canvas.create_text(x1 + 33, y1 + 33, text="O", font="System 50", fill="#282828")
            o.append(yue)
            por[p] = 'o'
    elif len(x) <= 1:
        if x[0] == 5:
            p = choice([m for m in range(1, 9) if m not in [yue]])
            yue = eval(f'clet{p}')
            x1, y1, x2, y2 = canvas.coords(yue)
            canvas.create_text(x1 + 33, y1 + 33, text="O", font="System 50", fill="#282828")
            o.append(yue)
            por[yue] = 'o'
        elif x[0] != 5:
            yue = eval(f'clet{5}')
            x1, y1, x2, y2 = canvas.coords(yue)
            canvas.create_text(x1 + 33, y1 + 33, text="O", font="System 50", fill="#282828")
            o.append(yue)
            por[yue] = 'o'
    for k in range(len(win)):
        for h in range(0, 3):
            if win[k][h] in o:
                win[k][h] = 'o'
    prov()
def prov():
    check_win = 0
    for oi in range(len(win)):
        if win[oi].count('x') == 3:
            check_win = 1
        elif win[oi].count('o') == 3:
            check_win =2
        elif por.count('x') == 5 and por.count('o') == 4 and (check_win != 1 or check_win !=2):
            check_win = 3
    if check_win == 1 or check_win == 2 or check_win == 3:
        ud = Toplevel()
        ud.attributes("-topmost", True)
        ud.resizable(False, False)
        ud.geometry(f'300x100+{wh}+{hh}')
        canvas = Canvas(ud, bg="white", width=300, height=100)
        canvas.pack(anchor=CENTER, expand=1)
        canvas.create_rectangle(5, 5, 295, 95, fill="#80CBC4", outline="#004D40", width=5)
        if check_win == 1:
            canvas.create_text(150, 40, text="WIN X", font="System 25", fill="#282828")
        elif check_win == 2:
            canvas.create_text(150, 40, text="WIN O", font="System 25", fill="#282828")
        elif check_win == 3:
            canvas.create_text(150, 40, text="НИЧЬЯ", font="System 25", fill="#282828")
        id = canvas.create_rectangle(115,65,185,85,fill="#80CBC4", outline="#004D40", width=3)
        ii = canvas.create_text(150, 75, text="Close", font="System 10", fill="#282828")
        canvas.tag_bind(id, "<Button>", lambda x: close(ud))
        canvas.tag_bind(ii, "<Button>", lambda x: close(ud))
        ud.grab_set()
def sos(hh,boti):
    global u
    global col;global x1,y1,x2,y2; x1,y1,x2,y2 = canvas.coords(hh)
    if u % 2 == 0:
        u +=1
        canvas.create_text(x1+33,y1+33,text="X",font="System 50", fill="#282828")
        for i in range(0,9):
            if hh == eval('clet{}'.format(i+1)):
                x.append(i+1)
                col +=1
                por[i+1] = 'x'
        for k in range(len(win)):
            for h in range(0,3):
                if win[k][h] in x:
                    win[k][h] = 'x'
    elif u % 2 != 0 and boti == 0:
        u += 1
        canvas.create_text(x1 + 33, y1 + 33, text="O", font="System 50", fill="#282828")
        for i in range(0, 9):
            if hh == eval('clet{}'.format(i + 1)):
                o.append(i + 1)
                col += 1
                por[i + 1] = 'o'
        for k in range(len(win)):
            for h in range(0, 3):
                if win[k][h] in o:
                    win[k][h] = 'o'
    prov()
for j in range(1,4):
    for i in range(1,4):
        l+=1
        exec(f'clet{l} = {canvas.create_rectangle(n, g, w, h, fill="#80CBC4", outline="#004D40",width= 5)}')
        n+=65;w+=65
    n= 10;w = 75;g+=65;h+=65
def igra(bo):
    one_vs["state"] = DISABLED
    bot_vs["state"] = DISABLED
    global u
    boti = bo
    canvas.tag_bind(clet1, "<ButtonPress>", lambda e: sos(clet1,boti))
    canvas.tag_bind(clet2, "<ButtonPress>", lambda e: sos(clet2,boti))
    canvas.tag_bind(clet3, "<ButtonPress>", lambda e: sos(clet3,boti))
    canvas.tag_bind(clet4, "<ButtonPress>", lambda e: sos(clet4,boti))
    canvas.tag_bind(clet5, "<ButtonPress>", lambda e: sos(clet5,boti))
    canvas.tag_bind(clet6, "<ButtonPress>", lambda e: sos(clet6,boti))
    canvas.tag_bind(clet7, "<ButtonPress>", lambda e: sos(clet7,boti))
    canvas.tag_bind(clet8, "<ButtonPress>", lambda e: sos(clet8,boti))
    canvas.tag_bind(clet9, "<ButtonPress>", lambda e: sos(clet9,boti))
    if boti == 1:
        canvas.tag_bind(clet1, "<ButtonRelease>", lambda e: bot(clet1))
        canvas.tag_bind(clet2, "<ButtonRelease>", lambda e: bot(clet2))
        canvas.tag_bind(clet3, "<ButtonRelease>", lambda e: bot(clet3))
        canvas.tag_bind(clet4, "<ButtonRelease>", lambda e: bot(clet4))
        canvas.tag_bind(clet5, "<ButtonRelease>", lambda e: bot(clet5))
        canvas.tag_bind(clet6, "<ButtonRelease>", lambda e: bot(clet6))
        canvas.tag_bind(clet7, "<ButtonRelease>", lambda e: bot(clet7))
        canvas.tag_bind(clet8, "<ButtonRelease>", lambda e: bot(clet8))
        canvas.tag_bind(clet9, "<ButtonRelease>", lambda e: bot(clet9))
one_vs = Button(root,text="1 vs 1",bg ="#80CBC4",fg="#282828",activebackground="#80CBC4",font="System 17",command = lambda: igra(0))
canvas.create_window(215, 50, anchor=NW, window=one_vs, width=125, height=50)
bot_vs = Button(root,text="1 vs bot",bg ="#80CBC4",fg="#282828",activebackground="#80CBC4",font="System 17",command = lambda: igra(1))
canvas.create_window(215, 120, anchor=NW, window=bot_vs, width=125, height=50)
root.mainloop()
