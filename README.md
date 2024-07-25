# Card Game Bot
Jest to bot, którego docelową funkcją będzie rozegranie całej gry w karty. Przed ostateczną wersją ma skupić się na analizie posiadanych w grze kart i proponować, które użyć w trwającej rundzie, by z największym prawdopodobieństwem pokonać przeciwnika.
>Obecnie projekt jest na etapie tworzenia samego obiektu karty na podstawie testowych screenów.

### **Klasa Card**
 Tworzy obiekt karty, która posiada:
  - przekształcone zdjęcie do odczytu danych **[image_read]**
  - ilość gwiazdek do ulepszeń karty **[n_stars]**
  - wartości mocy w kolejności: fioletowa (dowództwo), zielona (zręczność), niebieska (inteligencja), czerwona (siła) **[powers]**
  - ilość energii **[energy]**
  - pozycja karty **[position]**
  - level karty - ustalany przy pierwszym rozpoznaniu **[level]**
  ##### 
  Oprócz tego posiada metody:
   - **change_image** - zmieniającą screena karty w postać do odczytu danych
   - **set_level** - ustalającą level karty
   - **get_stars** - ustala ilość gwiazdek do ulepszenia
   - **set_position** - ustalenie pozycji karty i zwrócenie jej numeru
   - **get_powers** - pobranie mocy z karty
   - **get** - metoda tworząca kartę - dostępna za pomocą odwołania się do nazwy klasy (Card.get()) ze sprawdzaniem, czy nowa karta nie przekroczy maksymalnej ilości kart
### Zasady gry:
Wspinaczka - karty
 - składa się z czterech etapów
 - na start dostajemy 3 losowe karty
 - możemy mieć max 6 kart
 - każda karta ma swoje moce oraz energię
 - jedna karta może mieć max 4 punkty energii
 - moce:
	- fioletowa - dowództwo
	- zielona - zręczność
	- niebieska - inteligencja
	- czerwona - siła
- boss ma wszystkich mocy po 18 pkt.
- dostępne premie po poziomach:
	- boska karta
	- zwiększenie poziomu
	- odzyskanie energii
	- dopalacze (teoretycznie najmniej opłacalne)
 - etap pierwszy
	- rozpoznanie kart i zliczenie ich początkowej mocy, by ułatwić dalsze dobieranie
	- idziemy prawą ścieżką zawsze
	- priorytety na ten etap:
		- wymaksowanie niebieskich
		- zdobycie dużej ilości koni
		- utrzymanie energii
	