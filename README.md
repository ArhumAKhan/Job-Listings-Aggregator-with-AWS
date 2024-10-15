# AWS Job Scraper using Puppeteer, Lambda, S3, and DynamoDB

## Overview
This project scrapes job listings for "Software Engineer" positions from Indeed 
using **Puppeteer** (Node.js) and processes the data using **AWS Lambda**. 
The scraped job data is first uploaded to an **S3 bucket**. 
A Python-based Lambda function is triggered to retrieve the data from S3, 
store it in **DynamoDB**, and send notifications using **SNS**.

### Key Technologies:
- **Puppeteer (Node.js):** Used for scraping job listings.
- **AWS S3:** Temporary storage for the scraped data.
- **AWS Lambda (Python):** Processes the scraped data and stores it in DynamoDB.
- **DynamoDB:** Used to store job listings.
- **SNS:** Sends notifications when new job listings are added.

### File Roles
- **scraper.js:**                  Scraper using Puppeteer (Node.js)
- **package.json:**                Dependencies for the Node.js scraper
- **aws_lambda.py:**               Lambda function (Python) to process data
- **requirements.txt:**            Dependencies for the Python Lambda function
- **dynamodb.py:**                 Python module to handle DynamoDB insertion
- **sns_notifications.py:**        Python module to send SNS notifications
- **upload_to_s3.py:**             Optional script to upload files to S3
- **scraper.py:**                  Python alternative for local testing ONLY
- **deployment.zip:**              Deployment package for Lambda (NOT PROVIDED IN GIT)
