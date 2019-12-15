import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl = True)
connect = conn.login('yourmail@gmail.com', 'password')
print(connect)

inox = conn.select_folder('INBOX', readonly = True)
print(inbox)

UIDs = conn.search(['FROM', 'amritlc77@gmail.com'])
print(UIDs)



rawMessage = conn.fetch([17538],['BODY[]', 'FLAGS'] )
 
pymsg = pyzmail.PyzMessage.factory(rawMessage[17538][b'BODY[]'])
print(pymsg)

subject = pymsg.get_subject()
print(subject)

address = pymsg.get_address('from')
print(address)

addressTo = pymsg.get_address('to')
print(addressTo)

print(pymsg.get_address('bcc'))

print(pymsg.text_part) # for text part

print(pymsg.html_part) # for html part

#pymsg.text_part.get_payload().decode('UTF-8') #for decoding text
#pymsg.text_part.charset

folders = conn.list_folders() # show all folder
print(folders)

selectInbox = conn.select_folder('INBOX', readonly = False)
print(selectInbox)

delete = conn.delete_message([17538]) #to delete message



















