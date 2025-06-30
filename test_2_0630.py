import serial
import time
import numpy as np
from ArduinoConnect import ArduinoConnect
from collections import deque

AC = ArduinoConnect('COM7', 115200)


freq = 0.2
pwmMax = 255

INA_time = []
INA_data = []
PWM_time = []
PWM_data = []

start_time = time.time()

# 전류 평균용 버퍼 (최근 10개 샘플)
AVG_SIZE = 10
current_buffer = deque(maxlen=AVG_SIZE)

def update(frame):
    t = time.time() - start_time

    # 20초 지나면 종료 신호 전송
    if t >= 20:
        print("Stopping...")
        ser.write(b'999\n')
        time.sleep(1)
        plt.close()
        return

    duty = 0.75 + 0.25 * np.sin(2 * np.pi * freq * t)
    pwm_value = int(duty * pwmMax)
    ser.write(f"{pwm_value}\n".encode())

    line = ser.readline().decode().strip()
    try:
        current_A = float(line)
    except:
        current_A = 0

    # 버퍼에 새 전류값 추가
    current_buffer.append(current_A)

    # 버퍼 평균 계산
    avg_current = sum(current_buffer) / len(current_buffer)

    print(f"Duty: {duty:.2f}, PWM: {pwm_value}, Current: {current_A:.4f} A, Avg Current: {avg_current:.4f} A")

    x_data.append(t)
    y_data.append(avg_current)
    pwm_normalized = PWM_Sampled / 255
    z_data.append(pwm_normalized)

    ax.clear()
    ax.plot(x_data, y_data, label='Avg Current (A)')
    ax.plot(x_data, z_data, label='PWM (scaled)')
    ax.set_ylim(0, 2)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Average Current (A)')

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=20)

plt.show()

ser.close()
print(x_data.size)