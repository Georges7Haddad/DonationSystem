from telethon import events

from DonationSystem.telethon_client import telethon_client


@telethon_client.on(events.NewMessage(pattern='confirmed|Confirmed'))
async def handler(event):
    await event.respond('Thank you!')

telethon_client.add_event_handler(handler)
telethon_client.run_until_disconnected()
