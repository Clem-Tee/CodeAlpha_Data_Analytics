# Air Quality Data Visualization

This project demonstrates how to use various data visualization techniques to analyze and interpret air quality data for Nairobi. By leveraging libraries like Matplotlib, Seaborn, and Plotly, we transform a simple time-series dataset into compelling and insightful visuals.

The primary goal is to tell a story with the data, moving from high-level trends to specific relationships, and ultimately deriving actionable insights.

## 📊 Key Visualizations

The `notebooks/visualization.ipynb` notebook walks through the creation of several plot types, each designed to answer a specific question:

-   **Time Series Plot**: To observe how PM2.5 and PM10 pollutant levels change over time.
-   **Histogram & KDE Plot**: To understand the distribution and frequency of PM2.5 readings.
-   **Scatter Plot & Heatmap**: To explore the relationships between different metrics like pollutants, temperature, and humidity.
-   **Box Plot**: To compare pollution levels across different days of the week, identifying weekly patterns.
-   **Interactive Line Chart**: An interactive version of the time series plot using Plotly, allowing for dynamic exploration of the data points.


*A sample of visualizations created in this project.*

## 🛠️ Technology Stack

-   **Python**: The core programming language for the analysis.
-   **pandas**: For data manipulation and wrangling.
-   **Matplotlib**: For creating foundational static plots.
-   **Seaborn**: For creating beautiful and informative statistical graphics.
-   **Plotly Express**: For generating interactive, web-ready visualizations.
-   **Jupyter Notebook**: As the interactive development environment.

## 📂 Project Structure
visualization-air-quality/
├── myenv/ # Virtual environment directory (ignored by git)
├── notebooks/
│ └── visualization.ipynb # The main Jupyter Notebook with all analysis and plots
├── .gitignore
├── README.md
└── requirements.txt


## 🚀 How to Use

To run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd VISUALIZATION-AIR-QUALITY
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    # For Unix/macOS
    python3 -m venv myenv
    source myenv/bin/activate

    # For Windows
    python -m venv myenv
    .\myenv\Scripts\activate
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Launch Jupyter Notebook:**
    ```bash
    jupyter notebook
    ```
    Navigate to the `notebooks/` directory and open `visualization.ipynb`.

## 📈 Summary of Insights

The visualizations revealed several key patterns in the sample dataset:

-   **Weekly Cycle**: Particulate matter levels show a cyclical pattern, with peaks often occurring midweek and lower levels during the weekend, suggesting a strong influence from traffic or industrial work schedules.
-   **Strong Correlation**: PM2.5 and PM10 levels are highly correlated, indicating they likely originate from the same emission sources.
-   **Weather Influence**: A clear relationship exists between weather and air quality: hotter, drier days tend to have higher concentrations of PM2.5.
-   **Interactive Exploration**: The use of interactive charts significantly enhances the ability to explore specific data points, making detailed analysis more intuitive and accessible.

---

*This project serves as a practical guide to data visualization and storytelling for any time-series dataset.*
