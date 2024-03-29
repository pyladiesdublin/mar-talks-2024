from sagemaker.debugger import Rule, rule_configs, DebuggerHookConfig
from sagemaker.debugger import rule_configs, Rule, DebuggerHookConfig
from sagemaker.debugger import DebuggerHookConfig, CollectionConfig
import huggingface_estimator
import HuggingFace
import sagemaker
from sagemaker.model_monitor import CronExpressionGenerator, ModelMonitor
from sagemaker import get_execution_role
sagemaker_session = sagemaker.Session()
role = get_execution_role()
# Adding debugging rules and configurations to your estimator
huggingface_llama = "/meta-llama-Llama-2-7b-hfd"

# Define the estimator
huggingface_estimator = HuggingFace(
    entry_point='/home/ec2-user/environment/Py-Lady_Talk/Simple_Re_Model/Simple_RE_Training.py',                 # 
    source_dir='Simple_Re_Model',                    
    instance_type='ml.p3.2xlarge',         
    instance_count=1,                      
    role=role,                              
    transformers_version='4.6.1',           
    pytorch_version='1.7.1',                
    py_version='py36',                      
    image_uri= huggingface_llama,        
    sagemaker_session=sagemaker_session
)

# Set hyperparameters (adjust these based on your model and training script)
huggingface_estimator.set_hyperparameters(
    epochs=1,
    train_batch_size=32,
    model_name='models/meta-llama/Llama-2-7b-hf'          # Example model, choose according to your use case
)

huggingface_estimator.set_debugger_hook_config(
    debugger_hook_config=DebuggerHookConfig(
        s3_output_path='s3://sagemaker-studio-950548200505-ips11ncs7gq/debug-output/debug-output/',
        hook_parameters={
            "save_interval": "100"  # Saving tensors every 100 steps
        }
    )
)

huggingface_estimator.set_rules(
    rules=[Rule.sagemaker(rule_configs.vanishing_gradient())]
)


# Add Debugger hook configuration and rules
huggingface_estimator.debugger_hook_config = DebuggerHookConfig(
    hook_parameters={
        "train.save_interval": "100",      # Save tensors every 100 steps
        "eval.save_interval": "10"
    },
    collection_configs=[
        CollectionConfig(name="weights"),  # Collect weights
        CollectionConfig(name="gradients"),  # Collect gradients
        CollectionConfig(name="losses"),     # Collect losses
        CollectionConfig(name="biases")      # Collect biases
    ]
)

huggingface_estimator.rules = [
    Rule.sagemaker(rule_configs.vanishing_gradient()),
    Rule.sagemaker(rule_configs.loss_not_decreasing()),
    # Add more rules as needed
]



debugger_hook_config = DebuggerHookConfig(
    hook_parameters={"save_interval": "100"}
)

rules = [Rule.sagemaker(rule_configs.vanishing_gradient())]

# Example of adding Debugger to a HuggingFace estimator
huggingface_estimator.set_debugger_hook_config(debugger_hook_config)
huggingface_estimator.set_rules(rules)
