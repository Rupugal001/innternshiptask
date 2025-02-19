import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

region = 'us-east-2'  # Set your desired region here
bucket_name = 'pugal12345678'
file_name = 'C:\\Users\\DB Tech\\Desktop\\AWS.jpg'
s3_file_name = 'CTO.png'

# Initialize the S3 client
s3 = boto3.client('s3', region_name=region)

try:
    # Create a bucket
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={'LocationConstraint': region}
    )
    print(f"Bucket '{bucket_name}' created successfully.")
    
    # Upload a file to the bucket
    s3.upload_file(file_name, bucket_name, s3_file_name)
    print('Upload Successful')
except FileNotFoundError:
    print('The file was not found.')
except NoCredentialsError:
    print('Credentials not available.')
except PartialCredentialsError:
    print('Incomplete credentials provided.')
except ClientError as e:
    print(f"Error occurred: {e}")
