import serial
from pyfirmata2 import ArduinoMega, util
import time

# 포트 이름은 OS에 따라 다릅니다.
board = ArduinoMega('COM7')  # 실제 연결된 포트로 수정 필요
it = util.Iterator(board)
it.start()
arduino = serial.Serial('COM7', 115200, timeout=1)

print("시작합니다...")

while True:
    try:
        line = arduino.readline().decode('utf-8').strip()
        if line:
            parts = line.split(',')
            # 각 부분에서 숫자만 추출
            current_str = parts[0].replace('전류:', '').replace('mA', '').strip()
            voltage_str = parts[1].replace('전압:', '').replace('V', '').strip()

            current = float(current_str)
            voltage = float(voltage_str)

            print(f"전류: {current:.2f} mA, 전압: {voltage:.2f} V")
            time.sleep(1)
    except Exception as e:
        print("에러:", e)
