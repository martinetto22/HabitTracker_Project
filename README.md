# HabitTracker Project
To achieve any objective, one must set habits that will give him the necessary discipline to achieve his goals.
The project consists of a program that records the objectives that a user has set for himself. In each of his objectives, the user should define the habits necessary to achieve his goal. The habits have been divided into **daily habits** and **weekly habits**.

The program will keep track of the days that the daily habits have been fulfilled (the same with the weekly habits) and will display simple statistics that will allow a better analysis of the user's behavior (to facilitate its improvement).

## Starting 🚀

### Prerequisites 📋
For the execution of the program it will be necessary to have installed a SQL database manager (for example mySQL) and any IDE with which you can execute python code (it is not necessary to install any IDE, being able to execute python code through terminal would be enough, although it is advisable to install an IDE such as PyCharm).

### Installation 🔧
This program has been developed with PyCharm so I will discuss how to install the different libraries from PyCharm. When importing a library we will see the following:

![image](https://user-images.githubusercontent.com/110245293/182176958-c4922e03-a84b-4134-8b2d-3f2d3a97b674.png)

We only have to click on the red button that appears over the library we want to import (in this example webdriver). Once we have clicked on the button a window will pop up where we will have to click on:
*install package*

The other way to install a library using PyCharm would be to put the mouse over the library (the one marked in red) and press the keys: *Alt+Shift+Enter*.

This way we will be able to import all the libraries we need. On the other hand, the MySQL manager can be installed in the following way:

On a linux machine we have a perfectly detailed explanation here:

https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-install-linux-quick.html

On a Windows machine:

https://dev.mysql.com/doc/refman/8.0/en/windows-installation.html


## Example 🎁
It is necessary that at the beginning, we generate the database. All tables, test inserts... are defined in the bbdd.sql file, so we must type the following commands in our terminal (throughout the document I will discuss the steps to be performed using a Linux operating system, but in any case, in Windows or Mac you must do the same but with different instructions. They can be easily found by searching the internet):

![image](https://user-images.githubusercontent.com/110245293/182180878-792d5c47-0f1e-405d-86a1-d521823757dd.png)

With this command we enter our database manager (the commands are the white letters that we see after the blue letters and the $ symbol in white).

![image](https://user-images.githubusercontent.com/110245293/182181083-0e4a979e-539b-405c-ad4c-c8208c2635cd.png)

Now the SQL commands we apply are the letters after "***mysql>***". We can see that we have created a database named **HabitsProject**. The next command must be done in the same directory where the bbdd.sql file is located.

![image](https://user-images.githubusercontent.com/110245293/182180409-4cd24274-e4ac-4a97-b880-8823c2e4f8c4.png)

At this point, the database is ready for use.

Now we just need to run the main.py file (we must have the libraries installed!). With PyCharm it is very easy to run:

![image](https://user-images.githubusercontent.com/110245293/182183611-f93a25e5-35c2-40e9-9c55-b9b88ae62830.png)

We must click on the green button that I have circled and is marked by a blue arrow.

Now we should have the application running. You should see the following menu:

![image](https://user-images.githubusercontent.com/110245293/182185154-304bc907-d783-498c-b956-d424330b34ba.png)

At this point we must choose between logging in or registering. By default, when creating the tables in the database for the programme, we generate a user with name: "***marti***" and password: "***abc23***". As we answer the questions we should see the following (the letters in green are the letters I enter on the keyboard):

![image](https://user-images.githubusercontent.com/110245293/182185637-b217d30b-3b83-4372-888e-6ae64d04497a.png)

This is the main menu we arrived at:

![image](https://user-images.githubusercontent.com/110245293/182185951-3b68ff05-4705-44af-8087-502bbf7a20b6.png)

This main menu is the custom menu for the user "marti" with password "abc23". We see a table first in which we have all the objectives with their dates and with a column that indicates if the objective has been achieved or not yet (if the objective has been achieved we have a 1 and if it has not yet been achieved we have a 0). The same happens with the column "*Achievement date*", if there is nothing, it is because the objective has not yet been achieved.

Below the table we have all the options available for the programme. By entering any of the options (num. **1, 2, 3... 13**) we execute the option we want.

**1.** If we choose option 1, we will see exactly the same table that we already see every time we are in the main menu. So we will now show how we can see the daily habits of a target (option 2):

![image](https://user-images.githubusercontent.com/110245293/182187857-8b779f92-8294-479d-baa4-0fdf439b5309.png)
![image](https://user-images.githubusercontent.com/110245293/182187935-7d867171-78c1-48bc-8ea1-0b21e5fc5969.png)

When we indicate that we want to see the daily habits, the programme asks us to enter the identifier of the objective for which we want to see the daily habits. When we enter the target identifier, a table is displayed with all the daily habits defined to achieve the target (in this case we only get a single daily habit), below the table we also see them in list format.

**2.** Now we proceed to add a daily habit. When adding the daily habit (option 3) we will be asked again to enter the target ID. Then we will introduce the daily habit we want and we will specify that we don't want to add more daily habits for this objective.

![image](https://user-images.githubusercontent.com/110245293/182189257-0e481986-8dd3-4cd4-a042-347e65558cf5.png)

We see that our daily habit for the target with identifier "1" has been added. The operation for the weekly habits is exactly the same. In order to add a new target, the procedure is as follows:

![image](https://user-images.githubusercontent.com/110245293/182189747-a42985f4-3087-4c3f-bb32-1ba3e9e3a43c.png)

We see that first we are asked for the name of the objective, then we are asked to define the objective a little bit and finally the duration of the objective (in days). Once all the required questions have been answered, we return to the main menu where we see the table with the new objective added, with the start date, the end date, the identifier and a 0 in the "*Achievement*" column showing that we have not yet achieved it.

**3.** To identify an objective as achieved (option 7) the procedure is as follows:

![image](https://user-images.githubusercontent.com/110245293/182190699-47b5065e-52c2-42bc-b356-419ccbdc210f.png)
![image](https://user-images.githubusercontent.com/110245293/182190772-39b147cc-508c-4775-9436-298b69209229.png)

**4.** Option 8 shows three graphs. The first one shows with a dot the days that we have at least one goal started. The second graph shows us the deadlines to finish some of the objectives and finally we will have a bar graph that will show us the fulfilled objectives (1) and the objectives that we have not yet fulfilled (0).
 and the objectives we have not yet achieved (0).
 
**5.** To see the maximum number of daily habits completed is option 9:
 
 ![image](https://user-images.githubusercontent.com/110245293/182191828-ce7a0e59-4adb-44ac-831e-020168c823b3.png)
 
To see the same with the weekly habits, the operation is the same.
 
For the monitoring of the habits we have options 11 and 12:
 
 **6.** Option 11:
 
 ![image](https://user-images.githubusercontent.com/110245293/182192099-a5067b18-bd30-4f1a-be73-4a7412fcf4cf.png)
 
 **7.** Option 12:
 
 ![image](https://user-images.githubusercontent.com/110245293/182192223-08971e2e-4417-49c3-92f8-2fa1dac9a276.png)
 
We see that it tells us that today is not Sunday and therefore we cannot say that the weekly habit has been satisfied. We can only indicate that we have done the weekly habit on Sundays, when the week ends. If I wanted to say that I have done the weekly habit during the past week, I would not be able to do so. The programme would automatically register that we have not done the weekly habit.
 
 ![image](https://user-images.githubusercontent.com/110245293/182192663-f6290230-6cd1-4551-aa66-b2c7566252a7.png)
 
**8.** Finally we have option 13 to exit the programme and return to the start. Now we will show you how to register.
First of all, we must enter sign up:

![image](https://user-images.githubusercontent.com/110245293/182199549-e4339e69-40d7-4360-8739-f3fe303786c3.png)

Once we are registered we can enter the application:

![image](https://user-images.githubusercontent.com/110245293/182199680-d7e1e106-a22a-46ce-9ce1-0ef21fa417ce.png)

This is how the table looks like in the case of the user Judith that we have just created.



📌
So far we have seen how the programme works. There are still many things that could be improved that due to time constraints I have not been able to address. In any case, this first version can be used for the realisation of a more ambitious project since the basic functionalities are already implemented and although there are probably things that can be done to optimise the code, if we start a project with everything that it already has, we will save a lot of work.



## Built with 🛠️

* [PyCharm](https://www.jetbrains.com/pycharm/) - IDE used
* [MySQL Workbench](https://www.mysql.com/products/workbench/) - Database development environment used
