from future import annotations
import logging
from typing import Iterable
import pandas as pd

logger = logging.getLogger(__name__)

def filter_deliverd_orders(df: pd.DataFrame) -> pd.DataFrame:
    """Filter the DataFrame to include only delivered orders."""
    if 'order_status' not in df.columns:
        logger.error("DataFrame does not contain 'order_status' column.")
        raise ValueError("Missing 'order_status' column in DataFrame.")
    
    before = len(df)
    df_filtered = df[df['order_status'] == 'delivered'].copy()
    after = len(df_filtered)

    logger.info(f"Filtered orders: {before} -> {after} (delivered only)")
    return df_filtered

def add_order_datatime(df: pd.DataFrame) -> pd.DataFrame:
    """Convert order_purchase_timestamp to datetime."""
    if 'order_purchase_timestamp' not in df.columns:
        logger.error("DataFrame does not contain 'order_purchase_timestamp' column.")
        raise ValueError("Missing 'order_purchase_timestamp' column in DataFrame.")
    
    df = df.copy()
    df["order_purchase_dt"] = pd.to_datetime(df["order_purchase_timestamp"])
    return df

def add_time_features(df: pd.DataFrame, time_col: str) -> pd.DataFrame:
    """Add time-based features from a datetime column."""
    if time_col not in df.columns:
        logger.error(f"DataFrame does not contain '{time_col}' column.")
        raise ValueError(f"Missing '{time_col}' column in DataFrame.")
    
    df = df.copy()
    df[f"{time_col}_year"] = df[time_col].dt.year
    df[f"{time_col}_month"] = df[time_col].dt.month
    df[f"{time_col}_day"] = df[time_col].dt.day
    df[f"{time_col}_dayofweek"] = df[time_col].dt.dayofweek
    df[f"{time_col}_hour"] = df[time_col].dt.hour

    logger.info(f"Added time features based on '{time_col}'")
    return df
