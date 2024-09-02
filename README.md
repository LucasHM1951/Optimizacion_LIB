# Optimizacion LIB
Optimización de un modelo térmico paramétrico de baterías de litio mediante regresión simbólica 

## Resources
Contiene dataframes de los coeficientes, junto con el numero de celdas en cada uno. 

**cdrag:** coeficiente de arrastre

**ff:** factor de friccion

**n:** numero de nusselt

## GPLearn
Actualización: se añade un notebook para cada uno de los coeficientes.  Se añadieron como funciones las distintas potencias obtenidas en cada caso por Rafael:
Para el coeficiente de arrastre y el factor de fricción se consiguen replicar los resultados de Rafael, mientras que para el número de Nusselt no, pero a lo menos la función obtenida está en función de las 3 variables. 

UPDATE 02/29 

i) CDrag: el coeficiente de la exponencial del S se ajusta automaticamente, obteniendo valores similares que el valor original. Lo cual no ocurria para el coeficiente del Re, se probaron distintas combinaciones: distintos rangos para la constantes, dejar uno fijo y que se ajuste el otro, pero la única vez que considera el Reynolds en la ecuación es cuando esos parametros fijos. 

ii) FFriction: con incorporar las funciones explicitas, se consiguen replicar los resultados de Rafael. 


## PySR.
UPDATE 02/09: 

i) CDrag: se añade notebook con resultados de PySR con el coeficiente de arrastre, obteniendo métricas similares. 
