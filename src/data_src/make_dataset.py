""" Make imports  """
import pandas as pd

def generate_dataset_base() -> pd.DataFrame:
    """
    Reads a CSV file and modifies a dataset for the mining process flotation plant, chanding the date format.

    Returns:
        pandas.DataFrame: The created dataset.
    """

    data = pd.read_csv(r"data\raw\MiningProcess_Flotation_Plant_Database.csv",decimal=",")
    dataset = data.copy()
    dataset["date"] = pd.to_datetime(dataset["date"])
    return dataset.to_csv("data\interim\MiningProcess_Flotation_Plant_Database.csv", index=False)


