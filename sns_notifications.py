# sns_notifications.py
import boto3

sns = boto3.client('sns')
topic_arn = 'arn:aws:sns:us-east-1:123456789012:NewJobListings'

def notify_users():
    message = "New job listings have been added to the database!"
    sns.publish(TopicArn=topic_arn, Message=message)

if __name__ == "__main__":
    # Test notification
    notify_users()
