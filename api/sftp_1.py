import paramiko
import getpass

transport = paramiko.Transport(('114.71.220.5', 22))

user = input('Username: ')
pwd = getpass.getpass('Password: ')
transport.connect(username=user, password=pwd)

sftp = paramiko.SFTPClient.from_transport(transport)

# 서버의 'test' 폴더 안에 있는 iot.txt를 가져오도록 경로 수정
src_file_path = 'test/iot.txt' 
dst_file_path = 'iot.txt'

# 파일 가져오기 (다운로드)
sftp.get(src_file_path, dst_file_path)
print(f"다운로드 완료: {src_file_path}")

# 업로드 (기존 코드 유지)
src_file_path = 'index.html'
dst_file_path = 'index.html'
sftp.put(src_file_path, dst_file_path)
print(f"업로드 완료: {dst_file_path}")

sftp.close()
transport.close()