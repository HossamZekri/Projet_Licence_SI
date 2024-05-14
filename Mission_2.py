import robohat, select, sys

robohat.init()
# Fonction pour récupurer les informations disponibles 
# dans notre cas on utilisera la touche 'r' pour faire marcher le robot.
def is_data():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])

# ce flag sert à arrêter le robot dans le cas où le capteur ultrason
# détecte un objet à une distance définie
# pour commencer le flag sera à l'état haut 
# le robot attend que l'utlisateur appuie sur la touche r
flag = 1
vitesse_rotation = 80 # vitesse à laquelle notre robot tourne à gauche ou à droite
# boucle de fonctionnement 
troisieme_vitesse = 100
deuxieme_vitesse = 50 
premiere_vitesse = 30
while True :

	wallLeft = robohat.irLeft() # variable où on stocke l'état de notre IRSensor gauche
	wallRight = robohat.irRight() # variable où on stocke l'état de notre IRSensor droite
	dist = robohat.getDistance() # variable où on stocke la distance calculée par notre UltraSonic sensor
	
	# print ("Distance: ", int(dist))
	
	if wallLeft == True and flag == 0: # premier cas de figure où notre robot détecte un obstacle à gauche
		robohat.spinRight(vitesse_rotation) # tourne à droite
		flag = 0

	if wallRight == True and flag == 0 : # deuxième cas de figure où notre robot détecte un obstacle à droite
		robohat.spinLeft(vitesse_rotation) # tourne à gauche

	if wallLeft == False and wallRight == False and dist > 20 and flag == 0: # troisieme cas de figure où notre robot ne détecte pas d'obstacle à sa gauche ni à sa droite et la distance calculée par US sensor est plus grand que 20 cm 
		robohat.forward(troisieme_vitesse)
		flag = 0	

	if wallLeft == False and wallRight == False and dist >10 and dist < 20 and flag == 0: # quatrieme cas de figure où notre robot ne détecte pas d'obstacle à sa gauche ni à sa droite et la distance calculée par US sensor est plus grand que 10 cm et plus petit que 20 cm
		robohat.forward(deuxieme_vitesse)
		flag = 0

	if wallLeft == False and wallRight == False and dist < 10 and flag == 0:# cinquieme cas de figure où notre robot ne détecte pas d'obstacle à sa gauche ni à sa droite et la distance calculée par US sensor est plus petit que 10 cm 
		robohat.forward(premiere_vitesse)
		flag = 0

	if dist < 6 :  # dernier cas de figure où notre robot détecte un obstacle à moins de 6 cm 
		robohat.stop() # arrêt total
		flag = 1 

	if is_data() :
		input = sys.stdin.read(1)
		if input == 'r' :
			print("Touche R pressée")
			flag = 0
			input = 't'
	
