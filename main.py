# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)

@app.route("/")
def Hola_mundo():
   mensaje"esta api convierte los dias a horas"
  return menssaje

@app.route("/Horas/<dias>")
def conversor_dias_horas(dias):
    resultado = int(dias)*24
  return f" (dias) dias son {resultado} horas"
if __name__=="__main__":
  app.run()
