import os
from typing import Dict, List


class StakeHolder():
    def __init__(self, name: str) -> None:
        self.name = name

    def print_header(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        print((" {} ".format(self.name)).center(os.get_terminal_size().columns, "#"))

    def get_option(self, options: List[str]) -> int:
        print("[*] Options:")
        for opt in options:
            print("\t> {}".format(opt))

        while True:
            choice = input("\b[?] Choose option [1-{}]: ".format(len(options)))
            if choice.isnumeric() and 0 < int(choice) <= len(options):
                return int(choice)
            else:
                print("[!] Invalid input")

    def get_input(self, fields: List[str]) -> Dict[str, str]:
        inp: Dict[str, str] = dict()
        for field in fields:
            inp[field] = input("[?] Enter {}: ".format(field))

        return inp

    def get_confirmation(self, msg: str = "[?] Try again [y/n]: ") -> bool:
        while True:
            ch = input(msg).lower()
            if ch == 'n':
                return False
            elif ch == 'y':
                return True

    def menu(self):
        self.print_header()
        choice = self.get_option(["Login", "Back"])

        if choice == 1:
            self.login()
        elif choice == 2:
            return

    def login(self):
        raise NotImplemented

    def post_login(self):
        raise NotImplemented
