import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from data.email_config import EMAIL_CONFIG

class EmailService:

    def enviar(self, destinatario, asunto, mensaje):
        try:
            correo = MIMEMultipart()
            correo["From"] = EMAIL_CONFIG["email"]
            correo["To"] = destinatario
            correo["Subject"] = asunto

            correo.attach(MIMEText(mensaje, "plain"))

            servidor = smtplib.SMTP(
                EMAIL_CONFIG["smtp_server"],
                EMAIL_CONFIG["smtp_port"]
            )
            servidor.starttls()
            servidor.login(
                EMAIL_CONFIG["email"],
                EMAIL_CONFIG["password"]
            )
            servidor.send_message(correo)
            servidor.quit()

            return True

        except Exception as error:
            print("Error:", error)
            return False
