import pandas as pd

location = "C:/Users/Alan.Garcia/Downloads"
filename = "WizzAd_200322.xlsx"

wizzad_data = pd.read_excel(f"{location}/{filename}", skipfooter=5, skiprows= 11)

### Clasifying Brand into LoB

line_of_business = {"Mobility": "MOBILE", "Institutional": "BRAND", "Business": "BUSINESS", "Home": "HOME"}

for new_lob, old_lob in line_of_business.items():
    aux_bool = wizzad_data["Telco Line of Business 2022"].isin([old_lob])
    wizzad_data.loc[aux_bool, "Category"] = new_lob

cols_index = [1,2]
cols_index.extend(list(range(4,12)))
wizzad_data = wizzad_data.iloc[:,cols_index]

### Renaming Columns

old_columns_names = list(wizzad_data.columns)
new_columns_names = "Advertiser Brand Creative_Description Media_Type Media_Owner Date Month Week Spend Category".split(" ")
new_columns_names = {ocn: ncl for ocn, ncl in zip(old_columns_names,new_columns_names) }
wizzad_data.rename(columns = new_columns_names, inplace = True)


advertisers = {"DISH NETWORK": "DISH", "NEPTUNO NETWORKS": "NEPTUNO", "BOOST MOBILE": "BOOST"}
for old_adv, new_adv in advertisers.items():
    aux_bool = wizzad_data["Advertiser"].isin([old_adv])
    wizzad_data.loc[aux_bool, "Category"] = new_adv

wizzad_data.to_csv("C:/Users/Alan.Garcia/OneDrive - OneWorkplace/new_wizzad.csv", index = False)


# institutional = ["CLARO: INSTITUTIONAL", "LIBERTY: INSTITUTIONAL", # eran residence
#                      'T-MOBILE: INSTITUTIONAL',"AT&T: INSTITUTIONAL",'AT&T: CO BRAND', # eran mobility
#                      'LIBERTY MOBILE']

# home = ['AT&T: INTERNET', 'DIRECTV: INSTITUTIONAL', 'DISH: INSTITUTIONAL',
#                  'CLARO: INTERNET', 'CLARO: LIFELINE', 'CLARO: MULTIPROD', 'DIRECTV: CABLE',
#                  'DIRECTV: PROGRAM', 'DISH NETWORK: HOPPER', 'HUGHESNET: INTERNET',
#                  'LIBERTY: CABLE', 'LIBERTY: GO', 'LIBERTY: INTERNET', 'LIBERTY: LIFELINE',
#                  'LIBERTY: MULTIPROD', 'LIBERTY: ON DEMAND', 'LIBERTY: PAY PER VIEW', 'LIBERTY: PROGRAMACION','LIBERTY: HUB TV',
#                  'NEPTUNO: INTERNET', 'AT&T: DTV HBO MAX',
#                  'AT&T: DTV PPV', 'AT&T: DTV PROGRAM', 'AT&T: MULTIPROD', 'AERONET: INTERNET',
#                  'CLARO: CABLE', 'DISH NETWORK: ANYWHERE', 'DISH NETWORK: CABLE', 'DISH NETWORK: MULTIPROD',
#                  'LIBERTY: EVERYWHERE', 'LIBERTY: PREMIUM CHANNELS','OPTICO: INTERNET', 'PRWIRELESS: INTERNET',
#                  'WORLDNET: INTERNET','CLARO: TV','LIBERTY: CABLE TV', 'OPTICO FIBER',
#                  'KIWISAT: SATELITE']


# mobility = ['AT&T: FIRSTNET','AT&T: LIFELINE', 
#                  'AT&T: POST PAID', 'AT&T: PREPAID', 'BOOST: PREPAID',
#                  'CLARO: POST PAID', 'CLARO: PREPAID', 'T-MOBILE: INTERNET',
#                  'T-MOBILE: POST PAID', 'T-MOBILE: PREPAID','LIBERTY: POST PAID',
#                  'LIBERTY: PREPAID','BOOST: INSTITUTIONAL','SPRINT: POST PAID', 'SPRINT: INSTITUTIONAL',
#                  'ENTOUCH WIRELESS: POST PAID','Q LINK WIRELESS: POSTPAID','LIFE WIRELESS: POSTPAID']


# business = ['AT&T: BUSINESS', 'CLARO: BUSINESS', 'LIBERTY: BUSINESS',
#                 'T-MOBILE: BUSINESS','AERONET: BUSINESS', 'DIRECTV: BUSINESS', 
#                 'LIBERTY: BUSINESS MULTIPROD','FUSE: INTERNET','FUSE TELECOM',
#                 'WORLDNET: BUSINESS','DM WIRELESS: BUSINESS']
