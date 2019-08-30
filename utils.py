from sympy import Matrix, symbols
from sympy import solve_linear_system
import re


def get_compd(cheq):
    cheq_l, cheq_r = cheq.replace(" ","").split('=')
    compdl=cheq_l.split('+')
    compdr=cheq_r.split('+')
    return compdl,compdr



#求一组数的最小公倍数的方法
#每一次操作都把当前最小的那个数加上它的初始值，直到所有数都相等为止。
def get_lcm(num):
    '''
    num: list[int,int,...]
    '''
    num2=num.copy()
    while True:
        mi = min(num2)
        ma = max(num2)

        if mi!=ma:
            ind = num2.index(mi)
            num2[ind] += num[ind]
        else:
            break
    return num2[0]

def get_denom(ans):
    '''
    ans:dict
    ans = {'a':"4*d/3",'b':"2*d/3",'c':"d/2"}
    get [3,3,2]
    '''
    vals = ans.values()
    denoms = []     #分母
    for v in vals:
        if '/' in v:
            denoms.append(int(v.split('/')[-1]))
    return denoms

def solve_lin_eqs(A):
    M = Matrix(A)
	#元素个数
    count = M.shape[1]-1
    
	#下面的方法动态改变未知数的个数
    sml = []
    #根据所需定义符号
    for i in range(count):
        s = chr(i+97)
        sml.append(symbols(s))			
    ##	print(sml)
    #生成代码					
    cmd = "res = solve_linear_system(M,"
    for i in range(count):
        cmd += "sml[" +str(i)+"]" +','
    cmd = cmd[:-1]+")"

    ##	print(cmd)
    #执行代码
    exec(cmd)
    #打印结果
    #非常重要，必须这样写
    rr = locals()['res']
    # print(str(sml[0]))
    # print(str(rr[sml[0]]))
    res_dict={}

    for k,v in rr.items():
##        print(k,v)
        res_dict[str(k)] = str(v)

    # print(res_dict)
    return res_dict


def get_ans(res):
    #res为方程组的所有解
    #含有自由项d，并且还是分数（如数方程的未知数改变折话，也可能是e,f,c等）
    #需选取合适的d值，将结果变为整数
    #d取所有分母的最小公倍数，即能满足要求
    # ans = {'a':"4*d/3",'b':"2*d/3",'c':"d/2"}
    # ans = {'b': '5*e/6', 'd': 'e/3', 'c': '2*e/3', 'a': '2*e/3'}
    #得到所有的分母
    deno = get_denom(res)
    #分母的最小公倍数
    lcm = 1
    if deno != []:
        lcm = get_lcm(deno)
    
    #用lcm代替d,并计算表达式的值（如数方程的未知数改变折话，d也可能是e,f,c等）
    #需找到未知数是哪个字母并且用lcm代替
    #找到表达式第一个字母就是
    for alph in res['a']:
        if alph.isalpha():
            break
    
    for k,v in res.items():
        exp = str(v).replace(alph,str(lcm))
        val = int(eval(exp))
        res[k] = val
    res[alph] = lcm
    return res


#得到所有的元素
def get_elem(cmpd):
    elems = []
    for c in cmpd:
        for s in c:
            if s.isupper():
                elems.append(s)
            if s.islower():
                elems[-1]+=s
                

    return set(elems)

#元素计数
"HCl + NaOH = NaCl + HHO"
#字母后面的数字还不能识别
def count_elem(cmpd1,cmpd2,elem):
##    print(cmpd1,cmpd2)
##    print(elem)
    M=[]
    L=[]
    for e in elem:
        for c in cmpd1:
            L.append(c.count(e))
        for c in cmpd2:
            L.append(-c.count(e))
        L.append(0)
        M.append(L)
        L=[]

    return M


def get_compd2(cheq):
    cheq_l, cheq_r = cheq.replace(" ","").split('=')
    compdl=cheq_l.split('+')
    compdr=cheq_r.split('+')
    compdl = [extent2(x) for x in compdl]
    compdr = [extent2(x) for x in compdr]
    return compdl,compdr




def extent(ss):
    import re
    #"FeCl3" --> ["Fe","Cl3"] -> 'FeClClCl'
    
    pattern="[A-Z]"
    new_string=re.sub(pattern,lambda x:" "+x.group(0),ss)
    sp = new_string.split()
   #print(sp)

    #['Fe', 'Cl3']-->['Fe', 'ClClCl'] -->FeClClCl
    for j in range(len(sp)):
        cc = sp[j]     
        for i in range(len(cc)):
            if cc[i].isnumeric():
                sp[j]=(cc[:i]*int(cc[i:]))
                break
    return ''.join(sp)
    

def extent2(ss):
    
    #"FeCl3" --> ["Fe","Cl3"] -> 'FeClClCl'
    
    ss = del_pare(ss)


    pattern="[A-Z]"
    new_string=re.sub(pattern,lambda x:" "+x.group(0),ss)
    sp = new_string.split()
   #print(sp)

    #['Fe', 'Cl3']-->['Fe', 'ClClCl'] -->FeClClCl
    for j in range(len(sp)):
        cc = sp[j]     
        for i in range(len(cc)):
            if cc[i].isnumeric():
                sp[j]=(cc[:i]*int(cc[i:]))
                break
    return ''.join(sp)    


#去掉括号
#Cu(OH)2 -> CuOHOH

def del_pare(test_str):
    if "(" not in test_str: return test_str
    pare = re.match(r".*\((.*)\).*", test_str)
    pare_content = pare.group(1)
    # print(pare_content)
    pare_count =re.findall(r'(\d+)',test_str)[-1]
    # print(pare_count)
    # print(type(pare_count))
    temp = pare_content*int(pare_count)
    temp2 = f"({pare_content}){pare_count}"
    # print(temp2)
    test_str = test_str.replace(temp2,temp)
    return test_str


def balancer(cheq, verbose = False):
    if not check(cheq): return False
    if verbose: 
        print("需要配平的方程")
        print("    ",end = '')
        print(cheq)
    
    compd1,compd2 = get_compd(cheq)
    if verbose:
        print("提取反应物和生成物")
        print("    ",end = '')
        print(compd1,compd2)
    compdl,compdr = get_compd2(cheq)
    if verbose: 
        print("反应物和生成物进行变换")
        print("    ",end = '')
        print(compdl,compdr)
    #得到所有参与的元素
    elems = get_elem(compdr)
    if verbose: 
        print("提取参与反应的元素")
        print("    ",end = '')
        print(elems)
    #生成线性方程组的矩阵
    F = count_elem(compdl,compdr,elems)
    if verbose: 
        print("生成线性方程组的系数矩阵")
        for f in F:
            print("    ",end = '')
            print(f)
    #解方程组
    res = solve_lin_eqs(F)
    if verbose: 
        print("求解方程组通解")
        print("    ",end = '')
        print(res)
    #化简解
    ans = get_ans(res)
    if verbose: 
        print("将通解进行化简整理，得到正整数解")
        print("    ",end = '')
        print(ans)
    
    #将结果排序
    k = sorted(ans.keys())
    v = [ans[i] for i in k]
    
    #将系数增加到原化学方程中
    cheq_balanced = ''
    for i,c in enumerate(compd1):
        coe = ''
        if v[i] != 1:
            coe = v[i]
        cheq_balanced+=str(coe) + c + " + "
    cheq_balanced = cheq_balanced[:-2]
    cheq_balanced += "= "
    for i,c in enumerate(compd2):
        coe = ''
        if v[i+len(compdl)] != 1:
            coe = v[i+len(compdl)]
        cheq_balanced+=str(coe) + c + " + "
    cheq_balanced = cheq_balanced[:-2]
   
    if verbose:
        print("配平好的方程")
        print("    ",end = '')
        print(cheq_balanced)
        print()
    else: 
        return cheq_balanced

def check(cheq):

    illegal_sign_str = "`~!@$%^&*_-[];',./\{\}:'|<>，。！￥…——《》" + '"'
    illegal_sign = list(illegal_sign_str)

    for il in illegal_sign:
        if il in cheq:
            print(f'错误，存在非法字符"{il}"')
            return False


    if cheq.count("=") != 1:
        print('格式错误！反应物与生成物之间只能用一个"="连接')
        return False

    comp1,comp2 = get_compd2(cheq)
    elem1 = get_elem(comp1)
    elem2 = get_elem(comp2)

    if elem1!=elem2:
        print("错误，反应物与生成物含有不同的元素！")
        print(elem1)
        print(elem2)
        return False

    return True





if __name__ =='__main__':
    c4 = "Fe + Cl2 = FeCl3"
    c4 = "C6H5COOH + O2 = CO2 + H2O"
    c4 = "C6H14 + CuO = Cu + CO2 + H2O"
    c4 = "PhCH3 + KMnO4 + H2SO4 = PhCOOH + K2SO4 + MnSO4 + H2O"
    c4 = "CaCl2 + AgNO3 = Ca(NO3)2 + AgCl"
    c4 = "K4Fe(CN)6 + KMnO4 + H2SO4 = KHSO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O"
    
    c4 = "FeS2+O2=Fe2O3+8SO2"
    c4 = "FeSO4+H2SO4+KMnO4=Fe2(SO4)3+K2SO4+MnSO4+H2O"
    c4 = "P2I4+P4+H2O=PH4I+H3PO4"
    c4 = "K2NaCo(NO2)6+KMnO4+H2SO4=K2SO4+Na2SO4+CoSO4+MnSO4+HNO3+H2O"
    c4 = "FeS2 + O2 = Fe2O3 + SO2"
    c4 = "MnO2 + HCl = MnCl2 + H2O + Cl2"
    c4 = "K4Fe(SCN)6 + K2Cr2O7 + H2SO4 = Fe2(SO4)3 + Cr2(SO4)3 + CO2 + H2O + K2SO4 + KNO3"
    c4 = "K4Fe(CN)6 + KMnO4 + H2SO4 = K2SO4 + Fe2(SO4)3 + MnSO4 + HNO3 + CO2 + H2O"
    c4 = "H2+Ca(CN)2+NaAlF4+FeSO4+MgSiO3+KI+H3PO4+PbCrO4+BrCl+CF2Cl2+SO2=PbBr2+CrCl3+MgCO3+KAl(OH)4+Fe(SCN)3+PI3+Na2SiO3+CaF2+H2O"
    c4 = "KMnO4+H2SO4+FeSO4=Fe2(SO4)3+MnSO4+K2SO4+H2O"
    res = balancer(c4, True)
    print(res)
    
   