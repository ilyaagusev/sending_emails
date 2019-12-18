import smtplib
from config import EMAIL_FROM, EMAIL_TO, LOGIN, PASSWORD
from template_handler import email_text, email_subject


email_to_send = (
    "From: {0}\n"
    "To: {1}\n"
    "Subject: {2}\n"
    "Content-Type: text/plain; charset='UTF-8'; \n\n{3}".format(
        EMAIL_FROM, EMAIL_TO, email_subject, email_text).encode('UTF-8')
)

server = smtplib.SMTP_SSL("smtp.yandex.ru: 465")
server.login(LOGIN, PASSWORD)
server.sendmail(EMAIL_FROM, EMAIL_TO, email_to_send)
server.quit()
