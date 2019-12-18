<h1> Email sender </h1>

Данный скрипт написан в учебных целях для отрпавки электронной почты

<h2> Запуск скрипта </h2>

Убедитесь, что директория в которую вы распковали архив, имеет доступ к интернет и содержит следующие файлы:

Название файла      | Содержание файла
--------------------|----------------------
template_handler.py | Файл с обработанным шаблоном письма
mail_sender.py      | Функция отправки письма
README.md           | Данный файл
config.py           | логин и пароль к почтовому ящику, адресаты

В файле `config.py`
``` python

LOGIN = 'логин для почтового ящик с которого отправляем сообщение'
PASSWORD = 'пароль для почтового ящика с которого отправляем сообщение'

EMAIL_FROM = 'адрес почтового ящика с которого отправляем сообщение'
EMAIL_TO = 'адрес почтового ящика на который отправляем сообщение'

```

<h2> Требования </h2>

Запуск данного скрипта требует установки Python 3.7.4

<h2>Запуск</h2>

Запуск осуществляется через консоль командой: 

    
    python mail_sender.py

