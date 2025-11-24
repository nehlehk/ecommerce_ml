from pathlib import Path
import pandas as pd
import logging

logger = logging.getLogger(__name__)

PROJECT_DIR = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_DIR / "data"/ "raw"

def load_orders() -> pd.DataFrame:
    """Load orders data from a CSV file."""
    path = DATA_DIR / "olist_orders_dataset.csv"
    logger.info(f"Loading orders data from %s" , path)
    df = pd.read_csv(path)

    if df.empty:
        logger.warning("Orders data is empty.")
    else:
        logger.info(f"Loaded %d records from orders data." , len(df))

    return df


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    orders_df = load_orders()
    print(orders_df.head())
    print(orders_df.shape)