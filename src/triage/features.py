import pandas as pd

def process_features():

    #load the pre-processed data
    records_copy=pd.read_csv('data/pre-processeddata/preprocessed_data.csv')
   

    #Initialise a null dataframe
    COLUMNS = ["case_id","severe_legal_or_regulatory_risk","business_critical_impact","potential_fraud","conflicting_information","complex_incident_details","policy_interpretation_issues","legal_disputes","jurisdictional_complexity","coverage_terms_unclear","exclusions_may_apply","new_or_unusual_claim_type","unclear_incident_description","claim_invalid_or_fraudulent","required_conditions_not_met","has_regulator_involvement","has_cross_border_elements","has_time_sensitivity","has_missing_documentation","mentions_fraud_or_arson","risk_summary" ]
    df_all_signals = pd.DataFrame(columns=COLUMNS)

    #load all the output csv files from the llm and merge it with the base dataset
    for i in range(1,(len(records_copy)//500)+2):
        print(i)
        df=pd.read_csv(f"data/llmdata/llm_out{i}.csv")
        df_all_signals = pd.concat( [df_all_signals, df],ignore_index=True)
    
    print("The llm outputs are merged to a single dataframe")

    #merge the two dataframes
    processed_df=pd.merge(records_copy, df_all_signals, on="case_id", how="left")
    print("preprocessed dataset and the llm output merged successfully")

    #Save the processed data
    processed_df.to_csv('data/processeddata/processeddf.csv',index=False)
    print("Processed data saved to local successfully")

