import pandas as pd

location = "C:/Users/Alan.Garcia/Downloads/"
filename = "WizzAd_Creatives_130322.xlsx"

wizzad_data = pd.read_excel(f"{location}{filename}", skipfooter=3, skiprows= 11)

print(wizzad_data.info())