# Python Job Listing Scraper

Simple job scraper that extracts job titles, company names, locations, and job description link into a generated csv file.

## Setup
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the scraper:
   ```bash
   python3 main.py
   ```
2. The script will fetch job listings and save them to `jobs.csv`
3. Open `jobs.csv` to view the scraped job data (title, company, location, and application link)

## Structure
- **main.py** - Main scraper script that fetches and parses job listings from the website
- **requirements.txt** - Python package dependencies
- **jobs.csv** - Generated output file containing scraped job data (created after running main.py)
