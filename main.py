
import pydirectinput
import time
import pyautogui
import pyautogui as pt


vermelho = "vermelho.png"
vermelhoclicar = "vermelhoclicar.png"

branco = "branco.png"
brancoclicar = "brancoclicar.png"

roxo= "roxo.png"
roxoclicar = "roxoclicar.png"

azul = "azul.png"
azulclicar = "azulclicar.png"

laranja = "laranja.png"
laranjaclicar = "laranjaclicar.png"

rosa = "rosa.png"
rosaclicar = "rosaclicar.png"

preto = "preto.png"
pretoclicar = "pretoclicar.png"

amarelo = "amarelo.png"
amareloclicar= "amareloclicar.png"

verde = "verde.png"
verdeclicar = "verdeclicar.png"

def minerar():

    if pyautogui.locateOnScreen('branco.png'):
        print("achei")

        brancopos = pt.locateCenterOnScreen(brancoclicar)
        pt.moveTo(brancopos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('roxo.png', confidence = 0.97):
        print("achei")

        roxopos = pt.locateCenterOnScreen(roxoclicar, confidence = 0.97)
        pt.moveTo(roxopos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('azul.png', confidence = 0.97):
        print("achei")

        azulpos = pt.locateCenterOnScreen(azulclicar, confidence = 0.97)
        pt.moveTo(azulpos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('azul2.png', confidence = 0.97):
        print("achei")

        azulpos = pt.locateCenterOnScreen(azulclicar, confidence = 0.97)
        pt.moveTo(azulpos,duration = 0.2)
        pt.click()
        print("sucesso")

    
    if pyautogui.locateOnScreen('laranja.png'):
        print("achei")

        laranjapos = pt.locateCenterOnScreen(laranjaclicar)
        pt.moveTo(laranjapos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('rosa.png', confidence = 0.97):
        print("achei")

        rosapos = pt.locateCenterOnScreen(rosaclicar, confidence = 0.97)
        pt.moveTo(rosapos,duration = 0.2)
        pt.click()
        print("sucesso")
    

    if pyautogui.locateOnScreen('preto.png', confidence = 0.97):
        print("achei")

        pretopos = pt.locateCenterOnScreen(pretoclicar, confidence = 0.97)
        pt.moveTo(pretopos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('amarelo.png', confidence = 0.97):
        print("achei")

        amarelopos = pt.locateCenterOnScreen(amareloclicar, confidence = 0.97)
        pt.moveTo(amarelopos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('vermelho.png'):
        print("achei")

        vermelhopos = pt.locateCenterOnScreen(vermelhoclicar)
        pt.moveTo(vermelhopos,duration = 0.2)
        pt.click()
        print("sucesso")


    if pyautogui.locateOnScreen('verde.png', confidence = 0.97):
        print("achei")

        verdepos = pt.locateCenterOnScreen(verdeclicar, confidence = 0.97)
        pt.moveTo(verdepos,duration = 0.2)
        pt.click()
        print("sucesso")
    
    existir()








def existir():
    pydirectinput.click()
    pydirectinput.moveTo(100,150)

    time.sleep(5)
    pydirectinput.moveTo(-500,550)
    pydirectinput.keyUp("a")
    pydirectinput.keyDown("s")

    time.sleep(10)
    pydirectinput.keyUp("s")
    pydirectinput.moveTo(734,436)

while True:
    minerar()
