# sms.py
# Sends sms message to any cell phone using gmail smtp gateway
# Written by Alex Le

import smtplib

def main():
	Send_SMS()
	
def Send_SMS(TEXTMSG):
	# Use sms gateway provided by mobile carrier:
	# at&t:     number@mms.att.net
	# t-mobile: number@tmomail.net
	# verizon:  number@vtext.com
	# sprint:   number@page.nextel.com

	#TEXTMSG = 'TEST Text msg'

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 )
	print('connect to server')

	server.starttls()

	server.login( 'chiptseng1982@gmail.com', 'asdf1234!' )

	# Send text message through SMS gateway of destination number
	server.sendmail( 'HSINWEI', '4086851762@messaging.sprintpcs.com', TEXTMSG )
	print('Finish sending SMS to Hsinwei')

if __name__ == '__main__':
    main()
