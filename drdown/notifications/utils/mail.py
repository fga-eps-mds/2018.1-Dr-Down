from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import requests
try:
    from utility.email import EmailEnvironment
except ImportError:
    raise ImportError('Could not find the email configuration file')

DRDOWN_EMAIL = "equipe.drdown@gmail.com"


def __get_mail_config():
    try:
        return EmailEnvironment()
    except NameError:
        print("Mail is operating in fallback mode, no configuration provided!")
        return {'url': "", 'api': "", 'domain': "", 'email': ""}


def send_message(user_list, subject, text):

    mail_config = __get_mail_config()

    data = {
        "from": DRDOWN_EMAIL,
        "bcc": user_list,
        "subject": subject,
        "text": text
    }

    return requests.post(
        mail_config['url'],
        auth=("api", mail_config['api']),
        data=data,
    )


def send_event_creation_message(user_list, event):

    subject = _("DRDOWN: A new event has been created!")
    text = _(
        "The Dr. Down team would like to invite you to a event."
        "Here are the details:\n"
        "\tEvent name: %(name)s - Date and time: %(date)s at %(time)s\n"
        "\tLocation: %(location)s\n"
        "For more information, please visit the Dr. Down website."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        ) % {
            'name': event.name,
            'date': event.date,
            'time': event.time,
            'location': event.location
        }

    send_message(user_list, subject, text)
