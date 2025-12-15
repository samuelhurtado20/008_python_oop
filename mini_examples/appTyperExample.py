# pip install typer[all] 
# uv add typer[all]
import typer

# Create the Typer app
app = typer.Typer(help="A simple console app example with commands.")

# Command: greet
@app.command()
def greet(name: str, excited: bool = typer.Option(False, help="Add excitement!")):
    """
    Greet a user by name.
    """
    message = f"Hello, {name}"
    if excited:
        message += "!!! 🎉"
    typer.echo(message)

# Command: add
@app.command()
def add(a: float, b: float):
    """
    Add two numbers and display the result.
    """
    try:
        result = a + b
        typer.echo(f"The sum of {a} and {b} is {result}")
    except Exception as e:
        typer.echo(f"Error: {e}")

# Command: repeat
@app.command()
def repeat(text: str, times: int = 1):
    """
    Repeat a given text a number of times.
    """
    if times < 1:
        typer.echo("Times must be at least 1.")
        raise typer.Exit(code=1)
    for _ in range(times):
        typer.echo(text)

# Command: primo
@app.command()
def primo(n: int) -> str:
    # convert to int
    n = int(n)
    prime = True
    if n <= 1:
        prime = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break
    typer.echo(f"{n} no es un número primo.") if prime else typer.echo(f"{n} es un número primo.")

if __name__ == "__main__":
    app()
