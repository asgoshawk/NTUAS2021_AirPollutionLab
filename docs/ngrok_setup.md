## Ngrok 設定

在前面章節的伺服器建立中，若 Raspberry Pi 是位在區域網路內，其 IP 通常會長這樣：
* 192.168.x.x
* 172.16.x.x
* 10.0.x.x

這些 IP 為專用網路，通常在同個區域網路內的時候，可以藉由這些位址來連線，但是在外部網路就無法連入，除非透過通訊埠轉發 (Port fowarding)，對外部開啟特定通訊埠來連到區域網路內的特定位址，但這個做法前提是所使用的路由器 (Router) 必須可以讓外部網路取得其位址 (如固定 IP 等)。若所在網路沒辦法直接讓外部連入且又想要透過外部網路和 Raspberry Pi 來連線的話，可以使用 [Ngrok](https://ngrok.com/) 這個反向代理 (Reverse proxy) 的工具，藉此可以設定特定的 port 並建立出一個網址來讓他人從外部連入。

![](https://i.imgur.com/OOn989V.png)

要使用 Ngrok 前，需要先[註冊](https://dashboard.ngrok.com/signup)一個帳號，這部分是免費的，不過每次就只能建立一個網址來使用且每次重啟都會產生出新的網址，只有付費用戶才能使用多個且固定的網址，不過對於單純測試開發 Webhook 來說其實夠用了。登入後進到 Getting Started -> Setup & Installation 會看到以下畫面，因為系統使用的是 Raspberry Pi OS (32-bit) ，所以需要下載的是 Linux (ARM) 這個版本的 ngrok，可以右鍵複製連結並用 `wget` 指令來下載檔案。

![](https://i.imgur.com/miHtnop.png)

下載後用 `unzip` 指令來解壓縮，解壓縮後回到網站看到第二點 Connect your account ，複製底下的指令到命令列執行，此部分執行一次就好，除非有另外重置 token。 

> 需要注意 `./ngrok authtoken` 後面的字串是你個人的 token，請不要公開給其他人。

接下來就可以用 `screen` [(操作部分詳見此章節)]() 來執行前面建立好的伺服器，此時要記得伺服器所開的 port 是多少，因為 ngrok 開啟服務時需要輸入對應的 port 才能讓他產生出的網址導到你伺服器所在位址。假如前面使用的程式碼 port 沒更改的話就是 5000，在 detach 當前的 screen 後輸入：

```bash
./ngrok http 5000
```

輸入完便會出現下面的畫面：

![](https://i.imgur.com/NONri04.png)

Forwarding 後面的網址 (https://[字串].ngrok.io) 便是 ngrok 所產生的網址，直接在瀏覽器上輸入此網址會導向你所建立的伺服器位址 (理論上和輸入 192.168.0.1:5000 的結果要相同)，不過有時候瀏覽器會顯示危險網站的警告訊息，這部分只要確定輸入的是自己的網址即可，但若是來源不明的 .ngrok.io 結尾網址就不要隨便連入。若要關掉此服務就只要 Ctrl + C 就可以離開，但要注意如果是免費方案的話，關掉後重啟 ngrok 所得到的網址就會是新的，在設定 Webhook 時還需留意。
