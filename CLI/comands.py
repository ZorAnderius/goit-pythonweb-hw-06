from prompt_toolkit.completion import WordCompleter

def command_completer():
    commands = [
        "create-teacher", "list-teachers", "update-teacher", "delete-teacher",
        "create-group", "list-groups", "update-group", "delete-group",
        "create-grade", "list-grades", "update-grade", "delete-grade",
        "create-student", "list-students", "update-student", "delete-student",
        "create-subject", "list-subjects", "update-subject", "delete-subject",
        "help", "seed-data", "clean-all-tables",
        "exit"
    ]
    return WordCompleter(commands)