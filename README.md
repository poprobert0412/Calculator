# 🧮 Calculator

Un calculator simplu realizat în Python care permite utilizatorului să efectueze operații matematice de bază: adunare, scădere, înmulțire și împărțire.

---

## 📋 Descriere

Acest proiect oferă un calculator ce funcționează în linie de comandă, afișând o reprezentare ASCII a tastaturii calculatorului înainte de a cere input-ul utilizatorului. Sunt suportate operațiile:

- Adunare (`+`)
- Scădere (`-`)
- Înmulțire (`*`)
- Împărțire (`/`)

---

## 🧰 Tehnologii utilizate

- Python 3.x
- Modulul standard Python

---

## 📁 Structura proiectului

```

Calculator/
├── MAIN.py          # Codul principal al calculatorului
├── art.py           # Reprezentarea ASCII a tastaturii calculatorului
├── README.md        # Documentația proiectului

````

---

## 🚀 Cum rulezi proiectul

### 1. Clonează repository-ul

```bash
git clone https://github.com/poprobert0412/Calculator.git
cd Calculator
````

### 2. Rulează calculatorul

```bash
python MAIN.py
```

---

## 📝 Cum funcționează

* Programul afișează o reprezentare ASCII a tastaturii calculatorului.
* Cere utilizatorului primul număr.
* Afișează operațiile disponibile (`+`, `-`, `*`, `/`).
* Cere utilizatorului să aleagă simbolul operației dorite.
* Cere utilizatorului al doilea număr.
* Calculează și afișează rezultatul.

---

## Exemplu de rulare

```
  _________
 | 7 | 8 | 9 |
 |___|___|___|
 | 4 | 5 | 6 |
 |___|___|___|
 | 1 | 2 | 3 |
 |___|___|___|
 | 0 | . | = |
 |___|___|___|

What is the first number?: 10
+
-
*
/
Pick an operation symbol from the line above: *
What is the second number?: 5
10 * 5 = 50
```

---

## 📌 Observații

* În prezent, input-urile sunt convertite la `int`, deci nu sunt suportate numere cu virgulă mobilă (float).
* Funcția de împărțire nu tratează explicit împărțirea la zero — poate genera o excepție în acest caz.
* Proiectul poate fi extins pentru a suporta mai multe operații sau interfață grafică.

---

## 👤 Autor

**Pop Robert**
GitHub: [@poprobert0412](https://github.com/poprobert0412)
