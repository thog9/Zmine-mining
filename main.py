import os
import sys
import io
import asyncio
import inspect
from colorama import init, Fore, Style
import inquirer

init(autoreset=True)

if not getattr(sys, "_zm_utf8", False):
    try:
        sys.stdout.flush()
        sys.stderr.flush()
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", line_buffering=True)
        sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8", line_buffering=True)
        sys._zm_utf8 = True
    except Exception:
        pass

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
os.chdir(_HERE)

BORDER_WIDTH = 80

def print_border(text: str, color=Fore.CYAN, width=BORDER_WIDTH):
    text = text.strip()
    if len(text) > width - 4:
        text = text[:width - 7] + "..."
    padded_text = f" {text} ".center(width - 2)
    print(f"{color}┌{'─' * (width - 2)}┐{Style.RESET_ALL}")
    print(f"{color}│{padded_text}│{Style.RESET_ALL}")
    print(f"{color}└{'─' * (width - 2)}┘{Style.RESET_ALL}")

def _banner():
    banner = r"""

    
░
████████╗██╗░░██╗░█████╗░░██████╗░████████╗░█████╗░░█████╗░██╗░░░░░██╗░░██╗██╗░░░██╗██████╗░
╚══██╔══╝██║░░██║██╔══██╗██╔════╝░╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██║░░██║██║░░░██║██╔══██╗
░░░██║░░░███████║██║░░██║██║░░██╗░░░░██║░░░██║░░██║██║░░██║██║░░░░░███████║██║░░░██║██████╦╝
░░░██║░░░██╔══██║██║░░██║██║░░╚██╗░░░██║░░░██║░░██║██║░░██║██║░░░░░██╔══██║██║░░░██║██╔══██╗
░░░██║░░░██║░░██║╚█████╔╝╚██████╔╝░░░██║░░░╚█████╔╝╚█████╔╝███████╗██║░░██║╚██████╔╝██████╦╝
░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░░╚═════╝░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝░░╚═╝░╚═════╝░╚═════╝░


    """
    print(f"{Fore.GREEN}{banner:^80}{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
    print_border("ZMINE AUTOMATION SUITE", Fore.GREEN)
    print(f"{Fore.YELLOW}│ {'Website'}: {Fore.CYAN}https://thogtoolhub.com/{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Discord'}: {Fore.CYAN}https://discord.gg/MnmYBKfHQf{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}│ {'Channel Telegram'}: {Fore.CYAN}https://t.me/thogairdrops{Style.RESET_ALL}")
    print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")

def _clear():
    os.system('cls' if os.name == 'nt' else 'clear')

async def run_register(language):
    from scripts.register import run_register
    await run_register(language)

async def run_login(language):
    from scripts.login import run_login
    await run_login(language)

async def run_mining(language):
    from scripts.mining import run_mining
    await run_mining(language)

async def run_connectX(language):
    from scripts.connectX import run_connectX
    await run_connectX(language)

async def run_socialX(language):
    from scripts.socialX import run_socialX
    await run_socialX(language)

async def run_quiz(language):
    from scripts.quiz import run_quiz
    await run_quiz(language)

async def run_test_ai(language):
    from scripts.quiz import test_ai
    await test_ai(language)

async def cmd_exit(language: str):
    messages = {"vi": "Đang thoát...", "en": "Exiting..."}
    print_border(messages[language], Fore.GREEN)
    sys.exit(0)

SCRIPT_MAP = {
    "register": run_register,
    "login": run_login,
    "mining": run_mining,
    "connectx": run_connectX,
    "socialx": run_socialX,
    "quiz": run_quiz,
    "testai": run_test_ai,
    "exit": cmd_exit
}

def get_available_scripts(language):
    scripts = {
        'vi': [
            {"name": "1. Đăng ký tài khoản mới", "value": "register"},
            {"name": "2. Đăng nhập từ pvkey.txt", "value": "login"},
            {"name": "3. Kích hoạt đào 24h", "value": "mining"},
            {"name": "4. Liên kết tài khoản X", "value": "connectx"},
            {"name": "5. Làm task Social X", "value": "socialx"},
            {"name": "6. Giải Quiz SI", "value": "quiz"},
            {"name": "7. Kiểm tra AI ( ai.json )", "value": "testai"},
            {"name": "X. Thoát", "value": "exit"},
        ],
        'en': [
            {"name": "1. Register New Account", "value": "register"},
            {"name": "2. Login From pvkey.txt", "value": "login"},
            {"name": "3. Activate Mining 24h", "value": "mining"},
            {"name": "4. Link X Account", "value": "connectx"},
            {"name": "5. Do Social X Tasks", "value": "socialx"},
            {"name": "6. Solve SI Quiz", "value": "quiz"},
            {"name": "7. Test AI ( ai.json )", "value": "testai"},
            {"name": "X. Exit", "value": "exit"},
        ]
    }
    return scripts[language]

def run_script(script_func, language):
    if inspect.iscoroutinefunction(script_func):
        asyncio.run(script_func(language))
    else:
        script_func(language)

def select_language():
    while True:
        _clear()
        _banner()
        print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("CHỌN NGÔN NGỮ / SELECT LANGUAGE", Fore.YELLOW)
        questions = [
            inquirer.List('language',
                          message=f"{Fore.CYAN}Vui lòng chọn / Please select:{Style.RESET_ALL}",
                          choices=[("1. Tiếng Việt", 'vi'), ("2. English", 'en')],
                          carousel=True)
        ]
        answer = inquirer.prompt(questions)
        if answer and answer['language'] in ['vi', 'en']:
            return answer['language']
        print(f"{Fore.RED}❌ {'Lựa chọn không hợp lệ / Invalid choice':^76}{Style.RESET_ALL}")

def main():
    _clear()
    _banner()
    language = select_language()

    messages = {
        "vi": {
            "running": "Đang thực thi: {}",
            "completed": "Đã hoàn thành: {}",
            "error": "Lỗi: {}",
            "press_enter": "Nhấn Enter để tiếp tục...",
            "menu_title": "MENU CHÍNH",
            "select_script": "Chọn script để chạy"
        },
        "en": {
            "running": "Running: {}",
            "completed": "Completed: {}",
            "error": "Error: {}",
            "press_enter": "Press Enter to continue...",
            "menu_title": "MAIN MENU",
            "select_script": "Select script to run"
        }
    }

    while True:
        _clear()
        _banner()
        print(f"{Fore.YELLOW}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border(messages[language]["menu_title"], Fore.YELLOW)
        print(f"{Fore.CYAN}│ {messages[language]['select_script'].center(BORDER_WIDTH - 4)} │{Style.RESET_ALL}")

        available_scripts = get_available_scripts(language)
        questions = [
            inquirer.List('script',
                          message=f"{Fore.CYAN}{messages[language]['select_script']}{Style.RESET_ALL}",
                          choices=[script["name"] for script in available_scripts],
                          carousel=True)
        ]
        answers = inquirer.prompt(questions)
        if not answers:
            continue

        selected_script_name = answers['script']
        selected_script = next(script for script in available_scripts if script["name"] == selected_script_name)
        selected_script_value = selected_script["value"]

        script_func = SCRIPT_MAP.get(selected_script_value)
        if script_func is None:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(f"{'Chưa triển khai / Not implemented'}: {selected_script_name}", Fore.RED)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
            continue

        try:
            print(f"{Fore.CYAN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["running"].format(selected_script_name), Fore.CYAN)
            run_script(script_func, language)
            print(f"{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["completed"].format(selected_script_name), Fore.GREEN)
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")
        except Exception as e:
            print(f"{Fore.RED}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
            print_border(messages[language]["error"].format(str(e)), Fore.RED)
            print('')
            input(f"{Fore.YELLOW}⏎ {messages[language]['press_enter']}{Style.RESET_ALL:^76}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Fore.GREEN}{'═' * BORDER_WIDTH}{Style.RESET_ALL}")
        print_border("Đã thoát / Exited", Fore.GREEN)
