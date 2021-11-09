## Google Action 設定

在本篇教學中，我們將會在 Google Cloud Platform 開啟一個專案，接著利用 Google Action 及 DiagFlow 來設定語意及對應的值，接著串接前面設定的 Webhook，設定完後就可以透過 Google Assistant 來控制我們的 Raspberry Pi 了。

### 建立 Google 專案

1. 首先進到 [Google Cloud Platform](https://console.cloud.google.com/) 的頁面，若沒有創過專案的，在左上角 Google Cloud Platform 的右邊是不會有專案名稱如 control-mypi。

    ![](https://i.imgur.com/v85JTZ4.png)

2. 但不論如何都我們可以按下那個位置，他會跳出下列的視窗，接著按下 **新增專案** 來建立新的專案。

    ![](https://i.imgur.com/8YTYDAw.png)

3. 輸入專案名稱後就可以直接按下建立。

    ![](https://i.imgur.com/QIHk4iW.png)

### 設定 Google Action

4. 建立好 Google Cloud Platform 的專案後，就可以到 [Google Action Console](https://console.actions.google.com) 來導入剛剛的專案，進到 Console 頁面後按下 **New project**。

    ![](https://i.imgur.com/H8vZyRc.png)
    
 
5. 接著他會跳出下列視窗，然後選取剛剛建立的專案名稱，最後按下 **Import project**。這邊要注意如果顯示的是 **Create project** 代表沒有選到剛才建立的專案。

    ![](https://i.imgur.com/37d2f3g.png)

6. 接著會看到以下頁面，選擇 **Custom**後按下右上角的 **Next**。

    ![](https://i.imgur.com/Cgyz8ZB.png)

7. 進到下一個頁面後，因為我們要用 DiagFlow 來設定語意，所以要拉到最下面選取，這部分可能會需要較久的時間。

    ![](https://i.imgur.com/c4jK0vV.png)

8. 之後就會來到 Console 頁面，先按下箭頭指的方向來設定這個 App 的名稱（這是要對 Google Assistant 講的）。

    ![](https://i.imgur.com/LtinxPZ.png)

9. My Pi version 3 就是這次設定的名稱，設定好後按右上角的 Save。

    ![](https://i.imgur.com/bVVtQlf.png)

10. 存好後按左上角的按鈕，選取 **Actions**。
    
    ![](https://i.imgur.com/WhcX1n5.png)

11. 按下 **Add Action**，以及 **BUILD**。

    ![](https://i.imgur.com/pu0fb5a.png)
    ![](https://i.imgur.com/Jyj8GWW.png)

### 設定 DiagFlow

12. 在上述步驟會轉跳到 DiagFlow 的頁面，可以直接按下 **CREATE**。

    ![](https://i.imgur.com/gGkVmiV.png)

13. 接下來的 Intents 和 Entities 設定上有些複雜，有興趣可以去找找 DiagFlow 相關教學文章，不過目前已經有一份設定好來控制 RGB 的設定檔，可以到[這裡下載](https://github.com/asgoshawk/NTUAS2021_AirPollutionLab/blob/gh-pages/example_code/My-Pi.zip)。下載完後，點選左上的齒輪。

    ![](https://i.imgur.com/kOEpfUL.png)

14. 點選 Export and Import 頁面來匯入剛剛下載的檔案。

    ![](https://i.imgur.com/yMkAFzx.png)

15. 匯入完後，在左邊點選 Intents 和 Entities 理論上會多了以下這些：

    ![](https://i.imgur.com/tc6rv4V.png)
    ![](https://i.imgur.com/bp77RdD.png)

16. 確認好後到 Fulfillment 設定 Webhook，這邊記得 URL 設定成在 Ngrok 得到的 https 開頭的網址，要記得網址的 /webhook 需要留著，設定好後拉到底下按下 SAVE 存檔。

    ![](https://i.imgur.com/YVVmzEA.png)

17. 最後在 Integrations 這個頁面點選箭頭指的 integration。

    ![](https://i.imgur.com/HEYrlaB.png)

18. 接著點選 TEST，DiagFlow 就會把前面所設定的東西導入 Google Action 了。

    ![](https://i.imgur.com/TzLk4CE.png)

19. 回到 Console 頁面就可以在這邊測試了，一開始都必須要講 Talk to [你的App名稱]，來讓 Google 知道你要開啟甚麼 App，接著就可以用語音來測試是否可以控制 Raspberry Pi 的 RGB LED了。

    ![](https://i.imgur.com/aUd2iuS.png)