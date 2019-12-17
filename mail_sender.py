import smtplib
from config import adress_from, adress_to, login, password
from template_handler import template_subject, template_text


send_form = adress_from
send_to = adress_to
send_subject = template_subject
send_content = template_text

message_to_send = (
    "From: {0}\n"
    "To: {1}\n"
    "Subject: {2}\n"
    "Content-Type: text/plain; charset='UTF-8'; \n\n{3}".format(
        send_form, send_to, send_subject, send_content).encode('UTF-8')
)

server = smtplib.SMTP_SSL("smtp.yandex.ru: 465")
server.login(login, password)
server.sendmail(send_form, send_to, message_to_send)
server.quit()
