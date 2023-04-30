import os
import time


ESC_RED = "\033[0;31m"
ESC_GREEN = "\033[0;32m"
ESC_YELLOW = "\033[0;33m"
ESC_RESET = "\033[0m"


FRAMES = [
    f"{ESC_RED}Frame 1{ESC_RESET}",
    f"{ESC_GREEN}Frame 2{ESC_RESET}",
    f"{ESC_YELLOW}Frame 3{ESC_RESET}"
]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


while True:
    for frame in FRAMES:
        print(frame)
        time.sleep(1)  
        clear_console()  
