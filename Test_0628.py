import serial
import time
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

ser = serial.Serial('COM7', 115200)
time.sleep(2)

freq = 0.2
pwmMax = 255

x_data = []
y_data = []

start_time = time.time()

def update(frame):
    t = time.time() - start_time

    # 10초 지나면 종료 신호 전송
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

    print(f"Duty: {duty:.2f}, PWM: {pwm_value}, Current: {current_A:.4f} A")

    x_data.append(t)
    y_data.append(current_A)

    ax.clear()
    ax.plot(x_data, y_data)
    ax.set_ylim(0, 2)
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Current (A)')

fig, ax = plt.subplots()
ani = FuncAnimation(fig, update, interval=20)

plt.show()

ser.close()
