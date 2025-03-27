import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QFrame, QTabWidget, QTableView, QLineEdit, QHeaderView, QPushButton, QToolBar, QAction, QStatusBar, QSplitter
from PyQt5.QtCore import QSortFilterProxyModel, Qt, QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem, QIcon
from pyqtgraph import PlotWidget
import numpy as np
import platform
import psutil

class GUI(QMainWindow):
    def __init__(self, data_collector, data_processor):
        super().__init__()
        self.setWindowTitle("Real-Time System Monitor")
        self.setGeometry(100, 100, 1000, 800)

        self.data_collector = data_collector
        self.data_processor = data_processor

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Create toolbar
        self.toolbar = QToolBar("Main Toolbar")
        self.addToolBar(self.toolbar)

        # Add actions to toolbar
        refresh_action = QAction(QIcon("refresh.png"), "Refresh", self)
        refresh_action.setStatusTip("Refresh data")
        refresh_action.triggered.connect(self.update_metrics)
        self.toolbar.addAction(refresh_action)

        start_action = QAction(QIcon("start.png"), "Start", self)
        start_action.setStatusTip("Start monitoring")
        start_action.triggered.connect(self.start_monitoring)
        self.toolbar.addAction(start_action)

        stop_action = QAction(QIcon("stop.png"), "Stop", self)
        stop_action.setStatusTip("Stop monitoring")
        stop_action.triggered.connect(self.stop_monitoring)
        self.toolbar.addAction(stop_action)

        export_action = QAction(QIcon("export.png"), "Export", self)
        export_action.setStatusTip("Export data")
        export_action.triggered.connect(self.export_data)
        self.toolbar.addAction(export_action)

        # Create status bar
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        # Create tab widget
        self.tabs = QTabWidget()
        self.layout.addWidget(self.tabs)

        # Create system info tab
        self.sys_info_tab = QWidget()
        self.sys_info_layout = QVBoxLayout(self.sys_info_tab)
        self.tabs.addTab(self.sys_info_tab, "System Info")

        # System Information Labels
        self.sys_info_label = QLabel("System Information")
        self.sys_info_label.setStyleSheet("font-weight: bold; font-size: 14px;")
        self.sys_info_layout.addWidget(self.sys_info_label)

        # Add system information labels
        self.sys_info_layout.addWidget(QLabel(f"CPU: {self.data_collector.cpu_info['name']}"))
        self.sys_info_layout.addWidget(QLabel(f"Cores: {self.data_collector.cpu_info['cores']} (Physical), {self.data_collector.cpu_info['logical_cores']} (Logical)"))
        self.sys_info_layout.addWidget(QLabel(f"Total RAM: {self.data_collector.memory_info['total']:.1f} GB"))
        self.sys_info_layout.addWidget(QLabel(f"Total Disk: {self.data_collector.disk_info['total']:.1f} GB"))
        self.sys_info_layout.addWidget(QLabel(f"OS: {platform.platform()}"))

        # Add a separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        self.sys_info_layout.addWidget(separator)

        # Labels
        self.cpu_label = QLabel("CPU Usage: 0%")
        self.memory_label = QLabel("Memory Usage: 0%")
        self.disk_label = QLabel("Disk Usage: 0%")
        self.network_label = QLabel("Network Usage: 0 MB")
        self.sys_info_layout.addWidget(self.cpu_label)
        self.sys_info_layout.addWidget(self.memory_label)
        self.sys_info_layout.addWidget(self.disk_label)
        self.sys_info_layout.addWidget(self.network_label)

        # Plots
        self.cpu_mem_graph = PlotWidget(title="CPU and Memory Usage")
        self.disk_net_graph = PlotWidget(title="Disk and Network Usage")

        self.sys_info_layout.addWidget(self.cpu_mem_graph)
        self.sys_info_layout.addWidget(self.disk_net_graph)

        self.cpu_line = self.cpu_mem_graph.plot(self.data_processor.time_data, [0]*len(self.data_processor.time_data), pen='r', name='CPU')
        self.mem_line = self.cpu_mem_graph.plot(self.data_processor.time_data, [0]*len(self.data_processor.time_data), pen='b', name='Memory')
        self.disk_line = self.disk_net_graph.plot(self.data_processor.time_data, [0]*len(self.data_processor.time_data), pen='g', name='Disk')
        self.net_line = self.disk_net_graph.plot(self.data_processor.time_data, [0]*len(self.data_processor.time_data), pen='m', name='Network')

        # Add legends
        self.cpu_mem_graph.addLegend()
        self.disk_net_graph.addLegend()

        # Create process management tab
        self.process_tab = QWidget()
        self.process_layout = QVBoxLayout(self.process_tab)
        self.tabs.addTab(self.process_tab, "Process Management")

        # Search bar for filtering processes
        self.search_bar = QLineEdit()
        self.search_bar.setPlaceholderText("Search processes...")
        self.search_bar.textChanged.connect(self.filter_processes)
        self.process_layout.addWidget(self.search_bar)

        # Process table
        self.process_table = QTableView()
        self.process_layout.addWidget(self.process_table)

        # Model for process table
        self.process_model = QStandardItemModel(0, 5)
        self.process_model.setHorizontalHeaderLabels(["PID", "Name", "CPU %", "Memory %", "Terminate"])
        self.process_table.setModel(self.process_model)
        self.process_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # Proxy model for sorting and filtering
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.process_model)
        self.process_table.setModel(self.proxy_model)
        self.process_table.setSortingEnabled(True)

        # Set up QTimer to update metrics
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_metrics)
        self.timer.start(1000)  # Update every second

    def update_metrics(self):
        cpu_usage = self.data_collector.get_cpu_usage()
        memory_usage = self.data_collector.get_memory_usage()
        disk_usage = self.data_collector.get_disk_usage()
        network_usage = self.data_collector.get_network_usage()

        self.data_processor.update_data(cpu_usage, memory_usage, disk_usage, network_usage['recv'])

        data = self.data_processor.get_data()
        self.cpu_line.setData(data['time'], data['cpu'])
        self.mem_line.setData(data['time'], data['memory'])
        self.disk_line.setData(data['time'], data['disk'])
        self.net_line.setData(data['time'], data['network'])

        self.cpu_label.setText(f"CPU Usage: {cpu_usage:.1f}%")
        self.memory_label.setText(f"Memory Usage: {memory_usage:.1f}%")
        self.disk_label.setText(f"Disk Usage: {disk_usage:.1f}%")
        self.network_label.setText(f"Network Usage: Sent {network_usage['sent']:.1f} MB, Received {network_usage['recv']:.1f} MB")

        self.update_process_table()

    def update_process_table(self):
        process_data = []
        import psutil
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_percent']):
            try:
                process_data.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue

        self.process_model.setRowCount(len(process_data))
        for row, proc in enumerate(process_data):
            self.process_model.setItem(row, 0, QStandardItem(str(proc['pid'])))
            self.process_model.setItem(row, 1, QStandardItem(proc['name']))
            self.process_model.setItem(row, 2, QStandardItem(f"{proc['cpu_percent']:.1f}"))
            self.process_model.setItem(row, 3, QStandardItem(f"{proc['memory_percent']:.1f}"))

            # Add terminate button
            terminate_button = QPushButton("Terminate")
            terminate_button.clicked.connect(lambda _, pid=proc['pid']: self.terminate_process(pid))
            self.process_table.setIndexWidget(self.process_model.index(row, 4), terminate_button)

    def terminate_process(self, pid):
        try:
            proc = psutil.Process(pid)
            proc.terminate()
            proc.wait(timeout=3)
            print(f"Process {pid} terminated successfully.")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.TimeoutExpired) as e:
            print(f"Failed to terminate process {pid}: {e}")

    def filter_processes(self, text):
        self.proxy_model.setFilterRegExp(text)
        self.proxy_model.setFilterKeyColumn(1)  # Filter by process name column

    def start_monitoring(self):
        self.timer.start(1000)
        self.status_bar.showMessage("Monitoring started")

    def stop_monitoring(self):
        self.timer.stop()
        self.status_bar.showMessage("Monitoring stopped")

    def export_data(self):
        # Implement data export functionality
        self.status_bar.showMessage("Data exported")