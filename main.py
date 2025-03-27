import sys
from PyQt5.QtWidgets import QApplication
from data_collector import DataCollector
from data_processor import DataProcessor
from GUI import GUI


def main():
    app = QApplication(sys.argv)

    data_collector = DataCollector()
    data_processor = DataProcessor()

    gui = GUI(data_collector, data_processor)
    gui.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()