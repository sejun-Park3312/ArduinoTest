import time
from pyfirmata2 import ArduinoMega, util

board = ArduinoMega('COM7')
it = util.Iterator(board)
it.start()
time.sleep(1)

start_time = time.time()
board.digital[13].write(1)
end_time = time.time()

latency_ms = (end_time - start_time) * 1000
print(f"pyfirmata2 write latency: {latency_ms:.6f} ms")

board.exit()
