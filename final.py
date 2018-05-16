from tkinter import *
import random

list1=[]
buttons=[]
wlist={}
counter=1
wclick=0
pind=0

wordlist=[[1,3,4],[0,2,3,4,5],[1,4,5],[0,1,4,6,7],[0,1,2,3,5,6,7,8],[1,2,4,7,8],[3,4,7],[3,4,5,6,8],[4,5,7]]

def btnclick(letter,index):
    global i
    global string
    global select
    
    global wclick

    global pind
    wclick+=1
    e2.delete(0, END)
    
    if wclick==1:
        pind=index
        pass

    temp=wordlist[pind]
    if wclick >1:
        if index not in temp:
            e2.delete(0, END)
            e2.insert(0,"Plz Press Valid Key")
            return 
        else:
            pind=index
            pass

    string+=letter
    e1.insert(i,letter)
    i+=1
    buttons[index].config(state="disabled")

  

def Reset(list1):
    global i
    global wclick
    global string
    global counter
    list1=[]
    counter=1

    while len(list1)<rows*cols:
        character=chr(random.randint(97,121))
        list1.append(character)

    string=""
    e1.delete(0, END)
    i=0
    e2.delete(0, END)
    wclick=0
    main(list1)

def getResult():
    global res
    res+=10
    
    string=""
    e1.delete(0, END)
    i=0
    e2.delete(0, END)
  
    e3=Label(window,width=10,text= res)
    e3.config(font=('times', 14, 'bold'))
    e3.grid(row=1,column=2)



def chk_word(list1):
    global string
    global counter
    global wclick
    wclick=0
    e2.delete(0, END)
    if counter > 4:
        Reset(list1) 

    counter+=1
    if string=="":
        print("Press key then press OK")
        return 
        
    listofWords=wlist[string[0]]
    if string in listofWords:
        getResult()
        e2.insert(0,"Valid")
    else:
        e2.delete(0, END)
        e1.delete(0, END)
        e2.insert(0,"InValid")
    
    string = ""
    main(list1)



def main(list1):
    index=0
    for i in range(0,rows):
        for j in range(0,cols):
            b1=Button(window,text=list1[index],width=12,command=lambda k=index: click(list1[k],k),fg="black",bg="white",font=('arial',12,'bold'))
            b1.grid(row=2+i,column=j)
            buttons.append(b1)
            index+=1
        
    ok=Button(window,text="Check", fg="black",font=('arial',10,'bold'),width=10,command=lambda: chk_word(list1))
    ok.grid(row=i+3,column=0,padx=10,pady=20)

    Reset=Button(window,text="Reset", fg="black",bg="green",font=('arial',10,'bold'),width=10,command=lambda: Reset(list1))
    Reset.grid(row=i+3,column=1,padx=10,pady=20)

    cancel=Button(window,text="Cancle", fg="black" ,font=('arial',10,'bold'),width=10,command=window.quit)
    cancel.grid(row=i+3,column=2,padx=10,pady=20)

    window.mainloop()
    

def createHASH(temp):
    global wlist
    for i in range(1,27):
        char=96+i
        wlist[chr(char)]=[]
    print(wlist)
    for i in temp:
        if  len(i)==0:
            return

        if len(i)<10:
            wlist[i[0]].append(i)

def readfile():
    global wlist
    temp = []
    
    fp1=open('data.txt',"r")
    line1=fp1.read()
    temp= line1.split('\n')
    #print(temp)
    createHASH(temp)

if __name__ == "__main__":
    rows=3
    cols=3
    res=0
    i=0
    string=""
    
    readfile()   

    window=Tk()
    window.title("Cross Word Game")
     
    l1=Label(window,text="Enter String",font=('arial',12,'bold'))
    l1.grid(row=0,column=0)
    
    l2=Label(window,text="Reuslt",font=('arial',12,'bold'))
    l2.grid(row=1,column=0)
    
    l3=Label(window,text="Score")
    l3.config(font=('arial', 14, 'bold underline'))
    l3.grid(row=0,column=2)
    
    e1=Entry(window,bd=7,justify='right',width=20,font=('arial',14,'bold'),bg="white")
    e1.grid(row=0,column=1)
    
    e2=Entry(window,bd=7,justify='right',width=20,font=('arial',14,'bold'),bg="white")
    e2.grid(row=1,column=1,padx=10,pady=10)

    e3=Label(window,width=10,text= res)
    e3.config(font=('arial', 14, 'bold'))
    e3.grid(row=1,column=2)
   
    Reset(list1)
