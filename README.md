# Read Patient from DICOM

DICOM（Digital Imaging and Communications in Medicine）即医学数字成像和通信，是医学图像和相关信息的国际标准（ISO 12052）。DICOM被广泛应用于放射医疗，心血管成像以及放射诊疗诊断设备（X射线，CT，核磁共振，超声等）。所有患者的医学图像都以 DICOM 文件格式进行存储。这个格式包含关于患者的PHI（protected health information）信息，例如姓名，性别，年龄，以及其他图像相关信息比如捕获并生成图像的设备信息，医疗的一些上下文相关信息等。

在日常中我们获取了一批DICOM文件，并不知道它的影像信息，例如：不知道它的模态、序列、病人信息。我们就没法对这些数据进行分类。这个脚本可以帮你快速获取一个文件夹下的所有dicom文件的基本信息，并保存为一个excel表格。

## 依赖：

Python >=3.8

pandas

pydicom

## 安装：

需要先自行安装python！！！

```shell
clone 
cd Read_Patient_from_DICOM
pip install requirement -i https://pypi.tuna.tsinghua.edu.cn/simple #  使用清华源
```

## 使用：

本脚本提供两种传参方式：

1.在环境shell中直接使用：

```shell
python run.py dicomfolder  # 其中dicomfolder替换为你的dicom文件夹地址
```

2.在Run.py中修改：

```python
    folder_path = "dicomfolder"  # 替换为你要提取DICOM信息的文件夹路径(相对路径，建议把该脚本放在与执行文件夹同级目录)
```

然后，输出文件名也可以修改，默认为’‘Patientinf.xlsx“，输出位置：脚本所在文件夹下。

## 范例：



## License
This project is licensed under the MIT License - see the LICENSE file for details.






