# **Structure of repo**
This repo is divided by the two overarching processes in relation to the development of the QA-systems.
The process are as follows:

# Link to dataset
- https://drive.google.com/drive/folders/1XHYbwpc1A2Pu3cIyeM4aytApMhMze703?usp=drive_link
The datasets follow the same folder structure with RAG and Dataset generation. Add the dataset folder for Dataset generation and RAG respectively
<img width="419" alt="Screenshot 2024-05-13 at 13 03 56" src="https://github.com/Olafcito/bo_project_code/assets/122600472/33777653-3e4e-49db-9ebb-508ee0e565b8">

# Overarching outline of folders
### **Dataset generation**
The process of developing and evaluating the QA-pairs based on the webscraped data from Beoworld. The files is split between abstractive summarization and two-step approach
### **Retreival Augmented Generation**
This folder encompasses the development and usage of the RAG systems. It develops the vector database, saved as the storage folder. 
It allows for inference based on the RAG system with either the fine-tuned or baseline model. Additionally, it includes a chatbot based on one of the RAG models that can be run from the terminal.


# Dataset generation files descriptions
## Two_step_approach.ipynb && Two_step_approach.ipynb
### Overview
This Jupyter Notebook is designed for generating and evaluating question-answer pairs using the two-step and abstractive summarization approach by generating the questions. It utilizes  Llama2 7b, Llama2 70b, and GPT-3.5 for the dataset generation and evaluation, whilst evaluating based on GPT-3.5. 

### Usage
1. Ensure that the folder contains /datasets folder with the provided datasets from the Google Drive (See Link to dataset)
2. Set up the OpenAI and REPLICATE API key in the environment variables or directly in the script in the first code section.
3. Usage is not recommended due to a long and pricy process of generating the files  

### File outputs
**Outputs for Two_step_approach.ipynb**: 2s_gpt.csv, 2s_llama2_70b.csv, and 2s_llama2_7b.csv
**Outputs for abstractive_summarization.ipynb**: 'as_gpt.csv', 'as_llama2_70b.csv', and 'as_llama2_7b.csv'
