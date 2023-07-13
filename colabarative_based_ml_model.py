import pandas
ratings = pandas.read_csv('ratings.csv')[["userId","movieId","rating"]]

#create a dataset

from surprise import Dataset, Reader

reader = Reader(rating_scale=(1,5))
dataset = Dataset.load_from_df(ratings,reader)

#op = <surprise.dataset.DatasetAutoFolds at 0x7fa30b60fee0>

#build a dataset

trainset = dataset.build_full_trainset()
list(trainset.all_ratings())

#train the model


from surprise import SVD

svd = SVD()

svd.fit(trainset)

svd.predict(15,1956).est

#validation

from surprise import model_selection

model_selection.cross_validate(svd,dataset,measures=['RMSE','MAE'],cv=5)
