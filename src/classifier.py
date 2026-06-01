class Classifier:
    def init(self):
        self.rules = {
            "spam": [
                "заблокирован", "подтвердите пароль", "выиграли",
                "перейдите по ссылке", "срочно обновите", "бесплатно",
                "verify your account", "click here"
            ],
            "incidents": [
                "недоступен", "не работает", "не могу войти", "ошибка",
                "сбой", "err_", "не отвечает", "critical",
                "доступ запрещён", "не запускается", "статус"
            ],
            "monitoring": [
                "автоматическое уведомление", "мониторинг", "no-reply",
                "noreply", "monitoring.internal", "cpu usage",
                "сгенерировано автоматически", "healthcheck"
            ],
            "requests": [
                "нужны права", "нужен доступ", "новый сотрудник",
                "заявка", "предоставить доступ", "больничный",
                "отпуск", "созвон", "предлагаю", "оформление"
            ],
        }
        
    def classify(self, email):
        text = (email.subject + " " + email.body + " " + email.sender).lower()
        scores = {}
        for category, keywords in self.rules.items():
            scores[category] = sum(1 for w in keywords if w in text)
        best = max(scores, key=lambda c: scores[c])
        if scores[best] == 0:
            return "other"
        return best
