## 项目简介

配平化学方程式

## 使用方法
### 1.直接调用balancer()函数

c4 = "KMnO4+H2SO4+FeSO4=Fe2(SO4)3+MnSO4+K2SO4+H2O"

res = balancer(c4, True)

print(res)

结果如下：  
需要配平的方程 

    KMnO4+H2SO4+FeSO4=Fe2(SO4)3+MnSO4+K2SO4+H2O 
    
提取反应物和生成物 

    ['KMnO4', 'H2SO4', 'FeSO4'] ['Fe2(SO4)3', 'MnSO4', 'K2SO4', 'H2O'] 
    
反应物和生成物进行变换 

    ['KMnOOOO', 'HHSOOOO', 'FeSOOOO'] ['FeFeSOOOOSOOOOSOOOO', 'MnSOOOO', 'KKSOOOO', 'HHO'] 
    
提取参与反应的元素 

    {'Mn', 'O', 'H', 'Fe', 'S', 'K'} 
    
生成线性方程组的系数矩阵 

    [1, 0, 0, 0, -1, 0, 0, 0] 
    [4, 4, 4, -12, -4, -4, -1, 0] 
    [0, 2, 0, 0, 0, 0, -2, 0] 
    [0, 0, 1, -2, 0, 0, 0, 0] 
    [0, 1, 1, -3, -1, -1, 0, 0] 
    [1, 0, 0, 0, 0, -2, 0, 0] 
求解方程组通解 

    {'f': 'g/8', 'e': 'g/4', 'd': '5*g/8', 'c': '5*g/4', 'b': 'g', 'a': 'g/4'} 
    
将通解进行化简整理，得到正整数解 

    {'f': 1, 'e': 2, 'd': 5, 'c': 10, 'b': 8, 'a': 2, 'g': 8} 
    
配平好的方程 

    2KMnO4 + 8H2SO4 + 10FeSO4 = 5Fe2(SO4)3 + 2MnSO4 + K2SO4 + 8H2O  

### 使用GUI
非常简单，但是还有些bug.

![GUI](https://raw.githubusercontent.com/lemodd/Chemical_Equation_Balancer/master/GUI.png)
