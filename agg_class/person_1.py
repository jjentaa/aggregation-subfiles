import polars as pl

class Aggregator:
    @staticmethod
    def address_expr(df):
        address_cols = [col for col in df.columns if "addr" in col]
        expr_mode = [pl.mode(col).alias(f"mode_{col}") for col in address_cols]
        return expr_mode

    @staticmethod
    def personal_info_expr(df):
        categorical_cols = [col for col in df.columns if col[-1] in ("M", "L")]
        numerical_cols = [col for col in df.columns if col[-1] == "L" and col != "personindex_1023L"]

        expr_mode = [pl.mode(col).alias(f"mode_{col}") for col in categorical_cols]
        expr_median = [pl.median(col).alias(f"median_{col}") for col in numerical_cols]

        return expr_mode + expr_median

    def get_exprs(df):
        exprs = Aggregator.address_expr(df) + \
                Aggregator.personal_info_expr(df)

        return exprs
