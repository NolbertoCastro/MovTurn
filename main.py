import sys

x = 0
y = 0

Xdir = True
Continue = True

rotationAngle = 0

Map = []

direction = 1

size = range(10)

for i in size:
  newLine = []
  for j in size:
    newLine.append("--")
  Map.append(newLine)
  newLine = []

def cleanMap():
  global Map
  for i in size:
    for j in size:
      Map[i][j] = "--"

def printMap():
  global Map
  print("División------------------------")
  Map[y][x] = "XX"
  for i in size:
    print(Map[i])

def Turn(Angle):
  global rotationAngle
  global direction
  global Xdir
  if rotationAngle + Angle == 360:
    rotationAngle = 0
  elif rotationAngle + Angle > 360:
    rotationAngle = (rotationAngle + Angle) - 360
  else:
    rotationAngle = rotationAngle + Angle

  match rotationAngle:
    case 0:
        direction = 1
        Xdir = True

    case 90:
        direction = -1
        Xdir = False
    case 180:
        direction = -1
        Xdir = True
    
    case 270:
        direction = 1
        Xdir = False

def Mov(steps):
  global x
  global y
  global size
  global direction
  global Xdir
  global Continue
  if Xdir == True:
    if (x + (direction * steps)) > 9:
      sys.exit("Invalid Operation, out of range")
    else:
      x = x + (direction * steps)
  else:
    if (y + (direction * steps)) > 9:  
      sys.exit("Invalid Operation, out of range")
    else:
      y = y + (direction * steps)
  cleanMap()
  printMap()

def executeActionsFromFile(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            action, value = line.strip().split(', ')
            if action == 'MOV':
                Mov(int(value))
            elif action == 'TURN':
                Turn(int(value))

def main():
  printMap()
  executeActionsFromFile('instructions.asm')
main()