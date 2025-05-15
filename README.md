# 使用Hailo 8L在Raspberry Pi 5上進行物件追蹤

## Hailo 8L介紹

Hailo-8L是由以色列AI晶片公司Hailo Technologies推出的入門級邊緣AI加速器，專為需要低功耗、高效率AI推論的應用場景設計。

主要規格與特點<br>
-AI 計算性能：最高達13 TOPS<br>
-功耗：典型功耗約 1.5W，實現業界領先的能效比(TOPS/W)<br>
-介面：PCIe Gen 3.0，2 通道<br>
-模組尺寸：M.2 Key B+M、M.2 Key A+E<br>
-支援平台：x86或ARM架構主機<br>

## 使用步驟
1. 安裝 Visual Studio Code 並設定 Python 3.11 環境
2. 使用 YOLOv8n 訓練模型（產出 `.pt` 檔)
3. 將模型檔從 `.pt` 轉換成 `.onnx` 格式
4. 在本地端安裝 Ubuntu 虛擬機  
5. 在虛擬機中安裝 Hailo SDK 環境  
6. 使用 Hailo 工具鏈將模型從 `.onnx → .har → .hef` 格式轉換  
7. 在 Raspberry Pi 5 上安裝 Hailo 執行環境  
8. 在 Raspberry Pi 上進行即時物件追蹤推論

#### 步驟1.安裝 Visual Studio Code 並設定 Python 3.11 環境
在vscode終端機輸入指令來建立python 3.11環境

```bash
# 建立名為hailo_train的虛擬環境
py -3.11 -m venv hailo_train
```
#### 步驟2.使用Yolov8n訓練模型
在3.11環境使用ultralytics套件來訓練Yolov8n模型
```
if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")

    result = model.train(
        data = r"C:\egg_rgb2\data.yaml", #訓練集的位置
        epochs = 3500, #疊帶次數
        patience = 500, #信心值，減少patience以便更早停止
        batch = 8, #每次訓練的數量
        project = r"C:\egg_rgb2\runs" , #結果資料夾名稱
        name = 'egg_v8_v4' , #模型資料夾名稱
    )
```

