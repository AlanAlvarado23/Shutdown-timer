# Author: Alan Ricardo Alvarado Ahedo
# LinkedIn: https://www.linkedin.com/in/alan-alvarado-ahedo-629a04271/
# GitHub: https://github.com/AlanAlvarado23
# Email: alan.alvarado2303@gmail.com

from os import system
from time import sleep
from tkinter import *

global status_set, apagado
status_set = False
apagado = False

def set_all0 ():
	horas.set(0)
	minutos.set(0)
	segundos.set(0)

	texto_status.config(text="Tiempo 0 segundos", fg="white")
	texto_set_horas.config(text=0)
	texto_set_minutos.config(text=0)
	texto_set_segundos.config(text=0)

def cancelar ():

	set_all0()
	
	if apagado:
		texto_status.config(text="Apagado cancelado", fg="white")
		system("shutdown -a")

	else:
		texto_status.config(text="No hay operación en curso", fg="white")

def apagar ():
	print(status_set)

	tiempo_horas = horas.get()
	tiempo_minutos = minutos.get()
	tiempo_segundos = segundos.get()

	tiempo_final = (tiempo_horas*60*60) + (tiempo_minutos*60) + tiempo_segundos

	if status_set == False:
		texto_status.config(text="Error, no hay tiempo configurado", fg="red")

	elif tiempo_final <= 0:
		texto_status.config(text="Error, el tiempo es 0", fg="red")

	else:
		texto_status.config(text="Iniciado", fg="green")
		comando = "shutdown -s -t  {} ".format(tiempo_final)
		global apagado
		apagado = True

		system(comando)

def setear ():
	global status_set
	status_set = True
	tiempo_horas = horas.get()
	tiempo_minutos = minutos.get()
	tiempo_segundos = segundos.get()

	tiempo_final = (tiempo_horas*60*60) + (tiempo_minutos*60) + tiempo_segundos

	texto_status.config(text="Tiempo {} segundos".format(tiempo_final), fg="white")
	texto_set_horas.config(text=tiempo_horas)
	texto_set_minutos.config(text=tiempo_minutos)
	texto_set_segundos.config(text=tiempo_segundos)

	print(status_set)

def set_2horas ():
	horas.set(2)

def set_45min ():
	minutos.set(45)

def set_30min ():
	minutos.set(30)

def set0 (variable):
	variable.set(0)

def mas (variable, cantidad):
	dato = variable.get()
	variable.set(dato+cantidad)

def menos (variable, cantidad):
	dato = variable.get()
	if dato - cantidad < 0:
		variable.set(0)

	else:
		variable.set(dato-cantidad)

def main ():

	color_texto = "white"
	color_entradas = "#151515"
	color_fondo = "black"

	global horas, minutos, segundos, texto, texto_status1, texto_status2, texto_set_horas, texto_set_minutos, texto_set_segundos, texto_status

	raiz = Tk()
	raiz.geometry("800x800")
	raiz.config(bg=color_fondo)
	raiz.title("Apagado Automático")

	frame_principal = Frame(raiz, bg=color_fondo)
	frame_principal.place(relx=0.5,rely=0.5,anchor="c")

	#--------------------------------------------------------------- Texto Status
	frame_status = Frame(frame_principal, bg=color_fondo, width=20, height=20)
	frame_status.grid(row=0, column=0, pady=30, sticky="n", padx=190)

	Label(frame_status, text="Status:", font=("Arial", 16), bg=color_fondo, fg=color_texto).grid(row=1, column=0, pady=10, padx=3, columnspan=2, sticky="e")
	texto_status = Label(frame_status, text="Tiempo 0 segundos", font=("Arial", 16), bg=color_fondo, fg=color_texto)
	texto_status.grid(row=1, column=2, pady=10, columnspan=4, sticky="w", padx=2)

	Label(frame_status, text="Horas:", font=("Arial", 20), bg=color_fondo, fg=color_texto).grid(row=0, column=0, sticky="e", padx=15)
	Label(frame_status, text="Minutos:", font=("Arial", 20), bg=color_fondo, fg=color_texto).grid(row=0, column=2, sticky="e", padx=15)
	Label(frame_status, text="Segundos:", font=("Arial", 20), bg=color_fondo, fg=color_texto).grid(row=0, column=4, sticky="e", padx=15)

	texto_set_horas = Label(frame_status, text="0", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_set_horas.grid(row=0, column=1, sticky="w", padx=2)

	texto_set_minutos = Label(frame_status, text="0", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_set_minutos.grid(row=0, column=3, sticky="w", padx=2)

	texto_set_segundos = Label(frame_status, text="0", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_set_segundos.grid(row=0, column=5, sticky="w", padx=2)

	boton_iniciar = Button(frame_status, text="Iniciar", font=("Arial", 20), command=apagar)
	boton_iniciar.config(bg=color_entradas, fg=color_texto)
	boton_iniciar.grid(row=2, column=0, sticky="n", pady=15, padx=2, columnspan=3)

	boton_cancelar = Button(frame_status, text="cancelar", font=("Arial", 20), command=cancelar)
	boton_cancelar.config(bg=color_entradas, fg=color_texto)
	boton_cancelar.grid(row=2, column=3, sticky="n", pady=15, padx=2, columnspan=3)

	#--------------------------------------------------------------- Entradas tiempo
	frame_entrys = Frame(frame_principal, bg=color_fondo, width=720, height=720)
	frame_entrys.grid(row=1, column=0, pady=15, sticky="n", padx=150)

	horas = IntVar()
	minutos = IntVar()
	segundos = IntVar()

	texto_horas=Label(frame_entrys, text="Horas:", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_horas.grid(row=0, column=0, sticky="e", pady=15, padx=10)

	cuadro_horas=Entry(frame_entrys, textvariable=horas)
	cuadro_horas.grid(row=0, column=3, sticky="w", pady=15)
	cuadro_horas.config(fg=color_texto,bg=color_entradas, justify="center", font=("Arial", 20))

	boton_horas_menos = Button(frame_entrys, text="-", font=("Arial", 18), command=lambda:menos(horas, 1))
	boton_horas_menos.config(bg=color_entradas, fg=color_texto)
	boton_horas_menos.grid(row=0, column=1, sticky="n", pady=15, padx=2, columnspan=2)

	boton_horas_mas = Button(frame_entrys, text="+", font=("Arial", 18), command=lambda:mas(horas, 1))
	boton_horas_mas.config(bg=color_entradas, fg=color_texto)
	boton_horas_mas.grid(row=0, column=4, sticky="n", pady=15, padx=2, columnspan=2)

	boton_horas_cero = Button(frame_entrys, text="0", font=("Arial", 18), command=lambda:set0(horas))
	boton_horas_cero.config(bg=color_entradas, fg=color_texto)
	boton_horas_cero.grid(row=0, column=6, sticky="n", pady=15, padx=10)



	texto_minutos=Label(frame_entrys, text="Minutos:", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_minutos.grid(row=1, column=0, sticky="e", pady=15, padx=10)

	cuadro_minutos=Entry(frame_entrys, textvariable=minutos)
	cuadro_minutos.grid(row=1, column=3, sticky="w", pady=15)
	cuadro_minutos.config(fg=color_texto,bg=color_entradas, justify="center", font=("Arial", 20))

	boton_minutos_menos5 = Button(frame_entrys, text="-5", font=("Arial", 18), command=lambda:menos(minutos, 5))
	boton_minutos_menos5.config(bg=color_entradas, fg=color_texto)
	boton_minutos_menos5.grid(row=1, column=1, sticky="n", pady=15, padx=2)

	boton_minutos_menos = Button(frame_entrys, text="-", font=("Arial", 18), command=lambda:menos(minutos, 1))
	boton_minutos_menos.config(bg=color_entradas, fg=color_texto)
	boton_minutos_menos.grid(row=1, column=2, sticky="n", pady=15, padx=2)

	boton_minutos_mas = Button(frame_entrys, text="+", font=("Arial", 18), command=lambda:mas(minutos, 1))
	boton_minutos_mas.config(bg=color_entradas, fg=color_texto)
	boton_minutos_mas.grid(row=1, column=4, sticky="n", pady=15, padx=2)

	boton_minutos_mas5 = Button(frame_entrys, text="+5", font=("Arial", 18), command=lambda:mas(minutos, 5))
	boton_minutos_mas5.config(bg=color_entradas, fg=color_texto)
	boton_minutos_mas5.grid(row=1, column=5, sticky="n", pady=15, padx=2)

	boton_minutos_cero = Button(frame_entrys, text="0", font=("Arial", 18), command=lambda:set0(minutos))
	boton_minutos_cero.config(bg=color_entradas, fg=color_texto)
	boton_minutos_cero.grid(row=1, column=6, sticky="n", pady=15, padx=10)



	texto_segundos=Label(frame_entrys, text="Segundos:", font=("Arial", 20), bg=color_fondo, fg=color_texto)
	texto_segundos.grid(row=2, column=0, sticky="e", pady=15, padx=10)

	cuadro_segundos=Entry(frame_entrys, textvariable=segundos)
	cuadro_segundos.grid(row=2, column=3, sticky="w", pady=15, padx=5)
	cuadro_segundos.config(fg=color_texto,bg=color_entradas, justify="center", font=("Arial", 20))

	boton_segundos_menos5 = Button(frame_entrys, text="-5", font=("Arial", 18), command=lambda:menos(segundos, 5))
	boton_segundos_menos5.config(bg=color_entradas, fg=color_texto)
	boton_segundos_menos5.grid(row=2, column=1, sticky="n", pady=15, padx=2)

	boton_segundos_menos = Button(frame_entrys, text="-", font=("Arial", 18), command=lambda:menos(segundos, 1))
	boton_segundos_menos.config(bg=color_entradas, fg=color_texto)
	boton_segundos_menos.grid(row=2, column=2, sticky="n", pady=15, padx=2)

	boton_segundos_mas = Button(frame_entrys, text="+", font=("Arial", 18), command=lambda:mas(segundos, 1))
	boton_segundos_mas.config(bg=color_entradas, fg=color_texto)
	boton_segundos_mas.grid(row=2, column=4, sticky="n", pady=15, padx=2)

	boton_segundos_mas5 = Button(frame_entrys, text="+5", font=("Arial", 18), command=lambda:mas(segundos, 5))
	boton_segundos_mas5.config(bg=color_entradas, fg=color_texto)
	boton_segundos_mas5.grid(row=2, column=5, sticky="n", pady=15, padx=2)

	boton_segundos_cero = Button(frame_entrys, text="0", font=("Arial", 18), command=lambda:set0(segundos))
	boton_segundos_cero.config(bg=color_entradas, fg=color_texto)
	boton_segundos_cero.grid(row=2, column=6, sticky="n", pady=15, padx=10)

	#--------------------------------------------------------------- Botones tiempo
	frame_botones = Frame(frame_principal, bg=color_fondo, width=720, height=720)
	frame_botones.grid(row=2, column=0, sticky="n")

	boton_2hora = Button(frame_botones, text="2 horas", font=("Arial", 16), command=set_2horas)
	boton_2hora.config(bg=color_entradas, fg=color_texto)
	boton_2hora.grid(row=0, column=0, sticky="n", pady=12, padx=20)

	boton_45min = Button(frame_botones, text="45 minutos", font=("Arial", 16), command=set_45min)
	boton_45min.config(bg=color_entradas, fg=color_texto)
	boton_45min.grid(row=0, column=1, sticky="n", pady=12, padx=20)

	boton_30min = Button(frame_botones, text="30 minutos", font=("Arial", 16), command=set_30min)
	boton_30min.config(bg=color_entradas, fg=color_texto)
	boton_30min.grid(row=0, column=2, sticky="n", pady=12, padx=20)

	boton_set0 = Button(frame_botones, text="reiniciar", font=("Arial", 16), command=set_all0)
	boton_set0.config(bg=color_entradas, fg=color_texto)
	boton_set0.grid(row=1, column=0, sticky="n", pady=12, padx=20, columnspan=3)

	#--------------------------------------------------------------- Boton enviar
	frame_enviar = Frame(frame_principal, bg=color_fondo, width=720, height=720)
	frame_enviar.grid(row=3, column=0, sticky="n", pady=30)

	boton_enviar = Button(frame_enviar, text="Enviar", font=("Arial", 21), command=setear)
	boton_enviar.config(bg=color_entradas, fg=color_texto)
	boton_enviar.grid(row=0, column=0, sticky="n", padx=20)

	raiz.mainloop()

if __name__ == '__main__':
	main()