supportedLanguage = ["en_US", "zh_CN"]

class name:
    def __init__(self, userLanguage):
    # American English (en_US)
        if userLanguage == "en_US":
            # universal
            self.exitMessage = "Exited Installation."
            self.illegalInput = "Please input a legal option!"

            # network_check
            self.checkingNetwork = "Checking Network..."
            self.didntConnectToNetwork = "Seems that you didn't connect to network."
            self.connectToNetwork = "Do you want to connect a network? If you are SURE it's an error, enter N to skip. (Y/n) "

            # connect_network
            self.listingNetwork = "Listing Network..."
            self.recheckNetwork = "Rechecking Network..."
            self.recheckNetworkFailed = "Connect failed. Please try again."
            self.recheckNetworkSuccess = "Connect successfully."
            self.inputNetworkSSID = "Please input the network SSID you want to connect: "
            self.emptyNetworkSSID = "Please input a SSID!"
            self.inputNetworkPwd = "Please input password: "


        # 简体中文 (zh_CN)
        elif userLanguage == "zh_CN":
            # 通用
            self.exitMessage = "已退出安装程序。"
            self.illegalInput = "请输入一个合法的选项！"

            # network_check
            self.checkingNetwork = "正在检查网络..."
            self.didntConnectToNetwork = "似乎您没有连接到网络。"
            self.connectToNetwork = "您要连接到网络吗？如果您*确定*这是一个错误，输入 N 以跳过。(Y/n) "

            # connect_network
            self.listingNetwork = "正在列出网络..."
            self.recheckNetwork = "正在重新检测网络..."
            self.recheckNetworkFailed = "连接失败，请再试一次。"
            self.recheckNetworkSuccess = "连接成功。"
            self.inputNetworkSSID = "请输入您想要连接网络的 SSID: "
            self.emptyNetworkSSID = "请输入一个 SSID！"
            self.inputNetworkPwd = "请输入密码: "