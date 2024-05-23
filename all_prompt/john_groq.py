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
            "content": '''"You are John. 
John is intelligent in financial and also Artificial Intelligent. He can understand everything especially about evaluate Credit Risk Stability.
Giving features and their descriptions. John has to group some features for aggregate and providing what one statistic value(mean, median, mode, max, etc.) using for aggregation each group with the reasons. 
Some features can use alone or some useless.
Now, I present role you on John.
If you understand ,pls response with only  "pom John เมียเช่า"'''
        },
        # Set a user message for the assistant to respond to.
        {
            "role": "user",
            "content": '''actualdpd_943P
 description : Days Past Due (DPD) of previous contract (actual).
annuity_853A
 description : Monthly annuity for previous applications.
cancelreason_3545846M
 description : Application cancellation reason.
creationdate_885D
 description : Date when previous application was created.
credacc_credlmt_575A
 description : Credit card credit limit provided for previous applications.
credamount_590A
 description : Loan amount or card limit of previous applications.
credtype_587L
 description : Credit type of previous application.
district_544M
 description : District of the address used in the previous loan application.
downpmt_134A
 description : Previous application downpayment amount.
education_1138M
 description : Applicant's education level from their previous application.
inittransactioncode_279L
 description : Type of the initial transaction made in the previous application of the client.
isbidproduct_390L
 description : Flag for determining if the product is a cross-sell in previous applications.
postype_4733339M
 description : Type of point of sale.
profession_152M
 description : Profession of the client during their previous loan application.
rejectreason_755M
 description : Reason for previous application rejection.
rejectreasonclient_4145042M
 description : Reason for rejection of the client's previous application.
status_219L
 description : Previous application status.
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
    temperature=0.3,

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