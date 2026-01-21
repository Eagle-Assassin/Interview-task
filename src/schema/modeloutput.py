from pydantic import BaseModel, Field
from typing import Annotated
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
        Field(
            description=(
                "Indicates severe legal or regulatory exposure. "
                "Examples include regulatory investigations, enforcement actions, "
                "statutory breaches, compliance failures, FCA/SEC involvement, "
                "data protection authority actions, or court injunctions."
            )
        )
    ]

    business_critical_impact: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates business-critical impact such as major financial loss, "
                "business interruption, ransomware incidents, system-wide outages, "
                "or events threatening core operations."
            )
        )
    ]

    potential_fraud: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates indicators of fraud or intentional misrepresentation. "
                "Examples include suspected fraud, insurance fraud, suspicious activity, "
                "staged incidents, deliberate damage, or police investigations."
            )
        )
    ]

    conflicting_information: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates conflicting or inconsistent information across summaries, "
                "handler notes, timelines, documents, or claimant statements."
            )
        )
    ]

    complex_incident_details: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates technically complex or multi-factor incidents requiring "
                "expert interpretation, such as multi-party disputes, layered losses, "
                "or technically detailed scenarios."
            )
        )
    ]

    policy_interpretation_issues: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates ambiguity or uncertainty in policy wording or coverage scope. "
                "Examples include governing law unclear, unclear policy application, "
                "or terms requiring legal interpretation."
            )
        )
    ]

    legal_disputes: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates legal disputes or litigation risk. "
                "Examples include formal legal threats, breach of contract claims, "
                "employment disputes, IP infringement allegations, class actions, "
                "or formal letters from counterparties."
            ),
            alias="legal_disputs"  # typo safety net
        )
    ]

    jurisdictional_complexity: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates jurisdictional or cross-border complexity. "
                "Examples include cross-border claims, overseas elements, "
                "multiple jurisdictions, foreign courts, jurisdiction disputes, "
                "or governing law uncertainty."
            )
        )
    ]

    coverage_terms_unclear: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates unclear or insufficiently defined coverage terms, "
                "including uncertainty around insured events, limits, or conditions."
            )
        )
    ]

    exclusions_may_apply: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates that policy exclusions may apply. "
                "Examples include exclusions related to flood zones, wear and tear, "
                "prior losses, deliberate acts, or non-covered perils."
            )
        )
    ]

    new_or_unusual_claim_type: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates a new, rare, or unusual claim type not commonly encountered, "
                "or scenarios that fall outside typical historical patterns."
            )
        )
    ]

    unclear_incident_description: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates that the incident description is vague, incomplete, "
                "poorly structured, or lacks sufficient detail to assess the claim."
            )
        )
    ]

    claim_invalid_or_fraudulent: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates the claim may be invalid, non-covered, or intentionally misleading, "
                "including cases with implausible narratives or contradictory evidence."
            )
        )
    ]

    required_conditions_not_met: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates mandatory policy conditions have not been met, "
                "such as missing notifications, missing documentation, "
                "or failure to comply with policy requirements."
            )
        )
    ]

    # 🔹 Operational extraction flags (keyword-guided)

    has_regulator_involvement: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates regulator or regulatory authority involvement or expectation. "
                "Look for phrases such as regulator visit, regulator engagement, "
                "regulatory review, compliance breach, enforcement action, "
                "statutory breach, FCA, SEC, GDPR authority."
            )
        )
    ]

    has_cross_border_elements: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates cross-border or international elements. "
                "Look for phrases such as cross-border, overseas elements, "
                "international, foreign jurisdiction, multi-jurisdiction, "
                "governing law unclear, or jurisdiction disputed."
            )
        )
    ]

    has_time_sensitivity: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates urgency or time sensitivity. "
                "Look for phrases such as urgent, time-sensitive, immediate action required, "
                "injunction, limitation period, court deadline, ASAP, or statutory deadline."
            )
        )
    ]

    has_missing_documentation: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates missing or incomplete documentation. "
                "Look for phrases such as no policy documents, no supporting documentation, "
                "evidence not supplied, evidence pending, documents awaited, "
                "attachments missing, policy schedule missing, or insufficient evidence."
            )
        )
    ]

    mentions_fraud_or_arson: Annotated[
        YesNoUnknown,
        Field(
            description=(
                "Indicates mentions of fraud, arson, or suspicious activity. "
                "Look for phrases such as arson, suspected fraud, insurance fraud, "
                "class action, criminal investigation, police reference, theft, "
                "burglary, malicious damage, or misrepresentation."
            )
        )
    ]

    risk_summary: Annotated[
        str,
        Field(
            description=(
                "A concise 1–2 sentence plain-English summary explaining the main "
                "risk drivers, key concerns, and escalation factors identified in the claim."
            )
        )
    ]

    class Config:
        populate_by_name = True
