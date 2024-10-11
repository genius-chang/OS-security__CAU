import time
import threading

def process(name, duration):
    for i in range(duration):
        print(f"{name} is running... {i+1}")
        time.sleep(1)

def timer_interrupt():
    while True:
        time.sleep(5)  # Timer interval: 5 seconds
        print("Timer interrupt: Switching process!")

# Run the timer interrupt in a separate thread
interrupt_thread = threading.Thread(target=timer_interrupt)
interrupt_thread.daemon = True
interrupt_thread.start()

# Run processes A and B
process("Process A", 10)
process("Process B", 10)

