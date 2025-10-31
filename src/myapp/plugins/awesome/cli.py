from typing import Annotated

import typer
from rya.styles import stdout_console

from ..commons import Typer

app = Typer(name="awesome", help="An example built-in plugin.")


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
    stdout_console.print(f"Hi {name}. You are awesome!")
