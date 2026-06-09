# [문제 4] 네트워크 자동화 (10점)
# paramiko 모듈을 사용하여 원격 리눅스 서버에 접속한 후, /var/log/syslog 파일의 마지막 10줄을 읽어와 로컬 파일로 저장하는 프로그램을 작성하라.

import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    # 아래의 '실제_IP_주소', '아이디', '비번'을 본인 환경에 맞게 입력하세요.
    ssh.connect('192.168.x.x', username='본인아이디', password='본인비밀번호')
    
    stdin, stdout, stderr = ssh.exec_command('tail -n 10 /var/log/syslog')
    print(stdout.read().decode())
    ssh.close()
except Exception as e:
    print(f"접속 실패: {e}")