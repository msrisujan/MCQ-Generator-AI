import json
import os
import json
import traceback
import pandas as pd
from dotenv import load_dotenv
from src.mcqgen.utils import read_file,get_table_data
import streamlit as st
# from langchain.callbacks import get_openai_callback
from src.mcqgen.mcqgenerator import generate_evaluate_chain

#loading json file
with open('C:\Users\motamarri.s\Documents\MCQ-Generator AI\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

#print(RESPONSE_JSON)