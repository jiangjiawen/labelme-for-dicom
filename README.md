# labelme用作CT图像的工具

代码全部来自原版的labelme，这里我只是做基础的改动。

## 改动点

1. 能够读取ct图像，但是不能读取连续帧的dicom图像，即只能读单独ct，后缀为dcm的文件。目前做过一版能够读连续帧的，但是目前不方便释放。

2. 增加窗宽窗位的修改。

3. 将translate和default_config.yaml 放在同exe目录下，因为配置参数的问题。新增了一些ct值范围的设置参数，这样的话利于随时修改，不用去用户目录下找。因为工作中有的人不擅长找这个配置文件的位置。

4. 将原版labelme的复制模式（ctrl+p）的按钮也放到了工具菜单栏上，这个功能替代以前开发的导入上一个下一个功能。这样的话和和原版labelme逻辑上是一致的。即打开这个功能，推到下一张图片，会自动带上上一张图片的标注。

5. 应该同时也能够读基础图像文件了。

## 创建独立的app

python暂时使用3.8，好像3.9以上有些问题，不知道是不是其他包冲突的问题。

```bash
# Setup conda
conda create --name labelme python=3.8
conda activate labelme

# Build the standalone executable
pip install .
pip install 'matplotlib==3.2.2'
pip install gdcm pydicom
pip install pyinstaller
pyinstaller labelme.spec
dist/labelme --version
```
