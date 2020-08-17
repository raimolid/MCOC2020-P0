# MCOC2020-P0

# Mi computador principal

* Marca/modelo: HP Pavilion 15-cw1007la
* Tipo: Notebook
* Año adquisición: 2020
* Procesador:
  * Marca/Modelo: AMD Ryzen 7 3700U
  * Velocidad Base: 2.3 GHz
  * Velocidad Máxima: 4 GHz
  * Numero de núcleos: 4 
  * Humero de hilos: 8
  * Arquitectura: x86_64
* Tamaño de las cachés del procesador
  * L1: 384 KB
  * L2: 2 MB
  * L3: 4 MB
* Memoria 
  * Total: 16 GB
  * Tipo memoria: DDR4
  * Velocidad 2400 MHz
  * Numero de (SO)DIMM: 2
* Tarjeta Gráfica
  * Marca / Modelo: AMD Radeon RX Vega 10 Graphics
  * Memoria dedicada: 2 GB
  * Resolución: 1920 x 1080
* Disco 1: 
  * Marca: SK Hynix
  * Tipo: SSD
  * Tamaño: 512 GB
  * Particiones: 1
  * Sistema de archivos: NTFS

* Dirección MAC de la tarjeta wifi: D8-12-65-09-29-3F
* Dirección IP (Interna, del router): 192.168.0.6
* Dirección IP (Externa, del ISP): 190.162.178.62
* Proveedor internet: VTR Banda Ancha S.A.

# Desempeño MATMUL

![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega1-2/Plot_matmul.png)

* ¿Como difiere del gráfico del profesor/ayudante?: En todo en realidad, 
   ya que no alcance a graficar las 10 corridas y me falto poner los ticks 
   y etiquetas de los graficos. Aún así se presentan diferencias en el
   grafico del tiempo v tamaño de matriz y memoria v tamaño de la matriz

* ¿A qué se pueden deber las diferencias? Las diferencias pueden tener su 
   raíz, en el caso del tiempo, en la potencia del procesado o de algún otro 
   componente del hardware, en el caso dela memoria, claramente el 
   rendimiento se ve afectado por la cantidad de memoria del computador y 
   las diferencias entre el computador del profesor/ayudante y el mio.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, 
  pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  Porque la memoria va a ir variando proporcionalmente a como se ocupa su 
  almacenamiento, y mientras más grande la matriz más memoria ocupa.
  Crece linealmente. En el caso del tiempo no varia lineal, ya que este va a 
  depender de la cantidad de operaciones que pueden existir en el momento y estas 
  no varian linealmente necesariamente.

* ¿Qué versión de python está usando?: 3.8

* ¿Qué versión de numpy está usando?: 1.8

* Durante la ejecución de su código ¿se utiliza más de un procesador? 
  Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
  Si, en algunos casos supera el 100%

![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega1-2/Proc_matmul.png)

# Desempeño MIMATMUL

![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega3/Plot_mimatmul.png)

* ¿Como difiere del gráfico del profesor/ayudante?: Difiere en la cantidad de 
  matrices que ejecute. Si bien, hice las 10 corridas solicitadas, no logré hacer 
  matrices NxN más grandes que N=500, en cambio, en el codigo del ayudante se 
  ejecutaron hasta matrices de N=1000

* ¿A qué se pueden deber las diferencias?: Se debe al gran tiempo que se tomaba el 
  programa con la funcion nueva mimatmul en multiplicar matrices grandes, arriba de 
  N=250. Tomando hasta N=500, me tomo alrededor de 40 min en ejecutar todo, por lo
  que decidi implementarlo hasta ese límite, y que es lo que explica la diferencia
  del largo de las curvas

* El gráfico de uso de memoria es lineal con el tamaño de matriz, 
  pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  Porque la memoria va a ir variando proporcionalmente a como se ocupa su 
  almacenamiento, y mientras más grande la matriz más memoria ocupa.
  Crece linealmente. En el caso del tiempo no varia lineal, ya que este va a 
  depender de la cantidad de operaciones que pueden existir en el momento y estas 
  no varian linealmente necesariamente.

* ¿Qué versión de python está usando?: 3.8

* ¿Qué versión de numpy está usando?: 1.8

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una 
  imagen de su uso de procesador durante alguna corrida para confirmar. 
  Si, en algunos casos supera el 100%

![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master7Entrega3/Proc_mimatmul.png)

# Desempeño INV
## Caso 1: numpy.linalg.inv()
### dtype=np.half
* ERROR: ARRAY TYPE FLOAT16 UNSUPPORTED IN LINALG
### dtype=np.single
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_1_single.png)
### dtype=np.double
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_1_double.png)
### dtype=np.longdouble
* ERROR: ARRAY TYPE FLOAT64 UNSUPPORTED IN LINALG

## Caso 2: scipy.linalg.inv(overwrite_a=False)
### dtype=np.half
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_2_half.png)
### dtype=np.single
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_2_single.png)
### dtype=np.double
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_2_double.png)
### dtype=np.longdouble
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_2_longdouble.png)

## Caso 3: scipy.linalg.inv(overwrite_a=True)
### dtype=np.half
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_3_half.png)
### dtype=np.single
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_3_single.png)
### dtype=np.double
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_3_double.png)
### dtype=np.longdouble
![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega4/plot_3_longdouble.png)

* Es evidente y comprobable que en los 4 tipos de datos: Half, single, double y 
  longdouble hay diferencias en cuanto a la precisión de números, siendo half el menos
  preciso, aguantando números no tan extensos, y longdouble el más preciso. Con esa 
  lógica, se observa un proporcionalidad en cuanto a un mayor tiempo de procesamiento 
  en los tipos de datos más precisos y un menor tiempo en los menos precisos. Por 
  ejemplo, en el caso 3 se observó que para matrices (10.000 x 10.000), el dtype=np.half
  demoró 39,218 (s) en calcular la inversa, en cambio el dtype=np.longdouble, demoró
  58,675 (s) y los 2 ocuparon 1,6 GB se memoria.Esre tipo de ejemplos se repitio, por lo
  que es posible inferir que +precision = +tiempo pero no necesariamente +memoria.
* ¿Qué algoritmo de inversión cree que utiliza cada método?
   Se utiliza la solución analítica, de la regla de Cramer y teorema de Laplace, que
   basa el calculo del determinante de matrices grandes en la descomposición de sumas 
   de matrices más pequeñas. 
* ¿Como incide el paralelismo y la estructura de caché de su procesador en el desempeño 
  en cada caso? El paralelismo es una funcionalidad que permite realizar operaciones
  simultaneamente y buscar información en los distintos niveles de cachés del procesador,
  en mi caso tengo 3 niveles: L1: 384 KB, L2: 2 MB, L3: 4 MB, que se muestran en los 
  gráficos con lineas horizontales negras. Estas permiten regular la eficiencia con la 
  que se opera, las de menor memoria operan más rápido, como la caché 3.
  
  # Desempeño Ax=b
  
  ![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Entrega6/plot6.png)
