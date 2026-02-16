from tkinter import Tk, Entry, Button, font, StringVar

digito = ''

def tomar_digito(n):
    global digito
    digito = digito + str(n)
    calculo.set(digito)

def borrar_uno():
    global digito
    digito = digito[:-1]
    calculo.set(digito)

def resultado():
    try:
        global digito
        cuenta = digito.replace('%', '/100')
        total = str(eval(cuenta))
        calculo.set(total)
        digito = total
    except:
        calculo.set('Error')
        digito = ''

def limpiar_completo():
    global digito
    calculo.set('')
    digito = ''

ventana = Tk()

ventana.configure(background="#FADADD") 
ventana.title("Calculadora Basica")
ventana.geometry("400x600")
ventana.resizable(False,False)

calculo = StringVar()

texto_entry = font.Font(family="Roboto", size=25, weight="bold")
texto_botones = font.Font(family="Roboto", size=15, weight="bold")

datos = Entry(ventana, width=20, justify='right', font=texto_entry, fg="#474545", bg="lightgrey", textvariable=calculo)
datos.grid(row=0, column=0, columnspan=4, ipady=20, pady=20)

btnC = Button(ventana, text='C', bg='hotpink', fg='white', width=6, height=2, font=texto_botones, command=limpiar_completo)
btnC.grid(row=1, column=0, padx=5, pady=5)

btnDel = Button(ventana, text='DEL', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=borrar_uno)
btnDel.grid(row=1, column=1, padx=5, pady=5)

btnPorc = Button(ventana, text='%', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('%'))
btnPorc.grid(row=1, column=2, padx=5, pady=5)

btnDividir = Button(ventana, text='/', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('/'))
btnDividir.grid(row=1, column=3, padx=5, pady=5)

btn7 = Button(ventana, text='7', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(7))
btn7.grid(row=2, column=0, padx=5, pady=5)

btn8 = Button(ventana, text='8', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(8))
btn8.grid(row=2, column=1, padx=5, pady=5)

btn9 = Button(ventana, text='9', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(9))
btn9.grid(row=2, column=2, padx=5, pady=5)

btnPor = Button(ventana, text='*', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('*'))
btnPor.grid(row=2, column=3, padx=5, pady=5)

btn4 = Button(ventana, text='4', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(4))
btn4.grid(row=3, column=0, padx=5, pady=5)

btn5 = Button(ventana, text='5', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(5))
btn5.grid(row=3, column=1, padx=5, pady=5)

btn6 = Button(ventana, text='6', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(6))
btn6.grid(row=3, column=2, padx=5, pady=5)

btnResta = Button(ventana, text='-', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('-'))
btnResta.grid(row=3, column=3, padx=5, pady=5)

btn1 = Button(ventana, text='1', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(1))
btn1.grid(row=4, column=0, padx=5, pady=5)

btn2 = Button(ventana, text='2', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(2))
btn2.grid(row=4, column=1, padx=5, pady=5)

btn3 = Button(ventana, text='3', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(3))
btn3.grid(row=4, column=2, padx=5, pady=5)

btnMas = Button(ventana, text='+', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('+'))
btnMas.grid(row=4, column=3, padx=5, pady=5)

btn0 = Button(ventana, text='0', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(0))
btn0.grid(row=5, column=0, padx=5, pady=5)

btnDec = Button(ventana, text='.', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('.'))
btnDec.grid(row=5, column=1, padx=5, pady=5)

btnPA = Button(ventana, text='(', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito('('))
btnPA.grid(row=5, column=2, padx=5, pady=5)

btnPC = Button(ventana, text=')', bg='plum', fg='white', width=6, height=2, font=texto_botones, command=lambda: tomar_digito(')'))
btnPC.grid(row=5, column=3, padx=5, pady=5)

btnIgual = Button(ventana, text='=', bg='mediumorchid', fg='white', width=31, height=2, font=texto_botones, command=resultado)
btnIgual.grid(row=6, column=0, columnspan=4, padx=5, pady=5)

ventana.mainloop()
