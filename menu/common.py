def ask_yes_no(prompt: str) -> bool:
    while True:
        answer = input(f"{prompt} (y/n): ").strip().lower()
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("Invalid option. Please type Y or N.")

def ask_input_str(prompt: str) -> str:
    while True:
        answer = input(f"{prompt}: ").strip()
        if answer:
            return answer
        print("Please enter a value.")

def ask_input_int(prompt: str) -> str:
    while True:
        answer = input(f"{prompt}: ").strip()
        if answer and answer.isdigit():
            return answer
        print("Please enter a valid integer.")