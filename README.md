# 🌌 Exoplanet Habitability Potential Predictor

A machine-learning-based screening application that uses planetary and host-star characteristics from the **NASA Exoplanet Archive** to identify exoplanets that fall within a project-defined potential-habitability region.

> **Important:** This project is a habitability-potential screening tool. It does **not** determine whether life exists on an exoplanet or prove that a planet is actually habitable.

---

## 🎯 Project Objective

The goal of this project is to build an end-to-end Data Science and Machine Learning workflow around real astronomical data.

The project:

- Collects confirmed exoplanet data from NASA's Exoplanet Archive.
- Cleans and explores planetary and stellar measurements.
- Analyzes missing values, distributions, correlations, and extreme observations.
- Creates a project-defined **potential habitability screening label**.
- Trains and compares multiple classification models.
- Provides an interactive Streamlit application for prediction.

---

## 🛰️ Dataset

**Source:** NASA Exoplanet Archive  
**Table:** Planetary Systems Composite Parameters (PSCompPars)

NASA Exoplanet Archive:  
https://exoplanetarchive.ipac.caltech.edu/

The working dataset contains **6,360 exoplanet records** and **15 selected columns** from the PSCompPars data.

### Selected Data Fields

| Feature | Description |
|---|---|
| `planet_name` | Name of the exoplanet |
| `host_star` | Host star name |
| `planet_radius` | Planet radius in Earth radii |
| `planet_mass` | Planet mass in Earth masses |
| `orbital_period` | Orbital period in days |
| `semi_major_axis` | Approximate orbital distance in AU |
| `equilibrium_temperature` | Estimated equilibrium temperature in Kelvin |
| `insolation_flux` | Stellar energy received by the planet relative to Earth |
| `star_temperature` | Host-star temperature in Kelvin |
| `star_mass` | Host-star mass in Solar masses |
| `star_radius` | Host-star radius in Solar radii |
| `number_of_stars` | Number of stars in the system |
| `number_of_planets` | Number of planets in the system |
| `discovery_method` | Method used to discover the planet |
| `discovery_year` | Year of discovery |

---

## 🔎 Exploratory Data Analysis

The project includes:

- Dataset structure and data-type analysis
- Missing-value analysis
- Duplicate-row and duplicate-planet checks
- Descriptive statistics
- Distribution/histogram analysis
- Extreme-value investigation
- Discovery-method analysis
- Correlation matrix analysis

### Key Data Observations

- The dataset contains missing measurements, which is expected in real astronomical data.
- `planet_mass` has a relatively high proportion of missing values and was therefore excluded from the main model feature set.
- Several astronomical variables show strong right-skewness and very large ranges.
- `orbital_period` and `semi_major_axis` show a very strong relationship.
- The dataset contains legitimate extreme astronomical observations, so extreme values were investigated rather than blindly removed.

---

## 🧹 Data Preprocessing

The main model uses the following numerical features:

```text
planet_radius
orbital_period
semi_major_axis
equilibrium_temperature
insolation_flux
star_temperature
star_mass
star_radius
```

### Missing Values

For the model features, missing numerical values were filled using the **median of each feature**.

Median imputation was chosen because several variables have strongly skewed distributions and the median is less sensitive to extreme values than the mean.

`planet_mass` was excluded from the main model because approximately **61.5%** of its values were missing in the working dataset.

### Duplicate Checks

The dataset was checked for:

- Completely duplicated rows
- Duplicated planet names

Both checks returned **0 duplicates**.

---

## 🌍 Habitability-Potential Screening Criteria

The NASA dataset does not provide a definitive binary `habitable` label.

Therefore, this project creates a **project-defined screening label**.

An exoplanet is assigned:

```text
1 → Potentially Habitable
0 → Not Potentially Habitable
```

when all of the following conditions are satisfied:

| Measurement | Screening range |
|---|---|
| Planet radius | 0.5–2.0 Earth radii |
| Equilibrium temperature | 200–350 K |
| Insolation flux | 0.25–4.0 Earth units |

These thresholds are used as a **simplified screening framework for the project**.

They should not be interpreted as an official NASA habitability classification.

---

## 🤖 Machine Learning

Three classification models were trained and compared:

1. **Logistic Regression**
2. **Decision Tree**
3. **Random Forest**

For Logistic Regression, numerical features were standardized using `StandardScaler`.

The tree-based models were trained on the original feature scales.

### Evaluation Metrics

The models were evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC
- Confusion Matrix
- ROC Curves

### Important Modeling Limitation

The target label in this project is generated from rules based on some of the same planetary characteristics supplied to the models.

As a result, tree-based models can learn these screening rules very easily and may achieve near-perfect or perfect test performance.

Therefore, the reported classification scores **should not be interpreted as evidence that the model can scientifically predict real habitability**.

The ML component demonstrates how a classification system can learn and reproduce a predefined screening framework.

---

## 🌳 Final Model

**Random Forest Classifier** was selected as the final model for the application.

The model is stored in:

```text
exoplanet_habitability_model.pkl
```

The feature order is stored in:

```text
features.pkl
```

---

## 🖥️ Streamlit Application

The project includes an interactive Streamlit interface where users can enter:

- Planet radius
- Orbital period
- Semi-major axis
- Equilibrium temperature
- Insolation flux
- Star temperature
- Star mass
- Star radius

The application returns:

- Potential-habitability screening result
- Model probability
- Screening-criteria status
- Input summary

---

## 🗂️ Project Structure

```text
exoplanet-habitability-predictor/
│
├── app.py
├── SPACE.ipynb
├── exoplanet_raw.csv
├── exoplanet_habitability_model.pkl
├── features.pkl
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🛠️ Technologies Used

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
Joblib
Streamlit
```

---

## 🚀 Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/SohanBC/exoplanet-habitability-predictor.git
cd exoplanet-habitability-predictor
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📌 Project Workflow

```text
NASA Exoplanet Archive
        ↓
PSCompPars Dataset
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Missing-Value Analysis
        ↓
Outlier / Extreme-Value Investigation
        ↓
Correlation Analysis
        ↓
Feature Selection
        ↓
Habitability-Potential Screening Label
        ↓
Train/Test Split
        ↓
Classification Models
        ↓
Model Evaluation
        ↓
Random Forest
        ↓
Streamlit Application
```

---

## 🔮 Future Improvements

Possible future improvements include:

- Incorporating additional physical and atmospheric parameters.
- Using independently sourced habitability labels rather than labels generated from the model features.
- Exploring scientifically validated habitability indices.
- Adding SHAP-based explainability.
- Hyperparameter tuning and cross-validation.
- Investigating probabilistic and uncertainty-aware predictions.
- Expanding the application with NASA API-based live data retrieval.

---

## ⚠️ Scientific Disclaimer

This project is an educational and portfolio-oriented machine learning application.

A prediction from this application means only that an exoplanet matches the project's **defined screening framework**. It does not establish:

- the presence of liquid water,
- the presence of an atmosphere,
- the existence of life,
- biological activity,
- or confirmed habitability.

Actual planetary habitability depends on many additional physical, atmospheric, stellar, geological, and environmental factors that are not represented by this simplified model.

---

## 👤 Author

**Sohan BC**

GitHub:  
https://github.com/SohanBC
