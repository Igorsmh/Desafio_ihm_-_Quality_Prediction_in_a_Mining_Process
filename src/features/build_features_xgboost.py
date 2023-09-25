""" imports """
import pandas as pd


def generate_time(dataframe) -> pd.DataFrame:
    """
   Generate a week column in the dataset based on the date column.
   
   Parameters:
       dataset (pd.DataFrame): The input dataset.
   
   Returns:
       pd.DataFrame: The dataset with an additional "Dia_da_semana" column.
   """
    dataframe.index = pd.to_datetime(dataframe.index)
    dataframe['hora'] = dataframe.index.hour
    dataframe['dia_da_semana'] = dataframe.index.dayofweek
    dataframe['mes'] = dataframe.index.month
    dataframe['trimestre'] = dataframe.index.quarter
    dataframe['ano'] = dataframe.index.year
    dataframe['dia_do_ano'] = dataframe.index.dayofyear
    dataframe['dia_do_mes'] = dataframe.index.day
    dataframe['semana_do_ano'] = dataframe.index.isocalendar().week




    return  dataframe


def generate_dataset_train(dataframe) -> pd.DataFrame:
    """
	Generate a training dataset from the given dataframe.

	Parameters:
	- dataframe (pd.DataFrame): The input dataframe.

	Returns:
	- pd.DataFrame: The generated training dataset.
	"""

    dataframe_modified = dataframe.copy()
    dataframe_modified['% Silica Concentrate'] = dataframe_modified['% Silica Concentrate'].round(2)
    dataframe_modified = dataframe_modified.drop_duplicates(["% Iron Feed","% Silica Feed"])
    return  dataframe_modified


def generate_lag (dataframe)-> pd.DataFrame:
    """
	Create a lagged version of a column "% Silica Concentrate".
	
	:param dataframe: The input DataFrame.
	:return: The lagged DataFrame with one row shifted up.
	"""

    dataframe["% Silica_Concentrate_anterior"] = dataframe["% Silica Concentrate"].shift(1)
    return dataframe
