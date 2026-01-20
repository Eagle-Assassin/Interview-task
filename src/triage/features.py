import pandas as pd

def process_features():

    records=pd.read_csv("data/InterviewTask/AI/records.csv")
    #take the first 2000 rows
    records_copy=records.loc[0:1500].copy()

    #Drop columns ['received_at','free_text_summary', 'handler_notes', 'historical_outcome']
    records_copy.drop(['received_at','free_text_summary', 'handler_notes'],axis=1,inplace=True)

    #Replace null service_line with no data available
    records_copy['service_line'].fillna("No data Available", inplace=True)

    #Replace null client segment with no data available
    records_copy['client_segment'].fillna("No data Available", inplace=True)

    #Drop the cases without any case ids
    records_copy.drop(records_copy.loc[records_copy["case_id"].isna()].index,axis=0,inplace=True)

    #Replace null Jurisdiction with no data available
    records_copy['jurisdiction'].fillna("No data Available", inplace=True)

    #Replace the Null values in claim_value_band to Unknown
    records_copy['claim_value_band'].fillna("Unknown", inplace=True)

    #Replace Null values in the Attachment Present to False
    records_copy['attachments_present'].fillna(False, inplace=True)

    #Replace Null values in the historical_outcome to Unknown
    records_copy['historical_outcome'].fillna("Unknown", inplace=True)

    def covert_to_yesno(value):
        if value:
            return ("yes")
        else:
            return ("No")
    #Convert Attachment Present to Yes No 
    records_copy['attachments_present']=records_copy['attachments_present'].apply(covert_to_yesno)
    print("Null values and unwanted columns handled successfully")

    #Initialise a null dataframe
    COLUMNS = ['case_id','severe_legal_or_regulatory_risk','business_critical_impact','potential_fraud','conflicting_information','complex_incident_details','policy_interpretation_issues','legal_disputes','jurisdictional_complexity','coverage_terms_unclear','exclusions_may_apply','new_or_unusual_claim_type','no_legal_or_fraud_concerns','unclear_incident_description','claim_invalid_or_fraudulent','required_conditions_not_met','risk_summary']
    df_all_signals = pd.DataFrame(columns=COLUMNS)

    #load all the output csv files from the llm and merge it with the base dataset
    for i in range(1,4):
        df=pd.read_csv(f"data/llm_out{i}.0.csv")
        df_all_signals = pd.concat( [df_all_signals, df],ignore_index=True)
    
    print("The llm outputs are merged to a single dataframe")

    #merge the two dataframes
    processed_df=pd.merge(records_copy, df_all_signals, on="case_id", how="left")
    print("preprocessed dataset and the llm output merged successfully")

    #Save the processed data
    processed_df.to_csv('data/processeddata/processeddf.csv',index=False)
    print("Processed data saved to local Success fully")

