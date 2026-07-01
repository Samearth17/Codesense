def loan_payment(loan_amt, annual_interest_rate, loan_period):
  # convert the interest rate to a decimal
  interest_rate = annual_interest_rate / 100

  # calculate the monthly interest rate
  monthly_interest_rate = interest_rate/12

  # calculate the total number of payments
  total_payments = loan_period * 12

  # calculate the monthly payments
  monthly_payment = loan_amt*(monthly_interest_rate/(1\
          -(1+monthly_interest_rate)**(-total_payments)))

  return monthly_payment

#print the result 
print(loan_payment(10000, 5.5, 5))