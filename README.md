# Real-Time System Monitor

## Overview

This project is a real-time system monitoring application built with Python and PyQt5. It provides a graphical user interface to monitor CPU usage, memory usage, disk usage, network activity, and running processes. The application is divided into three modules for better organization and maintainability:

- **Data Collecting**: Collects system metrics using `psutil`, `platform`, and `cpuinfo`.
- **Data Processing**: Processes and stores collected data using `collections.deque` and `numpy`.
- **GUI**: Implements the graphical user interface using `PyQt5` and `pyqtgraph`.

## Features

- Real-time monitoring of CPU, memory, disk, and network usage.
- Graphical representation of system metrics using plots.
- Process management with the ability to terminate processes.
- Search bar for filtering processes.
- Start/Stop monitoring functionality.
- Data export functionality.

## Modules

### 1. Data Collecting (`data_collector.py`)

- Collects system information and metrics using `psutil`, `platform`, and `cpuinfo`.
- Provides methods to fetch CPU info, memory info, disk info, disk usage, network usage, CPU usage, and memory usage.

### 2. Data Processing (`data_processor.py`)

- Processes and stores collected data.
- Uses `collections.deque` to maintain a fixed-size window of recent data.
- Provides methods to update and retrieve data.

### 3. GUI (`gui.py`)

- Implements the graphical user interface using `PyQt5` and `pyqtgraph`.
- Displays real-time system metrics and plots.
- Provides process management functionality.

## Installation

1.  **Clone the repository:**

    ```
    git clone [repository_url]
    cd [repository_directory]
    ```

2.  **Create a virtual environment:**

    ```
    python -m venv venv
    ```

3.  **Activate the virtual environment:**

    -   On Windows:

        ```
        venv\Scripts\activate
        ```

    -   On macOS and Linux:

        ```
        source venv/bin/activate
        ```

4.  **Install the required packages:**

    ```
    pip install -r requirements.txt
    ```

    Create a `requirements.txt` file with the following content:

    ```
    psutil
    pyqt5
    pyqtgraph
    numpy
    cpuinfo
    ```

## Usage

1.  **Run the application:**

    ```
    python main.py
    ```

2.  **Interact with the GUI:**

    -   Monitor system metrics in real-time.
    -   Use the process management tab to view and terminate processes.
    -   Use the toolbar to start/stop monitoring and export data.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

[Specify the license under which the project is released. Example: MIT License]
