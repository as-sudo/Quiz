from quiz_manager import QuizMaster

 
def main():
    app = QuizMaster()
    
    while True:
        app.display_menu()
        choice = input("Wybierz opcję (1-3): ").strip()
        

        if choice == "1":
            app.run_quiz()
        elif choice == "2":
            app.add_question()
        elif choice == "3":
            print("Koniec programu")
            break
        else:
            print("Niepoprawny wybór (wpisz 1, 2 lub 3).")

if __name__ == "__main__":
    main()