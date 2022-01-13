from autogluon.tabular import TabularDataset, TabularPredictor
import pandas as pd

train_data = pd.read_csv('result.csv')

# # train_data = TabularDataset(file_path=f'result.csv')
# subsample_size = 500  # subsample subset of data for faster demo, try setting this to much larger values
# train_data = train_data.sample(n=subsample_size, random_state=0)
label = 'number'
# print("Summary of class variable: \n", train_data[label].describe())
save_path = 'agModels-predictClass'  # specifies folder to store trained models


time_limit = 5*60
num_trials = 20
search_strategy = 'auto'
hyperparameter_tune_kwargs = {  # HPO is not performed unless hyperparameter_tune_kwargs is specified
    'num_trials': num_trials,
    'scheduler' : 'local',
    'searcher': search_strategy,
}


predictor = TabularPredictor(label=label, path=save_path).fit(train_data, time_limit=time_limit,hyperparameter_tune_kwargs=hyperparameter_tune_kwargs,)

# predictor = TabularPredictor.load(save_path)


# test_data = pd.read_csv('test.csv')
# test_data_nolab = test_data.drop(columns=[label])
# print(test_data_nolab.head())
# y_pred = predictor.predict(test_data_nolab)
# print(y_pred)

# label_column = 'number' # specifies which column do we want to predict
# savedir = 'otto_models/' # where to save trained models
# predictor = task.fit(train_data=train_data,
#                         label=label_column,
#                         output_directory=savedir,
#                         eval_metric='log_loss',
#                         auto_stack=True,
#                         verbosity=2,
#                         visualizer='tensorboard')


