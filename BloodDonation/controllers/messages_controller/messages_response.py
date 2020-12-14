import django
django.setup()

import os
import re
from asgiref.sync import async_to_sync
from telethon import events
from BloodDonation.models import Request, Donor
from DonationSystem.telethon_client import telethon_client
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"

# todo: 1. Improve response messages
#       2. Improve patterns
@async_to_sync
@telethon_client.on(events.NewMessage(pattern='Unsubscribe|unsubscribe|إلغاء الاشتراك'))
async def unsubscribe_handler(event):
    """
       Handles the response of unsubscribe by removing the donor from the DB
       Parameters:
           event: New Message Event
    """
    entity = await telethon_client.get_entity(event.chat_id)
    donor = Donor.objects.get(phone_number=entity.phone[3:])
    donor.delete()
    await event.respond("We're sorry to see you leave.\nWe successfully removed you from our database.")


@async_to_sync
@telethon_client.on(events.NewMessage(pattern='confirmed|Confirmed|مؤكد'))
async def confirmation_handler(event):
    """
       Handles the response of confirmed by incrementing the number of confirmed users in a request
       Also handles the same user confirming multiple times
       Parameters:
           event: New Message Event
    """
    confirmation_count = 0
    request_id = 0
    entity = await telethon_client.get_entity(event.chat_id)
    async for message in telethon_client.iter_messages(entity.phone):
        if message.text == "Confirmed" or message.text == "confirmed" or message.text == "مؤكد":
            confirmation_count += 1
            if confirmation_count > 1:
                await event.respond("Thank you, but you have already confirmed you're going to donate.")
                return
        if "Patient" in message.text:
            request_id = re.findall("\d", message.text)
            request_id = int("".join(request_id))
            break

    try:
        request = Request.objects.get(pk=request_id)
        request.users_confirmations = request.users_confirmations + 1
        request.save()
        await event.respond('Thank you!')
    except Request.DoesNotExist:
        await event.respond(f'Thank you, but the request for patient {request_id} has been fulfilled')

telethon_client.add_event_handler(unsubscribe_handler)
telethon_client.add_event_handler(confirmation_handler)
telethon_client.run_until_disconnected()
