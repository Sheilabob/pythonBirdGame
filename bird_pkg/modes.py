from colorama import init, Fore, Style
init(autoreset=True)


def show_mode_menu():
    print(Fore.CYAN + Style.BRIGHT + "\n\t\t           Mode Menu")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "\t\t|  1. Play       |  2. Study      |")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------")
    print(Fore.CYAN + Style.BRIGHT + "\t\t|  3. Scoreboard |  4. Logout     |")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------\n")
    print(Fore.CYAN + Style.BRIGHT + "\t\t|            5. Exit              |")
    print(Fore.CYAN + Style.BRIGHT + "\t\t ---------------------------------\n")

# this may have been a better fit for the questions file.  BUT, I still have a few expansion ideas: hard vs. easy mode, hints vs. no-hints mode, multiple choice vs. all the choices. etc.
