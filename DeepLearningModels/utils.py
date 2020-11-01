# Admin utility script.
# from .admin_data import MAIL_ADDRESS, MAIL_PASSWORD
MAIL_ADDRESS = "mkshsahani852@gmail.com"
MAIL_PASSWORD = "Mukesh@9646647402"
import smtplib
import random 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# me == my email address
# you == recipient's email address
"""
me = "my@email.com"
you = "your@email.com"

# Create message container - the correct MIME type is multipart/alternative.
msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = me
msg['To'] = you

# Create the body of the message (a plain-text and an HTML version).
text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
html = \
<html>
  <head></head>
  <body>
    <p>Hi!<br>
       How are you?<br>
       Here is the <a href="http://www.python.org">link</a> you wanted.
    </p>
  </body>
</html>


# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText(text, 'plain')
part2 = MIMEText(html, 'html')

# Attach parts into message container.
# According to RFC 2046, the last part of a multipart message, in this case
# the HTML message, is best and preferred.
msg.attach(part1)
msg.attach(part2)
# Send the message via local SMTP server.
mail = smtplib.SMTP('smtp.gmail.com', 587)

mail.ehlo()

mail.starttls()

mail.login('userName', 'password')
mail.sendmail(me, you, msg.as_string())
mail.quit()
"""
def sendMail_otp_version(user_email_address, first_name, as_,otp):
    adminMailAddress = MAIL_ADDRESS # admin email address
    amdinMailPassword = MAIL_PASSWORD # admin email password 
    body = f"Hi! {first_name} you registered as {as_} your otp is  {otp}"
    msg = MIMEText(body)
    msg['Subject'] = "Atam NIRBHAR BHARAT"
    msg['From'] = adminMailAddress 
    msg['To'] = user_email_address
    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()

    mail.login(MAIL_ADDRESS, MAIL_PASSWORD)
    mail.send_message(msg)
    # mail.sendmail(MAIL_ADDRESS, user_email_address, message)
    mail.quit()

    return True 

if __name__ == '__main__':
    sendMail_otp_version("ishugambhir2001@gmail.com","ISHAN GAMBHIR", "Funder", random.randint(1234, 9999)) # mail it. 

    