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
