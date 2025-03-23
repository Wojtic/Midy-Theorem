# Midy’s theorem in non-integer numeral systems and properties of k-Fibonacci sequences

This is the Github repository for my Essay in the Czech Students' Professional Activities competition 2024/25. It contains all code developed in the process of arriving at the conclusions described in my Essay.

# Midyho věta v neceločíselných soustavách a vlastnosti k-Fibonacciho posloupností

Toto je Github repozitář pro moji práci v rámci Středoškolské Odborné Činnosti v roce 2024/25. Obsahuje všechen kód vytvořený během tvorby této práce.

## Užití

### midy_denominators.txt

Všechna čísla s Midyho vlastností od 1 do 100 000 pro m mezi 1 a 100 včetně.

### density.txt

Hustota čísel s Midyho vlastností menších než 100 000 pro m 1 až 100.

### python

#### real.py

Definuje třídu real(a, b, m, c, k), umožňující pracovat s racionálními čísly v kvadratických soustavách. Jsou definované funkce na převod do písma, sčítání, odčítání, násobení, mocnění a porovnávání, společně s výpočtem přibližné hodnoty.

#### sequences.py

Obsahuje pomocné funkce pro práci s m-Fibonacciho posloupnostmi a výpočet Pisanových period.

#### tests.py

Obsahuje funkce umožňující zjišťovat Midyho vlastnost jednotlivých jmenovatelů.

**checkMidyProperty(beta: real, n, maximum=0)**
Zkontroluje, zda má n v soustavě beta Midyho vlastnost, s využitím algoritmu písemného sčítání polovin period.

**checkMidyPropertyReal(beta: real, n, maximum=0)**
Zkontroluje, zda má n v soustavě beta Midyho vlastnost, pomocí převádění polovin period na objekt real() a následného sčítání. Trpí chybou při desetinné aritmetice pro větší n.

**checkMidyPropertyMatrix(beta: real, n, maximum=0)**
Zkontroluje, zda má n v soustavě beta Midyho vlastnost, pomocí mocnin matice společnice.

Zbylé funkce slouží k získávání velkého množství čísel s Midyho vlastností a vytváření grafů.

#### utils.py

Obsahuje všechny pomocné funkce.

**expansionToReal(beta, expansion)**
Převede rozvoj s nulovou desetinnou částí na objekt real().

**addExpansions(m, expansion1, expansion2)**
Provede písemný součet dvou rozvojů s nulovou desetinnou částí v soustavě beta_m.

**greedy(beta, x)**
Implementuje hladový algoritmus pro jakékoliv x.

**greedyT(beta, x)**
Zjistí desetinný rozvoj čísel v intervalu [0, 1) s využitím transformace T.

**T(beta, n, x)**
n-krát složená transformace T. [0, 1] -> [0, 1)

#### plots

Slouží k vytváření grafů.

### C

#### main.c

Pomocí matice společnice zjistí jakékoliv množství čísel s Midyho vlastností a uloží je do souboru.
