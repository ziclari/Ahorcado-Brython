
estado = "inicio"

def init():
  global estado
  estado = "inicio"
  

def update():
  global estado
  
  if estado == "inicio":
    eligeCategoria()
  if estado == "juego":
    #Solicita la letra
    adivinar =  captura()
    if adivinar!="":
      verificarLetra(adivinar)
    
    global causaFin
    causaFin = finDeJuego()
    if  causaFin != "":
      estado = "fin"
      
  if estado=="fin":
    estado=manejarFin()
    #  estado = "inicio"



def draw():
  screen.clear()
  #dibuja el inicio del juego
  global estado
  global palabra_elegida,palabra_oculta
  
  if estado == "inicio":
    global opcion_categoria
    estado,palabra_elegida = pantalla_inicio(opcion_categoria)
    if palabra_elegida != "":
      palabra_oculta = ["_"]*len(palabra_elegida)
      
  if estado == "juego":
    dibujaTablero()
  
  if estado == "fin":
    global causaFin
    dibujaFin(causaFin)
    
    
    
  #leeletra()
  
  #
  pass