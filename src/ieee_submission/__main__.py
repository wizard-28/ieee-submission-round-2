import typer
from rich import print
from rich.prompt import Prompt
from simple_term_menu import TerminalMenu

from ieee_submission.stack import EmptyStackError, Stack

from typing import Protocol


class SupportsStr(Protocol):
    def __str__(self) -> str: ...


app = typer.Typer(name="ieee_submission", no_args_is_help=True, add_completion=False)

input_prefix = "[bold][blue]<[/blue]"
output_prefix = "[bold][blue]>[/blue]"


def print_msg(message: str, value: SupportsStr = "", color: str = "green") -> None:
    print(f"{output_prefix} [{color}]{message}[/{color}] {value}")


def print_err(message: str, value: SupportsStr = "") -> None:
    print(f"[bold][red]{message}[/red] {value}")


@app.command()
def stack() -> None:
    stack = Stack()
    while True:
        options = ["push", "pop", "top", "getMin", "getMax", "exit"]
        terminal_menu = TerminalMenu(options, title="Select an operation")
        menu_entry_index = terminal_menu.show()
        assert isinstance(menu_entry_index, int)

        choice = options[menu_entry_index]

        match choice:
            case "push":
                try:
                    val = Prompt.ask(f"{input_prefix} Enter your value", default="5")
                    stack.push(int(val))
                    print_msg("Pushed!")
                except ValueError as e:
                    print_err("Invalid input:", e)
            case "pop":
                try:
                    print_msg("Popped:", stack.pop())
                except EmptyStackError as e:
                    print_err("Error:", e)
            case "top":
                try:
                    print_msg("Top element:", stack.top())
                except EmptyStackError as e:
                    print_err("Error:", e)
            case "getMin":
                try:
                    print_msg("Min element:", stack.getMin())
                except EmptyStackError as e:
                    print_err("Error:", e)
            case "getMax":
                try:
                    print_msg("Max element:", stack.getMax())
                except EmptyStackError as e:
                    print_err("Error:", e)
            case "exit":
                print("[bold]Goodbye!")
                break


if __name__ == "__main__":
    app()
