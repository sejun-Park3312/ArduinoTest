from pyfirmata2 import ArduinoMega, util
import time
from KeyBoard import KeyWaiting

KW = KeyWaiting()

# 보드 포트 설정
board = ArduinoMega('COM7')
it = util.Iterator(board)
it.start()
time.sleep(1)  # 초기화 대기

LED_PIN = board.get_pin('d:13:o')

try:
    while KW.Waiting:
        LED_PIN.write(KW.OnOff)
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Ctrl+C 종료")

finally:
    KW.Waiting = False
    board.exit()


