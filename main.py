import os
import subprocess

def check_adb_installed():
    """يتأكد إن adb متثبت."""
    try:
        subprocess.run(["adb", "version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True
    except Exception:
        return False

def run_adb_command(command):
    """يشغل أمر adb ويرجع الناتج."""
    try:
        result = subprocess.run(f'adb {command}', shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ خطأ في تنفيذ الأمر: {e.stderr.strip()}")

def list_menu():
    print("\n📱 DroidHelper - أدوات أندرويد بسيطة")
    print("1. عرض معلومات النظام")
    print("2. استخراج مسار تطبيق")
    print("3. تشغيل تطبيق")
    print("4. قراءة لوجات (logcat)")
    print("5. نسخ ملف من الجهاز إلى الكمبيوتر")
    print("6. نسخ ملف من الكمبيوتر إلى الجهاز")
    print("7. خروج")

def copy_from_device():
    source = input("اكتب مسار الملف على الجهاز: ")
    dest = input("اكتب مسار الحفظ على الكمبيوتر: ")
    run_adb_command(f"pull {source} {dest}")

def copy_to_device():
    source = input("اكتب مسار الملف على الكمبيوتر: ")
    dest = input("اكتب مسار الحفظ على الجهاز: ")
    run_adb_command(f"push {source} {dest}")

def main():
    if not check_adb_installed():
        print("❌ adb غير مثبت أو غير موجود في PATH. ثبت adb وجرب مرة أخرى.")
        return

    while True:
        list_menu()
        choice = input("اختر رقم: ")

        if choice == "1":
            run_adb_command("shell getprop ro.build.version.release")
        elif choice == "2":
            package = input("اكتب اسم الحزمة (package name): ")
            run_adb_command(f"shell pm path {package}")
        elif choice == "3":
            package = input("اكتب اسم الحزمة (package name): ")
            run_adb_command(f"shell monkey -p {package} -c android.intent.category.LAUNCHER 1")
        elif choice == "4":
            run_adb_command("logcat -d | tail -n 20")
        elif choice == "5":
            copy_from_device()
        elif choice == "6":
            copy_to_device()
        elif choice == "7":
            print("مع السلامة 👋")
            break
        else:
            print("❌ خيار غير صحيح، حاول مرة أخرى.")

if __name__ == "__main__":
    main()
