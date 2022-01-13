# https://webapi.sporttery.cn/gateway/lottery/getHistoryPageListV1.qry?gameNo=35&provinceId=0&isVerify=1&termLimits=50


import pandas as pd
import numpy as np
titanic_data = pd.read_csv('file1.csv')




titanic_data['he'] = titanic_data['blue1']+titanic_data['blue2']+titanic_data['blue3']
titanic_data['number'] = titanic_data.apply(lambda x: str(x['blue1']) + str(x['blue2'])+str(x['blue3']), axis=1)


titanic_data['last_number'] = titanic_data['number'].shift(-1)
titanic_data['last_he'] = titanic_data['he'].shift(-1)


titanic_data= titanic_data.drop(columns='he')
titanic_data= titanic_data.drop(columns='issue')
titanic_data= titanic_data.drop(columns='date')
titanic_data= titanic_data.drop(columns='blue1')
titanic_data= titanic_data.drop(columns='blue2')
titanic_data= titanic_data.drop(columns='blue3')

print(titanic_data.head())

titanic_data.to_csv("result.csv",  encoding='utf-8', index=False)





# titanic_data['blue1_new'] = np.where(
#     titanic_data['blue1'] % 2 == 0, "双数", "单数")

# titanic_data["subgroup"] = titanic_data["blue1_new"].ne(titanic_data["blue1_new"].shift()).cumsum()

# def get_max_consecutive(name):
#     return titanic_data.groupby(["blue1_new", "subgroup"]).apply(len)[name].max()

# for name in titanic_data.blue1_new.unique():
#     print(f"{name}: {get_max_consecutive(name)}")


# print(titanic_data.head())
# print(titanic_data['blue1_new'].value_counts())
