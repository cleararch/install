import os, json
import npyscreen

# 初始化封装器
class install(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", welcome, name="Welcome")
        self.addForm("LANGUAGE", language, name="Select Your Language")


# 欢迎
class welcome(npyscreen.ActionForm):
    def create(self):
        self.name = "Welcome"
        self.text = self.add(npyscreen.TitleFixedText, name="Welcome To Clear Arch Installer!")

    def on_ok(self):
        self.parentApp.switchForm("LANGUAGE")

    def on_cancel(self):
        exit()
    
# 选择语言
# self.select.value[0]
class language(npyscreen.ActionForm):
    def create(self):
        self.name = "Select Your Language"
        self.select = self.add(npyscreen.TitleSelectOne, name="Language", values=["zh_CN", "en_HK", "ja_JP"])

    def on_ok(self):
        self.parentApp.switchForm("")

    def on_cancel(self):
        self.parentApp.switchFormPrevious()


# 运行
if __name__ == "__main__":
    install().run()