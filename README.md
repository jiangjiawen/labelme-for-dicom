# labelme-for-dicom
只为dicom，jpg，png给我搞没了，后续改下。

代码主要来自 https://github.com/wkentaro/labelme

使用pydicom来导入dicom文件。

增加功能：调节dicom窗宽窗位，连续图片标注后一个导入前一个已标注的（便于调节）

```
python main.py
```

增加对.JL文件的支持，需要gdcm，安装参照 https://github.com/HealthplusAI/python3-gdcm
