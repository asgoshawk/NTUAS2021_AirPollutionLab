## Rclone
(Edited by Wei-Chieh Huang)<br>
有疑問請找：黃維傑 (r09229001@ntu.edu.tw)  2021.10.23

  * [安裝與更新](###安裝與更新)
  * [建立專案](###建立專案)
  * [建立連結](###建立連結)
  * [資料傳輸](###資料傳輸)

### 安裝與更新
套件安裝
`sudo apt-get install rclone`
更新到最新版本
```
cd /tmp
wget https://downloads.rclone.org/v1.47.0/rclone-v1.47.0-linux-arm.deb
sudo apt install ./rclone-v1.47.0-linux-arm.deb 
rm rclone-v1。 47.0-linux-arm.deb
```
### 建立專案
1. 登入[google cloud console](https://console.developers.google.com/)
2. 點選頂端列的專案選項，建立新的專案

![](https://i.imgur.com/08nb8OA.png)

3. 點選"+啟用API和服務(+ ENABLE APIS AND SERVICES)"<br>
   搜尋Google Drive API並啟用

![](https://i.imgur.com/YYv74h1.png)

4. 進入Google Drive API在左側點選憑證(Credentials)<br>
   建立憑證 → 選擇 OAuth 客戶端 ID (OAuth client ID)

![](https://i.imgur.com/jor3Jl9.png)

<details>
   若出現阻擋需先進行註冊認證

   → 進入 API 和服務中的憑證頁面<br>
   → 左列欄點選 OAuth 同意畫面<br>
   → 設定 OAuth 用戶名字<br>
   → 增添範圍選擇../auth/drive.*~ (可以搜尋Google drive API選取)

   ![](https://i.imgur.com/MtNN2lh.png)
</details>

5. 類型選擇電腦版應用程式(Desktop app)，憑證名稱可以取自己喜歡的

![](https://i.imgur.com/L3Dmtts.png)

6. 獲得憑證用戶端的ID及密碼

![](https://i.imgur.com/OUOnfwV.png)

資訊會存放在箭頭指向這邊

![](https://i.imgur.com/lyLe0cJ.png)

<details>
   若後續出現連接問題，可能是需要做程式認證<br>

   → 進入 API 和服務中的憑證頁面<br>
   → 左列欄點選設定 OAuth 同意畫面，進入"編輯應用程式"<br>
   ![](https://i.imgur.com/VXeAOXM.png)<br>
   → 給予應用程式網域(後面RPi連接會看到)及授權網域(可以直接打google.com)<br>
   → 在範圍/示範影片：範圍的預計使用方式/ 貼上一個youtube網址，可使用 "https://www.youtube.com/watch?v=f8K-V3HHDA0" 作證明<br>
   → 申請驗證後再測試一次<br>
</details>



### 建立連結
回到 RPi 輸入 `rclone config` 創建新的 remote<br>
依序回答下列問題：
1.  `Type of storage to configure.`<br>
    `Enter a string value. Press Enter for the default ("").`<br>
    `Choose a number from below, or type in your own value`<br>
    > 選擇 12 (Google Drive "drive")

2.  分別輸入專案的帳號(client_id)及密碼(client_secret)<br>

3.  `Scope that rclone should use when requesting access from drive.`<br>
    `Enter a string value. Press Enter for the default ("").`<br>
    `Choose a number from below, or type in your own value`<br>
    > 選擇 1 (Full access all files, excluding Application Data Folder."drive")

4.  `root_folder_id` 和 `service_account_file` 可以不做設定，直接 enter 進入預設

5.  `Edit advanced config? (y/n)`
    > 選擇 n (不需要高階功能)

6.  `Remote config`<br>
    `Use auto config?`<br>
    `  * Say Y if not sure`<br>
    `  * Say N if you are working on a remote or headless machine`<br>
    > 選擇 n (直接連線操作不需要此項)

7.  `If your browser doesn't open automatically go to the following link:` **(這邊會拿到一個網址)**<br>
    `Log in and authorize rclone for access`
    > 網址會給你一串認證碼，回來輸入
    ![](https://i.imgur.com/zdmLQdp.png)

    > [!WARNING] 
    > 若沒有出現認證碼，而是跳出錯誤訊息，請看到「建立專案」的最後一點操作   

8.  `Configure this as a team drive?`
    >選擇 n (單一連接不需此功能)

9.  完成設定，可以退出 rclone config<br>
    輸入`rclone ls --max-depth 1 (remote名稱):`可以測試是否成功連接

### 資料傳輸

```bash
# /usr/bin/rclone -v sync (RPi内需傳輸檔案位置) (remote名稱):(雲端上的路徑，若在主目錄上可以空白) --include "(檔案名稱)" --retries 1  --log-file=(提醒訊息存放位置)
# e.g.
/usr/bin/rclone -v sync /home/pi/ gdrive: --include "rgb_pwm.py" --retries 1  --log-file=/home/pi/rclone.log
```
即可完成資料傳輸，可以到google drive檢查確認

參考資料來源：
[Mounting Google Drive on Raspberry Pi](https://medium.com/@artur.klauser/mounting-google-drive-on-raspberry-pi-f5002c7095c2)
