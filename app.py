from flask import Flask 
 
app=Flask(__name__) 
 
@app.route("/") 
def inicio(): 
    return "<h1>Pagina de inicio" 
 
@app.route("/acerca") 
def acerca(): 
    return "<h1>Informacion sobre nosotros" 
 
@app.route("/contacto") 
def contacto(): 
    return "<h1>Pagina de contacto" 
 
@app.route("/info") 
def informacion(): 
    return "<h1>Pagina de informacion"

@app.route("/servicios")
def servicios():
    return "<h1>Pagina de servicios"

@app.route("/galeria")
def galeria():
    return "<h1>Pagina de galeria"
 
if __name__=="__main__": 
    app.run(debug=True)