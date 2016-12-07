#-*-coding:utf-8-*-

# 等额本息 equality corpus and interest

# [贷款本金×月利率×（1+月利率）^还款月数]÷[（1+月利率）^还款月数－1]
# B=等额本息还贷每月所还本金，
# a=贷款总金额
# i=贷款月利率，
# N=还贷总月数，
# n=第n期还贷数
# X=等额本息还贷每月所还的利息
# j=每月借款管理费费率 

#等额本金还款法利息计算
def equality_corpus_and_interest(a, i, N,n):
    x  = a * ( float(i) / 100 )
    y = (1+float(i) / 100) ** N 
    z = (1 + float(i) / 100) ** N - 1
    #每月还款额
    BX = x * y / z
    print '每月还款额 = %f '  % BX
    #return BX
    yy = (1+float(i) / 100) ** (n - 1)
    #某月还款本金
    B = x * yy / z
    print   '第%i 期应还本金 = %f ' %(n,B)
    #某月还款利息
    X = BX - B
    print '第%i期应还的利息 = %f ' % (n,X)
    #return  X

equality_corpus_and_interest(600000, 0.063, 120, 1)

# 每月借款管理费
def loan_manager_fee(a, j):
    loanManagerFee = a * (float(j) / 100)
    print  '每月借款管理费 = %f'  % loanManagerFee

equality_corpus_and_interest(50000,1,48,1)
#loan_manager_fee(10000,0.5)
 

# 一年的利息费
#sum =0
#for i in range(1,13):
#    aa = equality_corpus_and_interest(50000,1,48,i)
#   sum = aa+sum
    #print sum
#loan_manager_fee(50000,0.33)

# bn = equality_corpus_and_interest(288000,0.76,36,1)
# sum = bn 
# #print sum






