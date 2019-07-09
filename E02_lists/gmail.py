import imaplib
EMAIL = "karnobat1973@gmail.com"
PASSWORD = 'Who the fuck is Pesho?'
SERVER = 'imap.gmail.com'
PORT = 993

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
mail.select('inbox')
type, data = mail.search(None, 'ALL')



