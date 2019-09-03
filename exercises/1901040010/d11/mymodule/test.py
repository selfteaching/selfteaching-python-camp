import getpass
import yagmail

sender = input("Sender's Email:")
password = getpass.getpass("Enter your password:")
recipients = input("Recipients' Email:")


yag = yagmail.SMTP(sender,password,host='smtp.qq.com')
contents = ['https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA']
yag.send('cicimok@qq.com','Test',contents)
print("Success!")