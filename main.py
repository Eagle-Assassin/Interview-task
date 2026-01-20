from src.triage.model import GetFromLlm
import pandas as pd

def get_structured_data():

    llm=GetFromLlm()
    cases=pd.read_csv("./data/InterviewTask/AI/records.csv")

    col_data=[]

    for i in range(2501,10001):
        input_data= f"caseid:{cases['case_id'].loc[i]}; Summary: {cases['free_text_summary'].loc[i]}; handler_notes : {cases['free_text_summary'].loc[i]}; historical outcome: {cases['historical_outcome'].loc[i]}"
        data=llm.generate_details(input_data)
        col_data.append(data)
        if (i%500==0) and (i!=0):
            k = i/500
            print(i)
            
            df = pd.DataFrame([r.model_dump() for r in col_data])
            df.to_csv(f"data/llm_out{k}.csv",index=False)
            col_data=[]
    

get_structured_data()