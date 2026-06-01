import os
import shutil
CATEGORIES = ["incidents", "requests", "monitoring", "spam", "other"]
class FileHandler:
    def __init__(self, base_path):
        self.base_path = base_path
        for cat in CATEGORIES:
            folder = os.path.join(base_path, cat)
            if not os.path.exists(folder):
                os.makedirs(folder)

    def move_email(self, email, category):
        if category not in CATEGORIES:
            category = "other"

        src = os.path.join(self.base_path, "inbox", email.filename)
        dst = os.path.join(self.base_path, category, email.filename)

        if not os.path.exists(src):
            print(f"Файл не найден: {email.filename}")
            return False

        try:
            shutil.copy2(src, dst)
            return True
        except Exception as e:
            print(f"Ошибка при перемещении {email.filename}: {e}")
            return False
