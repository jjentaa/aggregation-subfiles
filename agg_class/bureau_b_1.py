class Aggregator:
    def contract_info_aggregations(df):
        exprs = [
            pl.mean(df['contractmaturitydate_151D'] - df['contractdate_551D']).alias('avg_contract_duration'),
            pl.median(df['contractmaturitydate_151D'] - df['contractdate_551D']).alias('median_contract_duration')
        ]
        return exprs
    
    def creditor_info_aggregations(df):
        exprs = [
            pl.mode(df['credor_3940957M']).alias('most_frequent_creditor')
        ]
        return exprs
    
    def debt_info_aggregations(df):
        exprs = [
            pl.max(df['dpdmax_851P']).alias('max_past_due_days'),
            pl.max(df['overdueamountmax_950A']).alias('max_past_due_amount')
        ]
        return exprs
    
    def payment_info_aggregations(df):
        exprs = [
            pl.mode(df['pmtmethod_731M']).alias('most_common_payment_method')
        ]
        return exprs
    
    def purpose_info_aggregations(df):
        exprs = [
            pl.mode(df['purposeofcred_722M']).alias('predominant_credit_purpose')
        ]
        return exprs
    
    def subject_role_info_aggregations(df):
        exprs = [
            pl.mode(df['subjectrole_326M']).alias('most_common_subject_role_active'),
            pl.mode(df['subjectrole_43M']).alias('most_common_subject_role_closed')
        ]
        return exprs
    
    def get_exprs(df):
        exprs = Aggregator.contract_info_aggregations(df) + \
                Aggregator.creditor_info_aggregations(df) + \
                Aggregator.debt_info_aggregations(df) + \
                Aggregator.payment_info_aggregations(df) + \
                Aggregator.purpose_info_aggregations(df) + \
                Aggregator.subject_role_info_aggregations(df)

        return exprs
