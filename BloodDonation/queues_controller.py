import django
django.setup()

from DonationSystem.settings import channel
from BloodDonation import messages_controller


def consume():
    for blood_type in ["A", "B", "O", "AB"]:
        for sign in ["+", "-"]:
            if sign == "+":
                callback = getattr(messages_controller, f"send_messages_{blood_type.lower()}_pos")
            else:
                callback = getattr(messages_controller, f"send_messages_{blood_type.lower()}_neg")
            channel.basic_consume(queue=f'{blood_type}{sign}', on_message_callback=callback)
    channel.start_consuming()


consume()

