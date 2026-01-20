from pydantic import BaseModel,Field
from typing import List,Annotated,Optional



#pydantic model to verify the llm output

from enum import Enum


class YesNoUnknown(str, Enum):
    """Tri-state indicator used when information may be missing or uncertain."""
    YES = "Yes"
    NO = "No"
    NO_DATA = "No data available"


class YesNo(str, Enum):
    """Binary indicator used when information is expected to be clearly present or absent."""
    YES = "Yes"
    NO = "No"


class ClientSegment(str, Enum):
    """Client size classification indicating scale of exposure."""
    SMB = "SMB"
    MID_MARKET = "Mid-Market"
    ENTERPRISE = "Enterprise"
    NO_DATA = "No data Available"


class Jurisdiction(str, Enum):
    """Primary legal or regulatory jurisdiction governing the claim."""
    UK = "UK"
    US = "US"
    EU = "EU"
    OTHER = "Other"
    NO_DATA = "No data Available"


class ServiceLine(str, Enum):
    """Business service line responsible for handling the claim."""
    LEGAL = "Legal"
    INSURANCE = "Insurance"
    ADVISORY = "Advisory"
    NO_DATA = "No data Available"


class ClaimValueBand(str, Enum):
    """Approximate financial exposure represented as a value band."""
    LT_50K = "<50k"
    BAND_50_250K = "50k-250k"
    BAND_250K_1M = "250k-1m"
    GT_1M = ">1m"
    UNKNOWN = "Unknown"


class HistoricalOutcome(str, Enum):
    """Final or most recent known outcome of the claim, if available."""
    SETTLED = "Settled"
    ACCEPTED = "Accepted"
    REJECTED = "Rejected"
    ESCALATED = "Escalated"
    UNKNOWN = "Unknown"



class ClaimInput(BaseModel):
    case_id: str = Field(
        description="Unique identifier for the claim or case, used for tracking and correlation."
    )

    client_segment: ClientSegment = Field(
        description="Client size category, used to estimate scale of financial and operational exposure."
    )

    jurisdiction: Jurisdiction = Field(
        description="Primary jurisdiction whose legal and regulatory framework applies to the claim."
    )

    service_line: ServiceLine = Field(
        description="Service area responsible for handling the claim, indicating level of legal or operational exposure."
    )

    claim_value_band: ClaimValueBand = Field(
        description="Estimated financial value of the claim expressed as a predefined monetary range."
    )

    attachments_present: YesNo = Field(
        description="Indicates whether supporting documents or evidence have been provided with the claim."
    )

    historical_outcome: HistoricalOutcome = Field(
        description="Previously recorded outcome of the claim, if it has already been processed or reviewed."
    )

    severe_legal_or_regulatory_risk: YesNoUnknown = Field(
        description="Indicates whether the claim poses significant legal or regulatory exposure such as fines, penalties, or statutory breaches."
    )

    business_critical_impact: YesNoUnknown = Field(
        description="Indicates whether the incident has caused or may cause major business disruption, such as ransomware or system outages."
    )

    potential_fraud: YesNoUnknown = Field(
        description="Indicates presence of indicators suggesting possible fraud or intentional misrepresentation."
    )

    conflicting_information: YesNoUnknown = Field(
        description="Indicates whether claim details contain inconsistencies or contradictions across sources."
    )

    complex_incident_details: YesNoUnknown = Field(
        description="Indicates whether the incident details are technically or procedurally complex and require expert interpretation."
    )

    policy_interpretation_issues: YesNoUnknown = Field(
        description="Indicates whether policy wording is ambiguous or requires interpretation to determine coverage."
    )

    legal_disputes: YesNoUnknown = Field(
        description="Indicates whether the claim involves ongoing or potential legal disputes or litigation."
    )

    jurisdictional_complexity: YesNoUnknown = Field(
        description="Indicates whether the claim spans multiple jurisdictions or involves complex legal boundaries."
    )

    coverage_terms_unclear: YesNoUnknown = Field(
        description="Indicates whether coverage terms are unclear, incomplete, or insufficient to assess eligibility."
    )

    exclusions_may_apply: YesNoUnknown = Field(
        description="Indicates whether policy exclusions may limit or deny coverage for this claim."
    )

    new_or_unusual_claim_type: YesNoUnknown = Field(
        description="Indicates whether the claim represents a rare, novel, or previously unseen claim type."
    )

    no_legal_or_fraud_concerns: YesNoUnknown = Field(
        description="Indicates explicit confirmation that no legal, regulatory, or fraud-related concerns are present."
    )

    unclear_incident_description: YesNoUnknown = Field(
        description="Indicates whether the incident description lacks clarity, detail, or sufficient context."
    )

    claim_invalid_or_fraudulent: YesNoUnknown = Field(
        description="Indicates whether the claim appears invalid, fraudulent, or intentionally misleading."
    )

    required_conditions_not_met: YesNoUnknown = Field(
        description="Indicates whether mandatory policy conditions or procedural requirements have not been satisfied."
    )

    risk_summary: str = Field(
        description="Free-text summary describing the key risk factors, context, and concerns identified for the claim."
    )
