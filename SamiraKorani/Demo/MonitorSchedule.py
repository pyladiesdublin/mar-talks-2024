import sagemaker
from sagemaker.model_monitor import CronExpressionGenerator, ModelMonitor
from sagemaker import get_execution_role
sagemaker_session = sagemaker.Session()
role = get_execution_role()
endpoint_name = "Llama2"
monitoring_schedule_name = "MonitorSchedule"
baseline_job_name = "training_Trip"

# Initialize your monitor object, this could be a DefaultModelMonitor or a specific monitor depending on your needs
my_monitor = ModelMonitor.attach(monitor_schedule_name=monitoring_schedule_name, sagemaker_session=sagemaker_session)

# Define the schedule
schedule_cron_expression = CronExpressionGenerator.daily()

# Create the monitoring schedule
my_monitor.create_monitoring_schedule(
    monitor_schedule_name=monitoring_schedule_name,
    endpoint_input=endpoint_name,
    output_s3_uri='s3://your-bucket/your-output-path/',  # Specify your S3 output path
    statistics=my_monitor.baseline_statistics(),
    constraints=my_monitor.suggested_constraints(),
    schedule_cron_expression=schedule_cron_expression,
    role_arn=role
)
