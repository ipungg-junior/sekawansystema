import imaplib, email
 
def get_email_messages(username, password, server):
    # Connect to the IMAP server
    mail = imaplib.IMAP4_SSL(server)
    
    # Login to the server
    mail.login(username, password)
    
    # Select the mailbox (e.g., INBOX)
    mail.select("INBOX")
    
    # Search for email messages
    result, data = mail.search(None, "ALL")
    
    # Get the list of email message IDs
    email_ids = data[0].split()
    
    # Iterate over the email IDs and fetch the messages
    for email_id in email_ids:
        result, data = mail.fetch(email_id, "(RFC822)")
        raw_email = data[0][1]
        # Parse the raw email data
        email_message = email.message_from_bytes(raw_email)
        
        # Extract the message content
        if email_message.is_multipart():
            for part in email_message.walk():
                content_type = part.get_content_type()
                if content_type == "text/plain":
                    message = part.get_payload(decode=True).decode()
                    print(message)
        else:
            message = email_message.get_payload(decode=True).decode()
            print(message)
        
        # Process the raw email data as needed
        # For example, you can use the email library to parse the email
        
    # Close the connection
    mail.logout()
 
# Example usage
username = "cs@systema.id"
password = "Ipung443833!"
server = "imap.hostinger.com"
 
get_email_messages(username, password, server)