import polars as pl

class Aggregator:
    @staticmethod
    def demographic_expr(df):
        cols = [
            'birth_259D', 'birthdate_87D', 'gender_992L', 'sex_738L', 'childnum_185L',
            'education_927M', 'familystate_447L', 'maritalst_703L'
        ]
        exprs = []
        for col in cols:
            if col in ['birth_259D', 'birthdate_87D']:
                exprs.append(pl.col(col).max().alias(f"max_{col}"))
                exprs.append(pl.col(col).min().alias(f"min_{col}"))
                exprs.append((pl.col(col).max() - pl.col(col).min()).alias(f"range_{col}"))
            else:
                exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
                exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def employment_expr(df):
        cols = [
            'empl_employedfrom_271D', 'empl_employedtotal_800L', 'empl_industry_691L',
            'mainoccupationinc_384A'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mean().alias(f"mean_{col}"))
            exprs.append(pl.col(col).median().alias(f"median_{col}"))
            exprs.append(pl.col(col).max().alias(f"max_{col}"))
            exprs.append(pl.col(col).min().alias(f"min_{col}"))
        return exprs

    @staticmethod
    def address_expr(df):
        cols = [
            'contaddr_district_15M', 'contaddr_zipcode_807M', 'empladdr_district_926M',
            'empladdr_zipcode_114M', 'registaddr_district_1083M', 'registaddr_zipcode_184M'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def relationship_expr(df):
        cols = [
            'isreference_387L', 'relationshiptoclient_415T', 'relationshiptoclient_642T',
            'type_25L', 'role_1084L', 'role_993L'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def housing_expr(df):
        cols = ['housetype_905L', 'housingtype_772L']
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def income_remittance_expr(df):
        cols = ['incometype_1044T', 'remitter_829L']
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def miscellaneous_expr(df):
        cols = [
            'contaddr_matchlist_1032L', 'contaddr_smempladdr_334L', 'persontype_1072L', 
            'persontype_792L', 'language1_981M', 'personindex_1023L', 
            'safeguarantyflag_411L'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs
    
    @staticmethod
    def demographic_expr(df):
        cols = [
            'birth_259D', 'birthdate_87D', 'gender_992L', 'sex_738L', 'childnum_185L',
            'education_927M', 'familystate_447L', 'maritalst_703L'
        ]
        exprs = []
        for col in cols:
            if col in ['birth_259D', 'birthdate_87D']:
                exprs.append(pl.col(col).max().alias(f"max_{col}"))
                exprs.append(pl.col(col).min().alias(f"min_{col}"))
                exprs.append((pl.col(col).max() - pl.col(col).min()).alias(f"range_{col}"))
            else:
                exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
                exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def employment_expr(df):
        cols = [
            'empl_employedfrom_271D', 'empl_employedtotal_800L', 'empl_industry_691L',
            'mainoccupationinc_384A'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mean().alias(f"mean_{col}"))
            exprs.append(pl.col(col).median().alias(f"median_{col}"))
            exprs.append(pl.col(col).max().alias(f"max_{col}"))
            exprs.append(pl.col(col).min().alias(f"min_{col}"))
        return exprs

    @staticmethod
    def address_expr(df):
        cols = [
            'contaddr_district_15M', 'contaddr_zipcode_807M', 'empladdr_district_926M',
            'empladdr_zipcode_114M', 'registaddr_district_1083M', 'registaddr_zipcode_184M'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def relationship_expr(df):
        cols = [
            'isreference_387L', 'relationshiptoclient_415T', 'relationshiptoclient_642T',
            'type_25L', 'role_1084L', 'role_993L'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def housing_expr(df):
        cols = ['housetype_905L', 'housingtype_772L']
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def income_remittance_expr(df):
        cols = ['incometype_1044T', 'remitter_829L']
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def miscellaneous_expr(df):
        cols = [
            'contaddr_matchlist_1032L', 'contaddr_smempladdr_334L', 'persontype_1072L', 
            'persontype_792L', 'language1_981M', 'personindex_1023L', 
            'safeguarantyflag_411L'
        ]
        exprs = []
        for col in cols:
            exprs.append(pl.col(col).mode().alias(f"mode_{col}"))
            exprs.append(pl.col(col).value_counts().alias(f"freq_counts_{col}"))
        return exprs

    @staticmethod
    def get_exprs(df):
        exprs = Aggregator.demographic_expr(df) + \
                Aggregator.employment_expr(df) + \
                Aggregator.address_expr(df) + \
                Aggregator.relationship_expr(df) + \
                Aggregator.housing_expr(df) + \
                Aggregator.income_remittance_expr(df) + \
                Aggregator.miscellaneous_expr(df) + \
                Aggregator.demographic_expr(df) + \
                Aggregator.employment_expr(df) + \
                Aggregator.address_expr(df) + \
                Aggregator.relationship_expr(df) + \
                Aggregator.housing_expr(df) + \
                Aggregator.income_remittance_expr(df) + \
                Aggregator.miscellaneous_expr(df)
        return exprs
