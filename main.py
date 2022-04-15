# FICHIER     : main.py
# PAR         : Gabriel Rondeau-Bouvrette
# DATE        : 2022-04-03
# DESCRIPTION : programme principal

import math
import numpy as np

from constantes_projet_mec329 import *
import dcl_plateforme as dclpla
import dcl_ensemble as dclens
import dcl_membrure_AIJB as AIJB
import dcl_diagramme_VM as VM

force_verin = round(math.sqrt(AIJB.reaction_J_x**2 + AIJB.reaction_J_y**2), 2)

force_I = round(math.sqrt(AIJB.reaction_I_x**2 + AIJB.reaction_I_y**2), 2)
theta_I = (math.atan(AIJB.reaction_I_y / AIJB.reaction_I_x) * 180 / math.pi) + 180

force_J = round(math.sqrt(AIJB.reaction_J_x**2 + AIJB.reaction_J_y**2), 2)
theta_J = (math.atan(AIJB.reaction_J_y / AIJB.reaction_J_x) * 180 / math.pi)

contrainte_max_sigma_x_AIJB = -(VM.moment_MAX_AIJB * Y_MAX) / IX

print("La reaction en By est:", round(dclpla.reaction_B, 2), "newtons.")
print("La reaction en Bx est:", 0, "newtons.")
print("La reaction en Dy est:", round(dclpla.reaction_D, 2), "newtons.")
print("La reaction en Dx est:", 0, "newtons.")
print("La reaction en Cy est:", round(dclens.reaction_C, 2), "newtons.")
print("La reaction en Cx est:", 0, "newtons.")
print("La reaction en Ay est:", round(dclens.reaction_A, 2), "newtons.")
print("La reaction en Ax est:", 0, "newtons.")
print("La reaction en Ix est:", round(AIJB.reaction_I_x, 2), "newtons.")
print("La reaction en Iy est:",  round(AIJB.reaction_I_y, 2), "newtons.")
print("La reaction en Jx est:",  round(AIJB.reaction_J_x, 2), "newtons.")
print("La reaction en Jy est:",  round(AIJB.reaction_J_y, 2), "newtons.")
print("La reaction en Kx est:",  round(-AIJB.reaction_J_x, 2), "newtons.")
print("La reaction en Ky est:",  round(-AIJB.reaction_J_y, 2), "newtons.")

print("La force du verin est:", force_verin, "newtons.")
print("La force en I est:",  round(force_I, 2), "newtons.")
print("La l'angle de la force I est:",  round(theta_I, 2), "deg.")
print("La l'angle de la force B est:",  round(((3 * math.pi / 2) - THETA) * 180 / math.pi, 2), "deg.")
print("La force en J est:",  round(force_J, 2), "newtons.")
print("La l'angle de la force J est:",  round(theta_J, 2), "deg.")
print("Le theta max est:",  round(THETA*180 / math.pi, 2), "deg.")
print("Le theta verin max est:",  round(THETA_VERIN*180 / math.pi, 2), "deg.")
print("Longueur du verin est:",  round(LONGUEUR_VERIN, 2), "m.")
print('Contraine max sigma_x:', f'{contrainte_max_sigma_x_AIJB:.3e}', )
print("Nom:", NOM_T)