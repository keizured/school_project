from tkinter import *
from tkinter import messagebox as mb
from math import *
import time
I_Value = 5
k = 3
N = 8
r = 100
R = 200
provoda = []
drawing_in_proccess = False
entrys = []


class Provod:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = 0
        self.r = 0
        self.F = 0
        self.Fx = 0
        self.Fy = 0


def loading(canv):
    canv.create_text(20, 700, text='Рисование в процессе...', font=('Arial Black', 20), anchor=W, tag='load')
    canv.update()
    time.sleep(1)


def drawing():
    global provoda, I_Value,  r, R, drawing_in_proccess, N
    check_rad()
    starts = [760-R-(R/5), 760-R-15, 760-R+15, 760-((R-r)/2)-r, 760-r-10]
    drawing_in_proccess = True
    loading(cooler_canvas)
    cooler_canvas.update
    provoda = []
    
    for dot in range(2*N):
        NewProvod = Provod()
        provoda.append(NewProvod)
        alpha = pi*dot/N
        if dot % 2 == 0 or dot == 0:
            NewProvod.x = r*cos(alpha) + 760
            NewProvod.y = r*sin(alpha) + 540
            canvas.create_oval(NewProvod.x-3, NewProvod.y-3, NewProvod.x+3, NewProvod.y+3, fill='blue', tag='drawing')
        else:
             NewProvod.x = R*cos(alpha) + 760
             NewProvod.y = R*sin(alpha) + 540
             canvas.create_oval(NewProvod.x-3, NewProvod.y-3, NewProvod.x+3, NewProvod.y+3, fill='red', tag='drawing')
    for i in range(len(starts)):
        x_start = starts[i]
        y_start = 540
        canvas.create_oval(x_start-3, y_start-3, x_start+3, y_start+3, fill='black', tag='drawing')
        nx_start = x_start
        ny_start = y_start
        count = 0
        while count<5000 and not((nx_start-60<x_start<nx_start+60) and (ny_start-5<y_start<ny_start+5) and count>200):
                count+=1
                F1x = 0
                F1y = 0
                for u in range(2*N):
                    provoda[u].dx = x_start-provoda[u].x
                    provoda[u].dy = provoda[u].y-y_start
                    provoda[u].r = sqrt(provoda[u].dx**2+provoda[u].dy**2)
                    provoda[u].F = k*2*I_Value/provoda[u].r
                    provoda[u].Fx = provoda[u].F*(provoda[u].dy/provoda[u].r)
                    provoda[u].Fy = provoda[u].F*(provoda[u].dx/provoda[u].r)
                    F1x += provoda[u].Fx
                    F1y += provoda[u].Fy
                canvas.create_line(x_start, y_start, x_start+F1x, y_start+F1y, fill='purple',
                                   tag='drawing')
                x_start = x_start + F1x
                y_start = y_start + F1y
    cooler_canvas.delete('load')
    drawing_in_proccess = False


def escape(event):
    answer = mb.askyesno(title="Выход из программы", message="Вы уверены, что хотите выйти?")
    if answer:
        exit()


def set_canvases(root):
    global canvas, cooler_canvas
    canvas = Canvas(root, width=1520, height=1080, bg='white')
    cooler_canvas = Canvas(root, width=400, height=1080, bg='#e0e3de')
    canvas.pack()
    cooler_canvas.pack()
    canvas.place(x=400, y=0)
    cooler_canvas.place(x=0, y=0)


def startt(root):
    button_start = Button(text='Перейти в меню', width=20, height=4, master=start_page,
                          command=lambda: button_start_destroy(button_start),
                          font=('Tahoma', 30))
    button_start.pack()
    button_start.place(x=670, y=500)


def from_menu_to_front(a, b, c, d):
    destroy_menu(a, b, c, d)
    frontpage_present()
    startt(root)


def button_start_destroy(button):
    button.destroy()
    start_page.delete('all')
    make_menu()


def destroy_menu(a, b, c, d):
    a.destroy()
    b.destroy()
    c.destroy()
    d.destroy()
    start_page.delete('all')


def description(a, b, c, d):

    destroy_menu(a, b, c, d)
    start_page.create_text(900, 600, justify='center', anchor=CENTER,
                           text='*Для вызова помощи нажмите <F1>',
                           font=('Comic Sans MS', 20))
    start_page.create_text(1600, 800, justify='center', anchor=CENTER,
                           text='*Для выхода из программы,\n нажмите кнопку <Esc>',
                           font=('Comic Sans MS', 20))
    start_page.create_text(400, 800, justify='center', anchor=CENTER,
                           text='*Для перехода в меню,\n нажмите на <Перейти в меню> левой кнопкой мыши',
                           font=('Comic Sans MS', 20))
    start_page.create_text(900, 100, justify='center', anchor=CENTER, text='Условие',
                           font =('Tahoma, 30'))
    start_page.create_text(900, 300, font=('Tahoma', 30), anchor=CENTER, justify='center',
                           text='Составить программу, моделирующую построение линий магнитной индукции поля,' +
                                '\nсоздаваемого тором с током. Рассмотреть возможность задать направление тока.')
    quit_descript = Button(text='Перейти в меню', width=20, height=3,
                           font=('Tahoma', 30), command=lambda: button_start_destroy(quit_descript))
    quit_descript.pack()
    quit_descript.place(x=820, y=700)


def help_text(a, b, c, d):
    destroy_menu(a, b, c, d)

    start_page.create_text(20, 250, font=('Tahoma', 20), anchor=W,
                             text='1. Для вызова помощи нажмите клавишу <F1>' +
                                  '\n2. Окно помощи пропадает, при смещении фокуса на главное окно' +
                                  '\n3. Для того, чтобы закрыть программу нажмите клавишу <Esc>' +
                                  '\n4. Чтобы выбрать любой пункт меню, кликните на него левой кнопкой мыши' +
                                  '\n5. Для автозаполнения нажмите <F3>, чтобы оно прошло,' +
                                  '\nнеобходимо перезайти в пункт <Моделирование>' +
                                  '\n6. Кнопки отключаются на время рисования' +
                                  '\n(кроме кнопок выхода и помощи)' +
                                  '\n7. Количество должно быть целым и между 3 и 20' +
                                  '\n8. Сила тока может быть дробной, но между 1 и 10' +
                                  '\n9. Малый радиус может быть дробным, но между 20 и 400' +
                                  '\n10. Большой радиус может быть дробным, но между 50 и 500' +
                                  '\n11. Большой радиус должен быть больше малого минимум на 50'
                                  '\n12. При вводе некорретных значений, они меняются на значения по умолчанию')


    quit_help = Button(text='Перейти в меню', width=20, height=3,
                           font=('Tahoma', 30), command=lambda: button_start_destroy(quit_help))
    quit_help.pack()
    quit_help.place(x=720, y=700)


def help_popup(event):
    popup = Toplevel()
    popup.title('Помощь')
    popup.geometry('1000x800')
    popup.focus()
    popup_canvas = Canvas(popup, width=1000, height=800, bg='white')
    popup_canvas.pack()
    popup_canvas.create_text(500, 30, text='Помощь', font=('Tahoma', 30))
    popup_canvas.create_text(20, 350, font=('Tahoma', 20), anchor=W,
                           text='1. Для вызова помощи нажмите клавишу <F1>' +
                                '\n2. Окно помощи пропадает, при смещении фокуса на главное окно' +
                                '\n3. Для того, чтобы закрыть программу нажмите клавишу <Esc>' +
                                '\n4. Чтобы выбрать любой пункт меню, кликните на него левой кнопкой мыши' +
                                '\n5. Для автозаполнения нажмите <F3>, чтобы оно прошло,' +
                                '\nнеобходимо перезайти в пункт <Моделирование>' +
                                '\n6. Кнопки отключаются на время рисования' +
                                '\n(кроме кнопок выхода и помощи)' +
                                '\n7. Количество должно быть целым и между 3 и 20' +
                                '\n8. Сила тока может быть дробной, но между 1 и 10' +
                                '\n9. Малый радиус может быть дробным, но между 20 и 400' +
                                '\n10. Большой радиус может быть дробным, но между 50 и 500' +
                                '\n11. Большой радиус должен быть больше малого минимум на 50'
                                '\n12. При вводе некорретных значений,' +
                                '\nони меняются на значения по умолчанию')
    popup.bind('<FocusOut>', popup.quit())
    popup.mainloop()

def make_menu():
    descript_button = Button(text='Условие', width=20, height=3, font=('Tahoma', 30),
                             command=lambda: description(descript_button, help_button, model_button, frontpage_button))
    descript_button.pack()
    descript_button.place(x=770, y=120)

    help_button = Button(text='Помощь', width=20, height=3, font=('Tahoma', 30),
                         command=lambda: help_text(descript_button, help_button, model_button, frontpage_button))
    help_button.pack()
    help_button.place(x=770, y=320)

    model_button = Button(text='Моделирование', width=20, height=3, font=('Tahoma', 30),
                          command=lambda: model_func(descript_button, help_button, model_button, frontpage_button))
    model_button.pack()
    model_button.place(x=770, y=520)

    frontpage_button = Button(text='Заставка', width=20, height=3, font=('Tahoma', 30),
                              command=lambda: from_menu_to_front(descript_button, help_button, model_button, frontpage_button))
    frontpage_button.pack()
    frontpage_button.place(x=770, y=720)

    start_page.create_text(1600, 300, justify='center', anchor = CENTER,
                           text='*Для перехода к пункту,\n кликните на него левой кнопкой мыши',
                           font=('Comic Sans MS', 20))
    start_page.create_text(300, 500, justify='center', anchor=CENTER,
                           text='*Для выхода из программы,\n нажмите кнопку <Esc>',
                           font=('Comic Sans MS', 20))
    start_page.create_text(1600, 700, justify='center', anchor=CENTER,
                           text='*Для вызова помощи нажмите <F1>',
                           font=('Comic Sans MS', 20))


def frontpage_present():
    introduction_text = 'Зачетная работа по информатике\n ученика 10 класса Г\n Недбая Павла\n\n\n Задание №15'
    start_page.create_text(890, 240, anchor=CENTER, text=introduction_text, font=('Tahoma', 30), justify='center')
    start_page.create_text(890, 800, justify='center',
                       text='*Для перехода в меню, нажмите на <Перейти в меню> левой кнопкой мыши',
                       font=('Comic Sans MS', 20))
    start_page.create_text(890, 900, justify='center', text='*Для выхода из программы нажмите клавишу <Esc>',
                       font=('Comic Sans MS', 20))
    start_page.create_text(890, 1000, justify='center', text='*Для вызова помощи нажмите <F1>',
                           font=('Comic Sans MS', 20))


def insert_smth(ent, param):
    global I_Value, r, R, N
    if param == 'I':
        try:
            value = float(ent.get())
            if 1.0 <= value <= 10.0:
                I_Value = value
            else:
                ent.delete(0, END)
                ent.insert(END, 5)
        except:
            ent.delete(0, END)
            ent.insert(END, 5)

    if param == 'N':
        try:
            value = int(ent.get())
            if 3 <= value <= 20:
                N = value
            else:
                ent.delete(0, END)
                ent.insert(END, 8)
        except:
            ent.delete(0, END)
            ent.insert(END, 8)
    if param == 'r':
        try:
            value = float(ent.get())
            if 20 <= value <= 400:
                r = value
            else:
                ent.delete(0, END)
                ent.insert(END, 100)
        except:
            ent.delete(0, END)
            ent.insert(END, 100)
    if param == 'R':
        try:
            value = float(ent.get())
            if 50<=value<=500:
                R = value
            else:
                ent.delete(0, END)
                ent.insert(END, 200)
        except:
            ent.delete(0, END)
            ent.insert(END, 200)





def from_model_to_menu():
    global start_page, drawing_in_proccess
    if not drawing_in_proccess:
        canvas.destroy()
        cooler_canvas.destroy()
        start_page = Canvas(root, width=1920, height=1080, bg='white')
        start_page.pack()
        make_menu()


def model_func(a, b, c, d):
    global I_Value, r, R, entrys, N
    destroy_menu(a, b, c, d)
    start_page.destroy()
    set_canvases(root)
    Button_From_Mod = Button(text='Меню', width=10, height=2, font=('Tahoma', 10), command=lambda: from_model_to_menu())
    Button_From_Mod.pack()
    Button_From_Mod.place(x=20, y=1000)
    I_ENtry = Entry(width=30)
    I_ENtry.pack()
    I_ENtry.place(x=140, y=30)
    I_ENtry.insert(END, I_Value)
    I_Button = Button(text='Вставить', width=25, command=lambda: insert_smth(I_ENtry, 'I'))
    I_Button.pack()
    I_Button.place(x=140, y=60)
    cooler_canvas.create_text(70, 40, text='Сила Тока:', font=('Tahoma', 15))
    N_ENtry = Entry(width=30)
    N_ENtry.pack()
    N_ENtry.place(x=140, y=140)
    N_ENtry.insert(END, N)
    N_Button = Button(text='Вставить', width=25, command=lambda: insert_smth(N_ENtry, 'N'))
    N_Button.pack()
    N_Button.place(x=140, y=170)
    cooler_canvas.create_text(70, 160, text='Количество\nвитков:', font=('Tahoma', 15))
    r_ENtry = Entry(width=30)
    r_ENtry.pack()
    r_ENtry.place(x=140, y=250)
    r_ENtry.insert(END, r)
    r_Button = Button(text='Вставить', width=25, command=lambda: insert_smth(r_ENtry, 'r'))
    r_Button.pack()
    r_Button.place(x=140, y=280)
    cooler_canvas.create_text(60, 250, text='Малый\nрадиус:', font=('Tahoma', 15))
    R_ENtry = Entry(width=30)
    R_ENtry.pack()
    R_ENtry.place(x=140, y=360)
    R_ENtry.insert(END, R)
    R_Button = Button(text='Вставить', width=25, command=lambda: insert_smth(R_ENtry, 'R'))
    R_Button.pack()
    R_Button.place(x=140, y=390)
    cooler_canvas.create_text(60, 380, text='Большой\nрадиус:', font=('Tahoma', 15))
    entrys.append(r_ENtry)
    entrys.append(R_ENtry)
    Draw_Button = Button(text='Нарисовать', width=40, height=5, command=lambda:drawing())
    Draw_Button.pack()
    Draw_Button.place(x=50, y=430)
    Erase_Button = Button(text='Стереть', width=40, height=5, command=lambda:canvas.delete('drawing'))
    Erase_Button.pack()
    Erase_Button.place(x=50, y=530)
    cooler_canvas.create_text(15, 850, anchor=W, font=('Comic Sans MS', 15),
                                                       text='*Для перехода в меню, нажмите' +
                              '\n левой кнопкой мыши на <Меню>' +
                              '\n*Для вызова помощи нажмите <F1>' +
                              '\n*Чтобы активировать кнопку,' +
                              '\n нажмите на нее левой кнопкой мыши' +
                              '\n*Для того, чтобы автозаполнение' +
                              '\n сработало, необходимо перезайти' +
                              '\n в пункт <Моделирование>')


def check_rad():
    global r, R, entrys, N
    dr = R-r
    if dr < 50:
        r = 100
        R = 200
        entrys[0].delete(0, END)
        entrys[0].insert(END, 100)
        entrys[1].delete(0, END)
        entrys[1].insert(END, 200)
    else:
        pass


def autofill(event):
    global I_Value, cooler_canvas, I_ENtry, N_ENtry, r, R
    I_Value = 5
    N = 8
    r = 100
    R = 200


root = Tk()
root.geometry('1920x1080')
root.title('Programm')
canvas = Canvas()
cooler_canvas = Canvas()
start_page = Canvas()
I_ENtry = Entry()
N_ENtry = Entry()


def fff():
    global cooler_canvas, canvas, start_page
    canvas = Canvas(root, width=1520, height=1080, bg='white')
    cooler_canvas = Canvas(root, width=400, height=1080, bg='#e0e3de')
    start_page = Canvas(root, width=1920, height=1080, bg='white')
    start_page.pack()


def show(event):
    global r, R
    print(r, R)


fff()
frontpage_present()
startt(root)
root.bind('<F7>', show)
root.bind('<F3>', autofill)
root.bind('<F1>', help_popup)
root.bind('<Escape>', escape)
root.mainloop()
