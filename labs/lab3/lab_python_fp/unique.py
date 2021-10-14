# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.used = set()
        self.ignore_case = kwargs.get("ignore_case", False)
        self.lower_set = set()
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False

    def __next__(self):
        # Нужно реализовать __next__
        current = None
        while True:
            if isinstance(self.items, list):
                if self.index >= len(self.items):
                    raise StopIteration
                else:
                    current = self.items[self.index]
                    self.index += 1
            else:
                current = next(self.items)

            if not self.ignore_case and current not in self.used:
                self.used.add(current)
                return current
            elif self.ignore_case and isinstance(current, str):
                if current.lower() not in self.lower_set:
                    self.used.add(current)
                    self.lower_set.add(current.lower())
                    return current

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = ["A", "B", "a", "b"]
    for i in Unique(data, ignore_case=True):
        print(i)
