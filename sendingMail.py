import smtplib

conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
print(conn)
print(conn.ehlo())
print(conn.starttls())

print(conn.login('yourmail@gmail.com','password'))

conn.sendmail('yourmail@gmail.com', 'othermail@gmail.com', 'Subject: Hey This Email is Sent From Python smtp_server :)\n\nDear Amrit,\nSo long thanks for taking interest in learning new langguage Python.\n\nI hope you will master in Python soon.\n\n-Best Wishesh Amrit')

print(conn.quit())

