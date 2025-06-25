# 📘 QUIZ – WORKING WITH TEXT FILES (Sekcja + Rozszerzenia tematyczne)

# 1. Co zwraca metoda `.readlines()`? Podaj przykład wyniku.
# 2. Dlaczego `with open(...)` jest bezpieczniejsze od `open()` bez `with`?
# 3. Jaka jest różnica między trybem `'r'`, `'w'`, `'a'` i `'x'` w `open()`?
# 4. Wyjaśnij, jak działa poniższy kod:
#    with open("plik.txt") as f:
#        lines = f.readlines()
#        print(lines[0])
#
# 5. Co się stanie, jeśli nie zamkniesz pliku otwartego bez `with`?
# 6. Jak poradzić sobie z wczytaniem pliku, w którym część linii ma złą strukturę?
# 7. Co oznacza `split(':')` w kontekście linii tekstowej? Podaj przykład użycia.
# 8. W jaki sposób można użyć `set()` do usunięcia duplikatów z listy logów?
# 9. Z czego wynikają błędy konwersji typu (np. `ValueError: invalid literal for int()`) podczas czytania pliku?
# 10. Jak zbudować słownik `user -> lista akcji` na podstawie danych tekstowych?

# 11. Czym różni się zapis `f.write("Hello\n")` od `f.writelines()`?
# 12. Co się stanie, jeśli otworzysz plik w trybie `'w'` i zapiszesz do niego 2 razy?
# 13. Dlaczego warto używać `.strip()` przed `split()`?
# 14. Jak przekształcić dane `Anna,Nowak,29` do formatu `Nowak Anna - 29 lat`?
# 15. Jak sprawdzić, czy linia składa się dokładnie z 3 pól?

# 16. Czym się różni `.read()` od `.readlines()` przy dużym pliku?
# 17. Kiedy warto używać `try/except` przy parsowaniu pliku?
# 18. Jak zapisać dane tylko tych użytkowników, którzy wykonali więcej niż jedną unikalną akcję?
# 19. Co oznacza format: `name:action:date` i jak można go walidować?
# 20. Jak przetwarzać duże pliki linia po linii bez wczytywania całości do pamięci?

# 21. Jakie są dobre praktyki przy zapisie plików tekstowych zawierających dane wielopolowe (np. CSV)?
# 22. Czym się różni plik `.txt` od `.csv`, jeśli oba są rozdzielane przecinkami?
# 23. Co się stanie, jeśli zapiszesz dane z `dict` do pliku bez konwersji na tekst?
# 24. Jak działa metoda `.join()` w zapisie listy do pliku jako jednej linii?
# 25. Co robi `','.join(lista)` i w jakim celu używa się tego przy zapisie?

# 26. Jaka jest różnica między `pandas.read_csv()` a `open()+split()`?
# 27. Co robi parametr `index_col` w `pd.read_csv()` i kiedy warto go używać?
# 28. W jakim celu stosuje się `squeeze=True` podczas wczytywania plików w pandas?
# 29. Jakie problemy mogą wystąpić przy użyciu `np.loadtxt()` do plików zawierających tekst?
# 30. Jakie rozszerzenie pliku sugeruje użycie `json.load()` zamiast `readlines()`?

# 💬 Wskazówka: Odpowiedzi pisz kodowo lub opisowo – zależnie od pytania.
