# Personal Finance Manager 💸

This is the final project for my first midterm of the **Python Practical Classes**  
in the **Master’s Program at ELTE** 🏦.

It is a **Command-Line Interface (CLI)** application for managing personal finance:  
accounts, transactions, and budgets.  
The project uses **virtual environments**, **pytest**, and a simple modular architecture.

---

## 📦 Project Structure

```
personalfinance/
│
├── exceptions.py
├── managers/
├── menu/
├── model/
├── storage/
└── tests/
    ├── unit/
    ├── integration/
    └── system/
├── utils/
├── app_state.py
├── application.py
├── main.py
├── pytest.ini.py
├── requirements.txt

```

---

## 📥 Install Dependencies

Once the virtual environment is activated:

```bash
pip install -r requirements.txt
```

This installs all required packages (e.g., pytest).

---

## ▶️ Running the Application

With the virtual environment activated:

```bash
python main.py
```

This launches the interactive CLI system.

---

## 🧪 Running Tests

The project includes:

- Unit tests  
- Integration tests  
- System (end-to-end) tests  

Run them all with:

```bash
pytest -vv
```

---

## 📝 Generating `requirements.txt`

If you install new packages inside the virtual environment, regenerate:

```bash
pip freeze > requirements.txt
```

---

## 👨‍💻 Author
[![LinkedIn](https://img.shields.io/badge/LinkedIn-André%20Llumiquinga-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/andre-llc/)
[![GitHub](https://img.shields.io/badge/GitHub-André%20Llumiquinga-black?style=flat&logo=github)](https://github.com/andrefernandoec2608)