# Q7: What is regularization in machine learning, and how can it be used to prevent overfitting? Describe
# some common regularization techniques and how they work.

# Aanswer - 

# Regularization is a set of techniques in machine learning that is used to prevent overfitting, which occurs when a model learns to fit the training data 
# too closely, capturing noise and making it perform poorly on unseen data. Regularization methods introduce additional constraints or 
# penalties on the model's parameters, encouraging it to be simpler and generalize better to new data.

# # some common regularization techniques and how they work:  
# L1 Regularization (Lasso):

# L1 regularization adds a penalty term to the loss function that is proportional to the absolute values of the model's coefficients.
# It encourages sparse parameter values by shrinking some coefficients to exactly zero.
# This leads to feature selection, as some features become irrelevant and are effectively removed from the model.
# L2 Regularization (Ridge):

# L2 regularization adds a penalty term to the loss function that is proportional to the square of the model's coefficients.
# It discourages extreme parameter values, leading to a more balanced distribution of coefficients.
# L2 regularization helps prevent multicollinearity by encouraging the model to use all features.