import pandas as pd

def make_dataset() -> pd.DataFrame:
    """
    Reads a CSV file and creates a dataset for the mining process flotation plant.

    Returns:
        pandas.DataFrame: The created dataset.
    """

    df = pd.read_csv(r"data\raw\MiningProcess_Flotation_Plant_Database.csv",decimal=",")
    dataset = df.copy()
    dataset["date"] = pd.to_datetime(dataset["date"])
    
    return dataset.to_csv("data\interim\MiningProcess_Flotation_Plant_Database.csv", index=False)
