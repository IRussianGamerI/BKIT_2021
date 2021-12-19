class StudentGroup:  # Студенты группы для реализации связи многие-ко-многим

    def __init__(self, group_id, stud_id):
        self.group_id = group_id
        self.stud_id = stud_id
