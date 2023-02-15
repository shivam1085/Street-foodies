# Python code to illustrate Sending mail from 
# your Gmail account 
import smtplib 

# creates SMTP session 
s = smtplib.SMTP_SSL('streetfoodies20@gmail.com', 465) 


# Authentication 
# s.login("aakashsagar640@gmail.com", "aakash9131597624") 

# # message to be sent 
# message = "Message_you_need_to_send"

# # sending the mail 
# s.sendmail("aakashsagar640@gmail.com", "aakashsagar640@gmail.com", message) 

# # terminating the session 
# s.quit() 
