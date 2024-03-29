from sagemaker.model_monitor import DataCaptureConfig, DefaultModelMonitor
import MonitorSchedule
from sagemaker import Predictor
from sagemaker import get_execution_role
import sagemaker
import huggingface_estimator



role = get_execution_role()
sagemaker_session = sagemaker.Session()


sagemaker_session.update_endpoint(
    endpoint_name=huggingface_estimator.endpoint,
    data_capture_config=DataCaptureConfig(
        enable_capture=True,
        sampling_percentage=100,
        destination_s3_uri="s3://sagemaker-studio-950548200505-ips11ncs7gq/Output/"
    )
)

# Setting up Model Monitor
model_monitor = DefaultModelMonitor(
    role=role,
    instance_count=1,
    instance_type='ml.m5.large',
    volume_size_in_gb=20,
    max_runtime_in_seconds=3600,
)

model_monitor.suggest_baseline(
    baseline_dataset="s3://sagemaker-studio-950548200505-ips11ncs7gq/Monitoring/baseline.csv",
    dataset_format={"csv": {"header": False}},
    output_s3_uri="s3://sagemaker-studio-950548200505-ips11ncs7gq/Monitoring/baseline-result/",
    wait=True
)

model_monitor.create_monitoring_schedule(
    monitor_schedule_name="MonitorSchedule", 
    endpoint_input=predictor.endpoint )