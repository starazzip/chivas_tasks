# 抽象介面
class LoginHandler:
    def login(self):
        raise NotImplementedError

# Google 登入流程
class GoogleLoginHandler(LoginHandler):
    def login(self):
        print("[Google] 跳轉到 OAuth 授權頁面")
        print("取得 access token")
        print("擷取使用者資料（email, name, picture）")
        print("登入成功")

# Facebook 登入流程
class FacebookLoginHandler(LoginHandler):
    def login(self):
        print("[Facebook] 連接 Facebook Graph API")
        print("驗證 token")
        print("擷取使用者基本資訊")
        print("登入成功")

# 帳號密碼登入流程
class UsernamePasswordLoginHandler(LoginHandler):
    def login(self):
        print("輸入帳號密碼")
        print("資料庫查詢帳號")
        print("驗證密碼哈希")
        print("登入成功")

# GitHub 登入流程
class GithubLoginHandler(LoginHandler):
    def login(self):
        print("[GitHub] 跳轉到 GitHub OAuth")
        print("拿到 token 後呼叫 GitHub API")
        print("解析使用者名稱與 repo 資訊")
        print("登入成功")

# 工廠
class LoginFactory:
    def get_handler(self, method):
        if method == "google":
            return GoogleLoginHandler()
        elif method == "facebook":
            return FacebookLoginHandler()
        elif method == "username":
            return UsernamePasswordLoginHandler()
        elif method == "github":
            return GithubLoginHandler()
        else:
            raise ValueError("不支援的登入方式")

# 使用端
factory = LoginFactory()
for method in ["google", "facebook", "username","github"]:
    handler = factory.get_handler(method)
    print(f"\n嘗試使用 {method.upper()} 登入：")
    handler.login()
