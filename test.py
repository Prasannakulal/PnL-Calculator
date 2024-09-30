import tabula
import pandas as pd
text=input('Enter the pdf name : ')
textt=f"{text}.pdf"
try:
    df = tabula.read_pdf(textt, pages='all')[0]
except Exception as e:
    print(f"Error reading PDF: {e}")
    df = pd.DataFrame()  
try:
    tabula.convert_into(textt, "Investments-1.csv", output_format="csv", pages='all')
except Exception as e:
    print(f"Error converting PDF to CSV: {e}")
try:
    df1 = pd.read_csv("Investments-1.csv")
except FileNotFoundError:
    df1 = pd.DataFrame()  
if not df1.empty:
    df1.columns = ['Stock Symbol', 'Date Purchased', 'Shares Purchased', 'Purchase Price/Share', 'Date Sold', 'Sale Price/Share']
    similarcolms = df1[['Stock Symbol', 'Shares Purchased', 'Purchase Price/Share', 'Sale Price/Share']].dropna()
    similarcolms['Profit'] = (similarcolms['Sale Price/Share'] - similarcolms['Purchase Price/Share']) * similarcolms['Shares Purchased']
    final_df = similarcolms[['Stock Symbol', 'Profit']].reset_index(drop=True)
    final_df.to_csv(f'{text}-PnL.csv', index=False)
    print(f"Profit and Loss report saved successfully : {text}-PnL.csv")
else:
    print("No data to process.")


