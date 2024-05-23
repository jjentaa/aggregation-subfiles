from groq import Groq

client = Groq(api_key='your_api_key')

chat_completion = client.chat.completions.create(
    #
    # Required parameters
    #
    messages=[
        # Set an optional system message. This sets the behavior of the
        # assistant and can be used to provide specific instructions for
        # how it should behave throughout the conversation.
        {
            "role": "system",
            "content": """Jeremy is expert in coding the Aggregation function with polars. Jeremy hate using pandas. 
            Users will give the concept of Aggregation function. Jeremy has to provide the Aggregation function in python.
            If the represented statistic value more than one, generate all possible function. 
            If Jeremy have to sum value, pls note that the value must be positive first.
            Jeremy is scrupulous person. No features missing from his sight.
            
'''
class Aggregator:
    #Please add or subtract features yourself, be aware that too many features will take up too much space.
    def num_expr(df):
        cols = [col for col in df.columns if col[-1] in ("P", "A")]
        expr_max = [pl.max(col).alias(f"max_{col}") for col in cols]
        return expr_max
    
    def date_expr(df):
        cols = [col for col in df.columns if col[-1] in ("D")]
        expr_max = [pl.max(col).alias(f"max_{col}") for col in cols]
        return  expr_max
    
    def str_expr(df):
        cols = [col for col in df.columns if col[-1] in ("M",)]
        expr_max = [pl.max(col).alias(f"max_{col}") for col in cols]
        return  expr_max
    
    def other_expr(df):
        cols = [col for col in df.columns if col[-1] in ("T", "L")]
        expr_max = [pl.max(col).alias(f"max_{col}") for col in cols]
        return  expr_max 
    
    def count_expr(df):
        cols = [col for col in df.columns if "num_group" in col]
        expr_max = [pl.max(col).alias(f"max_{col}") for col in cols] 
        return  expr_max
    
    def get_exprs(df):
        exprs = Aggregator.num_expr(df) + \
                Aggregator.date_expr(df) + \
                Aggregator.str_expr(df) + \
                Aggregator.other_expr(df) + \
                Aggregator.count_expr(df)

        return exprs
'''
"""
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": '''
            **1. Financial Features:**

- **credamount_590A (Mean, Median, Max)**: To assess the average, middle value, and highest loan amount or card limit of previous applications.
- **annuity_853A (Mean)**: To measure the average monthly annuity for previous applications.
- **downpmt_134A (Mean)**: To determine the average down payment amount for previous applications.

**2. Applicant Information:**

- **education_1138M (Mode)**: To identify the most common education level among previous applicants.
- **profession_152M (Mode)**: To determine the most frequent profession of previous applicants.

**3. Application Information:**

- **cancelreason_3545846M (Frequency)**: To count the number of applications canceled for each reason.
- **rejectreason_755M (Frequency)**: To count the number of applications rejected for each reason.
- **rejectreasonclient_4145042M (Frequency)**: To count the number of applications rejected due to client-related factors.

**4. Credit Information:**

- **credacc_credlmt_575A (Mean)**: To assess the average credit limit provided for previous applications.

**5. Additional Features:**

- **creationdate_885D (Mean)**: To determine the average time since the previous application was created.
- **isbidproduct_390L (Proportion)**: To calculate the proportion of previous applications that were cross-sells.

**Unuseful Features:**

- **postype_4733339M**: This feature is not relevant to credit risk stability evaluation.
- **district_544M**: This feature may not be useful as it does not directly relate to credit risk.
''',
        }
    ],

    # The language model which will generate the completion.
    model="Gemma-7b-It",

    #
    # Optional parameters
    #

    # Controls randomness: lowering results in less random completions.
    # As the temperature approaches zero, the model will become deterministic
    # and repetitive.
    temperature=0.2,

    # The maximum number of tokens to generate. Requests can use up to
    # 32,768 tokens shared between prompt and completion.
    max_tokens=1024,

    # A stop sequence is a predefined or user-specified text string that
    # signals an AI to stop generating content, ensuring its responses
    # remain focused and concise. Examples include punctuation marks and
    # markers like "[end]".
    stop=None,

    # If set, partial message deltas will be sent.
    stream=False,
)

# Print the completion returned by the LLM.
print(chat_completion.choices[0].message.content)