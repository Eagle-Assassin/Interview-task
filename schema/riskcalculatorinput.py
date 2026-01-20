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
        description="Unique identifier for the claim or case, used for tracking, joins, and auditability."
    )

    client_segment: ClientSegment = Field(
        description="Client size category (SMB, Mid-Market, Enterprise) used to estimate scale of exposure and escalation sensitivity."
    )

    jurisdiction: Jurisdiction = Field(
        description="Primary legal or regulatory jurisdiction governing the claim, influencing regulatory risk and legal complexity."
    )

    service_line: ServiceLine = Field(
        description="Service line responsible for handling the claim (Legal, Insurance, Advisory), used as a risk multiplier."
    )

    claim_value_band: ClaimValueBand = Field(
        description="Estimated financial exposure of the claim expressed as a predefined value band."
    )

    attachments_present: YesNo = Field(
        description="Indicates whether supporting documents or evidence were provided at intake."
    )

    historical_outcome: HistoricalOutcome = Field(
        description="Previously recorded or known outcome of the claim, if available, used only for analysis and calibration."
    )

    # ── Core LLM-extracted risk signals ────────────────────

    severe_legal_or_regulatory_risk: YesNoUnknown = Field(
        description="Indicates severe legal or regulatory exposure such as regulator investigations, enforcement actions, court injunctions, or statutory breaches."
    )

    business_critical_impact: YesNoUnknown = Field(
        description="Indicates business-critical impact including major operational disruption, ransomware incidents, or threats to core business continuity."
    )

    potential_fraud: YesNoUnknown = Field(
        description="Indicates presence of fraud risk signals such as suspicious activity, misrepresentation, staged incidents, or police involvement."
    )

    conflicting_information: YesNoUnknown = Field(
        description="Indicates conflicting or inconsistent information across summaries, timelines, handler notes, or supporting documents."
    )

    complex_incident_details: YesNoUnknown = Field(
        description="Indicates incidents with technical, multi-party, or layered complexity requiring expert or specialist interpretation."
    )

    policy_interpretation_issues: YesNoUnknown = Field(
        description="Indicates ambiguity or uncertainty in policy wording, coverage scope, governing law, or applicability of terms."
    )

    legal_disputes: YesNoUnknown = Field(
        description="Indicates actual or potential legal disputes, including breach of contract, employment disputes, IP claims, or litigation risk."
    )

    jurisdictional_complexity: YesNoUnknown = Field(
        description="Indicates cross-border, multi-jurisdictional, or legally complex jurisdictional considerations."
    )

    coverage_terms_unclear: YesNoUnknown = Field(
        description="Indicates unclear or insufficiently defined coverage terms that prevent confident eligibility assessment."
    )

    exclusions_may_apply: YesNoUnknown = Field(
        description="Indicates potential applicability of policy exclusions such as wear and tear, flood zones, deliberate acts, or prior losses."
    )

    new_or_unusual_claim_type: YesNoUnknown = Field(
        description="Indicates a rare, novel, or unusual claim type that does not follow standard historical patterns."
    )

    unclear_incident_description: YesNoUnknown = Field(
        description="Indicates vague, incomplete, or poorly structured incident descriptions that limit assessment quality."
    )

    claim_invalid_or_fraudulent: YesNoUnknown = Field(
        description="Indicates the claim may be invalid, non-covered, or intentionally misleading based on available information."
    )

    required_conditions_not_met: YesNoUnknown = Field(
        description="Indicates mandatory policy or procedural conditions have not been met, such as missing notifications or required documentation."
    )

    # ── Keyword-driven operational extraction flags ───────

    has_regulator_involvement: YesNoUnknown = Field(
        description=(
            "Indicates regulator or regulatory authority involvement or expectation. "
            "Derived from phrases such as 'regulator visit', 'regulator engagement', "
            "'regulatory review', 'FCA', 'SEC', or 'data protection authority'."
        )
    )

    has_cross_border_elements: YesNoUnknown = Field(
        description=(
            "Indicates cross-border or international elements. "
            "Derived from phrases such as 'cross-border', 'overseas elements', "
            "'foreign jurisdiction', or 'governing law unclear'."
        )
    )

    has_time_sensitivity: YesNoUnknown = Field(
        description=(
            "Indicates urgency or time sensitivity. "
            "Derived from phrases such as 'urgent', 'time-sensitive', 'injunction', "
            "'limitation period', or 'immediate action required'."
        )
    )

    has_missing_documentation: YesNoUnknown = Field(
        description=(
            "Indicates missing or incomplete documentation. "
            "Derived from phrases such as 'no policy documents', "
            "'evidence not supplied', 'attachments missing', or 'documents awaited'."
        )
    )

    mentions_fraud_or_arson: YesNoUnknown = Field(
        description=(
            "Indicates mentions of fraud, arson, or criminal activity. "
            "Derived from phrases such as 'arson', 'fraud', 'class action', "
            "'police reference', 'theft', or 'criminal investigation'."
        )
    )

    # ── Free-text rationale ───────────────────────────────

    risk_summary: str = Field(
        description="Concise 1–2 sentence plain-English explanation summarizing the primary risk drivers and escalation factors."
    )

    class Config:
        extra = "forbid"
