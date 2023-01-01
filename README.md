# Hướng dẫn cài đặt:
## Yêu cầu:
- Cài đặt môi trường ảo Anaconda để quản lí parkage Python - [Trang chủ Anaconda](https://docs.anaconda.com/anaconda/install/index.html) (*Được đề xuất)
- Cài đặt Graphviz để visualize cây quyết định - [Trang chủ graphviz](https://graphviz.org/download/) (*không yêu cầu)

## Cấu trúc thư mục:
- dataset/: Chứa tập dữ liệu cần train hoặc dữ liệu test
- model/: Chứa model đã train
- result/: Chứa kết quả sau khi train, chứa các file:
    - Báo cáo kết quả (classification_report)
    - Confusion_matrix
    - Visualize trained tree
    - Visualize tested tree
    - Visualize tree
- src/: Chứa source code
    - train.py: File huấn luyện model
    - predict.py: File đưa ra dự đoán
    - Water_Quality_Project.ipynb: File phân tích dữ liệu, phân tích mô hình (*dành cho developer)
# Hướng dẫn sử dụng:
### Tạo môi trường ảo Conda:
``` 
conda create -n water_quality python=3.7
conda activate water_quality
    
```
### Cài đặt parkage:
```
pip install -r requirements.txt
```
### Chạy huấn luyện:
```
python src/train.py
```
- File dataset mặc định là `water_potability.csv` được lưu trong folder `dataset/`. Có thể sử dụng tham số `--f file_name`
- Để visualize cây đã được huấn luyện, thêm tham số `--visualize`(* Yêu cầu cài đặt Graphviz)
```
python src/train.py --f dataset.csv --visualize
```

### Chạy dự đoán:
```
python src/train.py
```
- File dự đoán mẫu là predict_example.csv được lưu trong folder `dataset/`. Có thể sử dụng tham số `--f file_name`
```
python src/train.py --f predict.csv
```

## Xem kết quả trong folder `result/`:
- Báo cáo kết quả (classification_report)
- Confusion_matrix
- Visualize trained tree
- Visualize tree

## Model được lưu trong folder `model/`