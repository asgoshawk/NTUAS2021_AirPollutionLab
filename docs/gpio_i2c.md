## GPIO 操作範例 (I<sup>2</sup>C)

### 基本設定

在連接到 I<sup>2</sup>C 裝置前，先下載相關的套件及工具：

```bash
# 更新套件庫資訊及套件
sudo apt update && sudo apt upgrade -y

# 安裝所需的套件
sudo apt install build-essential python3-dev python3-smbus i2c-tools
```

安裝完上述套瑱後，輸入 `sudo raspi-config` 後進到 Interface Options 後移到 I<sup>2</sup>C 的選項並啟用它：

![](https://i.imgur.com/jdfieCJ.png)

接下來可以將 I<sup>2</sup>C 的裝置連上 Raspberry Pi，其中裝置的 SDA 和 SCL 要接到對應的腳位 (即 GPIO2 和 GPIO3 的位置)

![](https://i.imgur.com/ctuCllk.png)

接好後可以輸入以下指令，沒有問題的話應該可以看到裝置的所在位址 (如附圖)：

```bash
sudo i2cdetect -y 1
```

![](https://i.imgur.com/NUl0rDb.png)

其中 48 指的是16進位的 0x48，代表有裝置被偵測到且位址為 0x48，其他顯示 \-\- 則代表該位址為空。一般而言每個裝置的位址並不相同，若不幸遇到位址相同造成的衝突，依照裝置的不同有可能會要更改電路板的電阻或是加上跳線等方式來更改位址，這部分需要查詢裝置的資料表。

### 類比數位轉換器 ADC (ADS1115)

類比數位轉換器 (Analog-to-digital converter, ADC) 用於將類比訊號 (連續) 轉換成數位訊號 (離散)，通常用在儀器量測等訊號輸入上；反之，將數位轉換成類比訊號則叫 DAC，通常用在訊號輸出上，如喇叭等等。由於 Raspberry Pi 的 GPIO 不像 Arduino 或其他 MCU 本身就有 ADC 或 DAC 的腳位，因此會需要額外連接 ADC 設備來做訊號轉換。

![](https://i.imgur.com/R5S7GmZ.png)

目前實驗室的空氣盒子使用的氣體感測器本身就是輸出類比訊號，因此會透過 ADS1115 這顆四通道的 IC 來把感測器的訊號作轉換並藉由 I<sup>2</sup>C 來傳遞初始數值給 Raspberry Pi。如上圖所示，A0 - A3 腳位會和感測器的電極連接，其餘腳位 SDA、SCL、GND 及 VDD 則接到 Raspberry Pi 上。要使用 ADC 還需要額外的函式庫 (Library)，在此使用 Adafruit 提供的函式庫：

```bash
sudo pip3 install adafruit-ads1x15

# 範例 Python 檔
wget https://raw.githubusercontent.com/adafruit/Adafruit_Python_ADS1x15/master/examples/simpletest.py
```

下載後可以用 `python3 simpletest.py` 來執行看看 ADC 是否可以運作，理論上會出現以下畫面。由於執行時類比端並未接上任何的裝置，因此數值並沒有任何意義。

![](https://i.imgur.com/pCsht5F.png)

若要看到明顯差異，可以嘗試將 Raspberry Pi 的 GND 腳位接到任一個類比端 (如 A3)，就會看到接近 0 的數值。

![](https://i.imgur.com/q6T1kHR.png)

其他 ADS1115 的說明可以參考 [Adafruit 的文章](https://learn.adafruit.com/raspberry-pi-analog-to-digital-converters/ads1015-slash-ads1115)。
