import os

exitMessage = "Exited Installation."
illegalInput = "Please input a legal option!"


def welcome():
    print(
        "Welcome to Clear Arch Installation!\n"
        "To learn how to install Clear Arch, please go to https://cleararch.vercel.app/ for help.\n")
    while True:
        userInput = input("Do you want to continue? (Y/n)")
        if userInput in ['y', 'Y', '']:
            network_check()
            break
        elif userInput in ['n', 'N']:
            print(exitMessage)
            break
        else:
            print(illegalInput)


def network_check():
    print("Checking Network...")
    pingResult = os.popen("ping 9.9.9.9 -c 1").close()
    if pingResult == 512:
        print("Seems that you didn't connect to the network.\n"
        "You can exit and check the network connection, or just ignore and continue.\n")

        while True:
            userInput = input("Do you want to continue? (y/N)")
            if userInput in ['y', 'Y']:
                print("114514")
                break
            elif userInput in ['n', 'N', '']:
                print(exitMessage)
                break
            else:
                print(illegalInput)

    else:
        print("114514")


if __name__ == '__main__':
    welcome()