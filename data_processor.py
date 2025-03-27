from collections import deque
import numpy as np

class DataProcessor:
    def __init__(self, data_length=50):
        self.data_length = data_length
        self.cpu_data = deque([0] * self.data_length, maxlen=self.data_length)
        self.memory_data = deque([0] * self.data_length, maxlen=self.data_length)
        self.disk_data = deque([0] * self.data_length, maxlen=self.data_length)
        self.network_data = deque([0] * self.data_length, maxlen=self.data_length)
        self.time_data = np.arange(self.data_length)

    def update_data(self, cpu_usage, memory_usage, disk_usage, network_usage):
        self.cpu_data.append(cpu_usage)
        self.memory_data.append(memory_usage)
        self.disk_data.append(disk_usage)
        self.network_data.append(network_usage)

    def get_data(self):
        return {
            'cpu': list(self.cpu_data),
            'memory': list(self.memory_data),
            'disk': list(self.disk_data),
            'network': list(self.network_data),
            'time': self.time_data
        }