# используется для сортировки
from operator import itemgetter


class Student:
    """Студент"""

    def __init__(self, id, fio, scholarship, group_id):
        self.id = id
        self.fullname = fio
        self.scholarship = scholarship
        self.group_id = group_id


class Group:
    """Группа"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class StudentGroup:
    """
    'Студенты группы' для реализации
    связи многие-ко-многим
    """

    def __init__(self, group_id, stud_id):
        self.group_id = group_id
        self.stud_id = stud_id


# Группы
groups = [
    Group(1, 'АК1-31'),
    Group(2, 'АК3-52'),
    Group(3, 'ФН12-32Б'),
    Group(4, 'АК1-32'),
    Group(5, 'АК3-51'),
    Group(6, 'ФН12-31Б'),
    Group(7, 'ИУ5-34Б'),
    Group(8, 'PREP-12')
]

# Студенты
students = [
    Student(1, 'Абуховский', 3500, 1),
    Student(2, 'Бондаренко', 9000, 2),
    Student(3, 'Козлов', 0, 3),
    Student(4, 'Гордеев', 0, 7),
    Student(5, 'Коновалов', 100000, 5),
    Student(6, 'Барабанщиков', 12000, 7),
    Student(7, "Милевич", 3500, 4)
]

studs_groups = [
    StudentGroup(1, 1),
    StudentGroup(2, 2),
    StudentGroup(3, 3),
    StudentGroup(4, 7),
    StudentGroup(5, 5),
    StudentGroup(7, 4),
    StudentGroup(7, 6),
    StudentGroup(8, 6)
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(s.fullname, s.scholarship, g.name)
                   for g in groups
                   for s in students
                   if s.group_id == g.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(g.name, sg.group_id, sg.stud_id)
                         for g in groups
                         for sg in studs_groups
                         if g.id == sg.group_id]

    many_to_many = [(s.fullname, s.scholarship, group_name)
                    for group_name, group_id, stud_id in many_to_many_temp
                    for s in students if s.id == stud_id]

    print('Задание Г1')
    res1 = {}
    # Перебираем все отделы
    for g in groups:
        if 'А' == g.name[0]:
            # Список сотрудников отдела
            g_studs = list(filter(lambda i: i[2] == g.name, many_to_many))
            # Только ФИО сотрудников
            g_studs_names = [x for x, _, _ in g_studs]
            # Добавляем результат в словарь
            # ключ - отдел, значение - список фамилий
            res1[g.name] = g_studs_names
    print(res1)

    print('\nЗадание Г2')
    res_2_unsorted = []
    # Перебираем все отделы
    for g in groups:
        # Список сотрудников отдела
        g_studs = list(filter(lambda i: i[2] == g.name, one_to_many))
        # Если отдел не пустой
        if len(g_studs) > 0:
            g_scholarship_max = max(g_studs, key=lambda x: x[1])[1]
            res_2_unsorted.append((g.name, g_scholarship_max))

    # Сортировка по суммарной зарплате
    res_2 = sorted(res_2_unsorted, key=itemgetter(1), reverse=True)
    print(res_2)

    print('\nЗадание Г3')
    res_3 = sorted(many_to_many, key=itemgetter(2))
    print(res_3)


if __name__ == '__main__':
    main()
