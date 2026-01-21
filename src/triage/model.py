import logging
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from schema.modeloutput import ClaimRiskSignals

# Load environment variables
load_dotenv()

logger = logging.getLogger(__name__)


class GetFromLlm:
    def __init__(self):
        logger.info("Initializing LLM client")

        try:
            self.model = ChatOpenAI(model="gpt-4o-mini")
            logger.info("ChatOpenAI model initialized successfully | model=gpt-4o-mini")
        except Exception as exc:
            logger.critical(
                "Failed to initialize ChatOpenAI model",
                exc_info=True,
            )
            raise

    # -----------------------------------------------------

    def generate_details(self, input_data: str) -> ClaimRiskSignals:
        logger.info("Starting LLM risk signal extraction")

        # Initialize the output parser
        parser = PydanticOutputParser(pydantic_object=ClaimRiskSignals)
        logger.debug("Pydantic output parser initialized")

        # Prepare prompt
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
                "{format_instructions}"
            ),
            input_variables=["input_data"],
            partial_variables={
                "format_instructions": parser.get_format_instructions()
            },
        )

        logger.debug("Prompt template constructed")

        # Build chain
        chain = prompt | self.model | parser
        logger.debug("LLM execution chain created")

        # Invoke chain
        try:
            logger.info("Invoking LLM chain")
            output = chain.invoke({"input_data": input_data})

            logger.info(
                "LLM response parsed successfully | case_id=%s",
                getattr(output, "case_id", "unknown"),
            )

            return output

        except Exception as exc:
            logger.error(
                "LLM invocation or parsing failed",
                exc_info=True,
            )
            raise
