from abc import ABC


# 定義命令的抽象類別，規範子類應該實作的方法
class Command(ABC):
    def execute(self): pass
    def undo(self): pass

# 添加活動命令類別
class AddEventCommand(Command):
    def __init__(self, calendar, date, title):
        self.calendar = calendar
        self.date = date
        self.title = title

    # 執行添加方法
    def execute(self):
        self.calendar.events[self.date] = self.title
        print(f"新增：{self.date} - {self.title}")

    # 撤回添加方法
    def undo(self):
        self.calendar.events.pop(self.date, None)
        print(f"撤回新增：{self.date}") 

# 移除活動命令類別
class RemoveEventCommand(Command):
    def __init__(self, calendar, date):
        self.calendar = calendar
        self.date = date
        self.removed = None

    # 執行移除方法
    def execute(self):
        self.removed = self.calendar.events.pop(self.date, None)
        print(f"移除：{self.date}")

    # 撤回移除動作
    def undo(self):
        if self.removed:
            self.calendar.events[self.date] = self.removed
            print(f"撤回移除：{self.date} - {self.removed}") 

# 行事曆類別
class Calendar:
    def __init__(self):
        self.events = {}
        self.history = []
        self.redo_stack = []

    # 專注於執行命令，不需要管命令邏輯
    def execute(self, command):
        command.execute()
        self.history.append(command)
        self.redo_stack.clear()

    # 專注撤回行命令
    def undo(self):
        if self.history:
            cmd = self.history.pop()
            cmd.undo()
            
            # 有撤回才會有撤回列表
            self.redo_stack.append(cmd)
        else:
            print("無動作可撤回") 

    # 重做就是將撤回列表取出執行
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
    # 測試操作流程
    
    calendar = Calendar()

    # 添加蜜月
    cmd1 = AddEventCommand(calendar, "2025-05-01", "蜜月")
    calendar.execute(cmd1)
    calendar.show()
    # 添加面試
    cmd2 = AddEventCommand(calendar, "2025-05-03", "面試")
    calendar.execute(cmd2)
    calendar.show()
    
    # 撤回面試
    calendar.undo()
    calendar.show()
    
    # 撤回蜜月
    calendar.undo()
    calendar.show()
    
    # 重做蜜月 
    calendar.redo()

    # 顯示最後結果
    calendar.show()