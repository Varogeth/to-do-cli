from sys import argv
import json
import data
import actions

def main():
    action = argv[1]

    db = data.load_data()
    id_counter = db["id_counter"]
    tasklist = db["tasks"]

    if action == "add": actions.add(tasklist, id_counter, argv[2])
    elif action == "list": actions.list(tasklist)
    elif action == "delete": actions.delete(tasklist, int(argv[2]))
    else: print(f"Invalid command [{action}]:\nPlease enter a valid command! (add, list, or delete)")
    
    db = json.dumps(db)
    data.save_data(db)


main()
