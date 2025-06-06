# 🖥️ Jumia Laptops Web Scraping & Analysis

A full data science workflow project—from web scraping and cleaning to analysis—using laptop data from Jumia Kenya.

## 📖 Project Overview

This project demonstrates a complete data analysis workflow, starting from web scraping to data cleaning and final exploratory data analysis (EDA).  
The goal is to collect data on laptops and computer accessories from the Jumia Kenya website, process the raw data into a clean, usable format, and then perform EDA to uncover insights about pricing, brands, and customer ratings.

The project follows best practices for data science, making it easy to understand, reproduce, and extend.

## 📁 Project Structure

```
jumia-laptop-scraper/
├── data/
│   ├── processed/
│   │   └── cleaned_jumia_laptops.csv
│   └── raw/
│       └── raw_jumia_laptops.csv
├── notebooks/
│   └── analysis.ipynb
├── src/
│   ├── cleaner.py
│   └── scraper.py
├── venv/
├── .gitignore
├── README.md
└── requirements.txt
```

## 🚀 How to Run This Project

### 1. Prerequisites

- Python 3.8+
- pip (Python package manager)

### 2. Installation

Clone the repository to your local machine:

```bash
git clone <your-repo-url>
cd jumia-laptop-scraper
```

### 3. Create a virtual environment (optional but recommended)

```bash
python3 -m venv venv
source venv/bin/activate    # On Windows, use `venv\Scripts\activate`
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Scraper

```bash
python src/scraper.py
```

### 6. Clean the Data

```bash
python src/cleaner.py
```

### 7. Exploratory Data Analysis

```bash
jupyter notebook notebooks/analysis.ipynb
```

---

## 💡 Highlights

- Automated web scraping using Python (requests + BeautifulSoup)  
- Fast, modular data cleaning scripts  
- Ready-to-use Jupyter notebook for analysis and visualization  
- Clean project structure for easy extension and reproducibility  

## 🤝 Contributing

Have suggestions or want to contribute?  
Pull requests and issues are welcome!

## 📫 Contact

Project by Clement Ogol  
For questions or collaboration, reach out at clementogol@gmail.com

## ⭐️ If you found this useful, please star the repo!
