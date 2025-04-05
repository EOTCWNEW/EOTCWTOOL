import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server and login credentials
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('tagamasidsacw@gmail.com', 'Mata Ng CyberWorld.')

# Create the email message
msg = MIMEMultipart()
msg['From'] = 'tagamasidsacw@gmail.com'
msg['To'] = 'glitchedkasaki@gmail.com'
msg['Subject'] = 'test'
body = 'Hello, this is an automated email!'
msg.attach(MIMEText(body, 'plain'))

# Send the email
text = msg.as_string()
server.sendmail('tagamasidsacw@gmail.com', 'glitchedkasaki@gmail.com', text)

# Close the SMTP server connection
server.quit()
