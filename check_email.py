import imaplib
import email
from email.header import decode_header

def OpenEmail(email, password):
    """Log in to email andd return imap, messages to be passed into CheckEmails"""
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    try:
        imap.login(email, password)
    except Exception as e:
        print("Error: " + str(e))
    else:
        _, messages = imap.select("INBOX")
        return imap, messages

def CloseEmail(imap):
    """Close connection to email logged into via imap"""
    imap.close()
    imap.logout()

def CheckEmails(imap, messages, max_emails):
    """Iterate through (max_emails) emails and return email body with VitalCheck subject"""
    messages = int(messages[0])
    
    for i in range(messages, messages - max_emails, -1):
        _, msg = imap.fetch(str(i), "(RFC822)")

        for response in msg:
            if isinstance(response, tuple):
                # Parse email of bytes into message object
                msg = email.message_from_bytes(response[1]) # pylint: disable=unsubscriptable-object
                subject, encoding = decode_header(msg["Subject"])[0]
                sender, encoding = decode_header(msg.get("From"))[0]

                
                if isinstance(subject, bytes):
                    # If email subject is bytes, decode to str
                    if encoding is not None:
                        subject = subject.decode(encoding)

                #subject = str(email.header.make_header(email.header.decode_header(msg['Subject'])))
                
                if isinstance(sender, bytes):
                    if encoding is not None:
                        sender = sender.decode(encoding)

                if msg.is_multipart():
                    for part in msg.walk():
                        try:
                            # Get the body of the email
                            body = part.get_payload(decode=True).decode()
                        except:
                            pass
                else:
                    # Get the body of the email
                    body = msg.get_payload(decode=True).decode()

                if "IMPORTANT: Daily check for worksite clearance at Fordham Students" in subject:
                    return body

    return None  # Return None if email with VitalCheck subject not found

def ParseBody(body: str):
    """Takes in a VitalCheck email as a string and returns the link in the email body"""
    if body == None:
        return ''

    startIndex = body.find("https://urldefense")  # The link always starts with this, so this will find it in the email body
    endIndex = body.find("\"", startIndex)

    return body[startIndex:endIndex]
            