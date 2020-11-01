import dill
'''
def send_messages(queue):
    (while queue != null)
        request = queue[0]
        for donor in Donor.object.all()
            if (donor.blood_type == request.blood_type && (abs_value(donor.location - request.location) < 15 000))
                 send_message(donor)


'''

def send_messages_o_neg(ch, method, properties, body):
    request = dill.loads(body)






#TODO : Other channels ...