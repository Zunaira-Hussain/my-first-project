class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done
        
    def __show__(self):
        status = "done" if self.done else "Not done"
        return f"{status} - {self.title}"
    
    def __complete__(self):
        self.done = True
        print(f"Task {self.title} marked as done.")
        
    def __to_dict__(self):
        print(Task ('Buy Milk').__to_dict__())
        return {"title": self.title, "done": self.done}
    
    
class PriorityTask(Task):
    def __init__(self, title,priority, done=False):
        super(). __init__(title, done)
        self.priority = priority 
        
    def __show__(self):
        status = "done" if self.done else "Not done"
        return f"{status} - {self.title} (Priority: {self.priority})"
    
    def __to_dict__(self):
        return {"title": self.title, "done": self.done, "priority": self.priority}
    
p = PriorityTask("Pay rent", "high")
print(p.show())        # [ ] Pay rent (high)
print(p.to_dict())     # {'title': 'Pay rent', 'done': False, 'priority': 'high'}