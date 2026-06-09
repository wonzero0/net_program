# 3. [데이터 패킹(Pack/Unpack)] (20점)
# 다음은 IoT 센서로부터 수신한 8바이트 크기의 데이터입니다. 빅 엔디언(Big-endian) 규격에 맞춰 데이터를 언패킹하여 출력하는 코드를 작성하시오.

# 패킷 규격: 기기ID(2바이트 정수), 상태코드(2바이트 정수), 데이터값(4바이트 실수)

import struct

packet = b'\x04\xd2\x00\x01\x41\xcc\xcc\xcd' # 예시 패킷

unpacked_data = struct.unpack('!HHf', packet)

print(f"기기ID: {unpacked_data[0]}")
print(f"상태코드: {unpacked_data[1]}")
print(f"데이터 값: {unpacked_data[2]:.2f}")