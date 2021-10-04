## Screen

利用此指令可以在當前終端機額外開一個新的 shell 而不用另外開新的終端機再登入，且卸離並登出後依然會在背景繼續執行，適用在開啟伺服器或是下載大型檔案等等需要背景執行的情境。Raspberry Pi OS 是沒有預載此工具的，因此需要透過下列指令下載：
```
sudo apt install screen
```

要開啟新的 shell 可以直接輸入 `screen` 會出現下列畫面，直接按 enter 或 space 就好：

![](https://i.imgur.com/5WxVsLg.png)

接下來會進到 screen 的環境，基本上跟平常使用的 shell 一樣，使用者可以在此 shell 執行任何指令。若要保留當前工作階段在背景的話，可以按下 Ctrl + A 再按 D 就可以卸離 (Detach) 回到最一開始的 shell。如果要進到 screen 建立的 shell 可以輸入：

```bash
screen -r
```

要直接關閉此 shell 可以輸入 `exit` (和登出 shell 相同)，但此時就無法用 `screen -r` 來回到該 shell 了。其他 screen 的指令可以參考 [使用 Screen 指令操控 UNIX/Linux 終端機的教學與範例](https://blog.gtwang.org/linux/screen-command-examples-to-manage-linux-terminals/) 這網站，會有較詳細的敘述。
