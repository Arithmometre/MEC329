# FICHIER     : dcl_membrure_AIJB.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-04
# DESCRIPTION : Calcul des réactions du DCL de la membrure AIJB.

import math
import numpy as np

from constantes_projet_mec329 import *
import dcl_plateforme as dclpla
import dcl_ensemble as dclens

# Forces
f_B = -abs(dclpla.reaction_B)
x_FBA = X_BA
y_FBA = Y_BA
f_A = abs(dclens.reaction_A)

W_1 = -abs(POID_LIN_MEMBRURE * LONGUEUR_MEMBRURE)
x_W1A = X_IA

W_verin = -abs(POID_VERIN / 2)
x_W_verin_A = X_JA

x_JA = X_JA
y_JA = Y_JA

# Somme des forces connue scalaire
somme_forces_con_y = f_B + f_A + W_1 + W_verin
somme_forces_con_x = 0

# Somme des moments connue scalaire
somme_moment_con_A = (f_B * x_FBA) - (W_1 * x_W1A) - (W_verin * x_W_verin_A)
somme_moment_con_B = (f_A * x_FBA) + (W_1 * x_W1A) + (W_verin * x_W_verin_A)


# Systeme d'equations somme des forces et moments
# Somme des forces en x
coef_f_I_x = 1 #math.cos(THETA)
coef_f_J_x = 1 #math.cos(THETA_VERIN)
somme_forces_x = [coef_f_I_x, 0, coef_f_J_x, 0 ]

# Somme des forces en y
coef_f_I_y = 1 #math.sin(THETA)
coef_f_J_y = 1 #math.sin(THETA_VERIN)
somme_forces_y = [0, coef_f_I_y, 0, coef_f_J_y]

# Moment autour de A
coef_moment_A_x = -math.cos(THETA_VERIN) * Y_JA - math.cos(THETA) * Y_IA
coef_moment_A_y = -math.sin(THETA_VERIN) * X_JA - math.sin(THETA) * X_IA
somme_moment_A = [0, 0, coef_moment_A_x, coef_moment_A_y ]

# Moment autour de B
coef_moment_B_x = math.cos(THETA_VERIN) * (Y_BA - Y_JA) + math.cos(THETA) * Y_IA
coef_moment_B_y = math.sin(THETA_VERIN) * (X_BA - X_JA) + math.sin(THETA) * X_IA
somme_moment_B = [0, 0, coef_moment_B_x, coef_moment_B_y ]

c1 = -somme_forces_con_x
c2 = -somme_forces_con_y
c3 = -somme_moment_con_A
c4 = -somme_moment_con_B

A = np.array([somme_forces_x, somme_forces_y, somme_moment_A, somme_moment_B])
B = np.array([c1, c2, c3, c4])
X = np.linalg.solve(A,B)

# Reactions
reaction_I_x = X[0]
reaction_I_y = X[1]
reaction_J_x = X[2]
reaction_J_y = X[3]