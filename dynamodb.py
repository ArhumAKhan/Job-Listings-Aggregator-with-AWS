# dynamodb/dynamodb_handler.py
import boto3
import uuid

# Initialize a DynamoDB resource
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('JobListings')


def store_data(jobs):
    for job in jobs:
        job_id = str(uuid.uuid4())  # Generate unique JobID

        # Insert job listing into DynamoDB
        table.put_item(
            Item={
                'JobID': job_id,
                'Title': job['title'],
                'Company': job['company'],
                'Location': job['location']
            }
        )


if __name__ == "__main__":
    # Example usage with mock data (can be integrated with the scraper)
    mock_jobs = [
        {'title': 'Software Engineer', 'company': 'Company A', 'location': 'Austin, TX'},
        {'title': 'Software Engineer', 'company': 'Company B', 'location': 'New York, NY'}
    ]
    store_data(mock_jobs)
