class Aggregator:
    def address_features(df):
        addr_district_mode = pl.mode(df['addres_district_368M']).alias('mode_addres_district_368M')
        addr_zip_mode = pl.mode(df['addres_zip_823M']).alias('mode_addres_zip_823M')
        return [addr_district_mode, addr_zip_mode]

    def contact_role_feature(df):
        conts_role_mode = pl.mode(df['conts_role_79M']).alias('mode_conts_role_79M')
        return [conts_role_mode]

    def employment_features(df):
        empls_economicalst_mode = pl.mode(df['empls_economicalst_849M']).alias('mode_empls_economicalst_849M')
        empls_employer_name_mode = pl.mode(df['empls_employer_name_740M']).alias('mode_empls_employer_name_740M')
        return [empls_economicalst_mode, empls_employer_name_mode]

    def get_exprs(df):
        exprs = Aggregator.address_features(df) + \
                Aggregator.contact_role_feature(df) + \
                Aggregator.employment_features(df)
        return exprs
