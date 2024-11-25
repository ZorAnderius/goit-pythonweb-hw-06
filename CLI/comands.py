from prompt_toolkit.completion import WordCompleter

def command_completer():
    commands = [
        "create-teacher", "list-teachers", "update-teacher", "delete-teacher",
        "create-group", "list-groups", "update-group", "delete-group",
        "create-grade", "list-grades", "update-grade", "delete-grade",
        "create-student", "list-students", "update-student", "delete-student",
        "create-subject", "list-subjects", "update-subject", "delete-subject",
        "select_1", "select_2","select_3","select_4","select_5","select_6",
        "select_7", "select_8","select_9","select_10","select_11","select_12",
        "seed-data", "clean-all-tables",
        "help", "exit"
    ]
    return WordCompleter(commands)