from pathlib import Path
from fastapi.templating import Jinja2Templates

# 1. Encontra o caminho absoluto para o diretório ONDE ESTE ARQUIVO (config.py) ESTÁ.
#    Ex: C:/Users/20221imi005/Desktop/obratto/OBRATTO/
# BASE_DIR = Path(__file__).resolve().parent

# 2. Define o caminho para a pasta de templates de forma absoluta.
#    Junta o caminho base com o nome da pasta "templates".
#    Ex: C:/Users/20221imi005/Desktop/obratto/OBRATTO/templates
# TEMPLATE_DIR = BASE_DIR / "templates"

# 3. Cria a instância de templates usando este caminho absoluto.
#    Agora não há como o programa se confundir sobre onde procurar.
templates = Jinja2Templates("templates")
