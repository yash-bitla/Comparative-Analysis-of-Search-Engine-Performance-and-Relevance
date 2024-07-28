# Comparative Analysis of Search Engine Performance and Relevance

## Project Overview

This project involves developing Python-based web scrapers to compare the performance of multiple search engines—Ask, Yahoo, Bing, and DuckDuckGo—against Google. By analyzing the search results across 100K queries, I aim to understand the overlap in results and the differences in ranking algorithms.

## Features

- **Web Scrapers**: Developed using Python to extract top search results.
- **Comparative Study**: Analyzed search results for 100K queries.
- **Statistical Evaluation**: Calculated percent overlap and Spearman correlation coefficients to measure relevance and ranking differences.

## Key Findings

- **Percent Overlap**: The Ask search engine showed a 21.2% overlap with Google for 100 queries.
- **Spearman Coefficient**: The average Spearman's rank correlation coefficient was -13.4694, indicating uncorrelated ranking results.
- **Algorithmic Differences**: The significant differences in overlap and correlation suggest that Ask and Google use different algorithms for weighting and ranking documents, emphasizing different features.
- **Performance Evaluation**: The Ask search engine did not perform well compared to Google, with a low overlap percentage and negative correlation, highlighting its differing approach to relevance and ranking.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yash-bitla/Comparative-Analysis-of-Search-Engine-Performance-and-Relevance.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd Comparative-Analysis-of-Search-Engine-Performance-and-Relevance
   ```
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Run the web scrapers**:
   ```bash
   python scraper.py
   ```
2. **Generate JSON results and Analyze results**:
   ```bash
   python generate_results.py
   ```

## Project Structure

```bash
Comparative-Analysis-of-Search-Engine-Performance-and-Relevance/
│
├── data/
│ ├── queries.txt
│ ├── google_results.json
│ └── search_engine_results.json
│
├── src/
│ ├── scraper.py
│ ├── generate_results.py
│ └── analyze_results.py
│
├── README.md
└── requirements.txt
```
