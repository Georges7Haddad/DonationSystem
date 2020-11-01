from BloodDonation.messages_controller import *
from DonationSystem.settings import channel

channel.basic_consume(queue='O-', auto_ack=True, on_message_callback=send_messages_o_neg)
#TODO : Other channels ...
channel.start_consuming()


