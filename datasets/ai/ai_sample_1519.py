#Import the necessary libraries
from azureml.core import Workspace
from azureml.pipeline.core import Pipeline
from azureml.core.dataset import Dataset
from azureml.pipeline.steps import PythonScriptStep

#Create workspace
ws = Workspace.from_config()

#Build the Pipeline
pre_process_step = PythonScriptStep(
    script_name='pre-process.py',
    arguments=['--data', input_ds.as_named_input('input_ds').as_mount()],
    outputs=['processed_ds'],
    compute_target=compute_target
)

pipeline = Pipeline(
    workspace=ws,
    steps=[pre_process_step],
    description='A pipeline to pre-process the input dataset'
)

pipeline.validate()

#Submit the pipeline to the Azure Machine Learning workspace
pipeline_run = Experiment(ws, 'Pre-Process_Dataset').submit(pipeline)

#Wait for the pipeline to finish
pipeline_run.wait_for_completion(show_output=True)