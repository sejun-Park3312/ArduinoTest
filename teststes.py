from pyfirmata2 import ArduinoMega
import time

board = ArduinoMega('COM7')  # 포트는 너의 아두이노 포트에 맞게

led = board.get_pin('d:13:o')  # 디지털 13번 핀 → 출력

print("3초간 내장 LED 켜기")
led.write(1)
time.sleep(10)

print("LED 끄기")
led.write(0)

board.exit()
