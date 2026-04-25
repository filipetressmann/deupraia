import pandas as pd

def explode_on(df, args):
    return df.explode(args["column"])

def split_on(df, args):
    df[args["output"]] = df[args["column"]].str.split(args["split_string"], expand=args["expand"])
    return df

def from_timestampms_to_datetime(df, args):
    df[args["field"]] = pd.to_datetime(
        df[args["field"]], unit="ms"
    ).dt.strftime("%d/%m/%Y")
    return df

def normalize_column(df, args):
    df_clean = df.reset_index(drop=True)
    normalized_column_df = pd.json_normalize(df_clean[args["column"]]).reset_index(drop=True)

    return pd.concat(
        [df_clean.drop(columns=[args["column"]]), normalized_column_df],
        axis=1
    )