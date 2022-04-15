# FICHIER     : dcl_ensemble.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-04
# DESCRIPTION : Calcul des réactions du DCL de l'ensemble de la structure.

import math
import numpy as np

from constantes_projet_mec329 import *
import dcl_plateforme as dclpla

# Forces
f_B = -dclpla.reaction_B
f_D = -dclpla.reaction_D

# Poid des membrures (a param.)
W_1 = -POID_LIN_MEMBRURE * LONGUEUR_MEMBRURE * 2
x_W1A = X_IA
# Poid du verin (a param.)
W_2 = -POID_VERIN
x_W2A = ((X_KA - X_JA) / 2) + X_JA

# Somme des forces scalaire
somme_forces = f_B + f_D + W_1 + W_2

# Somme des moments scalaire
somme_moment_D = f_B * X_BA + W_1 * x_W1A + W_2 * x_W2A

# Systeme d'equations somme des forces et moments
x1 = 1
y1 = 1

x2 = 0
y2 = dclpla.longueur_segment_BD

c1 = -somme_forces
c2 = -somme_moment_D

A = np.array([[x1, y1], [x2, y2]])
B = np.array([c1, c2])
X = np.linalg.solve(A,B)

# Reactions
reaction_C = X[1]
reaction_A = X[0]