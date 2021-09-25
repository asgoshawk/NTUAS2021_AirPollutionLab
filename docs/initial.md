## 系統更新及初始設定
由於剛安裝系統部分軟體不一定是最新的，因此通常安裝完後建議先更新系統，以取得最新的套件。本次使用的系統是用 apt 做套件管理，不過在更新前需要更改鏡像站，否則用預設的鏡像站來下載更新套件會非常緩慢，在此推薦用[自由軟體實驗室NCHC](http://free.nchc.org.tw/pmwiki/pmwiki.php/FSLab/MirrorLists)提供的 Mirror lists。輸入下列指令來編輯：
```bash=
sudo nano /etc/apt/sources.list
```
預設鏡像站為`http://raspbian.raspberrypi.org/raspbian/`，修改時把該行給註解掉，並複製該行把網址部分改成`http://free.nchc.org.tw/raspbian/raspbian/`即可，內容應該會變成這樣：

```bash=
deb http://free.nchc.org.tw/raspbian/raspbian/ buster main contrib non-free rpi
#deb http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
# Uncomment line below then 'apt-get update' to enable 'apt-get source'
#deb-src http://raspbian.raspberrypi.org/raspbian/ buster main contrib non-free rpi
```
順帶一提，buster 為本次安裝系統的發行版名稱，因此更改時只改網址的部分就好，若使用的發行版本不是 buster 更新時便會發生錯誤。修改完後便可儲存離開，接著執行下列指令：

```bash=
sudo apt update && sudo apt upgrade -y    # 更新套件庫資料及更新套件 
sudo apt autoremove -y                    # 自動清除不需要的套件
sudo apt clean                            # 清除下載時的暫存安裝檔
```

設定語系及時區需輸入：
```bash=
sudo raspi-config
```
應該會出現下列畫面，此時可用方向鍵來選取要設定的項目，用空白鍵勾選項目(打星號)，用 Tab 鍵來切換到底下的兩個選項。語系及時區的設定在 Localisation Options 內，可自行更改。

![](https://i.imgur.com/XiTJ4dG.png)

完成設定後建議重新啟動來讓已更新的套件及設定生效，輸入以下第一個指令：
```bash=
sudo reboot             # 重新啟動
sudo poweroff           # 直接切斷電源關機
sudo shutdown -h now    # 會關閉程式後再關機 
```
