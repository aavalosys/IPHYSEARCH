# Importar el módulo pandas
import os
import pandas as pd


def extraexcel():
    excel_path = "D:\\Users\\avalos.nelson\\Documents\DOC_IP\\CONSOLIDADO_TAREAS\\T2024\\Reporte_Tareas_Proveedores_22_12_23.xlsx"
    tareas = pd.read_excel(excel_path)
    tareas_dic = tareas.to_dict()
    return {k: tareas_dic[k] for k in ['DIAS_TAREA','ID']}
print (extraexcel())