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
python yolo_train.py
```
#### 步驟3.將模型檔從.pt檔轉成.onnx檔
將模型檔從.pt檔轉成.onnx檔
```
python yolo_onnx.py
```
!!重要參數!!  
dynamic=False #表示輸出的ONNX模型會使用靜態輸入大小，若設為True可能會影響推論引擎的效能或相容性  
opset=11 #表示輸出的ONNX模型將使用第11版的操作定義

#### 步驟4.在本地端下載ubuntu虛擬機
```
ubuntu
```
#### 步驟5.在虛擬機安裝hailo環境
```
git clone https://github.com/BetaUtopia/Hailo8l.git
```
```
cd ~/Hailo8l && deactivate
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install python3.8 python3.8-venv python3.8-dev
```
```
python3.8 -m venv venv_hailo
source venv_hailo/bin/activate
sudo apt-get update
#下面兩個指令一開始會跑比較久
sudo apt-get install build-essential python3-dev graphviz graphviz-dev python3-tk
pip install pygraphviz
```
```
[Hailo Developer 區下載頁面](https://hailo.ai/developer-zone/software-downloads/)
#1.先從[Hailo Developer](https://hailo.ai/developer-zone/software-downloads/)
下載相關套件(上面有附上)
pip install whl/hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl
pip install whl/hailo_model_zoo-2.11.0-py3-none-any.whl
```
```
git clone https://github.com/hailo-ai/hailo_model_zoo.git
```
```




