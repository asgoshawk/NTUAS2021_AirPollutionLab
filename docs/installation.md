## 系統的燒錄與安裝
一般而言會建議新手參考官網的文件來安裝系統，在這邊非常推薦下載官網提供的 [Raspberry Pi Imager](https://www.raspberrypi.org/software/) 來安裝系統。另外也可以使用 [Etcher](https://www.balena.io/etcher/) 這套軟體來進行系統燒錄，但需要額外到官網下載作業系統的映像檔來燒錄。目前主流的系統叫 Raspberry Pi OS (舊版的叫 Raspbian)，跟 Ubuntu 同為 Debian 體系下的發行版，是由官方所維護的，不過目前只有32位元的版本，64位元的版本仍然在Beta測試階段。安裝的方式很簡單：
1. 插入新的SD卡至讀卡機並連接到電腦
2. 打開 Raspberry Pi Imager，選取想要安裝的系統(CHOOSE OS)及SD卡位置(CHOOSE STORAGE)
3. 按下 WRITE 後會自動下載所需的映像檔，接著等待燒錄完成
4. 將燒錄好系統的SD卡插入 Raspberry Pi 的SD卡插槽即可

![Raspberry Pi Imager的介面](https://i.imgur.com/d3bj2tj.png)

> 在這邊提醒，如果是用 Windows 系統來操作這部分燒錄的話，在燒錄完系統後會出現 boot 標籤的槽及一個無法讀取槽，Windows 系統會提示要求格式化，**請不要格式化它**。這是因為 Linux 使用的 ext4 檔案系統 (File system) Windows 無法辨識，只要確認SD卡插入Raspberry Pi後可以運作就好了。

除此之外，在 WRITE 之前可以進行初步設定 (這部分也可以在開機後進到系統再設定，後面篇幅會提到)，按下 Ctrl + Shift + X 會出現下列視窗，在這個視窗可以設定主機名稱 (hostname)、密碼、無線網路等設定。若沒開啟此視窗，在後續章節也會說明如何設定這些配置。

![](https://i.imgur.com/MRqDhbI.png)

