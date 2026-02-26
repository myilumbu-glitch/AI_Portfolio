tasks = [
    {'text' : 'Exercise', 'done' : False},
    {'text' : 'Study', 'done' : True},
    {'text' : 'Sleep', 'done' : False},
    {'text' : 'Dance', 'done' : True} 
]

def mark_task_done(tasks, task_text):
    for task in tasks:
        if task['text'] == task_text:
            task['done'] = True

def delete_task(tasks, task_text):
    for task in tasks[:]:   # loop over copy
        if task['text'] == task_text:
            tasks.remove(task)

def rename_task(tasks, old_text, new_text): 
    for task in tasks: 
        if task['text'] == old_text: 
            task['text'] = new_text

def count_done(tasks):
    count = 0
    for task in tasks:
        if task['done']:
            count += 1
    return count

def get_undone_tasks(tasks):
    return [task['text'] for task in tasks if not task['done']]

if __name__ == "__main__":
    tasks = [
        {'text' : 'Exercise', 'done' : False},
        {'text' : 'Study', 'done' : True},
        {'text' : 'Sleep', 'done' : False},
        {'text' : 'Dance', 'done' : True} 
    ]

        

print("Undone tasks:", get_undone_tasks(tasks))
print("Done count:", count_done(tasks))


