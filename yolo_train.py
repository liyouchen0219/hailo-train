if __name__ == "__main__":
    import multiprocessing
    multiprocessing.freeze_support()
    import os  
    os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
    from ultralytics import YOLO

    model = YOLO("yolov8n.pt")
    #模型位置

    result = model.train(
        data=r"C:\egg_rgb2\data.yaml", #訓練集的位置
        #imgsz=320, #影像大小
        epochs=3500, #疊帶次數
        patience=500, #信心值，減少patience以便更早停止
        batch=8, #每次訓練的數量
        project=r"C:\egg_rgb2\runs", #結果資料夾名稱
        name='egg_v8_v4', #模型資料夾名稱


    )# -*- coding: utf-8 -*-

"""
        augment=True,
        degrees=10.0,
        scale=0.5,        # 縮放
        shear=2.0,        # 剪切
        translate=0.1,    # 平移
        flipud=0.0,       # 上下翻轉
        fliplr=0.5,       # 左右翻轉
        mosaic=1.0,       # 使用 Mosaic
        mixup=0.1  
"""