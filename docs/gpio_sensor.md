## 藉由 GPIO 連接 Sensor

Raspberry Pi 和 sensor (或其他設備)的溝通主要藉由 GPIO (general-purpose input/output) 來達成，本章節會介紹如何經由GPIO來和不同傳輸協定的設備連線。

### GPIO 腳位定義
目前市售的 Raspberry Pi 的 GPIO 大部分都有40個腳位(pin)，所若是使用 Raspberry Pi 3B、3B+、4B 等以類型的版本，其腳位的對應如下圖所示：

![](https://i.imgur.com/XEjuh1g.png)

另外若是 Zero (W) 的版本，雖然板子較小，但其對應的腳位基本上和上述版本相同，為了方便對應，附在下方參考：
![](https://i.imgur.com/ctuCllk.png)

### 傳輸協定
基本上 Sensor 透過三種不同的傳輸協定來和 Raspberry Pi 來溝通，分別是 I<sup>2</sup>C 、 SPI 及 UART ，這三種有不同的接線方式，所以在連接 Sensor 時必須確認 Sensor所使用的協定為何，才可以順利藉由 GPIO 來進行溝通。

![](https://i.imgur.com/IpAUbWM.png)

#### I<sup>2</sup>C (Inter-Integrated Circuit)

#### SPI (Serial Peripheral Interface)


#### UART ( Universal Asynchronous Receiver / Transmitter)


### 程式碼控制 (以 Python 為例)




---
首先需要下載 Python 3 所需要的套件：
```bash
sudo apt update
sudo apt install python3-pip python3-spidev
```
