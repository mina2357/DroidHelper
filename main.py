# DroidHelper - ADB Android Tools
# أداة سطر أوامر بسيطة للتعامل مع أجهزة أندرويد باستخدام ADB
# Author: mina2357
# GitHub: https://github.com/mina2357/DroidHelper

import os

def run_adb_command(command):
    result = os.popen(f'adb {command}').read()
    print(result)

def main():
    print("\n📱 DroidHelper - أدوات أندرويد بسيطة عبر ADB\n")
    print("1. عرض إصدار النظام")
    print("2. استخراج تطبيق (Package Path)")
    print("3. تشغيل تطبيق")
    print("4. قراءة اللوج (logcat)")
    print("5. عرض جميع التطبيقات")
    print("6. حذف تطبيق")
    print("7. نسخ ملف من الهاتف إلى الكمبيوتر")
    print("8. نسخ ملف من الكمبيوتر إلى الهاتف")
    print("9. خروج")

    choice = input("\nاختر رقم: ")

    if choice == "1":
        run_adb_command("shell getprop ro.build.version.release")
    elif choice == "2":
        package = input("اكتب اسم الباكدج: ")
        run_adb_command(f"shell pm path {package}")
    elif choice == "3":
        package = input("اكتب اسم الباكدج: ")
        run_adb_command(f"shell monkey -p {package} -c android.intent.category.LAUNCHER 1")
    elif choice == "4":
        run_adb_command("logcat -d | tail -n 20")
    elif choice == "5":
        run_adb_command("shell pm list packages")
    elif choice == "6":
        package = input("اكتب اسم الباكدج اللي هتحذفه: ")
        run_adb_command(f"uninstall {package}")
    elif choice == "7":
        remote_path = input("📥 اكتب مسار الملف على الهاتف: ")
        local_path = input("💾 اكتب مسار الحفظ على الكمبيوتر: ")
        run_adb_command(f"pull {remote_path} {local_path}")
    elif choice == "8":
        local_path = input("📤 اكتب مسار الملف على الكمبيوتر: ")
        remote_path = input("📱 اكتب مكان الحفظ على الهاتف: ")
        run_adb_command(f"push {local_path} {remote_path}")
    elif choice == "9":
        print("👋 مع السلامة")
    else:
        print("❌ اختيار غير صحيح")

if __name__ == "__main__":
    main()
