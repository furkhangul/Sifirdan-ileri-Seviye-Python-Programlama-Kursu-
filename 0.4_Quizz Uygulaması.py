"""
Bu derste nesne tabanlı programlama üzerinden öğrendiğmiz bilgiler ile
bir quiz uygulaması yapmak olacak.
"""

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def checkAnswer(self, answer):
        return self.answer == answer


class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionIndex = 0

    def getQuestion(self):
        return self.questions[self.questionIndex]

    def displayQuestion(self):
        question = self.getQuestion()
        print(f"Soru {self.questionIndex + 1}: {question.text}")

        for i, choice in enumerate(question.choices):
            print(f"{i + 1}. {choice}")

        answer = input("Cevap numarasını giriniz: ")
        self.guess(answer)

    def guess(self, answer):
        question = self.getQuestion()
        if question.checkAnswer(question.choices[int(answer) - 1]):
            self.score += 1
            print("Doğru cevap!")
        else:
            print("Yanlış cevap!")

        self.questionIndex += 1
        self.loadNextQuestion()

    def loadNextQuestion(self):
        if self.questionIndex < len(self.questions):
            self.displayQuestion()
        else:
            self.showScore()

    def showScore(self):
        print(f"Quiz bitti! Skorunuz: {self.score}/{len(self.questions)}")


# Soru listesi
questions = [
    Question("Who am I?", ["Furkan", "Kemal", "Kadir", "Fatih"], "Furkan"),
    Question("Which programming language is the most popular?", ["C#", "Python", "C", "Java"], "Python"),
    Question("Which language is the best?", ["English", "Turkish", "Latin", "Spanish"], "English")
]

# Quiz başlat
quiz = Quiz(questions)
quiz.displayQuestion()

