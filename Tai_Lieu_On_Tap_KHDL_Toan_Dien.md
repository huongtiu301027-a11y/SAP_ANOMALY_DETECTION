# TÀI LIỆU ÔN TẬP TOÀN DIỆN - KHOA HỌC DỮ LIỆU & AI
**Người thực hiện:** Thiều Thị Yến Nhi  
**Môn học:** Khoa học Dữ liệu & AI  

Tài liệu này tổng hợp toàn bộ nội dung lý thuyết, công thức toán học từng bước và hướng dẫn thực hành Python cho 10 hạng mục ôn tập cốt lõi của môn học.

---

## PHẦN 1: CƠ BẢN - ĐẶC TRƯNG VÀ Ý NGHĨA HÌNH HỌC CỦA MA TRẬN

Trong Khoa học Dữ liệu, ma trận đóng vai trò là một **phép biến đổi tuyến tính** biến đổi cấu trúc hình học của không gian vector đầu vào thành không gian đầu ra ($y = Ax$).

### 1. Phân loại và ý nghĩa hình học
1. **Ma trận Đơn vị ($I$):**
   * *Định nghĩa:* Ma trận vuông có phần tử đường chéo chính bằng 1, các phần tử khác bằng 0.
   * *Ý nghĩa hình học:* Phép biến đổi đồng nhất, giữ nguyên hoàn toàn tọa độ, hướng và độ dài của mọi vector trong không gian: $Ix = x$.
2. **Ma trận Đường chéo ($D$):**
   * *Định nghĩa:* Các phần tử ngoài đường chéo chính đều bằng 0.
   * *Ý nghĩa hình học:* Thực hiện phép co hoặc giãn không gian độc lập dọc theo các trục tọa độ chính. Ví dụ, phần tử đường chéo chính là $[2, 0.5]$ sẽ nhân đôi tọa độ trục hoành và thu hẹp một nửa tọa độ trục tung.
3. **Ma trận Trực giao ($R$):**
   * *Định nghĩa:* Có nghịch đảo bằng chuyển vị: $R^T R = I \implies R^{-1} = R^T$.
   * *Ý nghĩa hình học:* Thực hiện phép xoay (Rotation) hoặc phép đối xứng (Reflection) không gian. Đặc biệt, nó bảo toàn khoảng cách/độ lớn vector ($||Rx|| = ||x||$) và bảo toàn góc giữa các trục.
4. **Ma trận Đối xứng ($S$):**
   * *Định nghĩa:* Bằng chuyển vị chính nó: $S = S^T$.
   * *Ý nghĩa hình học:* Có các vectơ riêng đôi một vuông góc tạo thành hệ cơ sở trực giao mới. Nó biểu thị sự co giãn không gian theo hướng của các vectơ riêng với hệ số co giãn bằng các trị riêng tương ứng.

Dưới đây là hình ảnh trực quan hóa các phép biến đổi ma trận trên đường tròn đơn vị:

![Biến đổi ma trận](matrix_transformations.png)

---

## PHẦN 2: TIỀN XỬ LÝ DỮ LIỆU

### 1. Phát hiện ngoại lai (Outliers)
* **Quy tắc Boxplot (Hàng rào Tukey):**
  * Tứ phân vị: $Q_1$ (25%), $Q_2$ (50% - trung vị), $Q_3$ (75%).
  * Độ trải giữa: $IQR = Q_3 - Q_1$.
  * Ranh giới bình thường: $[Q_1 - 1.5 	imes IQR, \quad Q_3 + 1.5 	imes IQR]$. Giá trị ngoài ranh giới là ngoại lai.
* **Quy tắc $2s$ và $3s$ (Sigma):**
  * Sử dụng trung bình $ar{x}$ và độ lệch chuẩn $s$ (hoặc $\sigma$).
  * Khoảng $2s$: $(ar{x} - 2s, \quad ar{x} + 2s)$
  * Khoảng $3s$: $(ar{x} - 3s, \quad ar{x} + 3s)$
  * Giá trị nằm ngoài khoảng ranh giới là điểm bất thường.

### 2. Các phương pháp chuẩn hóa dữ liệu
* **Trừ trung bình (Centered):** Dịch chuyển dữ liệu để trọng tâm nằm tại gốc tọa độ.
  $$x'_{centered} = x - ar{x}$$
* **Chuẩn hóa Z-score (Standardization):** Đưa dữ liệu về dạng trung bình bằng 0 và phương sai bằng 1.
  $$z = rac{x - ar{x}}{std}$$
  * *Chú ý:* Cần ghi rõ trong bài thi là sử dụng độ lệch chuẩn mẫu $s$ (chia $N-1$) hay độ lệch chuẩn tổng thể $\sigma$ (chia $N$). Nhiều học sinh thường bị trừ điểm do tính toán nhầm lẫn giữa hai loại này.
* **Chuẩn hóa Min-Max:** Đưa dữ liệu về đoạn $[0, 1]$.
  $$x'_{minmax} = rac{x - x_{min}}{x_{max} - x_{min}}$$

Dưới đây là hình ảnh so sánh biến động dữ liệu khi áp dụng các phương pháp chuẩn hóa khác nhau:

![So sánh chuẩn hóa](normalization_comparison.png)

### 3. Quy trình tính toán thuật toán PCA bằng tay
Để giảm chiều dữ liệu từ $2D$ về $1D$ bằng PCA:
1. **Centered:** Trừ trung bình dữ liệu để có $X_{centered}$.
2. **Hiệp biến:** Tính ma trận hiệp biến $C = rac{1}{N-1} X_{centered}^T X_{centered}$.
3. **Trị riêng:** Giải phương trình đặc trưng $\det(C - \lambda I) = 0$ để tìm $\lambda_1 \ge \lambda_2 \ge ... \ge 0$.
4. **Vectơ riêng:** Giải $(C - \lambda_1 I)v_1 = 0$ để tìm vectơ riêng tương ứng với trị riêng lớn nhất. *Bắt buộc phải chuẩn hóa về độ dài bằng 1:* $||v_1|| = 1$.
5. **Chiếu:** Tính tọa độ 1D mới bằng phép nhân tích vô hướng: $z_i = X_{centered, i} \cdot v_1$.

---

## PHẦN 3: HỌC MÁY - PHƯƠNG PHÁP BÌNH PHƯƠNG TỐI THIỂU (OLS)

Phương pháp Bình phương tối thiểu (Ordinary Least Squares - OLS) tìm đường thẳng khớp dữ liệu nhất bằng cách giảm thiểu tổng bình phương phần dư (sai số).

### 1. Công thức giải tích (Hồi quy đơn biến)
Mô hình dạng: $y = w_1 x + w_0$.
* Hệ số góc:
  $$w_1 = rac{Cov(x, y)}{Var(x)} = rac{\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})}{\sum_{i=1}^N (x_i - \bar{x})^2}$$
* Hệ số chặn:
  $$w_0 = \bar{y} - w_1 \bar{x}$$

### 2. Công thức ma trận (Multiple Linear Regression)
Công thức tổng quát cho mọi bài toán OLS đa biến:
$$w = (X^T X)^{-1} X^T y$$

#### **Bài toán mẫu giải chi tiết (Case Study):**
Tìm phương trình hồi quy đi qua 3 điểm: $(1, 2)$, $(2, 5)$, $(3, 7)$.

* **Bước 1: Thiết lập ma trận**
  Bổ sung cột bias (toàn số 1) vào ma trận thiết kế $X$:
  $$X = egin{pmatrix} 1 & 1 \ 2 & 1 \ 3 & 1 \end{pmatrix}, \quad y = egin{pmatrix} 2 \ 5 \ 7 \end{pmatrix}$$
* **Bước 2: Tính ma trận $X^T X$**
  $$X^T X = egin{pmatrix} 1 & 2 & 3 \ 1 & 1 & 1 \end{pmatrix} egin{pmatrix} 1 & 1 \ 2 & 1 \ 3 & 1 \end{pmatrix} = egin{pmatrix} 14 & 6 \ 6 & 3 \end{pmatrix}$$
* **Bước 3: Tính ma trận nghịch đảo $(X^T X)^{-1}$**
  $$\det(X^T X) = 14 	imes 3 - 6^2 = 6$$
  $$(X^T X)^{-1} = rac{1}{6} egin{pmatrix} 3 & -6 \ -6 & 14 \end{pmatrix}$$
* **Bước 4: Tính tích ma trận $X^T y$**
  $$X^T y = egin{pmatrix} 1 & 2 & 3 \ 1 & 1 & 1 \end{pmatrix} egin{pmatrix} 2 \ 5 \ 7 \end{pmatrix} = egin{pmatrix} 33 \ 14 \end{pmatrix}$$
* **Bước 5: Giải trọng số tối ưu $w$**
  $$w = rac{1}{6} egin{pmatrix} 3 & -6 \ -6 & 14 \end{pmatrix} egin{pmatrix} 33 \ 14 \end{pmatrix} = rac{1}{6} egin{pmatrix} 99 - 84 \ -198 + 196 \end{pmatrix} = rac{1}{6} egin{pmatrix} 15 \ -2 \end{pmatrix} = egin{pmatrix} 2.5 \ -0.333 \end{pmatrix}$$

Vậy phương trình hồi quy tuyến tính thu được là: **$y = 2.5x - 0.333$**.

Dưới đây là hình vẽ đường hồi quy và phần dư sai số (residuals) tương ứng:

![Đường hồi quy](regression_residuals.png)

---

## PHẦN 4: CÁC ĐỘ ĐO ĐÁNH GIÁ MÔ HÌNH

### 1. Đánh giá mô hình Hồi quy (Regression Metrics)
Sử dụng dữ liệu của bài toán mẫu ở phần trên làm ví dụ tính toán thực tế:
* Giá trị thực tế: $y = [2, \quad 5, \quad 7]$
* Giá trị dự báo: $\hat{y} = [2.167, \quad 4.667, \quad 7.167]$
* Sai số phần dư: $e = [-0.167, \quad 0.333, \quad -0.167]$

1. **Mean Squared Error (MSE):**
   $$MSE = rac{1}{N} \sum_{i=1}^N (y_i - \hat{y}_i)^2 = rac{(-0.167)^2 + (0.333)^2 + (-0.167)^2}{3} pprox 0.0556$$
2. **Root Mean Squared Error (RMSE):**
   $$RMSE = \sqrt{MSE} = \sqrt{0.0556} pprox 0.2357$$
3. **Mean Absolute Error (MAE):**
   $$MAE = rac{1}{N} \sum_{i=1}^N |y_i - \hat{y}_i| = rac{|-0.167| + |0.333| + |-0.167|}{3} pprox 0.2222$$
4. **Hệ số xác định ($R^2$):**
   Với trung bình thực tế $ar{y} = 4.667$, ta có $SS_{res} = 0.1667$ và $SS_{tot} = 12.667$:
   $$R^2 = 1 - rac{SS_{res}}{SS_{tot}} = 1 - rac{0.1667}{12.667} pprox 0.9868$$

### 2. Đánh giá mô hình Phân loại (Classification Metrics)
Được xác định dựa trên ma trận nhầm lẫn biểu diễn số lượng mẫu dự đoán chính xác và sai lệch.

![Ma trận nhầm lẫn](confusion_matrix_heatmap.png)

*Ví dụ tính toán:* Cho tập gồm 10 mẫu dữ liệu thực tế và dự báo:
* Thực tế: `[1, 1, 1, 0, 0, 0, 1, 0, 1, 0]`
* Dự đoán: `[1, 1, 0, 0, 0, 0, 1, 1, 0, 0]`

Phân loại các chỉ số từ dữ liệu trên:
* **True Positive (TP) = 3** (mẫu chỉ số 0, 1, 6 là 1 và dự đoán đúng là 1)
* **True Negative (TN) = 4** (mẫu chỉ số 3, 4, 5, 9 là 0 và dự đoán đúng là 0)
* **False Positive (FP) = 1** (mẫu chỉ số 7 là 0 nhưng dự đoán sai thành 1)
* **False Negative (FN) = 2** (mẫu chỉ số 2, 8 là 1 nhưng dự đoán sai thành 0)

Tính toán các chỉ số:
1. **Accuracy (Độ chính xác tổng quát):**
   $$Accuracy = rac{TP + TN}{TP + TN + FP + FN} = rac{3 + 4}{10} = 70\%$$
2. **Precision (Độ chính xác lớp dương):**
   $$Precision = rac{TP}{TP + FP} = rac{3}{3 + 1} = 75\%$$
3. **Recall / Sensitivity (Độ nhạy):**
   $$Recall = rac{TP}{TP + FN} = rac{3}{3 + 2} = 60\%$$
4. **F1-Score (Trung bình điều hòa giữa Precision và Recall):**
   $$F1 = 2 	imes rac{Precision 	imes Recall}{Precision + Recall} = 2 	imes rac{0.75 	imes 0.6}{0.75 + 0.6} pprox 66.7\%$$
