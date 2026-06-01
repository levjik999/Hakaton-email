#!/bin/bash

echo "=== Запуск системы обработки почты ==="

if [ ! -d "inbox" ]; then
    echo "Ошибка: папка inbox не найдена"
    exit 1
fi

count=$(ls inbox/ | wc -l)
echo "Найдено файлов в inbox: $count"

echo "Запускаем обработку..."
python3 src/main.py

if [ $? -eq 0 ]; then
    echo "Обработка завершена успешно"
else
    echo "Во время обработки возникла ошибка"
    exit 1
fi