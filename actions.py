def list(tasklist):
    for task in tasklist:
        print(f"{task["id"]}. {task["label"]}")


def add(tasklist, inc, task):
    inc += 1
    new_task = {"id": inc, "label": task}
    tasklist.append(new_task)

def delete(tasklist, id):
    for task in tasklist:
        if task["id"] == id:
            tasklist.remove(task)
