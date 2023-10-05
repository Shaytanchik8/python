from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Сортировка и поиск букв")
window.geometry('400x300')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

textInput_1 = Entry(
    frame,
)
textInput_1.grid(row=1, column=1)

def mergeSort(text_sort):
    if len(text_sort) == 1:
        return text_sort

    mid = (len(text_sort) - 1) // 2
    left = mergeSort(text_sort[:mid + 1])
    right = mergeSort(text_sort[mid + 1:])
    result_sort = merge(left, right)
    return result_sort

def merge(left, right):
    result = []
    i = j = 0

    while (i <= len(left) - 1 and j <= len(right)-1):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i>len(left)-1:
        while j <= len(right)-1:
            result.append(right[j])
            j += 1

    else:
        while i <= len(left) - 1:
            result.append(left[i])
            i += 1

    return ''.join(result)

label = Label(
    frame,
)
label.grid(row=2, column=1)

def method():
    text_sort = str(textInput_1.get()).replace(" ", "")
    s = mergeSort(text_sort)
    label.configure(text="Отсортированный список: " +s)
    return s



button_1 = Button(
    frame,
    text='сортировать',
    command=method
)
button_1.grid(row=1, column=3)


textInput_2 = Entry(
    frame,
)
textInput_2.grid(row=3, column=1)

def BinarySearch(text, val):
    left = 0
    right = len(text)-1
    index = -1
    while (left <= right) and (index == -1):
        mid = (left + right) // 2
        if text[mid] == val:
            index = mid
        else:
            if val < text[mid]:
                right = mid - 1
            else:
                left = mid + 1
    if index == -1:
        return False
    else:
        return True

def method2():
    text_sort = str(textInput_1.get()).replace(" ", "")
    s = mergeSort(text_sort)
    if BinarySearch(s, str(textInput_2.get())) == True:
        #return label2.configure(text="" )
        messagebox.showinfo('sort', f'Буква "{textInput_2.get()}" найдена в списке')
    else:
       # return label2.configure(text= "111111")
       messagebox.showinfo('sort', f'Буква "{textInput_2.get()}" не найдена в списке')


button_2 = Button(
    frame,
    text='поиск',
    command=method2
)

button_2.grid(row=3, column=3)

label2 = Label(
    frame,
)
label2.grid(row=4, column=1)

window.mainloop()
