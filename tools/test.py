#-*-coding:utf-8-*-

#  借款相关费用

# 一次性费用

# 1. 借款服务费
def loan_server_fee(countLoan, rate): 
  #费率
  x = float(rate) / 100
  loanServerFee = countLoan *  x
  print  loanServerFee

# 2. 借款人月还款金额 =  借款本金/期数+借款本金*月综合费率
#def aa():
# 3. 逾期罚息
# 4. 逾期管理费

loan_server_fee(50000, 5)