import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Mail:
    """
    Mail Class system responsible for the mailing system..
    Used to send emails to user from the back-end.
    Can be used for verification purposes as well as general communication.

    """

    def __init__(self):
        """
        Initialises the Mailing system with its parameters.

        """

        context = ssl.create_default_context()
        __password = 0
        self.port = 0
        self.smtp_server = ""
        self.sender_email = ""
        self.__password = ""

        self.server = smtplib.SMTP(self.smtp_server, self.port)
        self.server.ehlo()  # Can be omitted
        self.server.starttls(context=context)  # Secure the connection
        self.server.ehlo()  # Can be omitted
        self.server.login(self.sender_email, self.__password)

    def send_2fa_email(self, user):
        """
         Sends a 2-Factor Authentication token for the newly-registered user to set up their authenticator.
        :param user: The User object with all the user's attribute.
        :return: ``None``

        """

        message = MIMEMultipart("alternative")
        message["Subject"] = "2FA Authentication Setup for your account necessary"
        message["From"] = self.sender_email
        message["To"] = user.email
        secret = str(user.otp_key)[2:34]
        url = "otpauth://totp/Team32_Project?secret=" + secret

        text = f"""\
        Hello {user.username}!,

        Thank you for creating your account!

        Please setup 2FA for your account.

        Here is the 2FA secret you need for your Authenticator!
        {secret}
        {url}


        https://authy.com/features/
        """

        html = f"""\
        <html>
          <body>
            <p>Hello {user.username}!<br>
               Thank you for creating your account!<br><br>
               Here is the 2FA secret you need for your Authenticator!<br>
               <a href="{url}">{secret}</a><br> 
               <a href="https://authy.com/features/"> Authy</a> is an example of authenticator you can download and use!
            </p>
          </body>
        </html>
        
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")
        message.attach(part1)
        message.attach(part2)
        try:
            self.server.sendmail(self.sender_email, user.email, message.as_string())
        except Exception as e:
            # Print any error messages to stdout
            print(e)

        '''    
        def send_2fa_email(self, user):
        try:
            message = f"""Subject: 2FA Authentication Setup for your account necessary
            \n
            {user.otp_key}
            This message is sent from Python.\
            """
            self.server.sendmail(self.sender_email, user.email, message)
        except Exception as e:
            # Print any error messages to stdout
            print(e)
        
        '''

    def exit(self):
        """
         kills the mail session and clears attributes.
        :return: ``None``

        """

        self.server.quit()

        # Clear attributes
        self.port = None
        self.smtp_server = None
        self.sender_email = None
        self.__password = None
        self.server = None
