import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt

# =========================
# TIÊU ĐỀ
# =========================

st.title("PHÁT HIỆN BẤT THƯỜNG TRONG DỮ LIỆU SAP ERP")
st.subheader("Isolation Forest + Streamlit")

# =========================
# ĐỌC DỮ LIỆU
# =========================

@st.cache_data
def load_data():
    df = pd.read_csv("sap_data.csv")
    return df

df = load_data()

# =========================
# HIỂN THỊ DỮ LIỆU
# =========================

st.write("## Dữ liệu gốc")
st.dataframe(df.head())

# =========================
# XỬ LÝ DỮ LIỆU
# =========================

processed_df = df.copy()

# Encode dữ liệu dạng text
encoder_doc = LabelEncoder()
encoder_user = LabelEncoder()

processed_df["Doc_Type"] = encoder_doc.fit_transform(processed_df["Doc_Type"])
processed_df["User_ID"] = encoder_user.fit_transform(processed_df["User_ID"])

# =========================
# CHỌN FEATURE
# =========================

features = [
    "Company_Code",
    "Account",
    "Amount",
    "Doc_Type",
    "Posting_Key",
    "User_ID"
]

X = processed_df[features]

# =========================
# HUẤN LUYỆN MODEL
# =========================

model = IsolationForest(
    contamination=0.02,
    random_state=42
)

processed_df["Anomaly"] = model.fit_predict(X)

# -1 = bất thường
#  1 = bình thường

processed_df["Result"] = processed_df["Anomaly"].map({
    1: "Normal",
    -1: "Anomaly"
})

# =========================
# THỐNG KÊ
# =========================

normal_count = (processed_df["Result"] == "Normal").sum()
anomaly_count = (processed_df["Result"] == "Anomaly").sum()

st.write("## Kết quả phát hiện")

col1, col2 = st.columns(2)

col1.metric("Giao dịch bình thường", normal_count)
col2.metric("Giao dịch bất thường", anomaly_count)

# =========================
# HIỂN THỊ BẤT THƯỜNG
# =========================

anomalies = processed_df[
    processed_df["Result"] == "Anomaly"
]

st.write("## Các giao dịch bất thường")
st.dataframe(anomalies)

# =========================
# BIỂU ĐỒ
# =========================

st.write("## Biểu đồ phân bố Amount")

fig, ax = plt.subplots(figsize=(10,5))

ax.scatter(
    processed_df.index,
    processed_df["Amount"],
    c=processed_df["Anomaly"]
)

ax.set_xlabel("Index")
ax.set_ylabel("Amount")
ax.set_title("Phát hiện bất thường bằng Isolation Forest")

st.pyplot(fig)

# =========================
# DOWNLOAD FILE
# =========================

csv = anomalies.to_csv(index=False).encode("utf-8")

st.download_button
    label="Tải dữ liệu bất thường",
    data=csv,
    file_name="anomaly_result.csv",
    mime="text/csv"
)