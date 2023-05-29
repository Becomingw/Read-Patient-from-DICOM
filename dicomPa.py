"""
Author: BecomingW
Date: 2023/5/29
License: MIT License
"""


import os
import pandas as pd
import pydicom


def extract_dicom_info(folder_path):
    # 创建一个空的DataFrame来存储DICOM信息
    df = pd.DataFrame(
        columns=['文件路径', 'Patient name', 'Patient ID', 'Sex', 'Age', 'Study date', 'Study ID', 'Series',
                 'Series description', 'Count'])
    erro_ls = []
    nono_ls = []
    # 遍历文件夹下的所有文件
    verify = [66, 101, 99, 111, 109, 105, 110, 103, 87]
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
                    df = df.append({
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
                    }, ignore_index=True)
                except:
                    erro_ls.append(file_path)

            except pydicom.errors.InvalidDicomError:
                nono_ls.append(file_path)

    for erro in erro_ls:
        print(f'[{erro}]病人切片读取有误，请自行检查！')
    for nono in nono_ls:
        print(f"无效的DICOM文件: [{nono}]")
        # 将DataFrame导出为Excel文件
    CR = ''.join(chr(x) for x in verify)
    df.at[len(df['文件路径']), 'Count'] = CR
    df.to_excel('temporfile.xlsx', index=False)



def excel_trans(Df, OUT_excel='Patientinf.xlsx'):
    data = {'文件路径':[],'Patient name':[], 'Patient ID':[], 'Sex':[],'Study date':[],'Study ID':[],'Series':[],'Series description':[],'Count':[]}
    dt = pd.DataFrame(data)
    patient = ''
    studydate = ''
    serise = ''
    ss = ''
    count = 1
    i = 0
    for index, row in Df.iterrows():
        if row['Patient ID'] == patient:
            if row['Series description'] == serise:
                if row['Study date'] == studydate:
                    if row['Series'] == ss:
                        count += 1
                    else:
                        ss = row['Series']
                        dt.at[i, '文件路径'] = Df.at[index - 1 if index > 0 else 0, '文件路径']
                        dt.at[i, 'Patient name'] = Df.at[index - 1 if index > 0 else 0, 'Patient name']
                        dt.at[i, 'Patient ID'] = Df.at[index - 1 if index > 0 else 0, 'Patient ID']
                        dt.at[i, 'Sex'] = Df.at[index - 1 if index > 0 else 0, 'Sex']
                        dt.at[i, 'Study date'] = Df.at[index - 1 if index > 0 else 0, 'Study date']
                        dt.at[i, 'Study ID'] = Df.at[index - 1 if index > 0 else 0, 'Study ID']
                        dt.at[i, 'Series'] = Df.at[index - 1 if index > 0 else 0, 'Series']
                        dt.at[i, 'Series description'] = Df.at[index - 1 if index > 0 else 0, 'Series description']
                        dt.at[i, 'Count'] = count
                        count = 1
                        i += 1
                else:
                    studydate = row['Study date']
                    ss = row['Series']
                    dt.at[i, '文件路径'] = Df.at[index - 1 if index > 0 else 0, '文件路径']
                    dt.at[i, 'Patient name'] = Df.at[index - 1 if index > 0 else 0, 'Patient name']
                    dt.at[i, 'Patient ID'] = Df.at[index - 1 if index > 0 else 0, 'Patient ID']
                    dt.at[i, 'Sex'] = Df.at[index - 1 if index > 0 else 0, 'Sex']
                    dt.at[i, 'Study date'] = Df.at[index - 1 if index > 0 else 0, 'Study date']
                    dt.at[i, 'Study ID'] = Df.at[index - 1 if index > 0 else 0, 'Study ID']
                    dt.at[i, 'Series'] = Df.at[index - 1 if index > 0 else 0, 'Series']
                    dt.at[i, 'Series description'] = Df.at[index - 1 if index > 0 else 0, 'Series description']
                    dt.at[i, 'Count'] = count
                    count = 1
                    i += 1
            else:
                serise = row['Series description']
                studydate = row['Study date']
                ss = row['Series']
                dt.at[i, '文件路径'] = Df.at[index - 1 if index > 0 else 0, '文件路径']
                dt.at[i, 'Patient name'] = Df.at[index - 1 if index > 0 else 0, 'Patient name']
                dt.at[i, 'Patient ID'] = Df.at[index - 1 if index > 0 else 0, 'Patient ID']
                dt.at[i, 'Sex'] = Df.at[index - 1 if index > 0 else 0, 'Sex']
                dt.at[i, 'Study date'] = Df.at[index - 1 if index > 0 else 0, 'Study date']
                dt.at[i, 'Study ID'] = Df.at[index - 1 if index > 0 else 0, 'Study ID']
                dt.at[i, 'Series'] = Df.at[index - 1 if index > 0 else 0, 'Series']
                dt.at[i, 'Series description'] = Df.at[index - 1 if index > 0 else 0, 'Series description']
                dt.at[i, 'Count'] = count
                count = 1
                i += 1
        else:
            patient = row['Patient ID']
            serise = row['Series description']
            studydate = row['Study date']
            ss = row['Series']
            dt.at[i, '文件路径'] = Df.at[index - 1 if index > 0 else 0, '文件路径']
            dt.at[i, 'Patient name'] = Df.at[index - 1 if index > 0 else 0, 'Patient name']
            dt.at[i, 'Patient ID'] = Df.at[index - 1 if index > 0 else 0, 'Patient ID']
            dt.at[i, 'Sex'] = Df.at[index - 1 if index > 0 else 0, 'Sex']
            dt.at[i, 'Study date'] = Df.at[index - 1 if index > 0 else 0, 'Study date']
            dt.at[i, 'Study ID'] = Df.at[index - 1 if index > 0 else 0, 'Study ID']
            dt.at[i, 'Series'] = Df.at[index - 1 if index > 0 else 0, 'Series']
            dt.at[i, 'Series description'] = Df.at[index - 1 if index > 0 else 0, 'Series description']
            dt.at[i, 'Count'] = count
            count = 1
            i += 1
    dt = dt.drop(index=0)
    num = len(dt['文件路径'])
    dt.to_excel(OUT_excel, engine='openpyxl', index=False)
    return num, OUT_excel


if __name__ == '__main__':
    Df = pd.read_excel('pp.xlsx', engine='openpyxl')
    excel_trans(Df, 'patientID.xlsx')
