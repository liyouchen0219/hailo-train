from ultralytics import YOLO

# 載入 YOLOv8 模型
model = YOLO(r"C:\egg_rgb2\runs\egg_v8_v42\weights\best.pt")  # 替換為您的 .pt 文件路徑

# 將模型導出為 ONNX
model.export(format="onnx", dynamic=False, imgsz=640, opset=11)  # dynamic=True 可選，用於動態形狀
