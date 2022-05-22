import os

import npyscreen

global_bat_w = open("/tmp/install.sh", "w", encoding="utf8")
global_bat_r = open("/tmp/install.sh", "w", encoding="utf8")


class Dialog(npyscreen.Form):
    # 提示，需要的时候就创建一个
    def create(self):
        self.add(npyscreen.FixedText, name=self.name)


class LanguageSelect(npyscreen.Form):
    # 语言选择
    def create(self):
        self.keyLanguage = self.add(npyscreen.TitleText, name='Language')


class User(npyscreen.Form):
    # 用户设置
    def create(self):
        self.user = self.add(npyscreen.TitleText, name='user')
        self.password = self.add(npyscreen.TitleText, name='password')
        self.shell = self.add(npyscreen.TitleText, name="shell")


class install_kernel(npyscreen.Form):
    # 内核安装
    def create(self):
        self.kernel = self.add(npyscreen.TitleText, name="Kernel Name")

    def install(self):
        if self.kernel.value == "linux-clear":
            global_bat_w.write("pacm install-mode source linux-clear")
        elif self.kernel.value == "linux-zen":
            global_bat_w.write("pacstrap /mnt linux-zen")
        else:
            Dialog(name="Can't found this kernel")


class Part(npyscreen.Form):
    # 分区设置
    def create(self):
        self.show_part = self.add(npyscreen.TitleText, name="Show part(use fdisk)(Press Y to show):")
        self.part = self.add(npyscreen.TitleText, name="Part Create(Format: /dev/n type size(Mib))")
        self.tree = self.add(npyscreen.TitleText, name="Part Tree(Format:/dev/n mount_point")
        self.ok = self.add(npyscreen.TitleText, name="Finally Part Setting(Press 'Y')")
        self.part_tree = npyscreen.Pager(os.popen("fdisk -l"))


def part_create(*args):
    label_made=False
    Dialog("Warling:In Next Step,We Will Delete All Of Your Data")
    ShowPart = False
    F = Part(name="Build Part")
    F.edit()
    if F.show_part.value == "Y":
        F.add(F.part_tree)
        ShowPart = True
        part_create()
    if not ShowPart:
        if not label_made:
            os.system("parted mklable gpt")
            label_made=True
        part = F.part.value

        os.system("parted mkpart")


def language(*args):
    # 语言选择
    t = False
    F = LanguageSelect(name="LanguageSelect")
    F.edit()
    language_list = ["zh_CN", "ja_JP", "en_HK"]
    for i in language_list:
        if F.keyLanguage.value == i:
            t = True
    if t:
        global_bat_w.write("export LC_ALL=%s.utf8 LANG=%s.utf8" % (F.keyLanguage.value, F.keyLanguage.value))
        global_bat_w.write("echo %s.UTF-8 UTF-8 > /etc/locale,gen")
        global_bat_w.write("locale-gen")
    else:
        Dialog(name="Unsupported Language").edit()
        print(npyscreen.wrapper_basic(language))


class Time(npyscreen.Form):
    def create(self):
        self.keyTime = self.add(npyscreen.TitleText, name='Time')


def time_select(*args):
    t = False
    F = Time(name="TimeSelect")
    for i in ["Shanghai,Tokyo"]:
        if F.keyTime.value == i:
            t = True
            break
    if t:
        global_bat_w.write("ln -sf /mnt/usr/share/zoneinfo/Asia/%s/etc/localtime" % F.keyTime.value)
    else:
        Dialog(name="Unsupported Time Zone").edit()
        time_select()


def user_select(*args):
    F = User(name="User")
    F.edit()
    T = False
    for i in ["bash", "zsh", "fish"]:
        if F.shell.value == i:
            T = True
            break
    if T:
        global_bat_w.write("useradd -m -d /home/" + F.user.value + " " + F.user.value + "-s " \
                           + F.shell.value + " ; echo -e '" + F.password.value + "'|passwd ")
    else:
        Dialog(name="ShellError").edit()
        user_select()


if __name__ == '__main__':
    print("Welcome to clear-arch!")
    npyscreen.wrapper_basic(user_select)
    npyscreen.wrapper_basic(language)
