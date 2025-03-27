# Real-Time System Monitor

![Project Banner](https://via.placeholder.com/1000x300?text=Real-Time+System+Monitor)

## Overview

The **Real-Time System Monitor** is a versatile system monitoring tool that provides both a **Graphical User Interface (GUI)** and a **Command-Line Interface (CLI)** to track essential system metrics such as **CPU usage, memory consumption, disk activity, and network statistics**. The GUI leverages **PyQt5** and **PyQtGraph** for visualization, while the CLI version provides real-time updates in the terminal.

## Features

### 🖥️ GUI Application
- Displays real-time system metrics:
  - **CPU Usage**
  - **Memory Usage**
  - **Disk Usage**
  - **Network Activity**
- Interactive real-time graphs for performance monitoring.
- Alerts for high CPU and memory usage.
- 
## Installation

### Prerequisites
Ensure you have **Python 3.6+** installed on your system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/OS-monitor.git
   cd OS-monitor
   ```
2. Install the required dependencies:
   ```bash
   pip install pyqt5 pyqtgraph psutil numpy matplotlib py-cpuinfo
   ```

## Usage

### 🚀 Running the GUI Application
```bash
python main.py
```
This launches the graphical interface, displaying system metrics and real-time graphs.

## Project Structure

```
OS-monitor/
├── GUI.py          # GUI-based system monitor
├── monitor.py      # CLI-based system monitor
├── LICENSE         # License information
├── README.md       # Project documentation
└── requirements.txt # List of required dependencies
```

## Screenshots

### 🖥️ GUI Application
![GUI Screenshot](https://via.placeholder.com/800x400?text=GUI+Screenshot)

### 📊 CLI Application
![CLI Screenshot](https://via.placeholder.com/800x400?text=CLI+Screenshot)

## Contributing

🚀 Contributions are welcome! If you find a bug or have an idea for a new feature, feel free to:
- Open an **issue** 📌
- Submit a **pull request** 📥

## License

This project is licensed under the **MIT License**. See the [`LICENSE`](LICENSE) file for details.

## Acknowledgments
- [PyQt5 Documentation](https://riverbankcomputing.com/software/pyqt/intro)
- [PyQtGraph Documentation](http://www.pyqtgraph.org/)
- [psutil Documentation](https://psutil.readthedocs.io/)

---
⭐ If you find this project useful, consider giving it a star on [GitHub](https://github.com/your-username/OS-monitor)!

