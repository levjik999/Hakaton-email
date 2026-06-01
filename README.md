Hakaton-email

Система автоматической классификации корпоративной почты.

Описание

Приложение читает входящие письма из папки inbox/, определяет их категорию и раскладывает по соответствующим папкам. По результатам работы формируется лог-файл.

Категории

Категория     Описание

incidents     Критические инциденты: сервисы недоступны, ошибки

requests      Заявки: доступы, новые сотрудники, запросы

monitoring    Автоматические уведомления от систем мониторинга

spam          Подозрительные и нежелательные письма

other         Письма, не попавшие ни в одну из категорий

Структура проекта

hakaton-email/

├── inbox/

├── src/

│   ├── main.py

│   ├── email\_reader.py

│   ├── classifier.py

│   ├── file\_handler.py

│   └── report.py

├── tests/

│   └── test\_classifier.py

├── run.sh

└── README.md

Запуск

bash

bash run.sh

Или напрямую:

bash

python3 src/main.py

Запуск тестов

bash

pytest tests/test\_classifier.py -v



Требования

Python 3.8+

pytest

