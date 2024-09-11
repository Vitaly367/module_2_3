# Создаем фунцию send_email
def send_email(message, recipient, *, sender="university.help@gmail.com"):

    # Проверка на корректоность email отправителя и получателя
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print("Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return
    if "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print("Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка отправления самому себе
    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print("Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')

