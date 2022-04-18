import random
import pandas as pd

hom = pd.read_csv ('hombres.csv')
ap = pd.read_csv ('apellidos.csv')
muj = pd.read_csv ('mujeres.csv')

for n in range(50):
	x=random.randint(0, 1)
	if (x == 1):
		print(hom['nombre'][random.randint(0, len(hom))],end=" ")
		print(ap['apellido'][random.randint(0, len(ap))],end=" ")
		print(ap['apellido'][random.randint(0, len(ap))])
	else:
		print(muj['nombre'][random.randint(0, len(muj))],end=" ")
		print(ap['apellido'][random.randint(0, len(ap))],end=" ")
		print(ap['apellido'][random.randint(0, len(ap))])
