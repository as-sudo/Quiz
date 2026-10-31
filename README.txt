Quizmaster jest to konsolowa aplikacja do sprawdzenia wiedzy , lub dodawaniu pytań testowych. Program oferuje opcje:

1. Rozpoczęcie quizu (Używając gotowych pytań/pytań dodanych przez użytkownika można sprawdzić swoją wiedzę z pythona i nie tylko). Użytkownik wpisuje A-B-C lub D, w zależności od poprawności odpowiedzi. 
W przypadku pozytynwego wyniku , program zwróci: "poprawna odpowiedź." W przypadku błędu Program poinformuje o błędzie i wskaże poprawną odpowiedź. Po wyczerpaniu puli pytań, program zlicza poprawne odpowiedzi , zwracając wynik ułamkowy.

2. Własne pytanie - została dodana możliwosć dodania do bazy pytań kolejne , własne pytania. Na początku użytkownik podaje treść pytania, później 4 przykładowe odpowiedzi ,a na końcu wskazuje która z nich jest poprawna. 
Pytanie jest automatycznie zapisywane do pamięciu programi i trwale zapisane do .jsona 

3. Exit - wyjście

Do uruchomienia programu będziemy potrzebowali 4 plików: main.py, quiz_data.json , quiz_exceptions.py , oraz quiz_manager.py

Program jednak przewiduje, że w przypadku problemu z otworzeniem pliku .json , i tak program zadziała. W przypadku wybrania opcji 1 (gotowego quizu) wyświetlony informacja o braku pliku json Wtedy na początku trzeba przejśc do opcji 2 , by samemu zrobić pytania 

