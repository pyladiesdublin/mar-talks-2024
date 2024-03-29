# Importing necessary libraries
import sagemaker
from sagemaker.huggingface import HuggingFace
from sagemaker import get_execution_role

# Initializing SageMaker session
sagemaker_session = sagemaker.Session()

role = get_execution_role()

# Define the HuggingFace estimator for fine-tuning
huggingface_estimator = HuggingFace(
    entry_point='train.py',            # Your script name
    source_dir='. ',            # Directory where your script and requirements.txt are
    instance_type='ml.p3.2xlarge',     
    instance_count=1,                  # Number of instances
    role=role,                        
    transformers_version='4.6.1',      # Transformers version used
    pytorch_version='1.7.1',           # PyTorch version used
    py_version='py36',                 # Python version
    # Update the hyperparameters to use a LLaMA model
    hyperparameters={
        'epochs': 3, 
        'train_batch_size': 32, 
        'model_name': 'Salesforce/llama-7b'  # Specify the LLaMA model you wish to use. Adjust as needed.
    }
)

# Starting the training job
huggingface_estimator.fit({'train': 's3://your-bucket/training-data/', 'test': 's3://your-bucket/test-data/'})
