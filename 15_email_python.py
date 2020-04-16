import smtplib

# Obtains the connection to gmail
conn = smtplib.SMTP("smtp.gmail.com", 587) # server domain name, server portnumber

# Connects to the server
conn.ehlo()

# Starts the encryption
conn.starttls() 

# Login
conn.login('edu@gmail.es', 'xxxxx')

# Sending an email
conn.sendmail('edu@gmail.es', 'edu@gmail.es', 'Subject: Python boss...\n\nDear Edu you are a python boss\n\nEdu')

# Disconnectes you from the server
conn.quit()

# Checking the email box
import imapclient

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('edu@gmail.es', 'xxxxx')
conn.select_folder('INBOX', readonly=True) # select inbox folder
UIDs = conn.search(['SINCE', '20-Feb-2020']) # select messages since an specefic date
i = len(UIDs)-1 # take first message
raw_message = conn.fetch([UIDs[i]],['BODY[]','FLAGS']) # search it

# Converts message in something readable
import pyzmail

message = pyzmail.PyzMessage.factory(raw_message[UIDs[i]][b'BODY[]']) 
print(message.get_subject())
print(message.get_addresses('from'))
print(message.get_addresses('to'))

print(message.text_part) # finds if there is a text part
print(message.html_part) # finds if there is a html part
print(message.get_payload()) # obtain the text of the message

# Deletes emails
conn.select_folder('INBOX', readonly=False)
UIDs = conn.search(['SINCE', '20-Feb-2020']) 
conn.delete_messages(UIDs)