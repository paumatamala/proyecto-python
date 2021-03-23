from flask import Flask
app = Flask(__name__)

# esto es un comentario
def suma(a,b):
  resultado = a+b
  return a+b+resultado

# este es el endpoint
@app.route("/")
def hello():
    res = suma(3,2)
    #Comentario de lo que quieras
    #Otro Comentario
    return "Hello World! %s" % (res)

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000)
