from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.template import loader
from django.db.models import Q

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


def __get_html(template_name, context):

    template = loader.get_template(template_name)

    return template.render(context)


def send_message(user_list, subject, text, html=""):

    mail_config = __get_mail_config()

    data = {
        "from": DRDOWN_EMAIL,
        "to": DRDOWN_EMAIL,
        "bcc": user_list,
        "subject": subject,
        "text": text,
        "html": html,
    }

    request = requests.post(
        mail_config['url'],
        auth=("api", mail_config['api']),
        data=data,
    )

    return request


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

    html = __get_html(
        template_name="notifications/emails/create_event.html",
        context={'object': event, }
    )

    return send_message(user_list, subject, text, html)


def send_event_update_message(user_list, event):

    subject = str(_("DRDOWN: The %(name)s has changed.")) % {
        'name': event.name,
    }

    text = str(_(
        "A event created on our site has been changed, it is of high"
        "importance to go check its details again."
        "Here are some of the new details:\n"
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

    html = __get_html(
        template_name="notifications/emails/update_event.html",
        context={'object': event, }
    )

    return send_message(user_list, subject, text, html)


def send_appointment_cancel_message(patient, requests):

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

    user_list = [
        patient.user.email,
    ]

    if patient.responsible is not None:
        user_list.append(patient.responsible.user.email)

    html = __get_html(
        template_name="notifications/emails/appointment_canceled.html",
        context={'object': requests, }
    )

    return send_message(user_list, subject, text, html)


def send_appointment_sucess_message(patient, requests):

    subject = str(_("DRDOWN: Your request for consultation was accepted!"))
    text = str(_(
        "Dear Sir / Madam, we would like to inform you that your request\n "
        "was accepted. Please go to Dr. Down to confirm the request.\n"
        "For more information, please visit the Dr. Down website."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        ))

    user_list = [
        patient.user.email,
    ]

    if patient.responsible is not None:
        user_list.append(patient.responsible.user.email)

    html = __get_html(
        template_name="notifications/emails/appointment_sucess.html",
        context={'object': requests, }
    )

    return send_message(user_list, subject, text, html)


def send_patient_careline_status(patient):

    from drdown.users.models import User, Responsible

    subject = str(_("DRDOWN: %(name)s has procedures to be made.")) % {
            'name': patient.user.name,
        }

    text = str(_(
        "Hello! We would like to inform you that %(name)s has "
        "%(number)d procedure(s) to be made on the care line.\n"
        "Please visit the Dr. Down website to check which procedures need"
        " your attention."
        "\n\nThanks for your atention,\n\tDr. Down team.",
        )) % {
            'name': patient.user.name,
            'number': patient.count_incomplete_procedures_for_current_age(),
        }

    user_list = [
        patient.user.email,
    ]

    if patient.responsible is not None:
        user_list.append(patient.responsible.user.email)

    html = __get_html(
        template_name="notifications/emails/careline_check.html",
        context={'object': patient, }
    )

    return send_message(user_list, subject, text, html)
