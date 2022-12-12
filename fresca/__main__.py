import typer

from pathlib import Path

from fresca import __version__, __commit__

APP_NAME = "fresca"
CLI = typer.Typer(name=APP_NAME, no_args_is_help=True)
CONFIG_DIR = typer.get_app_dir(APP_NAME)
CONFIG_PATH = Path(CONFIG_DIR) / "fresca.toml"


@CLI.command(help="Prints the installed fresca version")
def version():
    typer.echo(f"fresca v{__version__} ({__commit__})")


@CLI.command(help="Installs fresca for first-time use")
def install(
    config: Path = typer.Option(CONFIG_PATH),
):
    if config.exists():
        print("Config exists")
    else:
        print(f"No config!: {config}")


@CLI.command(help="Checks fresca update rules")
def check(config: typer.FileText = typer.Option(CONFIG_PATH)):
    print(config.read())


@CLI.command(help="Applies updates to any outdated software per update rules")
def update(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")
