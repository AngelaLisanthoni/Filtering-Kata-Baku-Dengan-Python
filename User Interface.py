from tkinter import *
from tkinter import messagebox
import tkinter as tk

def kata():
    import numpy as np
    import pandas as pd
    A = pd.read_csv('kataUI.csv')
    x_array = np.array(A)

    def interpolationSearch(A, target):
        # define awal dan akhir
        left = 0
        right = len(A) -1

        #selama max != min dan min <= target <= max
        while A[right] != A[left] and A[left] <= target <= A[right]:
              #mencari mid
              mid = left + (target - A[left]) * (right - left) // (A[right] - A[left])
              #Jika nilai target sama yg di dlm array
              if target == A[mid]:
                 return mid
              #jika nilai target < sama yg di dlm array
              elif target < A[mid]:
                 right = mid - 1
              else:
                 left = mid + 1
        # if the key is found
        if target == A[left]:
           return left
        # target doesn't exist in the list
        return -1

    def user_input(): 
        #User input kata
        key = e1.get()
        outputstr = ''.join(key)
    
        dict = {'a' : '1', 'b' : '2', 'c' :'3', 'd':'4','e' : '5', 'f' : '6', 'g' :'7', 'h':'8','i': '9','j': '10',
                 'k' : '11', 'l' : '12', 'm' :'13', 'n':'14','o' : '15', 'p' : '16', 'q' :'17', 'r':'18','s': '19','t': '20',
                 'u' : '21', 'v' : '22', 'w' :'23', 'x':'24','y' : '25', 'z' : '26'}
        total = '0'

        for i in range(0,len(key)):
             total = total + dict.setdefault(outputstr[i],None)
        ganti = int(total)

        #cari indexnya
        index = interpolationSearch(x_array, ganti)
 
        if index != -1:
             messagebox.showinfo('ada', 'kata' + ' ' + key + ' ' + 'merupakan kata baku yang sesuai dalam database kami')
        else:
             messagebox.showinfo('tidak ada', 'kata'+ ' ' + key + ' ' + 'tidak ada dalam database kami. silahkan periksa https://kbbi.kemdikbud.go.id')
        print()
    user_input()

###########
window = tk.Tk()
window.config(background="light blue")
window.title('Mencari Kata Baku dalam Database')
window.geometry("500x300")

label = Label(text="Pencarian Kata Baku",font="Normal 50", background='light blue')
label.pack()

e1 = Entry(window)
e1.pack()
e1.insert(0,"Masukkan kata...")

button = Button(text='cari',font='Normal 25', activebackground = "blue",command = kata)
button.pack()

label1 = Label(text="Silahkan masukkan kata di kotak yang tersedia", font='Normal 15', background ='light blue')
label1.pack()

label2 = Label(text="klik ok pada messagebox yang muncul", font='Normal 15', background ='light blue')
label2.pack()

label3 = Label(text="Maka Anda bisa memasukkan kata lagi", font='Normal 15', background ='light blue')
label3.pack()
window.mainloop()
