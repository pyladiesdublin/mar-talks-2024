
import boto3
import pandas as pd
from io import StringIO

# Create an S3 client
s3 = boto3.client('s3')

# Specify the S3 bucket and object key
bucket_name = ''  # The actual bucket name
object_key = ''  # The full path to the file within the bucket

try:
    # Retrieve the object
    file_obj = s3.get_object(Bucket=bucket_name, Key=object_key)
    
    # Read the file's content into a string
    file_content = file_obj['Body'].read().decode('utf-8')
    
    # Use pandas to read the CSV file content from a string
    df = pd.read_csv(StringIO(file_content))
    
    # Print the DataFrame
    print("Content of the CSV file:")
    print(df)
except Exception as e:
    print(f"Error occurred: {e}")
