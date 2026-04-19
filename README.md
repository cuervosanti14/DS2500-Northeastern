# DS2500: Intermediate Programming with Data  
**Northeastern University — Spring 2026**  
**Professor:** Deahan Yu  
**Student:** Santiago Cuervo | cuervopaez.s@northeastern.edu  

---

## Course Overview

DS2500 is an intermediate Python programming course focused on data science workflows, including data collection, exploratory data analysis, machine learning, and model evaluation. The course covers Python programming fundamentals, statistics, data manipulation, and core ML algorithms including KNN, linear regression, and logistic regression.

---

## Repository Structure

```
ds2500/
├── README.md
├── week02/          # Python fundamentals I — variables, strings, lists, tuples
│   └── lab01/
├── week03/          # Python fundamentals II — dictionaries, conditionals, loops
│   └── lab02/
├── week04/          # Functions, main(), advanced Python concepts
│   ├── lab03/
│   └── hw01/
├── week05/          # OOP and classes
│   └── lab04/
├── week06/          # Google Colab, matplotlib, pandas, web scraping
├── week07/          # APIs and JSON, Statistics I
│   ├── lab06/
│   └── hw02/
├── week08/          # Statistics II — distributions and visualization plots
│   └── lab07/
├── week9/          # Data manipulation, feature extraction, scaling
│   ├── lab08/
│   └── hw03/
├── week10/          # Distance & similarity, clustering, KNN
│   └── lab09/
├── week11/          # Linear regression, logistic regression
│   └── lab10/
```

---

## Weekly Topics

| Week | Topics |
|------|--------|
| 2 | Python fundamentals I — variable assignment, commenting, strings, lists, tuples |
| 3 | Python fundamentals II — dictionaries, conditionals, loops |
| 4 | Python fundamentals III — functions, `main()`, CSV; advanced concepts — variable scope, lambda functions, list comprehension, error handling |
| 5 | OOP — classes, attributes, methods, `__init__`, `__str__`, encapsulation; project ideation |
| 6 | Google Colab, matplotlib, pandas; web scraping — HTML, `requests`, `BeautifulSoup`, `robots.txt` |
| 7 | APIs & JSON — GET/POST, query parameters, `.json()`; Statistics I — data types, central tendency (mean, median, mode) |
| 8 | Statistics II — data distributions, visualization plots (line, bar, histogram, box plot, scatter), IQR, outliers, standard error |
| 9 | data manipulation — centering, z-score, min-max scaling, log transformation, missing values, feature extraction |
| 10 | Distance & similarity measures (Euclidean, Manhattan, cosine, Hamming, Jaccard); clustering — K-Means, hierarchical, silhouette score; KNN classification |
| 11 | Linear regression — MSE, R², correlation vs. causation, K-fold cross-validation; logistic regression — sigmoid, log-odds, feature importance |

---

## Homeworks

### HW01 — Pixar Films & Ratings *(Week 4)*  
**Topics:** Python fundamentals — dictionaries, lists, strings, loops, conditionals, lambda functions, file I/O  
**Dataset:** `pixar_films.csv` — 27 Pixar films with release dates, runtimes, MPA ratings, and critic scores  
**Key tasks:** Data loading and cleaning, Rotten Tomatoes score statistics (min/max/avg), popular release   month, runtime categorization, original vs. sequel comparison, composite scoring using lambda  

---

### HW02 — English Women's Soccer Goals *(Week 7)*
**Topics:** OOP, data visualization, descriptive statistics  
**Dataset:** `wsl_goals_2324.csv` — per-game goals for 12 WSL teams over the 2023–24 season  
**Key tasks:** Build a `Team` class, compute mean/median/mode/variance/standard deviation from scratch, find   most consistent team (coefficient of variation), longest scoring streak, most improved team, animated   cumulative goals scatter plot  

---

### HW03 — KNN Classifier from Scratch *(Week 10)*  
**Topics:** KNN algorithm, Euclidean distance, data preprocessing, model evaluation (F1 score)  
**Dataset:** Shape measurement dataset — 16 geometric features, binary classification target  
**Key tasks:** Implement full `KNN` class from scratch (distance computation, neighbor selection, majority   vote), EDA and preprocessing, K optimization, generate test predictions scored on F1  

---

## Labs

| Lab | Week | Focus |
|-----|------|-------|
| Lab 01 | 2 | Variable assignment, string methods, list manipulation |
| Lab 02 | 3 | For/while loops, dictionaries, word frequency counting |
| Lab 03 | 4 | Functions with docstrings, list comprehension, lambda + sorted/map/filter |
| Lab 04 | 5 | OOP — `Movie` class with attributes, methods, and genre analysis functions |
| Lab 06 | 7 | Statistics I — mean, median, mode, population variance, standard deviation from scratch |
| Lab 06 | 7 | Statistics II — descriptive stats applied to student score datasets, plot selection discussion |
| Lab 07 | 8 | Z-score standardization, min-max scaling, handling missing values with pandas |
| Lab 08 | 9 | K-Means and hierarchical clustering on Iris dataset using sklearn; silhouette score optimization |
| Lab 09 | 10 | Linear regression pipeline — data splitting, feature selection, train and evaluate with MSE |
| Lab 10 | 11 | Logistic regression pipeline — binarize target, train and evaluate with accuracy and F1 |

---

## Team Project

The group project for this course was completed in a separate repository. It investigates how well publicly available pre-match statistics predict English Premier League match outcomes (Win, Draw, Loss) across four analytical angles — SPI gap, home advantage, possession, and draw predictability.

🔗 [EPL Match Outcome Prediction Repo](https://github.com/cuervosanti14/EPL-match-prediction)

---

*Santiago Cuervo | Data Science & Business Administration | Northeastern University*
