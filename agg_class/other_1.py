class Aggregator:
    def debit_card_transactions(df):
        incoming_col = "amtdebitincoming_4809443A"
        outgoing_col = "amtdebitoutgoing_4809440A"
        incoming_sum = pl.sum(pl.when(pl.col(incoming_col) > 0, pl.col(incoming_col)).otherwise(0)).alias(f"sum_{incoming_col}")
        outgoing_sum = pl.sum(pl.when(pl.col(outgoing_col) > 0, pl.col(outgoing_col)).otherwise(0)).alias(f"sum_{outgoing_col}")
        return [incoming_sum, outgoing_sum]

    def deposit_transactions(df):
        incoming_col = "amtdepositincoming_4809444A"
        outgoing_col = "amtdepositoutgoing_4809442A"
        incoming_sum = pl.sum(pl.when(pl.col(incoming_col) > 0, pl.col(incoming_col)).otherwise(0)).alias(f"sum_{incoming_col}")
        outgoing_sum = pl.sum(pl.when(pl.col(outgoing_col) > 0, pl.col(outgoing_col)).otherwise(0)).alias(f"sum_{outgoing_col}")
        return [incoming_sum, outgoing_sum]

    def deposit_balance(df):
        balance_col = "amtdepositbalance_4809441A"
        median_balance = pl.median(balance_col).alias(f"median_{balance_col}")
        return [median_balance]

    def get_exprs(df):
        exprs = Aggregator.debit_card_transactions(df) + \
                Aggregator.deposit_transactions(df) + \
                Aggregator.deposit_balance(df)
        return exprs
