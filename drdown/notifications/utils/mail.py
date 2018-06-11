from django.contrib.sites import requests
try:
    from utility.email import EmailEnvironment
except ImportError:
    raise ImportError('Could not find the email configuration file')


def send_simple_message(user, subject, text):

    try:
        Data = EmailEnvironment()
    except NameError:
        Data = {'url': "", 'api': "", 'domain': ""}

    return requests.post(
        Data['url'],
        auth=("api", Data['api']),
        data={"from": "Excited User <excited@samples.mailgun.org>",
              "to": user.email,
              "subject": subject,
              "text": text})
