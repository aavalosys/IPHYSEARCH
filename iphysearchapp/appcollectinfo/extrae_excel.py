# Importar el módulo pandas
import os
import pandas as pd


def extraexcel():
    current_dir = os.getcwd()
    excel_path = current_dir +"\env_var\\vlans_gt.xlsx"
    print (excel_path)
    vlans = pd.read_excel(excel_path)
    dicvlans = vlans.to_dict()
    return dicvlans[0]

print (extraexcel())