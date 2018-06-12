from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import requests
try:
    from utility.email_config import EmailEnvironment
except ImportError:
    pass

DRDOWN_EMAIL = "equipe.drdown@gmail.com"


def __get_mail_config():
    try:
        return EmailEnvironment()
    except NameError:
        print("Mail is operating in fallback mode, no configuration provided!")
        return {'url': "https://api.mailgun.net", 'api': "", 'domain': "",
                'email': ""}

def send_message(user_list, subject, text):

    mail_config = __get_mail_config()

    data = {
        "from": DRDOWN_EMAIL,
        "to": user_list,
        "subject": subject,
        "text": text
    }

    if settings.IS_TESTING:
        return data

    request = requests.post(
        mail_config['url'],
        auth=("api", mail_config['api']),
        data=data,
    )

    # Testing only. Remove it
    print ('Status: {0}'.format(request.status_code))
    print ('Body:   {0}'.format(request.text))



def send_event_creation_message(user_list, event):

    subject = str(_("DRDOWN: A new event has been created!"))
    text = str(_(
        "The Dr. Down team would like to invite you to a event."
        "Here are the details:\n"
        "\tEvent name: %(name)s - Date and time: %(date)s at %(time)s\n"
        "\tLocation: %(location)s\n"
        "For more information, please visit the Dr. Down website."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        )) % {
            'name': event.name,
            'date': event.date,
            'time': event.time,
            'location': event.location
        }

    send_message(user_list, subject, text)


def send_appointment_cancel_message(user, requests):

    subject = str(_("DRDOWN: Your medical appointment was canceled."))
    text = str(_(
        "Dear Sir / Madam, we would like to inform you that your request\n "
        " has been rejected for the following reason:"
        "\t%(reason)s -\n"
        "For more information, please visit the Dr. Down website."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        )) % {
            'reason': requests.observation,
        }

    send_message(user.email, subject, text)


def send_appointment_sucess_message(user):

    subject = str(_("DRDOWN: Your request for consultation was accepted!"))
    text = str(_(
        "Dear Sir / Madam, we would like to inform you that your request\n "
        "was accepted. Please go to Dr. Down to confirm the request.\n"
        "For more information, please visit the Dr. Down website."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        ))

    send_message(user.email, subject, text)
