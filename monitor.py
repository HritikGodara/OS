import platform
import psutil
import time
import matplotlib.pyplot as plt
import numpy as np
import threading

print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operatinig System: {platform.platform()}")

# Initialize data arrays
data_length = 50
cpu_usage_data = np.zeros(data_length)
mem_usage_data = np.zeros(data_length)
disk_usage_data = np.zeros(data_length)
network_usage_data = np.zeros(data_length)
cpu_temp_data = np.zeros(data_length)

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    return psutil.virtual_memory().percent

def alert_system(cpu, memory):
    if cpu > 80:
        print("ALERT: High CPU usage detected!")
    if memory > 80:
        print("ALERT: High Memory usage detected!")

def update_metrics():
    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()['percent']
        network_usage = get_network_usage()['bytes_recv']

        # Shift data and append new values
        cpu_usage_data[:-1] = cpu_usage_data[1:]
        cpu_usage_data[-1] = cpu_usage
        mem_usage_data[:-1] = mem_usage_data[1:]
        mem_usage_data[-1] = memory_usage
        disk_usage_data[:-1] = disk_usage_data[1:]
        disk_usage_data[-1] = disk_usage
        network_usage_data[:-1] = network_usage_data[1:]
        network_usage_data[-1] = network_usage

        alert_system(cpu_usage, memory_usage)

        time.sleep(1)

def get_disk_usage():
    disk_usage = psutil.disk_usage('/')
    return {
        'total': disk_usage.total,
        'used': disk_usage.used,
        'free': disk_usage.free,
        'percent': disk_usage.percent
    }

def plot_metrics():
    plt.ion()
    fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(8, 10))

    while True:
        ax[0].clear()
        ax[1].clear()
        ax[2].clear()

        ax[0].plot(cpu_usage_data, label='CPU Usage (%)', color='r')
        ax[0].plot(mem_usage_data, label='Memory Usage (%)', color='b')
        ax[1].plot(disk_usage_data, label='Disk Usage (%)', color='g')
        ax[1].plot(network_usage_data, label='Network Usage (Bytes Received)', color='m')

        ax[0].set_title('Real-time CPU and Memory Usage')
        ax[1].set_title('Real-time Disk and Network Usage')

        ax[0].legend()
        ax[1].legend()
        ax[2].legend()

        plt.draw()
        plt.pause(2)  # Update the plot every 2 seconds

def get_network_usage():
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def get_process_info():
    process_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_data.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_data

def main():
    update_thread = threading.Thread(target=update_metrics, daemon=True)
    update_thread.start()

    plot_metrics()  # blocks this thread, ensuring the plot updates continuously
    plt.show()

    while True:
        cpu_usage = get_cpu_usage()
        memory_usage = get_memory_usage()
        disk_usage = get_disk_usage()
        network_usage = get_network_usage()
        process_info = get_process_info()

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage['percent']}%")
        print(f"Network - Bytes Sent: {network_usage['bytes_sent']}, Bytes Received: {network_usage['bytes_recv']}")

        print("Active Processes:")
        for proc in process_info:
            print(proc)

        time.sleep(1)

if __name__ == '__main__':
    main()