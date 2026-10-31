import json
import re
from quiz_exceptions import InvalidAnswerError
 
def decorative_header(func):
    def wrapper(*args, **kwargs):
        print("\n" + "=" * 40)
        result = func(*args, **kwargs)
        print("=" * 40)
        return result
    return wrapper

class Question:
    def __init__(self, text, options, correct_answer):
        self.text = text
        self.options = options
        self.correct_answer = correct_answer 

class QuizMaster:
    def __init__(self):
        self.questions = []  
        self.load_initial_data()

    def load_initial_data(self):
        try:
            with open("quiz_data.json", "r", encoding="utf-8") as file:
                data = json.load(file)
            self.questions = [Question(q["text"], q["options"], q["correct_answer"]) for q in data]
        except FileNotFoundError:
            print("\n[INFO] Brak pliku json. Stwórz pytanie, albo pobierz plik!")
            self.questions = []
 
    def question_generator(self):
        for question in self.questions:
            yield question

    @decorative_header   
    def display_menu(self):
        print("         QUIZ MASTER          ")
        print("1. Rozpocznij Quiz")
        print("2. Dodaj własne pytanie")
        print("3. Exit")

    def run_quiz(self):
        if not self.questions:
            print("Brak pytań w bazie!")
            return

        score = 0
        for num, question in enumerate(self.question_generator(), 1):
            print(f"\nPytanie {num}: {question.text}")
            for option in question.options:
                print(option)

            while True:
                try:
                    user_answer = input("Twoja odpowiedź (A, B, C lub D): ").strip().upper()
                
                    if not re.match(r"^[A-D]$", user_answer):
                        raise InvalidAnswerError("Musisz wybrać literę A, B, C lub D!")
                    break
                except InvalidAnswerError as error:
                    print(f"[BŁĄD] {error}") 

            if user_answer == question.correct_answer.upper():
                print("Poprawna odpowiedź.")
                score += 1
            else:
                print(f"Źle! Poprawna odpowiedź to: {question.correct_answer}")

        print(f"\nKoniec quizu! Twój wynik to: {score}/{len(self.questions)}")

    def add_question(self):
        print("\nDODAWANIE NOWEGO PYTANIA")
        text = input("Podaj treść pytania: ")
        
        letters = ['A', 'B', 'C', 'D']
        
        format_option = lambda letter, option_text: f"{letter}) {option_text}"
        
        options = [format_option(letters[i], input(f"Podaj opcję {letters[i]}: ")) for i in range(4)]

        while True:
            correct_answer = input("Która odpowiedź jest poprawna (A, B, C, D)? ").strip().upper()
            if re.match(r"^[A-D]$", correct_answer):
                break
            print("Wpisz poprawną literę!")

        self.questions.append(Question(text, options, correct_answer))

        serialized_data = [{"text": q.text, "options": q.options, "correct_answer": q.correct_answer} for q in self.questions]
        with open("quiz_data.json", "w", encoding="utf-8") as file:
            json.dump(serialized_data, file, indent=4, ensure_ascii=False)
        
        print("Pytanie zapisane do bazy danych!")