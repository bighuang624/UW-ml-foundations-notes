train_data, test_data = sales.random_split(.8, seed=0)
sqft_model = graphlab.linear_regression.create(train_data, target='price', features=['sqft_living'],validation_set=None)


import matplotlib.pyplot as plt
%matplotlib inline # 使 matplotlib 在 notebook 里画图


plt.plot(test_data['sqft_living'], test_data['price'], '.', 
  test_data['sqft_living'],sqft_model.predict(test_data), '-')

sqft_model.get('coefficients') # 看权重（w1、w2）


# 

