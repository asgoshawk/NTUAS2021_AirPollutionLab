# Raspberry Pi 基本操作教學
Raspberry Pi 是由樹莓派基金會所開發的單板微型電腦(Single Board Computer)，其使用 Broadcom 出產的 ARM 架構晶片作為主要處理器，可以運作類 Unix 、 Android 、 FreeBSD 或是 Windows (ARM 版本的 Windows 11 甚至可在第四代主機板運行)等作業系統。

## Raspberry Pi 系統的燒錄與安裝
一般而言會建議新手參考官網的文件來安裝系統，在這邊非常推薦下載官網提供的 [Raspberry Pi Imager](https://www.raspberrypi.org/software/) 來安裝系統。另外也可以使用 [Etcher](https://www.balena.io/etcher/) 這套軟體來進行系統燒錄，但需要額外到官網下載作業系統的映像檔來燒錄。目前主流的系統叫 Raspberry Pi OS (舊版的叫 Raspbian)，跟 Ubuntu 同為 Debian 體系下的發行版，是由官方所維護的，不過目前只有32位元的版本，64位元的版本仍然在Beta測試階段。安裝的方式很簡單：
1. 插入新的SD卡至讀卡機並連接到電腦
2. 打開 Raspberry Pi Imager，選取想要安裝的系統(CHOOSE OS)及SD卡位置(CHOOSE STORAGE)
3. 按下 WRITE 後會自動下載所需的映像檔，接著等待燒錄完成
4. 將燒錄好系統的SD卡插入 Raspberry Pi 的SD卡插槽即可

![Raspberry Pi Imager的介面](https://i.imgur.com/d3bj2tj.png)

> 在這邊提醒，如果是用 Windows 系統來操作這部分燒錄的話，在燒錄完系統後會出現 boot 標籤的槽及一個無法讀取槽，Windows 系統會提示要求格式化，**請不要格式化它**。這是因為 Linux 使用的 ext4 檔案系統 (File system) Windows 無法辨識，只要確認SD卡插入Raspberry Pi後可以運作就好了。

---

## Raspberry Pi 的連線

### 將Raspberry Pi連線至無線網路
剛燒入的系統在沒有鍵盤螢幕或實體網路線 (Zero由於沒有RJ45網路孔，故須配合有線網卡使用) 的情況下，若需要經由無線網路連線，可以建立一個檔名為`wpa_supplicant.conf`的檔案放在`boot`的資料夾。當 Raspberry Pi 上電開機時，系統會自動讀取這份檔案，**並覆蓋掉當前無線網路的設定**。系統在讀取完後便會刪除，所以下次讀取SD卡時會找不到這份檔案，因此建議大家備份一份到自己的電腦當中，若日後需要做修改會方便許多。`wpa_supplicant.conf`的範例檔案內容如下：
```
country=TW
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1

network={
    ssid="SSID_NAME1"
    psk="SSID_KEY1"
    key_mgmt=WPA-PSK
    scan_ssid=1
    priority=1 
}

network={
    ssid="SSID_NAME2"
    psk="SSID_KEY2"
    key_mgmt=WPA-PSK
    scan_ssid=1
    priority=2 
}
```
`SSID_NAME`即為無線網路名稱，`SSID_KEY`為無線網路的密碼，另外`priority`越高的話，會優先使用該無線網路，以上述內容為例，系統會優先連上`SSID_NAME2`，除非此網路沒有被搜尋到的話才會使用到`SSID_NAME1`這個無線網路。

### 開啟 SSH 服務
另外，過去較舊版本系統的SSH預設是關閉的需要手動開啟，不過現在使用 Raspberry Pi Imager 來燒錄的話是可以設定是否要開啟 SSH，不過為了保險起見，還是建議手動開啟。開啟的方式只要在`boot`資料夾內加入`ssh`的空檔案，系統在開機後會辨識該檔並開啟 SSH 服務。若用 Windows 系統的話，最簡單的方式是新增一個空白的 txt 檔，將檔名命名為`ssh`即可，**但需要注意**`.txt`**的副檔名都需要刪除**。這步驟只要在新燒錄的系統做一次即可，SSH 服務便會永久開啟，除非後續有額外關閉它。

### SSH 遠端連線
Windows 系統的 SSH 連線需要額外安裝軟體，可以使用 [PuTTY](https://www.putty.org/) 或 [MobaXterm](https://mobaxterm.mobatek.net/) 來進行連線。連線需要先知道 Raspberry Pi 的所在 IP 位址，這部分可以藉由路由器或是 IP Scanner 軟體來尋找，假設 IP 為`192.168.0.2`，那麼用命令列 (Command line) 來連線時可以用下列指令：
```bash=
ssh pi@192.168.0.2     # pi為預設使用者名稱
```
若是第一次連線到該裝置，在輸入後會出現 authenticity 相關的訊息，會出現`Are you sure you want to continue connecting (yes/no)?`的提示，這邊輸入`yes`按下 enter 就好。最後會要求密碼，預設為`raspberry`，輸入完後即可進入系統。

---

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
