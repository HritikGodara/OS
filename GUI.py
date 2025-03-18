import sys
import time
import threading
import psutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel
from pyqtgraph import PlotWidget
import numpy as np
import platform
from PyQt5.QtWidgets import QFrame
import cpuinfo

class SystemMonitor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Real-Time System Monitor")
        self.setGeometry(100, 100, 1000, 800)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        # System Information Labels
        self.sys_info_label = QLabel("System Information")
        self.sys_info_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.layout.addWidget(self.sys_info_label)

        # Get system information
        self.cpu_info = self.get_cpu_info()
        self.memory_info = self.get_memory_info()
        self.disk_info = self.get_disk_info()

        # Add system information labels
        self.layout.addWidget(QLabel(f"CPU: {self.cpu_info['name']}"))
        self.layout.addWidget(
            QLabel(f"Cores: {self.cpu_info['cores']} (Physical), {self.cpu_info['logical_cores']} (Logical)"))
        self.layout.addWidget(QLabel(f"Total RAM: {self.memory_info['total']:.1f} GB"))
        self.layout.addWidget(QLabel(f"Total Disk: {self.disk_info['total']:.1f} GB"))
        self.layout.addWidget(QLabel(f"OS: {platform.platform()}"))

        # Add a separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.layout.addWidget(separator)

        # Labels
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.memory_label = QLabel("Memory Usage: 0%")
        self.disk_label = QLabel("Disk Usage: 0%")
        self.network_label = QLabel("Network Usage: 0 MB")
        self.layout.addWidget(self.cpu_label)
        self.layout.addWidget(self.memory_label)
        self.layout.addWidget(self.disk_label)
        self.layout.addWidget(self.network_label)

        # Plots
        self.cpu_mem_graph = PlotWidget(title="CPU and Memory Usage")
        self.disk_net_graph = PlotWidget(title="Disk and Network Usage")

        self.layout.addWidget(self.cpu_mem_graph)
        self.layout.addWidget(self.disk_net_graph)

        self.central_widget.setLayout(self.layout)

        # Initialize data arrays
        self.data_length = 50
        self.cpu_data = np.zeros(self.data_length)
        self.memory_data = np.zeros(self.data_length)
        self.disk_data = np.zeros(self.data_length)
        self.network_data = np.zeros(self.data_length)
        self.temp_data = np.zeros(self.data_length)
        self.time_data = np.arange(self.data_length)

        # Set up plots
        self.cpu_line = self.cpu_mem_graph.plot(self.time_data, self.cpu_data, pen='r', name='CPU')
        self.mem_line = self.cpu_mem_graph.plot(self.time_data, self.memory_data, pen='b', name='Memory')
        self.disk_line = self.disk_net_graph.plot(self.time_data, self.disk_data, pen='g', name='Disk')
        self.net_line = self.disk_net_graph.plot(self.time_data, self.network_data, pen='m', name='Network')

        # Add legends
        self.cpu_mem_graph.addLegend()
        self.disk_net_graph.addLegend()

        # Start update thread
        self.update_thread = threading.Thread(target=self.update_metrics, daemon=True)
        self.update_thread.start()

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
        return psutil.net_io_counters().bytes_recv / 1024 / 1024  # Convert to MB

    def update_metrics(self):
        while True:
            # Get metrics
            cpu_usage = psutil.cpu_percent()
            memory_usage = psutil.virtual_memory().percent
            disk_usage = self.get_disk_usage()
            network_usage = self.get_network_usage()

            # Update data arrays
            self.cpu_data[:-1] = self.cpu_data[1:]
            self.cpu_data[-1] = cpu_usage
            self.memory_data[:-1] = self.memory_data[1:]
            self.memory_data[-1] = memory_usage
            self.disk_data[:-1] = self.disk_data[1:]
            self.disk_data[-1] = disk_usage
            self.network_data[:-1] = self.network_data[1:]
            self.network_data[-1] = network_usage

            # Update plots
            self.cpu_line.setData(self.time_data, self.cpu_data)
            self.mem_line.setData(self.time_data, self.memory_data)
            self.disk_line.setData(self.time_data, self.disk_data)
            self.net_line.setData(self.time_data, self.network_data)

            # Update labels
            self.cpu_label.setText(f"CPU Usage: {cpu_usage:.1f}%")
            self.memory_label.setText(f"Memory Usage: {memory_usage:.1f}%")
            self.disk_label.setText(f"Disk Usage: {disk_usage:.1f}%")
            self.network_label.setText(f"Network Usage: {network_usage:.1f} MB")

            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    monitor_window = SystemMonitor()
    monitor_window.show()
    sys.exit(app.exec_())