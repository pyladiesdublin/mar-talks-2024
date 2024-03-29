# HuggingFace is the class provided by the SageMaker SDK

import huggingface_estimator

predictor = huggingface_estimator.deploy(initial_instance_count=1, instance_type="ml.m5.large")
