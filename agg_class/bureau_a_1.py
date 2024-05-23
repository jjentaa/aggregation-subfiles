import polars as pl

class Aggregator:
    @staticmethod
    def classification_expr(df):
        cols = [col for col in df.columns if col.startswith("classificationofcontr")]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode

    @staticmethod
    def contract_status_expr(df):
        cols = [col for col in df.columns if col.startswith("contractst")]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode

    @staticmethod
    def financial_institution_expr(df):
        cols = [col for col in df.columns if col.startswith("financialinstitution")]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode

    @staticmethod
    def purpose_of_credit_expr(df):
        cols = [col for col in df.columns if col.startswith("purposeofcred")]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode

    @staticmethod
    def subject_role_expr(df):
        cols = [col for col in df.columns if col.startswith("subjectrole")]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode

    @staticmethod
    def get_exprs(df):
        exprs = Aggregator.classification_expr(df) + \
                Aggregator.contract_status_expr(df) + \
                Aggregator.financial_institution_expr(df) + \
                Aggregator.purpose_of_credit_expr(df) + \
                Aggregator.subject_role_expr(df)
        
        return exprs

# Example usage:
# df = pl.DataFrame(...)
# aggregated_df = df.select(Aggregator.get_exprs(df))
