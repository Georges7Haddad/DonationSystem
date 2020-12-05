from django_telethon_session.sessions import DjangoSession
from telethon import TelegramClient

# Telethon
api_id = 2144908
api_hash = '4e22faa1183ea0ced9ddd9f173c7ee8d'
telethon_client = TelegramClient(DjangoSession("BloodDonation"), api_id, api_hash)


async def start_telethon_client():
    telethon_client.start()
