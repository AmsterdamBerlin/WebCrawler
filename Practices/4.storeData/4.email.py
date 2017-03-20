import smtplib
from email.mime.text import MIMEText


fromaddr = "yuang.chen.berlin@gmail.com"
toaddr = "cyanfeb@gmail.com"

msg = MIMEText("This an email send by python code")

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Python Email"


server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "Berlin2016")
#text = msg.as_string()
#server.sendmail(fromaddr, toaddr, text)
server.send_message(msg)
server.quit()

# keep eyes on news update, make alert until
# while(bsObj.find("a", {"id":"answer"}).attrs['title'] == "NO"):
#    print("It is not Christmas yet.")
#    time.sleep(3600)
# sendMail("bla,bla")
