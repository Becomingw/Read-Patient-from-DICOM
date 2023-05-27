"""
Author: BecomingW
Date: 2023/5/26
License: MIT License
"""

import os
import sys

import pandas as pd
import pydicom


def extract_dicom_info(folder_path, output_file):
    # 创建一个空的DataFrame来存储DICOM信息
    df = pd.DataFrame(
        columns=['文件路径', 'Patient name', 'Patient ID', 'Sex', 'Age', 'Study date', 'Study ID', 'Series',
                 'Series description', 'Count'])
    erro_ls = []
    # 遍历文件夹下的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            try:
                # 使用pydicom读取DICOM文件
                dicom_data = pydicom.dcmread(file_path)

                # 提取DICOM元数据
                try:
                    patient_name = dicom_data.PatientName
                    patient_id = dicom_data.PatientID
                    sex = dicom_data.PatientSex
                    age = dicom_data.PatientAge
                    study_date = dicom_data.StudyDate
                    study_id = dicom_data.StudyID
                    series = dicom_data.SeriesNumber
                    series_description = dicom_data.SeriesDescription
                    count = dicom_data.InstanceNumber
                    # 将DICOM信息添加到DataFrame中
                    df_t = pd.DataFrame({
                        '文件路径': file_path,
                        'Patient name': patient_name,
                        'Patient ID': patient_id,
                        'Sex': sex,
                        'Age': age,
                        'Study date': study_date,
                        'Study ID': study_id,
                        'Series': series,
                        'Series description': series_description,
                        'Count': count
                    })
                    df = pd.concat([df, df_t], ignore_index=True)
                except:
                    erro_ls.append(file_path)

            except pydicom.errors.InvalidDicomError:
                pass

    # 将DataFrame导出为Excel文件
    try:
        df.to_excel(output_file, index=False)
        item = '已导出中间DICOM信息到文件:'
    except:
        item = '无中间信息文件导出'
    for erro in erro_ls:
        print(f'[{erro}]病人切片读取有误，请自行检查！')
    if output_file:
        print(f"{item} {output_file},出错{len(erro_ls)}条！")
    else:
        print(f"{item},出错{len(erro_ls)}条！")
    return df


if __name__ == '__main__':
    if len(sys.argv) > 1:
        folder_path = sys.argv[1]
    else:
        folder_path = '请替换为你的文件夹地址，或者环境传参'
output_file = 'Patientinf.xlsx'
df = extract_dicom_info(folder_path, output_file)
print('ok')

