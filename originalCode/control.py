def captura():
  for letra in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    if checkInput(keyboard.press,letra):
      return letra.lower()
  return ""

def checkInput(obj,val):
  if hasattr(obj,val):
    return obj[val] != 0
  return 0
def mouseEncima(x,y,tamano):
  return abs(mouse.x - x) <= tamano/2 and abs(mouse.y - y) <= tamano/2

def huboClick(x,y,tamano):
  if mouseEncima(x,y,tamano):
    if mouse.press:
      return True
  return False