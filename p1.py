import os
import time
import psutil
import tkinter as tk
from tkinter import messagebox, simpledialog

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_memory_info_popup():
    memory_info = psutil.virtual_memory()
    message = (
        f"Total Memory: {memory_info.total} bytes\n"
        f"Available Memory: {memory_info.available} bytes\n"
        f"Used Memory: {memory_info.used} bytes\n"
        f"Memory Usage Percentage: {memory_info.percent}%"
    )
    messagebox.showinfo("Memory Information", message)

def display_dashboard():
    clear_screen()
    print("Memory Management Dashboard\n")
    print("1. Display Memory Information")
    print("2. Monitor Memory Usage of a Specific Application")
    print("3. Exit")
    choice = input("\nEnter your choice: ")
    return choice

def list_running_process_names():
    all_process_names = [proc.info['name'] for proc in psutil.process_iter(attrs=['name'])]
    return all_process_names

def monitor_memory_usage_popup(application_name):
    try:
        while True:
            clear_screen()
            processes = [proc for proc in psutil.process_iter(attrs=['pid', 'name', 'memory_info']) if application_name in proc.info['name']]
            if processes:
                total_memory = sum(proc.info['memory_info'].rss for proc in processes)
                message = f"'{application_name}' Memory Usage: {total_memory} bytes"
            else:
                message = f"No process found with name '{application_name}'"
            messagebox.showinfo("Memory Usage", message)
            time.sleep(2)  # Update every 2 seconds
    except KeyboardInterrupt:
        pass

def main():
    root = tk.Tk()
    root.withdraw()  # Hide the main root window

    while True:
        choice = display_dashboard()

        if choice == "1":
            display_memory_info_popup()
        elif choice == "2":
            all_process_names = list_running_process_names()
            names_display = "\n".join([f"{idx}. {name}" for idx, name in enumerate(all_process_names, start=1)])
            choice = simpledialog.askinteger("Select Process", f"All running process names:\n{names_display}\n\nEnter the number corresponding to the application to monitor:")
            if choice is not None and 1 <= choice <= len(all_process_names):
                application_name = all_process_names[choice - 1]
                monitor_memory_usage_popup(application_name)
            else:
                print("Invalid choice. Please select a valid option.")
        elif choice == "3":
            print("Exiting the Memory Management Dashboard...")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "_main_":
    main()