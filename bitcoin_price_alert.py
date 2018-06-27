import requests
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import getpass

def send_email():
  # create message object instance
  msg = MIMEMultipart()
  
  # the parameters of the message
  password = your_password
  msg['From'] = your_email
  msg['To'] = send_email_to
  msg['Subject'] = "Bitcoin price, ACT FAST"

  # your message
  message = "Dear " + your_name + "\nBitcoin prices are now " + str(bitcoin_rate) + ". Better buy quick.\nRegards,\n" + your_name
  
  # adds in the message from the above variable
  msg.attach(MIMEText(message, 'plain'))
  
  # create the gmail server
  server = smtplib.SMTP('smtp.gmail.com: 587')
  
  server.starttls()
  
  # Login Creds for sending the email
  server.login(msg['From'], password)
  
  # sends the message
  server.sendmail(msg['From'], msg['To'], message)
  
  server.quit()
  
  # prints to your console
  print("successfully sent email to %s:" % (msg['To']))
  print("Price of bitcoin was at " + str(bitcoin_rate))

# user inputs
your_name = input('Enter your name: ')
your_email = input('Enter your email address (gmail only): ')
your_password = getpass.getpass()
send_email_to = input('Enter email address to send to: ')
alert_amount = input('Alert if Bitcoin drops below: ')

while True:
  url = "https://api.coindesk.com/v1/bpi/currentprice.json"
  response = requests.get(
    url, 
    headers={"Accept": "application/json"},
  )
  data = response.json()
  bpi = data['bpi']
  USD = bpi['USD']
  bitcoin_rate = int(USD['rate_float'])
  if bitcoin_rate < int(alert_amount):
    send_email()
    print('Will check again in 3 minutes. Ctrl + C to quit.')
    time.sleep(180)
  else:
    time.sleep(300)
    print('Price is ' + str(bitcoin_rate) + '. Will check again in 5 minutes. Ctrl + C to quit.')

