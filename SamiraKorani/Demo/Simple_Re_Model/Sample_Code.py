# data 
import pandas as pd 
import numpy as np
from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sagemaker.pytorch import PyTorch
# sagemaker
import boto3
import sagemaker
from sagemaker import get_execution_role
import sagemaker
from sagemaker.session import Session
from sagemaker.inputs import TrainingInput

# SageMaker session and role
sagemaker_session = sagemaker.Session()
role = sagemaker.get_execution_role()


bucket = 'sagemaker-studio-950548200505-ips11ncs7gq'
prefix = 'Tripadvisor'



for obj in boto3.resource('s3').Bucket(bucket).objects.all():
     print(obj.key)



s3_input_path = f's3://{bucket}/{prefix}'

# Specify S3 input configurations
data_channels = {
    'train': TrainingInput(s3_data=s3_input_path, content_type='application/Simple_RE_Training.py'),
    # Add other data channels if necessary, such as 'validation' or 'test'
}

estimator.fit(data_channels)


output_path = None
    torch.save(mlp_classifier.state_dict(), 'relation_extraction_model.pt')

estimator = None