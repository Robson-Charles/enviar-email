'''
lembresse se nao for emviar um arquivo comenta toda a parte de envio de arquivo para nao quebrar o codigo pfv

'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from email.mime.base import MIMEBase
from email import encoders

from informacoes import login

def enviar_email():

    #efetuar login
    email = login.email
    senha = login.senha
    servidor = smtplib.SMTP('SMTP.gmail.com: 587')  # caso for usar outro provedor sem ser o gmail procure o host e a porta e troque
    servidor.ehlo()
    servidor.starttls()
    servidor.login(email, senha)

    #construie email no estilo mime
    body = 'fazendo o texte em'#coloque a mensagem aqui
    email_msg = MIMEMultipart()
    email_msg['Subject'] = 'fazendo um teste em google'
    email_msg['From'] = email #importei meu email de outro arquivo para nao ficar exposto
    email_msg['To'] = 'hitsu.4586@gmail.com; jhannajackson12@gmail.com'
    email_msg.attach(MIMEText(body, 'plain'))#caso queira um texto do estilo Html so trocar de plain para html
#comenta daqui ate
    #abre o arquivo em modo binario
    attachment = open('C:\\Users\\hitsu\\Desktop\\enviar emails\\arquivo\\hmmmmm.mp4', 'rb')# coloque o arquivo que voce quer enviar na pasta arquivo e coloque o nome + extenção dele no final
    Nome_do_arquivo = 'hmmmmm.mp4' #coloca aqui o nome do arquivo para ficar escrito no email

    #joga o arquivo para base64
    att = MIMEBase('application', 'octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)

    #adiciona um cabeçalho no tipo anexo
    att.add_header('Content-Disposition', f'attachment; filename= {Nome_do_arquivo}')

    #fecha o arquivo
    attachment.close()

    #coloca o anexo no corpo do email
    email_msg.attach(att)
#aqui
    #enviar email para servidor SMTP
    servidor.sendmail(email_msg['From'], email_msg['To'],email_msg.as_string())

    servidor.quit()

enviar_email()
