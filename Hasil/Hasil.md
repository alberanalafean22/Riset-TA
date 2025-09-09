

# Hasil Penelitian - SEGMENTASI BURNED AREA MENGGUNAKAN MODEL U-NET PADA CITRA LANDSAT 9 (STUDI KASUS: SUMATERA SELATAN)

## Area Kajian
<img src="https://github.com/user-attachments/assets/39aac020-3ba3-41be-8a6a-6f03d7318871" alt="Peta Daerah Penelitian" width="715"/>

## Diagram Alir Penelitian
<img src="https://github.com/user-attachments/assets/a7ea4eaf-6e9f-4fde-8626-7be1821dfd00" alt="flow" width="715"/>

### Tahapan Alur Penelitian
  * Data Citra Ladnsat 9 (diakses GEE di environment Google Colaboratory)
  * Data Preprocessing
    *  Koreksi Atmosferik (Dark Object Substraction)
    *  Cloud Masdking (QA Bands)
    *  Komposit Citra
  * Ekstraksi Fitur
    *  NDVI
    *  NBR
    *  dNBR
  * Band Stacking
  * Masking Citra
  * Split Data
    * Clipping Raster (Penyeragaman ukuran citra)
    * Image Patching (Memotong menjadi beberapa patch)
    * Image Filtering (Pemilihan citra layak)
    * Split Data
  * Model U-Net
  * Evaluasi Model  


## Konfigurasi Arsitektur U-Net digunakan
<img src="https://github.com/user-attachments/assets/a0d76507-e39e-41e0-b9f5-b8ea56f858f7" alt="Peta Daerah Penelitian" width="715"/>

## Konfigurasi Hyperparameter digunakan
|   Konfigurasi        |   Detail                                                        |
|----------------------|-----------------------------------------------------------------|
|   Optimizer          |   Adam                                                          |
|   Batch Size         |   4                                                             |
|   Input Size         |   512x512, 5 Channel (Multiband: NDVI,NBR,False Color Composite)|
|   Output Size        |   512x512, 1 Channel (prediction mask)                          |
|   Learning Rate      |   0.0001                                                        |
|   Epochs             |   200                                                           |
|   Callback           |   Early Stopping dan ReduceLROnPlateau                          |


## Spesifikasi Perangkat Keras

| Spesifikasi   | Detail                             |
|---------------|------------------------------------|
| Akselerator   | A100 GPU (Google Colaboratory Pro) |        
| CPU CORE      | 8 Core                             |        
| Tipe GPU      | NVIDIA A100-SXM4                   | 
| GPU Memory    | 40 GB                              | 
| RAM           | 83.5 GB(disediakan colab pro)      | 
| Disk Space    | 235.7 GB (disediakan colab pro)    | 


## Data Preprocessing dan Ekstraksi Fitur

### 1. Data Preprocessing
#### A. Koreksi Atmosferik
Proses ini dilakukan untuk menghilangkan perngaruh atmosfer pada nilai reflektansi, proses ini menggunakan metode Dark Object Substraction 

#### B. Cloud Masking
Proses ini dilakukan untuk menghilangkan pengaruh awan dan bayangan yang dapat mempengaruhi akurasi interpretasi spasial maupun spektral. Cloud masking menggunakan metode QA Bands pada Landsat yaitu QA Pixel.

#### C. Komposit Citra
Proses ini digunakan untuk menlihat interpretasi citra dengan False Color composite, dimana false color menggunakan 3 kombinasi band yaitu Band 7(SWIR2), Band 5(NIR) dan Band 4 (Red). False color ini yang nantinya merupakan bagian salah satu band pada citra multiband, yang mana citra multiband merupakan inputan citra

### 2. Ekstraksi Fitur
Ekstraksi fitur dilakukan untuk ekstrak fitur citra berupa indeks spektral, ekstraksi fitur digunakan yaitu NDVI, NBR, DNBR. Citra NDVI dan NBR digunakan dalam citra multiband, sedangkan dNBR nantinya digunakan dalam proses masking citra.


### 3. Masking Citra
Masking Citra dilakukan untuk memperoleh citra Mask burned area yang digunakan sebagai label/actual/ground truth pada segmentasi model, citra mask diperoleh dari thresholding nilai pada citra dNBR. Dengan kondisi, ketika nilai dNBR > 0.1 maka dipresentasikan ke piksel berwarna putih (1) dan ketika nilai dNBR < 0.1 maka direpresentasikan ke piksel hitam (0).


### 4. Band Stacking
Band Stacking dilakukan untuk mengabungkan informasi spektral dan indeks menjadi dalam satu represntasi citra multiband. Dalam hal ini, data akan menyimpan 5 band kedalam citra multiband, bandnya berupa : NDVI (1 band), NBR (1 band) dan False Color (3 band) menjadi 1 citra multiband yang menyimpan 5 band



### 5. Split Data
Dalam Proses split data, terdapat beberapa tahapan yang dilakukan sebelum split data: clipping raster, image patching, image filtering (filter citra yang layak digunakan) dan baru dilakukan split data. Rasio split data yang digunakan yaitu: Training 70%, Testing 15% dan Validation 15%


## Model U-Net
Dilakukan training model menggunakan data yang telah dilakukan split data. Model menggunakan hyperparamater diatas, dimana model mengalami penurunan secara konsisten

### Waktu Eksekusi dan Pemakaian Resource Sistem

|   Informasi         |   Detail                    |
|---------------------|-----------------------------|
|   Waktu Eksekusi    |   20 menit 21 detik         |
|   Pemakaian GPU     |   16.68 GB/ 40 GB           |
|   Pemakaian RAM     |   16.16 GB/ 83.48 GB        |
|   Pemakaian DISK    |   43.49 GB/ 235.68 GB       |


### Grafik Accuracy dan Loss Model U-Net
<img width="842" height="274" alt="image" src="https://github.com/user-attachments/assets/4f239ae6-862b-4f06-aee4-761395a08e69" />

## Evaluasi Model

Berikut Evaluasi model menggunakan data testing:
|   Evaluasi Model     |   Nilai    |
|----------------------|------------|
| Akurasi              | 0.93523    |
| IoU                  | 0.70858    |
| Dice Coefficient     | 0.82944    |
| Binary Cross Entropy | 0.18111    |



## Hasil Prediksi Model U-Net (per citra)

![Prediksi](prediksi-1.png)

## Hasil Penelitian secara lengkap dan detail bisa dicek pada link berikut atau kunjungi Perpustakaan ITERA
[.../link repo/....](https://repo.itera.ac.id/depan/submission/SB2509020010)

