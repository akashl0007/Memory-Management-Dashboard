import subprocess
import time


def clear_screen():
    subprocess.run(['cls'])  # Use 'cls' for Windows


def main():
    clear_screen()
    print("Memory Management Dashboard using TOP\n")

    try:
        while True:
            clear_screen()
            print("Memory Management Dashboard using TOP\n")
            subprocess.run(['top', '-b', '-n', '1'])
            time.sleep(2)  # Update every 2 seconds
    except KeyboardInterrupt:
        print("\nExiting the Memory Management Dashboard...")


if __name__ == "__main__":
    main()
