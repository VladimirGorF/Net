
import easygui

# easygui.msgbox("Hello Word!","welcome","Hello")

# out = easygui.ynbox(msg = "Я вам нравлюсь?",title = "Признание")
# print("Ваш выбор:", out)


# out = easygui.buttonbox(choices =('One','Two','Three','Four'))
# print("Ваш выбор:", out)
def enter_name():
    out = easygui.enterbox(msg="Пожалуйста, введите Ваше имя:",title = "Вход в чат.")
    print(out)

def no_name():
    easygui.msgbox("Вы не представились, поэтому мы будем звать вас Бобби", "ЧАТ")

def mess(message):
    easygui.msgbox(message, "ЧАТ")