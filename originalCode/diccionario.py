import random

categorias_disponibles = {
      "animales": ["perro","gato","pez","rinoceronte","pajaro","jirafa"],
      "frutas"  : ["mango","pera","manzana","platano","fresa","uva","granada"],
      "colores" : ["rojo","azul","verde","amarillo","morado","marron","cafe"],
      "profesiones": ["ingeniero","maestro","arquitecto","medico","enfermero","doctor"],
      "deportes": ["futbol","tenis","baloncesto","natacion"],
      "transporte": ["coche","avion","bicicleta","tren","metro","metrobus"],
      "emociones": ["enojo","felicidad","sorpresa","tristeza","pereza"]
  }
  
opcion_categoria = 0
palabra_elegida = ""




def pantalla_inicio(index_elegido):
  screen.drawText("¡Bienvenido  al juego del ahorcado!",0,75,20, "#FFF")
  screen.drawText("Tenemos las siguientes categorias:",0,60,15, "#FFF")
  global diccionario
  global palabra_elegida
  
  x = 38
  y = 0
  tam = 15
  color = "#FF0"
  colorElegido = "#F0F"
      
  
  for index, categoria in enumerate(categorias_disponibles):
    if index_elegido == index :
      screen.drawText(categoria.capitalize(), y, x, tam, colorElegido)
      if  checkInput(keyboard.press, "ENTER") :
        palabra_elegida = random.choice(categorias_disponibles[categoria])
        return "juego", palabra_elegida
    else:
      screen.drawText(categoria.capitalize(), y, x, tam, color)
    x -= 15

  
  return "inicio",""
  
  
def eligeCategoria():
  global opcion_categoria
  if checkInput(keyboard.press,"DOWN"):
    opcion_categoria+=1
    if opcion_categoria>len(categorias_disponibles):
      opcion_categoria = 0
        
  if checkInput(keyboard.press,"UP"):
    opcion_categoria-=1
    if opcion_categoria<0:
      opcion_categoria=len(categorias_disponibles)-1
