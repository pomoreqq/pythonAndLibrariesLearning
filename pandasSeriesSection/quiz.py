#	Pytanie	Twoja odpowiedź
# 1	Czym różni się Series.unique() od Series.nunique()?	—
    #unique zwraca jakie sa unikalne wartosci, a nunique ich ilosc
# 2	Jak dropna=True w nunique() wpływa na wynik?
#   #tak ze jest ze liczba unikalnych wartosci jest mniejsza o nan, czyli nie traktuje nanu jako unikalna wartosc	—
# 3	Dlaczego unique() zwraca numpy.ndarray, a nie Series?	—
    # bo zwraca poprostu array unikalnych wartosci
# 4	Podaj dwa scenariusze, w których nunique() jest wydajniejsze niż len(df.column.unique()).
#   nunique jest szybsze dla duzych zbiorow
    #nunique nie tworzy tablicy posredniej
# 5	Jak działa return_counts=True w numpy.unique() i jaki jest jego pandas-owy odpowiednik?	—
     #Zwraca (wartości, liczności). Odpowiednik: value_counts(),
# 6	Jak jedną linią przekonwertować Series do listy, a następnie do tablicy NumPy?	—
    # npArr = np.array(series.tolist())
# 7	Gdy wywołasz to_numpy() na Series, a potem zmienisz element tablicy – czy oryginalna Series się zmieni? Uzasadnij.	—
    # no zalezy czy nadpiszemy zmienna w ktorej jest chyba zapisany series tak? bo jesli nadmienimy w ten sposob to oryginalna series sie zmieni ale jesli uzyjemy tonumpy na 
    # series i zapiszemy to w zmiennej, zmienimy jedna rzecz i zapiszemy znowu do series no to oryginalna sie nie zmieni
# 8	Dlaczego sort_values() nie modyfikuje indeksu, mimo że zmienia kolejność wierszy?	
#   #bo to by wprowadzilo straszny nieporzadek, no jakby mogl pierwszy element miec index np 100, to byloby bezsensu—
# 9	W jakiej sytuacji sort_values() nie zadziała, ale sort_index() rozwiąże problem?
#   Kiedy chcemy sortować po indeksie, np. po set_index() lub concat().
# 10	Co zwróci sort_values(ascending=[True, False]) dla ramki sortowanej po dwóch kolumnach?	
#       #dla jednej zwroci sortowane rosnaca, a dla drugiej malejoco—
# 11	Wyjaśnij różnicę między parametrem key a kind w sort_values().
#   #key jest to jakas prosta funkcja lambda np, a w kind jest to caly lozony algorytm	—
# 12	Czemu przy dużym MultiIndex-ie sort_index() bywa szybsze niż reset + sort + ponowne ustawienie indeksu?	—
    # bo jest to tylko jeden step jakby do wykonania
# 13	Jak posortować MultiIndex malejąco po pierwszym poziomie i rosnąco po drugim, używając sort_index()?	
#       # uzyc ascending=[False,True]
# 14	Zbuduj one-liner, który: filtruje sales > 1000, sortuje malejąco po region i rosnąco po sales, zwraca Top 10 jako NumPy.
#       df[df['sales'] > 1000].sort_values(by=['region', 'sales'], ascending=[False, True]).head(10).to_numpy()
# 15	Jak pandas interpretuje typy danych przy sortowaniu kolumn ze stringami i liczbami jednocześnie?
#       # pandas rzuci blad ze nie mozna sortowac mieszanych typow danych
# 16	Dlaczego długie łańcuchy metod są trudne do debugowania i jak temu zapobiec (min. 2 praktyki)?	—   
        # bo czasami sa trubne do zrozumienia,co ostatecznie zwroci ten lancuch
        #1. praktyka: rozbijac te lancuchy na mniejsze
        #2.printowac wyniki danego lancuchu
# 17	Kiedy w łańcuchu metod pandas wykonuje operacje leniwie (“lazy”), a kiedy materializuje wynik?	—
        # pandas nie jest lazy, operacje sa materializowane odrazu
# 18	Jakie pułapki niesie „back-reference” (df = df.sort_values(...)) w dłuższych pipeline’ach?	—
    #nmoze nadpisac wazny etap
# 19	Podaj przykład, gdy df.col jest wygodniejsze od df['col'], i przykład, gdy to ryzykowne.
#       #jest wygodne gdy kolumna ma prosta nazwe, ryzykowne gdy koliduje z metodami innymi—
# 20	Czy Series.unique() zachowuje kolejność oryginalnych wartości? Jak uzyskać kolejność rosnącą?	—
        # tak zachowuje. mozna uzyskac wartosc poprzez uzyczie apply z lambda/mozna posortowac z np.sort?
# 21	Co robi ignore_index=True w sort_values() (pandas ≥ 2.0)?
#       #powoduje ze indexy wierszy sa reseteowane do numerycznych	—
# 22	Jakim parametrem sort_values() włączysz „locale-aware” sortowanie stringów (np. „Ł” vs „L”)?	—
    # paramterem key?
# 23	Czym różni się Series.array od Series.to_numpy() pod względem typu i zarządzania pamięcią?	—
        #✅ 1. Typ zwracany:
# Właściwość	Series.to_numpy()	Series.array
# Zwraca	np.ndarray	ExtensionArray
# Typ danych	klasyczna tablica NumPy	specjalny wewnętrzny typ Pandas, np. IntegerArray, StringArray

# ✅ 2. Zarządzanie pamięcią:
# Cecha	to_numpy()	array
# Czy tworzy kopię danych?	Zazwyczaj tak (czyli dane są kopiowane)	Nie zawsze – może wskazywać bezpośrednio na oryginalne dane
# Czy wspiera pd.NA?	Nie – zamienia na np.nan / NaT / None	Tak – zachowuje pełne wsparcie dla braków (pd.NA)
# Czy wymusza jeden typ (dtype)?	Tak – NumPy wymaga homogenicznych danych	Nie – ExtensionArray może zawierać typy nullable, kategorie, itp.
# 24	Wyjaśnij, dlaczego df.assign(...).query(...).sort_values(...) może zależeć od kolejności tych metod.
#   # kolejnosc ma znaczenie bo assign tworzy kolumny ktore moga byc uzyte w query, inaczej blad
# 25	Napisz kod, który na ramce orders podaje top 3 najczęściej zamawiane produkty, malejąco po liczbie zamówień, bez duplikatów nazw.
    # result = orders['product'].str.lower().str.strip().value_counts().head(3)