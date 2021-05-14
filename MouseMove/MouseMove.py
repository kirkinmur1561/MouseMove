import time
import os
import pyautogui

# 1. Отктройте http://цифровизацияшкол.рф/ и авторизуйтесь
# 2. Отктройте страницу http://цифровизацияшкол.рф/mailing и выберите нужную категорию
# 3. С помощью программы "Показать позицию курсора" определите координаты нужных кнопок и исправьте их ниже
# 4. Можно запускать этот скрипт. Установите английскую раскладку
#    и сначала оставьте в списке электронных адресов один, чтобы убедиться в
#    правильной работе:)

ADD_EMAIL_BUTTON = (2290, 432)  # Координаты кнопки "Добавить e-mail"
EMAIL_FIELD      = (2720, 280) # Координаты поля Email
ADD_BUTTON       = (3066, 422) # Координаты кнопки "Добавить"

##### Все что ниже этой строки лучше не трогать:) #####

# Ждем 5 секунд прежде чем начать работу
time.sleep(5)

# Открываем файл emails.txt где каждая строка это отдельный email
with open("emails.txt", "r") as file:
    for email in file:
        print(email.strip())
        # Жмем кнопку "Добавить e-mail"
        pyautogui.click(ADD_EMAIL_BUTTON)
        time.sleep(1)

        # Жмем на поле Email
        pyautogui.click(EMAIL_FIELD)
        time.sleep(1)

        # Очищаем поле, если там что-то было
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(0.1)
        pyautogui.press('delete')
        time.sleep(0.1)

        # Вписываем очередной email в поле Email
        pyautogui.write(email.strip())
        time.sleep(0.8)

        # Жмем кнопку "Добавить"
        pyautogui.click(ADD_BUTTON)
        time.sleep(0.9)

        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('tab')
        time.sleep(0.3)
        pyautogui.press('Enter')
        time.sleep(1)

        os.system('cls||clear')
