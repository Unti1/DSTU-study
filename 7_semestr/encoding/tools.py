from dotenv import load_dotenv,set_key
import os
"""
    Подгрузка переменной среды
"""
def dotenv_init():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
dotenv_init()