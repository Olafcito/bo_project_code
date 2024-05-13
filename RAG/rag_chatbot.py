import getpass
import os
from llama_index.core import Document
import faiss

from llama_index.core import (
    SimpleDirectoryReader,
    load_index_from_storage,
    VectorStoreIndex,
    StorageContext,
)
from llama_index.vector_stores.faiss import FaissVectorStore
from IPython.display import Markdown, display
from llama_index.llms.openai import OpenAI
import pandas as pd
from llama_index.core.chat_engine import CondenseQuestionChatEngine
import openai
API_KEY = 'sk..'
openai.api_key = API_KEY

# load index from disk
vector_store = FaissVectorStore.from_persist_dir("./storage")
storage_context = StorageContext.from_defaults(
    vector_store=vector_store, persist_dir="./storage/"
)
index = load_index_from_storage(storage_context=storage_context)

# query engine vanilla gpt35
llm_gpt35 = OpenAI(model='gpt-3.5-turbo-0125', api_key=API_KEY, temperature=1)
chat_engine_baseline = index.as_chat_engine(llm=llm_gpt35)

llm_ft = OpenAI(model="ft:gpt-3.5-turbo-0125:personal:master:9Bfq5w4r", api_key=API_KEY, temperature=1)
chat_engine_ft = index.as_chat_engine(llm=llm_ft)

chat_engine = chat_engine_ft
while True:
    text_input = input("\nReply:\n")

    if text_input == "c":
        break
    streaming_response = chat_engine.stream_chat(text_input)
    for token in streaming_response.response_gen:
        print(token, end="")