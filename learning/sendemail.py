import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

# Set the sender email, receiver email, password, email subject and body.
sender = "@gmail.com"
receiver = "@gmail.com"
password = ""
subject = "Lipsum Generator"

# Create a multipart message to hold the email content and attachments
message = MIMEMultipart()
message["From"] = sender
message["To"] = receiver
message["Subject"] = subject

# Add the body text to the email
body = """
Hi Nick 👋,

😶‍🌫️😶‍🌫️😶‍🌫️
🫥🫥🫥

We see the emojis in VSCODE as windows set emojis, but when email is received it changes to google emoji set

https://www.lipsum.com/
https://www.lipsum.com/
https://www.lipsum.com/

Links show as href in the mails, despite putting them links in here.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed eget tincidunt leo, ut imperdiet enim. Vivamus sodales quam neque, aliquet imperdiet arcu auctor in. Donec ut orci porttitor, porta urna quis, eleifend nisi. Cras ultrices elementum diam at faucibus. Aenean sagittis diam ac iaculis hendrerit. Suspendisse vel hendrerit nunc. Vivamus in dui egestas, aliquet lectus eget, porttitor leo. Aliquam sed gravida diam, id condimentum lorem. Nulla condimentum mi id massa imperdiet posuere. Vivamus varius at erat at bibendum. Nam elementum, nisi quis fermentum rhoncus, est mauris pharetra nisi, vitae laoreet magna eros nec tellus. Donec in pulvinar magna. Duis vel mattis felis. Donec a venenatis neque. In dapibus purus mauris, nec tristique arcu pharetra at.

    • Suspendisse potenti. 🤭Fusce sapien lorem, condimentum sit amet urna at, maximus feugiat nunc. In lorem odio, tristique at auctor eget, tempus sit amet dui. In arcu metus, fringilla a quam sit amet, ultricies volutpat eros. Sed convallis commodo felis, a ornare turpis aliquet ut. Vivamus pretium, purus ut consequat luctus, urna ante scelerisque augue, sed porttitor velit dui eu tellus. Vestibulum in sem mollis, euismod tortor eu, convallis leo. Fusce sit amet nulla nec urna accumsan consectetur. In at neque viverra, blandit leo eu, rutrum dolor. Nam tempor elit ligula, sit amet accumsan lorem consequat ut. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Curabitur commodo dolor eget nibh vehicula faucibus. Quisque nec orci tincidunt, elementum magna nec, porttitor eros. Donec ornare sapien eget magna pellentesque pretium at et elit.

Cras sollicitudin, purus sit amet sagitti😲😲😲😲s lobortis, ipsum urna pretium orci, id😉😉😉 lacinia tortor libero efficitur purus. Proin egestas porta arcu, eget aliquam leo ullamcorper id. Proin sit amet lorem enim. Mauris laoreet magna et efficitur volutpat. Quisque eleifend quis lectus et volutpat. Donec bibendum sapien sit amet sollicitudin blandit. Curabitur ut mauris nec lectus congue viverra. Curabitur malesuada volutpat odio, ut sollicitudin leo aliquet at. Suspendisse condimentum, erat at efficitur varius, neque ex gravida massa, vel efficitur enim libero a risus. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Vivamus in rutrum diam. Maecenas a commodo nisi, vitae blandit sapien. In convallis metus non aliquet aliquet.

Ut vel dictum mauris, eget pretium lacus. Suspendisse sed finibus nisi, sed faucibus dui. 🥶🥶🤭Nulla in vehicula augue. Fusce purus velit, convallis sed auctor et, efficitur sed nibh. Praesent at fringilla mi. Suspendisse condimentum, augue vel aliquet ultrices, neque elit sollicitudin nisl, eget pellentesque libero tortor eu libero. Mauris a consequat eros. Maecenas sit amet enim ut arcu commodo vehicula. Pellentesque malesuada sed nunc nec fringilla. Sed dictum ornare tempor. Nulla nec erat sed dui ullamcorper dictum. Quisque vel fringilla nisl.

Donec sodales risus eros. 😎😎Pellentesque scelerisque lorem fringilla venenatis hendrerit. In vulputate nisi elit, sit amet pretium neque facilisis ut. Ut tincidunt accumsan vulputate. Maecenas faucibus non urna vitae iaculis. Praesent cursus fermentum velit non viverra. Integer sit amet ligula et tellus posuere molestie. Proin nec metus bibendum, condimentum metus in, ultricies nisl. Mauris et dolor pellentesque sapien convallis porta. Aliquam erat volutpat. Aliquam sed tortor lectus. Curabitur pharetra varius nunc, tempor ultricies neque tempus ut. Sed pellentesque at ex ac viverra. Sed sagittis malesuada eros, eu semper felis rhoncus at.

Best regards,
GonTore Games 🌊🌊🌊
"""
message.attach(MIMEText(body))

# Attach the first image to the email
with open("C:\\Users\\user\\Desktop\\prog chall py\\learning\\itertools\\img examples\\accumulate.png", "rb") as f:
    img1 = MIMEImage(f.read())
    img1.add_header('Content-Disposition', 'attachment', filename="image1.jpg")
    message.attach(img1)

# Attach the second image to the email
with open("C:\\Users\\user\\Desktop\\prog chall py\\learning\\itertools\\img examples\\permutations.png", "rb") as f:
    img2 = MIMEImage(f.read())
    img2.add_header('Content-Disposition', 'attachment', filename="image2.jpg")
    message.attach(img2)

# Attach excel file to the email
with open('C:\\Users\\user\\Desktop\\prog chall py\\learning\\web scraping\\hockey\\hockey.xlsx', 'rb') as f:
    attachment = MIMEImage(f.read(), _subtype='xlsx')
    attachment.add_header('Content-Disposition', 'attachment', filename='data.xlsx')
    message.attach(attachment)

# Create an SMTP object to connect to the Gmail SMTP server
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

# Login to the Gmail SMTP server using the sender email and password
server.login(sender, password)
print('Connecting...')

# Send the email message using the SMTP server
server.sendmail(sender, receiver, message.as_string())
print(f'"{subject}" was sent to {receiver}!')

# Close the SMTP connection
server.quit()