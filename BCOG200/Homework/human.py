import time
from random import randint


class Human:
    def __init__(self, name: str, age: int, sex: str) -> None:
        self.has_brain = True
        self.has_heart = True
        self.name = name
        self.age = age
        self.sex = sex
        self.height = 0
        self.questions = ['Did you take shower?', 'Finished BCOG 200 HW?',
                          'Like BCOG 200?']

    def ask_question(self) -> str:
        question = randint(0, len(self.questions) - 1)
        print(self.questions[question])
        return question

    def answer_question(self, question: str) -> None:
        answers = ['Yes', 'No']
        answer = randint(0, len(answers) - 1)
        print(answers[answer])

    def celebrate_birthday(self) -> None:
        self.age += 1
        print(
            "\nHappy Birthday to {}! {} is now {} years old!".format(self.name,
                                                                     self.name,
                                                                     self.age))

    def get_taller(self) -> int:
        self.height += 1
        return self.height

    def get_name(self) -> str:
        self.name += 'a'
        return '%s%d' % (self.name, self.age)


def main():
    humans = [Human('human1', 10, 'Male'), Human('human2', 10, 'Male')]
    for _ in range(10):
        time.sleep(10)
        human_chosen = randint(0, 1)
        human = humans[human_chosen]
        question = human.ask_question()
        humans[(human_chosen + 1) % 2].answer_question(question)


if __name__ == '__main__':
    main()
