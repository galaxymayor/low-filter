#import itertools as ittl
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as pup
import tkinter.simpledialog as dia 
true,yes,no,false,none=True,True,False,False,None
data = []
sorted_data=[]
g=1
name=None
f=2

def clean_data():
    global data,sorted_data
    data,sorted_data=[],[]
def din (val:str=None,split_with:str=None):
    #h:取幾個
    global data#,sorted_data

    '''
    while True :
        instr=input()
        if instr in ('','stop'):
            break
        data.append(input().split(split_with)) 
        print(data)
    '''

    val=val if val else itext.get(1.0,'end')
    data=[s.split(split_with) for s in val.strip().split('\n')]
    #print(data)

    if [len(data[0])]*len(data)!= list(map(len,data)):raise Exception('diff-len error')
def out(h:int,sort:bool=False,keepall:bool=True,name:int=None):  
    global data,sorted_data
    
    if not name:
        for item  in   enumerate(data[-1]) :
            #print(item)
            try:
                float(item[1])
            except:
                continue
            else:
                name=item[0]
                break
    
    namelist=[x[0:name]for x in data]

    vals=list(map(list,map(lambda l :map(float,l),map(lambda l:l[name:],data))))
    #print(vals)
    sorted_data=list(map(sorted,vals))
    #print(sorted_data)
    usedata=list(map(lambda l : l[-h:] ,sorted_data))
    #print(usedata)
    avgl=list(map(lambda l:round(sum(l)/len(l),f),usedata))
    '''
    print(avgl)
    print(namelist)
    print(list(zip(namelist,avgl,list(vals))))
    print(['\t'.join(map(str,l[0]+[l[1]]+l[2])) for l in zip(namelist,avgl,list(vals))])
    print('\n'.join(['\t'.join(map(str,l[0]+[l[1]]+l[2])) for l in zip(namelist,avgl,list(vals))]))
    '''
    return '\n'.join(['\t'.join(map(str,l[0]+[l[1]]+l[2])) for l in zip(namelist,avgl,list(vals))]).replace('.0','')
def run ():
    try:
        din()
        otext.configure(state='normal')
        otext.delete(1.0,'end')
        otext.insert('end',out(h=g,name=name))
        otext.configure(state='disabled')
    except ZeroDivisionError as e:
        otext.configure(state='normal')
        otext.delete(1.0,'end')
        otext.insert('end','取值也許出錯\n'+str(e.args))
        otext.configure(state='disabled')
    except Exception as e:
        otext.configure(state='normal')
        otext.delete(1.0,'end')
        otext.insert('end',e.args)
        otext.configure(state='disabled')
def clean ():
    otext.configure(state='normal')
    otext.delete(1.0,'end')
    otext.configure(state='disabled')
    itext.delete(1.0,'end')
def ask_number ():
    global g
    g=dia.askinteger('input','輸入欲取之成績量')
def ask_name():
    global name
    name=dia.askinteger('input','輸入標示長度')
    name =name if name else None
def ask_f():
    global f
    f=dia.askinteger('input','小數點位數')
    f=abs(f)
'''
a=[]
for _ in range(10):a.append(list(input().split()))
print(a)
'''

base=tk.Tk()
base.title('低分過濾器')
#
menub=tk.Menu(base,bd=0)
setmu=tk.Menu(menub,tearoff=0)

menub.add_cascade(label='設定',underline=0,menu=setmu)
setmu.add_command(label='取幾個',  command=ask_number)
setmu.add_command(label='標籤長度',command=ask_name)
setmu.add_command(label='小數位數',command=ask_f)
base.configure(menu=menub)

iarea=ttk.Labelframe(base,text='input')
oarea=ttk.Labelframe(base,text='out')
marea=tk.Frame(base)
itext=tk.Text(iarea,bd=0,width=100)
otext=tk.Text(oarea,bd=0,width=100)
clbut=ttk.Button(marea,text='清除',command=clean)
rubut=ttk.Button(marea,text='計算'  ,command=run)


itext.pack()
otext.pack()

clbut.pack(side=tk.LEFT)
rubut.pack(side=tk.LEFT)

otext.configure(state='disabled')

iarea.pack()
marea.pack()
oarea.pack()

print('歡迎使用取高分程式：\n左上方設定提供欲取之最高成績個數，0表示全部-n表示去除n個低分。\n標籤長度標示姓名／座號佔前幾項，0表示自動偵測。\n小數位數標示平均值準確度。')


base.mainloop()
'''
din()
out(2)
'''