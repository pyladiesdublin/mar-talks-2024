# training data is in an S3 bucket
import huggingface_estimator

training_data_uri = ""

huggingface_estimator.fit({'train': training_data_uri})
