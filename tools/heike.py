#-*-coding:utf-8-*-

# 等额本息 equality corpus and interest

# 每期费率 = （还款总额 - 本金） / 本金 / 期限
# B=还款总额
# a=贷款总金额
# i=每月费率，
# N=还贷总月数，

def aaa(i,N,a):
    B = (i / 100) * N * a + a
    print B

aaa(0.4,12,100000)


book = ['Python','development',8]
book.append(2008)
print book

