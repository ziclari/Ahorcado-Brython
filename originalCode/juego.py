palabra_oculta = ["_"]*len(palabra_elegida)
dibujo = ["a0","a1","a2","a3","a4","a5","a6"]
oportunidades = len(dibujo)-1
letrasErradas = []
causaFin = ""

def dibujaTablero():
  #Muestra el tablero
    screen.clear()
    global letrasErradas,palabra_oculta
    screen.drawSprite(dibujo[len(letrasErradas)],0,45,100)
    screen.drawText(' '.join(palabra_oculta),0,-30,20, "#FFF")
    screen.drawText(', '.join(letrasErradas),0,-65,20, "#FFF")

def verificarLetra(adivinar):
  global palabra_oculta, palabra_elegida, oportunidades
  
  if adivinar in palabra_elegida:
    for i, val in enumerate(palabra_oculta):
        if adivinar == palabra_elegida[i]:
          palabra_oculta[i]=adivinar
  else:
    letrasErradas.append(adivinar)
    oportunidades-=1

def finDeJuego():
  global oportunidades,palabra_oculta, palabra_elegida,letras_erradas, dibujo
  if oportunidades==0:
      oportunidades = len(dibujo)-1
      letrasErradas.clear()
      return "Perdio"
  if "".join(palabra_oculta) == palabra_elegida:
      screen.clear()
      oportunidades = len(dibujo)-1
      letrasErradas.clear()
      return "Gano"
  else:
     return ""

def dibujaFin(causa):
  global palabra_oculta, letras_erradas, dibujo
  if causa=="Perdio":
      screen.drawSprite(dibujo[len(letrasErradas)-1],0,45,100)
      screen.drawText("Perdiste el juego :(",0,-30,20, "#FFF")
      screen.drawSprite("regresar",0,-65,50)

  if causa == "Gano":
      screen.drawText(' '.join(palabra_oculta),0,35,20, "#FFF")
      screen.drawText("Ganaste :D",0,0,20, "#FFF")
      screen.drawSprite("regresar",0,-50,50)

def manejarFin():
  x = 0
  y = -50
  # Tamaño del cuadrado
  tamano = 50
  
  # Comprobar si el clic del ratón está dentro del cuadrado
  if huboClick(x,y,tamano):
    return "inicio"
  
  return "fin"
  