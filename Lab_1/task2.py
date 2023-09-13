import csv


class Anket:  # Класс анкетируемого, где хранятся его ответы и имя
    def __init__(self, answers, name):
        self.answers = answers
        self.name = name


def parse_answers() -> list[Anket]:  # Создаем список с объектами класса Anket
    allankets = []

    with open("opros.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:
            row.pop("time")  # Этот столбец нам не нужен

            name = row["Имя Фамилия"]  # Получаем имя опрашиваемого
            row.pop("Имя Фамилия")  # Теперь этот столбец нам тоже не нужен

            answers = list(row.values())  # Получаем ответы на все вопросы в виде списка

            anket = Anket(answers, name)  # Создаем экземпляр класса и сохраняем в список
            allankets.append(anket)

    return allankets


def get_questions() -> list[str]:  # Достаем из файла вопросы
    questions = []

    with open("opros.csv", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=",")

        for row in reader:  # Не придумал, как получить заглавную строку с ключами, поэтому такой костыль
            row.pop("time")  # Удаляем ненужные столбцы
            row.pop("Имя Фамилия")

            questions = list(row.keys())  # Получаем все вопросы
            break  # Более одной итерации делать ненужно
    return questions


def check_anket(length: int, answers_form: list[str], anket_form: Anket) -> bool:
    for i in range(length):
        if answers_form[i] != anket_form.answers[i]:
            return False
    return True


def start_dialog(questions: list[str], ankets: list[Anket]):  # Ответами пользователя заполняем новый список
    newform = []
    flag = False
    for i, question in enumerate(questions):
        # Создаем список из анкет, в которых введенные ответы совпадают
        #Для оптимизации эти команды должны выполняться раньше, чем будет задан вопрос
        if i!=0:
                sameankets = [anket for anket in ankets if check_anket(i, newform, anket)]
                if len(sameankets) == 1: #Если существует только одна такая анкета, определяем этого человека
                    print(f"Вы - {sameankets[0].name}")
                    flag = True
                    break
        #Задаем вопрос
        print(question)
        ans = input("Type y/n: ")
        ans = ans.lower()
        if ans == 'y':
            newform.append("Да")
        else:
            newform.append("Нет")

    if not flag: print("Простите, мы не можем определить, кто вы.")


if __name__ == "__main__":
    ankets = parse_answers()
    questions = get_questions()
    start_dialog(questions, ankets)
