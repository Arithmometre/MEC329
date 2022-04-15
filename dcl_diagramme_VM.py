# FICHIER     : dcl_diagramme_VM.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-14
# DESCRIPTION :

import math
import numpy as np

from constantes_projet_mec329 import *
import dcl_plateforme as dclpla
import dcl_ensemble as dclens
import dcl_membrure_AIJB as AIJB

if AIJB.reaction_I_x < 0 :
	flip = 1
else :
	flip = -1

f_A = abs(dclens.reaction_A)
f_B = abs(dclpla.reaction_B)
f_C = abs(dclens.reaction_C)
f_D = abs(dclpla.reaction_D)

f_I = math.sqrt(AIJB.reaction_I_x**2 + AIJB.reaction_I_y**2)
f_I_x = abs(AIJB.reaction_I_x) * flip
f_I_y = abs(AIJB.reaction_I_y) * flip

f_J = math.sqrt(AIJB.reaction_J_x**2 + AIJB.reaction_J_y**2)
f_J_x = abs(AIJB.reaction_J_x) * flip
f_J_y = abs(AIJB.reaction_J_y) * flip

f_K = math.sqrt(AIJB.reaction_J_x**2 + AIJB.reaction_J_y**2)
W_1 = abs(POID_LIN_MEMBRURE * LONGUEUR_MEMBRURE)

f_A_x_prime = f_A * math.cos(math.pi / 2 + THETA)
f_A_y_prime = f_A * math.sin(math.pi / 2 + THETA)

f_B_x_prime = f_B * math.cos(-PHI)
f_B_y_prime = f_B * math.sin(-PHI)

f_C_x_prime = f_C * math.cos(PHI)
f_C_y_prime = f_C * math.sin(PHI)

f_D_x_prime = f_D * math.cos(math.pi + PHI)
f_D_y_prime = f_D * math.sin(math.pi + PHI)

f_W1_x_prime = W_1 * math.cos(-PHI)
f_W1_y_prime = W_1 * math.sin(-PHI)

f_W2_x_prime = W_1 * math.cos(math.pi + PHI)
f_W2_y_prime = W_1 * math.sin(math.pi + PHI)

f_Verrin1_x_prime = POID_VERIN * math.cos(-PHI)
f_Verrin1_y_prime = POID_VERIN * math.sin(-PHI)

f_Verrin2_x_prime = POID_VERIN * math.cos(math.pi + PHI)
f_Verrin2_y_prime = POID_VERIN * math.sin(math.pi + PHI)

f_I1_x_prime = f_I_x * math.cos(math.pi + THETA) + f_I_y * math.cos(math.pi / 2 + THETA)
f_I1_y_prime = f_I_x * math.sin(math.pi + THETA) + f_I_y * math.sin(math.pi / 2 + THETA)

f_I2_x_prime = f_I_x * math.cos(-THETA) + f_I_y * math.cos(math.pi + PHI)
f_I2_y_prime = f_I_x * math.sin(-THETA) + f_I_y * math.sin(math.pi + PHI)

f_J_x_prime = f_J_x * math.cos(THETA) + (f_J_y - POID_VERIN / 2) * math.cos(-PHI)
f_J_y_prime = f_J_x * math.sin(THETA) + (f_J_y - POID_VERIN / 2) * math.sin(-PHI)

f_K_x_prime = f_J_x * math.cos(math.pi / 2 + PHI) + (f_J_y + POID_VERIN / 2) * math.cos(PHI)
f_K_y_prime = f_J_x * math.sin(math.pi / 2 + PHI) + (f_J_y + POID_VERIN / 2) * math.sin(PHI)

f_I1_prime = math.sqrt(f_I1_x_prime**2 + f_I1_y_prime**2)
f_I2_prime = math.sqrt(f_I2_x_prime**2 + f_I2_y_prime**2)

effort_V1_B = f_B_y_prime
effort_V1_I1 = effort_V1_B + (f_W1_y_prime / 2) + f_I1_y_prime
effort_V1_J = effort_V1_I1 + f_J_y_prime + ((f_W1_y_prime / LONGUEUR_MEMBRURE) * DISTANCE_IJ)
effort_V1_A = effort_V1_J + ((f_W1_y_prime / LONGUEUR_MEMBRURE) * (3 - DISTANCE_IJ)) + f_A_y_prime

moment_I1 = (effort_V1_B + (f_W1_y_prime / 2)) * (LONGUEUR_MEMBRURE / 2) - ((f_W1_y_prime / 2) * (LONGUEUR_MEMBRURE / 2) / 2)
moment_J1 = moment_I1 + (effort_V1_I1 * DISTANCE_IJ) + (((f_W1_y_prime / LONGUEUR_MEMBRURE) * DISTANCE_IJ) * DISTANCE_IJ) / 2

liste_des_V1 = [effort_V1_B, effort_V1_I1, effort_V1_J, effort_V1_A]
liste_des_M1 = [moment_I1, moment_J1]

moment_MAX_AIJB = max(liste_des_M1, key=abs)

"""
print("F_A_x_prime:", round(f_A_x_prime, 2))
#print("F_A_y_prime:", round(f_A_y_prime, 2))
print("F_B_x_prime:", round(f_B_x_prime, 2))
#print("F_B_y_prime:", round(f_B_y_prime, 2))
print("F_W1_x_prime:", round(f_W1_x_prime, 2))
#print("F_W_y_prime:", round(f_W_y_prime, 2))
print("F_W2_x_prime:", round(f_W2_x_prime, 2))

print("F_C_x_prime:", round(f_C_x_prime, 2))
print("F_D_x_prime:", round(f_D_x_prime, 2))
print("F_K_x_prime:", round(f_K_x_prime, 2))

print("F_I1_x_prime:", round(f_I1_x_prime, 2))
#print("F_I1_y_prime:", round(f_I1_y_prime, 2))
print("F_I2_x_prime:", round(f_I2_x_prime, 2))
#print("F_I2_y_prime:", round(f_I2_y_prime, 2))

print("F_J_x_prime:", round(f_J_x_prime, 2))
#print("F_J_y_prime:", round(f_J_y_prime, 2))

print("Somme AIJB y:", round(f_J_y_prime + f_I1_y_prime + f_A_y_prime + f_B_y_prime + f_W1_y_prime + f_Verrin1_y_prime, 2))
print("Somme AIJB x:", round(f_J_x_prime + f_I1_x_prime + f_A_x_prime + f_B_x_prime + f_W1_x_prime + f_Verrin1_x_prime, 2))
print("Somme CIKD y:", round(f_C_y_prime + f_I2_y_prime + f_K_y_prime + f_D_y_prime + f_W2_y_prime + f_Verrin2_y_prime, 2))
print("Somme CIKD x:", round(f_C_x_prime + f_I2_x_prime + f_K_x_prime + f_D_x_prime + f_W2_x_prime + f_Verrin2_x_prime, 2))
print("V_B:",round(effort_V1_B, 2))
print("V_I:",round(effort_V1_I1, 2))
print("V_J:",round(effort_V1_J, 2))
print("V_A:",round(effort_V1_A, 2))
print("M_I:",round(moment_I1, 2))
print("M_J:",round(moment_J1, 2))
print("moment_MAX_AIJB:", round(moment_MAX_AIJB, 2))
#print("moment_MAX_CKID:", round(moment_MAX_CKID, 2))
"""
