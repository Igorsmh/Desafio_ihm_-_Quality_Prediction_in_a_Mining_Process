import pandas as pd


def generate_week() -> pd.DataFrame:
    """
    Generate a week dataset from the MiningProcess_Flotation_Plant_Database.

    Returns:
        pd.DataFrame: The dataset with the day name.
    """

    dataset_semana = pd.read_csv(r"data\interim\MiningProcess_Flotation_Plant_Database.csv",decimal=",")

    dataset_semana["Dia_da_semana"] = dataset_semana["date"].dt.day_name()
    return  dataset_semana.to_csv("data\processed\dataset_semana.csv", index=False)