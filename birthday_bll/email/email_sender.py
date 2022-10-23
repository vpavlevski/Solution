import smtplib

from birthday_bll.email.email import Email
from birthday_bll.email.email_server_settings import EmailServerSettings
from email.mime.text import MIMEText

from utils.operation import OperationResult


class EmailSender:
    def __init__(self, emailServerSettings: EmailServerSettings):
        self.emailServerSettings = emailServerSettings

    def SendEmail(self, email: Email) -> OperationResult:
        sender = email.From
        receiver = email.To

        msg = MIMEText(email.Message)

        msg['Subject'] = email.Subject
        msg['From'] = email.From
        msg['To'] = email.To

        user = self.emailServerSettings.Username
        password = self.emailServerSettings.Password

        tries = self.emailServerSettings.Retries
        for i in range(tries):
            try:
                with smtplib.SMTP(self.emailServerSettings.Server, self.emailServerSettings.Port) as server:
                    server.login(user, password)
                    server.sendmail(sender, receiver, msg.as_string())
                    return OperationResult.CreateSuccess("Reminder Email was sent to: " + receiver)
            except Exception as e:
                if i < tries - 1:
                    continue
                else:
                    return OperationResult.CreateError("We were unable to send email to: " + receiver)
            break

