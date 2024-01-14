# this code was made by Ahmad Alshami
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import openpyxl
import time
import os
import random

def send_email(to_email, subject, body, sender_email, sender_password, attachment_path=None):
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = to_email
    message["Subject"] = subject

    text_part = MIMEText(body, "plain")
    html_part = MIMEText(body, "html")

    message.attach(text_part)
    message.attach(html_part)

    if attachment_path:
        with open(attachment_path, "rb") as attachment:
            part = MIMEApplication(attachment.read(), Name=os.path.basename(attachment_path))
            part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment_path)}"'
            message.attach(part)

    with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, message.as_string())

def send_emails_from_excel(file_path, sender_email, sender_password, subject, body, attachment_path=None, min_delay=200, max_delay=340):
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active

    sent_emails_file = "sent_emails.txt"

    sent_emails = set()
    if os.path.exists(sent_emails_file):
        with open(sent_emails_file, "r") as file:
            sent_emails = set(file.read().splitlines())

    for row in sheet.iter_rows(min_row=2, values_only=True):
        email_cells = str(row[1]).split("/")

        for to_email in email_cells:
            to_email = to_email.strip()

            if to_email and '@' in to_email and to_email not in sent_emails:
                print(f"Sending email to: {to_email}")
                send_email(to_email, subject, body, sender_email, sender_password, attachment_path)

                sent_emails.add(to_email)
                with open(sent_emails_file, "a") as file:
                    file.write(to_email + "\n")

                delay = random.randint(min_delay, max_delay)
                print(f"Waiting for {delay} seconds before the next email.")
                time.sleep(delay)
            elif to_email and '@' in to_email:
                print(f"Email already sent to: {to_email}. Skipping to the next email.")
            else:
                print("Invalid email or email already sent. Skipping to the next email.")

if __name__ == "__main__":
    sender_email = "email"
    sender_password = "generated app password"
    subject = "subject"
    signature_html = """
////////////////////////////////// your signature if it exists
    """

    body = f"""
    the message you want to send
    {signature_html}
    """

    pdf_file_path = r"if existed"
    excel_file_path = r"excel file path that you are getting your emails from"

    send_emails_from_excel(excel_file_path, sender_email, sender_password, subject, body, pdf_file_path)
