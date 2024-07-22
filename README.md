# lunar-bioverse-demo
# Research Paper Code Repository

Welcome to the GitHub repository for the code and data accompanying our research paper. This repository is designed to provide an easy-to-access and comprehensive resource for researchers, developers, and practitioners who wish to understand, reproduce, or build upon the work presented in our paper.

## Paper Title

**An LLM-based Knowledge Synthesis and Scientific Reasoning Framework for Biomedical Discovery**

## Abstract

We present BioLunar, developed using the Lunar framework, as a tool for supporting biological analyses, with a particular emphasis on molecular-level evidence enrichment for biomarker discovery in oncology. The platform integrates Large Language Models (LLMs) to facilitate complex scientific reasoning across distributed evidence spaces, enhancing the capability for harmonizing and reasoning over heterogeneous data sources. Demonstrating its utility in cancer research, BioLunar leverages modular design, reusable data access and data analysis components, and a low-code user interface, enabling researchers of all programming levels to construct LLM-enabled scientific workflows. By facilitating automatic scientific discovery and inference from heterogeneous evidence, BioLunar exemplifies the potential of the integration between LLMs, specialised databases and biomedical tools to support expert-level knowledge synthesis and discovery.

## Citation

If you use this code or data in your research, please cite our paper as follows:
Wysocki, Oskar, et al. "An LLM-based Knowledge Synthesis and Scientific Reasoning Framework for Biomedical Discovery." arXiv preprint arXiv:2406.18626 (2024).

@article{wysocki2024llm,
  title={An LLM-based Knowledge Synthesis and Scientific Reasoning Framework for Biomedical Discovery},
  author={Wysocki, Oskar and Wysocka, Magdalena and Carvalho, Danilo and Bogatu, Alex Teodor and Gusicuma, Danilo Miranda and Delmas, Maxime and Unsworth, Harriet and Freitas, Andre},
  journal={arXiv preprint arXiv:2406.18626},
  year={2024}
}


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

