class Command:
    def execute(self): pass
    def undo(self): pass

class AddEventCommand(Command):
    def __init__(self, calendar, date, title):
        self.calendar = calendar
        self.date = date
        self.title = title

    def execute(self):
        self.calendar.events[self.date] = self.title
        print(f"新增：{self.date} - {self.title}")

    def undo(self):
        self.calendar.events.pop(self.date, None)
        print(f"撤銷新增：{self.date}")

class RemoveEventCommand(Command):
    def __init__(self, calendar, date):
        self.calendar = calendar
        self.date = date
        self.removed = None

    def execute(self):
        self.removed = self.calendar.events.pop(self.date, None)
        print(f"移除：{self.date}")

    def undo(self):
        if self.removed:
            self.calendar.events[self.date] = self.removed
            print(f"撤銷移除：{self.date} - {self.removed}")

class CalendarWithCommand:
    def __init__(self):
        self.events = {}
        self.history = []
        self.redo_stack = []

    def execute(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
            self.redo_stack.append(cmd)
        else:
            print("無動作可撤銷")

    def redo(self):
        if self.redo_stack:
            cmd = self.redo_stack.pop()
            cmd.execute()
            self.history.append(cmd)
        else:
            print("無動作可重做")

    def show(self):
        print("目前活動：", self.events)

if __name__=="__main__":
        # 🧪 測試操作流程
    cal = CalendarWithCommand()

    # 1. 添加蜜月
    cmd1 = AddEventCommand(cal, "2025-05-01", "蜜月")
    cal.execute(cmd1)
    cal.show()
    # 2. 添加面試
    cmd2 = AddEventCommand(cal, "2025-05-03", "面試")
    cal.execute(cmd2)
    cal.show()
    # 3. Undo（撤銷面試）
    cal.undo()
    cal.show()
    # 4. Undo（撤銷蜜月）
    cal.undo()
    cal.show()
    # 5. Redo（重做蜜月）
    cal.redo()

    # 顯示結果
    cal.show()