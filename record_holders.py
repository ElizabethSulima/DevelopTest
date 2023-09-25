import unittest


class TestCourses(unittest.TestCase):

    def setUp(self):
        self.courses = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля", "Frontend-разработчик с нуля"]
        self.mentors = [["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
                        ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
                        ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
                        ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]]
        self.durations = [14, 20, 12, 20]
        self.courses_list = []

        for title, mentor, duration in zip(self.courses, self.mentors, self.durations):
            course_dict = {'title': title, 'mentor': mentor, 'duration': duration}
            self.courses_list.append(course_dict)

        self.min_duration = min(self.durations)
        self.max_duration = max(self.durations)
        self.maxes = []
        self.minis = []

        for index, duration in enumerate(self.durations):
            if self.durations[index] == self.max_duration:
                self.maxes.append(index)
            elif self.durations[index] == self.min_duration:
                self.minis.append(index)

        self.courses_min = []
        self.courses_max = []
        for id in self.minis:
            self.courses_min.append(self.courses_list[id]['title'])

        for id in self.maxes:
            self.courses_max.append(self.courses_list[id]['title'])

        def test_min_duration(self):
            self.assertEqual(self.min_duration, 12, 'Самая короткая продолжительность курса должна быть 12 месяцев')

        def test_max_duration(self):
            self.assertEqual(self.max_duration, 20, 'Самая длинная продолжительность курса должна быть 20 месяцев')

        def test_courses_min(self):
            expected_courses_min = ['Python - разработчик с нуля']
            self.assertEqual(self.courses_min, expected_courses_min, 'Некорректно определены курсы с самой короткой продолжительностью')

        def test_courses_max(self):
            expected_courses_max = ['Fullstack - разработчик на Python', 'Frontend - разработчик с нуля']
            self.assertEqual(self.courses_max, expected_courses_max, 'Некорректно определены курсы с самой длинной продолжительностью')


if __name__ == '__main__':
    unittest.main()
