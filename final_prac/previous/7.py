import paramiko
import smtplib
from email.message import EmailMessage
import os

# 1. 설정 정보
HOST = '실습_서버_IP_주소'  # 예: '192.168.0.10' 또는 'iot.sch.ac.kr'
PORT = 22                 # SSH 기본 포트
USER = '20231312'        # 예: '20260001'
PASSWORD = '학교_비밀번호'
STUDENT_ID = '20231312'   # 본인 학번
EMAIL_SENDER = 'skdpa391@gmail.com'
EMAIL_PASSWORD = 'pjhm srpc edwc qbjd'
EMAIL_RECEIVER = 'won00@sch.ac.kr'

# 2. SSH 접속 및 명령 실행
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(HOST, port=PORT, username=USER, password=PASSWORD)

# 폴더 생성, 파일 생성, 압축 수행
commands = [
    f'mkdir -p {STUDENT_ID}',
    f'echo iot > {STUDENT_ID}/iot.txt',
    f'zip -r {STUDENT_ID}.zip {STUDENT_ID}'
]

for cmd in commands:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    stdout.channel.recv_exit_status() # 명령 완료 대기

# 3. SFTP를 이용하여 파일 가져오기
sftp = ssh.open_sftp()
sftp.get(f'{STUDENT_ID}.zip', f'{STUDENT_ID}.zip')
sftp.close()
ssh.close()

# 4. 이메일 전송
msg = EmailMessage()
msg['Subject'] = f'{STUDENT_ID}.zip'
msg['From'] = EMAIL_SENDER
msg['To'] = EMAIL_RECEIVER
msg.set_content('과제 파일 제출합니다.')

with open(f'{STUDENT_ID}.zip', 'rb') as f:
    file_data = f.read()
    msg.add_attachment(file_data, maintype='application', subtype='zip', filename=f'{STUDENT_ID}.zip')

# Gmail 등 SMTP 서버 설정 (예: 구글)
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
    smtp.send_message(msg)

print("작업이 완료되었습니다.")