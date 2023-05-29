"""
Author: BecomingW
Date: 2023/5/29
License: MIT License
"""
from dicomPa import extract_dicom_info, excel_trans
import pandas as pd

folder_path = "0522"  # 替换为你要提取DICOM信息的文件夹路径(相对路径，建议把该脚本放在与执行文件夹同级目录)
OUT_excel = 'patient3.xlsx'  # 最终导出excel的地址

# 主程序(以下程序非必要请勿修改)
extract_dicom_info(folder_path)
Df = pd.read_excel('temporfile.xlsx', engine='openpyxl')
nums, out = excel_trans(Df, OUT_excel)
print(f'导出数据[{nums}]个，最终文件存储在[{out}].]')

