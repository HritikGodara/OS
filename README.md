# 🖥️ Real-Time System Monitoring Dashboard


## 🌟 Overview

The **Real-Time System Monitoring Dashboard** is a Python-based application that provides a graphical interface for monitoring system metrics in real-time. It allows users to track CPU, memory, disk, and network usage, manage processes, and export data for analysis.

This project is divided into three main modules for better organization and maintainability:

- **📊 Data Collection**: Gathers system metrics using libraries like `psutil`, `platform`, and `cpuinfo`.
- **🧮 Data Processing**: Processes and organizes the collected data for visualization.
- **🖼️ GUI**: Implements an interactive graphical interface using `PyQt5` and `pyqtgraph`.

---

## ✨ Features

- **Real-Time Monitoring**: Track CPU, memory, disk, and network usage with live updates.
- **Interactive Graphs**: Visualize system metrics with dynamic plots.
- **Process Management**: View, filter, and terminate processes directly from the interface.
- **Search Functionality**: Quickly find processes using the search bar.
- **Start/Stop Monitoring**: Control the monitoring process with a single click.
- **Data Export**: Export collected data for further analysis.

---

## 🛠️ Modules

### 1. **Data Collection (`data_collector.py`)** 📥
- **Purpose**: Collects real-time system metrics.
- **Key Features**:
  - CPU information (name, cores, usage).
  - Memory and disk usage.
  - Network activity.

### 2. **Data Processing (`data_processor.py`)** 🧮
- **Purpose**: Processes and organizes raw data for visualization.
- **Key Features**:
  - Maintains a fixed-size window of recent data using `collections.deque`.
  - Prepares data for real-time plotting.

### 3. **Graphical User Interface (`GUI.py`)** 🖼️
- **Purpose**: Provides an interactive dashboard for monitoring and managing system metrics.
- **Key Features**:
  - Displays system information and real-time metrics.
  - Interactive plots for CPU, memory, disk, and network usage.
  - Process management with filtering and termination options.

---

## 🚀 Getting Started

### 1. **Clone the Repository**
```bash
git clone [repository_url]
cd OS-master
```

### 2. **Set Up a Virtual Environment**
```bash
python -m venv venv
```

### 3. **Activate the Virtual Environment**
- On **Windows**:
  ```bash
  venv\Scripts\activate
  ```
- On **macOS/Linux**:
  ```bash
  source venv/bin/activate
  ```

### 4. **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 5. **Run the Application**
```bash
python main.py
```

---

## 🖼️ Screenshots

### 📊 Dashboard
![Screenshot 2025-04-17 232425](https://github.com/user-attachments/assets/69c20bcb-5062-4c96-9695-57b33e2cf342)

### 🔍 Process Management
![Screenshot 2025-04-17 232259](https://github.com/user-attachments/assets/0bb59c16-4ede-4576-8b74-319c9bc3d817)

---

## 📚 Libraries Used

- **[PyQt5](https://pypi.org/project/PyQt5/)**: For creating the graphical user interface.
- **[pyqtgraph](https://www.pyqtgraph.org/)**: For plotting real-time graphs.
- **[psutil](https://pypi.org/project/psutil/)**: For retrieving system metrics.
- **[cpuinfo](https://pypi.org/project/py-cpuinfo/)**: For fetching CPU details.
- **[numpy](https://numpy.org/)**: For numerical operations.

---

## 🧑‍💻 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request. Please ensure your code adheres to the project's coding standards.

---

## 🛡️ License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

For any questions or feedback, feel free to reach out:

- **Email**: [your_email@example.com](mailto:arinchoubey9@gmail.com)
- **GitHub**: [Your GitHub Profile](https://github.com/Anonymous-0143)

---

## 🌟 Acknowledgments

- Thanks to the developers of `PyQt5`, `pyqtgraph`, and `psutil` for their amazing libraries.
- Inspired by the need for efficient system monitoring tools.

---

## 🛠️ Future Enhancements

- Add support for monitoring GPU usage.
- Implement advanced filtering and sorting for processes.
- Enable saving and loading of monitoring sessions.

---

