import argparse
from datetime import time
from time import sleep
from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from rich.console import Console

from CLI.comands import command_completer
from CLI.handle_commands import handle_command
from config.db import get_db
from queries.seed import seed_groups, seed_teachers, seed_subjects, seed_students, seed_grades

style = Style.from_dict({
    'command': '#ffcc00',
})
console = Console()


def execute_query():
    db = next(get_db())
    try:
        pass
    finally:
        db.close()

def main():
    console.print("Welcome to the University CLI! 🎓", style="bold green")
    completer = command_completer()

    session = PromptSession(completer=completer)
    try:
        while True:
            user_input = session.prompt([('class:command', 'Command: ')])
            if user_input:
                command, *args = user_input.split()
                if command in ("exit", "close"):
                    console.print("\nGoodbye!", style="bold blue")
                    break
                handle_command(command, args)
    except (KeyboardInterrupt, EOFError):
        console.print("\nGoodbye!", style="bold blue")

if __name__ == '__main__':
    execute_query()
    main()
    # print("Seeding database...")
    # groups = seed_groups()
    # print(f"Created {len(groups)} groups.")
    # teachers = seed_teachers()
    # print(f"Created {len(teachers)} teachers.")
    # subjects = seed_subjects(teachers)
    # print(f"Created {len(subjects)} subjects.")
    # students = seed_students(groups)
    # print(f"Created {len(students)} students.")
    # seed_grades(students, subjects)
    # print("Grades have been added.")
    # print("Seeding complete!")
