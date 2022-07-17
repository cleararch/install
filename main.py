import os
import multi_lang
supportedLanguage = ["en_US", "zh_CN"]

# 欢迎
def welcome():
    os.system("clear") # 清屏
    print(
        "Welcome to the Clear Arch installer!\n"
        "To learn how to install Clear Arch, please visit https://cleararch.vercel.app/ for help.\n")

    select_language()


# 选择语言
def select_language():
    global lang
    print("Supported language:")
    print(supportedLanguage, sep = ", ")

    while True:
        userInputLanguage = input("Which language do you want to use: ")
        if userInputLanguage in supportedLanguage:
            lang=multi_lang.name(userInputLanguage)
            network_check()
            break
        else:
            print("Please input a legal option!")


# 检测网络连接状态
def network_check():
    print(lang.checkingNetwork)

    pingResult = os.popen("ping 9.9.9.9 -c 1").close()
    if pingResult == 512: # ping 失败后会返回 512
        print() # 加 \n 会换两行，加在下条有空格
        print(lang.didntConnectToNetwork)

        while True:
                userInput = input(lang.connectToNetwork)
                if userInput in ['y', 'Y', '']:
                    connect_network()
                    break
                elif userInput in ['n', 'N']:
                    #partition()
                    break
                    exit()
                else:
                    print(lang.illegalInput)
    else:
        #partition()
        exit


# 连接网络
def connect_network():
    # 列出可用网络
    print(lang.listingNetwork)
    print()
    os.system("nmcli device wifi list")
    print()

    # 将重新检测网络部分放入函数，便于后续操作
    def check_again():
        global result

        print()
        print(lang.recheckNetwork) # 检测连接

        pingResult = os.popen("ping 9.9.9.9 -c 1").close()
        if pingResult == 512:
            print()
            print(lang.recheckNetworkFailed)
            result = False
        else:
            result = True
            print(lang.recheckNetworkSuccess)


    while True:

        userInputSSID = input(lang.inputNetworkSSID)
        if userInputSSID == "":
            print(lang.emptyNetworkSSID)

        else:
            userInputPwd = input(lang.inputNetworkPwd)
            if userInputPwd == "": # 无密码情况
                os.system("nmcli device wifi connect %s" %(userInputSSID))
                check_again()
                if result:
                    #partition()
                    break
                    exit

            else: # 包含密码
                os.system("nmcli device wifi connect %s password %s" %(userInputSSID, userInputPwd))
                check_again()
                if result:
                    #partition()
                    break
                    exit

        
if __name__ == '__main__':
    welcome()
