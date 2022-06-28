import os

exitMessage = "Exited Installation." # 退出后消息
illegalInput = "Please input a legal option!" #输入无效选项
splitLine = "===" # 分割线（改成 \n 可以换行）


# 欢迎
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


# 检测网络连接状态
def network_check():
    print("Checking Network...")

    pingResult = os.popen("ping 9.9.9.9 -c 1").close()
    if pingResult == 512: # ping 失败后会返回 512
        print(splitLine)
        print("Seems that you didn't connect to network.")
        while True:
                userInput = input("Do you want to connect a network? If you are SURE it's an error, enter N to skip. (Y/n)")
                if userInput in ['y', 'Y', '']:
                    connect_network()
                    break
                elif userInput in ['n', 'N']:
                    partition()
                    break
                else:
                    print(illegalInput)
    else:
        partition()


# 连接网络
def connect_network():
    # 列出可用网络
    print("Listing Network...\n")
    os.system("nmcli device wifi list")
    print(splitLine)

    # 将重新检测网络部分放入函数，便于后续操作
    def check_again():
        global result # 定义全局变量以传出判断结果

        print(splitLine)
        print("Rechecking Network...") # 检测连接

        pingResult = os.popen("ping 9.9.9.9 -c 1").close()
        if pingResult == 512:
            print("Connection failed. Please try again.")
            result = False
        else:
            result = True
            print("Success!")


    while True:

        userInputSSID = input("Please input the network SSID you want to connect: ")
        if userInputSSID == "":
            print("Please input a SSID!")

        else:
            userInputPwd = input("Please input password: ")
            if userInputPwd == "": # 无密码情况
                os.system("nmcli device wifi connect %s" %(userInputSSID))
                check_again()
                if result:
                    partition()
                    break

            else: # 包含密码
                os.system("nmcli device wifi connect %s password %s" %(userInputSSID, userInputPwd))
                check_again()
                if result:
                    partition()
                    break


# 分区
def partition():
    while True:
        userInput = input("Do you want to partition the disk? Enter Y to launch cfdisk, or N to skip. (Y/n)")
        if userInput in ['y', 'Y', '']:
            checkingExit = os.system("cfdisk")
            if checkingExit == 0: # os.system 进程结束后会返回 0，借此判断 cfdisk 退出情况
                formatting()
            break
        elif userInput in ['n', 'N']:
            formatting()
            break
        else:
            print(illegalInput)


# 格式化
def formatting():
    EFI=os.path.exists("/sys/firmware/efi")
    print(os.system("fdisk -l"))
    print("Choose the Partition")
    if EFI == True:
        userInput = input("Please input your EFI partition:")

    else:
        userInput = input("Where do you want to install the system?")

        
if __name__ == '__main__':
    welcome()
