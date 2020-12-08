import django
django.setup()

import threading

from DonationSystem.settings import channel
from BloodDonation.controllers.message_controller import messages_controller


def consume():
    """
       Declaring the callbacks for all blood queues
    """
    for blood_type in ["A", "B", "O", "AB"]:
        for sign in ["+", "-"]:
            if sign == "+":
                callback = getattr(messages_controller, f"consumer_{blood_type.lower()}_pos")
            else:
                callback = getattr(messages_controller, f"consumer_{blood_type.lower()}_neg")
            channel.basic_qos(prefetch_count=8)
            # threading.Thread(target=channel.basic_consume(queue=f'{blood_type}{sign}', on_message_callback=callback))
            channel.basic_consume(queue=f'{blood_type}{sign}', on_message_callback=callback)


consume()
channel.start_consuming()
