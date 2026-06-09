# paramiko를 이용하여 SSH 서버에 접속한 후

# 폴더 생성
# 파일 생성
# zip 압축
# SFTP 다운로드

import paramiko

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(
    paramiko.AutoAddPolicy()
)

ssh.connect(
    "localhost",
    username="user",
    password="1234"
)

ssh.exec_command("mkdir test")

ssh.exec_command(
    "echo iot > test/iot.txt"
)

ssh.exec_command(
    "zip -r test.zip test"
)

sftp = ssh.open_sftp()

sftp.get(
    "test.zip",
    "test.zip"
)

sftp.close()
ssh.close()