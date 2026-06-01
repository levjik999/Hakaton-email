import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
from email_reader import Email, EmailReader
from classifier import Classifier
def test_incident_classification():
    classifier = Classifier()
    email = Email("test.txt", "Сервер недоступен", "user@corp.ru", "Сервис не работает")
    result = classifier.classify(email)
    assert result == "incidents"

def test_spam_classification():
    classifier = Classifier()
    email = Email("test.txt", "Ваш аккаунт заблокирован", "hacker@bad.com", "Перейдите по ссылке")
    result = classifier.classify(email)
    assert result == "spam"

def test_monitoring_classification():
    classifier = Classifier()
    email = Email("test.txt", "CPU usage 90%", "no-reply@monitoring.internal", "Автоматическое уведомление")
    result = classifier.classify(email)
    assert result == "monitoring"

def test_request_classification():
    classifier = Classifier()
    email = Email("test.txt", "Нужен доступ к 1C", "manager@corp.ru", "Новый сотрудник нужны права")
    result = classifier.classify(email)
    assert result == "requests"

def test_unknown_goes_to_other():
    classifier = Classifier()
    email = Email("test.txt", "", "", "")
    result = classifier.classify(email)
    assert result == "other"

def test_empty_subject_no_crash():
    classifier = Classifier()
    email = Email("test.txt", "", "sender@corp.ru", "какой-то текст")
    result = classifier.classify(email)
    assert result in ["incidents", "requests", "monitoring", "spam", "other"]

def test_missing_folder():
    reader = EmailReader("/несуществующий/путь")
    emails = reader.read_all()
    assert emails == []

def test_empty_body_no_crash():
    classifier = Classifier()
    email = Email("test.txt", "Привет", "someone@corp.ru", "")
    result = classifier.classify(email)
    assert result in ["incidents", "requests", "monitoring", "spam", "other"]
