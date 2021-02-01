## What is Fintracker ?
Fintecher simply streaming data from information sources where cryptocurrencies are spoken. Like Reddit, Twitter, Telegram

## How can I use it ?
 You need some API key;
 - Twitter API
 - Telegram API
 - Reddit API

## Problems and Solutions
 - If you want to use TelegramSteams firstly you need to join Telegram channel manuel or run
"TelegramChannelJoin" function
 -  Twitter API run every 60 sec
 -  app.py have a little problem about Threading and processing you need to fix     telegram_crawler = TelegramStreamEngine(telegramurls) parts.

