#coding:utf-8
from email.utils import parseaddr, formataddr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib,sys,os
from email.header import Header
import configparser
#发送邮件类
class Sendemail():
    def __init__(self,password,from_addr,to_addr):
        self.password = password
        self.from_addr = from_addr
        self.to_addr = to_addr

    # 格式化收件人的显示名字，貌似现在不起作用了
    def _format_addr(self,s):
        '''格式化一个邮件地址。因为如果包含中文，需要通过Header对象进行编码'''
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    #设置邮件主题等信息
    def email_info(self,msg):
        #来邮件提示的信息
        msg['From'] = self._format_addr('大白菜自动化测试报告 <%s>' % self.from_addr)
        #邮件的主题信息
        msg['Subject'] = Header(u'大白菜自动化测试报告', 'utf8').encode()
        #邮件的收件人,必须使用join方法，才能发送给多人
        msg['To'] = ','.join(self.to_addr)
        #msg['To'] = self._format_addr('测试人员 <%s>' % self.to_addr)
        return msg

    #发送纯文本邮件
    def send_text(self):
        msg = MIMEText('邮件正文', 'plain', 'utf-8')
        msg = self.email_info(msg)
        return msg

    #发送正文是HTML格式的邮件
    def send_html(self,file_name):

        # 读取本地测试报告
        try:
            with open(file_name, 'rb') as f:
                html = f.read()
        except OSError as e:
            print('文件读取失败')

        msg = MIMEText(html, 'html', 'utf-8')
        msg = self.email_info(msg)
        return msg

    #发送带附件的邮件,
    def send_attachment(self,file_name):
        msg = MIMEMultipart()
        msg = self.email_info(msg)
        #邮件的正文内容
        msg.attach(MIMEText('测试报告在附件中，请下载查收', 'plain', 'utf-8'))

        #读取本地测试报告
        try:
            with open(file_name,'rb') as f:
                f_read = f.read()
        except OSError as e:
            print(e,"文件读取失败")

        att1 = MIMEText(f_read, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename=%s' % file_name.split('/')[-1]
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        msg.attach(att1)
        return msg

    #发送
    def main(self,msg):
        smtp_server = "smtp.126.com"
        try:
            server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口是25
            server.set_debuglevel(1)  # 打印发送过程
            server.login(self.from_addr, self.password)
            server.sendmail(self.from_addr, self.to_addr, msg.as_string())
            server.quit()
            print("发送邮件成功")
        except smtplib.SMTPException:
            print("发送邮件失败")

if __name__ == '__main__':
    email_path = "E:\python_project\myjiekoutest\config\config.ini"
    config = configparser.ConfigParser()
    config.read(email_path)
    from_addr = config['email']['FROM_ADDR']
    password = config['email']['PASSWORD']
    to_addr = config['email']['TO_ADDR']
    send_email = Sendemail(password,from_addr,to_addr)
    file_name = 'E:\\python_project\\myjiekoutest\\test_report\\2017-1101.html'
    msg = send_email.send_attachment(file_name)
    send_email.main(msg)
