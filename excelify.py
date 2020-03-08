import json
import csv

def json_to_csv(textfile):

    company_data = json.load(textfile)

    company_data_arr = [["ticker","market_cap","pe_ratio","roe","div_yield","net_margin_q0", "price_cash", "peg_ratio",
                         "pb_ratio", "eps_growth_5y", "eps_growth_this_yr", "sales_growth_5y", "dividend_payout_ratio"]]

    for company in company_data:

        company_data_arr.append([company['ticker'], company['market_val'], company['pe_ratio_12m'], company['roe_q0'],
                                 company['div_yield'], company['net_margin_q0'], company['price_cash'],
                                 company['peg_ratio'], company['price_book'], company['eps_growth_5y'],
                                 company['eps_growth_this_yr'], company['sales_growth_5y'], company['dividend_payout_ratio']])

    #write to a csv file
    with open('company_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(company_data_arr)
