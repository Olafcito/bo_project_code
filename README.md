# **Structure of repo**
This repo is divided by the two overarching processes in relation to the development of the QA-systems.
The process are as follows:

# Link to dataset
- https://drive.google.com/drive/folders/1XHYbwpc1A2Pu3cIyeM4aytApMhMze703?usp=drive_link
The datasets follow the same folder structure with RAG and Dataset generation. Add the respective dataset folders to Dataset generation and RAG respectively
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



## get_gpt_finetuned
### Overview
This Jupyter Notebook is contains a function to run queries on the fine tuned model. 

### Usage
1. Set up the OpenAI key in the environment variables or directly in the script in the first code section.
2. Call the get_gpt function with the prompt as input and the gpt_api_key variable

### Output
- The fine-tuned LLMs output from the input prompt


## scraper_beoworld.ipynb
### Overview
Webcrawler for the Beoworld using to subtract and clean relevant information from the forum posts using requests and beautifulsoup

### Usage
1. Modify the forum_links dictionary in the notebook to include the base URLs of the Beoworld forum sections you wish to scrape
2. Run the script to run the crawler and extract post data.
**OBS** It is important to note that Beoworld has undergone subsequent structural changes, thereby requieres that the code is adapted to adjust for the changes in the HTML-code.

### Output
The retrieve_all_posts function will return a dictionary for each URL processed. This dictionary contains:
  - header_name: The title of the forum post.
  - url: The URL of the forum post.
  - tags: A list of tags associated with the post.
  - posts: A list of dictionaries, each representing a post within the forum thread, including details such as the post number, author, role, and text

# RAG
## rag.ipynb
### Overview
This notebook details the setup of a Retrieval-Augmented Generation (RAG) system. It includes components for building and managing vector stores and creating query engines with baseline and fine-tuned models to handle answer input prompts. 

### Quick Start
Skip the vector store building by loading the existing vector stores and directly test queries using the outlined steps in the 'Testing' and 'Evaluation' sections.

### Usage
1. Set up the OpenAI key in the environment variables or directly in the script in the first code section.
2. Skip  'building vector store with documents'-part in order to load the existing vector stores and directly test queries using the  steps in the 'Testing' and 'Evaluation' sections.
3. Use the rag_query function with query engine and query as input. query_engine_ft is the fine-tuned RAG model, whilst query_engine_gpt35 
4. Usage is not recommended, but evaluations can be run using the included Excel dataset and generate detailed reports. 


## rag_chatbot.py

### Overview
This script sets up a chat engine using a RAG, integrating vector store management and handle query processing. The chatbot encorporates memory in order to remember the conversation.

### Features
- **Vector Store Loading**: Automatically loads a pre-configured vector store from disk.
- **Query Engine Configuration**: Includes setup for both a baseline and a fine-tuned GPT-3.5 model for handling queries.
- **Interactive Chat Session**: Users can input queries and receive responses interactively, leveraging the system's advanced NLP capabilities.

### Usage
1. Make sure the vector store data is present in the `./storage` directory.
2. Set up the OpenAI API key in the environment variables or directly in the script.
3. Define the chat_engine to either chat_engine_ft or chat_engine_baseline
- Enter 'c' to exit the chat session.

## /storage

### Overview
The FAISS vector database as developed in rag.ipynb



