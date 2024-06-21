import shutil
import os
from transformers import AutoModelForQuestionAnswering, GPTNeoForCausalLM, AutoTokenizer, GPT2Tokenizer
from tqdm import tqdm

# Ruta base para los modelos
base_model_path = os.path.join('.', 'app', 'model')

# Eliminar la carpeta ./app/model si existe
if os.path.exists(base_model_path):
    shutil.rmtree(base_model_path)

# Crear la carpeta base de nuevo
os.makedirs(base_model_path, exist_ok=True)

def download_and_save_model(model_name, save_directory, model_type='qa'):
    if model_type == 'qa':
        print(f"Descargando modelo QA: {model_name}")
        model = AutoModelForQuestionAnswering.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    elif model_type == 'gpt':
        print(f"Descargando modelo GPT: {model_name}")
        model = GPTNeoForCausalLM.from_pretrained(model_name)
        tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    else:
        raise ValueError(f"Model type '{model_type}' not supported.")
    
    print(f"Guardando modelo en {save_directory}")
    model.save_pretrained(save_directory)
    tokenizer.save_pretrained(save_directory)
    print(f"Modelo guardado en {save_directory}")

# Descargar y guardar los modelos en sus respectivas carpetas
download_and_save_model('EleutherAI/gpt-neo-1.3B', os.path.join(base_model_path, 'gpt'), model_type='gpt')
download_and_save_model('distilbert-base-uncased', os.path.join(base_model_path, 'qa'), model_type='qa')
