import json
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')


def lambda_function(event, context):
    # Parse the S3 event to get the bucket and key (file name)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Get the object from S3
    response = s3.get_object(Bucket=bucket, Key=key)
    data = response['Body'].read().decode('utf-8')
    job_listings = json.loads(data)

    # Process the job listings (e.g., store in DynamoDB)
    store_data(job_listings)

    # Optionally, send SNS notification
    notify_users()

    return {
        'statusCode': 200,
        'body': json.dumps('Job listings processed successfully!')
    }


def store_data(jobs):
    # This function stores data in DynamoDB (existing code)
    pass


def notify_users():
    # This function sends notifications via SNS (existing code)
    pass




## aws_lambda.py (LOCAL TESTING)
#from scraper import scrape_indeed_jobs
#from dynamodb import store_data


#def lambda_function(event, context):
#    # Step 1: Scrape jobs
#    jobs = scrape_indeed_jobs()

#    # Step 2: Store the scraped jobs in DynamoDB
#    store_data(jobs)

#    return {
#        'statusCode': 200,
#        'body': 'Job listings have been scraped and stored in DynamoDB'
#    }


#if __name__ == "__main__":
#    # Test the Lambda handler locally
#    lambda_function(None, None)
