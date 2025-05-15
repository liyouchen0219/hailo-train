# 使用Hailo 8L在Raspberry Pi 5上進行物件追蹤

## Hailo 8L介紹

Hailo-8L是由以色列AI晶片公司Hailo Technologies推出的入門級邊緣AI加速器，專為需要低功耗、高效率AI推論的應用場景設計。

主要規格與特點<br>
-AI 計算性能：最高達13 TOPS<br>
-功耗：典型功耗約 1.5W，實現業界領先的能效比(TOPS/W)<br>
-介面：PCIe Gen 3.0，2 通道<br>
-模組尺寸：M.2 Key B+M、M.2 Key A+E<br>
-支援平台：x86或ARM架構主機<br>

## 步驟介紹
1. 安裝 Visual Studio Code 並設定 Python 3.11 環境
2. 使用 YOLOv8n 訓練模型（產出 `.pt` 檔)
3. 將模型檔從 `.pt` 轉換成 `.onnx` 格式
4. 在本地端安裝 Ubuntu 虛擬機  
5. 在虛擬機中安裝 Hailo SDK 環境  
6. 使用 Hailo 工具鏈將模型從 `.onnx → .har → .hef` 格式轉換  
7. 在 Raspberry Pi 5 上安裝 Hailo 執行環境  
8. 在 Raspberry Pi 上進行即時物件追蹤推論

## 以下步驟於電腦本地端和虛擬機進行操作

#### 步驟1.安裝 Visual Studio Code 並設定 Python 3.11 環境
在vscode終端機輸入指令來建立python 3.11環境

```
# 建立名為hailo_train的虛擬環境
py -3.11 -m venv hailo_train
```
#### 步驟2.使用Yolov8n訓練模型
在3.11環境使用ultralytics套件來訓練Yolov8n模型
```
python yolo_train.py
```
#### 步驟3.將模型檔從.pt檔轉成.onnx檔
##### 將模型檔從.pt檔轉成.onnx檔
```
python yolo_onnx.py
```
##### !!重要參數!!  
##### dynamic=False #表示輸出的ONNX模型會使用靜態輸入大小，若設為True可能會影響推論引擎的效能或相容性  
##### opset=11 #表示輸出的ONNX模型將使用第11版的操作定義
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
#### (a)先從去下載相關套件(上面有附上)
![Hailo Training Screenshot](https://github.com/liyouchen0219/hailo-train/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202025-05-15%20190232.png?raw=true)
![Hailo Training Screenshot](https://github.com/liyouchen0219/hailo-train/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202025-05-15%20201234.png?raw=true)
[Hailo Developer 區下載頁面](https://hailo.ai/developer-zone/software-downloads/)，要使用學校信箱來註冊
#### (b)在虛擬機路的hailo8l資料夾建立一個名為whl的資料夾
#### (c)將下載的兩個套件放進資料夾
```
pip install whl/hailo_dataflow_compiler-3.27.0-py3-none-linux_x86_64.whl
pip install whl/hailo_model_zoo-2.11.0-py3-none-any.whl
```
```
git clone https://github.com/hailo-ai/hailo_model_zoo.git
```
#### 把圖片和標註轉成.tfrecord 格式，供Hailo模型訓練使用
```
python steps/2_install_dataset/create_custom_tfrecord.py val
python steps/2_install_dataset/create_custom_tfrecord.py train
```
#### 步驟6.使用hailo環境進行轉檔
#### 對模型進行解析.onnx→.har，程式碼第四和第五行須更改使用者名稱(一開始要等一下才會開始跑)
```
python steps/3_process/parse.py
```
#### 對模型進行最佳化best.har→best_quantized_model.har，程式碼第31、45和58須更改使用者名稱
```
python steps/3_process/optimize.py
```
#### 轉換模型best_quantized_model.har → best.hef
```
python steps/3_process/compile.py
```
### !!轉換成best.hef便完成轉檔!!

# 將模型透過Winscp或是隨身碟傳進Raspberry Pi 5
```
pip install /home/pi/hailo_platform-4.21.0-cp311-cp311-linux_aarch64.whl
```
```
pip install /home/pi/hailort-4.21.0-cp311-cp311-linux_aarch64.whl
```

## 以下步驟於Raspberry Pi 5進行操作
#### 在終端機輸入指令
```
cd hailo8l
git clone https://github.com/hailo-ai/hailo-rpi5-examples.git
pip install setproctitle
```
```
cd hailo-rpi5-examples
source setup_env.sh
cd ..
```
```
python basic_pipelines/detection.py -i rpi --hef best.hef --labels-json labels.json
```




