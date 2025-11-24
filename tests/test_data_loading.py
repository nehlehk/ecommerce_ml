import sys
from pathlib import Path

# Add project root to Python path so 'ecommerce_ml' can be imported
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(PROJECT_ROOT))


from ecommerce_ml.data_loading import load_orders
import pandas as pd

def test_load_orders():
    df = load_orders()
    assert isinstance(df, pd.DataFrame)
    assert len(df) > 0