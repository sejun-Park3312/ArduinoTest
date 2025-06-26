import threading
import keyboard
import time

class KeyWaiting:
    def __init__(self):
        self.Waiting = True
        self.OnOff = 0
        self.Q = 0
        self.W = 0
        self.E = 0
        self.PWM = 0
        self.PWM_Rate = 1
        threading.Thread(target = self.StartWaiting, daemon=True).start()

    def On_Key_Event(self, e):
        key = e.name
        if key == 'h':
            self.OnOff = 1
            print("High")

        elif key == 'l':
            self.OnOff = 0
            print("Low")

        elif key == 'q':
            if self.Q == 1:
                self.Q == 0
            else:
                self.Q == 1

        elif key == 'w':
            if self.W == 1:
                self.W == 0
            else:
                self.W == 1

        elif key == 'e':
            if self.E == 1:
                self.E == 0
            else:
                self.E == 1

        elif key == 'up':
            if self.PWM < 255:
                self.PWM = self.PWM + self.PWM_Rate

            if self.PWM > 255:
                self.PWM = 255

            print(f"PWM : {self.PWM:.1f}")

        elif key == 'down':
            if self.PWM > 0:
                self.PWM = self.PWM - self.PWM_Rate

            if self.PWM < 0:
                self.PWM = 0

            print(f"PWM : {self.PWM:.1f}")

        elif key == 'esc':
            self.Waiting = False



    def StartWaiting(self):
        keyboard.on_press(self.On_Key_Event)
        print("KeyWaiting...")
        while self.Waiting:

            time.sleep(0.1)
        print("KeyWaiting End!")



