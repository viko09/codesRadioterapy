# Created by. Viko Luna
# Calcular el numero de electrones en n número de moles a partir de los datos de la tabla periodica
import pandas as pd

data = pd.read_csv('elements.csv')
print(data)

elementos = data.drop(columns=['Period', 'Group', 'Phase', 'Radioactive', 'Natural', 'Metal', 'Nonmetal',
                               'Metalloid', 'Type', 'Nonmetal', 'Metalloid', 'Type', 'AtomicRadius',
                               'Electronegativity', 'FirstIonization', 'Density', 'MeltingPoint', 'BoilingPoint',
                               'NumberOfIsotopes', 'Discoverer', 'Year', 'SpecificHeat', 'NumberofShells',
                               'NumberofValence'])

print(elementos)

print("Introduzca el número atómico del elemento: ")
#
# numAtom = input()

print("Los datos del elemento ingresado son: ")
# print(data[numAtom])

print("Introduzca la masa de la sustancia en gramos: ")
# masa = input()

# Numero de moles
# Masa Atomica para calcular el numero de moles
# masaAtom = data[]

# numMols = masa/
