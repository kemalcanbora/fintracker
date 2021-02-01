from telethon import TelegramClient, events
from settings import TELEGRAM_API_ID, TELEGRAM_API_HASH
from telethon.tl.functions.channels import JoinChannelRequest

class TelegramEngine:
    @staticmethod
    def parser(user_id):
        data_list = []
        with TelegramClient("anon", TELEGRAM_API_ID, TELEGRAM_API_HASH) as client:
            for index, message in enumerate(client.iter_messages(user_id)):
                if index != 1:
                    if message.text != None and len(message.text) > 1:
                        data = {"sender_id": message.sender_id,
                                "text": message.text,
                                "date": int(message.date.timestamp())
                                }
                        print(data)
                        data_list.append(data)
                else:
                    break

        return data_list


class TelegramStreamEngine:

    client = TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH)

    def __init__(self, telegramurls):
        @self.client.on(events.NewMessage(chats=telegramurls))
        def parser(event):
            if event.message.text != None and len(event.message.text) > 1:
                data = {"sender_id": event.message.sender_id,
                        "text": event.message.text,
                        "date": int(event.message.date.timestamp()),
                        "channel": event.chat_id
                        }
                print(data)

        self.client.start()
        self.client.run_until_disconnected()


class TelegramChannelJoin:
    def __init__(self, telegramurls):
        client = TelegramClient('anon', TELEGRAM_API_ID, TELEGRAM_API_HASH)
        async def on_member_join():
            for item in telegramurls:
                await client(JoinChannelRequest(item))

        client.start()
        client.loop.run_until_complete(on_member_join())