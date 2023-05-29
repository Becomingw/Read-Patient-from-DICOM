# Read Patient from DICOM🎞

DICOM（Digital Imaging and Communications in Medicine）即医学数字成像和通信，是医学图像和相关信息的国际标准（ISO 12052）。DICOM被广泛应用于放射医疗，心血管成像以及放射诊疗诊断设备（X射线，CT，核磁共振，超声等）。所有患者的医学图像都以 DICOM 文件格式进行存储。这个格式包含关于患者的PHI（protected health information）信息，例如姓名，性别，年龄，以及其他图像相关信息比如捕获并生成图像的设备信息，医疗的一些上下文相关信息等。

在日常中我们获取了一批DICOM文件，并不知道它的影像信息，例如：不知道它的模态、序列、病人信息。我们就没法对这些数据进行分类或者做对应的图像处理。这个脚本可以帮你快速获取一个文件夹下的所有dicom文件的基本信息，并保存为一个excel表格。
### Feature: 任何混乱文件夹，只要文件夹里面有Dicom就能被读出来😉

## 🕶依赖：

Python >=3.9

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
在Run.py中修改：

```python
    folder_path = "dicomfolder"  # 替换为你要提取DICOM信息的文件夹路径(相对路径，建议把该脚本放在与执行文件夹同级目录)
```

输出文件名可以修改，默认为"Patientinf.xlsx"，输出位置：脚本所在文件夹下。\
‼ 程序运行时的警告报错属于正常现象，不用管就行。

## 范例：
#### ① 保存所有信息（这个保存在文件夹的temporfile.xlsx)

![Demo](https://github.com/Becomingw/Read-Patient-from-DICOM/blob/main/demo.png)
#### ② 最终保存的文件，将多余的序列信息汇总到了一起
![Demo2](https://github.com/Becomingw/Read-Patient-from-DICOM/blob/main/demo2.png)

## License
This project is licensed under the [MIT License](https://en.wikipedia.org/wiki/MIT_License)

## Refrence:
[医学图像DICOME格式信息解析](https://blog.csdn.net/Joker00007/article/details/127754815#:~:text=%E4%B8%89%E3%80%81DICOM%E5%86%85%E9%83%A8%E4%BF%A1%E6%81%AF%E8%AF%A6%E8%A7%A3%20%28DICOM%20Tag%E4%B8%8EVR%29%201%20TAG%E5%8F%B7%20%EF%BC%9A%E7%94%B14%E4%B8%AA%E5%AD%97%E8%8A%82%E7%BB%84%E6%88%90%EF%BC%8C%E5%8C%85%E6%8B%AC2%E5%AD%97%E8%8A%82%E7%9A%84%E7%BB%84%E5%8F%B7%E5%92%8C2%E5%AD%97%E8%8A%82%E7%9A%84%E5%85%83%E7%B4%A0%E5%8F%B7%EF%BC%88%E4%BE%8B%E5%A6%82%EF%BC%9A0010%200040%20%E8%A1%A8%E7%A4%BA%E6%82%A3%E8%80%85%E6%80%A7%E5%88%AB%EF%BC%8C,%E5%80%BC%E9%95%BF%E5%BA%A6%20%28value%20length%29%20%EF%BC%9A%E5%AD%98%E5%82%A8%E6%8F%8F%E8%BF%B0%E8%AF%A5%E9%A1%B9%E4%BF%A1%E6%81%AF%E7%9A%84%E6%95%B0%E6%8D%AE%E9%95%BF%E5%BA%A6%E3%80%82%204%20%E5%80%BC%E5%9F%9F%20%28value%29%20%EF%BC%9A%E5%AD%98%E5%82%A8%E6%8F%8F%E8%BF%B0%E8%AF%A5%E9%A1%B9%E4%BF%A1%E6%81%AF%E7%9A%84%E6%95%B0%E6%8D%AE%E5%80%BC%E3%80%82)





