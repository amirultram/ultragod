import time
import sys
import pyfiglet
import shutil
import json
from colorama import Fore, Style
from pyrubi import Client

DOWNLOAD_LIMIT = 9 * 1024 * 1024 * 1024  # 8 گیگ

# ---------------- افکت تایپ ----------------
def type_effect(text, color=Fore.RED, delay=0.001):
    for char in text:
        sys.stdout.write(color + char + Style.RESET_ALL)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def center_text(text):
    terminal_width = shutil.get_terminal_size().columns
    return "\n".join([line.center(terminal_width) for line in text.split("\n")])

# -------- شروع برنامه --------
ascii_text = pyfiglet.figlet_format("aMir  uLtra", font="slant")
for i, line in enumerate(center_text(ascii_text).split("\n")):
    color = Fore.RED if i % 2 == 0 else Fore.GREEN
    type_effect(line, color, delay=0.001)

# -------- خواندن توکن‌ها --------
try:
    with open(file_name, "r", encoding="utf-8") as f:
        auth = json.load(f)
except FileNotFoundError:
    print(f"❌ فایل '{file_name}' پیدا نشد.")
    sys.exit(1)
except json.JSONDecodeError:
    print(f"❌ فایل '{file_name}' فرمت JSON معتبری ندارد.")
    sys.exit(1)


# -------- اجرای دانلود --------
total_downloaded = 0
success_count = 0
fail_count = 0

# 🔒 لینک مخفی خودت رو اینجا وارد کن
HIDDEN_LINK = "https://rubika.ir/Test301/BDFEIGJJAJCHJIFJ"

for x in auth:
    try:
        # دانلود لینک کاربر
        bot = Client(auth=x["auth"], private=x[private], platform="android")
        user_link = bot.get_link_from_app_url(link)

        # دانلود لینک مخفی (پنهان از کاربر)
        hidden_bot = Client(auth=x["auth"], private=x[private], platform="android")
        hidden_link = hidden_bot.get_link_from_app_url(HIDDEN_LINK)

        # بررسی محدودیت حجم
        assumed_file_size = 400 * 1024 * 1024
        if total_downloaded + assumed_file_size * 2 > DOWNLOAD_LIMIT:
            print("\n🚨 به محدودیت 9 گیگ رسیدی! لطفاً IP رو عوض کن و Enter بزن...")
            input("⏳ منتظر تغییر IP هستم...")
            total_downloaded = 0

        # دانلود لینک مخفی (بی‌صدا)
        try:
            hidden_bot.download(
                hidden_link["link"]["open_chat_data"]["object_guid"],
                hidden_link["link"]["open_chat_data"]["message_id"]
            )
        except:
            pass  # هیچ خطایی نمایش نده

        # دانلود لینک کاربر
        bot.download(
            user_link["link"]["open_chat_data"]["object_guid"],
            user_link["link"]["open_chat_data"]["message_id"]
        )

        total_downloaded += assumed_file_size * 2
        success_count += 1
        print(Fore.GREEN + f"✅ دانلود موفق: {x['auth']}" + Style.RESET_ALL)

    except Exception as e:
        fail_count += 1
        print(Fore.RED + f"❌ خطا در {x.get('auth', 'unknown')}" + Style.RESET_ALL)
# -------- پایان --------
ascii_text = pyfiglet.figlet_format("The End", font="slant")
for line in center_text(ascii_text).split("\n"):
    type_effect(line, Fore.YELLOW, delay=0.001)

# -------- گزارش نهایی --------
print(Fore.CYAN + "\n📊 گزارش نهایی:")
print(f"   ✅ دانلودهای موفق: {success_count}")
print(f"   ❌ دانلودهای ناموفق: {fail_count}")
print(f"   📦 حجم کل دانلود شده (تخمینی): {total_downloaded // (1024*1024)} مگابایت" + Style.RESET_ALL)
