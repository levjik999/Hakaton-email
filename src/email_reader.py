import os
import json
class Email:
    def __init__(self, filename, subject, sender, body):
        self.filename = filename
        self.subject = subject
        self.sender = sender
        self.body = body

class EmailReader:
    def __init__(self, inbox_path):
        self.inbox_path = inbox_path

    def read_all(self):
        emails = []
        if not os.path.exists(self.inbox_path):
            print("Папка inbox не найдена")
            return emails
        for filename in os.listdir(self.inbox_path):
            filepath = os.path.join(self.inbox_path, filename)
            if not os.path.isfile(filepath):
                continue
            try:
                if filename.endswith(".json"):
                    email = self._read_json(filepath, filename)
                else:
                    email = self._read_txt(filepath, filename)
                emails.append(email)
            except Exception as e:
                print(f"Не удалось прочитать {filename}: {e}")
        return emails

    def _read_txt(self, filepath, filename):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                text = f.read()
        except UnicodeDecodeError:
            with open(filepath, "r", encoding="latin-1") as f:
                text = f.read()
        subject = ""
        sender = ""
        body = ""
        lines = text.splitlines()
        for i, line in enumerate(lines):
            low = line.lower()
            if low.startswith("тема:") or low.startswith("subject:"):
                subject = line.split(":", 1)[-1].strip()
            elif low.startswith("от кого:") or low.startswith("from:"):
                sender = line.split(":", 1)[-1].strip()
        body = " ".join(lines)
        return Email(filename, subject, sender, body)
    def _read_json(self, filepath, filename):
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
        subject = data.get("subject", "")
        sender = data.get("from", "")
        body = data.get("body", "")
        return Email(filename, subject, sender, body)
