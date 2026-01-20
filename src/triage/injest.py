import pandas as pd
import warnings
from src.triage.model import GetFromLlm
warnings.filterwarnings(
    "ignore",
    message="A value is trying to be set on a copy of a DataFrame",
    category=FutureWarning
)




def preprocess_getstructrureddata(path):
        
        # Load the datasets
        records=pd.read_csv(path) #"data/InterviewTask/AI/records.csv"
        print("Data loaded successfully")

        #load the model class
        llm=GetFromLlm()
        
        # #Initialize a list to store the lists of  output from the llm as a single row
        # col_data=[]
        # k=0
        
        # for i in range(0,len(records)):
            

        #     #prepare the input data for prompt
        #     input_data= f"caseid:{records['case_id'].loc[i]}; Summary: {records['free_text_summary'].loc[i]}; handler_notes : {records['free_text_summary'].loc[i]}; historical outcome: {records['historical_outcome'].loc[i]}; has attachment:  {records['attachments_present'].loc[i]} "
            
        #     # print(input_data)
            
        #     #llm call to retrieve the generated results
        #     try:
        #         data=llm.generate_details(input_data)
        #         print(f"row {i} data sent to LLM for structured extraction ")
        #     except Exception as E:
        #         print(f"row {i} data extraction failed due to {E}")   
        #     # print(data)
        #     col_data.append(data)

            
        #     #broken into batches to handle huge dataset
        #     if (i%500==0) and (i!=0):
        #         k +=1
        #         print(i)
                
        #         df = pd.DataFrame([r.model_dump() for r in col_data])
        #         df.to_csv(f"data/llmdata/llm_out{k}.csv",index=False)
        #         print(f"{k} records saved after extraction")
        #         col_data=[]
        #     elif(i+1==len(records)):
        #         k +=1
        #         print(i)                
        #         df = pd.DataFrame([r.model_dump() for r in col_data])
        #         df.to_csv(f"data/llmdata/llm_out{k}.csv",index=False)
        #         print(f"{k} records saved after extraction")

        print("LLM data generated successfully")
        
        #Processing the input data
        records_copy=records.loc[0:len(records)].copy()

        #Drop columns ['received_at','free_text_summary', 'handler_notes', 'historical_outcome']
        records_copy.drop(['received_at','free_text_summary', 'handler_notes'],axis=1,inplace=True)

        #Replace null service_line with no data available
        records_copy['service_line'].fillna("No data Available", inplace=True)

        #Replace null client segment with no data available
        records_copy['client_segment'].fillna("No data Available", inplace=True)

        #Drop the cases without any case ids
        records_copy.drop(records_copy.loc[records_copy["case_id"].isna()].index,axis=0,inplace=True)
        print("Missing caseid rows are removed successfully")

        #Replace null Jurisdiction with no data available
        records_copy['jurisdiction'].fillna("No data Available", inplace=True)

        #Replace the Null values in claim_value_band to Unknown
        records_copy['claim_value_band'].fillna("Unknown", inplace=True)

        #Replace Null values in the Attachment Present to False
        records_copy['attachments_present'].fillna(False, inplace=True)

        #Replace Null values in the historical_outcome to Unknown
        records_copy['historical_outcome'].fillna("Unknown", inplace=True)
        print("Null values and unwanted columns handled successfully")

        def covert_to_yesno(value):
            if value:
                return ("yes")
            else:
                return ("No")
        #Convert Attachment Present to Yes No 
        records_copy['attachments_present']=records_copy['attachments_present'].apply(covert_to_yesno)
        print("Data Preprocessed successfully")

        records_copy.to_csv('data/pre-processeddata/preprocessed_data.csv',index=False)
        print("Preprocessed data saved to local successfully")