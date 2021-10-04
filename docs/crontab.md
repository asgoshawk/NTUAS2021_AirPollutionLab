## Crontab

Crontab 是一個排程自動執行工具，可以讓系統定時或在特定時間執行想要的程式或指令。要編輯排程可以在命令列輸入：

```bash
crontab -e
```

若是第一次使用會出現下列畫面選擇編輯器：

![](https://i.imgur.com/TBmlpdD.png)

在這邊建議使用 `nano` 這個編輯器，所以輸入 1 後再按 enter 就會進到編輯器畫面，基本上會需要輸入六項參數：

```bash
# 引用自 GTWang 的網站
# ┌───────────── 分鐘   (0 - 59)
# │ ┌─────────── 小時   (0 - 23)
# │ │ ┌───────── 日     (1 - 31)
# │ │ │ ┌─────── 月     (1 - 12)
# │ │ │ │ ┌───── 星期幾 (0 - 7，0 是週日，6 是週六，7 也是週日)
# │ │ │ │ │
# * * * * * /path/to/command
```

\# 為註解也就是 crontab 不會執行的部分，而 \* 代表任意數值 (整數)，以下提供簡單範例：

```bash
# 每天的 12:00 用bash 執行 hello.sh
0 12 * * * /bin/bash /home/pi/hello.sh

# 每 10 分鐘執行 echo 寫入 hello 到 hello.txt
*/10 * * * * /usr/bin/echo "hello" >> /home/pi/hello.txt

# 開機後等待 60 秒後用 python3 執行 my.py (僅執行一次)
@reboot sleep 60 ; /usr/bin/python3 /home/pi/my.py    
```

在編輯 crontab 排程時，建議要使用指令及檔案的絕對路徑，以免 crontab 在執行排程時會不知道他在那裡執行或發生錯誤等等。編輯完並存檔後排程不會馬上生效，可以輸入以下指令重啟 crontab 服務，讓排程生效：

```bash
sudo /etc/init.d/cron restart

# 或是輸入下列指令
sudo service cron restart
```

將 Raspberry Pi 重新啟動亦可以讓 crontab 服務套用編輯後的排程。另外可以輸入 `crontab -l` 來列出目前有的排程工作，其他特殊排程或更詳細的說明可以參考 [Linux 設定 crontab 例行性工作排程教學與範例](https://blog.gtwang.org/linux/linux-crontab-cron-job-tutorial-and-examples/) 這篇文章。至於時間上的設定也可以利用 [Crontab guru](https://crontab.guru/) 來檢查是否是想要設定的排程時間。