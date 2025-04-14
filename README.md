# 🧠 Telco Customer Churn MLOps Pipeline with DVC, MLflow, Optuna

## 🚀 Giới thiệu dự án

Dự án này xây dựng một pipeline hoàn chỉnh cho bài toán dự đoán **Telco Customer Churn** từ dữ liệu Kaggle. Pipeline đáp ứng các tiêu chuẩn của **MLOps hiện đại** với:

- Data & Model Versioning (DVC)
- Experiment Tracking (MLflow)
- Hyperparameter Tuning (Optuna)
- Drift Detection
- CI/CD (có thể mở rộng với GitHub Actions)
- Triển khai mô hình với FastAPI (có thể nâng cấp thêm Prometheus + Grafana)

> 🎯 Mục tiêu: Dự đoán khách hàng có rời bỏ dịch vụ hay không, triển khai pipeline dễ mở rộng & tái sử dụng trong môi trường production.

---

## 🔧 Pipeline gồm những gì?

## 📁 Cấu trúc dự án

├── data/                          # Thư mục chứa dữ liệu
│   ├── raw/                       # Dữ liệu gốc tải từ Kaggle
│   └── processed/                 # Dữ liệu đã xử lý và sẵn sàng cho training
│
├── models/                        # Chứa mô hình đã huấn luyện và preprocessor
│   ├── model.pkl                  # Mô hình đã huấn luyện (Random Forest)
│   └── preprocessor.pkl           # Preprocessor cho dữ liệu (scaler, encoder, etc.)
│
├── scripts/                       # Thư mục chứa các script cho các bước trong pipeline
│   ├── data_load.py               # Xử lý và tải dữ liệu
│   ├── evaluate.py                # Đánh giá mô hình
│   ├── hyperparameter.py          # Tuning hyperparameter với Optuna
│   ├── logging.py                 # Log các thông số và kết quả vào MLflow
│   ├── train.py                   # Huấn luyện mô hình và log kết quả
│   └── drift_detect.py            # Phát hiện drift của dữ liệu (drift detection)
│
├── dvc.yaml                       # Định nghĩa các stages cho DVC pipelin
└── README.md                      # Hướng dẫn sử dụng và triển khai dự án


---

## 💡 Điểm nổi bật & sáng tạo

- ✅ **Tự động hoá toàn bộ quy trình training** thông qua `dvc.yaml`
- ✅ **Tracking toàn bộ thí nghiệm** bằng MLflow (params, metrics, artifact)
- ✅ **Tuning tự động** bằng Optuna + log lại vào MLflow
- ✅ **Xử lý drift dữ liệu** để kiểm tra nếu mô hình cần retrain
- ✅ Dễ dàng mở rộng với GitHub Actions, Prometheus, Grafana, FastAPI
- ✅ Thân thiện khi cộng tác nhóm (DVC hỗ trợ push/pull dữ liệu & model)

---

## ⚙️ Framework & Công nghệ sử dụng

| Công nghệ     | Mục đích |
|---------------|---------|
| **DVC**       | Pipeline orchestration & version control (dữ liệu & model) |
| **MLflow**    | Theo dõi thí nghiệm: hyperparams, metrics, artifact |
| **Optuna**    | Tối ưu hoá hyperparameters |
| **scikit-learn** | Huấn luyện model Random Forest |
| **FastAPI**   | (có thể triển khai) API dự đoán mô hình |
| **joblib**    | Lưu mô hình & pipeline |
| **Pandas/Numpy** | Xử lý dữ liệu |
| **Python ≥ 3.8** | Ngôn ngữ chính |

---

## 🛠️ Hướng dẫn cài đặt


✅ 1. Tải dataset từ Kaggle lưu trong raw

WA_Fn-UseC_-Telco-Customer-Churn.csv  #🔗 Link: https://www.kaggle.com/datasets/blastchar/telco-customer-churn

### 1. Clone repo & tạo môi trường ảo


git clone https://github.com/your-username/churn-prediction-mlops.git
cd churn-prediction-mlops

python -m venv venv
source venv/bin/activate   # hoặc venv\Scripts\activate trên Windows

pip install -r requirements.txt

▶️ Cách chạy pipeline

1. Tiền xử lý dữ liệu

python scripts/data_load.py

2. Huấn luyện mô hình

python scripts/train.py

3. Tuning hyperparameter

python scripts/hyperparameter.py

4. Đánh giá mô hình

python scripts/evaluate.py

5. Phát hiện drift dữ liệu

python scripts/drift_detect.py

6. Theo dõi MLflow

mlflow ui
# Truy cập tại: http://localhost:5000

🛠️ Sử dụng DVC
1. Khởi tạo DVC (nếu chưa)

dvc init
dvc remote add -d myremote gdrive://<your-id>   # hoặc s3, ssh, etc.

2. Theo dõi file

dvc add data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv
git add data/raw/WA_Fn-UseC_-Telco-Customer-Churn.csv.dvc .gitignore
git commit -m "Add raw data"

3. Tạo pipeline (nếu chưa có)

dvc repro

