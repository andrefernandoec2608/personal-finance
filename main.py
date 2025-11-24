from application import Application
from menu.main_menu import run_main_menu

def main():
    app = Application()
    app.run()
    run_main_menu(app)

if __name__ == "__main__":
    main()