# FICHIER     : constantes_projet_mec329.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-03
# DESCRIPTION : Liste de constantes pour le projets de MEC329.

import math

# 2 - Alex, 3 - Ariane, 1 - Charles, 4 - Gabriel
nom = 4
# 1 - haut, 0 - bas
position = 0

#------- DONNÉES DU PROBLÈME --------#
GRAND_P = -1500
H_MAX = 5
H_MIN = 1.2
LONGUEUR_PLATEFORME = 7
RHO = 7850
POID_GOUPILLE = RHO * (3.5 / 2) * math.pi * (2e-3)**2

#------- PROFILÉ -------#
AIRE_MEMBRURE = 1990e-6
POID_LIN_MEMBRURE = RHO * AIRE_MEMBRURE
POID_VERIN = 10*9.81
IX = 2.68e-6
Y_MAX = 101.6e-3 / 2

"""
AIRE_MEMBRURE = 418e-6
POID_LIN_MEMBRURE = RHO * AIRE_MEMBRURE
#verin temp. HTG4036-ORB, masse: 74lbs --> 34kg ---> poid = 333 newtons
POID_VERIN = 10*9.81
IX = 0.122e-6
Y_MAX = 25.4e-3 / 2
"""

#------- DONNÉES CHOISIE ------------#
if nom == 2 :
	NOM_T = "Alex"
	HAUTEUR_LIT = 0.0
	LONGUEUR_MEMBRURE = 7
	DISTANCE_IK = 1
	DISTANCE_IJ = 2.2
	X_D = 6.84

elif nom == 3 :
	NOM_T = "Ariane"
	HAUTEUR_LIT = 1.2 - 0.8065
	LONGUEUR_MEMBRURE = 6.5
	DISTANCE_IK = 0.4875
	DISTANCE_IJ = 2.4375
	X_D = 6.75

elif nom == 1 :
	NOM_T = "Charles"
	HAUTEUR_LIT = 0.3
	LONGUEUR_MEMBRURE = 6.0
	DISTANCE_IK = 1
	DISTANCE_IJ = 2.5
	X_D = 6

elif nom == 4 :
	NOM_T = "Gabriel"
	HAUTEUR_LIT = 0.6
	LONGUEUR_MEMBRURE = 6
	DISTANCE_IK = 1
	DISTANCE_IJ = 2.3418402161054
	X_D = 6.5

#------- DONNÉES CALCULÉES ----------#

#-------CHOIX DE LA POSITION -------#
if position == 1:
	DISTANCE = H_MAX - HAUTEUR_LIT
elif position == 0:
	DISTANCE = H_MIN - HAUTEUR_LIT

#THETA = math.pi / 2 + math.asin(DISTANCE / LONGUEUR_MEMBRURE)
THETA = math.asin(DISTANCE / LONGUEUR_MEMBRURE)
PHI = (math.pi / 2) - THETA
#THETA_PRIME = THETA

X_A = X_D
X_B = X_A - LONGUEUR_MEMBRURE * math.cos(THETA)

DISTANCE_BD = X_D - X_B

#-------DISTANCE DES POINTS PAR RAPPORT À A -------#
X_BA = abs(LONGUEUR_MEMBRURE * math.cos(THETA))
Y_BA = abs(LONGUEUR_MEMBRURE * math.sin(THETA))

X_DA = 0
Y_DA = abs(LONGUEUR_MEMBRURE * math.sin(THETA))

X_IA = abs((LONGUEUR_MEMBRURE / 2) * math.cos(THETA))
Y_IA = abs((LONGUEUR_MEMBRURE / 2) * math.sin(THETA))

X_JA = abs(((LONGUEUR_MEMBRURE / 2) - DISTANCE_IJ) * math.cos(THETA))
Y_JA = abs(((LONGUEUR_MEMBRURE / 2) - DISTANCE_IJ) * math.sin(THETA))

X_KA = abs(DISTANCE_BD - ((LONGUEUR_MEMBRURE / 2) + DISTANCE_IK) * math.cos(THETA))
Y_KA = abs(((LONGUEUR_MEMBRURE / 2) + DISTANCE_IK) * math.sin(THETA))

LONGUEUR_VERIN = abs(math.sqrt((DISTANCE_IK ** 2) + (DISTANCE_IJ ** 2)  - (2 * DISTANCE_IJ * DISTANCE_IK * math.cos(2 * THETA))))

THETA_VERIN = math.asin((Y_KA - Y_JA) / LONGUEUR_VERIN)
THETA_VERIN_PRIME = THETA_VERIN - THETA