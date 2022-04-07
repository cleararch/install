import npyscreen

global_bat_w = open("/tmp/install.sh", "w", encoding="utf8")
global_bat_r = open("/tmp/install.sh", "w", encoding="utf8")


class Dialog(npyscreen.Form):
    def create(self):
        self.add(npyscreen.FixedText, name=self.name)


class LanguageSelect(npyscreen.Form):
    def create(self):
        self.keyLanguage = self.add(npyscreen.TitleText, name='Language')


def language(*args):
    t = False
    F = LanguageSelect(name="LanguageSelect")
    F.edit()
    language_list = ["zh_CN", "zh_TW", "en_SG"]
    for i in language_list:
        if F.keyLanguage.value == i:
            t = True
    if t:
        global_bat_w.write("export LC_ALL=%s.utf8 LANG=%s.utf8"%(F.keyLanguage.value,F.keyLanguage.value))
    else:
        A = Dialog(name="Unsupported Language")
        A.edit()
        print(npyscreen.wrapper_basic(language))


if __name__ == '__main__':
    print("Welcome to clear-arch!")
    print(npyscreen.wrapper_basic(language))
