supportedLanguage = ["en_US", "zh_CN"]

exitMessage = ""
illegalInput = ""
checkingNetwork = ""
didntConnectToNetwork = ""
connectToNetwork = ""

def lang():
    import main

    global exitMessage, illegalInput, checkingNetwork, didntConnectToNetwork, connectToNetwork
    

    # American English (en_US)
    if userLanguage == "en_US":
        # universal
        exitMessage = "Exited Installation."
        illegalInput = "Please input a legal option!"

        # network_check
        checkingNetwork = "Checking Network..."
        didntConnectToNetwork = "Seems that you didn't connect to network."
        
        connectToNetwork = "Do you want to connect a network? If you are SURE it's an error, enter N to skip. (Y/n)"


    # 简体中文 (zh_CN)
    elif userLanguage == "zh_CN":
        # 通用
        exitMessage = "已退出安装程序。"
        illegalInput = "请输入一个合法的选项！"

        # network_check
        checkingNetwork = "正在检查网络..."
        didntConnectToNetwork = "似乎您没有连接到网络。"

        connectToNetwork = "您要连接到网络吗？如果您*确定*这是一个错误，输入 N 以跳过。(Y/n)"