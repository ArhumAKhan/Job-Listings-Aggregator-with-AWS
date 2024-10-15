import boto3

def upload_to_s3(file_name, bucket, object_name=None):
    # If S3 object_name is not specified, use file_name
    if object_name is None:
        object_name = file_name

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
    except Exception as e:
        print(f"Error: {e}")
        return False
    return True

if __name__ == "__main__":
    file_name = 'deployment.zip'
    bucket = 'your-s3-bucket'
    upload_to_s3(file_name, bucket)
