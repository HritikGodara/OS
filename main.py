import platform
import psutil
import cpuinfo

print(f"Architecture: {platform.architecture()}")
print(f"Network Name: {platform.node()}")
print(f"Operatinig System: {platform.platform()}")

def get_cpu_usage():
    """Fetch CPU usage percentage."""
    print(f"Processor: {platform.processor()}")

    my_cpuinfo = cpuinfo.get_cpu_info()

    print(f"Full CPU Name: {my_cpuinfo['brand_raw']}")
    print(f"Full CPU Name: {my_cpuinfo['hz_actual_friendly']}")
    print(f"Full CPU Name: {my_cpuinfo['hz_advertised_friendly']}")

    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Fetch memory usage percentage."""
    print(f"Total RAM: {psutil.virtual_memory().total / 1024 / 1024 / 1024:.2f} GB")
    return psutil.virtual_memory().percent


def get_disk_usage():
    """Fetch disk usage statistics."""
    disk_usage = psutil.disk_usage('/')
    return {
        'total': disk_usage.total,
        'used': disk_usage.used,
        'free': disk_usage.free,
        'percent': disk_usage.percent
    }


def get_network_usage():
    """Fetch network I/O statistics."""
    net_io = psutil.net_io_counters()
    return {
        'bytes_sent': net_io.bytes_sent,
        'bytes_recv': net_io.bytes_recv,
        'packets_sent': net_io.packets_sent,
        'packets_recv': net_io.packets_recv
    }

def get_process_info():
    """Fetch information about active processes."""
    process_data = []
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
        try:
            process_data.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    return process_data


def main():
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