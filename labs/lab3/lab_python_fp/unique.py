# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.index = 0
        self.used = set()
        self.ignore_case = kwargs.get("ignore_case", False)
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
            try:
                current = next(self.items)
            except TypeError:
                if self.index >= len(self.items):
                    raise StopIteration
                else:
                    current = self.items[self.index]
                    self.index += 1
            finally:
                if current not in self.used:
                    if not self.ignore_case:
                        try:
                            self.used.add(current.lower())
                        except:
                            self.used.add(current)
                    else:
                        self.used.add(current)
                    return current

    def __iter__(self):
        return self
