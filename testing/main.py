def simulate_robot(input_instructions_list):
    input_instructions = []
    with open(input_instructions_list, 'r') as file:
        for line in file:
            input_instructions.append(line)
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
        nonlocal Map
        for i in size:
            for j in size:
                Map[i][j] = "--"

    def printMap():
        nonlocal Map
        print("División------------------------")
        Map[y][x] = "XX"
        for i in size:
            print(Map[i])

    def Turn(Angle):
        nonlocal rotationAngle
        nonlocal direction
        nonlocal Xdir
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
        nonlocal x
        nonlocal y
        nonlocal size
        nonlocal direction
        nonlocal Xdir
        nonlocal Continue
        if Xdir == True:
            if (x + (direction * steps)) > 9:
                print("Invalid Operation, out of range")
                Continue = False
                return
            elif (direction == -1 and (x + (direction * steps)) < 0):
                print("Invalid Operation, out of range")
                Continue = False
                return
            else:
                x = x + (direction * steps)
        else:
            if (y + (direction * steps)) > 9:  
                print("Invalid Operation, out of range")
                Continue = False
                return
            elif (direction == -1 and (y + (direction * steps)) < 0):
                print("Invalid Operation, out of range")
                Continue = False
                return
            else:
                y = y + (direction * steps)
        cleanMap()
        printMap()

    def executeActions(input_instructions):
        for line in input_instructions:
            if (Continue):
                try:
                    action, value = line.strip().split(', ')
                    if action == 'MOV':
                        Mov(int(value))
                    elif action == 'TURN':
                        Turn(int(value))
                    else:
                        print("Invalid Operation, unrecognized")
                except ValueError:
                    print("Invalid Operation, not enough values")

    printMap()
    executeActions(input_instructions)

def main():
    simulate_robot("input.txt")

if __name__ == "__main__":
    main()