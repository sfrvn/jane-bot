## Jane-bot

This is a Telegram bot that helps you search for work using the [HeadHunter API](https://dev.hh.ru). Now she is looking for jobs only for my girlfriend, but it's very easy and fast to modify.

### How to install

To get data from [HeadHunter](https://hh.ru) no key required.  
To start the bot, look in Telegram [@jane_whybot](https://t.me/jane_whybot). If you live in Russia (or in another country where telegram is blocked), you may need a proxy or VPN.  
To make the code work on your computer, you will have to create your bot and get a token. To do this, write [@BotFather](https://t.me/BotFather).  

After receiving the token, you need to create in the root of the project `.env`-file where you assign the value of your token to the variable `TELEGRAM_BOT_TOKEN`. After that run `main.py` in your terminal, and the bot will start its work until you stop the script execution.  
My bot was hosted on [Heroku](https://heroku.com), if desired, you can also do it, and run the script on your PC is not required.

### Startup example

``
$ python3 main.py
``

You can also watch a video-demo of the bot [here](https://vimeo.com/364302218).

## Джейн-бот (ru)

Это Telegram-бот, который помогает искать работу с помощью [HeadHunter API](https://dev.hh.ru). Сейчас он ищет вакансии только для моей девушки, но его очень легко и быстро можно модифицировать.

### Как установить

Для получения данных с [HeadHunter](https://hh.ru) ключ не требуется.  
Чтобы запустить бота, найдите в Telegram [@jane_whybot](https://t.me/jane_whybot). Если вы живёте в России (или в другой стране, где Telegram заблокирован), может потребоваться прокси или VPN.  
Чтобы код работал на вашем компьютере, придётся создать своего бота и получить токен. Для этого напишите [@BotFather](https://t.me/BotFather).

После получения токена необходимо в корне проекта создать .env-файл, в котором вы присвоите значение своего токена переменной `TELEGRAM_BOT_TOKEN`. После этого запустите файл в терминале `main.py`, и бот начнёт свою работу, пока вы не остановите выполнение скрипта.  
Мой бот хостился на [Heroku](https://heroku.com), при желании вы тоже можете это сделать, и запуск скрипта на вашем ПК не потребуется.

### Пример запуска

``
$ python3 main.py
``

Вы также можете посмотреть видео-демонстрацию работы бота [здесь](https://vimeo.com/364302218).


UPD: Я больше не пишу ботов, этот бот больше не используется. Репозиторий отправляю в архив
