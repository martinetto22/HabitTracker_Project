import datetime
import calendar
from datetime import date, timedelta
import matplotlib.pyplot as plt
from tabulate import tabulate
from termcolor import colored


class Estadistiques:
    '''
    This class is used to make statistics with the objectives and habits previously defined by a user.
    '''

    def inicial_final_objectives_dates(self, cur, username):

        '''
        This function is used to show graphically, which days the targets start and which days they end. You will
        not see which target starts on which day, it simply serves to show on which days targets have been started
        and which days they end.
        We will look at a few points. The y-axis represents the data (in month-day or year-month format).
        The days when the targets start will be shown on the first chart and the days when they end will be shown
        on the second chart.

        Arguments:
        username(string) - The name of the user who is logged in.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        It does not return data, it prints 2 graphs. The first one with the days that targets have been started and the second one with the
        days that targets have ended.
        '''

        inicial_dates_list = list()
        final_dates_list = list()
        y = list()

        usr = username.replace("'", "")
        cur.execute('SELECT inici, finally FROM Objectives WHERE username LIKE ("%s")', (usr))
        dates = cur.fetchall()

        for date in dates:
            y.append(1)
            date_inici = date[0].replace("'", "")
            date_inici = date_inici.split("-")
            date1 = datetime.datetime(int(date_inici[0]), int(date_inici[1]), int(date_inici[2]))
            inicial_dates_list.append(date1)

            date_final = date[1].replace("'", "")
            date_final = date_final.split("-")
            date2 = datetime.datetime(int(date_final[0]), int(date_final[1]), int(date_final[2]))
            final_dates_list.append(date2)

        fig = plt.figure(figsize=[11, 4], facecolor="LightSalmon", edgecolor="#2E8B57", linewidth=10)
        plt.title('Dates inici', fontsize=16)
        plt.plot_date(inicial_dates_list, y)
        plt.tight_layout()
        plt.xlabel("Date(month-day)",
                   fontsize=10, )
        plt.ylabel("Number Objectives",
                   fontsize=10)
        plt.grid(alpha=0.2,
                 color="SteelBlue",
                 linestyle="-.",
                 linewidth=1.5)
        plt.show()

        fig = plt.figure(figsize=[11, 4], facecolor="LightSalmon", edgecolor="#2E8B57", linewidth=10)
        plt.title('Dates final', fontsize=16)
        plt.plot_date(final_dates_list, y)
        plt.tight_layout()
        plt.xlabel("Date(year-month)",
                   fontsize=10, )
        plt.ylabel("Number Objectives",
                   fontsize=10, )
        plt.grid(alpha=0.2,
                 color="SteelBlue",
                 linestyle="-.",
                 linewidth=1.5)
        plt.show()

    def assolits_no_assolits(self, cur, username):

        '''
        This function will be used to graphically display the relationship between the objectives achieved and
        those that have not yet been achieved. The graph will be in histogram format, where 1 will represent the
        number of objectives achieved and 0 the number of objectives not yet achieved.

        Arguments:
        username(string) - The name of the user who is logged in.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        It does not return data, it prints a graph to quickly see the ratio of targets achieved and the number of
        targets still to be achieved.
        '''

        positiu = 0
        negatiu = 0

        usr = username.replace("'", "")
        cur.execute('SELECT ACHIVEMENT FROM Objectives WHERE username LIKE ("%s")', (usr))
        resultats = cur.fetchall()
        sol = list()

        for resultat in resultats:
            sol.append(resultat[0])
            if resultat[0] == 1:
                positiu += 1
            else:
                negatiu += 1

        total = len(resultats)
        print("\n" * 3 + "-" * 100 + "\n\n")

        plt.style.use(plt.style.available[8])
        fig = plt.figure()
        fig.set_size_inches(15, 8)
        fig.suptitle("Relationship between the objectives achieved and those yet to be achieved",
                     fontsize=16,
                     backgroundcolor="DarkCyan",
                     color="w",
                     position=(0.5, 1.1)
                     )
        plt.hist(sol)
        plt.show()
        print(colored("You have achieved {} objectives, are yet to be achieved {} objectives".format(positiu, negatiu),
                      'blue'))

    def all_objectives_information(self, cur, username):

        '''
        This function is used to display all the information of the user's goals registered in the database (it
        does not show any of the habits, only the goals).
        We take the data from the database, generate the table and print it.

        Arguments:
        username(string) - The user name entered by the user.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        This function only shows the data of the user's targets, it does not return anything.
        '''

        usr = username.replace("'", "")
        cur.execute(
            'SELECT name_O, inici, finally, description_O, ID_O, ACHIVEMENT, achivement_date FROM Objectives WHERE username LIKE ("%s")',
            (usr))
        resultats = cur.fetchall()

        obj_list = list(resultats)
        titles = ("Objective name", "Start", "End", "Description", "ID", "Achivement", "Achivement date")
        obj_list.insert(0, titles)
        print(tabulate(obj_list, headers='firstrow', tablefmt='fancy_grid'))


class User(Estadistiques):
    '''
    This class inherits the properties of the Estadistiques class and is the one that represents the possible
    interactions of the user in the application.
    '''

    def registrar(self, cur, username, password):
        '''
        This function is used to register the user. Here we store the user name and password in the database.

        Arguments:
            username(string) - The user name entered by the user.
            password(string) - The password entered by the user.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            This function only enters data into the database.
        '''

        cur.execute('INSERT INTO Users (username, pw) VALUES '
                    '("%s", "%s")', (username, password))
        cur.connection.commit()


    def weekly_update(self, cur, username):
        '''
        This function marks the weekly habits that we have not updated as incomplete. For example: We have a weekly
        habit that consists in studying a minimum of 4h. If one week we have not marked anything because we have
        forgotten or for whatever reason, this function will fill the weekly task as incomplete.

        Arguments:
            username(string) - The user name entered by the user.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''

        no = "no"
        usr = username.replace("'", "")

        cur.execute('SELECT ID_O FROM Objectives WHERE username LIKE ("%s")', (usr))
        objectius_id = cur.fetchall()

        weekly_H = list()
        for objective in objectius_id:
            cur.execute('SELECT ID_WH FROM WeeklyHabits WHERE ID_O LIKE ("%s")', (objective[0]))
            weeklyHabits_id = cur.fetchall()
            weekly_H.append(weeklyHabits_id[0][0])

        dates = list()
        for w_habit in weekly_H:
            dates.clear()
            cur.execute('SELECT Data, YES_NO FROM WeeklyHabitsACHIEVED WHERE username LIKE ("%s") and ID_WH LIKE ("%s")', (usr, w_habit))
            habits_dates = cur.fetchall()

            for ndate in habits_dates:
                dates.append(datetime.datetime.strptime(ndate[0].replace("'", ""), "%Y-%m-%d"))


            if len(dates) > 0:
                last_date = datetime.datetime.strptime('2000-01-01', "%Y-%m-%d")

                for ndate in dates:
                    if ndate > last_date:
                        last_date = ndate
            else:
                last_date = datetime.datetime.now()

            sundays = list()

            i = 0
            while True:
                i += 1
                b = last_date + timedelta(i)
                today = calendar.day_name[b.weekday()]

                if b.date() >= date.today():
                    for sunday in sundays:
                        s = str(sunday)
                        cur.execute('INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES '
                                    '("%s", "%s", "%s", "%s")', (w_habit, usr, s, no))
                        cur.connection.commit()
                    break

                elif today == 'Sunday' and b.date() < date.today():
                    sundays.append(b.date())
                    i += 4


    def daily_update(self, cur, username):
        '''
        This function marks the daily habits that we have not updated as incomplete. For example: We have a daily
        habit that consists in studying a minimum of 4h. If one day we have not marked anything because we have
        forgotten or for whatever reason, this function will fill the daily task as incomplete.

        Arguments:
            username(string) - The user name entered by the user.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''

        usr = username.replace("'", "")

        cur.execute('SELECT ID_O FROM Objectives WHERE username LIKE ("%s")', (usr))
        objectius_id = cur.fetchall()

        daily_H = list()
        for objective in objectius_id:
            cur.execute('SELECT ID_DH FROM DailyHabits WHERE ID_O LIKE ("%s")', (objective[0]))
            dailyHabits_id = cur.fetchall()
            daily_H.append(dailyHabits_id[0][0])

        dates = list()

        for d_habit in daily_H:
            dates.clear()
            cur.execute('SELECT Data, YES_NO FROM DailyHabitsACHIEVED WHERE username LIKE ("%s") and ID_DH LIKE ("%s")', (usr, d_habit))
            habits_dates = cur.fetchall()

            for ndate in habits_dates:
                dates.append(datetime.datetime.strptime(ndate[0].replace("'", ""), "%Y-%m-%d"))

            if len(dates) > 0:
                last_date = datetime.datetime.strptime('2000-01-01', "%Y-%m-%d")

                for ndate in dates:
                    if ndate > last_date:
                        last_date = ndate
            else:
                last_date = datetime.datetime.now()

            difference = date.today() - last_date.date()

            a = str(difference)
            a = a.split(' ')
            try:
                num_days = int(a[0])
            except:
                num_days = 0

            for d in range(1, num_days):
                new_date = last_date.date() + datetime.timedelta(d)
                _date = str(new_date)
                no = "no"
                cur.execute('INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES '
                            '("%s", "%s", "%s", "%s")', (d_habit, usr, _date, no))
                cur.connection.commit()




    def obj_assolit(self, cur, obj_id):
        '''
        This function is used to enter the data on which a target has been achieved. Once the day on which the
        target was achieved has been entered, the database will be updated.

        Arguments:
            obj_id(string) - The identifier of the objective.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            Returns nothing, this function updates the database with the data on which the target has been achieved.
        '''

        data_acabat = input("Enter the end data in the following format: %Y-%m-%d\n")

        objectiu_id = int(obj_id)
        cur.execute("UPDATE Objectives SET ACHIVEMENT=true, achivement_date='" + data_acabat + "' WHERE ID_O={}".format(
            objectiu_id))
        cur.connection.commit()

    def llista_objectius(self, cur, username):
        '''
        This function prints a table with all the targets and their respective identifiers defined by the user.

        Arguments:
            username(string) - The user name entered by the user.

        Returns:
            It does not return data, it prints a table with all the objectives defined by the user.
        '''

        usr = username.replace("'", "")
        cur.execute('SELECT name_O, ID_O FROM Objectives WHERE username LIKE ("%s")', (usr))
        objectius_id = cur.fetchall()

        obj_list = list(objectius_id)
        titles = ("Objectives", "ID")
        obj_list.insert(0, titles)
        print(tabulate(obj_list, headers='firstrow', tablefmt='fancy_grid', showindex=True))


# No cal relacionar els habits amb l'objectiu aqui. Ho fem a la classe objective
class DailyHabits:
    '''
    Class to define the functions that a daily habit has.
    '''

    def define_dailyHabits(self, cur, identifier_O):

        '''
        This function is used to enter by keyboard the daily habits necessary for a specific objective.

        Arguments:
            identifier_O(string) - Target identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            It does not return anything, it enters in the database the habits we have defined for the objective.
        '''

        cur.execute('SELECT daily_habits, ID_DH FROM DailyHabits WHERE ID_O LIKE ("%s")', (identifier_O))
        d_hab = cur.fetchall()
        print(d_hab)

        if len(d_hab) == 0:
            print(colored('There are no objectives with this ID.', 'red'))
        else:
            while True:
                habit = input("Introduce the daily habits you need to achieve your goal:")
                cur.execute('INSERT INTO DailyHabits (ID_O, daily_habits) VALUES '
                            '("%s", "%s")', (identifier_O, habit))
                cur.connection.commit()
                mes_habits = input("Do you need to add more daily habits?")
                if mes_habits != "yes":
                    break

    def mirar_dailyHabits(self, cur, objective_identifier):

        '''
        This function is used to view in table format the daily habits defined to achieve a specific objective.

        Arguments:
            objective_identifier(string) - Target identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            Does not return data, prints a table with the daily habits of a target.
        '''

        try:
            objective = int(objective_identifier)
            cur.execute('SELECT daily_habits, ID_DH FROM DailyHabits WHERE ID_O LIKE ("%s")', (objective))
            objectius = cur.fetchall()
        except:
            objectius = list()

        if len(objectius) == 0:
            print(colored(
                "\n\nThere are no defined daily habits or you entered a bad target! You must define a daily habit to achieve your goal.\n\n",
                "blue"))
        else:
            print("\n")
            dHabits_list = list(objectius)
            titles = ("Daily Habits", "ID")
            dHabits_list.insert(0, titles)
            print(tabulate(dHabits_list, headers='firstrow', tablefmt='fancy_grid', showindex=True))
            for objectiu in objectius:
                obj = objectiu[0].replace("'", "")
                print(colored(obj, "blue"))
            print("\n")

    def Dlongest_run_streak(selfself, cur, dailyHabit_identifier):
        '''
        This function counts the maximum streak of completed daily habits.

        Arguments:
            dailyHabit_identifier(int) - Daily Habit identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''

        cur.execute('SELECT Data, YES_NO FROM DailyHabitsACHIEVED WHERE ID_DH LIKE ("%s")', (dailyHabit_identifier))
        habits_achievement = cur.fetchall()
        count1 = 0
        count2 = 0

        for day in habits_achievement:
            if day[1] == "'yes'":
                count1 += 1
            else:
                if count1 > count2:
                    count2 = count1
                count1 = 0
        if count1 > count2:
            print("LONGEST STREAK: ", count1)
        else:
            print("LONGEST STREAK", count2)

    def check_dailyHabit(self, cur, id, username):

        '''
        Function to confirm the non-performance or performance of a daily habit

        Arguments:
            id(int) - Daily Habit identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''
        usr = username.replace("'", "")
        confirmation = input('Did you realized the task(answer with: "yes" or "no")?')
        today = str(datetime.date.today())
        cur.execute('INSERT INTO DailyHabitsACHIEVED (ID_DH, username, Data, YES_NO) VALUES '
                    '("%s", "%s", "%s", "%s")', (id, usr, today, confirmation))
        cur.connection.commit()



class WeeklyHabits:
    '''
    Class to define the functions that a weekly habit has.
    '''

    def define_weeklyHabits(self, cur, identifier_O):

        '''
        This function is used to enter by keyboard the weekly habits necessary for a specific objective.

        Arguments:
        identifier_O(string) - Target identifier.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        It does not return anything, it enters in the database the weekly habits we have defined for the objective.
        '''

        cur.execute('SELECT weekly_habits, ID_WH FROM WeeklyHabits WHERE ID_O LIKE ("%s")', (identifier_O))
        w_hab = cur.fetchall()

        if len(w_hab) == 0:
            print(colored('There are no objectives with this ID.', 'red'))
        else:
            while True:
                habit = input("Introduce the weekly habits you need to achieve your goal:")
                cur.execute('INSERT INTO WeeklyHabits (ID_O, weekly_habits) VALUES '
                            '("%s", "%s")', (identifier_O, habit))
                cur.connection.commit()

                mes_habits = input("Do you need to add more weekly habits?")
                if mes_habits != "yes":
                    break

    def mirar_weeklyHabits(self, cur, objective_identifier):

        '''
        This function is used to view in table format the weekly habits defined to achieve a specific objective.

        Arguments:
        objective_identifier(string) - Target identifier.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        Does not return data, prints a table with the weekly habits of a target.
        '''

        objective = int(objective_identifier)
        cur.execute('SELECT weekly_habits, ID_WH FROM WeeklyHabits WHERE ID_O LIKE ("%s")', (objective))
        objectius = cur.fetchall()
        if len(objectius) == 0:
            print(colored(
                "\n\nThere are no defined daily habits! You must define a daily habit to achieve your goal.\n\n",
                "blue"))
        else:
            print("\n")
            wHabits_list = list(objectius)
            titles = ("Weekly Habits", "ID")
            wHabits_list.insert(0, titles)
            print(tabulate(wHabits_list, headers='firstrow', tablefmt='fancy_grid', showindex=True))
            for objectiu in objectius:
                obj = objectiu[0].replace("'", "")
                print(colored(obj, "blue"))
            print("\n")


    def Wlongest_run_streak(selfself, cur, weeklyHabit_identifier):

        '''
        This function counts the maximum streak of completed weekly habits.

        Arguments:
            weeklyHabit_identifier(int) - Weekly Habit identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''


        cur.execute('SELECT Data, YES_NO FROM WeeklyHabitsACHIEVED WHERE ID_WH LIKE ("%s")', (weeklyHabit_identifier))
        habits_achievement = cur.fetchall()
        count1 = 0
        count2 = 0

        for day in habits_achievement:
            if day[1] == "'yes'":
                count1 += 1
            else:
                if count1 > count2:
                    count2 = count1
                count1 = 0
        if count1 > count2:
            print("LONGEST STREAK: ", count1)
        else:
            print("LONGEST STREAK", count2)

    def check_weeklyHabit(self, cur, id, username):
        '''
        Function to confirm the non-performance or performance of a weekly habit

        Arguments:
            id(int) - Weekly Habit identifier.
            cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
            None
        '''


        usr = username.replace("'", "")
        confirmation = input('Did you realized the task(answer with: "yes" or "no")?')
        today = str(datetime.date.today())
        cur.execute('INSERT INTO WeeklyHabitsACHIEVED (ID_WH, username, Data, YES_NO) VALUES '
                    '("%s", "%s", "%s", "%s")', (id, usr, today, confirmation))
        cur.connection.commit()



class Objective(DailyHabits, WeeklyHabits):
    '''
    Class that inherits the properties of DailyHabits and WeeklyHabits. Here we will define the functionalities
    that the targets have.
    '''

    def mirar_objectius(self, cur, username):
        '''
        This function will print a table with all the user's targets.

        Arguments:
        username(string) - The user name entered by the user.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        Does not return data, prints a table with the objectives of the user.
        '''

        usr = username.replace("'", "")
        cur.execute('SELECT description_O FROM Objectives WHERE username LIKE ("%s")', (usr))
        objectius = cur.fetchall()

        for objectiu in objectius:
            objective = objectiu[0].replace("'", "")
            print(objective)

    def afegir_objectiu(self, cur, username, identificador, date1, date2, objectiu):
        '''
        This function will be used to define new targets

        Arguments:
        username(string) - The user name entered by the user.
        identificador(string) - Objective name.
        dat1(string) - Target start date.
        dat2(string) - Target end date.
        objectiu(string) - Description of the objective.
        cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

        Returns:
        This function does not return anything, it only registers a new target in the database.
        '''

        usr = username.replace("'", "")
        cur.execute('INSERT INTO Objectives (username, name_O, inici, finally, description_O) VALUES '
                    '("%s", "%s", "%s", "%s", "%s")', (usr, identificador, date1, date2, objectiu))
        cur.connection.commit()
        print("Added objective")
        cur.execute('SELECT ID_O FROM Objectives WHERE username LIKE ("%s") and name_O LIKE ("%s")',
                    (username, identificador))
        return cur.fetchall()