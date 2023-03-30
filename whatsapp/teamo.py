import pyautogui as pt
from time import sleep

import schedule
import time

AMORCITO = "AMOR DE MI VIDA"

def buscar_contacto():
    global x, y
    #Abre whatsapp
    x, y = pt.locateCenterOnScreen('buscar.png', confidence=0.6)
    pt.moveTo(x, y, duration=0.5)
    pt.click()
    sleep(1)

    #Busca a mi amorcito
    pt.typewrite(AMORCITO, interval = 0.1)

    #Selecciona el contacto: PARTE NO AÑADIDA
    result_position = (326, 306) 
    pt.click(result_position)

    #Envia el mensaje
    enviar_mensaje()

def enviar_mensaje():
    global x, y
    #Selecciona el cuadro de texto
    x, y = pt.locateCenterOnScreen('smilie.png', confidence=0.6)
    pt.moveTo(x + 160, y, duration=0.5)
    pt.click()
    sleep(1)

    #Escribe el mensaje
    pt.typewrite("BUENOS DIAS MI AMOL COMO DORMISTE??", interval = 0.1)

    #Envia el mensaje
    x, y = pt.locateCenterOnScreen('enviar.png', confidence=0.8)
    pt.moveTo(x, y, duration=0.5)
    pt.click()


#MODIFICAR LA HORA: 15:40
schedule.every().day.at("15:40").do(buscar_contacto)

#Ejecuta el programa
while True:
    schedule.run_pending()
    time.sleep(1) #puedes poner un sleep de más tiempo
    print("La tarea se ha ejecutado.")  #Para ver que se ejecuta