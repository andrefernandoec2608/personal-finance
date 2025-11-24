# Personal Finance Manager (Python CLI)

This is a command–line application for managing personal finance:  
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

## 🔧 Virtual Environment Setup

### 1. Create a virtual environment

```bash
python -m venv venv
```

### 2. Activate it

#### Windows (PowerShell):
```powershell
venv\Scripts\Activate
```

#### Windows (CMD):
```cmd
venv\Scripts\activate.bat
```

#### macOS / Linux:
```bash
source venv/bin/activate
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

This file must be included when submitting the project.

Example:

```
pytest==8.2.0
pluggy==1.4.0
iniconfig==2.0.0
colorama==0.4.6
```

---

## 🚫 Note About Virtual Environments

Do **not** upload the `venv/` folder.  
Use `.gitignore` to exclude it:

```
venv/
```

---

## ✔ Submission Requirements Checklist

- [x] The project runs inside an activated virtual environment  
- [x] `requirements.txt` lists all necessary packages  
- [x] Tests run correctly with pytest  
- [x] No virtual environment is included in the submission  

---

## 📚 License

This project is for educational purposes (BME / Python course).

## 👨‍💻 Author
[![LinkedIn](https://img.shields.io/badge/LinkedIn-André%20Llumiquinga-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/andre-llc/)
[![GitHub](https://img.shields.io/badge/GitHub-André%20Llumiquinga-black?style=flat&logo=github)](https://github.com/andrefernandoec2608)