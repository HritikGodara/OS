# 🖥️ Real-Time System Monitoring Dashboard

![Real-Time Monitor](https://github.com/user-attachments/assets/8517e182-0a79-4bf5-98d9-456cb850ad69)

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
![Dashboard](https://via.placeholder.com/800x400?text=Dashboard+Screenshot)

### 🔍 Process Management
![Process Management](https://via.placeholder.com/800x400?text=Process+Management+Screenshot)

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

- **Email**: [your_email@example.com](mailto:your_email@example.com)
- **GitHub**: [Your GitHub Profile](https://github.com/yourusername)

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

![Footer](https://github.com/user-attachments/assets/655fbeb5-401d-494d-af1b-cf8d33c2a750)
