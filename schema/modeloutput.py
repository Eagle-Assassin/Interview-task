from pydantic import BaseModel,Field
from typing import List,Annotated,Optional



#pydantic model to verify the llm output
from enum import Enum

class YesNoUnknown(str, Enum):
    YES = "Yes"
    NO = "No"
    NO_DATA = "No data available"


class ClaimRiskSignals(BaseModel):
    case_id: Annotated[
        str,
        Field(description="Unique identifier for the claim or case.")
    ]

    severe_legal_or_regulatory_risk: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the claim involves severe legal or regulatory risk.")
    ]

    business_critical_impact: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the incident has business-critical impact such as ransomware or major lawsuits.")
    ]

    potential_fraud: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether there are indicators of potential fraud or misrepresentation.")
    ]

    conflicting_information: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether conflicting or inconsistent information is present.")
    ]

    complex_incident_details: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the incident details are complex or require expert interpretation.")
    ]

    policy_interpretation_issues: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether policy wording is ambiguous or requires interpretation.")
    ]

    legal_disputes: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether legal disputes or litigation are involved.",
              alias="legal_disputs")  # 👈 TYPO SAFETY NET
    ]

    jurisdictional_complexity: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether cross-border or legally complex jurisdictions are involved.")
    ]

    coverage_terms_unclear: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether coverage terms are unclear or insufficiently defined.")
    ]

    exclusions_may_apply: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether policy exclusions may apply.")
    ]

    new_or_unusual_claim_type: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the claim is new, rare, or unusual.")
    ]

    no_legal_or_fraud_concerns: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether there are no apparent legal, regulatory, or fraud concerns.")
    ]

    unclear_incident_description: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the incident description is vague or incomplete.")
    ]

    claim_invalid_or_fraudulent: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether the claim appears invalid or fraudulent.")
    ]

    required_conditions_not_met: Annotated[
        YesNoUnknown,
        Field(description="Indicates whether mandatory policy conditions have not been met.")
    ]

    risk_summary: Annotated[
        str,
        Field(
            description="A brief, plain-English summary (1–2 sentences) explaining the main risk factors identified in this claim."
        )
    ]
