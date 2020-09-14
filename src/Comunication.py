"""This file will store all the functions about managing communication"""

import sys

try:
    import telepot

except:
    sys.exit("Please run: pip install telepot")

class TelegramBot():
    """This class will store all the functions for using a TelegramBot
    """

    def __init__(self, token):
        self.token = token
        self.bot = telepot.Bot(self.token)

    def get_updates(self):
        """This function will return json data of all the messages it was sent

        Returns:
            json: The json data of all the messages
        """

        updates = self.bot.getUpdates()
        return updates
    
    def send_message(self, msg, chat_id):
        """This function will send a message

        Args:
            msg (str): The message you want sent
            chat_id (str): The chat id of user you want the message sent to
        """

        self.bot.sendMessage(chat_id, msg)

    def send_photo(self, path, chat_id):
        """This function will send a photo

        Args:
            path (str): The path of the photo you want sent
            chat_id (str): The chat id of the user you want the photo sent to
        """
        self.bot.sendPhoto(chat_id, photo=open(path, "rb"))
    
    def send_audio(self, path, chat_id):
        """This function will send a audio message

        Args:
            path (str): The path of the audio
            chat_id (str): The chat id of the user you want the audio sent to
        """
        self.bot.sendAudio(chat_id, path)


def send_email(yourEmailAddress, YourPassword, EmailAdressToSendTo, subject, msg):
    """This function will send a email

    Args:
        yourEmailAddress (str): Your email
        YourPassword (str): Your email password
        EmailAdressToSendTo (str): The email to send to
        subject (str): The subject of the email
        msg (str): The message
    """
    failCount = 0
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(emailAddress, password)
        message = ('Subject: {}\n\n{}'.format(subject, msg))

        server.sendmail(EmailAdressToSendTo, EmailAdressToSendTo, message)
        server.quit()
    except:
        if failCount == 3:
            print("ERROR Failed to send email.")
        else:
            failCount += 1