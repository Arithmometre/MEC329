# FICHIER     : dcl_plateforme.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-03
# DESCRIPTION : Calcul des réactions du DCL de la plateforme.

import math
import numpy as np

from constantes_projet_mec329 import *

# Positions des points, segments, etc.
longueur_segment_DE = LONGUEUR_PLATEFORME - X_D
longueur_segment_BD = X_D - X_B
longueur_segment_OB = LONGUEUR_PLATEFORME - longueur_segment_DE - longueur_segment_BD

# Forces p1, p2, et p3
p3 = (longueur_segment_DE / LONGUEUR_PLATEFORME) * GRAND_P
#vecteur_p3 = [p3, 0]
r_p3D = longueur_segment_DE / 2
moment_p3D = p3 * r_p3D

p2 = (longueur_segment_BD / LONGUEUR_PLATEFORME) * GRAND_P
#vecteur_p2 = [p2, 0]
r_p2D = longueur_segment_BD / 2
moment_p2D = -p2 * r_p2D

p1 = (longueur_segment_OB / LONGUEUR_PLATEFORME) * GRAND_P
#vecteur_p1 = [p1, 0]
r_p1D = longueur_segment_OB / 2 + longueur_segment_BD
moment_p1D = -p1 * r_p1D

# Somme des moments scalaire
somme_moment_D = moment_p1D + moment_p2D + moment_p3D

# Systeme d'equations somme des forces et moments

x1 = 1
y1 = 1

x2 = 0
y2 = -longueur_segment_BD

c1 = -GRAND_P
c2 = -somme_moment_D

A = np.array([[x1, y1], [x2, y2]])
B = np.array([c1, c2])
X = np.linalg.solve(A,B)

# Reactions
reaction_B = X[1]
reaction_D = X[0]