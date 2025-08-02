## Dataset
Diperoleh dari Platform GEE diakses melalui google colab pro, berikut link data yang telah dilakukakuna preprocessing dan siap digunakan dalam model U-Net:
*  ..... (Dalam pengajuan di Mendeley Data)
*  .... (Sudah dilakukan split data)

## Rasio Data (Split Data)

| Data     | Persentase    | Jumlah Data                                  |
|----------|---------------|----------------------------------------------|
| Train    | 70%           | 706                                          |
| Test     | 30%           | 151                                          |
| Val      | 30%           | 151                                          |
| Total    | 100%          | 10008 pasangan (multiband dan mask)          |


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


## Gambaran Data
*    Multiband
![170 124](https://github.com/user-attachments/assets/3828ef1d-924c-4af8-845c-4302cf900850)
*    Mask
![170 124 MASK](https://github.com/user-attachments/assets/8e078114-1c85-4f0e-a8ac-53ad2c2f2b57)
