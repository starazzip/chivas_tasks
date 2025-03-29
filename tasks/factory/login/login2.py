class LoginManager:
    def login(self, method):
        print(f"\n嘗試使用 {method.upper()} 登入：")

        if method == "google":
            print("[Google] 跳轉到 OAuth 授權頁面")
            print("取得 access token")
            print("擷取使用者資料（email, name, picture）")
            print("登入成功")

        elif method == "facebook":
            print("[Facebook] 連接 Facebook Graph API")
            print("驗證 token")
            print("擷取使用者基本資訊")
            print("登入成功")

        elif method == "username":
            print("輸入帳號密碼")
            print("資料庫查詢帳號")
            print("驗證密碼哈希")
            print("登入成功")


        elif method == "github":
            print("[GitHub] 跳轉到 GitHub OAuth")
            print("拿到 token 後呼叫 GitHub API")
            print("解析使用者名稱與 repo 資訊")
            print("登入成功")

        else:
            print("不支援的登入方式")


manager = LoginManager()
for method in ["google", "facebook", "username", "github"]:
    manager.login(method)
