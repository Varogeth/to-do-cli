def list(tasklist):
    for task in tasklist:
        print(f"{task["id"]}. {task["label"]}")


def add(data, task):
    data["id_counter"] += 1
    new_task = {"id": data["id_counter"], "label": task}
    data["tasks"].append(new_task)

def delete(tasklist, id):
    for task in tasklist:
        if task["id"] == id:
            tasklist.remove(task)
