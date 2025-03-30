class Calendar:
    def __init__(self):
        # 用來儲存日期與活動名稱的字典
        self.events = {}
        # 執行紀錄，需將每個命令存在堆疊裡
        self.history = []
        # 撤回紀錄，需將每個撤回命令存在堆疊裡
        self.redo_stack = []

    # 新增活動方法 
    def add_event(self, date, title):        
        self.events[date] = title
        # 紀錄命令
        self.history.append(("add", date, title))
        # 有新命令就將撤回紀錄清空
        self.redo_stack.clear()
        print(f"新增：{date} - {title}")

    # 移除活動
    def remove_event(self, date):
        if date in self.events:
            removed = self.events.pop(date)
            self.history.append(("remove", date, removed))
            self.redo_stack.clear()
            print(f"移除：{date} - {removed}")
        else:
            print("無此活動")

    # 撤回方法
    def undo(self):
        # 如果沒有執行紀錄則無法撤回
        if not self.history:
            print("無動作可撤回")
            return
        # 取出最後一筆執行紀錄
        action, date, title = self.history.pop()
        
        # 根據指令內容掉用對應方法
        if action == "add":
            self.events.pop(date, None)
            print(f"撤回新增：{date}")
        elif action == "remove":
            self.events[date] = title
            print(f"撤回移除：{date} - {title}")
        # 將撤回的動作放入重做堆疊中
        self.redo_stack.append((action, date, title))

    # 重做方法
    def redo(self):
        # 如果重做堆疊為空則無法重做
        if not self.redo_stack:
            print("無動作可重做")
            return
        # 取出最後一個被撤回的動作 
        action, date, title = self.redo_stack.pop()
        if action == "add":
            self.events[date] = title
            print(f"重做新增：{date} - {title}")
        elif action == "remove":
            self.events.pop(date, None)
            print(f"重做移除：{date}")
        # 重做完後，動作重新放進執行堆疊中
        self.history.append((action, date, title))

    def show(self):
        print("目前活動：", self.events)


if __name__ == "__main__":
    # 測試操作流程
        
    calendar = Calendar()

    # 添加蜜月
    calendar.add_event("2025-05-01", "蜜月")
    calendar.show()

    # 添加面試
    calendar.add_event("2025-05-03", "面試")
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