import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("perros.xlsx")

@app.route("/")
def Principal():
  return "Esta es una API que te muetra el nombre de perros, raza y estatura"

@app.route("/Por_Numero/<Numero>")
def PorNumero(Numero):
  Numero=int(Numero)
  fila=base[base["Numero"]==Numero]
  respuesta=f"El Perro {Numero} es {fila.loc[:,'Nombre']}"
  return respuesta

@app.route("/Por_raza/<raza>")
def Porraza(raza):
  resultados=base[base["raza"]==raza]
  resultados=srt(resultados)
  return resultados

@app.route("/Por_estatura/<estatura>")
def Porestatura(estatura):
  resultados=base[base["estatura"]==estatura]
  resultados=float(resultados)
  return resultados


if __name__=="__main__":
  app.run()
