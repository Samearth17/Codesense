import pandas as pd

#Read the sales data
data = pd.read_csv('sales_data.csv')

# Generate a report for the sales data
def generate_report (data):
  #Group data by Region and Month
  region_month = data.groupby(['Region','Month'])
  
  #Calculate total sales
  total_sales = region_month.sum()['Sales']
  
  #Calculate total profit
  total_profit = region_month.sum()['Profit']
  
  #Calculate max sales
  max_sales = region_month.max()['Sales']
  
  #Create a report for the data
  report = pd.DataFrame({'Total Sales': total_sales,
                'Total Profit': total_profit,
                'Max Sales': max_sales})
  
  #Return the report
  return report

#Run the report
print(generate_report(data))