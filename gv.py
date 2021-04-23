import pygame, circuitMatrix

pygame.init()

width = 105
height = 60
sizeFactor = 13
isRunning = False
frame = False
showGrid = True
showFPS = False
ambientSprk = True
boardColor = (0, 0, 0)
transColor = (127, 127, 127)
andColor = (127, 127, 230)
notColor = (127, 230, 127)
sprkColor = (230, 230, 0)
batteColor = (0, 128, 128)
deletColor = (230, 0, 0)
size = (width * sizeFactor, height * sizeFactor)
screen = pygame.display.set_mode(size)
Game = circuitMatrix.Matrix()
GameF = circuitMatrix.Matrix()
Game.build(width, height)
GameF.build(width, height)
pygame.display.set_caption("The Circuit Toy", "TCT")
icon = pygame.image.load("TheCircuitToy.jpg")
pygame.display.set_icon(icon)
font = pygame.font.Font("pixelated.ttf", 17)
#font = pygame.font.SysFont("comicsansms", 17)