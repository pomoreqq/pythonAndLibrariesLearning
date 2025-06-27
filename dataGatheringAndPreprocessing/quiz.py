# 📋 Quiz: Data Cleaning and Data Preprocessing (20 pytań)

# 1. Co oznacza termin "data cleaning" w kontekście analizy danych?
    # oznacza oczyszczanie danych, czyli usuwanie np nan,ow
# 2. Dlaczego proces czyszczenia danych jest kluczowy przed analizą?
    # bo przygotowuje dane do nastepnego etapu czyli np wizualizacji lub bardziej do tematow ml
# 3. Co to są wartości brakujące (missing values)?
    # nan
# 4. Jakie są trzy sposoby radzenia sobie z brakującymi danymi?
    # wyplenianie ich np srednia,mediana a trzeciego sposobu nie wiem
# 5. Co oznacza termin "outlier" (wartość odstająca)?
    # czyli zbyt duza lub zbyt mala wartosc w danym datasecie ktora zaburza inne zaleznosci
# 6. Jakie metody można wykorzystać do wykrywania outlierów?
    # IQR (interquartile range),,z-score,boxplots

#
# 7. Kiedy należy usunąć wiersz, a kiedy tylko uzupełnić brakujące dane?
    #usunac wiersz gdy np sa same nany albo nieproawidlowe wartosci, oznacza to ze dany wiersz jest jakims bledem, uzueplnic dane gdy w danym wierszu sa pojedyncze przypadki
# 8. Czym różni się metoda `.dropna()` od `.fillna()` w Pandas?
    # dropna wiersze gdzie sa nany, a fillna wyplenia nany jakas docelowa wartoscia
# 9. Jakie problemy mogą powodować błędne typy danych w kolumnach?
    #bledy np w obliczaniu zaleznosci miedzy kolumnami, bledy w interpretacji danych, wizualizacji danych
# 10. Co to znaczy "konwersja typów danych"? Podaj przykład.
    # np konwertowanie intow na floaty, lub string na int
# 11. W jaki sposób można wykryć i poprawić literówki w danych tekstowych?
    # sprawdz np w pandas za pomoca metody unique() unikalne wartosci a poprawic hmm nie wiem jakim sposobem//fuzzywuzzy,difflib.get_close_matches(),


# 12. Czym jest duplikat w zbiorze danych?
    #jest to taka sama wartosc wystepujaca, czyli ten sam wiersz lub kolumna
# 13. Jak usunąć duplikaty w Pandas?
    # za pomoca metody drop_duplicates()
# 14. Kiedy warto standaryzować (normalizować) dane?
    # kiedy sa zbyt duze roznice miedzy dynami
# 15. Jaka jest różnica między skalowaniem (scaling) a normalizacją (normalization)?
    # Scaling (standaryzacja): przesuwa dane do rozkładu o średniej 0 i odch. std. 1 (np. Z-score). Normalization: przekształca dane do zakresu [0,1] (np. min-max scaling).


# 16. Co to jest imputacja i kiedy się ją stosuje?
    #jest to proces zamieniana brakujacych danych lub problematycznych ich estymowanymi wartosciami
# 17. W jaki sposób można wykryć niezgodność danych (inconsistencies)?
    # metodami np pandas.isna np.isnan
# 18. Jakie są potencjalne skutki błędnego oczyszczenia danych?
    # zle zaprojektowane modele do ml, zle wizualizacje
# 19. Czym różni się preprocessing danych od cleaning?
    # preprocessing oznacza etap przygotowywania danych poprzez standaryzowanie,normalizowane a cleaning to usuwanie nanow
# 20. Dlaczego dokumentacja procesu czyszczenia danych jest istotna?
    # zeby przyszly uzytkownik,wspolracownik wiedzial co sie wykonalo na tym datasecie, moze niektore akcje byly niepotrzebne