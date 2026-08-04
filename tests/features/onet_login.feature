@onet-bdd
Feature: Logowanie użytkownika do serwisu Onet
  Jako zarejestrowany użytkownik
  Chcę mieć możliwość logowania się do serwisu
  Aby uzyskać dostęp do zabezpieczonej części aplikacji

  Background:
    Given użytkownik otwiera stronę główną
    And użytkownik akceptuje pliki cookies

  @smoke
  Scenario: Udawanie logowania
    When użytkownik klika w przycisk logowania
    And użytkownik przełącza się na okno logowania
    And użytkownik podaje email
    Then pojawia się ekran wysłania hasła