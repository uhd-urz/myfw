from typing import Annotated

import typer
from rya.styles import stdout_console

from ...loggers import get_logger
from ..commons import Typer

app = Typer(name="awesome", help="An example built-in plugin.", no_args_is_help=True)
logger = get_logger()


@app.command()
def greet(
    name: Annotated[
        str,
        typer.Option(
            "--name",
            "-n",
            help="The name to greet.",
            show_default=True,
        ),
    ] = "there",
):
    """
    An example command that greets the passing user `--name`.

    """
    logger.info("Greeting user.")
    stdout_console.print(f"Hi {name}. You are awesome!")
