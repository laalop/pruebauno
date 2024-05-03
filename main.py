import pandas as pd
from flask import Flask

app=Flask(__name__)

base=pd.read_excel("perros.xlsx")

@app.route("/")
def Principal():
  return "Esta es una API que te muetra el nombre de perros, raza y estatura"

@app.route("/conumero/<Numero>")
def PorNumero(Numero):
  Numero=int(Numero)
  fila=base[base["Numero"]==Numero]
  respuesta=f"El Perro {Numero} es {fila.loc[:,'nombre']}"
  return respuesta

if __name__=="__main__":
  app:run()
