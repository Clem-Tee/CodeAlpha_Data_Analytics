# Nairobi Air Quality - Exploratory Data Analysis 📊🇰🇪

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

An exploratory data analysis (EDA) of forecasted air quality data for Nairobi, Kenya. This project demonstrates how to fetch data from a live API, process it into a usable format, and derive meaningful insights through statistical analysis and visualization.

---

## 🚀 Project Overview

The primary goal of this project is to investigate the air quality forecast for Nairobi. By analyzing different pollutants, we aim to answer key questions about air quality trends, identify the most significant pollutants, and understand their behavior over time.

### Key Features:
- **Secure API Integration**: Fetches data from the World Air Quality Index (WAQI) API while securely managing credentials using a `.env` file.
- **Data Processing**: Transforms nested JSON data into structured and pivoted pandas DataFrames, ready for analysis.
- **Data Visualization**: Generates clear, informative visualizations, including time-series plots and correlation heatmaps, using Matplotlib and Seaborn.
- **Insightful Analysis**: Uncovers key findings about dominant pollutants, volatility, and daily trends to provide a clear summary of the air quality situation.


*(A sample plot from the analysis showing daily pollutant trends)*

---

## 🔧 Technology Stack
- **Python**: Core programming language.
- **Pandas**: For data manipulation and analysis.
- **Matplotlib & Seaborn**: For data visualization.
- **Requests**: For making HTTP requests to the API.
- **python-dotenv**: For managing environment variables.
- **Jupyter Notebook (in VS Code)**: For interactive analysis and presentation.

---

## ⚙️ Setup and Installation

To run this project on your local machine, please follow these steps:

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/your-username/nairobi-air-quality.git
    cd nairobi-air-quality
    ```

2.  **Create and Activate a Virtual Environment**
    ```bash
    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

    # For Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Install Dependencies**
    This project's dependencies are listed in `requirements.txt`.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set Up Environment Variables**
    You will need an API token from the [WAQI Platform](https://aqicn.org/data-platform/token/).
    
    - Create a file named `.env` in the root of the project.
    - Add your API token to it like this:
      ```
      WAQI_TOKEN="your_api_token_here"
      ```
    The `.gitignore` file is already configured to prevent this file from being committed to the repository.

5.  **Run the Notebook**
    Open the `exploratory-data-analysis.ipynb` notebook in VS Code or Jupyter and run the cells.

---

## 📈 Key Findings from the EDA

Our analysis of the forecast data revealed several key insights:

*   **Dominant Pollutants**: **PM2.5** and **PM10** are the most significant pollutants, with PM2.5 consistently showing the highest average daily values.
*   **High Correlation**: A very strong positive correlation exists between PM2.5 and PM10, strongly suggesting they originate from common sources like vehicle exhaust, industrial emissions, or dust.
*   **Volatility**: PM2.5 is also the most volatile pollutant, meaning its levels fluctuate more significantly day-to-day compared to others.
*   **Overall Trend**: The forecast showed a general downward trend for particulate matter after an initial peak, suggesting that air quality was projected to improve over the period.

---

## 🔮 Future Work & Next Steps

This EDA serves as a strong foundation. Potential next steps include:
-   **Source Investigation**: Correlate pollution spikes with traffic data or weather events to identify primary emission sources.
-   **Weekday vs. Weekend Analysis**: Quantify the impact of daily commuter traffic by comparing pollution levels on weekdays versus weekends.
-   **Health Impact Assessment**: Compare the forecasted peak levels to World Health Organization (WHO) guidelines to assess public health risk.
-   **Predictive Modeling**: Build a machine learning model to predict high-pollution days with greater accuracy, potentially incorporating weather forecast data.

---
