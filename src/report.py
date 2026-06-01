from datetime import datetime
class Report:
    def __init__(self):
        self.results = []
        self.errors = []

    def add_result(self, filename, category):
        self.results.append((filename, category))

    def add_error(self, filename):
        self.errors.append(filename)

    def print_summary(self):
        print("\n=== Итог обработки ===")
        print(f"Обработано: {len(self.results)}")
        print(f"Ошибок: {len(self.errors)}")

        counts = {}
        for _, cat in self.results:
            counts[cat] = counts.get(cat, 0) + 1

        print("\nПо категориям:")
        for cat, count in sorted(counts.items()):
            print(f"  {cat}: {count}")

        if self.errors:
            print("\nПроблемные файлы:")
            for f in self.errors:
                print(f"  - {f}")

    def save_log(self, log_path):
        with open(log_path, "w", encoding="utf-8") as f:
            f.write(f"Лог от {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            for filename, cat in self.results:
                f.write(f"{filename} -> {cat}\n")
            if self.errors:
                f.write("\nОшибки:\n")
                for err in self.errors:
                    f.write(f"{err}\n")
        print(f"Лог сохранён: {log_path}")
