from tkinter import *
import tkinter as tk
import time

data=[]   
box_list = []   

def ApplytoLabel():
    
    xx=size.get()
    for i in range(xx):
        element=int(box_list[i].get())
        data.append(element)

    next_screen.destroy()
    
    def merge_sort(data, drawData, timeTick):
        merge_sort_alg(data,0, len(data)-1, drawData, timeTick)


    def merge_sort_alg(data, left, right, drawData, timeTick):
        if left < right:
            middle = (left + right) // 2
            merge_sort_alg(data, left, middle, drawData, timeTick)
            merge_sort_alg(data, middle+1, right, drawData, timeTick)
            merge(data, left, middle, right, drawData, timeTick)

    def merge(data, left, middle, right, drawData, timeTick):
        drawData(data, getColorArray(len(data), left, middle, right))
        time.sleep(timeTick)

        leftPart = data[left:middle+1]
        rightPart = data[middle+1: right+1]

        leftIdx = rightIdx = 0

        for dataIdx in range(left, right+1):
            if leftIdx < len(leftPart) and rightIdx < len(rightPart):
                if leftPart[leftIdx] <= rightPart[rightIdx]:
                    data[dataIdx] = leftPart[leftIdx]
                    leftIdx += 1
                else:
                    data[dataIdx] = rightPart[rightIdx]
                    rightIdx += 1

            elif leftIdx < len(leftPart):
                data[dataIdx] = leftPart[leftIdx]
                leftIdx += 1
            else:
                data[dataIdx] = rightPart[rightIdx]
                rightIdx += 1

        drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
        time.sleep(timeTick)

    def getColorArray(leght, left, middle, right):
        colorArray = []

        for i in range(leght):
            if i >= left and i <= right:
                if i >= left and i <= middle:
                    colorArray.append("yellow")
                else:
                    colorArray.append("pink")
            else:
                colorArray.append("white")

        return colorArray



    def drawData(data, colorArray):
        canvas.delete("all")
        c_height = 380
        c_width = 600
        x_width = c_width / (len(data) + 1)
        offset = 30
        spacing = 10
        normalizedData = [ i / max(data) for i in data]
        for i, height in enumerate(normalizedData):
            #top left
            x0 = i * x_width + offset + spacing
            y0 = c_height - height*340
            #bottom right
            x1 = (i + 1) * x_width + offset
            y1 = c_height

            canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
            canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

        last_screen.update_idletasks()


    def StartAlgorithm():
        global data
        if not data: return

        drawData(data, ['green' for x in range(len(data))])
        merge_sort(data, drawData, speedScale.get())

    def close():
        last_screen.destroy()

    global last_screen
    last_screen=Tk()
    last_screen.geometry("1200x700")
    last_screen.resizable(width=0,height=0)
    
    last_screen.configure(bg='chartreuse3')
    last_screen.title("Entry Page")
    UI_frame = Frame(last_screen, width= 1100, height=200, bg='grey')
    UI_frame.grid(row=0, column=0, padx=10, pady=5)

    global canvas

    canvas = Canvas(last_screen, width=1150, height=430, bg='white')
    canvas.grid(row=2, column=0, padx=10, pady=5)


    Label(UI_frame, text="MERGE SORT ALGORITHM VISUALIZATION",font="Century 20 bold", bg='chartreuse3',fg='white').grid(row=0, column=0, padx=5, pady=5, sticky=W)
    global speedScale
    speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed")
    speedScale.grid(row=1, column=0, padx=5, pady=5)
    Button(UI_frame, text="Start", command=StartAlgorithm, bg='red',width=10).grid(row=1, column=1, padx=5, pady=5)

    Button(last_screen, text="EXIT", command=close, bg='red',width=10).grid(row=3, column=0, padx=5, pady=5)
    Button(last_screen, text="RESET THE INPUT", command=login, bg='red',width=30).grid(row=4, column=0, padx=5, pady=5)


    
def Boxes():
    xx=size.get()
    for i in range(xx):        
        box=tk.Entry(next_screen,font="Arial 10 bold",bd="5",width="5")
        box.pack(side="left")
        box_list.append(box)
   
    
    ApplytoLabel1=tk.Button(next_screen,text="Generate",command=ApplytoLabel)
    ApplytoLabel1.pack(side="left")

def login():
    del data[:]   
    del box_list[:]
    
    try:
        main_screen.destroy()
    except:
        last_screen.destroy()
    global next_screen
    next_screen=Tk()
    next_screen.geometry("1200x700")
    next_screen.resizable(width=0,height=0)
    
    next_screen.configure(bg='chartreuse3')
    next_screen.title("Entry Page")
    Label(next_screen, text="Enter the size of Array",font="Century 16 bold",bg='chartreuse3',fg='white',pady=60).pack()

    global size
    size=tk.IntVar()
    Entry(next_screen,textvariable=size).pack()
    Button(next_screen,text="Submit",command=Boxes).pack()
    
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("600x380")
    main_screen.resizable(width=0,height=0)
    
    main_screen.configure(bg='chartreuse3')
    main_screen.title("Sorting visualization")
    Label(main_screen, text="Welcome to the sorting visualization",font=("Century 20 bold"),bg='chartreuse3',pady=60,fg='white').pack()
    Label(main_screen, text="Enter Your User Name",font=("Century",12),bg='chartreuse3').pack()
    Entry(main_screen, textvariable="username",width="30").pack()
    Label(main_screen,bg='chartreuse3',pady=30).pack()
    Button(text="LOGIN", bg="gold", height="2", width="40",border=8, command =login ).pack()
    

    main_screen.mainloop()


main_account_screen()
