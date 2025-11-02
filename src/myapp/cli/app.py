from rya.cli import app
from rya.config import AppConfig

from ..loggers import get_logger
from ..styles import stdout_console

logger = get_logger()


@app.command(
    name="print-config",
    short_help="An example command that prints the validated configuration.",
)
def print_validated_config():
    """
    Print the validated configuration.
    """
    stdout_console.print("Validated configuration:")
    stdout_console.print(AppConfig.validated)
