# viratkohli_ipl_analysis
# Virat Kohli IPL Analytics (2008–2023)

## Project Overview

This project analyzes Virat Kohli's batting performance across IPL seasons using ball-by-ball IPL data. The objective is to perform data cleaning, exploratory data analysis (EDA), and generate meaningful insights about Kohli's consistency, scoring patterns, opponent-wise performance, phase-wise performance, and dismissal trends.

The project was built using Python, Pandas, NumPy, and Jupyter Notebook.

---

## Dataset

Source: IPL Ball-by-Ball Dataset (Kaggle)

Files Used:

* deliveries.csv

The dataset contains ball-by-ball information for IPL matches including batsman runs, extras, dismissals, batting team, bowling team, overs, and match identifiers.

---

## Project Objectives

* Clean and preprocess raw IPL ball-by-ball data.
* Calculate Virat Kohli's season-wise batting statistics.
* Analyze performance against different opponents.
* Analyze scoring patterns across innings phases.
* Study dismissal trends.
* Export cleaned analytical outputs for reporting and dashboard creation.

---

## Data Cleaning Performed

The following preprocessing steps were applied:

* Handled missing values in dismissal-related columns.
* Replaced missing values in extras columns with zero.
* Standardized data types.
* Created IPL season mapping from match identifiers.
* Removed records with unmapped seasons.
* Applied cricket-standard batting calculations.
* Excluded wides from balls faced calculations.

---

## Key Metrics Calculated

### Batting Runs

Total runs scored by Virat Kohli.

### Batting Average

Average = Runs Scored ÷ Number of Times Dismissed

### Strike Rate

Strike Rate = (Runs Scored ÷ Balls Faced) × 100

### Boundaries

* Number of Fours
* Number of Sixes

---

## Analysis Performed

### 1. Season-wise Performance

Metrics calculated for each IPL season:

* Matches
* Runs
* Average
* Strike Rate
* Fours
* Sixes

### 2. Opponent-wise Analysis

Performance against each IPL franchise:

* Runs
* Average
* Strike Rate
* Boundaries
* Innings Played

### 3. Phase-wise Analysis

Batting performance across:

* Powerplay (Overs 1–6)
* Middle Overs (Overs 7–15)
* Death Overs (Overs 16–20)

### 4. Dismissal Analysis

Frequency of dismissals by:

* Caught
* Bowled
* LBW
* Run Out
* Stumped
* Caught and Bowled

---

## Major Insights

### Best IPL Season

Virat Kohli's most dominant season was 2016.

* Runs: 973
* Average: 81.08
* Strike Rate: 152.03
* Fours: 84
* Sixes: 38

### Opponent Analysis

* Highest aggregate runs were scored against Chennai Super Kings.
* Strong records were also observed against Kolkata Knight Riders and Delhi franchises.

### Phase Analysis

* Most runs were scored during middle overs.
* Highest strike rate was achieved during death overs.
* Boundary-hitting increased significantly in the final overs.

### Dismissal Pattern

* "Caught" was the most common dismissal mode.
* Bowled and LBW dismissals occurred much less frequently.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Jupyter Notebook
* Excel
* CSV Reporting

---

## Project Structure

IPL-Virat-Kohli-Analytics/

├── data/

│ └── deliveries.csv

├── outputs/

│ ├── virat_kohli_ipl_season_summary.csv

│ ├── virat_kohli_by_opponent.csv

│ ├── virat_kohli_by_phase.csv

│ └── virat_kohli_dismissals.csv

├── notebooks/

│ └── virat_kohli_analysis.ipynb

├── src/

│ └── kohli_analysis.py

├── README.md

└── requirements.txt

--
