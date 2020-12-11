import pandas as pd
columns_list = ['Name','O','C','E','A','N']
#df = pd.DataFrame(columns=columns_list)
df1 = pd.DataFrame(columns=columns_list)
df = pd.read_excel('psychologistic/data.xlsx',index_col=0)
print(df)
#转成dataframe类型，再用append方法合并
def input_data():
    list = [0,0,0,0,0,0]
    for i in range(6):
        print('请输入第%s维度的数据：'%(i))
        list[i] = input()
    df1.loc[0] = list
    return df1
    
def output(df,df1):
    df1 = df1.apply(pd.to_numeric,errors='ignore') #忽略错误强制转换为浮点
    df = df.append(df1, ignore_index=True)
    df.to_excel('psychologistic/data.xlsx')


if __name__ == "__main__":
    new_input_data = input_data()
    new_output = output(df,new_input_data)


