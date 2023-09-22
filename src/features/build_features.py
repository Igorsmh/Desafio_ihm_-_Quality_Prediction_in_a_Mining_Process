""" imports """
import pandas as pd


def generate_week(dataframe) -> pd.DataFrame:
    """
   Generate a week column in the dataset based on the date column.
   
   Parameters:
       dataset (pd.DataFrame): The input dataset.
   
   Returns:
       pd.DataFrame: The dataset with an additional "Dia_da_semana" column.
   """
    dataframe["Dia_da_semana"] = dataframe["date"].dt.day_name()
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

    dataframe["%Silica_Concentrate_anterior"] = dataframe["% Silica Concentrate"].shift(1)
    return dataframe
