## Data
Diperoleh dari Platform GEE diakses melalui google colab dan telah dilakukan tahapan data preparation dan preprocessing yang bisa dilihat pada direktori code pada github ini, berikut link data yang telah dilakukakun preprocessing dan siap digunakan dalam model U-Net:
*  https://data.mendeley.com/preview/vvkvbkjk2k?a=460361ae-7592-4009-8db4-37f5b43473a8 (Dalam pengajuan & preview)
*  https://www.kaggle.com/datasets/alberanalafean/burned-area-dataset

## Rasio Data (Split Data)

| Data     | Persentase    | Jumlah Data                                  |
|----------|---------------|----------------------------------------------|
| Train    | 70%           | 706                                          |
| Test     | 30%           | 151                                          |
| Val      | 30%           | 151                                          |
| Total    | 100%          | 10008 pasangan (multiband dan mask)          |


## Gambaran Data
Gambar kiri merupakan citra multiband yang menampilkan band komposit false color, sedangkan kanan merupakan citra mask (label/actual/groundtruth) dari citra multiband yang diperoleh dari tresholding dari DNBR

<img height="300" alt="image" src="https://github.com/user-attachments/assets/2701abca-1880-464f-9b33-74d94cc772a7" />


## Direktori Data

```text
data/
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
