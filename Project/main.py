from Logic import *

def main():
    application = QApplication([])
    TV_remote = tv_logic()
    TV_remote.show()
    application.exec()

if __name__ == '__main__':
    main()