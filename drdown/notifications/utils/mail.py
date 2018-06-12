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

