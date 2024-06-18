import smtplib

sender = "dang12394@gmail.com"
receiver = "danhthuyngoc1203@gmail.com"
password = "gkpn lxfl ibxw bdea"
subject = "Yeu no nhieu nham"
body = "<3 <3 <3 <3 <3 <3 <3 <3"

#header
message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()

server.login(sender,password)
print("Logged in...")
server.sendmail(sender, receiver, message)
print("Email has been sent!")


