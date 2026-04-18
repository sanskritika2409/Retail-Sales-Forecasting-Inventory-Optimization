import numpy as np
from scipy.stats import norm

def calculate_inventory(df, lead_time=7, service_level=0.95):
    df = df.copy()

    z = norm.ppf(service_level)

    df['demand_std'] = df.groupby(['store','product'])['prediction'].transform('std')

    df['safety_stock'] = z * df['demand_std'] * np.sqrt(lead_time)

    df['rop'] = (df['prediction'] * lead_time) + df['safety_stock']

    df['order_qty'] = df['rop'] - df['stock']
    df['order_qty'] = df['order_qty'].apply(lambda x: max(x, 0))

    print("✅ Advanced Inventory Calculated")
    return df
