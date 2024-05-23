import polars as pl

class Aggregator:
    # Financial Attributes
    @staticmethod
    def financial_expr():
        cols = ["annuity_853A", "credacc_credlmt_575A", "credamount_590A", "downpmt_134A"]
        expr_mean = [pl.col(col).mean().alias(f"mean_{col}") for col in cols]
        expr_median = [pl.col(col).median().alias(f"median_{col}") for col in cols]
        return expr_mean + expr_median
    
    # Application Attributes
    @staticmethod
    def application_expr():
        cols = ["credtype_587L", "status_219L", "isbidproduct_390L", "inittransactioncode_279L"]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode
    
    # Date and Time
    @staticmethod
    def date_expr():
        cols = ["creationdate_885D"]
        expr_max = [pl.col(col).max().alias(f"max_{col}") for col in cols]
        expr_min = [pl.col(col).min().alias(f"min_{col}") for col in cols]
        return expr_max + expr_min
    
    # Application Outcome Reasons
    @staticmethod
    def outcome_reason_expr():
        cols = ["rejectreason_755M", "rejectreasonclient_4145042M", "cancelreason_3545846M"]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode
    
    # Client Demographics
    @staticmethod
    def demographics_expr():
        cols = ["education_1138M", "profession_152M", "district_544M"]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode
    
    # Other Attributes
    @staticmethod
    def other_expr():
        cols = ["postype_4733339M"]
        expr_mode = [pl.col(col).mode().alias(f"mode_{col}") for col in cols]
        return expr_mode
    
    @staticmethod
    def get_exprs():
        exprs = Aggregator.financial_expr() + \
                Aggregator.application_expr() + \
                Aggregator.date_expr() + \
                Aggregator.outcome_reason_expr() + \
                Aggregator.demographics_expr() + \
                Aggregator.other_expr()
        
        return exprs

# Example usage
# df = pl.DataFrame(...)
# aggregated_df = df.select(Aggregator.get_exprs())
