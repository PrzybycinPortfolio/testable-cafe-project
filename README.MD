\# Cafe Order System – Portfolio Projekt (Junior Software Manual Tester)



\## 📌 O projekcie

Aplikacja konsolowa napisana w języku Python, symulująca system sprzedaży w kawiarni. Projekt został przygotowany jako \*\*materiał dowodowy do procesów rekrutacyjnych\*\*, mający na celu zaprezentowanie praktycznych umiejętności z zakresu manualnego zapewnienia jakości (QA).



> \[!NOTE]

> Projekt ma charakter edukacyjny i demonstracyjny. Skupia się na wybranych modułach logiki biznesowej, aby ukazać sposób identyfikacji defektów oraz podejście do walidacji danych.



\## 🛠️ Zakres kompetencji (Tester Perspective)

W ramach projektu zrealizowano następujące zadania testerskie:

\* \*\*Projektowanie Test Case’ów:\*\* Przygotowanie scenariuszy testowych w oparciu o analizę wymagań biznesowych (np. weryfikacja wieku przy sprzedaży alkoholu).

\* \*\*Analiza wartości brzegowych (BVA):\*\* Testowanie skrajnych przypadków dat urodzenia oraz identyfikatorów produktów.

\* \*\*Testowanie negatywne (Negative Testing):\*\* Weryfikacja odporności aplikacji na błędne dane wejściowe (znaki nieliczbowe, nieistniejące ID).

\* \*\*Raportowanie błędów:\*\* Dokumentowanie defektów logicznych (Bug Reporting) wraz z priorytetyzacją i krokami do reprodukcji.







\## 📋 Dokumentacja Testowa

W repozytorium znajdują się opracowane przypadki testowe (TC\_01 - TC\_05), które obejmują:

\* \*\*Happy Path:\*\* Pomyślne przejście procesu zamówienia dla klienta pełnoletniego i niepełnoletniego.

\* \*\*Error Handling:\*\* Sprawdzenie komunikatów systemowych przy wpisaniu nieprawidłowych danych.

\* \*\*Logic Defects:\*\* Identyfikacja błędów w walidacji dat (np. akceptacja daty urodzenia z przyszłości).



\## 🚀 Scenariusze poddane analizie

1\. \*\*Weryfikacja 18+:\*\* System blokuje dodanie alkoholu (np. Vodka, Piwo) do koszyka, jeśli wiek klienta jest niższy niż 18 lat.

2\. \*\*Agregacja produktów:\*\* Sprawdzenie, czy wielokrotne dodanie tego samego produktu poprawnie sumuje ilość i cenę na paragonie.

3\. \*\*Integralność danych:\*\* Próba obejścia systemu poprzez wpisywanie liter w polach numerycznych oraz dat niemożliwych chronologicznie.



\## 📄 Instrukcja uruchomienia

1\. Upewnij się, że posiadasz zainstalowane środowisko Python (v3.x).

2\. Pobierz pliki projektu do jednego folderu.

3\. Uruchom aplikację komendą: `python main.py`.

4\. Postępuj zgodnie z instrukcjami wyświetlanymi w konsoli, aby przeprowadzić własne testy.

