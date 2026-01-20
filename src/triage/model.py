from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schema.modeloutput import ClaimRiskSignals
# from app.core.logger import logger
# from app.schema.model_output import QAResponse

#load the environment variables
load_dotenv()



# llm= HuggingFacePipeline.from_model_id(model_id="meta-llama/Llama-3.3-70B-Instruct", task="text-generation")



class GetFromLlm():
    def __init__(self):
        # initialisze the model
        # self.llm =HuggingFaceEndpoint(    
        # repo_id="meta-llama/Llama-3.3-70B-Instruct",
        # task="text-generation")

        #load the  model
        # self.model = ChatOpenAI()
        self.model = ChatOpenAI(model="gpt-4o-mini")

        # model= ChatHuggingFace(llm=self.llm)


    def generate_details(self,input_data):

        
        #Initialize the output parsers
        parser=PydanticOutputParser(pydantic_object=ClaimRiskSignals)
        

        #prepare the Dyanamic prompt 
        prompt = PromptTemplate( 

        template=(
        "You are an insurance claim risk analyst.\n\n"
        "Analyze the following claim information and extract risk signals.\n\n"
        "Claim Information:\n"
        "{input_data}\n\n"
        "Rules:\n"
        "- Use ONLY the field names exactly as defined in the schema\n"
        "- Do NOT rename, misspell, or omit any fields\n"
        "- Every field in the schema MUST be present\n"
        "- Use only: 'Yes', 'No', or 'No data available'\n"
        "- Do not assume missing facts\n"
        "- Provide a brief risk_summary (1–2 sentences)\n\n"
        "{format_instructions}" ),    input_variables=["input_data"],    
        partial_variables={"format_instructions": parser.get_format_instructions() }
        
        )

        
        #Initialize the chain
        chain= prompt | self.model | parser

        #invoke the chain with the inputvariables
        output = chain.invoke({"input_data": input_data})

    

        #Return the result
        return (output)