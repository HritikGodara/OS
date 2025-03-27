import psutil
import platform
import cpuinfo

class DataCollector:
    def __init__(self):
        self.cpu_info = self.get_cpu_info()
        self.memory_info = self.get_memory_info()
        self.disk_info = self.get_disk_info()

    def get_cpu_info(self):
        cpu_info = {}
        try:
            cpu_info['name'] = cpuinfo.get_cpu_info()['brand_raw']
        except:
            cpu_info['name'] = "Unknown CPU"

        cpu_info['cores'] = psutil.cpu_count(logical=False)
        cpu_info['logical_cores'] = psutil.cpu_count(logical=True)
        return cpu_info

    def get_memory_info(self):
        memory = psutil.virtual_memory()
        return {
            'total': memory.total / (1024 ** 3),  # Convert to GB
            'available': memory.available / (1024 ** 3),
            'percent': memory.percent
        }

    def get_disk_info(self):
        disk = psutil.disk_usage('/')
        return {
            'total': disk.total / (1024 ** 3),  # Convert to GB
            'used': disk.used / (1024 ** 3),
            'free': disk.free / (1024 ** 3),
            'percent': disk.percent
        }

    def get_disk_usage(self):
        return psutil.disk_usage('/').percent

    def get_network_usage(self):
        io_counters = psutil.net_io_counters()
        return {
            'sent': io_counters.bytes_sent / 1024 / 1024,  # Convert to MB
            'recv': io_counters.bytes_recv / 1024 / 1024  # Convert to MB
        }

    def get_cpu_usage(self):
        return psutil.cpu_percent()

    def get_memory_usage(self):
        return psutil.virtual_memory().percent