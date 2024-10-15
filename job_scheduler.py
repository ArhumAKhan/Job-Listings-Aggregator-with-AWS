# jobs_scheduler.py
import schedule
import time
from aws_lambda import lambda_function

def run_scraper():
    lambda_function(None, None)

# Schedule the scraper to run every day at 9am
schedule.every().day.at("09:00").do(run_scraper)

if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Wait one minute before checking again
