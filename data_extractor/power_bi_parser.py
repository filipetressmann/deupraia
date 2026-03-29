import pandas as pd

def parse_power_bi_data(bi_rows, num_cols=5):
    rows = []
    prev_row = [None] * num_cols
    for row in bi_rows:
        C = row.get("C", [])
        R = row.get("R", 0)

        new_row = prev_row.copy()
        c_idx = 0

        for col_idx in range(num_cols):
            # Check if this column should be reused (bit = 1)
            if (R >> col_idx) & 1:
                continue
            else:
                if c_idx < len(C):
                    new_row[col_idx] = C[c_idx]
                    c_idx += 1
                    
        rows.append(new_row)
        prev_row = new_row

    return rows