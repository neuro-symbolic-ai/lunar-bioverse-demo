# lunar-bioverse-demo

*TODO: Add project description*


## Running workflows
First, you need to provide a valid OpenAI API key and endpoint in the *lunarverse_config.env* file. Then run the command:

```bash
sh run_workflow.sh <path to workflow descriptor file>
```

to run a single workflow, or 

```bash
sh run_workflow.sh all
```

to run all workflows.

You can get workflow information, including the paths, with the following command:
```bash
python util/workflow_index.py
```

