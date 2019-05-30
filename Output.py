# By Ethan Wentworth & Jacob H.
# TODO add message length check
import twilio
from twilio.rest import Client


def list_to_string(list):
    # str = ",".join(list)
    str1 = "".join(str(e) for e in list)
    return str1


def main(list1, list2, input_dict):
    print(list1)
    str1 = list_to_string(list1)
    str2 = list_to_string(list2)
    Fpart = "This many characters have been changed, "
    Mpart = ". Key: + is added, - is removed. These were the characters that were added, or removed "
    # list1 is each character added

    # list2 is number total

    client = Client(input_dict["sid"], input_dict["authtok"])

    message = client.messages.create(
        body=(Fpart + str2 + Mpart + str1),
        from_=input_dict["twinum"],
        to=input_dict["destnum"],
    )
    print(message.sid)
