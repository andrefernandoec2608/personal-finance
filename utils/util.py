import csv
from pathlib import Path

from utils.enums import AccountType, Currency

storage_dir = Path("./storage")
name_account_file = "account_file.csv"

def load_storage_from_cvs (filename: str) -> list[list[str]]:
    file_path = storage_dir / filename

    with file_path.open("r", newline="", encoding="utf-8") as f:
        reader = csv.reader(f)
        return [row for row in reader]
    
def load_storage_to_cvs (filename: str, records: list[list[str]]) -> None:
    file_path = storage_dir / filename

    with file_path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows(records)