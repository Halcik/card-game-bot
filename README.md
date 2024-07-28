# Card Game Bot
Jest to bot, którego docelową funkcją będzie rozegranie całej gry w karty. Przed ostateczną wersją ma skupić się na analizie posiadanych w grze kart i proponować, które użyć w trwającej rundzie, by z największym prawdopodobieństwem pokonać przeciwnika.
>Obecnie projekt jest na etapie tworzenia samego obiektu karty na podstawie testowych screenów.

### **Klasa Card**
 Tworzy obiekt karty, która posiada:
  - przekształcone zdjęcie do odczytu danych **[image_read]**
  - ilość gwiazdek do ulepszeń karty **[n_stars]**
  - wartości mocy w kolejności: fioletowa (dowództwo), zielona (zręczność), niebieska (inteligencja), czerwona (siła), suma **[powers]**
  - ilość energii **[energy]**
  - numer karty w grze **[n_card]**
  - pozycja karty **[position]**

  - level karty - ustalany przy pierwszym rozpoznaniu **[level]** ***chwilowo nie wiem, czy będzie jednak potrzebna***

  ##### 
  Oprócz tego posiada metody:
   - **change_image** - zmieniającą screena karty w postać do odczytu danych

   - **set_level** - ustalającą level karty - ***chwilowo nie wiem, czy będzie potrzebna, patrząc na to, że pozycję zaczęłam ustawiać względem sumy mocy.***

   - **get_stars** - ustala ilość gwiazdek do ulepszenia
   - **set_position** - ustalenie pozycji karty i zwrócenie jej numeru
   - **get_powers** - pobranie mocy z karty
   - **use** - oznacza użycie karty i aktualizuje jej energię (zmniejsza ją o 1)
   - **update_stars** - aktualizuje dostępną liczbę ulepszeń
   - **get** - metoda tworząca kartę - dostępna za pomocą odwołania się do nazwy klasy (Card.get()) ze sprawdzaniem, czy nowa karta nie przekroczy maksymalnej ilości kart

#####
...oraz statyczne pola:
 - **star** - przechowuje odczytaną gwiazdkę
 - **n_cards** - liczba kart istniejących w danej grze (niekoniecznie już aktywnych). Istotne przy ustalaniu kolejności kart - nowsza karta=wyższa pozycja
 - **positions** - lista z kartami (ich słabymi referencjami do obiektu), na której operujemy zmianą kolejności
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

### Określanie pozycji kart - notatka na przyszłość
 - Wyjaśnienie oznaczeń:
    - F - karta fioletowa (najwyższy level)
    - G - karta złota
    - N - karta niebieska
    - SZ - karta szara (najniższy level)
    - liczba za skrótem oznacza ilość gwiazdek (ulepszeń) w grze
 - Jest ona zależna od:
    - sumy mocy kart
    - kolejności dodania do gry (nowsza karta = wyższe miejsce, gdy suma jest taka sama)
 - Sumy mocy kart w zależności od poziomu i ilości gwiazdek:
    - F5 (27)
    - F4 (23)
    - G4 (21)
    - F3 (19)
    - G3 (17)
    - F2 i N3 (15)
    - G2 (13)
    - F1 i N2 (11)
    - G1 i SZ2 (9)
    - N1 (7)
    - SZ1 (5)