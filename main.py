import pymysql
from termcolor import colored
import app


'''
Here is where the program execution starts. We start with an infinite loop. First of all, when running the
program, it will ask us if we want to register or log in. To log in we must enter "log in" or "start" and to
register we must enter "register" or "sign up". When we have specified what we want, we will proceed with the
registration or go on to login.
'''


def inici(cur):
    while True:
        print("\n\n")
        print(colored("-" * 100, "red"))
        print(colored("\n\nWelcome!", "red"))

        opcio = input("Want to sign up or log in? ")
        flag = 0

        for i in paraules_iniciar_sessio:
            if i in opcio:
                flag = 1
                username = input("Enter your user name: ")
                passwd = input("Introduce the password: ")
                success = app.login(cur, username, passwd)
                if success == 0:
                    break
                else:
                    app.app(cur, success)

        if flag == 0:
            for i in paraules_registre:
                if i in opcio:
                    print("Welcome, we start with the registration.")
                    app.registre(cur)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', user='root', passwd=None, db='mysql', charset='utf8')
    cur = conn.cursor()
    cur.execute("USE HabitsProject")

    paraules_iniciar_sessio = ["log in", "start"]
    paraules_registre = ["register", "sign up"]

    inici(cur)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
