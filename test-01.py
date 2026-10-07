from ultralytics import YOLO
model = YOLO("best.pt")
model.predict(
    source=r"您文件的绝对路径",
    save=True,
    show=False,

)
