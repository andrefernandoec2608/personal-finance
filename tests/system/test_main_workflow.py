from application import Application
from menu.main_menu import run_main_menu

def test_main_menu_exit_system(monkeypatch, capsys):
    app = Application()

    inputs = iter(["4"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    from menu import main_menu
    monkeypatch.setattr(main_menu, "ask_yes_no", lambda msg: True)

    run_main_menu(app)

    captured = capsys.readouterr()

    assert "PERSONAL FINANCE MENU" in captured.out
    assert "Goodbye!" in captured.out
