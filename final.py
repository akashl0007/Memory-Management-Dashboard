import os
import time
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_dashboard():
    clear_screen()
    print("Dynamic Memory Management Dashboard\n")
    print("1. Display Memory Information")
    print("2. Allocate Memory for an Application")
    print("3. Monitor Memory Usage of an Application")
    print("4. Deallocate Memory for an Application")
    print("5. Display Allocated Application Memory")
    print("6. Exit")
    choice = input("\nEnter your choice: ")
    return choice

def display_memory_info():
    print("\nMemory Information:")
    # Simulated memory values
    total_memory = 8192  # Total system memory
    available_memory = total_memory - sum(app['memory_allocated'] for app in applications)
    used_memory = total_memory - available_memory
    memory_usage_percentage = (used_memory / total_memory) * 100

    print(f"Total Memory: {total_memory} bytes")
    print(f"Available Memory: {available_memory} bytes")
    print(f"Used Memory: {used_memory} bytes")
    print(f"Memory Usage Percentage: {memory_usage_percentage:.2f}%")
    input("\nPress Enter to continue...")

# New function to allocate application memory
def allocate_application_memory(application_name):
    memory_allocated = random.randint(100, 1000)  # Simulated memory allocation size

    application_info = {
        'name': application_name,
        'memory_allocated': memory_allocated
    }

    applications.append(application_info)
    print(f"Memory allocated for '{application_name}': {memory_allocated} bytes")

def monitor_application_memory(application_name):
    try:
        while True:
            clear_screen()
            print(f"Monitoring Memory Usage of '{application_name}' (Press Ctrl+C to stop)...\n")
            app = next((app for app in applications if app['name'] == application_name), None)
            
            if app:
                total_memory = 8192  # Simulated total system memory
                used_memory = sum(app['memory_allocated'] for app in applications if app['name'] == application_name)
                memory_percentage = (used_memory / total_memory) * 100

                print(f"Total System Memory: {total_memory} bytes")
                print(f"'{application_name}' Memory Usage: {used_memory} bytes")
                print(f"Memory Usage Percentage by '{application_name}': {memory_percentage:.2f}%")
            else:
                print(f"No application found with name '{application_name}'")
            time.sleep(1.5)  # Update every 1.5 seconds
    except KeyboardInterrupt:
        pass

# New function to stop a running application
def stop_running_application(application_name):
    app = next((app for app in applications if app['name'] == application_name), None)
    if app:
        applications.remove(app)
        print(f"'{application_name}' has been stopped and memory deallocated.")
    else:
        print(f"No running application found with name '{application_name}'")

def display_application_memory():
    clear_screen()
    print("Allocated Application Memory\n")
    for app in applications:
        print(f"Application: {app['name']}\tAllocated Memory: {app['memory_allocated']} bytes")
    input("\nPress Enter to continue...")

def main():
    while True:
        choice = display_dashboard()

        if choice == "1":
            display_memory_info()
        elif choice == "2":
            application_name = input("Enter the name of the application to allocate memory for: ")
            allocate_application_memory(application_name)
        elif choice == "3":
            application_name = input("Enter the name of the application to monitor memory for: ")
            monitor_application_memory(application_name)
        elif choice == "4":
            application_name = input("Enter the name of the application to stop: ")
            stop_running_application(application_name)
        elif choice == "5":
            display_application_memory()
        elif choice == "6":
            print("Exiting the Dynamic Memory Management Dashboard...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    applications = []  # List to store application memory information
    main()
