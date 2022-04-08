import npyscreen

global_bat_w = open("/tmp/install.sh", "w", encoding="utf8")
global_bat_r = open("/tmp/install.sh", "w", encoding="utf8")


class Dialog(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, name=self.name)


class LanguageSelect(npyscreen.Form):
    def create(self):
        self.keyLanguage = self.add(npyscreen.TitleText, name='Language')


class UserNameAndSuch(npyscreen.Form):
    # 包括用户名、密码、时区等
    def create(self):
        pass


def language(*args):
    # 语言选择
    t = False
    F = LanguageSelect(name="LanguageSelect")
    F.edit()
    language_list = ["zh_CN", "ja_JP"]
    for i in language_list:
        if F.keyLanguage.value == i:
            t = True
    if t:
        global_bat_w.write("export LC_ALL=%s.utf8 LANG=%s.utf8"%(F.keyLanguage.value,F.keyLanguage.value))
        global_bat_w.write("echo %s.UTF-8 UTF-8 > /etc/locale,gen")
        global_bat_w.write("locale-gen")
    else:
        Dialog(name="Unsupported Language").edit()
        print(npyscreen.wrapper_basic(language))


class Time(npyscreen.Form):
    def create(self):
        self.keyTime = self.add(npyscreen.TitleText, name='Time')


def time_select(*args):
    t=False
    F = Time(name="TimeSelect")
    for i in ["Shanghai,Tokyo"]:
        if F.keyTime.value == i:
            t=True
            break
    if t:
        global_bat_w.write("ln -sf /mnt/usr/share/zoneinfo/Asia/%s/etc/localtime"%F.keyTime.value)
    else:
        Dialog(name="Unsupported Time Zone").edit()
        time_select()


if __name__ == '__main__':
    print("Welcome to clear-arch!")
    npyscreen.wrapper_basic(language)
