import serial
import time
from KeyBoard import KeyWaiting

KW = KeyWaiting()

# 아두이노와 연결된 포트 지정 (예: 'COM7' 또는 '/dev/ttyACM0')
arduino = serial.Serial('COM7', 115200, timeout=1)
time.sleep(3)  # 아두이노 초기화 대기 (필수!)

try:
    while KW.Waiting:
        # 제어 입력값 (0 또는 0.5 등)
        input_value = KW.OnOff

        # 문자열로 변환해서 개행 문자 포함해 전송
        arduino.write(f"{input_value}\n".encode())
        time.sleep(0.1)  # 100ms 간격으로 송신

except KeyboardInterrupt:
    print("종료됨.")
    arduino.close()

finally:
    KW.Waiting = False
