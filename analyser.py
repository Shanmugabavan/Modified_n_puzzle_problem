import math
import statistics
import numpy as np
import scipy.stats as st

def getText(file):
    f=open(file,'r')
    input_list=f.read().split('\n')
    f.close()
    if input_list[-1]=="":
        del input_list[-1]
    number_list=[int(i) for i in (input_list)]
    return number_list

def showResult(output,analysis_report):
    f=open(analysis_report,'w')
    m=""
    for i in output:
        m=m+str(i)+'\n'
    print(m)
    f.write(m)
    f.close()

def find_differences(misplaced_list,manhatton_list):
    difference_list=[]
    for i in range(len(misplaced_list)):
        difference_list.append(abs(misplaced_list[i]-manhatton_list[i]))
    return difference_list

misplaced='analyse_misplaced.txt'
manhatton='analyse_manhatton.txt'
analysis_report='analysis report.txt'
misplaced_list=getText(misplaced)
manhatton_list=getText(manhatton)

manhattan = np.array(manhatton_list)
misplaced = np.array(misplaced_list)

differences_list=find_differences(misplaced_list,manhatton_list)
mean=(statistics.mean(find_differences(misplaced_list,manhatton_list)))
t_test = st.ttest_ind(a=misplaced,b = manhattan)
# t_test_1=t_test.statistics
# t_test_2=t_test.pvalue


output_list=["misplaced_list: ",str(misplaced_list),"manhatton_list: ",str(manhatton_list),"difference_list: ",str(differences_list),"Mean: ",str(mean)]

showResult(output_list,analysis_report)

print("t-test")

print(t_test.statistic)
print(t_test.pvalue)




