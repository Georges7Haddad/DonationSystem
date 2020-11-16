from DonationSystem.settings import channel
from BloodDonation.messages_controller import send_messages_o_neg


# def consume():
#     for blood_type in ["A", "B", "O", "AB"]:
#         for sign in ["+", "-"]:
#             if sign == "+":
#                 callback = getattr(messages_controller, f"send_messages_{blood_type.lower()}_pos")
#             else:
#                 callback = getattr(messages_controller, f"send_messages_{blood_type.lower()}_neg")
#             channel.basic_consume(queue=f'{blood_type}{sign}', auto_ack=True, on_message_callback=callback())
#     channel.start_consuming()


# consume()

channel.basic_consume(queue='O-', auto_ack=True, on_message_callback=send_messages_o_neg)
channel.start_consuming()
