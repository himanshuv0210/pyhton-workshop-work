import smtplib as ma
"""
step1 : import smtplib
step2 : open mail connection(mail port no.)
step3 : login using username and password
step4 : send mail
step5 : close connnection
"""

con = ma.SMTP("smtp.gmail.com", 587)
con.starttls()
con.login("prfounder43@gmail.com", "r@pankaj21")
msg = "sending mail using python script"
con.sendmail("prfounder43@gmail.com", "himanshuv102@gmail.com", msg)
print("Mail sucessfully")
con.close()