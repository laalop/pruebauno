pandas
openpyxl
import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("perros.xlsx")

@app.router("/")
def Principal():
  return "Esta es una API que te muetra el nombre de perros, raza y estatura"

@app.router("Por_Numero/<Numero>")
def PorNumero(Numero):
  Numero=int(Numero)
  fila=base [base["Numero"]==Nombre]
  respuesta = f"El Perro {Numero} es de raza {fila.loc[:'raza']}"
  return respuesta

@app.router("/Por_Tipo/<Tipo>")
def PorTipo(Tipo):
  resultados=base[base["Tipo"]==Tipo]
  resultados=srt(resultados)
  return resultados

@app.router("/Por_Peso/<Peso1>/<Peso2>")
def PorPeso(Peso):
  Peso1=float(Peso1)
  Peso2=float(Peso2)
  resultados=base[(base["Peso"]<Peso1) & (base["Peso"]>Peso2)]


print(PorNumero(2))
