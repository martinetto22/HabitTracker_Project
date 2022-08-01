# HabitTracker_Project
To achieve any objective, one must set habits that will give him the necessary discipline to achieve his goals.
The project consists of a program that records the objectives that a user has set for himself. In each of his objectives, the user should define the habits necessary to achieve his goal. The habits have been divided into "daily habits" and "weekly habits".

The program will keep track of the days that the daily habits have been fulfilled (the same with the weekly habits) and will display simple statistics that will allow a better analysis of the user's behavior (to facilitate its improvement).

## Starting

### Prerequisites
For the execution of the program it will be necessary to have installed a SQL database manager (for example mySQL) and any IDE with which you can execute python code (it is not necessary to install any IDE, being able to execute python code through terminal would be enough, although it is advisable to install an IDE such as PyCharm).

### Installation
This program has been developed with PyCharm so I will discuss how to install the different libraries from PyCharm:

Al importar una libreria veremos lo siguiente:

![image](https://user-images.githubusercontent.com/110245293/182176958-c4922e03-a84b-4134-8b2d-3f2d3a97b674.png)

Solamente deberemos pulsar sobre el boton rojo que aparece sobre la libreria que queremos importar (en este ejemplo webdriver). Una vez hemos pulsado el boton se depliega una ventana donde deveremos pulsar a:
install package

La otra forma de instalar una libreria usando PyCharm seria poniendo el raton sobre la libreria (la que esta marcada en rojo) y pulsar las teclas: Alt+Shift+Enter

De este modo lograremos importar todas las librerias que necesitemos. Por otro lado, el gestor MySQL, lo podemos instalar del siguiente modo:

En una maquina linux tenemos la explicación perfectamente detallada aqui:

https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html

En una maquina Windows:

https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html


## Example
Es necesario que al empezar, generemos la base de datos. Todas las tablas, inserciones... estan definidas en el fichero bbdd.sql, de modo que debemos escribir los siguientes comandos en nuestra terminal (durante todo el documento comentare los pasos que se deben realizar usando un sistema operativo Linux, pero en cualquier caso, en Windows o Mac se debera hacer lo mismo aunque con instrucciones distintas. Se pueden encontrar con facilidad buscando en internet):

![image](https://user-images.githubusercontent.com/110245293/182180878-792d5c47-0f1e-405d-86a1-d521823757dd.png)

Con este comando entramos en nuestro gestor de bases de datos (los comandos son las letras blancas que vemos a continuación de las letras azules y el simbolo $ en blanco).

![image](https://user-images.githubusercontent.com/110245293/182181083-0e4a979e-539b-405c-ad4c-c8208c2635cd.png)

Ahora los comandos SQL que aplicamos son las letras que hay a continuación de "mysql>". Vemos que hemos creado una base de datos con nombre HabitsProject. El siguiente comandos debe realizarse en el mismo directorio en el que tenemos localizado el fichero bbdd.sql.

![image](https://user-images.githubusercontent.com/110245293/182180409-4cd24274-e4ac-4a97-b880-8823c2e4f8c4.png)

Una vez llegados en este punto ya tenemos la base de datos preparada para utilizarla.

Ahora solamente necesitamos ejecutar el fichero main.py (debemos tener las librerias instaladas!). Con PyCharm es muy senzilla la ejecución:

![image](https://user-images.githubusercontent.com/110245293/182183611-f93a25e5-35c2-40e9-9c55-b9b88ae62830.png)

Debemos hacer click en el boton verde que al que le he hecho un circulo y esta señalada for una flexa azul.

Ahora ya deberiamos tener la aplicación en funcionamiento. Debemos ver el siguiente menu:

![image](https://user-images.githubusercontent.com/110245293/182185154-304bc907-d783-498c-b956-d424330b34ba.png)

En este punto debemos escojer entre iniciar sesión o registrarnos. Por defecto, al crear las tablas en la base de datos para el programa, generamos un usuario con nombre: "marti" y contraseña: "abc23". A medida que vamos contestando las preguntas deberiamos ver los siguiente (las letras en verde son las letras que introduzco por teclado):

![image](https://user-images.githubusercontent.com/110245293/182185637-b217d30b-3b83-4372-888e-6ae64d04497a.png)

Este es el menu principal al que llegamos:

![image](https://user-images.githubusercontent.com/110245293/182185951-3b68ff05-4705-44af-8087-502bbf7a20b6.png)

Este menu principal es el menu personalizado para el usuario "marti" con contraseña "abc23". Vemos una tabla primero en la que tenemos todos los objetivos con sus fechas y con una columna que indica si se ha logrado el objetivo o todavia no (si ya se a logrado el objetivo tenemos un 1 y si todavia no se a logrado tenemos un 0). Lo mismo sucede con la columna "Achivement date", si no hay nada, es porque todavia no se a logrado el objetivo.

Debajo de la tabla tenemos todas las opciones disponibles para el programa. Con introducir cualquiera de las opciones (num. 1, 2, 3... 13) procedemos a ejecutar la opcion que queremos.

Si escojemos la opción 1, veremos exactamente la misma tabla que ya vemos cada vez que estamos en el menu principal. Asi que mostraremos ahora como podemos ver los habitos diarios de un objetivo (opcion 2):

![image](https://user-images.githubusercontent.com/110245293/182187857-8b779f92-8294-479d-baa4-0fdf439b5309.png)
![image](https://user-images.githubusercontent.com/110245293/182187935-7d867171-78c1-48bc-8ea1-0b21e5fc5969.png)

Al indicar que queremos ver los habitos diarios, el programa nos pide introducir el identificador del objetivo del que queremos ver los habitos diarios. Al introducir el identificador del objetivo se nos muestra una tabla con todos los habitos diarios definidos para lograr el objetivo (en este caso solamente nos sale un unico habito diario), debajo de la tabla tambien los vemos en formato lista.

Ahora procedemos a añadir un habito diario. Al añadir el habito diario (opción 3) nos volvera a pedir introducir el identificado del objetivo. A continuación introduciremos el habito diario que queremos y especificaremos que no deseamos añadir más habitos diarios para este objetivo

![image](https://user-images.githubusercontent.com/110245293/182189257-0e481986-8dd3-4cd4-a042-347e65558cf5.png)

Vemos que nuestro habito diario para el objetivo con identificado "1", a sido añadido.

El funcionamiento para los habitos semanales es exactamente el mismo.

Para poder añadir un nuevo objetivo el procedimiento es el siguiente:

![image](https://user-images.githubusercontent.com/110245293/182189747-a42985f4-3087-4c3f-bb32-1ba3e9e3a43c.png)

Vemos que primero nos pide el nombre del objetivo, a continuación definir un poco el objetivo y por ultimo la duración de dicho objetivo. Una vez contestadas todas las preguntas requeridas, volvemos al menu principal donde vemos la tabla con el nuevo objetivo añadido, con la fecha de inicio, la fecha final, el identificador y un 0 en la columna "Achivement" mostrando que todavia no lo hemos logrado.

Para identificar un objetivo como cumplido (opción 7) el procedimiento es el siguiente:

![image](https://user-images.githubusercontent.com/110245293/182190699-47b5065e-52c2-42bc-b356-419ccbdc210f.png)
![image](https://user-images.githubusercontent.com/110245293/182190772-39b147cc-508c-4775-9436-298b69209229.png)

La opción 8 nos muestra tres graficos. El primero muestra con un punto los dias que tenemos por lo menos un objetivo iniciado. El segundo grafico nos muestra las fechas limite para terminar alguno de los objetivos y por ultimo tendremos un grafico de barras que nos mostrara los objetivos cumplidos (1)
 y los objetivos que todavia no hemos cumplido (0).
 
 Para ver la racha maxima de habitos diarios cumplidos es la opcion 9:
 
 ![image](https://user-images.githubusercontent.com/110245293/182191828-ce7a0e59-4adb-44ac-831e-020168c823b3.png)
 
 Para ver lo mismo con los habitos semanales el funcionamiento es el mismo.
 
 Para el control de los habitos tenemos las opciones 11 y 12:
 
 Opción 11:
 
 ![image](https://user-images.githubusercontent.com/110245293/182192099-a5067b18-bd30-4f1a-be73-4a7412fcf4cf.png)
 
 Opción 12:
 
 ![image](https://user-images.githubusercontent.com/110245293/182192223-08971e2e-4417-49c3-92f8-2fa1dac9a276.png)
 
 Vemos que nos dice que hoy no es domingo y que por lo tanto no puedo decir que el habito semanal a sido satisfecho. Solamente podemos indicar que hemos realizado el habito semanal los domingos, cuando termina la semana. En caso de que quisiera decir que he hecho los habitos semanales de la semana pasada, no podria. El programa registra como que no hemos realizado el habito semanal.
 
 ![image](https://user-images.githubusercontent.com/110245293/182192663-f6290230-6cd1-4551-aa66-b2c7566252a7.png)

Por ultimo tenemos la opción 13 para salir del programa y volver al inicio. Ahora mostraremos el procedimiento para registrarse.
Antes de nada, debemos introducir sign up:

![image](https://user-images.githubusercontent.com/110245293/182199549-e4339e69-40d7-4360-8739-f3fe303786c3.png)

Una vez estamos registrados podemos entrar en la aplicación:

![image](https://user-images.githubusercontent.com/110245293/182199680-d7e1e106-a22a-46ce-9ce1-0ef21fa417ce.png)

Asi es como queda la tabla en el caso del usuario Judith que acabamos de crear.



