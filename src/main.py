import sys
import os
sys.path.insert(0, os.path.dirname(__file__))
from email_reader import EmailReader
from classifier import Classifier
from file_handler import FileHandler
from report import Report
def main():
    base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    inbox_path = os.path.join(base_path, "inbox")
    print("Запуск обработки почты...")
    reader = EmailReader(inbox_path)
    classifier = Classifier()
    handler = FileHandler(base_path)
    report = Report()
    emails = reader.read_all()
    if not emails:
        print("Писем не найдено.")
        return
    for email in emails:
        category = classifier.classify(email)
        success = handler.move_email(email, category)
        if success:
            report.add_result(email.filename, category)
        else:
            report.add_error(email.filename)

    report.print_summary()
    report.save_log(os.path.join(base_path, "log.txt"))

if __name__ == "__main__":
    main()
