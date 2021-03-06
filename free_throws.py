import numpy as np

print('===== Simulación de Montecarlo =====')

# FT = free throws (tiros libres)
ft_total_percentage = 0.907

"""
Cantidad de veces que se cumple la probabilidad de las
estadísticas en cada prueba
"""
true_probability = []
tests_number = 10000  # Ensayos
free_throws = 1000  # Lanzamientos

for i in range(0, tests_number):
	shots_made = []
	for j in range(0, free_throws):
		pseudo_random_num = np.random.random()
		if pseudo_random_num <= ft_total_percentage:
			shots_made.append(1)
		else:
			shots_made.append(0)

	if sum(shots_made) >= (free_throws * ft_total_percentage):
		true_probability.append(1)
	else:
		true_probability.append(0)

print('Promedio de aciertos en ', tests_number, ' ensayos de ', free_throws, ' tiros libres c/u')
average_ft_rate = np.average(true_probability)
print(average_ft_rate, '\n')

print('Número de veces que acerto más de ', free_throws * ft_total_percentage, ' tiros libres ', true_probability.count(1))
print('======')
print('Número de veces que no acerto ', true_probability.count(0))