class CalendarWithHistory:
    def __init__(self):
        self.events = {}
        self.history = []        # list of (action, data)
        self.redo_stack = []

    def add_event(self, date, title):
        self.events[date] = title
        self.history.append(("add", date, title))
        self.redo_stack.clear()
        print(f"新增：{date} - {title}")

    def remove_event(self, date):
        if date in self.events:
            removed = self.events.pop(date)
            self.history.append(("remove", date, removed))
            self.redo_stack.clear()
            print(f"移除：{date} - {removed}")
        else:
            print("無此活動")

    def undo(self):
        if not self.history:
            print("無動作可撤銷")
            return
        action, date, title = self.history.pop()
        if action == "add":
            self.events.pop(date, None)
            print(f"↩撤銷新增：{date}")
        elif action == "remove":
            self.events[date] = title
            print(f"↩撤銷移除：{date} - {title}")
        self.redo_stack.append((action, date, title))

    def redo(self):
        if not self.redo_stack:
            print("無動作可重做")
            return
        action, date, title = self.redo_stack.pop()
        if action == "add":
            self.events[date] = title
            print(f"重做新增：{date} - {title}")
        elif action == "remove":
            self.events.pop(date, None)
            print(f"重做移除：{date}")
        self.history.append((action, date, title))

    def show(self):
        print("目前活動：", self.events)


if __name__=="__main__":

    # 操作範例：新增蜜月 → 新增面試 → Undo 兩次 → Redo 一次
    cal = CalendarWithHistory()

    # 1. 新增「蜜月」
    cal.add_event("2025-05-01", "蜜月")
    cal.show()
    # 2. 新增「面試」
    cal.add_event("2025-05-03", "面試")
    cal.show()
    # 3. Undo（撤銷面試）
    cal.undo()
    cal.show()
    # 4. Undo（撤銷蜜月）
    cal.undo()
    cal.show()
    # 5. Redo（重做蜜月）
    cal.redo()
    cal.show()
    # 顯示當前活動
    cal.show()