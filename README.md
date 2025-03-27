# Real-Time Process Monitoring Dashboard

## Overview

A graphical dashboard that displays real-time information about process states, CPU usage, and memory consumption. The tool allows administrators to manage processes efficiently and identify potential issues promptly. The application is divided into three modules for better organization and maintainability:

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

- Purpose: Gathers real-time information about system processes from the operating system.
- Role: Acts as the data source for the dashboard, continuously fetching details like process IDs, names, states, CPU usage, and memory consumption. This module ensures the dashboard has up-to-date information to display.

### 2. Data Processing (`data_processor.py`)

- Purpose: Processes and organizes raw data collected from the system into a format suitable for visualization and analysis
- Uses `collections.deque` to maintain a fixed-size window of recent data.
- Role: Filters, sorts, and aggregates process data to make it meaningful for administrators. It may also include basic logic to highlight potential issues, such as high resource usage, without requiring machine learning.

### 3. GUI (`gui.py`)

- Purpose: Provides the graphical interface and visualizations for administrators to interact with the process data.
- Displays real-time system metrics and plots.
- Provides process management functionality.

These modules work together seamlessly: the Data Collection Module feeds raw data to the Data Processing Module, which prepares it for the GUI Module to display.

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
    
## Usage

1.  **Run the application:**

    ```
    python main.py
    ```

2.  **Interact with the GUI:**

    -   Monitor system metrics in real-time.
    -   Use the process management tab to view and terminate processes.
    -   Use the toolbar to start/stop monitoring and export data.

## License

[Specify the license under which the project is released. Example: MIT License]
