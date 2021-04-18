# Credit to The Powder Toy for inspiring me
import pygame, math, gv, sys

pygame.init()
clock = pygame.time.Clock()

gv.Game.NodesData = gv.GameF.NodesData

# key0 = board, key1 = trans, key2 = sprk, key3 = battery, key4 = andGate, key5 = andsprk, key6 = notGate, key7 = notsprk, key8 = backtrans, key9 = backtrans2
def check(node):
    if node.key != 0 and node.key != 3:
        neighbors = []
        neighbors.append(gv.Game.get(node.Xm - 1, node.Ym + 1).key)
        neighbors.append(gv.Game.get(node.Xm, node.Ym + 1).key)
        neighbors.append(gv.Game.get(node.Xm + 1, node.Ym + 1).key)
        neighbors.append(gv.Game.get(node.Xm - 1, node.Ym).key)
        neighbors.append(gv.Game.get(node.Xm + 1, node.Ym).key)
        neighbors.append(gv.Game.get(node.Xm - 1, node.Ym - 1).key)
        neighbors.append(gv.Game.get(node.Xm, node.Ym - 1).key)
        neighbors.append(gv.Game.get(node.Xm + 1, node.Ym - 1).key)

        if node.key == 8:
            node.key = 1

        if node.key == 9:
            node.key = 8

        if node.key == 2 or node.key == 5 or node.key == 7:
            if 2 not in neighbors or 3 not in neighbors or 5 not in neighbors or 7 not in neighbors:
                if node.key != 2:
                    node.key -= 1

                else:
                    node.key = 9

        if node.key == 1:
            if 2 in neighbors or 3 in neighbors or 5 in neighbors or 7 in neighbors:
                node.key = 2

        if node.key == 4 or node.key == 5:
            check = 0
            for neighbor in neighbors:
                if neighbor == 2 or neighbor == 3 or neighbor == 5 or neighbor == 7 or neighbor == 8 or neighbor == 9:
                    check += 1

            if check >= 2:
                node.key = 5

            else:
                node.key = 4

    else:
        return node

    return node

class CircuitGame:
    def __init__(self):
        pass

    def update(self):
        gv.Game.transmit(gv.GameF)
        for node in gv.GameF.Nodes:
            node = check(node)
        gv.Game.transmit(gv.GameF)
        gv.frame = False

    def keyUpdate(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    (Mx, My) = pygame.mouse.get_pos()
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    gv.GameF.get(Nx, Ny).key = 1

                if event.button == 2:
                    (Mx, My) = pygame.mouse.get_pos()
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    gv.GameF.get(Nx, Ny).key = 0

                if event.button == 3:
                    (Mx, My) = pygame.mouse.get_pos()
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    gv.GameF.get(Nx, Ny).key = 3

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if gv.isRunning:
                        gv.isRunning = False

                    else:
                        gv.isRunning = True

                if event.key == pygame.K_f:
                    gv.frame = True

                if event.key == pygame.K_c:
                    for node in gv.GameF.Nodes:
                        node.key = 0

                if event.key == pygame.K_a:
                    (Mx, My) = pygame.mouse.get_pos()
                    Nx, Ny = math.ceil(Mx / gv.sizeFactor), math.ceil(My / gv.sizeFactor)
                    gv.GameF.get(Nx, Ny).key = 4

                if event.key == pygame.K_g:
                    if gv.showGrid:
                        gv.showGrid = False

                    else:
                        gv.showGrid = True

                if event.key == pygame.K_s:
                    gv.GameF.save("CircuitSave")
                    gv.GameF.save("CircuitSaveBackup")

                if event.key == pygame.K_l:
                    try:
                        gv.GameF = gv.GameF.load("CircuitSave")

                    except:
                        gv.GameF = gv.GameF.load("CircuitSaveBackup")
                    gv.Game.transmit(gv.GameF)
                    gv.Game.NodesData = gv.GameF.NodesData
                    gv.Game.sizeX, gv.Game.sizeY, gv.Game.size = gv.GameF.sizeX, gv.GameF.sizeY, gv.GameF.size
                    gv.width = gv.GameF.sizeX
                    gv.height = gv.GameF.sizeY

            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()

    def draw(self):
        for node in gv.GameF.Nodes:
            if gv.GameF.get(node.Xm, node.Ym).key == 1:
                pygame.draw.rect(gv.screen, gv.transColor, ((node.Xm - 1) * gv.sizeFactor, (node.Ym - 1) * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

            elif gv.GameF.get(node.Xm, node.Ym).key == 2 or gv.GameF.get(node.Xm, node.Ym).key == 5 or gv.GameF.get(node.Xm, node.Ym).key == 7 or gv.GameF.get(node.Xm, node.Ym).key == 8 or gv.GameF.get(node.Xm, node.Ym).key == 9:
                pygame.draw.rect(gv.screen, gv.sprkColor, ((node.Xm - 1) * gv.sizeFactor, (node.Ym - 1) * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

            elif gv.GameF.get(node.Xm, node.Ym).key == 3:
                pygame.draw.rect(gv.screen, gv.batteColor, ((node.Xm - 1) * gv.sizeFactor, (node.Ym - 1) * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

            elif gv.GameF.get(node.Xm, node.Ym).key == 4:
                pygame.draw.rect(gv.screen, gv.andColor, ((node.Xm - 1) * gv.sizeFactor, (node.Ym - 1) * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

            elif gv.GameF.get(node.Xm, node.Ym).key == 6:
                pygame.draw.rect(gv.screen, gv.notColor, ((node.Xm - 1) * gv.sizeFactor, (node.Ym - 1) * gv.sizeFactor, gv.sizeFactor, gv.sizeFactor))

        if gv.showGrid:
            for column in range(1, gv.width):
                pygame.draw.line(gv.screen, "dark green", (column * gv.sizeFactor, 0), (column * gv.sizeFactor, gv.height * gv.sizeFactor))

            for row in range(1, gv.height):
                pygame.draw.line(gv.screen, "dark green", (0, row * gv.sizeFactor), (gv.width * gv.sizeFactor, row * gv.sizeFactor))
        #fps
def main():
    Circuit = CircuitGame()
    notNew = True
    try:
        gv.GameF = gv.GameF.load("CircuitSave")

    except:
        try:
            gv.GameF = gv.GameF.load("CircuitSaveBackup")
        except:
            notNew = False

    if notNew:
        gv.Game.transmit(gv.GameF)
        gv.Game.NodesData = gv.GameF.NodesData
        gv.Game.sizeX, gv.Game.sizeY, gv.Game.size = gv.GameF.sizeX, gv.GameF.sizeY, gv.GameF.size
        gv.width = gv.GameF.sizeX
        gv.height = gv.GameF.sizeY

    while True:
        clock.tick(70)
        gv.screen.fill(gv.boardColor)
        if gv.isRunning or gv.frame:
            Circuit.update()

        Circuit.draw()
        Circuit.keyUpdate()
        pygame.display.flip()

if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
