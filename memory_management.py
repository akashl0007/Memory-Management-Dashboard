import psutil
import os
import time


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def display_dashboard():
    clear_screen()
    print("Memory Management Dashboard\n")
    print("1. Display Memory Information")
    print("2. Monitor Memory Usage")
    print("3. Exit")
    choice = input("\nEnter your choice: ")
    return choice


def display_memory_info():
    memory_info = psutil.virtual_memory()
    print("\nMemory Information:")
    print(f"Total Memory: {memory_info.total} bytes")
    print(f"Available Memory: {memory_info.available} bytes")
    print(f"Used Memory: {memory_info.used} bytes")
    print(f"Memory Usage Percentage: {memory_info.percent}%")
    input("\nPress Enter to continue...")


def monitor_memory_usage():
    print("\nMonitoring Memory Usage (Press Ctrl+C to stop)...\n")
    try:
        while True:
            memory_info = psutil.virtual_memory()
            print(
                f"Used Memory: {memory_info.used} bytes | Memory Usage Percentage: {memory_info.percent}%")
            time.sleep(2)  # Update every 2 seconds
            clear_screen()
    except KeyboardInterrupt:
        pass


def main():
    while True:
        choice = display_dashboard()

        if choice == "1":
            display_memory_info()
        elif choice == "2":
            monitor_memory_usage()
        elif choice == "3":
            print("Exiting the Memory Management Dashboard...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
