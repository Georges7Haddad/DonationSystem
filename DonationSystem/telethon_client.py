from telethon import TelegramClient, sync, events

api_id = 2144908
api_hash = '4e22faa1183ea0ced9ddd9f173c7ee8d'
telethon_client = TelegramClient("BloodDonation", api_id, api_hash)


telethon_client.start()
print(telethon_client.get_me().stringify())
