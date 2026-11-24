
import logging
import pathlib

import logging

# Crear carpeta de logs
audit_dir = pathlib.Path("logs")
audit_dir.mkdir(exist_ok=True)

# Configuración global
logging.basicConfig(
    filename=audit_dir / "suite.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s - %(message)s",
    datefmt="%H:%M:%S",
    force=True
)

# Logger del proyecto
logger = logging.getLogger("talentolab")
