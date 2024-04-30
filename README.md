# -*- coding: utf-8 -*-
from flask import Flask

app=Flask(__name__)


@app.route("/Horas/<dias>")
def conversor_dias_horas(dias):
    resultado = int(dias)*24
  return f" (dias) dias son {resultado} horas"

@app.route("/Horas/<minutos>")
def conversor_dias_horas(dias):
    resultado = int(dias)*24
  return f" (minutos) dias son {resultado} minutos"

if __name__=="__main__":
  app.run()
