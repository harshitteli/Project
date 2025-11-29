from email.message import EmailMessage
email="babagspeaking@gmail.com"
app_password=""
receiver="mauryakumarsujitssm2006@gmail.com"
msg=EmailMessage()
msg["From"]=email
msg["To"]=receiver
msg["Subject"]="Hello from Python"
msg.set_content("This email was shared")
context=ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com",400,context=context) as server:
    server.login(email,app_password)
    server.send_message(msg)
    print("Mail sent")
