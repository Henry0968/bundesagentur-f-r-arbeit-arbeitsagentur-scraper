thonimport requests
import json
import csv
import os
from .extractors.arbeitsagentur_parser import parse_job_listing
from .outputs.exporters import export_to_json, export_to_csv

def fetch_job_listings(query, max_results=100):
    base_url = "https://www.arbeitsagentur.de/jobsuche"
    params = {'query': query, 'maxResults': max_results}
    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch data: {response.status_code}")

    return response.json()

def scrape_jobs(query, max_results=100, output_format='json'):
    job_listings = fetch_job_listings(query, max_results)
    parsed_jobs = [parse_job_listing(job) for job in job_listings]

    if output_format == 'json':
        export_to_json(parsed_jobs, 'output/jobs.json')
    elif output_format == 'csv':
        export_to_csv(parsed_jobs, 'output/jobs.csv')
    else:
        raise ValueError("Unsupported output format")

if __name__ == "__main__":
    query = "software engineer"
    scrape_jobs(query, max_results=50, output_format='json')