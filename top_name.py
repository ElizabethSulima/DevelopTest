import unittest

def get_unique_names(mentors):
    all_list = []
    for m in mentors:
        all_list = mentors[0] + mentors[1] + mentors[2] + mentors[3]
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ', maxsplit=1)
        all_names_list.append(name[0])
    unique_names = list(set(all_names_list))
    all_names_sorted = sorted(unique_names)
    return all_names_sorted

def get_popular_names(mentors):
    all_list = []
    for m in mentors:
        all_list = mentors[0] + mentors[1] + mentors[2] + mentors[3]
    all_names_list = []
    for mentor in all_list:
        name = mentor.split(' ', maxsplit=1)
        all_names_list.append(name[0])
    unique_names = list(set(all_names_list))

    popular = []
    for name in unique_names:
        popular.append([name, all_names_list.count(name)])

    popular.sort(key=lambda x: x[1], reverse=True)

    top_3 = popular[0:3]
    return top_3

class TestMentors(unittest.TestCase):
    def setUp(self):
        self.mentors = [
	    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев", "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков", "Роман Гордиенко"],
	    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев", "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
	    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский", "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
	    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
                       ]

    def test_get_unique_names(self):
        expected_result = [ 'Адилет', 'Александр', 'Алена', 'Азамат', 'Анатолий', 'Анна', 'Антон', 'Вадим', 'Валерий', 'Владимир', 'Денис', 'Дмитрий', 'Евгений', 'Елена', 'Иван', 'Илья', 'Кирилл', 'Константин', 'Максим', 'Михаил', 'Никита', 'Николай', 'Олег', 'Павел', 'Ринат', 'Роман', 'Сергей', 'Татьяна', 'Тимур', 'Хаслер', 'Шмаргунов', 'Шек', 'Шлейко', 'Юрий']