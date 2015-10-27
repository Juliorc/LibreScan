import smtplib


class MailService:

    server = "localhost"

    def get_email_receiver(self):
        return "librescan@gmail.com"

    #Formats the mail msg with the sender information and the body msg.
    def prepare_msg(self, p_name, p_msg, p_phone, p_from):
        msg = """\
        Enviado pt: %s <%s>
        Tel: %s
        Cuerpo del mensaje: %s
        """ % (p_name, p_from, p_phone, p_msg)
        print(msg)
        return msg

    def send(self, mail):
        s = smtplib.SMTP(self.server)
        sender = mail.sender
        to = self.get_email_receiver()
        msg = self.prepare_msg(mail.name, mail.msg, mail.phone, mail.sender)
        try:
            s.sendmail(sender, to, msg)
            print("Email was sent successfully.")
        except Exception as exc:
            print("Mail failed: {}".format(exc))
        finally:
            s.quit()
