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
