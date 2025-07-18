import typer

from . import hello

app = typer.Typer()


@app.command()
def run():
    hello()


def entrypoint():
    app()
