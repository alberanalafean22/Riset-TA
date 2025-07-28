

# Hasil Penelitian - SEGMENTASI BURNED AREA MENGGUNAKAN MODEL U-NET PADA CITRA LANDSAT 9 (STUDI KASUS: SUMATERA SELATAN)

## Area Kajian
<img src="https://github.com/user-attachments/assets/39aac020-3ba3-41be-8a6a-6f03d7318871" alt="Peta Daerah Penelitian" width="710"/>



## Konfigurasi Arsitektur U-Net digunakan
![ModelArsitekturUnet (1)](https://github.com/user-attachments/assets/a0d76507-e39e-41e0-b9f5-b8ea56f858f7)

## Konfigurasi Hyperparameter digunakan
|   Konfigurasi        |   Detail                                |
|----------------------|-----------------------------------------|
|   Optimizer          |   Adam                                  |
|   Batch Size         |   4                                     |
|   Input Size         |   512x512x5                             |
|   Output Size        |   512x512x1                             |
|   Learning Rate  n   |   0.0001                                |
|   Epochs             |   200                                   |
|   Callback           |   Early Stopping dan ReduceLROnPlateau  |

## Rasio Data

| Data     | Persentase    | Jumlah Data                                  |
|----------|---------------|----------------------------------------------|
| Train    | 70%           | 706                                          |
| Test     | 30%           | 151                                          |
| Val      | 30%           | 151                                          |
| Total    | 100%          | 10008 pasangan (multiband dan mask)          |


## Waktu Eksekusi dan Pemakaian GPU

|   Informasi         |   Detail                    |
|---------------------|-----------------------------|
|   Waktu Eksekusi    |   20 menit 21 detik         |
|   Pemakaian GPU     |   16.16 GB/ 40 GB           |


## Grafik Accuracy dan Loss Model U-Net
<img width="842" height="274" alt="image" src="https://github.com/user-attachments/assets/4f239ae6-862b-4f06-aee4-761395a08e69" />

## Evaluasi Model

|   Evaluasi Model     |   Nilai    |
|----------------------|------------|
| Akurasi              | 0.93523    |
| IoU                  | 0.70858    |
| Dice Coefficient     | 0.82944    |
| Binary Cross Entropy | 0.18111    |



## Hasil Prediksi Model U-Net (beberapa citra)
https://github.com/alberanalafean22/Riset-TA/blob/9fb0e7065d18b72ff983fc38db1fb231f0cdbeb4/Hasil/prediksi.png 

