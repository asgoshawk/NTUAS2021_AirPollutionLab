## GPIO 與傳輸協定

Raspberry Pi 和 sensor (或其他設備)的溝通主要藉由 GPIO (general-purpose input/output) 來達成，本章節會介紹如何經由GPIO來和不同傳輸協定的設備連線。

### GPIO 腳位定義
目前市售的 Raspberry Pi 的 GPIO 大部分都有40個腳位(pin)，所若是使用 Raspberry Pi 3B、3B+、4B 等以類型的版本，其腳位的對應如下圖所示：

![](https://i.imgur.com/XEjuh1g.png)

另外若是 Zero (W) 的版本，雖然板子較小，但其對應的腳位基本上和上述版本相同，為了方便對應，附在下方參考：
![](https://i.imgur.com/ctuCllk.png)

### 傳輸協定
基本上 Sensor 透過三種不同的傳輸協定來和 Raspberry Pi 來溝通，分別是 I<sup>2</sup>C 、 SPI 及 UART ，這三種有不同的接線方式，所以在連接 Sensor 時必須確認 Sensor所使用的協定為何，才可以順利藉由 GPIO 來進行溝通。

![](https://i.imgur.com/IpAUbWM.png)

這三種傳輸協定都可以進行資料的傳輸，但傳輸的運作方式不同，以下簡述這三者不同的地方，並以 Master (主設備) 和 Slave (從設備) 分別來代表 Raspberry Pi 及 Sensor：

#### I<sup>2</sup>C (Inter-Integrated Circuit)
兩設備用資料線 (Serial Data Line, SDA) 及時脈線 (Serial Clock Line, SCL) 來和連線，接線時兩設備的 SDA 互接且 SCL 互接。此協定可以雙向由 Master 傳至 Slave 或是 Slave 傳至 Master，但由於資料線只有一條，因此資料傳輸時在同一時間只能有一個方向的傳輸，稱為半雙工 (Half duplex)。

#### SPI (Serial Peripheral Interface)
兩設備基本上由四條線來連線，分別為 MOSI (Master Out Slave In)、MISO (Master In Slave Out)、SCLK (Serial Clock 也有縮寫為 SCK) 及 SS (Slave Select 或稱 Chip Select, CS)，另外 MOSI 及 MISO 這兩組也有不分主從的名稱：SDO (Serial Data Out) 及 SDI (Serial Data In)。名稱種類稍微複雜，**不過接線上一樣都是相同名稱連接在一起即可**。SPI 由於有兩條資料傳輸線，因此能做到 I<sup>2</sup>C 無法做到的雙向傳輸也就是全雙工 (Full duplex)。

#### UART ( Universal Asynchronous Receiver / Transmitter)
兩設備由兩條線連接 (第三條 GND 不一定需要)，且只能用在一對一的連接，無法像上述兩種協定可進行串接。此部分須注意接線上兩設備的 **Tx (Transmitter) 和 Rx (Receiver) 須交叉對接**，而 GND (Ground) 相連即可。不同於上述兩種協定都有時脈線，因此 UART 的資料傳輸為非同步 (Asynchronous)。較常聽到的 RS232、RS485 等 RS 系列標準都是屬於 UART 的協定。