import typer
from .generator import gen

app = typer.Typer(help="A simple command line password generator")

@app.command()
def generate(length: int = None):
    """
    Generate a password with given length
    :param length: the length of the generated password
    :return: the generated password
    """
    typer.echo("Generating passwords...")
    typer.echo(gen(length))

@app.command()
def genc(length: int):
    """
    Generate a more complex password given a certain length.
    :param length: the length of the generated password
    :return: the generated password
    """
    typer.echo("Generating passwords...")
    typer.echo(gen(length))

if __name__ == "__main__":
    app()

