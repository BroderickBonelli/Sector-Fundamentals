import pandas as pd 
import requests
from bs4 import BeautifulSoup
from IPython.display import display
import matplotlib.pyplot as plt 


telecom_services = ['VZ', 'T', 'TMUS', 'LUMN']
industrials_specialty_machinery = ['HON', 'MMM', 'GE', 'ITW', 'ROP', 'EMR', 'ETN', 'CMI', 'PNR', 'ROK', 'PH', 'TT', 'AME', 'DOV', 'IR', 'XYL', 'IEX', 'AOS', 'HWM', 'OTIS']
healthcare_medical_devices = ['ABT', 'MDT', 'SYK', 'BSX', 'EW', 'ZBH', 'ALGN', 'ABMD']
healthcare_drug_manufacturers_general = ['JNJ', 'PFE', 'MRK', 'LLY', 'AMGN', 'BMY', 'GILD', 'ABBV', 'BIIB']
financial_insurance_life = ['MET', 'AFL', 'PRU', 'GL', 'LNC', 'UNM']
basic_materials_chemicals = ['APD', 'DD', 'DOW', 'CE', 'EMN']
apd_linde = ['APD', 'LIN']
materials_specialty_chemicals = ['LIN', 'ECL', 'PPG', 'SHW', 'LYB', 'IFF', 'ALB']
consumer_cyclical_packaging_and_containers = ['BLL', 'AMCR', 'PKG', 'WRK', 'IP', 'SEE']
consumer_defensive_farm_products = ['ADM', 'TSN']
utilities_regulated_gas = ['ATO', 'CNP', 'NI']
industrials_staffing_and_employment_services = ['ADP', 'PAYX', 'RHI']
healthcare_medical_instruments_and_supplies = ['BDX', 'BAX', 'ISRG', 'TFX', 'COO', 'HOLX', 'RMD', 'STE', 'XRAY', 'WST']
consumer_defensive_beverages_wineries_and_distilleries = ['BF-B', 'STZ']
healthcare_medical_distribution = ['ABC', 'CAH', 'HSIC', 'MCK']
industrials_farm_and_heavy_construction_machinery = ['CAT', 'DE', 'PCAR']
energy_oil_and_gas_integrated = ['CVX', 'XOM', 'RDS-A', 'BP']
financial_insurance_property_and_casualty = ['CB', 'PGR', 'ALL', 'TRV', 'CINF', 'L', 'WRB']
industrials_specialty_business_services = ['CTAS', 'GPN', 'CPRT']
ctas_closest_competitors = ['CTAS', 'ARMK', 'UNF']
consumer_defensive_beverages_nonalcoholic = ['KO', 'PEP', 'MNST']
consumer_defensive_household_and_personal_products = ['CLX', 'PG', 'EL', 'KMB', 'CL', 'CHD', 'NWL', 'COTY']
utilities_regulated_electricity = ['NEE', 'SO', 'DUK', 'WEC', 'XEL', 'ES', 'AEP', 'ED', 'DTE', 'PPL', 'AEE', 'CMS', 'LNT', 'EVRG', 'PNW']
reit_residential = ['EQR', 'AVB', 'ESS', 'MAA', 'UDR', 'AIV']
industrials_integrated_freight_and_logistics = ['UPS', 'FDX', 'EXPD', 'JBHT', 'CHRW']
reit_retail = ['FRT', 'SPG', 'O', 'KIM', 'REG']
financial_asset_management = ['BLK', 'BK', 'STT', 'TROW', 'AMP', 'NTRS', 'BEN', 'IVZ']
industrials_aerospace_and_defense = ['LMT', 'RTX', 'BA', 'LHX', 'GD', 'TDG', 'NOC', 'HII', 'TXT']
consumer_cyclical_specialty_retail = ['GPC', 'ORLY', 'AZO', 'BBY', 'TSCO', 'ULTA', 'AAP']
consumer_defensive_packaged_foods = ['HRL', 'KHC', 'GIS', 'MKC', 'K', 'CAG', 'SJM', 'LW', 'CPB']
technology_information_technology_services = ['ACN', 'IBM', 'FIS', 'FISV', 'CTSH', 'FLT', 'CDW', 'LDOS', 'BR', 'JKHY']
consumer_cyclical_furnishings_fixtures_and_appliances = ['LEG', 'WHR', 'FBHS', 'MHK']
consumer_cyclical_home_improvement_retail = ['LOW', 'HD']
consumer_cyclical_restaurants = ['MCD', 'SBUX', 'YUM', 'DRI', 'CMG', 'WEN', 'QSR']
financials_banks_regional = ['USB', 'TFC', 'PNC', 'FRC', 'FITB', 'MTB', 'SIVB', 'KEY', 'CFG', 'HBAN', 'CMA', 'ZION', 'PBCT']
financial_financial_data_and_stock_exhanges = ['SPGI', 'CME', 'ICE', 'MCO', 'MSCI', 'NDAQ', 'CBOE']
industrials_tools_accessories = ['SWK', 'SNA']
consumer_defensive_food_distribution = ['SYY', 'USFD', 'PFGC']
consumer_defensive_discount_stores = ['TGT', 'WMT', 'COST', 'DG', 'DLTR']
consumer_cyclical_apparel_manufacturing = ['VFC', 'RL', 'UAA', 'PVH', 'HBI', 'CPRI']
healthcare_pharmaceutical_retailers = ['WBA', 'CVX', 'RAD']
semiconductors = ['NVDA', 'AVGO', 'QCOM', 'INTC', 'TXN', 'MU', 'ADI', 'AMD', 'XLNX', 'MCHP', 'SWKS', 'QRVO']
cyber_security = ['AKAM', 'FFIV', 'FTNT', 'NLOK', 'CRWD', 'PANW', 'FEYE', 'ZS']
gold_miners = ['NEM', 'GOLD', 'AEM', 'KL', 'AU', 'KGC']
entertainment = ['DIS', 'CMCSA', 'NFLX', 'CHTR', 'VIAC', 'DISH', 'LYV', 'DISCA']
grocery_stores = ['KR', 'ACI', 'CASY', 'GO', 'SFM']
technology_software_infrastructure = ['MSFT', 'ADBE', 'ORCL', 'SNPS']
technology_software_application = ['CRM', 'INTU', 'NOW', 'ADSK', 'ANSS', 'PAYC', 'TYL', 'CTXS', 'PTC', 'CDNS']
technology_information_technology_services = ['ACN', 'IBM', 'FIS', 'FISV', 'CTSH', 'IT', 'CDW', 'BR', 'LDOS']
technology_communication_equipment = ['CSCO', 'ZBRA', 'MSI', 'HPE', 'JNPR']
technology_semiconductor_equipment = ['AMAT', 'LRCX', 'KLAC', 'TER', 'IPGP']
technology_scientific_instruments = ['GRMN', 'KEYS', 'FTV', 'TRMB', 'TDY']
technology_computer_hardware = ['HPQ', 'ANET', 'STX', 'WDC', 'NTAP']
technology_electronic_components = ['TEL', 'APH', 'GLW']
REITS_specialty = ['AMT', 'CCI', 'IRM', 'EQIX', 'SBAC', 'WY']
REITS_industrial = ['DRE', 'PLD', 'PSA', 'EXR']
healthcare_diagnostics_and_research = ['DHR', 'TMO', 'ILMN', 'A', 'DXCM', 'IDXX', 'IQV', 'MTD', 'WAT', 'LH', 'CRL']
healthcare_biotech = ['MRNA', 'REGN', 'VRTX', 'INCY']
healthcare_plans = ['UNH', 'CVS', 'ANTM', 'CI', 'HUM', 'CNC']




def sector_fundamentals(sector):

	current_ratio_list = []
	quick_ratio_list = []
	cash_per_share_list = []
	debt_to_eq_list = []
	LTdebt_to_eq_list = []
	roa_list = []
	roi_list = []
	gross_margin_list = []
	operating_margin_list = []
	profit_margin_list = []
	five_year_sales_list = []
	five_earnings_list = []
	index_list = [' ', 'Current Ratio', 'Quick Ratio', 'Cash per Share', 'Debt to Equity', 'LT Debt to Equity', 'ROA', 'ROI', 'Gross Margin', 'Oper. Margin', 'Profit Margin', '5y EPS Growth', '5y Sales Growth']
	final_list = [sector, current_ratio_list, quick_ratio_list, cash_per_share_list, debt_to_eq_list, LTdebt_to_eq_list, roa_list, roi_list, gross_margin_list, operating_margin_list, profit_margin_list, five_earnings_list, five_year_sales_list]

	for each_aristocrat in sector:
		url = 'https://finviz.com/quote.ashx?t={}'.format(each_aristocrat)
		r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
		soup = BeautifulSoup(r.text, 'lxml')

		current_ratio = soup.find('td', string='Current Ratio').find_next('td').text
		if current_ratio != '-':
			current_ratio_list.append(float(current_ratio))
		else:
			current_ratio_list.append(current_ratio)

		quick_ratio = soup.find('td', string='Quick Ratio').find_next('td').text
		if quick_ratio != '-':
			quick_ratio_list.append(float(quick_ratio))
		else:
			quick_ratio_list.append(quick_ratio)

		cash_per_share = soup.find('td', string='Cash/sh').find_next('td').text
		if cash_per_share != '-':
			cash_per_share_list.append(float(cash_per_share))
		else:
			cash_per_share_list.append(cash_per_share)

		debt_to_eq = soup.find('td', string='Debt/Eq').find_next('td').text
		if debt_to_eq != '-':
			debt_to_eq_list.append(float(debt_to_eq))
		else:
			debt_to_eq_list.append(debt_to_eq)

		LTdebt_to_eq = soup.find('td', string='LT Debt/Eq').find_next('td').text
		if LTdebt_to_eq != '-':
			LTdebt_to_eq_list.append(float(LTdebt_to_eq))
		else:
			LTdebt_to_eq_list.append(LTdebt_to_eq)


		roa = soup.find('td', string='ROA').find_next('td').text.strip('%')
		if roa != '-':
			roa_list.append(float(roa))
		else:
			roa_list.append(roa)		

		roi = soup.find('td', string='ROI').find_next('td').text.strip('%')
		if roi != '-':
			roi_list.append(float(roi))
		else:
			roi_list.append(roi)

		gross_margin = soup.find('td', string='Gross Margin').find_next('td').text.strip('%')
		if gross_margin != '-':
			gross_margin_list.append(float(gross_margin))
		else:
			gross_margin_list.append(gross_margin)

		op_margin = soup.find('td', string='Oper. Margin').find_next('td').text.strip('%')
		if op_margin != '-':
			operating_margin_list.append(float(op_margin))
		else:
			operating_margin_list.append(op_margin)


		profit_margin = soup.find('td', string='Profit Margin').find_next('td').text.strip('%')
		if profit_margin != '-':
			profit_margin_list.append(float(profit_margin))
		else:
			profit_margin_list.append(profit_margin)

		five_year_sales = soup.find('td', string='Sales past 5Y').find_next('td').text.strip('%')
		if five_year_sales != '-':
			five_year_sales_list.append(float(five_year_sales))
		else:
			five_year_sales_list.append(five_year_sales)

		five_earnings = soup.find('td', string='EPS past 5Y').find_next('td').text.strip('%')
		if five_earnings != '-':
			five_earnings_list.append(float(five_earnings))
		else:
			five_earnings_list.append(five_earnings)


	df = pd.DataFrame(final_list)
	df[' '] = index_list

	new_header = df.iloc[0]
	df = df[1:]
	df.columns = new_header
	df.set_index(' ', inplace=True, drop=True)
	df.reset_index()

	df.to_csv('/Users/broderickbonelli/Desktop/test.csv')
    
    
    
    
    

sector_fundamentals(entertainment)


#read in data and graph w/ color gradient

data = pd.read_csv('/Users/broderickbonelli/Desktop/test.csv', index_col=" ", na_values='-')

#data = data.style.background_gradient(axis=1, cmap='RdYlGn').set_precision(2).background_gradient(cmap='RdYlGn_r', subset=(data.index[2], data.columns)).background_gradient(cmap='RdYlGn_r', subset=(data.index[3], data.columns))
data = data.style.background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[0], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[1], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[2], data.columns)).background_gradient(axis=1, cmap='RdYlGn_r', subset=(data.index[3], data.columns)).background_gradient(axis=1, cmap='RdYlGn_r', subset=(data.index[4], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[5], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[6], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[7], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[8], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[9], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[10], data.columns)).background_gradient(axis=1, cmap='RdYlGn', subset=(data.index[11], data.columns)).set_precision(2)
display(data)