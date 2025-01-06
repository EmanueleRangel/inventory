import sys
from pathlib import Path

# Adiciona o diretório raiz ao PYTHONPATH
sys.path.append(str(Path(__file__).resolve().parent))

# Execute o módulo
import package.module2 # type: ignore
