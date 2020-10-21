#Author : John07-noob
#Date : Oct/21/2020
import smtplib
import getpass
from email.message import EmailMessage

class User:
    def __init__(self, user_mail, user_passwd):
        self.user_mail = user_mail
        self.user_passwd = user_passwd

    def mail_main(self, title, mfrom, text, to):
        msg = EmailMessage()
        msg['Subject'] = title
        msg['From'] = mfrom
        msg['To'] = to
        msg.set_content(text)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as m:
            m.login(self.user_mail, self.user_passwd)
            return m.send_message(msg)

if __name__=='__main__':
    print("Welcome To PymailClient?")
    try:
        user = input("Put your email here: ")
        passwd = getpass.getpass(prompt="Put your email password here: ", stream=None)
        
        to = input("Put recipient email here: ")
        title = input("Put title here: ")
        text = input("Put text here: ")
        mfrom = user
        print("Sending...")
        user_cred = User(user, passwd)
        user_cred.mail_main(title, mfrom, text, to)
        print("Done!")
    except smtplib.SMTPAuthenticationError:
        print("Your Email or Password Incorrect!")