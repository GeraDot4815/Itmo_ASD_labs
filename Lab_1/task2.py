import csv
class Anket: #Класс анкетируемого, где хранятся его ответы и имя
    def __init__(self, answers, name):
        self.answers=answers
        self.name=name
def ParseAnswers(): #Создаем список с объектами класса Anket
    Ankets=[]
    with open("opros.csv", encoding="utf-8") as file:
        reader=csv.DictReader(file, delimiter=",")
        for row in reader:
            row.pop("time")
            name=row["Имя Фамилия"]
            row.pop("Имя Фамилия")
            answers=list(row.values())
            anket=Anket(answers, name)
            Ankets.append(anket)
    return Ankets
def GetQuestions(): #Достаем из файла вопросы
    Questions=[]
    with open("opros.csv", encoding="utf-8") as file:
        reader=csv.DictReader(file, delimiter=",")
        for row in reader: #Не придумал, как получить заглавную строку с ключами, поэтому такой костыль
            row.pop("time")
            row.pop("Имя Фамилия")
            Questions=list(row.keys())
            break
    return Questions
def StartDialog(Questions, Ankets): #Ответами пользователя заполняем новый список
    NewForm = []
    for quest in Questions:
        print(quest)
        ans = input("Type y/n: ")
        ans = ans.lower()
        if ans == 'y':
            NewForm.append("Да")
        else:
            NewForm.append("Нет")
    flag = False
    for anket in Ankets: #Сравниваем ответы с существующими объектами
        if NewForm == anket.answers:
            print(f"Вы - {anket.name}")
            flag = True
            break
    if not flag: print("Простите, ваши ответы никому не соответствуют.")

if __name__ == "__main__":
    Ankets=ParseAnswers()
    Questions=GetQuestions()
    StartDialog(Questions, Ankets)
