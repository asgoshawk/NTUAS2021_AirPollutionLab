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

### PWM 簡介

PWM (Pulse Width Modulation) 中文簡稱脈寬調變，是一種利用數位訊號來模擬類比訊號的技術。由於 GPIO 只能輸出數位訊號，也就是只有高和低電位，對於 LED 來說只會有明滅兩種情況。然而 PWM 所做的事情就是輸出一連串的高低電位切換訊號，藉由改變工作週期 (Duty cycle) 模擬不同電壓來調整 LED 的亮度，同樣的方式也被應用在風扇或馬達轉速等等。

![](https://i.stack.imgur.com/g1C2r.png)

### Python 程式碼範例

簡易版本的範例如下所示，但需要注意的是，該程式碼是利用共陽極版本的 RGB LED，若使用共陰極版本則需要針對程式碼做修改。

```python 
# 引入模組
import RPi.GPIO as GPIO
import time

# RGB 對應的腳位編號(這裡用 BOARD 的腳位編號)
R_PIN = 8
G_PIN = 10
B_PIN = 12

# PWM 的頻率(Hz) 建議設定在 200 以上
PWM_FREQ = 300    

# GPIO mode 設定
GPIO.setmode(GPIO.BOARD)       # GPIO.BOARD 或 GPIO.BCM
GPIO.setup(R_PIN, GPIO.OUT)    # 設定三個腳位為輸出
GPIO.setup(G_PIN, GPIO.OUT)
GPIO.setup(B_PIN, GPIO.OUT)
GPIO.setwarnings(False)        # 關閉警告提示

# 設定 PWM 的頻率
r_pwm = GPIO.PWM(R_PIN, PWM_FREQ)
g_pwm = GPIO.PWM(G_PIN, PWM_FREQ)
b_pwm = GPIO.PWM(B_PIN, PWM_FREQ)

# 初始化 PWM 的 duty cycle 為 100%
r_pwm.start(100)
g_pwm.start(100)
b_pwm.start(100)
time.sleep(1)    # 停止1秒

# 建立函式方便後續藉由更改 duty cycle (%) 來調整 LED 亮度
def setColor(r, g, b):
    r_pwm.ChangeDutyCycle(100-int(r/255*100))
    g_pwm.ChangeDutyCycle(100-int(g/255*100))
    b_pwm.ChangeDutyCycle(100-int(b/255*100))

print("Show Red")
setColor(255, 0, 0)    # 設定 (r, g, b) = (255, 0, 0) 即紅色
time.sleep(1)

print("Exiting...")
r_pwm.stop()           # 關閉 PWM
g_pwm.stop()
b_pwm.stop()
GPIO.cleanup()         # 清空 GPIO 設定
```

另外，較進階的範例程式碼 (以類別 Class 來改寫，方便後續實作使用) 可以藉由下列指令取得，不過一樣需要注意的是，該程式碼是針對共陽極版本的 RGB LED 來撰寫的，視情況還需要做修改。

```bash
wget https://raw.githubusercontent.com/asgoshawk/NTUAS2021_AirPollutionLab/gh-pages/example_code/rgb_pwm.py
```
