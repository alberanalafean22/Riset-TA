## Data
Diperoleh dari Platform GEE diakses melalui google colab dan telah dilakukan tahapan data preparation dan preprocessing yang bisa dilihat pada direktori code pada github ini, berikut link data yang telah dilakukan preprocessing dan siap digunakan dalam model U-Net:
*  https://www.kaggle.com/datasets/alberanalafean/burned-area-dataset

## Rasio Data (Split Data)

| Data     | Persentase    | Jumlah Data                                  |
|----------|---------------|----------------------------------------------|
| Train    | 70%           | 706                                          |
| Test     | 30%           | 151                                          |
| Val      | 30%           | 151                                          |
| Total    | 100%          | 1008 pasangan (multiband dan mask)          |


## Gambaran Data
Gambar kiri merupakan citra multiband yang menampilkan band komposit false color, sedangkan kanan merupakan citra mask (label/actual/groundtruth) dari citra multiband yang diperoleh dari tresholding dari DNBR

<img height="300" alt="image" src="https://github.com/user-attachments/assets/2701abca-1880-464f-9b33-74d94cc772a7" />

Informasi Band disimpan pada citra multiband:

| Band     | Informasi disimpan   |
|----------|----------------------|
| 1        | NDVI                 |
| 2        | NBR                  |
| 3        | False Color (Band 4) |
| 4        | False Color (Band 5) |
| 5        | False Color (Band 7) |



## Direktori Data

```text
SPLITDATA/
├── TRAIN/
│   ├── MULTIBAND/
│   │   ├── patch_0004_125_multiband.tif
│   │   ├── patch_0005_124_multiband.tif
│   │   └── ...
│   └── MASK/
│       ├── patch_0004_125_mask.tif
│       ├── patch_0005_124_mask.tif
│       └── ...
│
├── VAL/
│   ├── MULTIBAND/
│   │   ├── patch_0004_124_multiband.tif
│   │   ├── patch_0005_125_multiband.tif
│   │   └── ...
│   └── MASK/
│       ├── patch_0004_124_mask.tif
│       ├── patch_0005_125_mask.tif
│       └── ...
│
└── TEST/
    ├── MULTIBAND/
    │   ├── patch_0007_124_multiband.tif
    │   ├── patch_0039_125_multiband.tif
    │   └── ...
    └── MASK/
        ├── patch_0007_124_mask.tif
        ├── patch_0039_125_mask.tif
        └── ...
```
