# labelme-for-dicom
代码主要来自 https://github.com/wkentaro/labelme

本代码是在labelme基础上改的，主要是了能标注dicom数据，jpg，png于是让给改没了。

使用pydicom来导入dicom文件。

后期增加对.JL文件的支持，需要gdcm，安装参照 https://github.com/HealthplusAI/python3-gdcm 

其实就是加了个 ```import gdcm```，在app.py的第六行，如果是dicom文件，其实可以删除这行，没什么用，而且gdcm按照起来挺麻烦的。

然后最主要这个改造初始是为了肝脏肿瘤分割任务，所以窗宽窗位都是设计好了的, 40和200。

```
line 172:       self.wc_value = 40
line 173:       self.ww_value = 200
```
包括app.py文件最末端和widgets/zoom_widget.py里的一些配置，都写死了。所以其他器官可能需要改动下，包括还截了一下dicom值1200。

主要增加功能：
1. 是能够调节dicom窗宽窗位;
2. 是连续图片标注后一个导入前一个已标注的（便于调节），功能键是prelabel和nextlabel

注意事项：
1. prelabel和nextlabel从左右借完之后，最好调一下才能保存，最好要借的没有标注生成的json文件哈;
2. 和原版labelme 冲突，需要卸载原版labelme才能使用。

运行就简单的
```
python main.py
```

大概就是这个样子

![image](jiangjiawen/labelme-for-dicom/blob/master/pics/pic.png)
