## 建立 Web 伺服器 (Flask)

### 基本範例

![](https://i.imgur.com/0fyvq7G.png)

[Flask](https://flask.palletsprojects.com/en/2.0.x/) 是以 Python 所編寫的輕量級 Web 開發應用框架，另外也有較完整的框架如 [Django](https://www.djangoproject.com/) 等等，適合用於建立大型的網站，不過本次實作目的是透過網路對伺服器發出一個 Request 後，再讓伺服器控制我們的RGB燈泡，故使用這類的框架，而如果想用來建立靜態網頁，Flask 其實也足以應付這類的開發，有興趣可以自行尋找相關教學。在建立伺服器前，首先需要下載 Flask 套件：
```
pip3 install Flask
```

下載完後便可以開始簡單撰寫程式碼，輸入 `nano webapp.py` 後開始編輯，範例如下所示：
```python
from flask import Flask

app = Flask(__name__)

@app.route("/")              
def hello():
    return "Hello world!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
```

編輯完後存檔，在命令列輸入 `python3 webapp.py` 就可以啟動伺服器，同時也會自己顯示伺服器的所在 IP 。若要關閉伺服器，在鍵盤上按下 Ctrl + C 即可關閉。另外上述程式碼有建立一個 "/" 的路由 (假設伺服器 IP 為 192.168.0.1 且連接埠設為5000)，所以當連線至 192.168.0.1:5000/ 時，伺服器便會判斷路由並執行 hello() 這個函式並在網頁上顯示 Hello world! 這個字串，但如果輸入的是不存在的路由就會顯示 404 Not Found 這類的內容。若需要新增一個路由，可在 "/" 後自己新增另一個路由，理論上會長這樣： 

```python
@app.route("/")              
def hello():
    return "Hello world!"

@app.route("/new")
def new_route():
    return "My new route!"
```

重新啟動伺服器後，連線至 192.168.0.1:5000/new 時就會顯示 My new route! 這個內容了。

### 透過伺服器控制 RGB LED

根據上述程式碼，我們可以設定不同路由來執行我們想要的函式，所以將程式碼稍作改寫後，是可以用來控制 RGB LED 的，範例程式碼可以藉由下列指令來下載：

```bash
wget https://raw.githubusercontent.com/asgoshawk/NTUAS2021_AirPollutionLab/gh-pages/example_code/webapp_with_rgb.py
```

不過因為有使用到 `rgb_pwm.py` 定義的類別，所以記得要從[這個章節](gpio_rgb.md)的最後來下載 `.py` 檔，並確定這兩個程式碼要在同個目錄裡。載完後就可以執行 `python3 webapp_with_app.py` 並試著連線到不同路由來控制 RGB LED 了。 
