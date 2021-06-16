from .stakeholder import StakeHolder


class University(StakeHolder):
    def __init__(self) -> None:
        super().__init__("University")

    def login(self) -> None:
        while True:
            self.print_header()
            creds = self.get_input(["email", "password"])

            if creds["email"] == "root" and creds["password"] == "toor":
                print("[*] Login successful")
                self.post_login()
                return

            else:
                print("[!] Login unsuccessful")
                try_again = self.get_confirmation()
                if not try_again:
                    return

    def post_login(self):
        self.print_header()
        action = self.get_option(["Manage Professors", "Manage Teaching Assistants", "Manage Students", "Back"])

        if action == 1:
            self.manage_professors()
        elif action == 2:
            self.manage_teachingAssitants()
        elif action == 3:
            self.manage_students()
        elif action == 4:
            return

    def manage_professors(self):
        self.print_header()
        print("=> Under Construction")

    def manage_teachingAssitants(self):
        self.print_header()
        print("=> Under Construction")

    def manage_students(self):
        self.print_header()
        print("=> Under Construction")
