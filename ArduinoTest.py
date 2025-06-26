from pyfirmata2 import ArduinoMega, util
import time
import cv2

# 보드 포트 설정
board = ArduinoMega('COM7', baudrate=115200)
it = util.Iterator(board)
it.start()
time.sleep(1)  # 초기화 대기

PWM_PINs = [2]
DIR_PINs = [30]
BRK_PINs = [38]

pwm_list = [board.get_pin(f'd:{pin}:p') for pin in PWM_PINs]
dir_list = [board.get_pin(f'd:{pin}:o') for pin in DIR_PINs]
brk_list = [board.get_pin(f'd:{pin}:o') for pin in BRK_PINs]

Time_start = time.time()
brk_list[0].write(0)  # 브레이크 해제
print("Start!")

while time.time() - Time_start < 10:

    dir_list[0].write(1)  # 방향 설정
    pwm_list[0].write(1.0)  # 전류 인가 (100%)


pwm_list[0].write(1.0)  # 전류 인가 (100%)
brk_list[0].write(0)  # 브레이크 해제

print("End!")
# 종료 처리
board.exit()