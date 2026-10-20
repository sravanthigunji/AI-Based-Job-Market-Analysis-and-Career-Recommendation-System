# AI-Powered Job Market Analytics & Career Recommendation System

An intelligent, data-driven web application that helps users explore job market trends, compare salaries, identify skill gaps, and discover suitable career opportunities based on their existing skills.

## Overview

Choosing the right career requires an understanding of industry demands, salary trends, and the skills employers expect. This project brings these insights together in an interactive dashboard built using Python and Streamlit.

The application uses machine learning techniques to compare user-provided skills with job requirements and recommend relevant career roles.

## Key Features

- **Job Market Dashboard** — View job listings, job roles, average salaries, and market insights.
- **Job Search** — Search and filter job listings by job title.
- **Salary Analysis** — Compare average, minimum, and maximum salaries across job roles.
- **Skills Analytics** — Explore in-demand skills and identify frequently requested technologies.
- **AI Career Recommendation** — Receive job role recommendations based on skill similarity.
- **Skill Gap Analysis** — Identify skills required for a selected career that you have not listed yet.
- **Learning Resources** — Access YouTube tutorial searches for skills you want to learn.
- **CSV Export** — Download job market data for further analysis.
- **Interactive UI** — Explore insights through a Streamlit dashboard with custom styling.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core application logic |
| Streamlit | Interactive web application |
| Pandas | Data processing and analysis |
| Scikit-learn | Machine learning and similarity calculations |
| TF-IDF | Text feature extraction |
| Cosine Similarity | Matching user skills with job requirements |
| HTML & CSS | Dashboard styling |
| CSV | Job market and skills datasets |

## How It Works

1. Job market data is loaded from CSV files.
2. The dashboard analyzes job roles, salary information, locations, and skills.
3. The recommendation system transforms skills into numerical text features using TF-IDF.
4. Cosine similarity measures how closely user skills match job requirements.
5. The application displays relevant career recommendations and missing skills.
6. Learning links help users explore resources for developing additional skills.

## Project Structure

```text
job-market-ai/
├── app.py
├── analysis.py
├── train_model.py
├── requirements.txt
├── data/
│   ├── jobs.csv
│   └── skills_analysis.csv
├── models/
│   └── career_model.pkl
├── assets/
│   └── style.css
└── .gitignore
```

## Installation & Setup

### Prerequisites

- Python 3.10 or a compatible Python version
- Git
- pip

### 1. Clone the Repository

```bash
git clone https://github.com/sravanthigunji/AI-Based-Job-Market-Analysis-and-Career-Recommendation-System.git
```

### 2. Open the Project Folder

```bash
cd AI-Based-Job-Market-Analysis-and-Career-Recommendation-System
```

### 3. Create and Activate a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Application

```bash
python -m streamlit run app.py
```

The terminal will display a local URL. Open that URL in your browser to use the application.

> **Note:** The trained model file must be present in `models/career_model.pkl`. If it is not available, train the model using `python train_model.py` after installing the required dependencies.

## Project Goals

- Make job market information easier to explore.
- Help users understand salary differences across career roles.
- Identify skill requirements for selected job opportunities.
- Provide data-driven career recommendations.
- Encourage continuous learning and skill development.

## Future Enhancements

- Integration with live job market data.
- More advanced personalized career recommendations.
- Additional salary and employment trend visualizations.
- Expanded datasets covering more job roles and locations.
- Improved learning recommendations and career pathways.

## Limitations

This project uses a sample job dataset. Salary figures and recommendations are illustrative and should not be treated as live market data or guaranteed career outcomes.

## Author

**Sravanthi Gunji**

GitHub: [@sravanthigunji](https://github.com/sravanthigunji)

---

If you find this project useful, consider giving the repository a ⭐ on GitHub.
