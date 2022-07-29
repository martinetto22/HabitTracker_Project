import classes
import datetime
from termcolor import colored
import calendar

def registre(cur):
    '''
    This function will be used to start the user registration. It will ask to enter the user name and password,
    then it will call the register function of the User class, where it will proceed to insert the data into the
    database.In this function it will also be possible to register a goal and the necessary habits to achieve the
    goal.

    Arguments:
    None

    Returns:
    None
    '''

    resposta = input("Do you want to register?")
    if resposta.lower() == "yes":
        print(colored("We start the registration procedure. Enter a user name:", 'red'))
        while True:
            username = input()
            if len(username) > 19:
                print(colored('Too long user name, please write another name', 'red'))
                print('Enter a user name:\n')
            else:
                break

        while True:
            print("Enter a password:")
            passwd = input()
            if len(passwd) > 99:
                print(colored('Too long password, please write another name', 'red'))
            else:
                break

        # INSERCIO A LA BBDD
        user = classes.User()
        user.registrar(cur, username, passwd)

        answer = input("Do you want to add a target?")
        if answer.lower() == "yes":
            identificador = input("Objective name:")
            objectiu = input("Define the objective")
            duracio = int(input("How long does the target last (in days)?"))

            data_inici = datetime.date.today()
            print("CURRENT DAY : ", data_inici)
            td = datetime.timedelta(duracio)
            data_final = data_inici + td
            date1 = data_inici.strftime("%Y-%m-%d")
            date2 = data_final.strftime("%Y-%m-%d")

            obj = classes.Objective()

            identifier_O = obj.afegir_objectiu(cur, username, identificador, date1, date2, objectiu)

            print(identifier_O[0][0])

            obj.define_dailyHabits(cur, identifier_O[0][0])
            obj.define_weeklyHabits(cur, identifier_O[0][0])

        else:
            print("At least one objective should be created at a later date.")
            print("You already have an account created, you can log in whenever you want.")
    else:
        print("Ok, bye!")


def login(cur, username, password):
    '''
    Login function. It verifies that the user exists and the password is correct.

    Arguments:
    username(string) - User name previously entered by keyboard.
    password(string) - Password previously entered by keyboard.
    cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

    Returns:
    Returns the user name if it was possible to log in. In case the name or password is wrong or does not exist, it
    will return 0.
    '''

    cur.execute('SELECT username FROM Users WHERE username LIKE ("%s") and pw LIKE ("%s")',
                (username, password))
    users = cur.fetchall()
    try:
        print(users[0][0])
        return users[0][0]

    except IndexError:
        print("Incorrect user name or password")
        return 0


def app(cur, username):
    '''
    This is the function we will be in once we have logged in. Here we will enter in an infinite loop in which we
    will be able to make use of all the possibilities. When starting session we will be in a main menu where we
    will be able to choose between a certain number of options. When we choose an option, it is executed and
    returns to the menu.

    Arguments:
    username(string) - Login user name of the logged in user.
    cur(pymysql.cursors.Cursor) - Cursor to perform SQL queries.

    Returns:
    None
    '''

    print('User name: ' + username)

    user = classes.User()
    print(1)
    obj = classes.Objective()
    print(2)
    user.daily_update(cur, username)
    print(3)
    user.weekly_update(cur, username)
    print(4)


    print("You are already inside the application.")
    while True:
        user.all_objectives_information(cur, username)
        try:
            opcio = int(input(
                "Choose one of the following options:\n1.See objectives.\n2.See daily habits.\n3.Add daily habits.\n4.Add a target.\n5.Add weekly habits.\n6.See weekly habits.\n7.Objective achieved.\n8.Statistics.\n9.Longest daily habit streak\n10.Longest weekly habit streak\n11.Have you complied with the daily routine?\n12.Have you complied with the weekly routine?\n13.Exit the program\n"))

            if opcio == 1:
                obj.mirar_objectius(cur, username)

            elif opcio == 2:
                user.llista_objectius(cur, username)
                objective_identifier = input("Enter the identifier of the target for which you want to see the habit.")
                obj.mirar_dailyHabits(cur, objective_identifier)

            elif opcio == 3:
                user.llista_objectius(cur, username)
                objective_identifier = int(input("Enter the identifier of the target for which you want to add daily habits."))
                obj.define_dailyHabits(cur, objective_identifier)


            elif opcio == 4:
                name_O = input("Objective name: ")
                objectiu = input("Define the objective")
                duracio = int(input("How long will it last in days?"))
                data_inici = datetime.date.today()
                print("CURRENT DAY : ", data_inici)
                td = datetime.timedelta(duracio)
                data_final = data_inici + td
                date1 = data_inici.strftime("%Y-%m-%d")
                date2 = data_final.strftime("%Y-%m-%d")

                obj.afegir_objectiu(cur, username, name_O, date1, date2, objectiu)

            elif opcio == 5:
                user.llista_objectius(cur, username)
                objective_identifier = int(input("Enter the identifier of the target for which you want to add weekly habits."))
                obj.define_weeklyHabits(cur, objective_identifier)

            elif opcio == 6:
                user.llista_objectius(cur, username)
                objective_identifier = input("Enter the identifier of the target for which you want to see the habit.")
                obj.mirar_weeklyHabits(cur, objective_identifier)

            elif opcio == 7:
                user.llista_objectius(cur, username)
                objectiu_id = input("Enter the identifier of the achieved objective: ")
                user.obj_assolit(cur, objectiu_id)

            elif opcio == 8:
                user.inicial_final_objectives_dates(cur, username)
                user.assolits_no_assolits(cur, username)

            elif opcio == 9:
                user.llista_objectius(cur, username)
                objective_identifier = input("Enter the identifier of the target for which you want to see the habit.")
                obj.mirar_dailyHabits(cur, objective_identifier)
                dailyHabit_identifier = int(input("Introduce the daily habit identifiers to see the longest streak or introduce any character to return to the main menu"))
                obj.Dlongest_run_streak(cur, dailyHabit_identifier)

            elif opcio == 10:
                user.llista_objectius(cur, username)
                objective_identifier = input("Enter the identifier of the target for which you want to see the habits.")
                obj.mirar_weeklyHabits(cur, objective_identifier)
                weekyHabit_identifier = int(input("Introduce the weekly habit identifiers to see the longest streak or introduce any character to return to the main menu"))
                obj.Wlongest_run_streak(cur, weekyHabit_identifier)

            elif opcio == 11:
                user.llista_objectius(cur, username)
                objective_identifier = input("Enter the identifier of the target.")
                obj.mirar_dailyHabits(cur, objective_identifier)
                dailyHabit_identifier = int(
                    input("Introduce the daily habit identifier to confirm that you have performed the task"))
                obj.check_dailyHabit(cur, dailyHabit_identifier, username)

            elif opcio == 12:
                curr_date = datetime.date.today()
                week_day = calendar.day_name[curr_date.weekday()]
                if week_day == 'Sunday':
                    user.llista_objectius(cur, username)
                    objective_identifier = input("Enter the identifier of the target.")
                    obj.mirar_weeklyHabits(cur, objective_identifier)
                    weeklyHabit_identifier = int(
                        input("Introduce the weekly habit identifier to confirm that you have performed the task"))
                    obj.check_weeklyHabit(cur, weeklyHabit_identifier)
                else:
                    print(colored('\nYou cannot change the weekly habit yet. You can only enter that you have completed it on Sunday.\n', "red"))

            elif opcio == 13:
                print(colored("\n\nBYE!", "cyan"))
                print(colored("-" * 100 + "\n", "cyan"))
                print(colored("-" * 100 + "\n\n", "cyan"))
                break
            else:
                pass
        except:
            print(colored('\n\nYou have entered something wrong, please try again.\n\n', 'red'))