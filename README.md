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

![Alt Text](https://github.com/raimolid/MCOC2020-P0/blob/master/Plot_matmul.png)

* ¿Como difiere del gráfico del profesor/ayudante?: En todo en realidad, 
   ya que no alcance a graficar las 10 corridas y me falto poner los ticks 
   y etiquetas de los graficos. Aún así se presentan diferencias en el
   grafico del tiempo v tamaño de matriz y memoria v tamaño de la matriz

* ¿A qué se pueden deber las diferencias? Las diferencias pueden tener su 
   raíz, en el caso del tiempo, en la potencia del procesado o de algún otro 
   componente del hardware, en el caso dela memoria, claramente el 
   rendimiento se ve afectado por la cantidad de memoria del computador y 
   las diferencias entre el computador del profesor/ayudante y el mio.

* El gráfico de uso de memoria es lineal con el tamaño de matriz, pero el de tiempo transcurrido no lo es ¿porqué puede ser?
  poque la memoria, va a ir variando proporcionalmente a como se ocupa su almacenamiento, y mientras más grande la matriz
  más memoria ocupa. En el caso del tiempo no varia lineal, ya que este va a dependen de la cantidad de operaciones que pueden
  existir y estas no varian linealmente necesariamente.

* ¿Qué versión de python está usando?: 3.8

* ¿Qué versión de numpy está usando?: 1.8

* Durante la ejecución de su código ¿se utiliza más de un procesador? Muestre una imagen de su uso de procesador durante alguna corrida para confirmar. 
Si, en algunos casos supera el 100%

![Alt Text](/rendi% procesador.png)
