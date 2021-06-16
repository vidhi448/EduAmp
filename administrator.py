from .stakeholder import StakeHolder
from mysql.connector import connect, Error
import random


class Administrator(StakeHolder):
    def __init__(self) -> None:
        super().__init__("Administrator")

        self.connection = connect(host="localhost", user="root", password="toor", database="DBMS")
        self.cursor = self.connection.cursor()

    def login(self) -> None:
        while True:
            self.print_header()
            creds = self.get_input(["email", "password"])

            self.cursor.execute("SELECT ID FROM USERS WHERE EMAIL=%(email)s AND PASSWORD=%(password)s", {
                "email": creds["email"],
                "password": creds["password"]
            })
            auth = self.cursor.fetchall()

            if len(auth) > 0:
                self.cursor.execute("SELECT ID FROM ADMINISTRATOR WHERE ID=%(uid)s", {
                    "uid": auth[0][0]
                })
                auth_uni = self.cursor.fetchall()

                if len(auth_uni) > 0:
                    print("[*] Login successful")
                    self.post_login()
                    return

            print("[!] Login unsuccessful")
            try_again = self.get_confirmation()
            if not try_again:
                return

    def post_login(self):
        while True:
            self.print_header()
            action = self.get_option(["Manage Universities", "Manage Users", "Back"])

            if action == 1:
                self.manage_university()
            elif action == 2:
                self.manage_users()
            elif action == 3:
                return

    def manage_university(self):
        while True:
            self.print_header()
            action = self.get_option(["Create University", "Remove University", "Back"])

            if action == 1:
                self.create_university()
            elif action == 2:
                self.remove_university()
            elif action == 3:
                return

    def manage_users(self):
        self.print_header()
        print("=> Under Construction")

    def create_university(self):
        while True:
            self.print_header()
            data = self.get_input(["name", "email", "password", "university location", "university info"])

            uid = random.randint(100000000, 999999999)

            self.cursor.execute("SELECT * FROM USERS WHERE EMAIL=%(email)s", {
                "email": data["email"]
            })
            existing_users = self.cursor.fetchall()
            if len(existing_users) > 0:
                print("[!] User with provided email exists")

                try_again = self.get_confirmation()
                if try_again:
                    continue
                else:
                    break

            try:
                self.cursor.execute("INSERT INTO USERS (ID, NAME, EMAIL, PASSWORD) VALUES (%(uid)s, %(name)s, %(email)s, %(password)s)", {
                    "uid": uid,
                    "name": data["name"],
                    "email": data["email"],
                    "password": data["password"]
                })

                self.cursor.execute("INSERT INTO UNIVERSITY (ID, LOCATION, INFO, EDUCAMP_RANKING) VALUES (%(uid)s, %(location)s, %(info)s, %(ranking)s )", {
                    "uid": uid,
                    "location": data["university location"],
                    "info": data["university info"],
                    "ranking": 1500
                })

                self.connection.commit()
            except Error as err:
                print("[!] Runtime Error: " + str(err))

                try_again = self.get_confirmation()
                if try_again:
                    continue
                else:
                    break

            add_another_uni = self.get_confirmation("[?] Want to add another university [y/n]: ")
            if add_another_uni:
                continue

            break

    def remove_university(self):
        return
