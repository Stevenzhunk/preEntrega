import logging
import pathlib
from datetime import datetime

# Crear carpeta de logs
audit_dir = pathlib.Path("logs")
audit_dir.mkdir(exist_ok=True)

# Generar identificador por ejecución
timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")

# Configuración global
logging.basicConfig(
    filename=audit_dir / f"log_{timestamp}.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    force=True
)

# Logger del proyecto
logger = logging.getLogger("TalentoTech")