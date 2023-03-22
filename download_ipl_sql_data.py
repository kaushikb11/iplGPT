import os
import opendatasets as od

kaggle_sql_data_url = "https://www.kaggle.com/datasets/harsha547/ipldatabase"

if __name__ == "__main__":
    # First we will check if the repo has kaggle.json file
    # Read more here: https://github.com/JovianHQ/opendatasets/blob/master/README.md#kaggle-credentials
    if not os.path.exists("kaggle.json"):
        raise FileNotFoundError(
            "kaggle.json not found. Follow the link: https://github.com/JovianHQ/opendatasets/blob/master/README.md#kaggle-credentials to get your copy of kaggle.json file"
        )
    try:
        od.download(kaggle_sql_data_url)
    except Exception as e:
        raise e
