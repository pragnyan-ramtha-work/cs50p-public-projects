import time
import random

green_text = "\033[32m"
reset_text = "\033[0m"

while True:
    print(green_text + "".join(random.choice("0123456789ABCDEF") for _ in range(50)) + reset_text)
    time.sleep(0.1)
