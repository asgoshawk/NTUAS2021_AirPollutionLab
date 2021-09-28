## GPIO 操作範例 (RGB LED)

### Python 套件安裝
首先需要下載 Python 3 所需要的套件：
```bash
sudo apt update
sudo apt install python3-pip
sudo pip3 install RPi.GPIO
```

### GPIO 的模式
若使用 RPi.GPIO 的套件 需要注意 GPIO 模式有分為 **BCM** 及 **BOARD** 模式，使用上需要對應到不同模式的腳位編碼，若不確定自己的腳位編碼，可以看上一頁的腳位定義對照圖，除此之外也可以在命令列輸入：

```bash
pinout
```
理論上會根據自己使用板子的型號顯示相關資訊，若使用的是 Raspberry Pi Zero W 就會顯示如下圖：

![](https://i.imgur.com/mjbGHmk.png)

括號內的數字就是 BOARD 的編號，而綠色 GPIO 顯示的數字就是 BCM 所代表的編號，設定時還需要注意。 

### RGB LED 的連接

本次實作將用 RGB LED 來連接 GPIO 並利用程式碼來控制所顯示的顏色，接法大致如下所示：

![](https://i.imgur.com/rOpZGvA.png)

其中 RGB LED 最長的腳即為共(陰/陽)極，若使用的是共陽極 (Common anode) 的版本便該腳便需要接到 3.3V 腳位，反之共陰極 (Common cathode) 的版本就需要接到 GND，而其他三根則需要串聯相同歐姆電阻後連接到 GPIO上。三根腳位由左至右分別代表 Red、Green、Blue 所以要確定這三根所對應到的 GPIO 腳位編號才能控制。 
  
### Python 程式碼範例
範例 Python 程式碼可以藉由下列指令取得：

```bash
wget https://raw.githubusercontent.com/asgoshawk/NTUAS2021_AirPollutionLab/gh-pages/example_code/rgb_pwm.py
```

但需要注意的是，該程式碼是利用共陽極版本的 RGB LED，若使用共陰極版本則需要針對程式碼做修改。

