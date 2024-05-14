import robohat
import time

speed = 100  # Vitesse de base du robot
turnSpeed = 100 # vitesse de rotation
reverseSpeed = 80 # vitesse de marche arriière
robohat.init()  # Initialisation de RoboHat

black = False
white = True

# Boucle principale pour le suivi de ligne
go = input()
while True and go == 'g': 
    # Si les deux capteurs détectent le noir (ligne), avancer
	if robohat.irLeftLine() == black and robohat.irRightLine() == black:
		robohat.forward(speed)
    # Si les deux capteurs détectent le blanc (hors ligne), reculer légèrement
	if robohat.irLeftLine() == white and robohat.irRightLine() == white:
		robohat.reverse(reverseSpeed)
    # Si seul le capteur gauche détecte blanc, tourner à gauche
	if robohat.irLeftLine() == black and robohat.irRightLine() == white:
		robohat.spinLeft(turnSpeed)
    # Si seul le capteur droit détecte blanc, tourner à droite
	if robohat.irLeftLine() == white and robohat.irRightLine() == black:
		robohat.spinRight(turnSpeed)

