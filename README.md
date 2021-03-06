# Montecarlo free throws

### Este es un modelo de simulación Montecarlo para simular la cantidad de veces que un jugador de baloncesto, acierta tiros libres, basados en las estadísticas del sitio web de [E.S.P.N. Stat Free Throws](https://www.espn.com/nba/stats/player/_/stat/free-throws).

Basados en las estadísticas históricas totales, para un jugador, en cuanto a lanzamientos libres se refiere, tenemos el porcentaje de acierto total en lanzamientos libres que ha realizado en el histórico de su carrera.

Con esta estadística, podemos realizar un método Montecarlo, en el cual generamos números pseudo aleatorios (entre 0 y 1), y realizamos una condición para cada número generado, si el número generado es menor o igual a la prob de acierto del jugador, entonces se tomará como un acierto, mientras que si es mayor, se interpretará como que no acertó el lanzamiento.

Esto se hará en n ensayos, cada ensayo con n lanzamientos, finalmente observaremos el promedio de pruebas en las cuales se cumplio la probabilidad dada, es decir que se cumplio la estadística que se menciona en el sitio web.

### Simulación por computador
#### Integrantes
- [Richard Agudelo](https://github.com/Richardagudelo)
- [Christian Chamorro](https://github.com/cris2014971130)
- [Luis Torres](https://github.com/luisTorres14)
- [Oscar Rojas](https://github.com/augusticor)

### Requerimientos
- Python ^3.6
- Libreria [NumPy](https://numpy.org/)
- Datos de un jugador, disponibles en [E.S.P.N. Stat Free Throws](https://www.espn.com/nba/stats/player/_/stat/free-throws)

#### Otros
Documentación oficial [Python](https://docs.python.org/3/library/random.html#random.random)
