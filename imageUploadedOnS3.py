import boto3

# Create a session using the specific profile
session = boto3.Session(profile_name='Vimal-Kumar')

# Create an S3 client using the session
s3 = session.client('s3')

# Specify the file to upload and the target bucket
file_name = 'C:\\Users\\DB Tech\\Desktop\AWS.jpg'  # Full path to the image
bucket_name = 'pugal12345671'

# Upload the file
s3.upload_file(file_name, bucket_name, 'image.jpg')  # The last argument is the S3 key (name in the bucket)

print(f"File {file_name} uploaded successfully to {bucket_name}.")


#'C:\\Users\\DB Tech\\Desktop\AWS.jpg'