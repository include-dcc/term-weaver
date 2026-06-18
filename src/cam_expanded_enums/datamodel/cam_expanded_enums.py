# Auto generated from cam_expanded_enums.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-06-17T15:58:35
# Schema: cam-expanded-enums
#
# id: https://includedcc.org/cam-expanded-enums
# description: LinkML Schema for the Common Access Model Expanded Enums
# license: MIT

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import String

metamodel_version = "1.11.0"
version = None

# Namespaces
DUO = CurieNamespace('DUO', 'http://purl.obolibrary.org/obo/DUO_')
HP = CurieNamespace('HP', 'http://purl.obolibrary.org/obo/HP_')
MONDO = CurieNamespace('MONDO', 'http://purl.obolibrary.org/obo/MONDO_')
NCIT = CurieNamespace('NCIT', 'http://purl.obolibrary.org/obo/NCIT_')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
CAM = CurieNamespace('cam', 'https://includedcc.org/common-access-model/')
CDC_RACE_ETH = CurieNamespace('cdc_race_eth', 'urn:oid:2.16.840.1.113883.6.238/')
HL7_NULL = CurieNamespace('hl7_null', 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/')
IG2_BIOSPECIMEN_AVAILABILITY = CurieNamespace('ig2_biospecimen_availability', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/')
IG2DAC = CurieNamespace('ig2dac', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/')
IG2DAT = CurieNamespace('ig2dat', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/')
IG_DOB_METHOD = CurieNamespace('ig_dob_method', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/')
IGCONDTYPE = CurieNamespace('igcondtype', 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
MESH = CurieNamespace('mesh', 'http://id.nlm.nih.gov/mesh/')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SNOMED_CT = CurieNamespace('snomed_ct', 'http://snomed.info/id/')
DEFAULT_ = CAM


# Types

# Class references



@dataclass(repr=False)
class RequiredClass(YAMLRoot):
    """
    This is a placeholder class to satisfy the LinkML requirement of at least one class and is not otherwise used.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = CAM["RequiredClass"]
    class_class_curie: ClassVar[str] = "cam:RequiredClass"
    class_name: ClassVar[str] = "RequiredClass"
    class_model_uri: ClassVar[URIRef] = CAM.RequiredClass

    id: Optional[str] = None
    full_name: Optional[str] = None
    aliases: Optional[str] = None
    phone: Optional[str] = None
    age: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.id is not None and not isinstance(self.id, str):
            self.id = str(self.id)

        if self.full_name is not None and not isinstance(self.full_name, str):
            self.full_name = str(self.full_name)

        if self.aliases is not None and not isinstance(self.aliases, str):
            self.aliases = str(self.aliases)

        if self.phone is not None and not isinstance(self.phone, str):
            self.phone = str(self.phone)

        if self.age is not None and not isinstance(self.age, str):
            self.age = str(self.age)

        super().__post_init__(**kwargs)


# Enumerations
class EnumDataUsePermission(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    _defn = EnumDefinition(
        name="EnumDataUsePermission",
        description="Data Use Ontology (DUO) terms for data use permissions.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DUO:0000004",
            PermissibleValue(
                text="DUO:0000004",
                title="no restriction",
                description="This data use permission indicates there is no restriction on use."))
        setattr(cls, "DUO:0000006",
            PermissibleValue(
                text="DUO:0000006",
                title="health or medical or biomedical research",
                description="""This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry."""))
        setattr(cls, "DUO:0000007",
            PermissibleValue(
                text="DUO:0000007",
                title="disease specific research",
                description="""This data use permission indicates that use is allowed provided it is related to the specified disease.
This term should be coupled with a term describing a disease from an ontology to specify the disease the restriction applies to.

DUO recommends MONDO be used, to provide the basis for automated evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md

Other resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can also be used. When those other resources are being used, this may require an extra mapping step to leverage automated matching algorithms."""))
        setattr(cls, "DUO:0000011",
            PermissibleValue(
                text="DUO:0000011",
                title="population origins or ancestry research only",
                description="""This data use permission indicates that use of the data is limited to the study of population origins or ancestry."""))
        setattr(cls, "DUO:0000042",
            PermissibleValue(
                text="DUO:0000042",
                title="general research use",
                description="""This data use permission indicates that use is allowed for general research use for any research purpose.
This includes but is not limited to: health/medical/biomedical purposes, fundamental biology research, the study of population origins or ancestry, statistical methods and algorithms development, and social-sciences research."""))

class EnumDataUseModifier(EnumDefinitionImpl):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    _defn = EnumDefinition(
        name="EnumDataUseModifier",
        description="Data Use Ontology (DUO) terms for data use modifiers.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "DUO:00000044",
            PermissibleValue(
                text="DUO:00000044",
                title="population origins or ancestry research prohibited",
                description="""This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited."""))
        setattr(cls, "DUO:0000012",
            PermissibleValue(
                text="DUO:0000012",
                title="research specific restrictions",
                description="""This data use modifier indicates that use is limited to studies of a certain research type."""))
        setattr(cls, "DUO:0000015",
            PermissibleValue(
                text="DUO:0000015",
                title="no general methods research",
                description="""This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms)."""))
        setattr(cls, "DUO:0000016",
            PermissibleValue(
                text="DUO:0000016",
                title="genetic studies only",
                description="""This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)"""))
        setattr(cls, "DUO:0000018",
            PermissibleValue(
                text="DUO:0000018",
                title="not for profit, non commercial use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use."""))
        setattr(cls, "DUO:0000019",
            PermissibleValue(
                text="DUO:0000019",
                title="publication required",
                description="""This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community."""))
        setattr(cls, "DUO:0000020",
            PermissibleValue(
                text="DUO:0000020",
                title="collaboration required",
                description="""This could be coupled with a string describing the primary study investigator(s).
This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s)."""))
        setattr(cls, "DUO:0000021",
            PermissibleValue(
                text="DUO:0000021",
                title="ethics approval required",
                description="""This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval."""))
        setattr(cls, "DUO:0000022",
            PermissibleValue(
                text="DUO:0000022",
                title="geographical restriction",
                description="""This data use modifier indicates that use is limited to within a specific geographic region.
This should be coupled with an ontology term describing the geographical location the restriction applies to."""))
        setattr(cls, "DUO:0000024",
            PermissibleValue(
                text="DUO:0000024",
                title="publication moratorium",
                description="""This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.
This should be coupled with a date specified as ISO8601"""))
        setattr(cls, "DUO:0000025",
            PermissibleValue(
                text="DUO:0000025",
                title="time limit on use",
                description="""This data use modifier indicates that use is approved for a specific number of months.
This should be coupled with an integer value indicating the number of months."""))
        setattr(cls, "DUO:0000026",
            PermissibleValue(
                text="DUO:0000026",
                title="user specific restriction",
                description="This data use modifier indicates that use is limited to use by approved users."))
        setattr(cls, "DUO:0000027",
            PermissibleValue(
                text="DUO:0000027",
                title="project specific restriction",
                description="""This data use modifier indicates that use is limited to use within an approved project."""))
        setattr(cls, "DUO:0000028",
            PermissibleValue(
                text="DUO:0000028",
                title="institution specific restriction",
                description="""This data use modifier indicates that use is limited to use within an approved institution."""))
        setattr(cls, "DUO:0000029",
            PermissibleValue(
                text="DUO:0000029",
                title="return to database or resource",
                description="""This data use modifier indicates that the requestor must return derived/enriched data to the database/resource."""))
        setattr(cls, "DUO:0000043",
            PermissibleValue(
                text="DUO:0000043",
                title="clinical care use",
                description="""Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making.
This data use modifier indicates that use is allowed for clinical use and care."""))
        setattr(cls, "DUO:0000045",
            PermissibleValue(
                text="DUO:0000045",
                title="not for profit organisation use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit organizations."""))
        setattr(cls, "DUO:0000046",
            PermissibleValue(
                text="DUO:0000046",
                title="non-commercial use only",
                description="""This data use modifier indicates that use of the data is limited to not-for-profit use.
This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes."""))

class EnumProgram(EnumDefinitionImpl):
    """
    Funding programs relevant to inform operations.
    """
    include = PermissibleValue(
        text="include",
        title="INCLUDE")
    kf = PermissibleValue(
        text="kf",
        title="KF")
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumProgram",
        description="Funding programs relevant to inform operations.",
    )

class EnumResearchDomain(EnumDefinitionImpl):
    """
    Domains of Research used to find studies.
    """
    behavior_and_behavior_mechanisms = PermissibleValue(
        text="behavior_and_behavior_mechanisms",
        title="Behavior and Behavior Mechanisms",
        meaning=MESH["D001520"])
    congenital_heart_defects = PermissibleValue(
        text="congenital_heart_defects",
        title="Congenital Heart Defects",
        meaning=MESH["D006330"])
    immune_system_diseases = PermissibleValue(
        text="immune_system_diseases",
        title="Immune System Diseases",
        meaning=MESH["D007154"])
    hematologic_diseases = PermissibleValue(
        text="hematologic_diseases",
        title="Hematologic Diseases",
        meaning=MESH["D006402"])
    neurodevelopment = PermissibleValue(
        text="neurodevelopment",
        title="Neurodevelopment",
        meaning=MESH["D065886"])
    sleep_wake_disorders = PermissibleValue(
        text="sleep_wake_disorders",
        title="Sleep Wake Disorders",
        meaning=MESH["D012893"])
    all_co_occurring_conditions = PermissibleValue(
        text="all_co_occurring_conditions",
        title="All Co-occurring Conditions",
        meaning=MESH["D013568"])
    physical_fitness = PermissibleValue(
        text="physical_fitness",
        title="Physical Fitness",
        meaning=MESH["D010809"])
    other = PermissibleValue(
        text="other",
        title="Other")

    _defn = EnumDefinition(
        name="EnumResearchDomain",
        description="Domains of Research used to find studies.",
    )

class EnumParticipantLifespanStage(EnumDefinitionImpl):
    """
    Stages of life during which participants may be recruited.
    """
    fetal = PermissibleValue(
        text="fetal",
        title="Fetal",
        description="Before birth")
    neonatal = PermissibleValue(
        text="neonatal",
        title="Neonatal",
        description="0-28 days old")
    pediatric = PermissibleValue(
        text="pediatric",
        title="Pediatric",
        description="Birth-17 years old")
    adult = PermissibleValue(
        text="adult",
        title="Adult",
        description="18+ years old")

    _defn = EnumDefinition(
        name="EnumParticipantLifespanStage",
        description="Stages of life during which participants may be recruited.",
    )

class EnumStudyDesign(EnumDefinitionImpl):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    case_control = PermissibleValue(
        text="case_control",
        title="Case-Control")
    case_set = PermissibleValue(
        text="case_set",
        title="Case Set")
    control_set = PermissibleValue(
        text="control_set",
        title="Control Set")
    clinical_trial = PermissibleValue(
        text="clinical_trial",
        title="Clinical Trial")
    cross_sectional = PermissibleValue(
        text="cross_sectional",
        title="Cross-Sectional")
    family_twins_trios = PermissibleValue(
        text="family_twins_trios",
        title="Family/Twins/Trios")
    interventional = PermissibleValue(
        text="interventional",
        title="Interventional")
    longitudinal = PermissibleValue(
        text="longitudinal",
        title="Longitudinal")
    trial_readiness_study = PermissibleValue(
        text="trial_readiness_study",
        title="Trial Readiness Study")
    tumor_vs_matched_normal = PermissibleValue(
        text="tumor_vs_matched_normal",
        title="Tumor vs Matched Normal")

    _defn = EnumDefinition(
        name="EnumStudyDesign",
        description="Approaches for collecting data, investigating interventions, and/or analyzing data.",
    )

class EnumClinicalDataSourceType(EnumDefinitionImpl):
    """
    Approaches to ascertain clinical information about a participant.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained directly from medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown")

    _defn = EnumDefinition(
        name="EnumClinicalDataSourceType",
        description="Approaches to ascertain clinical information about a participant.",
    )

class EnumDataCategory(EnumDefinitionImpl):
    """
    Categories of data which may be collected about participants.
    """
    unharmonized_demographic_clinical_data = PermissibleValue(
        text="unharmonized_demographic_clinical_data",
        title="Unharmonized Demographic/Clinical Data")
    harmonized_demographic_clinical_data = PermissibleValue(
        text="harmonized_demographic_clinical_data",
        title="Harmonized Demographic/Clinical Data")
    genomics = PermissibleValue(
        text="genomics",
        title="Genomics")
    transcriptomics = PermissibleValue(
        text="transcriptomics",
        title="Transcriptomics")
    epigenomics = PermissibleValue(
        text="epigenomics",
        title="Epigenomics")
    proteomics = PermissibleValue(
        text="proteomics",
        title="Proteomics")
    metabolomics = PermissibleValue(
        text="metabolomics",
        title="Metabolomics")
    cognitive_behavioral = PermissibleValue(
        text="cognitive_behavioral",
        title="Cognitive/Behavioral")
    immune_profiling = PermissibleValue(
        text="immune_profiling",
        title="Immune Profiling")
    imaging = PermissibleValue(
        text="imaging",
        title="Imaging")
    microbiome = PermissibleValue(
        text="microbiome",
        title="Microbiome")
    fitness = PermissibleValue(
        text="fitness",
        title="Fitness")
    physical_activity = PermissibleValue(
        text="physical_activity",
        title="Physical Activity")
    other = PermissibleValue(
        text="other",
        title="Other")
    sleep_study = PermissibleValue(
        text="sleep_study",
        title="Sleep Study")

    _defn = EnumDefinition(
        name="EnumDataCategory",
        description="Categories of data which may be collected about participants.",
    )

class EnumSubjectType(EnumDefinitionImpl):
    """
    Types of Subject entities
    """
    participant = PermissibleValue(
        text="participant",
        description="Study participant with consent, assent, or waiver of consent.")
    non_participant = PermissibleValue(
        text="non_participant",
        description="""An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.""")
    cell_line = PermissibleValue(
        text="cell_line",
        description="Cell Line")
    animal_model = PermissibleValue(
        text="animal_model",
        description="Animal model")
    group = PermissibleValue(
        text="group",
        description="A group of individuals or entities.")
    other = PermissibleValue(
        text="other",
        description="A different entity type- ideally this will be resolved!")

    _defn = EnumDefinition(
        name="EnumSubjectType",
        description="Types of Subject entities",
    )

class EnumSex(EnumDefinitionImpl):
    """
    Subject Sex
    """
    female = PermissibleValue(
        text="female",
        title="Female",
        meaning=NCIT["C16576"])
    male = PermissibleValue(
        text="male",
        title="Male",
        meaning=NCIT["C20197"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumSex",
        description="Subject Sex",
    )

class EnumRace(EnumDefinitionImpl):
    """
    Participant Race
    """
    american_indian_or_alaska_native = PermissibleValue(
        text="american_indian_or_alaska_native",
        title="American Indian or Alaska Native",
        meaning=NCIT["C41259"])
    asian = PermissibleValue(
        text="asian",
        title="Asian",
        meaning=NCIT["C41260"])
    black_or_african_american = PermissibleValue(
        text="black_or_african_american",
        title="Black or African American",
        meaning=NCIT["C16352"])
    more_than_one_race = PermissibleValue(
        text="more_than_one_race",
        title="More than one race",
        meaning=NCIT["C67109"])
    native_hawaiian_or_other_pacific_islander = PermissibleValue(
        text="native_hawaiian_or_other_pacific_islander",
        title="Native Hawaiian or Other Pacific Islander",
        meaning=NCIT["C41219"])
    other = PermissibleValue(
        text="other",
        title="Other",
        meaning=NCIT["C17649"])
    white = PermissibleValue(
        text="white",
        title="White",
        meaning=NCIT["C41261"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])
    east_asian = PermissibleValue(
        text="east_asian",
        title="East Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C161419"])
    latin_american = PermissibleValue(
        text="latin_american",
        title="Latin American",
        description="UK only; do not use for US data",
        meaning=NCIT["C126531"])
    middle_eastern_or_north_african = PermissibleValue(
        text="middle_eastern_or_north_african",
        title="Middle Eastern or North African",
        description="UK only; do not use for US data",
        meaning=NCIT["C43866"])
    south_asian = PermissibleValue(
        text="south_asian",
        title="South Asian",
        description="UK only; do not use for US data",
        meaning=NCIT["C41263"])

    _defn = EnumDefinition(
        name="EnumRace",
        description="Participant Race",
    )

class EnumEthnicity(EnumDefinitionImpl):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    hispanic_or_latino = PermissibleValue(
        text="hispanic_or_latino",
        title="Hispanic or Latino",
        meaning=NCIT["C17459"])
    not_hispanic_or_latino = PermissibleValue(
        text="not_hispanic_or_latino",
        title="Not Hispanic or Latino",
        meaning=NCIT["C41222"])
    prefer_not_to_answer = PermissibleValue(
        text="prefer_not_to_answer",
        title="Prefer not to answer",
        meaning=NCIT["C132222"])
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumEthnicity",
        description="Participant ethnicity, specific to Hispanic or Latino.",
    )

class EnumVitalStatus(EnumDefinitionImpl):
    """
    Descriptions of a Subject's vital status
    """
    dead = PermissibleValue(
        text="dead",
        title="Dead",
        meaning=NCIT["C28554"])
    alive = PermissibleValue(
        text="alive",
        title="Alive",
        meaning=NCIT["C37987"])

    _defn = EnumDefinition(
        name="EnumVitalStatus",
        description="Descriptions of a Subject's vital status",
    )

class EnumNull(EnumDefinitionImpl):
    """
    Base enumeration providing null options.
    """
    unknown = PermissibleValue(
        text="unknown",
        title="Unknown",
        meaning=NCIT["C17998"])

    _defn = EnumDefinition(
        name="EnumNull",
        description="Base enumeration providing null options.",
    )

class EnumFamilyType(EnumDefinitionImpl):
    """
    Enumerations describing research family type
    """
    control_only = PermissibleValue(
        text="control_only",
        title="Control-only",
        description="Control Only")
    duo = PermissibleValue(
        text="duo",
        title="Duo",
        description="Duo")
    proband_only = PermissibleValue(
        text="proband_only",
        title="Proband-only",
        description="Proband Only")
    trio = PermissibleValue(
        text="trio",
        title="Trio",
        description="Trio (2 parents and affected child)")
    trio_plus = PermissibleValue(
        text="trio_plus",
        title="Trio+",
        description="2 Parents and 2 or more children")

    _defn = EnumDefinition(
        name="EnumFamilyType",
        description="Enumerations describing research family type",
    )

class EnumConsanguinityAssertion(EnumDefinitionImpl):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = PermissibleValue(
        text="not_suspected",
        title="not-suspected",
        description="Not suspected",
        meaning=SNOMED_CT["428263003"])
    suspected = PermissibleValue(
        text="suspected",
        title="suspected",
        description="Suspected",
        meaning=SNOMED_CT["415684004"])
    known_present = PermissibleValue(
        text="known_present",
        title="known-present",
        description="Known Present",
        meaning=SNOMED_CT["410515003"])
    unknown = PermissibleValue(
        text="unknown",
        title="unknown",
        description="Unknown",
        meaning=SNOMED_CT["261665006"])

    _defn = EnumDefinition(
        name="EnumConsanguinityAssertion",
        description="Asserts known or suspected consanguinity in this study family",
    )

class EnumAssertionProvenance(EnumDefinitionImpl):
    """
    Possible data sources for assertions.
    """
    medical_record = PermissibleValue(
        text="medical_record",
        title="Medical Record",
        description="Data obtained from a medical record")
    investigator_assessment = PermissibleValue(
        text="investigator_assessment",
        title="Investigator Assessment",
        description="Data obtained by examination, interview, etc. with investigator")
    participant_or_caregiver_report = PermissibleValue(
        text="participant_or_caregiver_report",
        title="Participant or Caregiver Report",
        description="Data obtained from survey, questionnaire, etc. filled out by participant or caregiver")
    other = PermissibleValue(
        text="other",
        title="Other",
        description="Data obtained from other source, such as tissue bank")

    _defn = EnumDefinition(
        name="EnumAssertionProvenance",
        description="Possible data sources for assertions.",
    )

class EnumAvailabilityStatus(EnumDefinitionImpl):
    """
    Is the biospecimen available for use?
    """
    available = PermissibleValue(
        text="available",
        title="Available",
        description="Biospecimen is Available",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["available"])
    unavailable = PermissibleValue(
        text="unavailable",
        title="Unavailable",
        description="Biospecimen is Unavailable",
        meaning=IG2_BIOSPECIMEN_AVAILABILITY["unavailable"])

    _defn = EnumDefinition(
        name="EnumAvailabilityStatus",
        description="Is the biospecimen available for use?",
    )

class EnumSampleCollectionMethod(EnumDefinitionImpl):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    _defn = EnumDefinition(
        name="EnumSampleCollectionMethod",
        description="The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.",
    )

class EnumSite(EnumDefinitionImpl):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is
    recommended.
    """
    _defn = EnumDefinition(
        name="EnumSite",
        description="""The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.""",
    )

class EnumSpatialQualifiers(EnumDefinitionImpl):
    """
    Any spatial/location qualifiers.
    """
    _defn = EnumDefinition(
        name="EnumSpatialQualifiers",
        description="Any spatial/location qualifiers.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "SNOMED:106233006",
            PermissibleValue(
                text="SNOMED:106233006",
                title="Topographical modifier (qualifier value)",
                description="Topographical modifier (qualifier value)"))
        setattr(cls, "SNOMED:103339001",
            PermissibleValue(
                text="SNOMED:103339001",
                title="Long axis"))
        setattr(cls, "SNOMED:103340004",
            PermissibleValue(
                text="SNOMED:103340004",
                title="Short axis"))
        setattr(cls, "SNOMED:103341000",
            PermissibleValue(
                text="SNOMED:103341000",
                title="Off axis"))
        setattr(cls, "SNOMED:103342007",
            PermissibleValue(
                text="SNOMED:103342007",
                title="Mid-longitudinal"))
        setattr(cls, "SNOMED:103343002",
            PermissibleValue(
                text="SNOMED:103343002",
                title="Parasagittal"))
        setattr(cls, "SNOMED:103344008",
            PermissibleValue(
                text="SNOMED:103344008",
                title="Transvesical"))
        setattr(cls, "SNOMED:103345009",
            PermissibleValue(
                text="SNOMED:103345009",
                title="Transthecal"))
        setattr(cls, "SNOMED:103346005",
            PermissibleValue(
                text="SNOMED:103346005",
                title="Transsplenic"))
        setattr(cls, "SNOMED:103347001",
            PermissibleValue(
                text="SNOMED:103347001",
                title="Transrenal"))
        setattr(cls, "SNOMED:103348006",
            PermissibleValue(
                text="SNOMED:103348006",
                title="Transpleural"))
        setattr(cls, "SNOMED:103349003",
            PermissibleValue(
                text="SNOMED:103349003",
                title="Transpancreatic"))
        setattr(cls, "SNOMED:103353001",
            PermissibleValue(
                text="SNOMED:103353001",
                title="Transgastric"))
        setattr(cls, "SNOMED:103354007",
            PermissibleValue(
                text="SNOMED:103354007",
                title="Transmural"))
        setattr(cls, "SNOMED:11070000",
            PermissibleValue(
                text="SNOMED:11070000",
                title="Capsular"))
        setattr(cls, "SNOMED:1146002",
            PermissibleValue(
                text="SNOMED:1146002",
                title="Arcuate"))
        setattr(cls, "SNOMED:11896004",
            PermissibleValue(
                text="SNOMED:11896004",
                title="Intermediate"))
        setattr(cls, "SNOMED:1217011006",
            PermissibleValue(
                text="SNOMED:1217011006",
                title="Non-adjacent"))
        setattr(cls, "SNOMED:131183008",
            PermissibleValue(
                text="SNOMED:131183008",
                title="Intra-articular"))
        setattr(cls, "SNOMED:131184002",
            PermissibleValue(
                text="SNOMED:131184002",
                title="Area of defined region"))
        setattr(cls, "SNOMED:131185001",
            PermissibleValue(
                text="SNOMED:131185001",
                title="Vertical long axis"))
        setattr(cls, "SNOMED:131186000",
            PermissibleValue(
                text="SNOMED:131186000",
                title="Horizontal long axis"))
        setattr(cls, "SNOMED:131187009",
            PermissibleValue(
                text="SNOMED:131187009",
                title="Major Axis"))
        setattr(cls, "SNOMED:131188004",
            PermissibleValue(
                text="SNOMED:131188004",
                title="Minor Axis"))
        setattr(cls, "SNOMED:131189007",
            PermissibleValue(
                text="SNOMED:131189007",
                title="Perpendicular axis"))
        setattr(cls, "SNOMED:131190003",
            PermissibleValue(
                text="SNOMED:131190003",
                title="Radius"))
        setattr(cls, "SNOMED:131191004",
            PermissibleValue(
                text="SNOMED:131191004",
                title="Perimeter"))
        setattr(cls, "SNOMED:14414005",
            PermissibleValue(
                text="SNOMED:14414005",
                title="Peripheral"))
        setattr(cls, "SNOMED:1483009",
            PermissibleValue(
                text="SNOMED:1483009",
                title="Angular"))
        setattr(cls, "SNOMED:18769003",
            PermissibleValue(
                text="SNOMED:18769003",
                title="Juxta-posed"))
        setattr(cls, "SNOMED:21006006",
            PermissibleValue(
                text="SNOMED:21006006",
                title="Hemispheric"))
        setattr(cls, "SNOMED:21481007",
            PermissibleValue(
                text="SNOMED:21481007",
                title="Over"))
        setattr(cls, "SNOMED:24020000",
            PermissibleValue(
                text="SNOMED:24020000",
                title="Horizontal"))
        setattr(cls, "SNOMED:24028007",
            PermissibleValue(
                text="SNOMED:24028007",
                title="Right (qualifier value)",
                description="Right (qualifier value)"))
        setattr(cls, "SNOMED:24422004",
            PermissibleValue(
                text="SNOMED:24422004",
                title="Axial"))
        setattr(cls, "SNOMED:255527003",
            PermissibleValue(
                text="SNOMED:255527003",
                title="Horizontal - 3 and 9"))
        setattr(cls, "SNOMED:255528008",
            PermissibleValue(
                text="SNOMED:255528008",
                title="Horizontal and vertical"))
        setattr(cls, "SNOMED:261129000",
            PermissibleValue(
                text="SNOMED:261129000",
                title="Mediolateral"))
        setattr(cls, "SNOMED:26216008",
            PermissibleValue(
                text="SNOMED:26216008",
                title="Central"))
        setattr(cls, "SNOMED:26283006",
            PermissibleValue(
                text="SNOMED:26283006",
                title="Superficial"))
        setattr(cls, "SNOMED:263687007",
            PermissibleValue(
                text="SNOMED:263687007",
                title="Bony extra-articular"))
        setattr(cls, "SNOMED:263688002",
            PermissibleValue(
                text="SNOMED:263688002",
                title="Bony intra-articular"))
        setattr(cls, "SNOMED:264731004",
            PermissibleValue(
                text="SNOMED:264731004",
                title="Lateral to the left"))
        setattr(cls, "SNOMED:264732006",
            PermissibleValue(
                text="SNOMED:264732006",
                title="Lateral to the right"))
        setattr(cls, "SNOMED:264733001",
            PermissibleValue(
                text="SNOMED:264733001",
                title="Linear longitudinal"))
        setattr(cls, "SNOMED:264737000",
            PermissibleValue(
                text="SNOMED:264737000",
                title="Linear transverse"))
        setattr(cls, "SNOMED:264741001",
            PermissibleValue(
                text="SNOMED:264741001",
                title="Posterolateral to the left"))
        setattr(cls, "SNOMED:264742008",
            PermissibleValue(
                text="SNOMED:264742008",
                title="Posterolateral to the right"))
        setattr(cls, "SNOMED:264839005",
            PermissibleValue(
                text="SNOMED:264839005",
                title="Horizontal cleavage"))
        setattr(cls, "SNOMED:27237009",
            PermissibleValue(
                text="SNOMED:27237009",
                title="Triangular"))
        setattr(cls, "SNOMED:28241006",
            PermissibleValue(
                text="SNOMED:28241006",
                title="Rhomboid"))
        setattr(cls, "SNOMED:28947002",
            PermissibleValue(
                text="SNOMED:28947002",
                title="Right curve"))
        setattr(cls, "SNOMED:30730003",
            PermissibleValue(
                text="SNOMED:30730003",
                title="Sagittal"))
        setattr(cls, "SNOMED:30899007",
            PermissibleValue(
                text="SNOMED:30899007",
                title="Quadrangular"))
        setattr(cls, "SNOMED:32381004",
            PermissibleValue(
                text="SNOMED:32381004",
                title="Portal"))
        setattr(cls, "SNOMED:32400000",
            PermissibleValue(
                text="SNOMED:32400000",
                title="Preaxial"))
        setattr(cls, "SNOMED:33096000",
            PermissibleValue(
                text="SNOMED:33096000",
                title="Vertical"))
        setattr(cls, "SNOMED:33843005",
            PermissibleValue(
                text="SNOMED:33843005",
                title="Efferent"))
        setattr(cls, "SNOMED:350722008",
            PermissibleValue(
                text="SNOMED:350722008",
                title="Behind"))
        setattr(cls, "SNOMED:351726001",
            PermissibleValue(
                text="SNOMED:351726001",
                title="Below"))
        setattr(cls, "SNOMED:352730000",
            PermissibleValue(
                text="SNOMED:352730000",
                title="Supra-"))
        setattr(cls, "SNOMED:353734004",
            PermissibleValue(
                text="SNOMED:353734004",
                title="Upward"))
        setattr(cls, "SNOMED:354652004",
            PermissibleValue(
                text="SNOMED:354652004",
                title="Circular"))
        setattr(cls, "SNOMED:355648006",
            PermissibleValue(
                text="SNOMED:355648006",
                title="Surrounding"))
        setattr(cls, "SNOMED:37197008",
            PermissibleValue(
                text="SNOMED:37197008",
                title="Anterolateral"))
        setattr(cls, "SNOMED:38717003",
            PermissibleValue(
                text="SNOMED:38717003",
                title="Longitudinal"))
        setattr(cls, "SNOMED:39187007",
            PermissibleValue(
                text="SNOMED:39187007",
                title="Bent"))
        setattr(cls, "SNOMED:40415009",
            PermissibleValue(
                text="SNOMED:40415009",
                title="Proximal"))
        setattr(cls, "SNOMED:410674003",
            PermissibleValue(
                text="SNOMED:410674003",
                title="Regional"))
        setattr(cls, "SNOMED:410679008",
            PermissibleValue(
                text="SNOMED:410679008",
                title="Surface"))
        setattr(cls, "SNOMED:42798000",
            PermissibleValue(
                text="SNOMED:42798000",
                title="Area"))
        setattr(cls, "SNOMED:43674008",
            PermissibleValue(
                text="SNOMED:43674008",
                title="Apical"))
        setattr(cls, "SNOMED:45226003",
            PermissibleValue(
                text="SNOMED:45226003",
                title="Cylindrical"))
        setattr(cls, "SNOMED:46053002",
            PermissibleValue(
                text="SNOMED:46053002",
                title="Distal"))
        setattr(cls, "SNOMED:47021000",
            PermissibleValue(
                text="SNOMED:47021000",
                title="Left curve"))
        setattr(cls, "SNOMED:49370004",
            PermissibleValue(
                text="SNOMED:49370004",
                title="Lateral"))
        setattr(cls, "SNOMED:49530007",
            PermissibleValue(
                text="SNOMED:49530007",
                title="Afferent"))
        setattr(cls, "SNOMED:50009006",
            PermissibleValue(
                text="SNOMED:50009006",
                title="Linear"))
        setattr(cls, "SNOMED:50362007",
            PermissibleValue(
                text="SNOMED:50362007",
                title="Stellate"))
        setattr(cls, "SNOMED:50974003",
            PermissibleValue(
                text="SNOMED:50974003",
                title="Junctional"))
        setattr(cls, "SNOMED:51440002",
            PermissibleValue(
                text="SNOMED:51440002",
                title="Right and left"))
        setattr(cls, "SNOMED:5686001",
            PermissibleValue(
                text="SNOMED:5686001",
                title="Remote"))
        setattr(cls, "SNOMED:56924007",
            PermissibleValue(
                text="SNOMED:56924007",
                title="Square"))
        setattr(cls, "SNOMED:57183005",
            PermissibleValue(
                text="SNOMED:57183005",
                title="Along edge"))
        setattr(cls, "SNOMED:57195005",
            PermissibleValue(
                text="SNOMED:57195005",
                title="Basal"))
        setattr(cls, "SNOMED:59410002",
            PermissibleValue(
                text="SNOMED:59410002",
                title="Rectangular"))
        setattr(cls, "SNOMED:60301000",
            PermissibleValue(
                text="SNOMED:60301000",
                title="Curved"))
        setattr(cls, "SNOMED:60583000",
            PermissibleValue(
                text="SNOMED:60583000",
                title="Postaxial"))
        setattr(cls, "SNOMED:61397002",
            PermissibleValue(
                text="SNOMED:61397002",
                title="Subcapsular"))
        setattr(cls, "SNOMED:62083003",
            PermissibleValue(
                text="SNOMED:62083003",
                title="Sectional"))
        setattr(cls, "SNOMED:62372003",
            PermissibleValue(
                text="SNOMED:62372003",
                title="Segmental"))
        setattr(cls, "SNOMED:62824007",
            PermissibleValue(
                text="SNOMED:62824007",
                title="Transverse"))
        setattr(cls, "SNOMED:66787007",
            PermissibleValue(
                text="SNOMED:66787007",
                title="Cephalic"))
        setattr(cls, "SNOMED:68493006",
            PermissibleValue(
                text="SNOMED:68493006",
                title="Gutter"))
        setattr(cls, "SNOMED:69320009",
            PermissibleValue(
                text="SNOMED:69320009",
                title="Extracellular"))
        setattr(cls, "SNOMED:69389007",
            PermissibleValue(
                text="SNOMED:69389007",
                title="Saccular"))
        setattr(cls, "SNOMED:710097009",
            PermissibleValue(
                text="SNOMED:710097009",
                title="Incisal"))
        setattr(cls, "SNOMED:710098004",
            PermissibleValue(
                text="SNOMED:710098004",
                title="Occlusal"))
        setattr(cls, "SNOMED:710099007",
            PermissibleValue(
                text="SNOMED:710099007",
                title="Mesial"))
        setattr(cls, "SNOMED:7771000",
            PermissibleValue(
                text="SNOMED:7771000",
                title="Left (qualifier value)",
                description="Left (qualifier value)"))
        setattr(cls, "SNOMED:795002",
            PermissibleValue(
                text="SNOMED:795002",
                title="Deep"))
        setattr(cls, "SNOMED:81654009",
            PermissibleValue(
                text="SNOMED:81654009",
                title="Coronal"))
        setattr(cls, "SNOMED:83167003",
            PermissibleValue(
                text="SNOMED:83167003",
                title="Intracellular"))
        setattr(cls, "SNOMED:84177009",
            PermissibleValue(
                text="SNOMED:84177009",
                title="Straddling"))
        setattr(cls, "SNOMED:87687004",
            PermissibleValue(
                text="SNOMED:87687004",
                title="Extra-articular"))
        setattr(cls, "SNOMED:90069004",
            PermissibleValue(
                text="SNOMED:90069004",
                title="Posterolateral"))
        setattr(cls, "SNOMED:272424004",
            PermissibleValue(
                text="SNOMED:272424004",
                title="Relative sites (qualifier value)",
                description="Relative sites (qualifier value)"))
        setattr(cls, "SNOMED:112233002",
            PermissibleValue(
                text="SNOMED:112233002",
                title="Marginal"))
        setattr(cls, "SNOMED:1197041002",
            PermissibleValue(
                text="SNOMED:1197041002",
                title="Intercostal"))
        setattr(cls, "SNOMED:1285325005",
            PermissibleValue(
                text="SNOMED:1285325005",
                title="Intralobular"))
        setattr(cls, "SNOMED:128590009",
            PermissibleValue(
                text="SNOMED:128590009",
                title="Anatomical reference point of right atrium"))
        setattr(cls, "SNOMED:1362012009",
            PermissibleValue(
                text="SNOMED:1362012009",
                title="Inlet projection"))
        setattr(cls, "SNOMED:1363295008",
            PermissibleValue(
                text="SNOMED:1363295008",
                title="Unilobar"))
        setattr(cls, "SNOMED:1363296009",
            PermissibleValue(
                text="SNOMED:1363296009",
                title="Ipsilateral multilobar"))
        setattr(cls, "SNOMED:182353008",
            PermissibleValue(
                text="SNOMED:182353008",
                title="Side"))
        setattr(cls, "SNOMED:225780003",
            PermissibleValue(
                text="SNOMED:225780003",
                title="Sublingual"))
        setattr(cls, "SNOMED:229801003",
            PermissibleValue(
                text="SNOMED:229801003",
                title="Intra-arterial"))
        setattr(cls, "SNOMED:255208005",
            PermissibleValue(
                text="SNOMED:255208005",
                title="Ipsilateral"))
        setattr(cls, "SNOMED:255209002",
            PermissibleValue(
                text="SNOMED:255209002",
                title="Contralateral"))
        setattr(cls, "SNOMED:255348000",
            PermissibleValue(
                text="SNOMED:255348000",
                title="Inframammary"))
        setattr(cls, "SNOMED:255472009",
            PermissibleValue(
                text="SNOMED:255472009",
                title="Panretinal"))
        setattr(cls, "SNOMED:255482005",
            PermissibleValue(
                text="SNOMED:255482005",
                title="Left upper segment"))
        setattr(cls, "SNOMED:255486008",
            PermissibleValue(
                text="SNOMED:255486008",
                title="Lower segment"))
        setattr(cls, "SNOMED:255496004",
            PermissibleValue(
                text="SNOMED:255496004",
                title="Right lower segment"))
        setattr(cls, "SNOMED:255499006",
            PermissibleValue(
                text="SNOMED:255499006",
                title="Right upper segment"))
        setattr(cls, "SNOMED:255501003",
            PermissibleValue(
                text="SNOMED:255501003",
                title="Upper segment"))
        setattr(cls, "SNOMED:255546002",
            PermissibleValue(
                text="SNOMED:255546002",
                title="Underlay"))
        setattr(cls, "SNOMED:255547006",
            PermissibleValue(
                text="SNOMED:255547006",
                title="Overlay"))
        setattr(cls, "SNOMED:255548001",
            PermissibleValue(
                text="SNOMED:255548001",
                title="Sandwich graft"))
        setattr(cls, "SNOMED:255549009",
            PermissibleValue(
                text="SNOMED:255549009",
                title="Anterior"))
        setattr(cls, "SNOMED:255550009",
            PermissibleValue(
                text="SNOMED:255550009",
                title="Anterior to epiglottis"))
        setattr(cls, "SNOMED:255551008",
            PermissibleValue(
                text="SNOMED:255551008",
                title="Posterior"))
        setattr(cls, "SNOMED:255552001",
            PermissibleValue(
                text="SNOMED:255552001",
                title="Posterior to epiglottis"))
        setattr(cls, "SNOMED:255554000",
            PermissibleValue(
                text="SNOMED:255554000",
                title="Dorsal"))
        setattr(cls, "SNOMED:255557007",
            PermissibleValue(
                text="SNOMED:255557007",
                title="Intracerebral"))
        setattr(cls, "SNOMED:255558002",
            PermissibleValue(
                text="SNOMED:255558002",
                title="Intragastric"))
        setattr(cls, "SNOMED:255559005",
            PermissibleValue(
                text="SNOMED:255559005",
                title="Intramuscular"))
        setattr(cls, "SNOMED:255560000",
            PermissibleValue(
                text="SNOMED:255560000",
                title="Intravenous"))
        setattr(cls, "SNOMED:255561001",
            PermissibleValue(
                text="SNOMED:255561001",
                title="Medial"))
        setattr(cls, "SNOMED:255562008",
            PermissibleValue(
                text="SNOMED:255562008",
                title="Mid"))
        setattr(cls, "SNOMED:255563003",
            PermissibleValue(
                text="SNOMED:255563003",
                title="Mid-zone"))
        setattr(cls, "SNOMED:255564009",
            PermissibleValue(
                text="SNOMED:255564009",
                title="Perivascular"))
        setattr(cls, "SNOMED:255565005",
            PermissibleValue(
                text="SNOMED:255565005",
                title="Peripapillary"))
        setattr(cls, "SNOMED:255567002",
            PermissibleValue(
                text="SNOMED:255567002",
                title="Postauricular"))
        setattr(cls, "SNOMED:255568007",
            PermissibleValue(
                text="SNOMED:255568007",
                title="Retrosternal"))
        setattr(cls, "SNOMED:255569004",
            PermissibleValue(
                text="SNOMED:255569004",
                title="Suprasternal"))
        setattr(cls, "SNOMED:255579002",
            PermissibleValue(
                text="SNOMED:255579002",
                title="Palatal-lingual"))
        setattr(cls, "SNOMED:255584008",
            PermissibleValue(
                text="SNOMED:255584008",
                title="Septal"))
        setattr(cls, "SNOMED:255690001",
            PermissibleValue(
                text="SNOMED:255690001",
                title="Drug in contact with skin"))
        setattr(cls, "SNOMED:258186003",
            PermissibleValue(
                text="SNOMED:258186003",
                title="Via collaterals"))
        setattr(cls, "SNOMED:258187007",
            PermissibleValue(
                text="SNOMED:258187007",
                title="Via native vessel - graft impaired"))
        setattr(cls, "SNOMED:258188002",
            PermissibleValue(
                text="SNOMED:258188002",
                title="Via native vessel - graft occluded"))
        setattr(cls, "SNOMED:258189005",
            PermissibleValue(
                text="SNOMED:258189005",
                title="Via skip graft"))
        setattr(cls, "SNOMED:258329003",
            PermissibleValue(
                text="SNOMED:258329003",
                title="Supratentorial"))
        setattr(cls, "SNOMED:258330008",
            PermissibleValue(
                text="SNOMED:258330008",
                title="Infratentorial"))
        setattr(cls, "SNOMED:260240005",
            PermissibleValue(
                text="SNOMED:260240005",
                title="Interdental"))
        setattr(cls, "SNOMED:260318004",
            PermissibleValue(
                text="SNOMED:260318004",
                title="1 o'clock position"))
        setattr(cls, "SNOMED:260319007",
            PermissibleValue(
                text="SNOMED:260319007",
                title="1.30 o'clock position"))
        setattr(cls, "SNOMED:260322009",
            PermissibleValue(
                text="SNOMED:260322009",
                title="10 o'clock position"))
        setattr(cls, "SNOMED:260323004",
            PermissibleValue(
                text="SNOMED:260323004",
                title="10.30 o'clock position"))
        setattr(cls, "SNOMED:260324005",
            PermissibleValue(
                text="SNOMED:260324005",
                title="11 o'clock position"))
        setattr(cls, "SNOMED:260325006",
            PermissibleValue(
                text="SNOMED:260325006",
                title="11.30 o'clock position"))
        setattr(cls, "SNOMED:260326007",
            PermissibleValue(
                text="SNOMED:260326007",
                title="12 o'clock position"))
        setattr(cls, "SNOMED:260327003",
            PermissibleValue(
                text="SNOMED:260327003",
                title="12.30 o'clock position"))
        setattr(cls, "SNOMED:260328008",
            PermissibleValue(
                text="SNOMED:260328008",
                title="2 o'clock position"))
        setattr(cls, "SNOMED:260329000",
            PermissibleValue(
                text="SNOMED:260329000",
                title="2.30 o'clock position"))
        setattr(cls, "SNOMED:260330005",
            PermissibleValue(
                text="SNOMED:260330005",
                title="3 o'clock position"))
        setattr(cls, "SNOMED:260331009",
            PermissibleValue(
                text="SNOMED:260331009",
                title="3.30 o'clock position"))
        setattr(cls, "SNOMED:260333007",
            PermissibleValue(
                text="SNOMED:260333007",
                title="4 o'clock position"))
        setattr(cls, "SNOMED:260334001",
            PermissibleValue(
                text="SNOMED:260334001",
                title="4.30 o'clock position"))
        setattr(cls, "SNOMED:260335000",
            PermissibleValue(
                text="SNOMED:260335000",
                title="5 o'clock position"))
        setattr(cls, "SNOMED:260336004",
            PermissibleValue(
                text="SNOMED:260336004",
                title="5.30 o'clock position"))
        setattr(cls, "SNOMED:260337008",
            PermissibleValue(
                text="SNOMED:260337008",
                title="6 o'clock position"))
        setattr(cls, "SNOMED:260338003",
            PermissibleValue(
                text="SNOMED:260338003",
                title="6.30 o'clock position"))
        setattr(cls, "SNOMED:260339006",
            PermissibleValue(
                text="SNOMED:260339006",
                title="7 o'clock position"))
        setattr(cls, "SNOMED:260340008",
            PermissibleValue(
                text="SNOMED:260340008",
                title="7.30 o'clock position"))
        setattr(cls, "SNOMED:260341007",
            PermissibleValue(
                text="SNOMED:260341007",
                title="8 o'clock position"))
        setattr(cls, "SNOMED:260342000",
            PermissibleValue(
                text="SNOMED:260342000",
                title="8.30 o'clock position"))
        setattr(cls, "SNOMED:260343005",
            PermissibleValue(
                text="SNOMED:260343005",
                title="9 o'clock position"))
        setattr(cls, "SNOMED:260344004",
            PermissibleValue(
                text="SNOMED:260344004",
                title="9.30 o'clock position"))
        setattr(cls, "SNOMED:260419006",
            PermissibleValue(
                text="SNOMED:260419006",
                title="Projection"))
        setattr(cls, "SNOMED:260421001",
            PermissibleValue(
                text="SNOMED:260421001",
                title="Left lateral oblique"))
        setattr(cls, "SNOMED:260422008",
            PermissibleValue(
                text="SNOMED:260422008",
                title="C1-C2 left oblique"))
        setattr(cls, "SNOMED:260424009",
            PermissibleValue(
                text="SNOMED:260424009",
                title="Right lateral oblique"))
        setattr(cls, "SNOMED:260425005",
            PermissibleValue(
                text="SNOMED:260425005",
                title="C1-C2 right oblique"))
        setattr(cls, "SNOMED:260426006",
            PermissibleValue(
                text="SNOMED:260426006",
                title="Medial oblique"))
        setattr(cls, "SNOMED:260427002",
            PermissibleValue(
                text="SNOMED:260427002",
                title="Oblique lateral"))
        setattr(cls, "SNOMED:260428007",
            PermissibleValue(
                text="SNOMED:260428007",
                title="Mandible X-ray - lateral oblique"))
        setattr(cls, "SNOMED:260430009",
            PermissibleValue(
                text="SNOMED:260430009",
                title="Anteroposterior left lateral decubitus"))
        setattr(cls, "SNOMED:260431008",
            PermissibleValue(
                text="SNOMED:260431008",
                title="C1-C2 left lateral"))
        setattr(cls, "SNOMED:260432001",
            PermissibleValue(
                text="SNOMED:260432001",
                title="Left true lateral"))
        setattr(cls, "SNOMED:260434000",
            PermissibleValue(
                text="SNOMED:260434000",
                title="Anteroposterior right lateral decubitus"))
        setattr(cls, "SNOMED:260435004",
            PermissibleValue(
                text="SNOMED:260435004",
                title="C1-C2 right lateral"))
        setattr(cls, "SNOMED:260436003",
            PermissibleValue(
                text="SNOMED:260436003",
                title="Right true lateral"))
        setattr(cls, "SNOMED:260437007",
            PermissibleValue(
                text="SNOMED:260437007",
                title="Lateral vertical beam"))
        setattr(cls, "SNOMED:260438002",
            PermissibleValue(
                text="SNOMED:260438002",
                title="Lateral horizontal beam"))
        setattr(cls, "SNOMED:260439005",
            PermissibleValue(
                text="SNOMED:260439005",
                title="Lateral inverted"))
        setattr(cls, "SNOMED:260440007",
            PermissibleValue(
                text="SNOMED:260440007",
                title="True lateral of mandible"))
        setattr(cls, "SNOMED:260441006",
            PermissibleValue(
                text="SNOMED:260441006",
                title="Frog lateral"))
        setattr(cls, "SNOMED:260442004",
            PermissibleValue(
                text="SNOMED:260442004",
                title="Erect lateral"))
        setattr(cls, "SNOMED:260443009",
            PermissibleValue(
                text="SNOMED:260443009",
                title="Anteroposterior inverted"))
        setattr(cls, "SNOMED:260444003",
            PermissibleValue(
                text="SNOMED:260444003",
                title="Rotated posteroanterior"))
        setattr(cls, "SNOMED:260445002",
            PermissibleValue(
                text="SNOMED:260445002",
                title="Posteroanterior 20 degree"))
        setattr(cls, "SNOMED:260446001",
            PermissibleValue(
                text="SNOMED:260446001",
                title="Posteroanterior in ulnar deviation"))
        setattr(cls, "SNOMED:260447005",
            PermissibleValue(
                text="SNOMED:260447005",
                title="Penetrated posteroanterior"))
        setattr(cls, "SNOMED:260450008",
            PermissibleValue(
                text="SNOMED:260450008",
                title="Lordotic projection"))
        setattr(cls, "SNOMED:260451007",
            PermissibleValue(
                text="SNOMED:260451007",
                title="Supine decubitus"))
        setattr(cls, "SNOMED:260452000",
            PermissibleValue(
                text="SNOMED:260452000",
                title="Decubitus"))
        setattr(cls, "SNOMED:260453005",
            PermissibleValue(
                text="SNOMED:260453005",
                title="Internal/external rotation"))
        setattr(cls, "SNOMED:260454004",
            PermissibleValue(
                text="SNOMED:260454004",
                title="45 degree projection"))
        setattr(cls, "SNOMED:260455003",
            PermissibleValue(
                text="SNOMED:260455003",
                title="Head and neck projection"))
        setattr(cls, "SNOMED:260458001",
            PermissibleValue(
                text="SNOMED:260458001",
                title="Slit Towne's"))
        setattr(cls, "SNOMED:260459009",
            PermissibleValue(
                text="SNOMED:260459009",
                title="Reverse Towne's"))
        setattr(cls, "SNOMED:260460004",
            PermissibleValue(
                text="SNOMED:260460004",
                title="Slit 35 degree fronto-occipital"))
        setattr(cls, "SNOMED:260461000",
            PermissibleValue(
                text="SNOMED:260461000",
                title="Vertex projection"))
        setattr(cls, "SNOMED:260463002",
            PermissibleValue(
                text="SNOMED:260463002",
                title="Left Stenver's"))
        setattr(cls, "SNOMED:260464008",
            PermissibleValue(
                text="SNOMED:260464008",
                title="Right Stenver's"))
        setattr(cls, "SNOMED:260465009",
            PermissibleValue(
                text="SNOMED:260465009",
                title="Occipitofrontal projection"))
        setattr(cls, "SNOMED:260466005",
            PermissibleValue(
                text="SNOMED:260466005",
                title="Occipitomental projection"))
        setattr(cls, "SNOMED:260467001",
            PermissibleValue(
                text="SNOMED:260467001",
                title="Occipitomental - erect"))
        setattr(cls, "SNOMED:260468006",
            PermissibleValue(
                text="SNOMED:260468006",
                title="Occipitomental - tilted"))
        setattr(cls, "SNOMED:260469003",
            PermissibleValue(
                text="SNOMED:260469003",
                title="Occipitomental - prone"))
        setattr(cls, "SNOMED:260470002",
            PermissibleValue(
                text="SNOMED:260470002",
                title="Occipitomental - 15 degree"))
        setattr(cls, "SNOMED:260471003",
            PermissibleValue(
                text="SNOMED:260471003",
                title="Occipitomental - 30 degree"))
        setattr(cls, "SNOMED:260472005",
            PermissibleValue(
                text="SNOMED:260472005",
                title="Occipitomental - 45 degree"))
        setattr(cls, "SNOMED:260473000",
            PermissibleValue(
                text="SNOMED:260473000",
                title="Waters - 35 degree tilt to radiographic baseline"))
        setattr(cls, "SNOMED:260475007",
            PermissibleValue(
                text="SNOMED:260475007",
                title="Submentovertical reduced exposure for zygomatic arches"))
        setattr(cls, "SNOMED:260476008",
            PermissibleValue(
                text="SNOMED:260476008",
                title="Slit submentovertical"))
        setattr(cls, "SNOMED:260477004",
            PermissibleValue(
                text="SNOMED:260477004",
                title="Dental/oral projection"))
        setattr(cls, "SNOMED:260478009",
            PermissibleValue(
                text="SNOMED:260478009",
                title="Body - molar"))
        setattr(cls, "SNOMED:260479001",
            PermissibleValue(
                text="SNOMED:260479001",
                title="Body - premolar"))
        setattr(cls, "SNOMED:260481004",
            PermissibleValue(
                text="SNOMED:260481004",
                title="Ramus projection"))
        setattr(cls, "SNOMED:260482006",
            PermissibleValue(
                text="SNOMED:260482006",
                title="Bimolar projection"))
        setattr(cls, "SNOMED:260483001",
            PermissibleValue(
                text="SNOMED:260483001",
                title="Transpharyngeal projection"))
        setattr(cls, "SNOMED:260484007",
            PermissibleValue(
                text="SNOMED:260484007",
                title="Transmaxillary projection"))
        setattr(cls, "SNOMED:260485008",
            PermissibleValue(
                text="SNOMED:260485008",
                title="Temporomandibular joint setting"))
        setattr(cls, "SNOMED:260486009",
            PermissibleValue(
                text="SNOMED:260486009",
                title="Maxillary sinus setting"))
        setattr(cls, "SNOMED:260487000",
            PermissibleValue(
                text="SNOMED:260487000",
                title="Dental panoramic"))
        setattr(cls, "SNOMED:260489002",
            PermissibleValue(
                text="SNOMED:260489002",
                title="Implant setting projection"))
        setattr(cls, "SNOMED:260490006",
            PermissibleValue(
                text="SNOMED:260490006",
                title="Segmental setting"))
        setattr(cls, "SNOMED:260491005",
            PermissibleValue(
                text="SNOMED:260491005",
                title="Axial view for sesamoid bones"))
        setattr(cls, "SNOMED:260492003",
            PermissibleValue(
                text="SNOMED:260492003",
                title="Brewerton's projection"))
        setattr(cls, "SNOMED:260493008",
            PermissibleValue(
                text="SNOMED:260493008",
                title="Harris Beath axial projection"))
        setattr(cls, "SNOMED:260494002",
            PermissibleValue(
                text="SNOMED:260494002",
                title="Intercondylar projection"))
        setattr(cls, "SNOMED:260496000",
            PermissibleValue(
                text="SNOMED:260496000",
                title="Judet projection"))
        setattr(cls, "SNOMED:260497009",
            PermissibleValue(
                text="SNOMED:260497009",
                title="Mortice projection"))
        setattr(cls, "SNOMED:260499007",
            PermissibleValue(
                text="SNOMED:260499007",
                title="Occlusal projection"))
        setattr(cls, "SNOMED:260500003",
            PermissibleValue(
                text="SNOMED:260500003",
                title="Projected oblique occlusal"))
        setattr(cls, "SNOMED:260501004",
            PermissibleValue(
                text="SNOMED:260501004",
                title="Lower true occlusal"))
        setattr(cls, "SNOMED:260502006",
            PermissibleValue(
                text="SNOMED:260502006",
                title="Power grip series"))
        setattr(cls, "SNOMED:260503001",
            PermissibleValue(
                text="SNOMED:260503001",
                title="Radial head projection"))
        setattr(cls, "SNOMED:260504007",
            PermissibleValue(
                text="SNOMED:260504007",
                title="Skyline projection"))
        setattr(cls, "SNOMED:260506009",
            PermissibleValue(
                text="SNOMED:260506009",
                title="Van Rosen projection"))
        setattr(cls, "SNOMED:260514003",
            PermissibleValue(
                text="SNOMED:260514003",
                title="Via body reference line"))
        setattr(cls, "SNOMED:260520002",
            PermissibleValue(
                text="SNOMED:260520002",
                title="Extracorporeal"))
        setattr(cls, "SNOMED:260521003",
            PermissibleValue(
                text="SNOMED:260521003",
                title="Internal"))
        setattr(cls, "SNOMED:260528009",
            PermissibleValue(
                text="SNOMED:260528009",
                title="Median"))
        setattr(cls, "SNOMED:260529001",
            PermissibleValue(
                text="SNOMED:260529001",
                title="Vectors"))
        setattr(cls, "SNOMED:260530006",
            PermissibleValue(
                text="SNOMED:260530006",
                title="Via body region"))
        setattr(cls, "SNOMED:260532003",
            PermissibleValue(
                text="SNOMED:260532003",
                title="Thoracoabdominal"))
        setattr(cls, "SNOMED:260535001",
            PermissibleValue(
                text="SNOMED:260535001",
                title="Lateral extrapleural"))
        setattr(cls, "SNOMED:260541008",
            PermissibleValue(
                text="SNOMED:260541008",
                title="Nasopancreatic"))
        setattr(cls, "SNOMED:260544000",
            PermissibleValue(
                text="SNOMED:260544000",
                title="Endobronchial"))
        setattr(cls, "SNOMED:260549005",
            PermissibleValue(
                text="SNOMED:260549005",
                title="Orogastric"))
        setattr(cls, "SNOMED:260568008",
            PermissibleValue(
                text="SNOMED:260568008",
                title="Via cardiovascular system"))
        setattr(cls, "SNOMED:260602004",
            PermissibleValue(
                text="SNOMED:260602004",
                title="Via superficialized vessel (qualifier value)"))
        setattr(cls, "SNOMED:260620008",
            PermissibleValue(
                text="SNOMED:260620008",
                title="Postaural approach"))
        setattr(cls, "SNOMED:260637001",
            PermissibleValue(
                text="SNOMED:260637001",
                title="Sublabial transseptal"))
        setattr(cls, "SNOMED:260641002",
            PermissibleValue(
                text="SNOMED:260641002",
                title="Extraperitoneal"))
        setattr(cls, "SNOMED:260642009",
            PermissibleValue(
                text="SNOMED:260642009",
                title="Retroperitoneal"))
        setattr(cls, "SNOMED:260668002",
            PermissibleValue(
                text="SNOMED:260668002",
                title="Venovenous"))
        setattr(cls, "SNOMED:261045000",
            PermissibleValue(
                text="SNOMED:261045000",
                title="Anterior dorsal"))
        setattr(cls, "SNOMED:261052003",
            PermissibleValue(
                text="SNOMED:261052003",
                title="Aortocoronary"))
        setattr(cls, "SNOMED:261054002",
            PermissibleValue(
                text="SNOMED:261054002",
                title="Arterio-arterial"))
        setattr(cls, "SNOMED:261055001",
            PermissibleValue(
                text="SNOMED:261055001",
                title="Arteriovenous"))
        setattr(cls, "SNOMED:261057009",
            PermissibleValue(
                text="SNOMED:261057009",
                title="Between intestinal loops"))
        setattr(cls, "SNOMED:261059007",
            PermissibleValue(
                text="SNOMED:261059007",
                title="Bicoronal"))
        setattr(cls, "SNOMED:261065007",
            PermissibleValue(
                text="SNOMED:261065007",
                title="Circumareolar"))
        setattr(cls, "SNOMED:261067004",
            PermissibleValue(
                text="SNOMED:261067004",
                title="Dorsal part"))
        setattr(cls, "SNOMED:261073003",
            PermissibleValue(
                text="SNOMED:261073003",
                title="Epicardial"))
        setattr(cls, "SNOMED:261074009",
            PermissibleValue(
                text="SNOMED:261074009",
                title="External"))
        setattr(cls, "SNOMED:261075005",
            PermissibleValue(
                text="SNOMED:261075005",
                title="Extra-amniotic"))
        setattr(cls, "SNOMED:261076006",
            PermissibleValue(
                text="SNOMED:261076006",
                title="Extracoronal"))
        setattr(cls, "SNOMED:261089000",
            PermissibleValue(
                text="SNOMED:261089000",
                title="Inferior"))
        setattr(cls, "SNOMED:261094000",
            PermissibleValue(
                text="SNOMED:261094000",
                title="Into urinary bladder"))
        setattr(cls, "SNOMED:261095004",
            PermissibleValue(
                text="SNOMED:261095004",
                title="Into ureter"))
        setattr(cls, "SNOMED:261097007",
            PermissibleValue(
                text="SNOMED:261097007",
                title="Intracoronal"))
        setattr(cls, "SNOMED:261100002",
            PermissibleValue(
                text="SNOMED:261100002",
                title="Intraperitoneal"))
        setattr(cls, "SNOMED:261101003",
            PermissibleValue(
                text="SNOMED:261101003",
                title="Intravascular"))
        setattr(cls, "SNOMED:261117009",
            PermissibleValue(
                text="SNOMED:261117009",
                title="Laryngotracheal"))
        setattr(cls, "SNOMED:261119007",
            PermissibleValue(
                text="SNOMED:261119007",
                title="Lateral part"))
        setattr(cls, "SNOMED:261122009",
            PermissibleValue(
                text="SNOMED:261122009",
                title="Lower"))
        setattr(cls, "SNOMED:261123004",
            PermissibleValue(
                text="SNOMED:261123004",
                title="Lower anterior"))
        setattr(cls, "SNOMED:261128008",
            PermissibleValue(
                text="SNOMED:261128008",
                title="Medial part"))
        setattr(cls, "SNOMED:261131009",
            PermissibleValue(
                text="SNOMED:261131009",
                title="Midaxillary"))
        setattr(cls, "SNOMED:261132002",
            PermissibleValue(
                text="SNOMED:261132002",
                title="Midclavicular"))
        setattr(cls, "SNOMED:261133007",
            PermissibleValue(
                text="SNOMED:261133007",
                title="Middle third"))
        setattr(cls, "SNOMED:261136004",
            PermissibleValue(
                text="SNOMED:261136004",
                title="Mural"))
        setattr(cls, "SNOMED:261137008",
            PermissibleValue(
                text="SNOMED:261137008",
                title="Musculocutaneous"))
        setattr(cls, "SNOMED:261146002",
            PermissibleValue(
                text="SNOMED:261146002",
                title="Para-aortic"))
        setattr(cls, "SNOMED:261147006",
            PermissibleValue(
                text="SNOMED:261147006",
                title="Paracolic"))
        setattr(cls, "SNOMED:261148001",
            PermissibleValue(
                text="SNOMED:261148001",
                title="Paraspinal"))
        setattr(cls, "SNOMED:261149009",
            PermissibleValue(
                text="SNOMED:261149009",
                title="Parasternal"))
        setattr(cls, "SNOMED:261154000",
            PermissibleValue(
                text="SNOMED:261154000",
                title="Penis and urinary bladder neck"))
        setattr(cls, "SNOMED:261156003",
            PermissibleValue(
                text="SNOMED:261156003",
                title="Periadrenal"))
        setattr(cls, "SNOMED:261165005",
            PermissibleValue(
                text="SNOMED:261165005",
                title="Posterior dorsal"))
        setattr(cls, "SNOMED:261172006",
            PermissibleValue(
                text="SNOMED:261172006",
                title="Proximal third"))
        setattr(cls, "SNOMED:261174007",
            PermissibleValue(
                text="SNOMED:261174007",
                title="Retrocecal (qualifier value)"))
        setattr(cls, "SNOMED:261175008",
            PermissibleValue(
                text="SNOMED:261175008",
                title="Retroduodenal"))
        setattr(cls, "SNOMED:261181000",
            PermissibleValue(
                text="SNOMED:261181000",
                title="Tracheobronchial"))
        setattr(cls, "SNOMED:261183002",
            PermissibleValue(
                text="SNOMED:261183002",
                title="Upper"))
        setattr(cls, "SNOMED:261184008",
            PermissibleValue(
                text="SNOMED:261184008",
                title="Upper anterior"))
        setattr(cls, "SNOMED:261185009",
            PermissibleValue(
                text="SNOMED:261185009",
                title="Venoarterial"))
        setattr(cls, "SNOMED:261186005",
            PermissibleValue(
                text="SNOMED:261186005",
                title="Ventral part"))
        setattr(cls, "SNOMED:261411001",
            PermissibleValue(
                text="SNOMED:261411001",
                title="Distal third"))
        setattr(cls, "SNOMED:261446009",
            PermissibleValue(
                text="SNOMED:261446009",
                title="Transpulmonary annulus"))
        setattr(cls, "SNOMED:261466000",
            PermissibleValue(
                text="SNOMED:261466000",
                title="Via intrapulmonary trunk tunnel"))
        setattr(cls, "SNOMED:261469007",
            PermissibleValue(
                text="SNOMED:261469007",
                title="Via orbitotomy"))
        setattr(cls, "SNOMED:261760007",
            PermissibleValue(
                text="SNOMED:261760007",
                title="Deep to rectus abdominis"))
        setattr(cls, "SNOMED:261788001",
            PermissibleValue(
                text="SNOMED:261788001",
                title="Exteriorized (qualifier value)"))
        setattr(cls, "SNOMED:261799004",
            PermissibleValue(
                text="SNOMED:261799004",
                title="From existing graft to coronary artery"))
        setattr(cls, "SNOMED:261847009",
            PermissibleValue(
                text="SNOMED:261847009",
                title="Intracervical"))
        setattr(cls, "SNOMED:261851006",
            PermissibleValue(
                text="SNOMED:261851006",
                title="Internally to bladder"))
        setattr(cls, "SNOMED:261945002",
            PermissibleValue(
                text="SNOMED:261945002",
                title="Mixed venoarterial and venovenous"))
        setattr(cls, "SNOMED:261964008",
            PermissibleValue(
                text="SNOMED:261964008",
                title="Muscle fibers only (qualifier value)"))
        setattr(cls, "SNOMED:261980003",
            PermissibleValue(
                text="SNOMED:261980003",
                title="Neuromuscular junction only"))
        setattr(cls, "SNOMED:262379005",
            PermissibleValue(
                text="SNOMED:262379005",
                title="Dominant side"))
        setattr(cls, "SNOMED:262458006",
            PermissibleValue(
                text="SNOMED:262458006",
                title="Non-dominant side"))
        setattr(cls, "SNOMED:263672002",
            PermissibleValue(
                text="SNOMED:263672002",
                title="Anocutaneous"))
        setattr(cls, "SNOMED:263674001",
            PermissibleValue(
                text="SNOMED:263674001",
                title="Anovestibular"))
        setattr(cls, "SNOMED:263759007",
            PermissibleValue(
                text="SNOMED:263759007",
                title="Foraminal"))
        setattr(cls, "SNOMED:263794000",
            PermissibleValue(
                text="SNOMED:263794000",
                title="Left side-by-side"))
        setattr(cls, "SNOMED:263795004",
            PermissibleValue(
                text="SNOMED:263795004",
                title="Left sided"))
        setattr(cls, "SNOMED:263830001",
            PermissibleValue(
                text="SNOMED:263830001",
                title="Panacinar"))
        setattr(cls, "SNOMED:263831002",
            PermissibleValue(
                text="SNOMED:263831002",
                title="Panlobular"))
        setattr(cls, "SNOMED:263838008",
            PermissibleValue(
                text="SNOMED:263838008",
                title="Periacinar"))
        setattr(cls, "SNOMED:263846009",
            PermissibleValue(
                text="SNOMED:263846009",
                title="Prevascular"))
        setattr(cls, "SNOMED:263848005",
            PermissibleValue(
                text="SNOMED:263848005",
                title="Proximal acinar"))
        setattr(cls, "SNOMED:263869007",
            PermissibleValue(
                text="SNOMED:263869007",
                title="Separate"))
        setattr(cls, "SNOMED:263887005",
            PermissibleValue(
                text="SNOMED:263887005",
                title="Subcutaneous"))
        setattr(cls, "SNOMED:263938007",
            PermissibleValue(
                text="SNOMED:263938007",
                title="Above middle turbinate"))
        setattr(cls, "SNOMED:263942005",
            PermissibleValue(
                text="SNOMED:263942005",
                title="Anterior segment"))
        setattr(cls, "SNOMED:263943000",
            PermissibleValue(
                text="SNOMED:263943000",
                title="Anterior wall"))
        setattr(cls, "SNOMED:263952009",
            PermissibleValue(
                text="SNOMED:263952009",
                title="Periorbital"))
        setattr(cls, "SNOMED:263953004",
            PermissibleValue(
                text="SNOMED:263953004",
                title="Perioral"))
        setattr(cls, "SNOMED:263955006",
            PermissibleValue(
                text="SNOMED:263955006",
                title="Atlantoaxial"))
        setattr(cls, "SNOMED:263958008",
            PermissibleValue(
                text="SNOMED:263958008",
                title="Between left common carotid and brachiocephalic arteries"))
        setattr(cls, "SNOMED:263959000",
            PermissibleValue(
                text="SNOMED:263959000",
                title="Between left subclavian and common carotid arteries"))
        setattr(cls, "SNOMED:263965000",
            PermissibleValue(
                text="SNOMED:263965000",
                title="Bronchocutaneous"))
        setattr(cls, "SNOMED:263966004",
            PermissibleValue(
                text="SNOMED:263966004",
                title="Bronchopleural"))
        setattr(cls, "SNOMED:263969006",
            PermissibleValue(
                text="SNOMED:263969006",
                title="Centriacinar"))
        setattr(cls, "SNOMED:263970007",
            PermissibleValue(
                text="SNOMED:263970007",
                title="Centrilobular"))
        setattr(cls, "SNOMED:263974003",
            PermissibleValue(
                text="SNOMED:263974003",
                title="Cervicothoracic"))
        setattr(cls, "SNOMED:263975002",
            PermissibleValue(
                text="SNOMED:263975002",
                title="Cervicothoracolumbar"))
        setattr(cls, "SNOMED:263981005",
            PermissibleValue(
                text="SNOMED:263981005",
                title="Distal to left subclavian artery"))
        setattr(cls, "SNOMED:263990003",
            PermissibleValue(
                text="SNOMED:263990003",
                title="Duodenoduodenal"))
        setattr(cls, "SNOMED:263991004",
            PermissibleValue(
                text="SNOMED:263991004",
                title="Duodenojejunal"))
        setattr(cls, "SNOMED:263996009",
            PermissibleValue(
                text="SNOMED:263996009",
                title="Extrafoveal"))
        setattr(cls, "SNOMED:263997000",
            PermissibleValue(
                text="SNOMED:263997000",
                title="Extraureteric"))
        setattr(cls, "SNOMED:263998005",
            PermissibleValue(
                text="SNOMED:263998005",
                title="Extravaginal"))
        setattr(cls, "SNOMED:263999002",
            PermissibleValue(
                text="SNOMED:263999002",
                title="From anterosuperior-superior bridging leaflet commissure"))
        setattr(cls, "SNOMED:264000000",
            PermissibleValue(
                text="SNOMED:264000000",
                title="From left inferior bridging leaflet-lateral commissure"))
        setattr(cls, "SNOMED:264001001",
            PermissibleValue(
                text="SNOMED:264001001",
                title="From left septal commissure"))
        setattr(cls, "SNOMED:264002008",
            PermissibleValue(
                text="SNOMED:264002008",
                title="From left superior bridging leaflet-lateral commissure"))
        setattr(cls, "SNOMED:264004009",
            PermissibleValue(
                text="SNOMED:264004009",
                title="From left ventricular component"))
        setattr(cls, "SNOMED:264005005",
            PermissibleValue(
                text="SNOMED:264005005",
                title="From right anterosuperior-inferior commissure"))
        setattr(cls, "SNOMED:264006006",
            PermissibleValue(
                text="SNOMED:264006006",
                title="From right inferior bridging leaflet-inferior commissure"))
        setattr(cls, "SNOMED:264007002",
            PermissibleValue(
                text="SNOMED:264007002",
                title="From right septal commissure"))
        setattr(cls, "SNOMED:264008007",
            PermissibleValue(
                text="SNOMED:264008007",
                title="From right ventricular component"))
        setattr(cls, "SNOMED:264011008",
            PermissibleValue(
                text="SNOMED:264011008",
                title="Gastroduodenal"))
        setattr(cls, "SNOMED:264012001",
            PermissibleValue(
                text="SNOMED:264012001",
                title="Gastrogastric"))
        setattr(cls, "SNOMED:264015004",
            PermissibleValue(
                text="SNOMED:264015004",
                title="Hepatopleural"))
        setattr(cls, "SNOMED:264023002",
            PermissibleValue(
                text="SNOMED:264023002",
                title="Ileocecal (qualifier value)"))
        setattr(cls, "SNOMED:264024008",
            PermissibleValue(
                text="SNOMED:264024008",
                title="Ileocolic"))
        setattr(cls, "SNOMED:264025009",
            PermissibleValue(
                text="SNOMED:264025009",
                title="Iliofemoral vein zone"))
        setattr(cls, "SNOMED:264026005",
            PermissibleValue(
                text="SNOMED:264026005",
                title="Ileo-ileal"))
        setattr(cls, "SNOMED:264027001",
            PermissibleValue(
                text="SNOMED:264027001",
                title="Ileorectal"))
        setattr(cls, "SNOMED:264030008",
            PermissibleValue(
                text="SNOMED:264030008",
                title="In joint"))
        setattr(cls, "SNOMED:264031007",
            PermissibleValue(
                text="SNOMED:264031007",
                title="In situ"))
        setattr(cls, "SNOMED:264034004",
            PermissibleValue(
                text="SNOMED:264034004",
                title="Infracardiac"))
        setattr(cls, "SNOMED:264035003",
            PermissibleValue(
                text="SNOMED:264035003",
                title="Infravesical"))
        setattr(cls, "SNOMED:264040006",
            PermissibleValue(
                text="SNOMED:264040006",
                title="Interchordal"))
        setattr(cls, "SNOMED:264041005",
            PermissibleValue(
                text="SNOMED:264041005",
                title="Interdigital"))
        setattr(cls, "SNOMED:264042003",
            PermissibleValue(
                text="SNOMED:264042003",
                title="Intervertebral"))
        setattr(cls, "SNOMED:264043008",
            PermissibleValue(
                text="SNOMED:264043008",
                title="Intraligamentous"))
        setattr(cls, "SNOMED:264044002",
            PermissibleValue(
                text="SNOMED:264044002",
                title="Intracardiac"))
        setattr(cls, "SNOMED:264045001",
            PermissibleValue(
                text="SNOMED:264045001",
                title="Intraluminal"))
        setattr(cls, "SNOMED:264046000",
            PermissibleValue(
                text="SNOMED:264046000",
                title="Intramammary"))
        setattr(cls, "SNOMED:264047009",
            PermissibleValue(
                text="SNOMED:264047009",
                title="Intrapulmonary"))
        setattr(cls, "SNOMED:264049007",
            PermissibleValue(
                text="SNOMED:264049007",
                title="Intravaginal"))
        setattr(cls, "SNOMED:264056001",
            PermissibleValue(
                text="SNOMED:264056001",
                title="Lateral column"))
        setattr(cls, "SNOMED:264060003",
            PermissibleValue(
                text="SNOMED:264060003",
                title="Lateral segment"))
        setattr(cls, "SNOMED:264065008",
            PermissibleValue(
                text="SNOMED:264065008",
                title="Left anterior"))
        setattr(cls, "SNOMED:264067000",
            PermissibleValue(
                text="SNOMED:264067000",
                title="Left lateral wall"))
        setattr(cls, "SNOMED:264068005",
            PermissibleValue(
                text="SNOMED:264068005",
                title="Left lower segment"))
        setattr(cls, "SNOMED:264076007",
            PermissibleValue(
                text="SNOMED:264076007",
                title="Lower left parasternal"))
        setattr(cls, "SNOMED:264081003",
            PermissibleValue(
                text="SNOMED:264081003",
                title="Lower third"))
        setattr(cls, "SNOMED:264083000",
            PermissibleValue(
                text="SNOMED:264083000",
                title="Lumbosacral"))
        setattr(cls, "SNOMED:264096004",
            PermissibleValue(
                text="SNOMED:264096004",
                title="Medial segment"))
        setattr(cls, "SNOMED:264103001",
            PermissibleValue(
                text="SNOMED:264103001",
                title="Midtarsal"))
        setattr(cls, "SNOMED:264107000",
            PermissibleValue(
                text="SNOMED:264107000",
                title="Paravertebral"))
        setattr(cls, "SNOMED:264110007",
            PermissibleValue(
                text="SNOMED:264110007",
                title="Esophagocolonic (qualifier value)"))
        setattr(cls, "SNOMED:264111006",
            PermissibleValue(
                text="SNOMED:264111006",
                title="Esophagogastric (qualifier value)"))
        setattr(cls, "SNOMED:264112004",
            PermissibleValue(
                text="SNOMED:264112004",
                title="Esophagojejunal (qualifier value)"))
        setattr(cls, "SNOMED:264114003",
            PermissibleValue(
                text="SNOMED:264114003",
                title="Ostium"))
        setattr(cls, "SNOMED:264117005",
            PermissibleValue(
                text="SNOMED:264117005",
                title="Paraesophageal (qualifier value)"))
        setattr(cls, "SNOMED:264118000",
            PermissibleValue(
                text="SNOMED:264118000",
                title="Paraduodenal"))
        setattr(cls, "SNOMED:264119008",
            PermissibleValue(
                text="SNOMED:264119008",
                title="Parafoveal"))
        setattr(cls, "SNOMED:264121003",
            PermissibleValue(
                text="SNOMED:264121003",
                title="Paramacular"))
        setattr(cls, "SNOMED:264123000",
            PermissibleValue(
                text="SNOMED:264123000",
                title="Paraseptal"))
        setattr(cls, "SNOMED:264124006",
            PermissibleValue(
                text="SNOMED:264124006",
                title="Paraumbilical"))
        setattr(cls, "SNOMED:264126008",
            PermissibleValue(
                text="SNOMED:264126008",
                title="Paravascular"))
        setattr(cls, "SNOMED:264127004",
            PermissibleValue(
                text="SNOMED:264127004",
                title="Paraovarian"))
        setattr(cls, "SNOMED:264128009",
            PermissibleValue(
                text="SNOMED:264128009",
                title="Paratracheal"))
        setattr(cls, "SNOMED:264131005",
            PermissibleValue(
                text="SNOMED:264131005",
                title="Peri-intestinal"))
        setattr(cls, "SNOMED:264133008",
            PermissibleValue(
                text="SNOMED:264133008",
                title="Perianal"))
        setattr(cls, "SNOMED:264136000",
            PermissibleValue(
                text="SNOMED:264136000",
                title="Perihepatic"))
        setattr(cls, "SNOMED:264137009",
            PermissibleValue(
                text="SNOMED:264137009",
                title="Perinephric"))
        setattr(cls, "SNOMED:264139007",
            PermissibleValue(
                text="SNOMED:264139007",
                title="Peripancreatic"))
        setattr(cls, "SNOMED:264142001",
            PermissibleValue(
                text="SNOMED:264142001",
                title="Perisplenic"))
        setattr(cls, "SNOMED:264153007",
            PermissibleValue(
                text="SNOMED:264153007",
                title="Posterior pole"))
        setattr(cls, "SNOMED:264154001",
            PermissibleValue(
                text="SNOMED:264154001",
                title="Posterior segment"))
        setattr(cls, "SNOMED:264159006",
            PermissibleValue(
                text="SNOMED:264159006",
                title="Posterior wall"))
        setattr(cls, "SNOMED:264168008",
            PermissibleValue(
                text="SNOMED:264168008",
                title="Rectocloacal"))
        setattr(cls, "SNOMED:264169000",
            PermissibleValue(
                text="SNOMED:264169000",
                title="Rectocutaneous"))
        setattr(cls, "SNOMED:264170004",
            PermissibleValue(
                text="SNOMED:264170004",
                title="Rectourethral"))
        setattr(cls, "SNOMED:264171000",
            PermissibleValue(
                text="SNOMED:264171000",
                title="Rectovaginal"))
        setattr(cls, "SNOMED:264172007",
            PermissibleValue(
                text="SNOMED:264172007",
                title="Rectovesical"))
        setattr(cls, "SNOMED:264173002",
            PermissibleValue(
                text="SNOMED:264173002",
                title="Rectovulval"))
        setattr(cls, "SNOMED:264174008",
            PermissibleValue(
                text="SNOMED:264174008",
                title="Retromammary"))
        setattr(cls, "SNOMED:264175009",
            PermissibleValue(
                text="SNOMED:264175009",
                title="Retrocolumellar"))
        setattr(cls, "SNOMED:264176005",
            PermissibleValue(
                text="SNOMED:264176005",
                title="Right anterior"))
        setattr(cls, "SNOMED:264178006",
            PermissibleValue(
                text="SNOMED:264178006",
                title="Right lateral wall"))
        setattr(cls, "SNOMED:264179003",
            PermissibleValue(
                text="SNOMED:264179003",
                title="Right side-by-side"))
        setattr(cls, "SNOMED:264180000",
            PermissibleValue(
                text="SNOMED:264180000",
                title="Right sided"))
        setattr(cls, "SNOMED:264193005",
            PermissibleValue(
                text="SNOMED:264193005",
                title="Segment"))
        setattr(cls, "SNOMED:264201006",
            PermissibleValue(
                text="SNOMED:264201006",
                title="Sternocostal"))
        setattr(cls, "SNOMED:264202004",
            PermissibleValue(
                text="SNOMED:264202004",
                title="Subaortic"))
        setattr(cls, "SNOMED:264205002",
            PermissibleValue(
                text="SNOMED:264205002",
                title="Subareolar"))
        setattr(cls, "SNOMED:264206001",
            PermissibleValue(
                text="SNOMED:264206001",
                title="Subconjunctival"))
        setattr(cls, "SNOMED:264208000",
            PermissibleValue(
                text="SNOMED:264208000",
                title="Subcostal"))
        setattr(cls, "SNOMED:264209008",
            PermissibleValue(
                text="SNOMED:264209008",
                title="Subfoveal"))
        setattr(cls, "SNOMED:264216009",
            PermissibleValue(
                text="SNOMED:264216009",
                title="Superficial to rectus abdominis"))
        setattr(cls, "SNOMED:264217000",
            PermissibleValue(
                text="SNOMED:264217000",
                title="Superior"))
        setattr(cls, "SNOMED:264221007",
            PermissibleValue(
                text="SNOMED:264221007",
                title="Supraumbilical"))
        setattr(cls, "SNOMED:264222000",
            PermissibleValue(
                text="SNOMED:264222000",
                title="Supracardiac"))
        setattr(cls, "SNOMED:264224004",
            PermissibleValue(
                text="SNOMED:264224004",
                title="Supraglottic"))
        setattr(cls, "SNOMED:264225003",
            PermissibleValue(
                text="SNOMED:264225003",
                title="Suprahepatic"))
        setattr(cls, "SNOMED:264227006",
            PermissibleValue(
                text="SNOMED:264227006",
                title="Tarsometatarsal"))
        setattr(cls, "SNOMED:264232007",
            PermissibleValue(
                text="SNOMED:264232007",
                title="Thoracolumbar"))
        setattr(cls, "SNOMED:264245006",
            PermissibleValue(
                text="SNOMED:264245006",
                title="Upper left parasternal"))
        setattr(cls, "SNOMED:264253003",
            PermissibleValue(
                text="SNOMED:264253003",
                title="Upper third"))
        setattr(cls, "SNOMED:264261008",
            PermissibleValue(
                text="SNOMED:264261008",
                title="Cholecystoduodenal"))
        setattr(cls, "SNOMED:264262001",
            PermissibleValue(
                text="SNOMED:264262001",
                title="Cholecystenteric (qualifier value)"))
        setattr(cls, "SNOMED:264263006",
            PermissibleValue(
                text="SNOMED:264263006",
                title="Cholecystogastric"))
        setattr(cls, "SNOMED:264264000",
            PermissibleValue(
                text="SNOMED:264264000",
                title="Choledochoduodenal"))
        setattr(cls, "SNOMED:264266003",
            PermissibleValue(
                text="SNOMED:264266003",
                title="Colocolic"))
        setattr(cls, "SNOMED:264267007",
            PermissibleValue(
                text="SNOMED:264267007",
                title="Colorectal"))
        setattr(cls, "SNOMED:264463009",
            PermissibleValue(
                text="SNOMED:264463009",
                title="Epitrochlear"))
        setattr(cls, "SNOMED:264940008",
            PermissibleValue(
                text="SNOMED:264940008",
                title="Under inferior bridging leaflet"))
        setattr(cls, "SNOMED:264941007",
            PermissibleValue(
                text="SNOMED:264941007",
                title="Under superior bridging leaflet"))
        setattr(cls, "SNOMED:272288000",
            PermissibleValue(
                text="SNOMED:272288000",
                title="Onlay"))
        setattr(cls, "SNOMED:272425003",
            PermissibleValue(
                text="SNOMED:272425003",
                title="General site descriptor"))
        setattr(cls, "SNOMED:272427006",
            PermissibleValue(
                text="SNOMED:272427006",
                title="Anatomical part descriptor"))
        setattr(cls, "SNOMED:272428001",
            PermissibleValue(
                text="SNOMED:272428001",
                title="Anatomical third"))
        setattr(cls, "SNOMED:272429009",
            PermissibleValue(
                text="SNOMED:272429009",
                title="Part structure"))
        setattr(cls, "SNOMED:272430004",
            PermissibleValue(
                text="SNOMED:272430004",
                title="Column structure"))
        setattr(cls, "SNOMED:272431000",
            PermissibleValue(
                text="SNOMED:272431000",
                title="Segment structure"))
        setattr(cls, "SNOMED:272432007",
            PermissibleValue(
                text="SNOMED:272432007",
                title="Wall structure"))
        setattr(cls, "SNOMED:272434008",
            PermissibleValue(
                text="SNOMED:272434008",
                title="Anatomical relationship descriptor"))
        setattr(cls, "SNOMED:272435009",
            PermissibleValue(
                text="SNOMED:272435009",
                title="Centri-location"))
        setattr(cls, "SNOMED:272436005",
            PermissibleValue(
                text="SNOMED:272436005",
                title="Circum-location"))
        setattr(cls, "SNOMED:272437001",
            PermissibleValue(
                text="SNOMED:272437001",
                title="Extra-location"))
        setattr(cls, "SNOMED:272438006",
            PermissibleValue(
                text="SNOMED:272438006",
                title="Extrapleural"))
        setattr(cls, "SNOMED:272439003",
            PermissibleValue(
                text="SNOMED:272439003",
                title="Infra-location"))
        setattr(cls, "SNOMED:272440001",
            PermissibleValue(
                text="SNOMED:272440001",
                title="Inter-location"))
        setattr(cls, "SNOMED:272441002",
            PermissibleValue(
                text="SNOMED:272441002",
                title="Intra-location"))
        setattr(cls, "SNOMED:272442009",
            PermissibleValue(
                text="SNOMED:272442009",
                title="Mid-location"))
        setattr(cls, "SNOMED:272443004",
            PermissibleValue(
                text="SNOMED:272443004",
                title="Pan-location"))
        setattr(cls, "SNOMED:272444005",
            PermissibleValue(
                text="SNOMED:272444005",
                title="Para-location"))
        setattr(cls, "SNOMED:272446007",
            PermissibleValue(
                text="SNOMED:272446007",
                title="Per-location"))
        setattr(cls, "SNOMED:272447003",
            PermissibleValue(
                text="SNOMED:272447003",
                title="Peri-location"))
        setattr(cls, "SNOMED:272448008",
            PermissibleValue(
                text="SNOMED:272448008",
                title="Post-location"))
        setattr(cls, "SNOMED:272449000",
            PermissibleValue(
                text="SNOMED:272449000",
                title="Pre-location"))
        setattr(cls, "SNOMED:272450000",
            PermissibleValue(
                text="SNOMED:272450000",
                title="Retro-location"))
        setattr(cls, "SNOMED:272451001",
            PermissibleValue(
                text="SNOMED:272451001",
                title="Sub-location"))
        setattr(cls, "SNOMED:272452008",
            PermissibleValue(
                text="SNOMED:272452008",
                title="Supra-location"))
        setattr(cls, "SNOMED:272455005",
            PermissibleValue(
                text="SNOMED:272455005",
                title="Inferosuperior projection"))
        setattr(cls, "SNOMED:272456006",
            PermissibleValue(
                text="SNOMED:272456006",
                title="Apical projection"))
        setattr(cls, "SNOMED:272457002",
            PermissibleValue(
                text="SNOMED:272457002",
                title="Vertical projection"))
        setattr(cls, "SNOMED:272458007",
            PermissibleValue(
                text="SNOMED:272458007",
                title="Prone projection"))
        setattr(cls, "SNOMED:272459004",
            PermissibleValue(
                text="SNOMED:272459004",
                title="Supine projection"))
        setattr(cls, "SNOMED:272460009",
            PermissibleValue(
                text="SNOMED:272460009",
                title="Anterior projection"))
        setattr(cls, "SNOMED:272461008",
            PermissibleValue(
                text="SNOMED:272461008",
                title="Right posterior projection"))
        setattr(cls, "SNOMED:272462001",
            PermissibleValue(
                text="SNOMED:272462001",
                title="Left posterior projection"))
        setattr(cls, "SNOMED:272464000",
            PermissibleValue(
                text="SNOMED:272464000",
                title="Perorbital projection"))
        setattr(cls, "SNOMED:272465004",
            PermissibleValue(
                text="SNOMED:272465004",
                title="Temporomandibular joint projection"))
        setattr(cls, "SNOMED:272466003",
            PermissibleValue(
                text="SNOMED:272466003",
                title="Optic foramen projection"))
        setattr(cls, "SNOMED:272467007",
            PermissibleValue(
                text="SNOMED:272467007",
                title="Lateral facial skeleton projection"))
        setattr(cls, "SNOMED:272468002",
            PermissibleValue(
                text="SNOMED:272468002",
                title="Ear projection"))
        setattr(cls, "SNOMED:272469005",
            PermissibleValue(
                text="SNOMED:272469005",
                title="Mid face projection"))
        setattr(cls, "SNOMED:272470006",
            PermissibleValue(
                text="SNOMED:272470006",
                title="Cervical spine projection"))
        setattr(cls, "SNOMED:272472003",
            PermissibleValue(
                text="SNOMED:272472003",
                title="Macro projection"))
        setattr(cls, "SNOMED:272473008",
            PermissibleValue(
                text="SNOMED:272473008",
                title="Outlet projection"))
        setattr(cls, "SNOMED:272474002",
            PermissibleValue(
                text="SNOMED:272474002",
                title="Swimmer's projection"))
        setattr(cls, "SNOMED:272475001",
            PermissibleValue(
                text="SNOMED:272475001",
                title="Tibial tuberosity projection"))
        setattr(cls, "SNOMED:272476000",
            PermissibleValue(
                text="SNOMED:272476000",
                title="Transthoracic projection"))
        setattr(cls, "SNOMED:272478004",
            PermissibleValue(
                text="SNOMED:272478004",
                title="Transcranial projection"))
        setattr(cls, "SNOMED:272479007",
            PermissibleValue(
                text="SNOMED:272479007",
                title="Posteroanterior projection"))
        setattr(cls, "SNOMED:272480005",
            PermissibleValue(
                text="SNOMED:272480005",
                title="Horizontal projection"))
        setattr(cls, "SNOMED:272481009",
            PermissibleValue(
                text="SNOMED:272481009",
                title="Erect projection"))
        setattr(cls, "SNOMED:272482002",
            PermissibleValue(
                text="SNOMED:272482002",
                title="Adduction projection"))
        setattr(cls, "SNOMED:272483007",
            PermissibleValue(
                text="SNOMED:272483007",
                title="True projection"))
        setattr(cls, "SNOMED:272484001",
            PermissibleValue(
                text="SNOMED:272484001",
                title="Contralateral projection"))
        setattr(cls, "SNOMED:272485000",
            PermissibleValue(
                text="SNOMED:272485000",
                title="Clockface position"))
        setattr(cls, "SNOMED:272486004",
            PermissibleValue(
                text="SNOMED:272486004",
                title="Trans-direction"))
        setattr(cls, "SNOMED:272487008",
            PermissibleValue(
                text="SNOMED:272487008",
                title="Into-structure"))
        setattr(cls, "SNOMED:272488003",
            PermissibleValue(
                text="SNOMED:272488003",
                title="From-structure"))
        setattr(cls, "SNOMED:272489006",
            PermissibleValue(
                text="SNOMED:272489006",
                title="Via values"))
        setattr(cls, "SNOMED:272496008",
            PermissibleValue(
                text="SNOMED:272496008",
                title="Via incision"))
        setattr(cls, "SNOMED:276749003",
            PermissibleValue(
                text="SNOMED:276749003",
                title="Epi-location"))
        setattr(cls, "SNOMED:276825009",
            PermissibleValue(
                text="SNOMED:276825009",
                title="Overlapping sites"))
        setattr(cls, "SNOMED:276979001",
            PermissibleValue(
                text="SNOMED:276979001",
                title="Aortoiliac"))
        setattr(cls, "SNOMED:277292000",
            PermissibleValue(
                text="SNOMED:277292000",
                title="Endo-location"))
        setattr(cls, "SNOMED:277407002",
            PermissibleValue(
                text="SNOMED:277407002",
                title="Deep locations"))
        setattr(cls, "SNOMED:277409004",
            PermissibleValue(
                text="SNOMED:277409004",
                title="Superficial locations"))
        setattr(cls, "SNOMED:277410009",
            PermissibleValue(
                text="SNOMED:277410009",
                title="Anterior locations"))
        setattr(cls, "SNOMED:277411008",
            PermissibleValue(
                text="SNOMED:277411008",
                title="Posterior locations"))
        setattr(cls, "SNOMED:277412001",
            PermissibleValue(
                text="SNOMED:277412001",
                title="Proximal locations"))
        setattr(cls, "SNOMED:277413006",
            PermissibleValue(
                text="SNOMED:277413006",
                title="Distal locations"))
        setattr(cls, "SNOMED:277414000",
            PermissibleValue(
                text="SNOMED:277414000",
                title="Between locations"))
        setattr(cls, "SNOMED:277415004",
            PermissibleValue(
                text="SNOMED:277415004",
                title="Above locations"))
        setattr(cls, "SNOMED:277593009",
            PermissibleValue(
                text="SNOMED:277593009",
                title="Right posterior"))
        setattr(cls, "SNOMED:277594003",
            PermissibleValue(
                text="SNOMED:277594003",
                title="Left posterior"))
        setattr(cls, "SNOMED:277681008",
            PermissibleValue(
                text="SNOMED:277681008",
                title="Intrastomal"))
        setattr(cls, "SNOMED:277685004",
            PermissibleValue(
                text="SNOMED:277685004",
                title="Tubo-ovarian"))
        setattr(cls, "SNOMED:277686003",
            PermissibleValue(
                text="SNOMED:277686003",
                title="Peritubular"))
        setattr(cls, "SNOMED:277806003",
            PermissibleValue(
                text="SNOMED:277806003",
                title="Sidedness"))
        setattr(cls, "SNOMED:278227002",
            PermissibleValue(
                text="SNOMED:278227002",
                title="Limited structures"))
        setattr(cls, "SNOMED:278255003",
            PermissibleValue(
                text="SNOMED:278255003",
                title="Posterior projection"))
        setattr(cls, "SNOMED:278267001",
            PermissibleValue(
                text="SNOMED:278267001",
                title="Abduction projection"))
        setattr(cls, "SNOMED:278318001",
            PermissibleValue(
                text="SNOMED:278318001",
                title="Transorbital projection"))
        setattr(cls, "SNOMED:278701003",
            PermissibleValue(
                text="SNOMED:278701003",
                title="Periumbilical"))
        setattr(cls, "SNOMED:278702005",
            PermissibleValue(
                text="SNOMED:278702005",
                title="Transumbilical"))
        setattr(cls, "SNOMED:285418008",
            PermissibleValue(
                text="SNOMED:285418008",
                title="Subcuticular"))
        setattr(cls, "SNOMED:298107004",
            PermissibleValue(
                text="SNOMED:298107004",
                title="Orthotopic"))
        setattr(cls, "SNOMED:298108009",
            PermissibleValue(
                text="SNOMED:298108009",
                title="Heterotopic"))
        setattr(cls, "SNOMED:298109001",
            PermissibleValue(
                text="SNOMED:298109001",
                title="Ectopic"))
        setattr(cls, "SNOMED:303218009",
            PermissibleValue(
                text="SNOMED:303218009",
                title="Subfascial"))
        setattr(cls, "SNOMED:303231004",
            PermissibleValue(
                text="SNOMED:303231004",
                title="Intracranial"))
        setattr(cls, "SNOMED:303232006",
            PermissibleValue(
                text="SNOMED:303232006",
                title="Extracranial"))
        setattr(cls, "SNOMED:303483009",
            PermissibleValue(
                text="SNOMED:303483009",
                title="Subcranial"))
        setattr(cls, "SNOMED:304047000",
            PermissibleValue(
                text="SNOMED:304047000",
                title="Transannular"))
        setattr(cls, "SNOMED:304059001",
            PermissibleValue(
                text="SNOMED:304059001",
                title="Endocardial"))
        setattr(cls, "SNOMED:306766009",
            PermissibleValue(
                text="SNOMED:306766009",
                title="Low - site descriptor"))
        setattr(cls, "SNOMED:306767000",
            PermissibleValue(
                text="SNOMED:306767000",
                title="High - site descriptor"))
        setattr(cls, "SNOMED:312206004",
            PermissibleValue(
                text="SNOMED:312206004",
                title="Periapical"))
        setattr(cls, "SNOMED:3583002",
            PermissibleValue(
                text="SNOMED:3583002",
                title="Caudal"))
        setattr(cls, "SNOMED:373863008",
            PermissibleValue(
                text="SNOMED:373863008",
                title="Intracavitary"))
        setattr(cls, "SNOMED:397406000",
            PermissibleValue(
                text="SNOMED:397406000",
                title="Collateral branch of vessel"))
        setattr(cls, "SNOMED:397421006",
            PermissibleValue(
                text="SNOMED:397421006",
                title="Vessel origin"))
        setattr(cls, "SNOMED:398236008",
            PermissibleValue(
                text="SNOMED:398236008",
                title="Intrauterine"))
        setattr(cls, "SNOMED:398994001",
            PermissibleValue(
                text="SNOMED:398994001",
                title="Five chamber view"))
        setattr(cls, "SNOMED:398996004",
            PermissibleValue(
                text="SNOMED:398996004",
                title="Leonard-George projection"))
        setattr(cls, "SNOMED:398998003",
            PermissibleValue(
                text="SNOMED:398998003",
                title="Right ventricular inflow tract view"))
        setattr(cls, "SNOMED:399000008",
            PermissibleValue(
                text="SNOMED:399000008",
                title="Mayer projection"))
        setattr(cls, "SNOMED:399001007",
            PermissibleValue(
                text="SNOMED:399001007",
                title="Posterior emissive projection"))
        setattr(cls, "SNOMED:399002000",
            PermissibleValue(
                text="SNOMED:399002000",
                title="Nolke projection"))
        setattr(cls, "SNOMED:399003005",
            PermissibleValue(
                text="SNOMED:399003005",
                title="Hughston projection"))
        setattr(cls, "SNOMED:399004004",
            PermissibleValue(
                text="SNOMED:399004004",
                title="Oblique axial projection"))
        setattr(cls, "SNOMED:399005003",
            PermissibleValue(
                text="SNOMED:399005003",
                title="Miller projection"))
        setattr(cls, "SNOMED:399006002",
            PermissibleValue(
                text="SNOMED:399006002",
                title="Left posterior oblique projection"))
        setattr(cls, "SNOMED:399011000",
            PermissibleValue(
                text="SNOMED:399011000",
                title="Axillary tail mammography view"))
        setattr(cls, "SNOMED:399012007",
            PermissibleValue(
                text="SNOMED:399012007",
                title="Medial-lateral emissive projection"))
        setattr(cls, "SNOMED:399013002",
            PermissibleValue(
                text="SNOMED:399013002",
                title="Chassard-Lapin projection"))
        setattr(cls, "SNOMED:399022001",
            PermissibleValue(
                text="SNOMED:399022001",
                title="Pirie projection"))
        setattr(cls, "SNOMED:399024000",
            PermissibleValue(
                text="SNOMED:399024000",
                title="May projection"))
        setattr(cls, "SNOMED:399025004",
            PermissibleValue(
                text="SNOMED:399025004",
                title="Ischerwood projection"))
        setattr(cls, "SNOMED:399026003",
            PermissibleValue(
                text="SNOMED:399026003",
                title="Zanelli projection"))
        setattr(cls, "SNOMED:399028002",
            PermissibleValue(
                text="SNOMED:399028002",
                title="Clements projection"))
        setattr(cls, "SNOMED:399033003",
            PermissibleValue(
                text="SNOMED:399033003",
                title="Frontal projection"))
        setattr(cls, "SNOMED:399036006",
            PermissibleValue(
                text="SNOMED:399036006",
                title="Parasternal short axis view at the mitral valve level"))
        setattr(cls, "SNOMED:399037002",
            PermissibleValue(
                text="SNOMED:399037002",
                title="Lewis projection"))
        setattr(cls, "SNOMED:399038007",
            PermissibleValue(
                text="SNOMED:399038007",
                title="Right posterior oblique projection"))
        setattr(cls, "SNOMED:399043000",
            PermissibleValue(
                text="SNOMED:399043000",
                title="Cardiac imaging views"))
        setattr(cls, "SNOMED:399059000",
            PermissibleValue(
                text="SNOMED:399059000",
                title="Postero-anterior oblique projection"))
        setattr(cls, "SNOMED:399061009",
            PermissibleValue(
                text="SNOMED:399061009",
                title="Axial projection"))
        setattr(cls, "SNOMED:399065000",
            PermissibleValue(
                text="SNOMED:399065000",
                title="Causton projection"))
        setattr(cls, "SNOMED:399067008",
            PermissibleValue(
                text="SNOMED:399067008",
                title="Lateral projection"))
        setattr(cls, "SNOMED:399071006",
            PermissibleValue(
                text="SNOMED:399071006",
                title="Plantodorsal projection"))
        setattr(cls, "SNOMED:399073009",
            PermissibleValue(
                text="SNOMED:399073009",
                title="Fuchs projection"))
        setattr(cls, "SNOMED:399074003",
            PermissibleValue(
                text="SNOMED:399074003",
                title="Left anterior oblique emissive projection"))
        setattr(cls, "SNOMED:399075002",
            PermissibleValue(
                text="SNOMED:399075002",
                title="Right posterior oblique emissive projection"))
        setattr(cls, "SNOMED:399080006",
            PermissibleValue(
                text="SNOMED:399080006",
                title="Kuchendorf projection"))
        setattr(cls, "SNOMED:399082003",
            PermissibleValue(
                text="SNOMED:399082003",
                title="Gaynor-Hart projection"))
        setattr(cls, "SNOMED:399083008",
            PermissibleValue(
                text="SNOMED:399083008",
                title="Hsieh projection"))
        setattr(cls, "SNOMED:399089007",
            PermissibleValue(
                text="SNOMED:399089007",
                title="Oblique axial emissive projection"))
        setattr(cls, "SNOMED:399098005",
            PermissibleValue(
                text="SNOMED:399098005",
                title="Staunig projection"))
        setattr(cls, "SNOMED:399099002",
            PermissibleValue(
                text="SNOMED:399099002",
                title="Latero-medial oblique projection"))
        setattr(cls, "SNOMED:399101009",
            PermissibleValue(
                text="SNOMED:399101009",
                title="Cranio-caudal projection exaggerated medially"))
        setattr(cls, "SNOMED:399103007",
            PermissibleValue(
                text="SNOMED:399103007",
                title="Friedman projection"))
        setattr(cls, "SNOMED:399106004",
            PermissibleValue(
                text="SNOMED:399106004",
                title="Suprasternal long axis view"))
        setattr(cls, "SNOMED:399108003",
            PermissibleValue(
                text="SNOMED:399108003",
                title="Right anterior oblique emissive projection"))
        setattr(cls, "SNOMED:399110001",
            PermissibleValue(
                text="SNOMED:399110001",
                title="Tangential projection"))
        setattr(cls, "SNOMED:399113004",
            PermissibleValue(
                text="SNOMED:399113004",
                title="Eponymous projection"))
        setattr(cls, "SNOMED:399118008",
            PermissibleValue(
                text="SNOMED:399118008",
                title="Left lateral emissive projection"))
        setattr(cls, "SNOMED:399125001",
            PermissibleValue(
                text="SNOMED:399125001",
                title="Twining projection"))
        setattr(cls, "SNOMED:399127009",
            PermissibleValue(
                text="SNOMED:399127009",
                title="Teufel projection"))
        setattr(cls, "SNOMED:399129007",
            PermissibleValue(
                text="SNOMED:399129007",
                title="Holly projection"))
        setattr(cls, "SNOMED:399130002",
            PermissibleValue(
                text="SNOMED:399130002",
                title="West Point projection"))
        setattr(cls, "SNOMED:399132005",
            PermissibleValue(
                text="SNOMED:399132005",
                title="Frontal-oblique axial projection"))
        setattr(cls, "SNOMED:399135007",
            PermissibleValue(
                text="SNOMED:399135007",
                title="Left anterior oblique projection"))
        setattr(cls, "SNOMED:399136008",
            PermissibleValue(
                text="SNOMED:399136008",
                title="Left posterior oblique emissive projection"))
        setattr(cls, "SNOMED:399138009",
            PermissibleValue(
                text="SNOMED:399138009",
                title="Penner projection"))
        setattr(cls, "SNOMED:399139001",
            PermissibleValue(
                text="SNOMED:399139001",
                title="Parasternal long axis view"))
        setattr(cls, "SNOMED:399142007",
            PermissibleValue(
                text="SNOMED:399142007",
                title="Albers-Schönberg projection"))
        setattr(cls, "SNOMED:399145009",
            PermissibleValue(
                text="SNOMED:399145009",
                title="Suprasternal short axis view"))
        setattr(cls, "SNOMED:399146005",
            PermissibleValue(
                text="SNOMED:399146005",
                title="Grashey projection"))
        setattr(cls, "SNOMED:399148006",
            PermissibleValue(
                text="SNOMED:399148006",
                title="Chamberlain projection"))
        setattr(cls, "SNOMED:399152006",
            PermissibleValue(
                text="SNOMED:399152006",
                title="Kandel projection"))
        setattr(cls, "SNOMED:399156009",
            PermissibleValue(
                text="SNOMED:399156009",
                title="Laquerriere-Pierquin projection"))
        setattr(cls, "SNOMED:399157000",
            PermissibleValue(
                text="SNOMED:399157000",
                title="Norgaard's projection"))
        setattr(cls, "SNOMED:399159002",
            PermissibleValue(
                text="SNOMED:399159002",
                title="Latero-medial oblique emissive projection"))
        setattr(cls, "SNOMED:399160007",
            PermissibleValue(
                text="SNOMED:399160007",
                title="Frontal oblique projection"))
        setattr(cls, "SNOMED:399161006",
            PermissibleValue(
                text="SNOMED:399161006",
                title="Cleavage mammography view"))
        setattr(cls, "SNOMED:399162004",
            PermissibleValue(
                text="SNOMED:399162004",
                title="Cranio-caudal projection"))
        setattr(cls, "SNOMED:399163009",
            PermissibleValue(
                text="SNOMED:399163009",
                title="Magnified projection"))
        setattr(cls, "SNOMED:399168000",
            PermissibleValue(
                text="SNOMED:399168000",
                title="Hough projection"))
        setattr(cls, "SNOMED:399169008",
            PermissibleValue(
                text="SNOMED:399169008",
                title="Lauenstein projection"))
        setattr(cls, "SNOMED:399171008",
            PermissibleValue(
                text="SNOMED:399171008",
                title="Ottonello projection"))
        setattr(cls, "SNOMED:399173006",
            PermissibleValue(
                text="SNOMED:399173006",
                title="Left lateral projection"))
        setattr(cls, "SNOMED:399179005",
            PermissibleValue(
                text="SNOMED:399179005",
                title="Lawrence projection"))
        setattr(cls, "SNOMED:399181007",
            PermissibleValue(
                text="SNOMED:399181007",
                title="Pawlow projection"))
        setattr(cls, "SNOMED:399182000",
            PermissibleValue(
                text="SNOMED:399182000",
                title="Oblique projection"))
        setattr(cls, "SNOMED:399184004",
            PermissibleValue(
                text="SNOMED:399184004",
                title="Left oblique projection"))
        setattr(cls, "SNOMED:399188001",
            PermissibleValue(
                text="SNOMED:399188001",
                title="Superolateral to inferomedial oblique projection"))
        setattr(cls, "SNOMED:399192008",
            PermissibleValue(
                text="SNOMED:399192008",
                title="Cranio-caudal projection exaggerated laterally"))
        setattr(cls, "SNOMED:399195005",
            PermissibleValue(
                text="SNOMED:399195005",
                title="Right ventricular outflow tract view"))
        setattr(cls, "SNOMED:399196006",
            PermissibleValue(
                text="SNOMED:399196006",
                title="Caudo-cranial projection"))
        setattr(cls, "SNOMED:399198007",
            PermissibleValue(
                text="SNOMED:399198007",
                title="Right lateral projection"))
        setattr(cls, "SNOMED:399199004",
            PermissibleValue(
                text="SNOMED:399199004",
                title="Henschen projection"))
        setattr(cls, "SNOMED:399200001",
            PermissibleValue(
                text="SNOMED:399200001",
                title="Subcostal short axis view"))
        setattr(cls, "SNOMED:399201002",
            PermissibleValue(
                text="SNOMED:399201002",
                title="Judd projection"))
        setattr(cls, "SNOMED:399206007",
            PermissibleValue(
                text="SNOMED:399206007",
                title="Law projection"))
        setattr(cls, "SNOMED:399212002",
            PermissibleValue(
                text="SNOMED:399212002",
                title="Camp-Coventry projection"))
        setattr(cls, "SNOMED:399214001",
            PermissibleValue(
                text="SNOMED:399214001",
                title="Apical four chamber view"))
        setattr(cls, "SNOMED:399215000",
            PermissibleValue(
                text="SNOMED:399215000",
                title="Wigby-Taylor projection"))
        setattr(cls, "SNOMED:399218003",
            PermissibleValue(
                text="SNOMED:399218003",
                title="Arcelin projection"))
        setattr(cls, "SNOMED:399225005",
            PermissibleValue(
                text="SNOMED:399225005",
                title="Oblique caudo-cranial projection"))
        setattr(cls, "SNOMED:399227002",
            PermissibleValue(
                text="SNOMED:399227002",
                title="Kemp Harper projection"))
        setattr(cls, "SNOMED:399232001",
            PermissibleValue(
                text="SNOMED:399232001",
                title="Apical two chamber view"))
        setattr(cls, "SNOMED:399234000",
            PermissibleValue(
                text="SNOMED:399234000",
                title="Rhese projection"))
        setattr(cls, "SNOMED:399236003",
            PermissibleValue(
                text="SNOMED:399236003",
                title="Right oblique projection"))
        setattr(cls, "SNOMED:399237007",
            PermissibleValue(
                text="SNOMED:399237007",
                title="Alexander projection"))
        setattr(cls, "SNOMED:399239005",
            PermissibleValue(
                text="SNOMED:399239005",
                title="Parasternal short axis view at the aortic valve level"))
        setattr(cls, "SNOMED:399241006",
            PermissibleValue(
                text="SNOMED:399241006",
                title="Titterington projection"))
        setattr(cls, "SNOMED:399242004",
            PermissibleValue(
                text="SNOMED:399242004",
                title="Acanthioparietal projection"))
        setattr(cls, "SNOMED:399243009",
            PermissibleValue(
                text="SNOMED:399243009",
                title="Settegast projection"))
        setattr(cls, "SNOMED:399245002",
            PermissibleValue(
                text="SNOMED:399245002",
                title="Cleaves projection"))
        setattr(cls, "SNOMED:399246001",
            PermissibleValue(
                text="SNOMED:399246001",
                title="Blackett-Healy projection"))
        setattr(cls, "SNOMED:399247005",
            PermissibleValue(
                text="SNOMED:399247005",
                title="Tarrant projection"))
        setattr(cls, "SNOMED:399251007",
            PermissibleValue(
                text="SNOMED:399251007",
                title="Lorenz projection"))
        setattr(cls, "SNOMED:399255003",
            PermissibleValue(
                text="SNOMED:399255003",
                title="Submentovertical projection"))
        setattr(cls, "SNOMED:399260004",
            PermissibleValue(
                text="SNOMED:399260004",
                title="Mediolateral projection"))
        setattr(cls, "SNOMED:399263002",
            PermissibleValue(
                text="SNOMED:399263002",
                title="Beclere projection"))
        setattr(cls, "SNOMED:399265009",
            PermissibleValue(
                text="SNOMED:399265009",
                title="Exaggerated cranio-caudal projection"))
        setattr(cls, "SNOMED:399268006",
            PermissibleValue(
                text="SNOMED:399268006",
                title="Medio-lateral oblique emissive projection"))
        setattr(cls, "SNOMED:399270002",
            PermissibleValue(
                text="SNOMED:399270002",
                title="Towne's projection"))
        setattr(cls, "SNOMED:399271003",
            PermissibleValue(
                text="SNOMED:399271003",
                title="Parasternal short axis view at the papillary muscle level"))
        setattr(cls, "SNOMED:399272005",
            PermissibleValue(
                text="SNOMED:399272005",
                title="Parietoacanthial projection"))
        setattr(cls, "SNOMED:399273000",
            PermissibleValue(
                text="SNOMED:399273000",
                title="Sagittal-oblique axial emissive projection"))
        setattr(cls, "SNOMED:399277004",
            PermissibleValue(
                text="SNOMED:399277004",
                title="Hickey projection"))
        setattr(cls, "SNOMED:399278009",
            PermissibleValue(
                text="SNOMED:399278009",
                title="Cahoon projection"))
        setattr(cls, "SNOMED:399280003",
            PermissibleValue(
                text="SNOMED:399280003",
                title="Kasabach projection"))
        setattr(cls, "SNOMED:399281004",
            PermissibleValue(
                text="SNOMED:399281004",
                title="Fleischner projection"))
        setattr(cls, "SNOMED:399284007",
            PermissibleValue(
                text="SNOMED:399284007",
                title="Merchant projection"))
        setattr(cls, "SNOMED:399285008",
            PermissibleValue(
                text="SNOMED:399285008",
                title="Holmblad projection"))
        setattr(cls, "SNOMED:399288005",
            PermissibleValue(
                text="SNOMED:399288005",
                title="Oblique cranio-caudal projection"))
        setattr(cls, "SNOMED:399290006",
            PermissibleValue(
                text="SNOMED:399290006",
                title="Schüller projection"))
        setattr(cls, "SNOMED:399292003",
            PermissibleValue(
                text="SNOMED:399292003",
                title="Stecher projection"))
        setattr(cls, "SNOMED:399296000",
            PermissibleValue(
                text="SNOMED:399296000",
                title="Taylor projection"))
        setattr(cls, "SNOMED:399297009",
            PermissibleValue(
                text="SNOMED:399297009",
                title="Right lateral emissive projection"))
        setattr(cls, "SNOMED:399300004",
            PermissibleValue(
                text="SNOMED:399300004",
                title="Lateral-medial emissive projection"))
        setattr(cls, "SNOMED:399303002",
            PermissibleValue(
                text="SNOMED:399303002",
                title="Dunlap projection"))
        setattr(cls, "SNOMED:399306005",
            PermissibleValue(
                text="SNOMED:399306005",
                title="Parasternal short axis view"))
        setattr(cls, "SNOMED:399308006",
            PermissibleValue(
                text="SNOMED:399308006",
                title="Lindblom projection"))
        setattr(cls, "SNOMED:399310008",
            PermissibleValue(
                text="SNOMED:399310008",
                title="Subcostal long axis view"))
        setattr(cls, "SNOMED:399311007",
            PermissibleValue(
                text="SNOMED:399311007",
                title="Grandy projection"))
        setattr(cls, "SNOMED:399312000",
            PermissibleValue(
                text="SNOMED:399312000",
                title="Antero-posterior oblique projection"))
        setattr(cls, "SNOMED:399313005",
            PermissibleValue(
                text="SNOMED:399313005",
                title="Swanson projection"))
        setattr(cls, "SNOMED:399316002",
            PermissibleValue(
                text="SNOMED:399316002",
                title="Parieto-orbital projection"))
        setattr(cls, "SNOMED:399318001",
            PermissibleValue(
                text="SNOMED:399318001",
                title="Kovacs projection"))
        setattr(cls, "SNOMED:399320003",
            PermissibleValue(
                text="SNOMED:399320003",
                title="Clements-Nakayama projection"))
        setattr(cls, "SNOMED:399321004",
            PermissibleValue(
                text="SNOMED:399321004",
                title="Anterior emissive projection"))
        setattr(cls, "SNOMED:399325008",
            PermissibleValue(
                text="SNOMED:399325008",
                title="Sagittal-oblique axial projection"))
        setattr(cls, "SNOMED:399327000",
            PermissibleValue(
                text="SNOMED:399327000",
                title="Low-Beer projection"))
        setattr(cls, "SNOMED:399330007",
            PermissibleValue(
                text="SNOMED:399330007",
                title="Valdini projection"))
        setattr(cls, "SNOMED:399332004",
            PermissibleValue(
                text="SNOMED:399332004",
                title="Kurzbauer projection"))
        setattr(cls, "SNOMED:399335002",
            PermissibleValue(
                text="SNOMED:399335002",
                title="Dorsoplantar projection"))
        setattr(cls, "SNOMED:399339008",
            PermissibleValue(
                text="SNOMED:399339008",
                title="Apical long axis"))
        setattr(cls, "SNOMED:399341009",
            PermissibleValue(
                text="SNOMED:399341009",
                title="Haas projection"))
        setattr(cls, "SNOMED:399342002",
            PermissibleValue(
                text="SNOMED:399342002",
                title="Lilienfeld projection"))
        setattr(cls, "SNOMED:399344001",
            PermissibleValue(
                text="SNOMED:399344001",
                title="Broden projection"))
        setattr(cls, "SNOMED:399348003",
            PermissibleValue(
                text="SNOMED:399348003",
                title="Antero-posterior projection"))
        setattr(cls, "SNOMED:399349006",
            PermissibleValue(
                text="SNOMED:399349006",
                title="Stenver's projection"))
        setattr(cls, "SNOMED:399351005",
            PermissibleValue(
                text="SNOMED:399351005",
                title="Orbito-parietal projection"))
        setattr(cls, "SNOMED:399352003",
            PermissibleValue(
                text="SNOMED:399352003",
                title="Lateral-medial projection"))
        setattr(cls, "SNOMED:399355001",
            PermissibleValue(
                text="SNOMED:399355001",
                title="Chausse projection"))
        setattr(cls, "SNOMED:399356000",
            PermissibleValue(
                text="SNOMED:399356000",
                title="Right anterior oblique projection"))
        setattr(cls, "SNOMED:399358004",
            PermissibleValue(
                text="SNOMED:399358004",
                title="Caldwell projection"))
        setattr(cls, "SNOMED:399360002",
            PermissibleValue(
                text="SNOMED:399360002",
                title="Verticosubmental projection"))
        setattr(cls, "SNOMED:399361003",
            PermissibleValue(
                text="SNOMED:399361003",
                title="Nuclear medicine projection"))
        setattr(cls, "SNOMED:399362005",
            PermissibleValue(
                text="SNOMED:399362005",
                title="Bertel projection"))
        setattr(cls, "SNOMED:399365007",
            PermissibleValue(
                text="SNOMED:399365007",
                title="Pearson projection"))
        setattr(cls, "SNOMED:399368009",
            PermissibleValue(
                text="SNOMED:399368009",
                title="Medio-lateral oblique projection"))
        setattr(cls, "SNOMED:399370000",
            PermissibleValue(
                text="SNOMED:399370000",
                title="Lysholm projection"))
        setattr(cls, "SNOMED:399371001",
            PermissibleValue(
                text="SNOMED:399371001",
                title="Parasternal short axis view at the level of the mitral chords"))
        setattr(cls, "SNOMED:399372008",
            PermissibleValue(
                text="SNOMED:399372008",
                title="Ferguson projection"))
        setattr(cls, "SNOMED:399488007",
            PermissibleValue(
                text="SNOMED:399488007",
                title="Midline (qualifier value)",
                description="Midline (qualifier value)"))
        setattr(cls, "SNOMED:408723005",
            PermissibleValue(
                text="SNOMED:408723005",
                title="Cranial LAO"))
        setattr(cls, "SNOMED:408724004",
            PermissibleValue(
                text="SNOMED:408724004",
                title="Caudal LAO"))
        setattr(cls, "SNOMED:408725003",
            PermissibleValue(
                text="SNOMED:408725003",
                title="Cranial RAO"))
        setattr(cls, "SNOMED:408726002",
            PermissibleValue(
                text="SNOMED:408726002",
                title="Caudal RAO"))
        setattr(cls, "SNOMED:421610009",
            PermissibleValue(
                text="SNOMED:421610009",
                title="Bottom"))
        setattr(cls, "SNOMED:421812003",
            PermissibleValue(
                text="SNOMED:421812003",
                title="Top"))
        setattr(cls, "SNOMED:422534007",
            PermissibleValue(
                text="SNOMED:422534007",
                title="Rafert-Long projection"))
        setattr(cls, "SNOMED:422568001",
            PermissibleValue(
                text="SNOMED:422568001",
                title="Moore projection"))
        setattr(cls, "SNOMED:422670003",
            PermissibleValue(
                text="SNOMED:422670003",
                title="Apple projection"))
        setattr(cls, "SNOMED:422795009",
            PermissibleValue(
                text="SNOMED:422795009",
                title="Neer projection"))
        setattr(cls, "SNOMED:422861003",
            PermissibleValue(
                text="SNOMED:422861003",
                title="Burman projection"))
        setattr(cls, "SNOMED:422954003",
            PermissibleValue(
                text="SNOMED:422954003",
                title="Stryker projection"))
        setattr(cls, "SNOMED:422996004",
            PermissibleValue(
                text="SNOMED:422996004",
                title="Wolf projection"))
        setattr(cls, "SNOMED:423091003",
            PermissibleValue(
                text="SNOMED:423091003",
                title="Colcher-Sussman projection"))
        setattr(cls, "SNOMED:423720000",
            PermissibleValue(
                text="SNOMED:423720000",
                title="Rafer projection"))
        setattr(cls, "SNOMED:424086005",
            PermissibleValue(
                text="SNOMED:424086005",
                title="Hirtz Modification projection"))
        setattr(cls, "SNOMED:424655003",
            PermissibleValue(
                text="SNOMED:424655003",
                title="Eraso Modification projection"))
        setattr(cls, "SNOMED:424811006",
            PermissibleValue(
                text="SNOMED:424811006",
                title="Danelius-Miller projection"))
        setattr(cls, "SNOMED:424962005",
            PermissibleValue(
                text="SNOMED:424962005",
                title="Fisk projection"))
        setattr(cls, "SNOMED:425030002",
            PermissibleValue(
                text="SNOMED:425030002",
                title="Kite projection"))
        setattr(cls, "SNOMED:425035007",
            PermissibleValue(
                text="SNOMED:425035007",
                title="Robert projection"))
        setattr(cls, "SNOMED:425042007",
            PermissibleValue(
                text="SNOMED:425042007",
                title="Rosenberg projection"))
        setattr(cls, "SNOMED:425157002",
            PermissibleValue(
                text="SNOMED:425157002",
                title="Folio projection"))
        setattr(cls, "SNOMED:425188003",
            PermissibleValue(
                text="SNOMED:425188003",
                title="Garth projection"))
        setattr(cls, "SNOMED:441505008",
            PermissibleValue(
                text="SNOMED:441505008",
                title="Dorsopalmar projection"))
        setattr(cls, "SNOMED:441555000",
            PermissibleValue(
                text="SNOMED:441555000",
                title="Inferomedial to superolateral oblique view"))
        setattr(cls, "SNOMED:441672003",
            PermissibleValue(
                text="SNOMED:441672003",
                title="Dorso-ventral projection"))
        setattr(cls, "SNOMED:441753009",
            PermissibleValue(
                text="SNOMED:441753009",
                title="Mammography view"))
        setattr(cls, "SNOMED:442361004",
            PermissibleValue(
                text="SNOMED:442361004",
                title="Stereoscopic view"))
        setattr(cls, "SNOMED:442441009",
            PermissibleValue(
                text="SNOMED:442441009",
                title="Ventro-dorsal projection"))
        setattr(cls, "SNOMED:442580003",
            PermissibleValue(
                text="SNOMED:442580003",
                title="Axillary tissue mammography view"))
        setattr(cls, "SNOMED:442581004",
            PermissibleValue(
                text="SNOMED:442581004",
                title="Nipple in profile mammography view"))
        setattr(cls, "SNOMED:442593008",
            PermissibleValue(
                text="SNOMED:442593008",
                title="Infra-mammary fold mammography view"))
        setattr(cls, "SNOMED:442594002",
            PermissibleValue(
                text="SNOMED:442594002",
                title="Right stereoscopic view"))
        setattr(cls, "SNOMED:442640004",
            PermissibleValue(
                text="SNOMED:442640004",
                title="Left stereoscopic view"))
        setattr(cls, "SNOMED:442653001",
            PermissibleValue(
                text="SNOMED:442653001",
                title="Stereoscopic view incremented from baseline"))
        setattr(cls, "SNOMED:442667005",
            PermissibleValue(
                text="SNOMED:442667005",
                title="Stereoscopic view decremented from baseline"))
        setattr(cls, "SNOMED:443082005",
            PermissibleValue(
                text="SNOMED:443082005",
                title="Parasternal long axis view of right ventricular inflow tract"))
        setattr(cls, "SNOMED:443083000",
            PermissibleValue(
                text="SNOMED:443083000",
                title="Parasternal long axis view of right ventricular outflow tract"))
        setattr(cls, "SNOMED:443100003",
            PermissibleValue(
                text="SNOMED:443100003",
                title="Subcostal view of cardiac outlets directed anteriorly"))
        setattr(cls, "SNOMED:443160001",
            PermissibleValue(
                text="SNOMED:443160001",
                title="Subcostal short axis view at papillary muscle level"))
        setattr(cls, "SNOMED:443162009",
            PermissibleValue(
                text="SNOMED:443162009",
                title="Suprasternal coronal view"))
        setattr(cls, "SNOMED:443163004",
            PermissibleValue(
                text="SNOMED:443163004",
                title="Suprasternal sagittal view"))
        setattr(cls, "SNOMED:443293000",
            PermissibleValue(
                text="SNOMED:443293000",
                title="Transgastric short axis view"))
        setattr(cls, "SNOMED:443459002",
            PermissibleValue(
                text="SNOMED:443459002",
                title="Intramedullary"))
        setattr(cls, "SNOMED:443499004",
            PermissibleValue(
                text="SNOMED:443499004",
                title="Subcostal short axis view at mitral valve level"))
        setattr(cls, "SNOMED:443500008",
            PermissibleValue(
                text="SNOMED:443500008",
                title="Subcostal short axis view at venous inflow level"))
        setattr(cls, "SNOMED:443562002",
            PermissibleValue(
                text="SNOMED:443562002",
                title="Suprasternal long axis view of aortic arch"))
        setattr(cls, "SNOMED:443609003",
            PermissibleValue(
                text="SNOMED:443609003",
                title="Subcostal short axis view at aortic valve level"))
        setattr(cls, "SNOMED:443640005",
            PermissibleValue(
                text="SNOMED:443640005",
                title="Subcostal oblique coronal view"))
        setattr(cls, "SNOMED:443662005",
            PermissibleValue(
                text="SNOMED:443662005",
                title="Transesophageal four chamber view (qualifier value)"))
        setattr(cls, "SNOMED:443698002",
            PermissibleValue(
                text="SNOMED:443698002",
                title="Transesophageal short axis view (qualifier value)"))
        setattr(cls, "SNOMED:65424008",
            PermissibleValue(
                text="SNOMED:65424008",
                title="Contiguous"))
        setattr(cls, "SNOMED:66459002",
            PermissibleValue(
                text="SNOMED:66459002",
                title="Unilateral"))
        setattr(cls, "SNOMED:72906007",
            PermissibleValue(
                text="SNOMED:72906007",
                title="Common"))
        setattr(cls, "SNOMED:741000124103",
            PermissibleValue(
                text="SNOMED:741000124103",
                title="Dorsoventral"))
        setattr(cls, "SNOMED:761000124104",
            PermissibleValue(
                text="SNOMED:761000124104",
                title="Dorsolateral"))
        setattr(cls, "SNOMED:771000124106",
            PermissibleValue(
                text="SNOMED:771000124106",
                title="Ventrolateral"))
        setattr(cls, "SNOMED:781000124109",
            PermissibleValue(
                text="SNOMED:781000124109",
                title="Palmar"))

class EnumLaterality(EnumDefinitionImpl):
    """
    Laterality information for the site
    """
    _defn = EnumDefinition(
        name="EnumLaterality",
        description="Laterality information for the site",
    )

class EnumEDAMFormats(EnumDefinitionImpl):
    """
    Data formats from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMFormats",
        description="Data formats from the EDAM ontology.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "EDAM:format_1915",
            PermissibleValue(
                text="EDAM:format_1915",
                title="Format",
                description="Format"))
        setattr(cls, "EDAM_format:1196",
            PermissibleValue(
                text="EDAM_format:1196",
                title="SMILES",
                description="""Chemical structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation."""))
        setattr(cls, "EDAM_format:1197",
            PermissibleValue(
                text="EDAM_format:1197",
                title="InChI",
                description="""Chemical structure specified in IUPAC International Chemical Identifier (InChI) line notation."""))
        setattr(cls, "EDAM_format:1198",
            PermissibleValue(
                text="EDAM_format:1198",
                title="mf",
                description="""Chemical structure specified by Molecular Formula (MF), including a count of each element in a compound.
The general MF query format consists of a series of valid atomic symbols, with an optional number or range."""))
        setattr(cls, "EDAM_format:1199",
            PermissibleValue(
                text="EDAM_format:1199",
                title="InChIKey",
                description="""An InChIKey identifier is not human- nor machine-readable but is more suitable for web searches than an InChI chemical structure specification.
The InChIKey (hashed InChI) is a fixed length (25 character) condensed digital representation of an InChI chemical structure specification. It uniquely identifies a chemical compound."""))
        setattr(cls, "EDAM_format:1200",
            PermissibleValue(
                text="EDAM_format:1200",
                title="smarts",
                description="""SMILES ARbitrary Target Specification (SMARTS) format for chemical structure specification, which is a subset of the SMILES line notation."""))
        setattr(cls, "EDAM_format:1206",
            PermissibleValue(
                text="EDAM_format:1206",
                title="unambiguous pure",
                description="""Alphabet for a molecular sequence with possible unknown positions but without ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:1207",
            PermissibleValue(
                text="EDAM_format:1207",
                title="nucleotide",
                description="""Alphabet for a nucleotide sequence with possible ambiguity, unknown positions and non-sequence characters.
Non-sequence characters may be used for example for gaps."""))
        setattr(cls, "EDAM_format:1208",
            PermissibleValue(
                text="EDAM_format:1208",
                title="protein",
                description="""Alphabet for a protein sequence with possible ambiguity, unknown positions and non-sequence characters.
Non-sequence characters may be used for gaps and translation stop."""))
        setattr(cls, "EDAM_format:1209",
            PermissibleValue(
                text="EDAM_format:1209",
                title="consensus",
                description="Alphabet for the consensus of two or more molecular sequences."))
        setattr(cls, "EDAM_format:1210",
            PermissibleValue(
                text="EDAM_format:1210",
                title="pure nucleotide",
                description="""Alphabet for a nucleotide sequence with possible ambiguity and unknown positions but without non-sequence characters."""))
        setattr(cls, "EDAM_format:1211",
            PermissibleValue(
                text="EDAM_format:1211",
                title="unambiguous pure nucleotide",
                description="""Alphabet for a nucleotide sequence (characters ACGTU only) with possible unknown positions but without ambiguity or non-sequence characters ."""))
        setattr(cls, "EDAM_format:1212",
            PermissibleValue(
                text="EDAM_format:1212",
                title="dna",
                description="""Alphabet for a DNA sequence with possible ambiguity, unknown positions and non-sequence characters."""))
        setattr(cls, "EDAM_format:1213",
            PermissibleValue(
                text="EDAM_format:1213",
                title="rna",
                description="""Alphabet for an RNA sequence with possible ambiguity, unknown positions and non-sequence characters."""))
        setattr(cls, "EDAM_format:1214",
            PermissibleValue(
                text="EDAM_format:1214",
                title="unambiguous pure dna",
                description="""Alphabet for a DNA sequence (characters ACGT only) with possible unknown positions but without ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:1215",
            PermissibleValue(
                text="EDAM_format:1215",
                title="pure dna",
                description="""Alphabet for a DNA sequence with possible ambiguity and unknown positions but without non-sequence characters."""))
        setattr(cls, "EDAM_format:1216",
            PermissibleValue(
                text="EDAM_format:1216",
                title="unambiguous pure rna sequence",
                description="""Alphabet for an RNA sequence (characters ACGU only) with possible unknown positions but without ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:1217",
            PermissibleValue(
                text="EDAM_format:1217",
                title="pure rna",
                description="""Alphabet for an RNA sequence with possible ambiguity and unknown positions but without non-sequence characters."""))
        setattr(cls, "EDAM_format:1218",
            PermissibleValue(
                text="EDAM_format:1218",
                title="unambiguous pure protein",
                description="""Alphabet for any protein sequence with possible unknown positions but without ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:1219",
            PermissibleValue(
                text="EDAM_format:1219",
                title="pure protein",
                description="""Alphabet for any protein sequence with possible ambiguity and unknown positions but without non-sequence characters."""))
        setattr(cls, "EDAM_format:1248",
            PermissibleValue(
                text="EDAM_format:1248",
                title="EMBL feature location",
                description="""Format for sequence positions (feature location) as used in DDBJ/EMBL/GenBank database."""))
        setattr(cls, "EDAM_format:1295",
            PermissibleValue(
                text="EDAM_format:1295",
                title="quicktandem",
                description="""Report format for tandem repeats in a nucleotide sequence (format generated by the Sanger Centre quicktandem program)."""))
        setattr(cls, "EDAM_format:1296",
            PermissibleValue(
                text="EDAM_format:1296",
                title="Sanger inverted repeats",
                description="""Report format for inverted repeats in a nucleotide sequence (format generated by the Sanger Centre inverted program)."""))
        setattr(cls, "EDAM_format:1297",
            PermissibleValue(
                text="EDAM_format:1297",
                title="EMBOSS repeat",
                description="Report format for tandem repeats in a sequence (an EMBOSS report format)."))
        setattr(cls, "EDAM_format:1316",
            PermissibleValue(
                text="EDAM_format:1316",
                title="est2genome format",
                description="Format of a report on exon-intron structure generated by EMBOSS est2genome."))
        setattr(cls, "EDAM_format:1318",
            PermissibleValue(
                text="EDAM_format:1318",
                title="restrict format",
                description="""Report format for restriction enzyme recognition sites used by EMBOSS restrict program."""))
        setattr(cls, "EDAM_format:1319",
            PermissibleValue(
                text="EDAM_format:1319",
                title="restover format",
                description="""Report format for restriction enzyme recognition sites used by EMBOSS restover program."""))
        setattr(cls, "EDAM_format:1320",
            PermissibleValue(
                text="EDAM_format:1320",
                title="REBASE restriction sites",
                description="Report format for restriction enzyme recognition sites used by REBASE database."))
        setattr(cls, "EDAM_format:1332",
            PermissibleValue(
                text="EDAM_format:1332",
                title="FASTA search results format",
                description="""Format of results of a sequence database search using FASTA.
This includes (typically) score data, alignment data and a histogram (of observed and expected distribution of E values.)"""))
        setattr(cls, "EDAM_format:1333",
            PermissibleValue(
                text="EDAM_format:1333",
                title="BLAST results",
                description="""Format of results of a sequence database search using some variant of BLAST.
This includes score data, alignment data and summary table."""))
        setattr(cls, "EDAM_format:1334",
            PermissibleValue(
                text="EDAM_format:1334",
                title="mspcrunch",
                description="Format of results of a sequence database search using some variant of MSPCrunch."))
        setattr(cls, "EDAM_format:1335",
            PermissibleValue(
                text="EDAM_format:1335",
                title="Smith-Waterman format",
                description="Format of results of a sequence database search using some variant of Smith Waterman."))
        setattr(cls, "EDAM_format:1336",
            PermissibleValue(
                text="EDAM_format:1336",
                title="dhf",
                description="""Format of EMBASSY domain hits file (DHF) of hits (sequences) with domain classification information.
The hits are relatives to a SCOP or CATH family and are found from a search of a sequence database."""))
        setattr(cls, "EDAM_format:1337",
            PermissibleValue(
                text="EDAM_format:1337",
                title="lhf",
                description="""Format of EMBASSY ligand hits file (LHF) of database hits (sequences) with ligand classification information.
The hits are putative ligand-binding sequences and are found from a search of a sequence database."""))
        setattr(cls, "EDAM_format:1341",
            PermissibleValue(
                text="EDAM_format:1341",
                title="InterPro hits format",
                description="Results format for searches of the InterPro database."))
        setattr(cls, "EDAM_format:1342",
            PermissibleValue(
                text="EDAM_format:1342",
                title="InterPro protein view report format",
                description="""Format of results of a search of the InterPro database showing matches of query protein sequence(s) to InterPro entries.
The report includes a classification of regions in a query protein sequence which are assigned to a known InterPro protein family or group."""))
        setattr(cls, "EDAM_format:1343",
            PermissibleValue(
                text="EDAM_format:1343",
                title="InterPro match table format",
                description="""Format of results of a search of the InterPro database showing matches between protein sequence(s) and signatures for an InterPro entry.
The table presents matches between query proteins (rows) and signature methods (columns) for this entry. Alternatively the sequence(s) might be from from the InterPro entry itself. The match position in the protein sequence and match status (true positive, false positive etc) are indicated."""))
        setattr(cls, "EDAM_format:1349",
            PermissibleValue(
                text="EDAM_format:1349",
                title="HMMER Dirichlet prior",
                description="Dirichlet distribution HMMER format."))
        setattr(cls, "EDAM_format:1350",
            PermissibleValue(
                text="EDAM_format:1350",
                title="MEME Dirichlet prior",
                description="Dirichlet distribution MEME format."))
        setattr(cls, "EDAM_format:1351",
            PermissibleValue(
                text="EDAM_format:1351",
                title="HMMER emission and transition",
                description="""Format of a report from the HMMER package on the emission and transition counts of a hidden Markov model."""))
        setattr(cls, "EDAM_format:1356",
            PermissibleValue(
                text="EDAM_format:1356",
                title="prosite-pattern",
                description="Format of a regular expression pattern from the Prosite database."))
        setattr(cls, "EDAM_format:1357",
            PermissibleValue(
                text="EDAM_format:1357",
                title="EMBOSS sequence pattern",
                description="Format of an EMBOSS sequence pattern."))
        setattr(cls, "EDAM_format:1360",
            PermissibleValue(
                text="EDAM_format:1360",
                title="meme-motif",
                description="A motif in the format generated by the MEME program."))
        setattr(cls, "EDAM_format:1366",
            PermissibleValue(
                text="EDAM_format:1366",
                title="prosite-profile",
                description="Sequence profile (sequence classifier) format used in the PROSITE database."))
        setattr(cls, "EDAM_format:1367",
            PermissibleValue(
                text="EDAM_format:1367",
                title="JASPAR format",
                description="A profile (sequence classifier) in the format used in the JASPAR database."))
        setattr(cls, "EDAM_format:1369",
            PermissibleValue(
                text="EDAM_format:1369",
                title="MEME background Markov model",
                description="Format of the model of random sequences used by MEME."))
        setattr(cls, "EDAM_format:1370",
            PermissibleValue(
                text="EDAM_format:1370",
                title="HMMER format",
                description="Format of a hidden Markov model representation used by the HMMER package."))
        setattr(cls, "EDAM_format:1391",
            PermissibleValue(
                text="EDAM_format:1391",
                title="HMMER-aln",
                description="FASTA-style format for multiple sequences aligned by HMMER package to an HMM."))
        setattr(cls, "EDAM_format:1392",
            PermissibleValue(
                text="EDAM_format:1392",
                title="DIALIGN format",
                description="Format of multiple sequences aligned by DIALIGN package."))
        setattr(cls, "EDAM_format:1393",
            PermissibleValue(
                text="EDAM_format:1393",
                title="daf",
                description="""EMBASSY 'domain alignment file' (DAF) format, containing a sequence alignment of protein domains belonging to the same SCOP or CATH family.
The format is clustal-like and includes annotation of domain family classification information."""))
        setattr(cls, "EDAM_format:1419",
            PermissibleValue(
                text="EDAM_format:1419",
                title="Sequence-MEME profile alignment",
                description="""Format for alignment of molecular sequences to MEME profiles (position-dependent scoring matrices) as generated by the MAST tool from the MEME package."""))
        setattr(cls, "EDAM_format:1421",
            PermissibleValue(
                text="EDAM_format:1421",
                title="HMMER profile alignment (sequences versus HMMs)",
                description="""Format used by the HMMER package for an alignment of a sequence against a hidden Markov model database."""))
        setattr(cls, "EDAM_format:1422",
            PermissibleValue(
                text="EDAM_format:1422",
                title="HMMER profile alignment (HMM versus sequences)",
                description="""Format used by the HMMER package for of an alignment of a hidden Markov model against a sequence database."""))
        setattr(cls, "EDAM_format:1423",
            PermissibleValue(
                text="EDAM_format:1423",
                title="Phylip distance matrix",
                description="""Data Type must include the distance matrix, probably as pairs of sequence identifiers with a distance (integer or float).
Format of PHYLIP phylogenetic distance matrix data."""))
        setattr(cls, "EDAM_format:1424",
            PermissibleValue(
                text="EDAM_format:1424",
                title="ClustalW dendrogram",
                description="Dendrogram (tree file) format generated by ClustalW."))
        setattr(cls, "EDAM_format:1425",
            PermissibleValue(
                text="EDAM_format:1425",
                title="Phylip tree raw",
                description="""Raw data file format used by Phylip from which a phylogenetic tree is directly generated or plotted."""))
        setattr(cls, "EDAM_format:1430",
            PermissibleValue(
                text="EDAM_format:1430",
                title="Phylip continuous quantitative characters",
                description="PHYLIP file format for continuous quantitative character data."))
        setattr(cls, "EDAM_format:1432",
            PermissibleValue(
                text="EDAM_format:1432",
                title="Phylip character frequencies format",
                description="PHYLIP file format for phylogenetics character frequency data."))
        setattr(cls, "EDAM_format:1433",
            PermissibleValue(
                text="EDAM_format:1433",
                title="Phylip discrete states format",
                description="Format of PHYLIP discrete states data."))
        setattr(cls, "EDAM_format:1434",
            PermissibleValue(
                text="EDAM_format:1434",
                title="Phylip cliques format",
                description="Format of PHYLIP cliques data."))
        setattr(cls, "EDAM_format:1435",
            PermissibleValue(
                text="EDAM_format:1435",
                title="Phylip tree format",
                description="Phylogenetic tree data format used by the PHYLIP program."))
        setattr(cls, "EDAM_format:1436",
            PermissibleValue(
                text="EDAM_format:1436",
                title="TreeBASE format",
                description="The format of an entry from the TreeBASE database of phylogenetic data."))
        setattr(cls, "EDAM_format:1437",
            PermissibleValue(
                text="EDAM_format:1437",
                title="TreeFam format",
                description="The format of an entry from the TreeFam database of phylogenetic data."))
        setattr(cls, "EDAM_format:1445",
            PermissibleValue(
                text="EDAM_format:1445",
                title="Phylip tree distance format",
                description="""Format for distances, such as Branch Score distance, between two or more phylogenetic trees as used by the Phylip package."""))
        setattr(cls, "EDAM_format:1454",
            PermissibleValue(
                text="EDAM_format:1454",
                title="dssp",
                description="""Format of an entry from the DSSP database (Dictionary of Secondary Structure in Proteins).
The DSSP database is built using the DSSP application which defines secondary structure, geometrical features and solvent exposure of proteins, given atomic coordinates in PDB format."""))
        setattr(cls, "EDAM_format:1455",
            PermissibleValue(
                text="EDAM_format:1455",
                title="hssp",
                description="Entry format of the HSSP database (Homology-derived Secondary Structure in Proteins)."))
        setattr(cls, "EDAM_format:1457",
            PermissibleValue(
                text="EDAM_format:1457",
                title="Dot-bracket format",
                description="""Format of RNA secondary structure in dot-bracket notation, originally generated by the Vienna RNA package/server."""))
        setattr(cls, "EDAM_format:1458",
            PermissibleValue(
                text="EDAM_format:1458",
                title="Vienna local RNA secondary structure format",
                description="""Format of local RNA secondary structure components with free energy values, generated by the Vienna RNA package/server."""))
        setattr(cls, "EDAM_format:1475",
            PermissibleValue(
                text="EDAM_format:1475",
                title="PDB database entry format",
                description="Format of an entry (or part of an entry) from the PDB database."))
        setattr(cls, "EDAM_format:1476",
            PermissibleValue(
                text="EDAM_format:1476",
                title="PDB",
                description="Entry format of PDB database in PDB format."))
        setattr(cls, "EDAM_format:1477",
            PermissibleValue(
                text="EDAM_format:1477",
                title="mmCIF",
                description="Entry format of PDB database in mmCIF format."))
        setattr(cls, "EDAM_format:1478",
            PermissibleValue(
                text="EDAM_format:1478",
                title="PDBML",
                description="Entry format of PDB database in PDBML (XML) format."))
        setattr(cls, "EDAM_format:1504",
            PermissibleValue(
                text="EDAM_format:1504",
                title="aaindex",
                description="Amino acid index format used by the AAindex database."))
        setattr(cls, "EDAM_format:1551",
            PermissibleValue(
                text="EDAM_format:1551",
                title="Pcons report format",
                description="""Format of output of the Pcons Model Quality Assessment Program (MQAP).
Pcons ranks protein models by assessing their quality based on the occurrence of recurring common three-dimensional structural patterns. Pcons returns a score reflecting the overall global quality and a score for each individual residue in the protein reflecting the local residue quality."""))
        setattr(cls, "EDAM_format:1552",
            PermissibleValue(
                text="EDAM_format:1552",
                title="ProQ report format",
                description="""Format of output of the ProQ protein model quality predictor.
ProQ is a neural network-based predictor that predicts the quality of a protein model based on the number of structural features."""))
        setattr(cls, "EDAM_format:1582",
            PermissibleValue(
                text="EDAM_format:1582",
                title="findkm",
                description="""A report format for the kinetics of enzyme-catalysed reaction(s) in a format generated by EMBOSS findkm. This includes Michaelis Menten plot, Hanes Woolf plot, Michaelis Menten constant (Km) and maximum velocity (Vmax)."""))
        setattr(cls, "EDAM_format:1627",
            PermissibleValue(
                text="EDAM_format:1627",
                title="Primer3 primer",
                description="""Report format on PCR primers and hybridisation oligos as generated by Whitehead primer3 program."""))
        setattr(cls, "EDAM_format:1628",
            PermissibleValue(
                text="EDAM_format:1628",
                title="ABI",
                description="A format of raw sequence read data from an Applied Biosystems sequencing machine."))
        setattr(cls, "EDAM_format:1629",
            PermissibleValue(
                text="EDAM_format:1629",
                title="mira",
                description="Format of MIRA sequence trace information file."))
        setattr(cls, "EDAM_format:1630",
            PermissibleValue(
                text="EDAM_format:1630",
                title="CAF",
                description="""Common Assembly Format (CAF). A sequence assembly format including contigs, base-call qualities, and other metadata."""))
        setattr(cls, "EDAM_format:1631",
            PermissibleValue(
                text="EDAM_format:1631",
                title="EXP",
                description="Sequence assembly project file EXP format."))
        setattr(cls, "EDAM_format:1632",
            PermissibleValue(
                text="EDAM_format:1632",
                title="SCF",
                description="""Staden Chromatogram Files format (SCF) of base-called sequence reads, qualities, and other metadata."""))
        setattr(cls, "EDAM_format:1633",
            PermissibleValue(
                text="EDAM_format:1633",
                title="PHD",
                description="PHD sequence trace format to store serialised chromatogram data (reads)."))
        setattr(cls, "EDAM_format:1637",
            PermissibleValue(
                text="EDAM_format:1637",
                title="dat",
                description="Format of Affymetrix data file of raw image data."))
        setattr(cls, "EDAM_format:1638",
            PermissibleValue(
                text="EDAM_format:1638",
                title="cel",
                description="""Format of Affymetrix data file of information about (raw) expression levels of the individual probes."""))
        setattr(cls, "EDAM_format:1639",
            PermissibleValue(
                text="EDAM_format:1639",
                title="affymetrix",
                description="""Format of affymetrix gene cluster files (hc-genes.txt, hc-chips.txt) from hierarchical clustering."""))
        setattr(cls, "EDAM_format:1641",
            PermissibleValue(
                text="EDAM_format:1641",
                title="affymetrix-exp",
                description="""Affymetrix data file format for information about experimental conditions and protocols."""))
        setattr(cls, "EDAM_format:1644",
            PermissibleValue(
                text="EDAM_format:1644",
                title="CHP",
                description="""Format of Affymetrix data file of information about (normalised) expression levels of the individual probes."""))
        setattr(cls, "EDAM_format:1665",
            PermissibleValue(
                text="EDAM_format:1665",
                title="Taverna workflow format",
                description="Format of Taverna workflows."))
        setattr(cls, "EDAM_format:1705",
            PermissibleValue(
                text="EDAM_format:1705",
                title="HET group dictionary entry format",
                description="The format of an entry from the HET group dictionary (HET groups from PDB files)."))
        setattr(cls, "EDAM_format:1734",
            PermissibleValue(
                text="EDAM_format:1734",
                title="PubMed citation",
                description="Format of bibliographic reference as used by the PubMed database."))
        setattr(cls, "EDAM_format:1735",
            PermissibleValue(
                text="EDAM_format:1735",
                title="Medline Display Format",
                description="""Bibliographic reference information including citation information is included
Format for abstracts of scientific articles from the Medline database."""))
        setattr(cls, "EDAM_format:1736",
            PermissibleValue(
                text="EDAM_format:1736",
                title="CiteXplore-core",
                description="CiteXplore 'core' citation format including title, journal, authors and abstract."))
        setattr(cls, "EDAM_format:1737",
            PermissibleValue(
                text="EDAM_format:1737",
                title="CiteXplore-all",
                description="""CiteXplore 'all' citation format includes all known details such as Mesh terms and cross-references."""))
        setattr(cls, "EDAM_format:1739",
            PermissibleValue(
                text="EDAM_format:1739",
                title="pmc",
                description="Article format of the PubMed Central database."))
        setattr(cls, "EDAM_format:1740",
            PermissibleValue(
                text="EDAM_format:1740",
                title="iHOP format",
                description="The format of iHOP (Information Hyperlinked over Proteins) text-mining result."))
        setattr(cls, "EDAM_format:1741",
            PermissibleValue(
                text="EDAM_format:1741",
                title="OSCAR format",
                description="""OSCAR (Open-Source Chemistry Analysis Routines) software performs chemistry-specific parsing of chemical documents. It attempts to identify chemical names, ontology concepts, and chemical data from a document.
OSCAR format of annotated chemical text."""))
        setattr(cls, "EDAM_format:1861",
            PermissibleValue(
                text="EDAM_format:1861",
                title="PlasMapper TextMap",
                description="Map of a plasmid (circular DNA) in PlasMapper TextMap format."))
        setattr(cls, "EDAM_format:1910",
            PermissibleValue(
                text="EDAM_format:1910",
                title="newick",
                description="Phylogenetic tree Newick (text) format."))
        setattr(cls, "EDAM_format:1911",
            PermissibleValue(
                text="EDAM_format:1911",
                title="TreeCon format",
                description="Phylogenetic tree TreeCon (text) format."))
        setattr(cls, "EDAM_format:1912",
            PermissibleValue(
                text="EDAM_format:1912",
                title="Nexus format",
                description="Phylogenetic tree Nexus (text) format."))
        setattr(cls, "EDAM_format:1919",
            PermissibleValue(
                text="EDAM_format:1919",
                title="Sequence record format",
                description="Data format for a molecular sequence record."))
        setattr(cls, "EDAM_format:1920",
            PermissibleValue(
                text="EDAM_format:1920",
                title="Sequence feature annotation format",
                description="Data format for molecular sequence feature information."))
        setattr(cls, "EDAM_format:1921",
            PermissibleValue(
                text="EDAM_format:1921",
                title="Alignment format",
                description="Data format for molecular sequence alignment information."))
        setattr(cls, "EDAM_format:1923",
            PermissibleValue(
                text="EDAM_format:1923",
                title="acedb",
                description="ACEDB sequence format."))
        setattr(cls, "EDAM_format:1925",
            PermissibleValue(
                text="EDAM_format:1925",
                title="codata",
                description="Codata entry format."))
        setattr(cls, "EDAM_format:1926",
            PermissibleValue(
                text="EDAM_format:1926",
                title="dbid",
                description="Fasta format variant with database name before ID."))
        setattr(cls, "EDAM_format:1927",
            PermissibleValue(
                text="EDAM_format:1927",
                title="EMBL format",
                description="EMBL entry format."))
        setattr(cls, "EDAM_format:1928",
            PermissibleValue(
                text="EDAM_format:1928",
                title="Staden experiment format",
                description="Staden experiment file format."))
        setattr(cls, "EDAM_format:1929",
            PermissibleValue(
                text="EDAM_format:1929",
                title="FASTA",
                description="FASTA format including NCBI-style IDs."))
        setattr(cls, "EDAM_format:1930",
            PermissibleValue(
                text="EDAM_format:1930",
                title="FASTQ",
                description="FASTQ short read format ignoring quality scores."))
        setattr(cls, "EDAM_format:1931",
            PermissibleValue(
                text="EDAM_format:1931",
                title="FASTQ-illumina",
                description="FASTQ Illumina 1.3 short read format."))
        setattr(cls, "EDAM_format:1932",
            PermissibleValue(
                text="EDAM_format:1932",
                title="FASTQ-sanger",
                description="FASTQ short read format with phred quality."))
        setattr(cls, "EDAM_format:1933",
            PermissibleValue(
                text="EDAM_format:1933",
                title="FASTQ-solexa",
                description="FASTQ Solexa/Illumina 1.0 short read format."))
        setattr(cls, "EDAM_format:1934",
            PermissibleValue(
                text="EDAM_format:1934",
                title="fitch program",
                description="Fitch program format."))
        setattr(cls, "EDAM_format:1935",
            PermissibleValue(
                text="EDAM_format:1935",
                title="GCG",
                description="""GCG SSF (single sequence file) file format.
GCG sequence file format."""))
        setattr(cls, "EDAM_format:1936",
            PermissibleValue(
                text="EDAM_format:1936",
                title="GenBank format",
                description="Genbank entry format."))
        setattr(cls, "EDAM_format:1937",
            PermissibleValue(
                text="EDAM_format:1937",
                title="genpept",
                description="""Currently identical to refseqp format
Genpept protein entry format."""))
        setattr(cls, "EDAM_format:1938",
            PermissibleValue(
                text="EDAM_format:1938",
                title="GFF2-seq",
                description="GFF feature file format with sequence in the header."))
        setattr(cls, "EDAM_format:1939",
            PermissibleValue(
                text="EDAM_format:1939",
                title="GFF3-seq",
                description="GFF3 feature file format with sequence."))
        setattr(cls, "EDAM_format:1940",
            PermissibleValue(
                text="EDAM_format:1940",
                title="giFASTA format",
                description="FASTA sequence format including NCBI-style GIs."))
        setattr(cls, "EDAM_format:1941",
            PermissibleValue(
                text="EDAM_format:1941",
                title="hennig86",
                description="Hennig86 output sequence format."))
        setattr(cls, "EDAM_format:1942",
            PermissibleValue(
                text="EDAM_format:1942",
                title="ig",
                description="Intelligenetics sequence format."))
        setattr(cls, "EDAM_format:1943",
            PermissibleValue(
                text="EDAM_format:1943",
                title="igstrict",
                description="Intelligenetics sequence format (strict version)."))
        setattr(cls, "EDAM_format:1944",
            PermissibleValue(
                text="EDAM_format:1944",
                title="jackknifer",
                description="Jackknifer interleaved and non-interleaved sequence format."))
        setattr(cls, "EDAM_format:1945",
            PermissibleValue(
                text="EDAM_format:1945",
                title="mase format",
                description="Mase program sequence format."))
        setattr(cls, "EDAM_format:1946",
            PermissibleValue(
                text="EDAM_format:1946",
                title="mega-seq",
                description="Mega interleaved and non-interleaved sequence format."))
        setattr(cls, "EDAM_format:1947",
            PermissibleValue(
                text="EDAM_format:1947",
                title="GCG MSF",
                description="GCG MSF (multiple sequence file) file format."))
        setattr(cls, "EDAM_format:1948",
            PermissibleValue(
                text="EDAM_format:1948",
                title="nbrf/pir",
                description="NBRF/PIR entry sequence format."))
        setattr(cls, "EDAM_format:1949",
            PermissibleValue(
                text="EDAM_format:1949",
                title="nexus-seq",
                description="Nexus/paup interleaved sequence format."))
        setattr(cls, "EDAM_format:1950",
            PermissibleValue(
                text="EDAM_format:1950",
                title="pdbatom",
                description="""PDB sequence format (ATOM lines).
pdb format in EMBOSS."""))
        setattr(cls, "EDAM_format:1951",
            PermissibleValue(
                text="EDAM_format:1951",
                title="pdbatomnuc",
                description="""PDB nucleotide sequence format (ATOM lines).
pdbnuc format in EMBOSS."""))
        setattr(cls, "EDAM_format:1952",
            PermissibleValue(
                text="EDAM_format:1952",
                title="pdbseqresnuc",
                description="""PDB nucleotide sequence format (SEQRES lines).
pdbnucseq format in EMBOSS."""))
        setattr(cls, "EDAM_format:1953",
            PermissibleValue(
                text="EDAM_format:1953",
                title="pdbseqres",
                description="""PDB sequence format (SEQRES lines).
pdbseq format in EMBOSS."""))
        setattr(cls, "EDAM_format:1954",
            PermissibleValue(
                text="EDAM_format:1954",
                title="Pearson format",
                description="Plain old FASTA sequence format (unspecified format for IDs)."))
        setattr(cls, "EDAM_format:1957",
            PermissibleValue(
                text="EDAM_format:1957",
                title="raw",
                description="Raw sequence format with no non-sequence characters."))
        setattr(cls, "EDAM_format:1958",
            PermissibleValue(
                text="EDAM_format:1958",
                title="refseqp",
                description="""Currently identical to genpept format
Refseq protein entry sequence format."""))
        setattr(cls, "EDAM_format:1960",
            PermissibleValue(
                text="EDAM_format:1960",
                title="Staden format",
                description="Staden suite sequence format."))
        setattr(cls, "EDAM_format:1961",
            PermissibleValue(
                text="EDAM_format:1961",
                title="Stockholm format",
                description="Stockholm multiple sequence alignment format (used by Pfam and Rfam)."))
        setattr(cls, "EDAM_format:1962",
            PermissibleValue(
                text="EDAM_format:1962",
                title="strider format",
                description="DNA strider output sequence format."))
        setattr(cls, "EDAM_format:1963",
            PermissibleValue(
                text="EDAM_format:1963",
                title="UniProtKB format",
                description="UniProtKB entry sequence format."))
        setattr(cls, "EDAM_format:1964",
            PermissibleValue(
                text="EDAM_format:1964",
                title="plain text format (unformatted)",
                description="Plain text sequence format (essentially unformatted)."))
        setattr(cls, "EDAM_format:1966",
            PermissibleValue(
                text="EDAM_format:1966",
                title="ASN.1 sequence format",
                description="NCBI ASN.1-based sequence format."))
        setattr(cls, "EDAM_format:1967",
            PermissibleValue(
                text="EDAM_format:1967",
                title="DAS format",
                description="DAS sequence (XML) format (any type)."))
        setattr(cls, "EDAM_format:1968",
            PermissibleValue(
                text="EDAM_format:1968",
                title="dasdna",
                description="""DAS sequence (XML) format (nucleotide-only).
The use of this format is deprecated."""))
        setattr(cls, "EDAM_format:1969",
            PermissibleValue(
                text="EDAM_format:1969",
                title="debug-seq",
                description="EMBOSS debugging trace sequence format of full internal data content."))
        setattr(cls, "EDAM_format:1970",
            PermissibleValue(
                text="EDAM_format:1970",
                title="jackknifernon",
                description="Jackknifer output sequence non-interleaved format."))
        setattr(cls, "EDAM_format:1972",
            PermissibleValue(
                text="EDAM_format:1972",
                title="NCBI format",
                description="""NCBI FASTA sequence format with NCBI-style IDs.
There are several variants of this."""))
        setattr(cls, "EDAM_format:1973",
            PermissibleValue(
                text="EDAM_format:1973",
                title="nexusnon",
                description="Nexus/paup non-interleaved sequence format."))
        setattr(cls, "EDAM_format:1974",
            PermissibleValue(
                text="EDAM_format:1974",
                title="GFF2",
                description="General Feature Format (GFF) of sequence features."))
        setattr(cls, "EDAM_format:1975",
            PermissibleValue(
                text="EDAM_format:1975",
                title="GFF3",
                description="Generic Feature Format version 3 (GFF3) of sequence features."))
        setattr(cls, "EDAM_format:1978",
            PermissibleValue(
                text="EDAM_format:1978",
                title="DASGFF",
                description="DAS GFF (XML) feature format."))
        setattr(cls, "EDAM_format:1979",
            PermissibleValue(
                text="EDAM_format:1979",
                title="debug-feat",
                description="EMBOSS debugging trace feature format of full internal data content."))
        setattr(cls, "EDAM_format:1982",
            PermissibleValue(
                text="EDAM_format:1982",
                title="ClustalW format",
                description="ClustalW format for (aligned) sequences."))
        setattr(cls, "EDAM_format:1983",
            PermissibleValue(
                text="EDAM_format:1983",
                title="debug",
                description="EMBOSS alignment format for debugging trace of full internal data content."))
        setattr(cls, "EDAM_format:1984",
            PermissibleValue(
                text="EDAM_format:1984",
                title="FASTA-aln",
                description="Fasta format for (aligned) sequences."))
        setattr(cls, "EDAM_format:1985",
            PermissibleValue(
                text="EDAM_format:1985",
                title="markx0",
                description="Pearson MARKX0 alignment format."))
        setattr(cls, "EDAM_format:1986",
            PermissibleValue(
                text="EDAM_format:1986",
                title="markx1",
                description="Pearson MARKX1 alignment format."))
        setattr(cls, "EDAM_format:1987",
            PermissibleValue(
                text="EDAM_format:1987",
                title="markx10",
                description="Pearson MARKX10 alignment format."))
        setattr(cls, "EDAM_format:1988",
            PermissibleValue(
                text="EDAM_format:1988",
                title="markx2",
                description="Pearson MARKX2 alignment format."))
        setattr(cls, "EDAM_format:1989",
            PermissibleValue(
                text="EDAM_format:1989",
                title="markx3",
                description="Pearson MARKX3 alignment format."))
        setattr(cls, "EDAM_format:1990",
            PermissibleValue(
                text="EDAM_format:1990",
                title="match",
                description="Alignment format for start and end of matches between sequence pairs."))
        setattr(cls, "EDAM_format:1991",
            PermissibleValue(
                text="EDAM_format:1991",
                title="mega",
                description="Mega format for (typically aligned) sequences."))
        setattr(cls, "EDAM_format:1992",
            PermissibleValue(
                text="EDAM_format:1992",
                title="meganon",
                description="Mega non-interleaved format for (typically aligned) sequences."))
        setattr(cls, "EDAM_format:1996",
            PermissibleValue(
                text="EDAM_format:1996",
                title="pair",
                description="EMBOSS simple sequence pairwise alignment format."))
        setattr(cls, "EDAM_format:1997",
            PermissibleValue(
                text="EDAM_format:1997",
                title="PHYLIP format",
                description="Phylip format for (aligned) sequences."))
        setattr(cls, "EDAM_format:1998",
            PermissibleValue(
                text="EDAM_format:1998",
                title="PHYLIP sequential",
                description="Phylip non-interleaved format for (aligned) sequences."))
        setattr(cls, "EDAM_format:1999",
            PermissibleValue(
                text="EDAM_format:1999",
                title="scores format",
                description="Alignment format for score values for pairs of sequences."))
        setattr(cls, "EDAM_format:2000",
            PermissibleValue(
                text="EDAM_format:2000",
                title="selex",
                description="SELEX format for (aligned) sequences."))
        setattr(cls, "EDAM_format:2001",
            PermissibleValue(
                text="EDAM_format:2001",
                title="EMBOSS simple format",
                description="EMBOSS simple multiple alignment format."))
        setattr(cls, "EDAM_format:2002",
            PermissibleValue(
                text="EDAM_format:2002",
                title="srs format",
                description="Simple multiple sequence (alignment) format for SRS."))
        setattr(cls, "EDAM_format:2003",
            PermissibleValue(
                text="EDAM_format:2003",
                title="srspair",
                description="Simple sequence pair (alignment) format for SRS."))
        setattr(cls, "EDAM_format:2004",
            PermissibleValue(
                text="EDAM_format:2004",
                title="T-Coffee format",
                description="T-Coffee program alignment format."))
        setattr(cls, "EDAM_format:2005",
            PermissibleValue(
                text="EDAM_format:2005",
                title="TreeCon-seq",
                description="Treecon format for (aligned) sequences."))
        setattr(cls, "EDAM_format:2006",
            PermissibleValue(
                text="EDAM_format:2006",
                title="Phylogenetic tree format",
                description="Data format for a phylogenetic tree."))
        setattr(cls, "EDAM_format:2013",
            PermissibleValue(
                text="EDAM_format:2013",
                title="Biological pathway or network format",
                description="Data format for a biological pathway or network."))
        setattr(cls, "EDAM_format:2014",
            PermissibleValue(
                text="EDAM_format:2014",
                title="Sequence-profile alignment format",
                description="Data format for a sequence-profile alignment."))
        setattr(cls, "EDAM_format:2017",
            PermissibleValue(
                text="EDAM_format:2017",
                title="Amino acid index format",
                description="Data format for an amino acid index."))
        setattr(cls, "EDAM_format:2020",
            PermissibleValue(
                text="EDAM_format:2020",
                title="Article format",
                description="Data format for a full-text scientific article."))
        setattr(cls, "EDAM_format:2021",
            PermissibleValue(
                text="EDAM_format:2021",
                title="Text mining report format",
                description="Data format of a report from text mining."))
        setattr(cls, "EDAM_format:2027",
            PermissibleValue(
                text="EDAM_format:2027",
                title="Enzyme kinetics report format",
                description="Data format for reports on enzyme kinetics."))
        setattr(cls, "EDAM_format:2030",
            PermissibleValue(
                text="EDAM_format:2030",
                title="Chemical data format",
                description="Format of a report on a chemical compound."))
        setattr(cls, "EDAM_format:2031",
            PermissibleValue(
                text="EDAM_format:2031",
                title="Gene annotation format",
                description="Format of a report on a particular locus, gene, gene system or groups of genes."))
        setattr(cls, "EDAM_format:2032",
            PermissibleValue(
                text="EDAM_format:2032",
                title="Workflow format",
                description="Format of a workflow."))
        setattr(cls, "EDAM_format:2033",
            PermissibleValue(
                text="EDAM_format:2033",
                title="Tertiary structure format",
                description="Data format for a molecular tertiary structure."))
        setattr(cls, "EDAM_format:2035",
            PermissibleValue(
                text="EDAM_format:2035",
                title="Chemical formula format",
                description="Text format of a chemical formula."))
        setattr(cls, "EDAM_format:2036",
            PermissibleValue(
                text="EDAM_format:2036",
                title="Phylogenetic character data format",
                description="Format of raw (unplotted) phylogenetic data."))
        setattr(cls, "EDAM_format:2037",
            PermissibleValue(
                text="EDAM_format:2037",
                title="Phylogenetic continuous quantitative character format",
                description="Format of phylogenetic continuous quantitative character data."))
        setattr(cls, "EDAM_format:2038",
            PermissibleValue(
                text="EDAM_format:2038",
                title="Phylogenetic discrete states format",
                description="Format of phylogenetic discrete states data."))
        setattr(cls, "EDAM_format:2039",
            PermissibleValue(
                text="EDAM_format:2039",
                title="Phylogenetic tree report (cliques) format",
                description="Format of phylogenetic cliques data."))
        setattr(cls, "EDAM_format:2040",
            PermissibleValue(
                text="EDAM_format:2040",
                title="Phylogenetic tree report (invariants) format",
                description="Format of phylogenetic invariants data."))
        setattr(cls, "EDAM_format:2049",
            PermissibleValue(
                text="EDAM_format:2049",
                title="Phylogenetic tree report (tree distances) format",
                description="Format for phylogenetic tree distance data."))
        setattr(cls, "EDAM_format:2052",
            PermissibleValue(
                text="EDAM_format:2052",
                title="Protein family report format",
                description="Format for reports on a protein family."))
        setattr(cls, "EDAM_format:2054",
            PermissibleValue(
                text="EDAM_format:2054",
                title="Protein interaction format",
                description="Format for molecular interaction data."))
        setattr(cls, "EDAM_format:2055",
            PermissibleValue(
                text="EDAM_format:2055",
                title="Sequence assembly format",
                description="Format for sequence assembly data."))
        setattr(cls, "EDAM_format:2056",
            PermissibleValue(
                text="EDAM_format:2056",
                title="Microarray experiment data format",
                description="""Format for information about a microarray experimental per se (not the data generated from that experiment)."""))
        setattr(cls, "EDAM_format:2057",
            PermissibleValue(
                text="EDAM_format:2057",
                title="Sequence trace format",
                description="Format for sequence trace data (i.e. including base call information)."))
        setattr(cls, "EDAM_format:2058",
            PermissibleValue(
                text="EDAM_format:2058",
                title="Gene expression report format",
                description="Format of a file of gene expression data, e.g. a gene expression matrix or profile."))
        setattr(cls, "EDAM_format:2060",
            PermissibleValue(
                text="EDAM_format:2060",
                title="Map format",
                description="Format of a map of (typically one) molecular sequence annotated with features."))
        setattr(cls, "EDAM_format:2061",
            PermissibleValue(
                text="EDAM_format:2061",
                title="Nucleic acid features (primers) format",
                description="Format of a report on PCR primers or hybridisation oligos in a nucleic acid sequence."))
        setattr(cls, "EDAM_format:2062",
            PermissibleValue(
                text="EDAM_format:2062",
                title="Protein report format",
                description="Format of a report of general information about a specific protein."))
        setattr(cls, "EDAM_format:2064",
            PermissibleValue(
                text="EDAM_format:2064",
                title="3D-1D scoring matrix format",
                description="Format of a matrix of 3D-1D scores (amino acid environment probabilities)."))
        setattr(cls, "EDAM_format:2065",
            PermissibleValue(
                text="EDAM_format:2065",
                title="Protein structure report (quality evaluation) format",
                description="Format of a report on the quality of a protein three-dimensional model."))
        setattr(cls, "EDAM_format:2066",
            PermissibleValue(
                text="EDAM_format:2066",
                title="Database hits (sequence) format",
                description="""Format of a report on sequence hits and associated data from searching a sequence database."""))
        setattr(cls, "EDAM_format:2067",
            PermissibleValue(
                text="EDAM_format:2067",
                title="Sequence distance matrix format",
                description="Format of a matrix of genetic distances between molecular sequences."))
        setattr(cls, "EDAM_format:2068",
            PermissibleValue(
                text="EDAM_format:2068",
                title="Sequence motif format",
                description="Format of a sequence motif."))
        setattr(cls, "EDAM_format:2069",
            PermissibleValue(
                text="EDAM_format:2069",
                title="Sequence profile format",
                description="Format of a sequence profile."))
        setattr(cls, "EDAM_format:2072",
            PermissibleValue(
                text="EDAM_format:2072",
                title="Hidden Markov model format",
                description="Format of a hidden Markov model."))
        setattr(cls, "EDAM_format:2074",
            PermissibleValue(
                text="EDAM_format:2074",
                title="Dirichlet distribution format",
                description="Data format of a dirichlet distribution."))
        setattr(cls, "EDAM_format:2075",
            PermissibleValue(
                text="EDAM_format:2075",
                title="HMM emission and transition counts format",
                description="Data format for the emission and transition counts of a hidden Markov model."))
        setattr(cls, "EDAM_format:2076",
            PermissibleValue(
                text="EDAM_format:2076",
                title="RNA secondary structure format",
                description="Format for secondary structure (predicted or real) of an RNA molecule."))
        setattr(cls, "EDAM_format:2077",
            PermissibleValue(
                text="EDAM_format:2077",
                title="Protein secondary structure format",
                description="Format for secondary structure (predicted or real) of a protein molecule."))
        setattr(cls, "EDAM_format:2078",
            PermissibleValue(
                text="EDAM_format:2078",
                title="Sequence range format",
                description="Format used to specify range(s) of sequence positions."))
        setattr(cls, "EDAM_format:2094",
            PermissibleValue(
                text="EDAM_format:2094",
                title="pure",
                description="""Alphabet for molecular sequence with possible unknown positions but without non-sequence characters."""))
        setattr(cls, "EDAM_format:2095",
            PermissibleValue(
                text="EDAM_format:2095",
                title="unpure",
                description="""Alphabet for a molecular sequence with possible unknown positions but possibly with non-sequence characters."""))
        setattr(cls, "EDAM_format:2096",
            PermissibleValue(
                text="EDAM_format:2096",
                title="unambiguous sequence",
                description="""Alphabet for a molecular sequence with possible unknown positions but without ambiguity characters."""))
        setattr(cls, "EDAM_format:2097",
            PermissibleValue(
                text="EDAM_format:2097",
                title="ambiguous",
                description="""Alphabet for a molecular sequence with possible unknown positions and possible ambiguity characters."""))
        setattr(cls, "EDAM_format:2155",
            PermissibleValue(
                text="EDAM_format:2155",
                title="Sequence features (repeats) format",
                description="Format used for map of repeats in molecular (typically nucleotide) sequences."))
        setattr(cls, "EDAM_format:2158",
            PermissibleValue(
                text="EDAM_format:2158",
                title="Nucleic acid features (restriction sites) format",
                description="""Format used for report on restriction enzyme recognition sites in nucleotide sequences."""))
        setattr(cls, "EDAM_format:2170",
            PermissibleValue(
                text="EDAM_format:2170",
                title="Sequence cluster format",
                description="Format used for clusters of molecular sequences."))
        setattr(cls, "EDAM_format:2171",
            PermissibleValue(
                text="EDAM_format:2171",
                title="Sequence cluster format (protein)",
                description="Format used for clusters of protein sequences."))
        setattr(cls, "EDAM_format:2172",
            PermissibleValue(
                text="EDAM_format:2172",
                title="Sequence cluster format (nucleic acid)",
                description="Format used for clusters of nucleotide sequences."))
        setattr(cls, "EDAM_format:2181",
            PermissibleValue(
                text="EDAM_format:2181",
                title="EMBL-like (text)",
                description="""A text format resembling EMBL entry format.
This concept may be used for the many non-standard EMBL-like text formats."""))
        setattr(cls, "EDAM_format:2182",
            PermissibleValue(
                text="EDAM_format:2182",
                title="FASTQ-like format (text)",
                description="""A text format resembling FASTQ short read format.
This concept may be used for non-standard FASTQ short read-like formats."""))
        setattr(cls, "EDAM_format:2183",
            PermissibleValue(
                text="EDAM_format:2183",
                title="EMBLXML",
                description="XML format for EMBL entries."))
        setattr(cls, "EDAM_format:2184",
            PermissibleValue(
                text="EDAM_format:2184",
                title="cdsxml",
                description="Specific XML format for EMBL entries (only uses certain sections)."))
        setattr(cls, "EDAM_format:2185",
            PermissibleValue(
                text="EDAM_format:2185",
                title="INSDSeq",
                description="""INSDSeq provides the elements of a sequence as presented in the GenBank/EMBL/DDBJ-style flatfile formats, with a small amount of additional structure."""))
        setattr(cls, "EDAM_format:2186",
            PermissibleValue(
                text="EDAM_format:2186",
                title="geneseq",
                description="Geneseq sequence format."))
        setattr(cls, "EDAM_format:2187",
            PermissibleValue(
                text="EDAM_format:2187",
                title="UniProt-like (text)",
                description="A text sequence format resembling uniprotkb entry format."))
        setattr(cls, "EDAM_format:2194",
            PermissibleValue(
                text="EDAM_format:2194",
                title="medline",
                description="Abstract format used by MedLine database."))
        setattr(cls, "EDAM_format:2195",
            PermissibleValue(
                text="EDAM_format:2195",
                title="Ontology format",
                description="Format used for ontologies."))
        setattr(cls, "EDAM_format:2196",
            PermissibleValue(
                text="EDAM_format:2196",
                title="OBO format",
                description="A serialisation format conforming to the Open Biomedical Ontologies (OBO) model."))
        setattr(cls, "EDAM_format:2197",
            PermissibleValue(
                text="EDAM_format:2197",
                title="OWL format",
                description="A serialisation format conforming to the Web Ontology Language (OWL) model."))
        setattr(cls, "EDAM_format:2200",
            PermissibleValue(
                text="EDAM_format:2200",
                title="FASTA-like (text)",
                description="""A text format resembling FASTA format.
This concept may also be used for the many non-standard FASTA-like formats."""))
        setattr(cls, "EDAM_format:2204",
            PermissibleValue(
                text="EDAM_format:2204",
                title="EMBL format (XML)",
                description="""An XML format for EMBL entries.
This is a placeholder for other more specific concepts. It should not normally be used for annotation."""))
        setattr(cls, "EDAM_format:2205",
            PermissibleValue(
                text="EDAM_format:2205",
                title="GenBank-like format (text)",
                description="""A text format resembling GenBank entry (plain text) format.
This concept may be used for the non-standard GenBank-like text formats."""))
        setattr(cls, "EDAM_format:2206",
            PermissibleValue(
                text="EDAM_format:2206",
                title="Sequence feature table format (text)",
                description="Text format for a sequence feature table."))
        setattr(cls, "EDAM_format:2304",
            PermissibleValue(
                text="EDAM_format:2304",
                title="STRING entry format (XML)",
                description="Entry format (XML) for the STRING database of protein interaction."))
        setattr(cls, "EDAM_format:2305",
            PermissibleValue(
                text="EDAM_format:2305",
                title="GFF",
                description="GFF feature format (of indeterminate version)."))
        setattr(cls, "EDAM_format:2306",
            PermissibleValue(
                text="EDAM_format:2306",
                title="GTF",
                description="Gene Transfer Format (GTF), a restricted version of GFF."))
        setattr(cls, "EDAM_format:2310",
            PermissibleValue(
                text="EDAM_format:2310",
                title="FASTA-HTML",
                description="FASTA format wrapped in HTML elements."))
        setattr(cls, "EDAM_format:2311",
            PermissibleValue(
                text="EDAM_format:2311",
                title="EMBL-HTML",
                description="EMBL entry format wrapped in HTML elements."))
        setattr(cls, "EDAM_format:2330",
            PermissibleValue(
                text="EDAM_format:2330",
                title="Textual format",
                description="""Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual).
Textual format."""))
        setattr(cls, "EDAM_format:2331",
            PermissibleValue(
                text="EDAM_format:2331",
                title="HTML",
                description="HTML format."))
        setattr(cls, "EDAM_format:2332",
            PermissibleValue(
                text="EDAM_format:2332",
                title="XML",
                description="""Data in XML format can be serialised into text, or binary format.
eXtensible Markup Language (XML) format."""))
        setattr(cls, "EDAM_format:2333",
            PermissibleValue(
                text="EDAM_format:2333",
                title="Binary format",
                description="""Binary format.
Only specific native binary formats are listed under 'Binary format' in EDAM. Generic binary formats - such as any data being zipped, or any XML data being serialised into the Efficient XML Interchange (EXI) format - are not modelled in EDAM. Refer to http://wsio.org/compression_004."""))
        setattr(cls, "EDAM_format:2350",
            PermissibleValue(
                text="EDAM_format:2350",
                title="Format (by type of data)",
                description="""A placeholder concept for visual navigation by dividing data formats by the content of the data that is represented.
This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. The concept branch under 'Format (typed)' provides an alternative organisation of the concepts nested under the other top-level branches ('Binary', 'HTML', 'RDF', 'Text' and 'XML'. All concepts under here are already included under those branches."""))
        setattr(cls, "EDAM_format:2352",
            PermissibleValue(
                text="EDAM_format:2352",
                title="BioXSD (XML)",
                description="""'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioXSD in XML' is the XML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.
BioXSD-schema-based XML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, Web services, and object-oriented programming."""))
        setattr(cls, "EDAM_format:2376",
            PermissibleValue(
                text="EDAM_format:2376",
                title="RDF format",
                description="A serialisation format conforming to the Resource Description Framework (RDF) model."))
        setattr(cls, "EDAM_format:2532",
            PermissibleValue(
                text="EDAM_format:2532",
                title="GenBank-HTML",
                description="Genbank entry format wrapped in HTML elements."))
        setattr(cls, "EDAM_format:2543",
            PermissibleValue(
                text="EDAM_format:2543",
                title="EMBL-like format",
                description="""A format resembling EMBL entry (plain text) format.
This concept may be used for the many non-standard EMBL-like formats."""))
        setattr(cls, "EDAM_format:2545",
            PermissibleValue(
                text="EDAM_format:2545",
                title="FASTQ-like format",
                description="""A format resembling FASTQ short read format.
This concept may be used for non-standard FASTQ short read-like formats."""))
        setattr(cls, "EDAM_format:2546",
            PermissibleValue(
                text="EDAM_format:2546",
                title="FASTA-like",
                description="""A format resembling FASTA format.
This concept may be used for the many non-standard FASTA-like formats."""))
        setattr(cls, "EDAM_format:2547",
            PermissibleValue(
                text="EDAM_format:2547",
                title="uniprotkb-like format",
                description="A sequence format resembling uniprotkb entry format."))
        setattr(cls, "EDAM_format:2548",
            PermissibleValue(
                text="EDAM_format:2548",
                title="Sequence feature table format",
                description="Format for a sequence feature table."))
        setattr(cls, "EDAM_format:2549",
            PermissibleValue(
                text="EDAM_format:2549",
                title="OBO",
                description="OBO ontology text format."))
        setattr(cls, "EDAM_format:2550",
            PermissibleValue(
                text="EDAM_format:2550",
                title="OBO-XML",
                description="OBO ontology XML format."))
        setattr(cls, "EDAM_format:2551",
            PermissibleValue(
                text="EDAM_format:2551",
                title="Sequence record format (text)",
                description="Data format for a molecular sequence record (text)."))
        setattr(cls, "EDAM_format:2552",
            PermissibleValue(
                text="EDAM_format:2552",
                title="Sequence record format (XML)",
                description="Data format for a molecular sequence record (XML)."))
        setattr(cls, "EDAM_format:2553",
            PermissibleValue(
                text="EDAM_format:2553",
                title="Sequence feature table format (XML)",
                description="XML format for a sequence feature table."))
        setattr(cls, "EDAM_format:2554",
            PermissibleValue(
                text="EDAM_format:2554",
                title="Alignment format (text)",
                description="Text format for molecular sequence alignment information."))
        setattr(cls, "EDAM_format:2555",
            PermissibleValue(
                text="EDAM_format:2555",
                title="Alignment format (XML)",
                description="XML format for molecular sequence alignment information."))
        setattr(cls, "EDAM_format:2556",
            PermissibleValue(
                text="EDAM_format:2556",
                title="Phylogenetic tree format (text)",
                description="Text format for a phylogenetic tree."))
        setattr(cls, "EDAM_format:2557",
            PermissibleValue(
                text="EDAM_format:2557",
                title="Phylogenetic tree format (XML)",
                description="XML format for a phylogenetic tree."))
        setattr(cls, "EDAM_format:2558",
            PermissibleValue(
                text="EDAM_format:2558",
                title="EMBL-like (XML)",
                description="""An XML format resembling EMBL entry format.
This concept may be used for the any non-standard EMBL-like XML formats."""))
        setattr(cls, "EDAM_format:2559",
            PermissibleValue(
                text="EDAM_format:2559",
                title="GenBank-like format",
                description="""A format resembling GenBank entry (plain text) format.
This concept may be used for the non-standard GenBank-like formats."""))
        setattr(cls, "EDAM_format:2561",
            PermissibleValue(
                text="EDAM_format:2561",
                title="Sequence assembly format (text)",
                description="Text format for sequence assembly data."))
        setattr(cls, "EDAM_format:2566",
            PermissibleValue(
                text="EDAM_format:2566",
                title="completely unambiguous",
                description="""Alphabet for a molecular sequence without any unknown positions or ambiguity characters."""))
        setattr(cls, "EDAM_format:2567",
            PermissibleValue(
                text="EDAM_format:2567",
                title="completely unambiguous pure",
                description="""Alphabet for a molecular sequence without unknown positions, ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:2568",
            PermissibleValue(
                text="EDAM_format:2568",
                title="completely unambiguous pure nucleotide",
                description="""Alphabet for a nucleotide sequence (characters ACGTU only) without unknown positions, ambiguity or non-sequence characters ."""))
        setattr(cls, "EDAM_format:2569",
            PermissibleValue(
                text="EDAM_format:2569",
                title="completely unambiguous pure dna",
                description="""Alphabet for a DNA sequence (characters ACGT only) without unknown positions, ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:2570",
            PermissibleValue(
                text="EDAM_format:2570",
                title="completely unambiguous pure rna sequence",
                description="""Alphabet for an RNA sequence (characters ACGU only) without unknown positions, ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:2571",
            PermissibleValue(
                text="EDAM_format:2571",
                title="Raw sequence format",
                description="Format of a raw molecular sequence (i.e. the alphabet used)."))
        setattr(cls, "EDAM_format:2572",
            PermissibleValue(
                text="EDAM_format:2572",
                title="BAM",
                description="""BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data."""))
        setattr(cls, "EDAM_format:2573",
            PermissibleValue(
                text="EDAM_format:2573",
                title="SAM",
                description="""Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
The format supports short and long reads (up to 128Mbp) produced by different sequencing platforms and is used to hold mapped data within the GATK and across the Broad Institute, the Sanger Centre, and throughout the 1000 Genomes project."""))
        setattr(cls, "EDAM_format:2585",
            PermissibleValue(
                text="EDAM_format:2585",
                title="SBML",
                description="""Systems Biology Markup Language (SBML), the standard XML format for models of biological processes such as for example metabolism, cell signaling, and gene regulation."""))
        setattr(cls, "EDAM_format:2607",
            PermissibleValue(
                text="EDAM_format:2607",
                title="completely unambiguous pure protein",
                description="""Alphabet for any protein sequence without unknown positions, ambiguity or non-sequence characters."""))
        setattr(cls, "EDAM_format:2848",
            PermissibleValue(
                text="EDAM_format:2848",
                title="Bibliographic reference format",
                description="Format of a bibliographic reference."))
        setattr(cls, "EDAM_format:2919",
            PermissibleValue(
                text="EDAM_format:2919",
                title="Sequence annotation track format",
                description="Format of a sequence annotation track."))
        setattr(cls, "EDAM_format:2920",
            PermissibleValue(
                text="EDAM_format:2920",
                title="Alignment format (pair only)",
                description="""Data format for molecular sequence alignment information that can hold sequence alignment(s) of only 2 sequences."""))
        setattr(cls, "EDAM_format:2921",
            PermissibleValue(
                text="EDAM_format:2921",
                title="Sequence variation annotation format",
                description="Format of sequence variation annotation."))
        setattr(cls, "EDAM_format:2922",
            PermissibleValue(
                text="EDAM_format:2922",
                title="markx0 variant",
                description="Some variant of Pearson MARKX alignment format."))
        setattr(cls, "EDAM_format:2923",
            PermissibleValue(
                text="EDAM_format:2923",
                title="mega variant",
                description="Some variant of Mega format for (typically aligned) sequences."))
        setattr(cls, "EDAM_format:2924",
            PermissibleValue(
                text="EDAM_format:2924",
                title="Phylip format variant",
                description="Some variant of Phylip format for (aligned) sequences."))
        setattr(cls, "EDAM_format:3000",
            PermissibleValue(
                text="EDAM_format:3000",
                title="AB1",
                description="""AB1 binary format of raw DNA sequence reads (output of Applied Biosystems' sequencing analysis software). Contains an electropherogram and the DNA base sequence.
AB1 uses the generic binary Applied Biosystems, Inc. Format (ABIF)."""))
        setattr(cls, "EDAM_format:3001",
            PermissibleValue(
                text="EDAM_format:3001",
                title="ACE",
                description="""ACE sequence assembly format including contigs, base-call qualities, and other metadata (version Aug 1998 and onwards)."""))
        setattr(cls, "EDAM_format:3003",
            PermissibleValue(
                text="EDAM_format:3003",
                title="BED",
                description="""BED detail format includes 2 additional columns (http://genome.ucsc.edu/FAQ/FAQformat#format1.7) and BED 15 includes 3 additional columns for experiment scores (http://genomewiki.ucsc.edu/index.php/Microarray_track).
Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser."""))
        setattr(cls, "EDAM_format:3004",
            PermissibleValue(
                text="EDAM_format:3004",
                title="bigBed",
                description="bigBed format for large sequence annotation tracks, similar to textual BED format."))
        setattr(cls, "EDAM_format:3005",
            PermissibleValue(
                text="EDAM_format:3005",
                title="WIG",
                description="""Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser."""))
        setattr(cls, "EDAM_format:3006",
            PermissibleValue(
                text="EDAM_format:3006",
                title="bigWig",
                description="""bigWig format for large sequence annotation tracks that consist of a value for each sequence position. Similar to textual WIG format."""))
        setattr(cls, "EDAM_format:3007",
            PermissibleValue(
                text="EDAM_format:3007",
                title="PSL",
                description="""PSL format of alignments, typically generated by BLAT or psLayout. Can be displayed in a genome browser like a sequence annotation track."""))
        setattr(cls, "EDAM_format:3008",
            PermissibleValue(
                text="EDAM_format:3008",
                title="MAF",
                description="""Multiple Alignment Format (MAF) supporting alignments of whole genomes with rearrangements, directions, multiple pieces to the alignment, and so forth.
Typically generated by Multiz and TBA aligners; can be displayed in a genome browser like a sequence annotation track. This should not be confused with MIRA Assembly Format or Mutation Annotation Format."""))
        setattr(cls, "EDAM_format:3009",
            PermissibleValue(
                text="EDAM_format:3009",
                title="2bit",
                description="""2bit binary format of nucleotide sequences using 2 bits per nucleotide. In addition encodes unknown nucleotides and lower-case 'masking'."""))
        setattr(cls, "EDAM_format:3010",
            PermissibleValue(
                text="EDAM_format:3010",
                title=".nib",
                description=""".nib (nibble) binary format of a nucleotide sequence using 4 bits per nucleotide (including unknown) and its lower-case 'masking'."""))
        setattr(cls, "EDAM_format:3011",
            PermissibleValue(
                text="EDAM_format:3011",
                title="genePred",
                description="""genePred format has 3 main variations (http://genome.ucsc.edu/FAQ/FAQformat#format9 http://www.broadinstitute.org/software/igv/genePred). They reflect UCSC Browser DB tables.
genePred table format for gene prediction tracks."""))
        setattr(cls, "EDAM_format:3012",
            PermissibleValue(
                text="EDAM_format:3012",
                title="pgSnp",
                description="""Personal Genome SNP (pgSnp) format for sequence variation tracks (indels and polymorphisms), supported by the UCSC Genome Browser."""))
        setattr(cls, "EDAM_format:3013",
            PermissibleValue(
                text="EDAM_format:3013",
                title="axt",
                description="axt format of alignments, typically produced from BLASTZ."))
        setattr(cls, "EDAM_format:3014",
            PermissibleValue(
                text="EDAM_format:3014",
                title="LAV",
                description="LAV format of alignments generated by BLASTZ and LASTZ."))
        setattr(cls, "EDAM_format:3015",
            PermissibleValue(
                text="EDAM_format:3015",
                title="Pileup",
                description="""Pileup format of alignment of sequences (e.g. sequencing reads) to (a) reference sequence(s). Contains aligned bases per base of the reference sequence(s)."""))
        setattr(cls, "EDAM_format:3016",
            PermissibleValue(
                text="EDAM_format:3016",
                title="VCF",
                description="""1000 Genomes Project has its own specification for encoding structural variations in VCF (https://www.internationalgenome.org/wiki/Analysis/Variant%20Call%20Format/VCF%20(Variant%20Call%20Format)%20version%204.0/encoding-structural-variants). This is based on VCF version 4.0 and not directly compatible with VCF version 4.3.
Variant Call Format (VCF) is tabular format for storing genomic sequence variations."""))
        setattr(cls, "EDAM_format:3017",
            PermissibleValue(
                text="EDAM_format:3017",
                title="SRF",
                description="""Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive."""))
        setattr(cls, "EDAM_format:3018",
            PermissibleValue(
                text="EDAM_format:3018",
                title="ZTR",
                description="ZTR format for storing chromatogram data from DNA sequencing instruments."))
        setattr(cls, "EDAM_format:3019",
            PermissibleValue(
                text="EDAM_format:3019",
                title="GVF",
                description="""Genome Variation Format (GVF). A GFF3-compatible format with defined header and attribute tags for sequence variation."""))
        setattr(cls, "EDAM_format:3020",
            PermissibleValue(
                text="EDAM_format:3020",
                title="BCF",
                description="""BCF is the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation)."""))
        setattr(cls, "EDAM_format:3033",
            PermissibleValue(
                text="EDAM_format:3033",
                title="Matrix format",
                description="Format of a matrix (array) of numerical values."))
        setattr(cls, "EDAM_format:3097",
            PermissibleValue(
                text="EDAM_format:3097",
                title="Protein domain classification format",
                description="""Format of data concerning the classification of the sequences and/or structures of protein structural domain(s)."""))
        setattr(cls, "EDAM_format:3098",
            PermissibleValue(
                text="EDAM_format:3098",
                title="Raw SCOP domain classification format",
                description="""Format of raw SCOP domain classification data files.
These are the parsable data files provided by SCOP."""))
        setattr(cls, "EDAM_format:3099",
            PermissibleValue(
                text="EDAM_format:3099",
                title="Raw CATH domain classification format",
                description="""Format of raw CATH domain classification data files.
These are the parsable data files provided by CATH."""))
        setattr(cls, "EDAM_format:3100",
            PermissibleValue(
                text="EDAM_format:3100",
                title="CATH domain report format",
                description="""Format of summary of domain classification information for a CATH domain.
The report (for example http://www.cathdb.info/domain/1cukA01) includes CATH codes for levels in the hierarchy for the domain, level descriptions and relevant data and links."""))
        setattr(cls, "EDAM_format:3155",
            PermissibleValue(
                text="EDAM_format:3155",
                title="SBRML",
                description="""Systems Biology Result Markup Language (SBRML), the standard XML format for simulated or calculated results (e.g. trajectories) of systems biology models."""))
        setattr(cls, "EDAM_format:3156",
            PermissibleValue(
                text="EDAM_format:3156",
                title="BioPAX",
                description="BioPAX is an exchange format for pathway data, with its data model defined in OWL."))
        setattr(cls, "EDAM_format:3157",
            PermissibleValue(
                text="EDAM_format:3157",
                title="EBI Application Result XML",
                description="""EBI Application Result XML is a format returned by sequence similarity search Web services at EBI."""))
        setattr(cls, "EDAM_format:3158",
            PermissibleValue(
                text="EDAM_format:3158",
                title="PSI MI XML (MIF)",
                description="XML Molecular Interaction Format (MIF), standardised by HUPO PSI MI."))
        setattr(cls, "EDAM_format:3159",
            PermissibleValue(
                text="EDAM_format:3159",
                title="phyloXML",
                description="""phyloXML is a standardised XML format for phylogenetic trees, networks, and associated data."""))
        setattr(cls, "EDAM_format:3160",
            PermissibleValue(
                text="EDAM_format:3160",
                title="NeXML",
                description="NeXML is a standardised XML format for rich phyloinformatic data."))
        setattr(cls, "EDAM_format:3161",
            PermissibleValue(
                text="EDAM_format:3161",
                title="MAGE-ML",
                description="MAGE-ML XML format for microarray expression data, standardised by MGED (now FGED)."))
        setattr(cls, "EDAM_format:3162",
            PermissibleValue(
                text="EDAM_format:3162",
                title="MAGE-TAB",
                description="""MAGE-TAB textual format for microarray expression data, standardised by MGED (now FGED)."""))
        setattr(cls, "EDAM_format:3163",
            PermissibleValue(
                text="EDAM_format:3163",
                title="GCDML",
                description="""GCDML XML format for genome and metagenome metadata according to MIGS/MIMS/MIMARKS information standards, standardised by the Genomic Standards Consortium (GSC)."""))
        setattr(cls, "EDAM_format:3164",
            PermissibleValue(
                text="EDAM_format:3164",
                title="GTrack",
                description="""'GTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GTrack' is the tabular format for representing features of sequences and genomes.
GTrack is a generic and optimised tabular format for genome or sequence feature tracks. GTrack unifies the power of other track formats (e.g. GFF3, BED, WIG), and while optimised in size, adds more flexibility, customisation, and automation (\"machine understandability\")."""))
        setattr(cls, "EDAM_format:3166",
            PermissibleValue(
                text="EDAM_format:3166",
                title="Biological pathway or network report format",
                description="Data format for a report of information derived from a biological pathway or network."))
        setattr(cls, "EDAM_format:3167",
            PermissibleValue(
                text="EDAM_format:3167",
                title="Experiment annotation format",
                description="Data format for annotation on a laboratory experiment."))
        setattr(cls, "EDAM_format:3235",
            PermissibleValue(
                text="EDAM_format:3235",
                title="Cytoband format",
                description="""Cytoband format for chromosome cytobands.
Reflects a UCSC Browser DB table."""))
        setattr(cls, "EDAM_format:3239",
            PermissibleValue(
                text="EDAM_format:3239",
                title="CopasiML",
                description="CopasiML, the native format of COPASI."))
        setattr(cls, "EDAM_format:3240",
            PermissibleValue(
                text="EDAM_format:3240",
                title="CellML",
                description="CellML, the format for mathematical models of biological and other networks."))
        setattr(cls, "EDAM_format:3242",
            PermissibleValue(
                text="EDAM_format:3242",
                title="PSI MI TAB (MITAB)",
                description="Tabular Molecular Interaction format (MITAB), standardised by HUPO PSI MI."))
        setattr(cls, "EDAM_format:3243",
            PermissibleValue(
                text="EDAM_format:3243",
                title="PSI-PAR",
                description="""Protein affinity format (PSI-PAR), standardised by HUPO PSI MI. It is compatible with PSI MI XML (MIF) and uses the same XML Schema."""))
        setattr(cls, "EDAM_format:3244",
            PermissibleValue(
                text="EDAM_format:3244",
                title="mzML",
                description="""mzML format for raw spectrometer output data, standardised by HUPO PSI MSS.
mzML is the successor and unifier of the mzData format developed by PSI and mzXML developed at the Seattle Proteome Center."""))
        setattr(cls, "EDAM_format:3245",
            PermissibleValue(
                text="EDAM_format:3245",
                title="Mass spectrometry data format",
                description="Format for mass pectra and derived data, include peptide sequences etc."))
        setattr(cls, "EDAM_format:3246",
            PermissibleValue(
                text="EDAM_format:3246",
                title="TraML",
                description="""TraML (Transition Markup Language) is the format for mass spectrometry transitions, standardised by HUPO PSI MSS."""))
        setattr(cls, "EDAM_format:3247",
            PermissibleValue(
                text="EDAM_format:3247",
                title="mzIdentML",
                description="""mzIdentML is the exchange format for peptides and proteins identified from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of proteomics search engines."""))
        setattr(cls, "EDAM_format:3248",
            PermissibleValue(
                text="EDAM_format:3248",
                title="mzQuantML",
                description="""mzQuantML is the format for quantitation values associated with peptides, proteins and small molecules from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of quantitation software for proteomics."""))
        setattr(cls, "EDAM_format:3249",
            PermissibleValue(
                text="EDAM_format:3249",
                title="GelML",
                description="""GelML is the format for describing the process of gel electrophoresis, standardised by HUPO PSI PS."""))
        setattr(cls, "EDAM_format:3250",
            PermissibleValue(
                text="EDAM_format:3250",
                title="spML",
                description="""spML is the format for describing proteomics sample processing, other than using gels, prior to mass spectrometric protein identification, standardised by HUPO PSI PS. It may also be applicable for metabolomics."""))
        setattr(cls, "EDAM_format:3252",
            PermissibleValue(
                text="EDAM_format:3252",
                title="OWL Functional Syntax",
                description="A human-readable encoding for the Web Ontology Language (OWL)."))
        setattr(cls, "EDAM_format:3253",
            PermissibleValue(
                text="EDAM_format:3253",
                title="Manchester OWL Syntax",
                description="""A syntax for writing OWL class expressions.
This format was influenced by the OWL Abstract Syntax and the DL style syntax."""))
        setattr(cls, "EDAM_format:3254",
            PermissibleValue(
                text="EDAM_format:3254",
                title="KRSS2 Syntax",
                description="""A superset of the \"Description-Logic Knowledge Representation System Specification from the KRSS Group of the ARPA Knowledge Sharing Effort\".
This format is used in Protege 4."""))
        setattr(cls, "EDAM_format:3255",
            PermissibleValue(
                text="EDAM_format:3255",
                title="Turtle",
                description="""The SPARQL Query Language incorporates a very similar syntax.
The Terse RDF Triple Language (Turtle) is a human-friendly serialisation format for RDF (Resource Description Framework) graphs."""))
        setattr(cls, "EDAM_format:3256",
            PermissibleValue(
                text="EDAM_format:3256",
                title="N-Triples",
                description="""A plain text serialisation format for RDF (Resource Description Framework) graphs, and a subset of the Turtle (Terse RDF Triple Language) format.
N-Triples should not be confused with Notation 3 which is a superset of Turtle."""))
        setattr(cls, "EDAM_format:3257",
            PermissibleValue(
                text="EDAM_format:3257",
                title="Notation3",
                description="""A shorthand non-XML serialisation of Resource Description Framework model, designed with human-readability in mind."""))
        setattr(cls, "EDAM_format:3261",
            PermissibleValue(
                text="EDAM_format:3261",
                title="RDF/XML",
                description="""RDF/XML can be used as a standard serialisation syntax for OWL DL, but not for OWL Full.
Resource Description Framework (RDF) XML format."""))
        setattr(cls, "EDAM_format:3262",
            PermissibleValue(
                text="EDAM_format:3262",
                title="OWL/XML",
                description="OWL ontology XML serialisation format."))
        setattr(cls, "EDAM_format:3281",
            PermissibleValue(
                text="EDAM_format:3281",
                title="A2M",
                description="""The A2M format is used as the primary format for multiple alignments of protein or nucleic-acid sequences in the SAM suite of tools. It is a small modification of FASTA format for sequences and is compatible with most tools that read FASTA."""))
        setattr(cls, "EDAM_format:3284",
            PermissibleValue(
                text="EDAM_format:3284",
                title="SFF",
                description="""Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing."""))
        setattr(cls, "EDAM_format:3285",
            PermissibleValue(
                text="EDAM_format:3285",
                title="MAP",
                description="The MAP file describes SNPs and is used by the Plink package."))
        setattr(cls, "EDAM_format:3286",
            PermissibleValue(
                text="EDAM_format:3286",
                title="PED",
                description="The PED file describes individuals and genetic data and is used by the Plink package."))
        setattr(cls, "EDAM_format:3287",
            PermissibleValue(
                text="EDAM_format:3287",
                title="Individual genetic data format",
                description="Data format for a metadata on an individual and their genetic data."))
        setattr(cls, "EDAM_format:3288",
            PermissibleValue(
                text="EDAM_format:3288",
                title="PED/MAP",
                description="The PED/MAP file describes data used by the Plink package."))
        setattr(cls, "EDAM_format:3309",
            PermissibleValue(
                text="EDAM_format:3309",
                title="CT",
                description="File format of a CT (Connectivity Table) file from the RNAstructure package."))
        setattr(cls, "EDAM_format:3310",
            PermissibleValue(
                text="EDAM_format:3310",
                title="SS",
                description="XRNA old input style format."))
        setattr(cls, "EDAM_format:3311",
            PermissibleValue(
                text="EDAM_format:3311",
                title="RNAML",
                description="RNA Markup Language."))
        setattr(cls, "EDAM_format:3312",
            PermissibleValue(
                text="EDAM_format:3312",
                title="GDE",
                description="Format for the Genetic Data Environment (GDE)."))
        setattr(cls, "EDAM_format:3313",
            PermissibleValue(
                text="EDAM_format:3313",
                title="BLC",
                description="""A multiple alignment in vertical format, as used in the AMPS (Alignment of Multiple Protein Sequences) package."""))
        setattr(cls, "EDAM_format:3326",
            PermissibleValue(
                text="EDAM_format:3326",
                title="Data index format",
                description="Format of a data index of some type."))
        setattr(cls, "EDAM_format:3327",
            PermissibleValue(
                text="EDAM_format:3327",
                title="BAI",
                description="BAM indexing format."))
        setattr(cls, "EDAM_format:3328",
            PermissibleValue(
                text="EDAM_format:3328",
                title="HMMER2",
                description="HMMER profile HMM file for HMMER versions 2.x."))
        setattr(cls, "EDAM_format:3329",
            PermissibleValue(
                text="EDAM_format:3329",
                title="HMMER3",
                description="HMMER profile HMM file for HMMER versions 3.x."))
        setattr(cls, "EDAM_format:3330",
            PermissibleValue(
                text="EDAM_format:3330",
                title="PO",
                description="""PO is the output format of Partial Order Alignment program (POA) performing Multiple Sequence Alignment (MSA)."""))
        setattr(cls, "EDAM_format:3331",
            PermissibleValue(
                text="EDAM_format:3331",
                title="BLAST XML results format",
                description="XML format as produced by the NCBI Blast package."))
        setattr(cls, "EDAM_format:3462",
            PermissibleValue(
                text="EDAM_format:3462",
                title="CRAM",
                description="Reference-based compression of alignment format."))
        setattr(cls, "EDAM_format:3464",
            PermissibleValue(
                text="EDAM_format:3464",
                title="JSON",
                description="""JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs."""))
        setattr(cls, "EDAM_format:3466",
            PermissibleValue(
                text="EDAM_format:3466",
                title="EPS",
                description="Encapsulated PostScript format."))
        setattr(cls, "EDAM_format:3467",
            PermissibleValue(
                text="EDAM_format:3467",
                title="GIF",
                description="Graphics Interchange Format."))
        setattr(cls, "EDAM_format:3468",
            PermissibleValue(
                text="EDAM_format:3468",
                title="xls",
                description="Microsoft Excel spreadsheet format."))
        setattr(cls, "EDAM_format:3475",
            PermissibleValue(
                text="EDAM_format:3475",
                title="TSV",
                description="Tabular data represented as tab-separated values in a text file."))
        setattr(cls, "EDAM_format:3477",
            PermissibleValue(
                text="EDAM_format:3477",
                title="Cytoscape input file format",
                description="""Format of the cytoscape input file of gene expression ratios or values are specified over one or more experiments."""))
        setattr(cls, "EDAM_format:3484",
            PermissibleValue(
                text="EDAM_format:3484",
                title="ebwt",
                description="Bowtie format for indexed reference genome for \"small\" genomes."))
        setattr(cls, "EDAM_format:3485",
            PermissibleValue(
                text="EDAM_format:3485",
                title="RSF",
                description="""RSF-format files contain one or more sequences that may or may not be related. In addition to the sequence data, each sequence can be annotated with descriptive sequence information (from the GCG manual).
Rich sequence format."""))
        setattr(cls, "EDAM_format:3486",
            PermissibleValue(
                text="EDAM_format:3486",
                title="GCG format variant",
                description="Some format based on the GCG format."))
        setattr(cls, "EDAM_format:3487",
            PermissibleValue(
                text="EDAM_format:3487",
                title="BSML",
                description="Bioinformatics Sequence Markup Language format."))
        setattr(cls, "EDAM_format:3491",
            PermissibleValue(
                text="EDAM_format:3491",
                title="ebwtl",
                description="Bowtie format for indexed reference genome for \"large\" genomes."))
        setattr(cls, "EDAM_format:3499",
            PermissibleValue(
                text="EDAM_format:3499",
                title="Ensembl variation file format",
                description="Ensembl standard format for variation data."))
        setattr(cls, "EDAM_format:3506",
            PermissibleValue(
                text="EDAM_format:3506",
                title="docx",
                description="Microsoft Word format."))
        setattr(cls, "EDAM_format:3507",
            PermissibleValue(
                text="EDAM_format:3507",
                title="Document format",
                description="Format of documents including word processor, spreadsheet and presentation."))
        setattr(cls, "EDAM_format:3508",
            PermissibleValue(
                text="EDAM_format:3508",
                title="PDF",
                description="Portable Document Format."))
        setattr(cls, "EDAM_format:3547",
            PermissibleValue(
                text="EDAM_format:3547",
                title="Image format",
                description="Format used for images and image metadata."))
        setattr(cls, "EDAM_format:3548",
            PermissibleValue(
                text="EDAM_format:3548",
                title="DICOM format",
                description="""Medical image format corresponding to the Digital Imaging and Communications in Medicine (DICOM) standard."""))
        setattr(cls, "EDAM_format:3549",
            PermissibleValue(
                text="EDAM_format:3549",
                title="nii",
                description="""An open file format from the Neuroimaging Informatics Technology Initiative (NIfTI) commonly used to store brain imaging data obtained using Magnetic Resonance Imaging (MRI) methods."""))
        setattr(cls, "EDAM_format:3550",
            PermissibleValue(
                text="EDAM_format:3550",
                title="mhd",
                description="""Text-based tagged file format for medical images generated using the MetaImage software package."""))
        setattr(cls, "EDAM_format:3551",
            PermissibleValue(
                text="EDAM_format:3551",
                title="nrrd",
                description="""Nearly Raw Rasta Data format designed to support scientific visualisation and image processing involving N-dimensional raster data."""))
        setattr(cls, "EDAM_format:3554",
            PermissibleValue(
                text="EDAM_format:3554",
                title="R file format",
                description="""File format used for scripts written in the R programming language for execution within the R software environment, typically for statistical computation and graphics."""))
        setattr(cls, "EDAM_format:3555",
            PermissibleValue(
                text="EDAM_format:3555",
                title="SPSS",
                description="File format used for scripts for the Statistical Package for the Social Sciences."))
        setattr(cls, "EDAM_format:3556",
            PermissibleValue(
                text="EDAM_format:3556",
                title="MHTML",
                description="""MHTML is not strictly an HTML format, it is encoded as an HTML email message (although with multipart/related instead of multipart/alternative). It, however, contains the main HTML block as its core, and thus it is for practical reasons included in EDAM as a specialisation of 'HTML'.
MIME HTML format for Web pages, which can include external resources, including images, Flash animations and so on."""))
        setattr(cls, "EDAM_format:3578",
            PermissibleValue(
                text="EDAM_format:3578",
                title="IDAT",
                description="""Proprietary file format for (raw) BeadArray data used by genomewide profiling platforms from Illumina Inc. This format is output directly from the scanner and stores summary intensities for each probe-type on an array."""))
        setattr(cls, "EDAM_format:3579",
            PermissibleValue(
                text="EDAM_format:3579",
                title="JPG",
                description="""Joint Picture Group file format for lossy graphics file.
Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type."""))
        setattr(cls, "EDAM_format:3580",
            PermissibleValue(
                text="EDAM_format:3580",
                title="rcc",
                description="""Reporter Code Count-A data file (.csv) output by the Nanostring nCounter Digital Analyzer, which contains gene sample information, probe information and probe counts."""))
        setattr(cls, "EDAM_format:3581",
            PermissibleValue(
                text="EDAM_format:3581",
                title="arff",
                description="""ARFF (Attribute-Relation File Format) is an ASCII text file format that describes a list of instances sharing a set of attributes.
This file format is for machine learning."""))
        setattr(cls, "EDAM_format:3582",
            PermissibleValue(
                text="EDAM_format:3582",
                title="afg",
                description="""AFG is a single text-based file assembly format that holds read and consensus information together."""))
        setattr(cls, "EDAM_format:3583",
            PermissibleValue(
                text="EDAM_format:3583",
                title="bedgraph",
                description="""Holds a tab-delimited chromosome /start /end / datavalue dataset.
The bedGraph format allows display of continuous-valued data in track format. This display type is useful for probability scores and transcriptome data."""))
        setattr(cls, "EDAM_format:3584",
            PermissibleValue(
                text="EDAM_format:3584",
                title="bedstrict",
                description="""Browser Extensible Data (BED) format of sequence annotation track that strictly does not contain non-standard fields beyond the first 3 columns.
Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not."""))
        setattr(cls, "EDAM_format:3585",
            PermissibleValue(
                text="EDAM_format:3585",
                title="bed6",
                description="""BED file format where each feature is described by chromosome, start, end, name, score, and strand.
Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 6"""))
        setattr(cls, "EDAM_format:3586",
            PermissibleValue(
                text="EDAM_format:3586",
                title="bed12",
                description="""A BED file where each feature is described by all twelve columns.
Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 12"""))
        setattr(cls, "EDAM_format:3587",
            PermissibleValue(
                text="EDAM_format:3587",
                title="chrominfo",
                description="""Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not.
Tabular format of chromosome names and sizes used by Galaxy."""))
        setattr(cls, "EDAM_format:3588",
            PermissibleValue(
                text="EDAM_format:3588",
                title="customtrack",
                description="""Custom Sequence annotation track format used by Galaxy.
Used for tracks/track views within galaxy."""))
        setattr(cls, "EDAM_format:3589",
            PermissibleValue(
                text="EDAM_format:3589",
                title="csfasta",
                description="""Color space FASTA format sequence variant.
FASTA format extended for color space information."""))
        setattr(cls, "EDAM_format:3590",
            PermissibleValue(
                text="EDAM_format:3590",
                title="HDF5",
                description="""An HDF5 file appears to the user as a directed graph. The nodes of this graph are the higher-level HDF5 objects that are exposed by the HDF5 APIs: Groups, Datasets, Named datatypes. Currently supported by the Python MDTraj package.
HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).
HDF5 is the new version, according to the HDF group, a completely different technology (https://support.hdfgroup.org/products/hdf4/ compared to HDF."""))
        setattr(cls, "EDAM_format:3591",
            PermissibleValue(
                text="EDAM_format:3591",
                title="TIFF",
                description="""A versatile bitmap format.
The TIFF format is perhaps the most versatile and diverse bitmap format in existence. Its extensible nature and support for numerous data compression schemes allow developers to customize the TIFF format to fit any peculiar data storage needs."""))
        setattr(cls, "EDAM_format:3592",
            PermissibleValue(
                text="EDAM_format:3592",
                title="BMP",
                description="""Although it is based on Windows internal bitmap data structures, it is supported by many non-Windows and non-PC applications.
Standard bitmap storage format in the Microsoft Windows environment."""))
        setattr(cls, "EDAM_format:3593",
            PermissibleValue(
                text="EDAM_format:3593",
                title="im",
                description="""IFUNC library reads and writes most uncompressed interchange versions of this format.
IM is a format used by LabEye and other applications based on the IFUNC image processing library."""))
        setattr(cls, "EDAM_format:3594",
            PermissibleValue(
                text="EDAM_format:3594",
                title="pcd",
                description="""PCD was developed by Kodak. A PCD file contains five different resolution (ranging from low to high) of a slide or film negative. Due to it PCD is often used by many photographers and graphics professionals for high-end printed applications.
Photo CD format, which is the highest resolution format for images on a CD."""))
        setattr(cls, "EDAM_format:3595",
            PermissibleValue(
                text="EDAM_format:3595",
                title="pcx",
                description="""PCX is an image file format that uses a simple form of run-length encoding. It is lossless."""))
        setattr(cls, "EDAM_format:3596",
            PermissibleValue(
                text="EDAM_format:3596",
                title="ppm",
                description="The PPM format is a lowest common denominator color image file format."))
        setattr(cls, "EDAM_format:3597",
            PermissibleValue(
                text="EDAM_format:3597",
                title="psd",
                description="""PSD (Photoshop Document) is a proprietary file that allows the user to work with the images' individual layers even after the file has been saved."""))
        setattr(cls, "EDAM_format:3598",
            PermissibleValue(
                text="EDAM_format:3598",
                title="xbm",
                description="""The XBM format was replaced by XPM for X11 in 1989.
X BitMap is a plain text binary image format used by the X Window System used for storing cursor and icon bitmaps used in the X GUI."""))
        setattr(cls, "EDAM_format:3599",
            PermissibleValue(
                text="EDAM_format:3599",
                title="xpm",
                description="""Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type.
X PixMap (XPM) is an image file format used by the X Window System, it is intended primarily for creating icon pixmaps, and supports transparent pixels."""))
        setattr(cls, "EDAM_format:3600",
            PermissibleValue(
                text="EDAM_format:3600",
                title="rgb",
                description="""RGB file format is the native raster graphics file format for Silicon Graphics workstations."""))
        setattr(cls, "EDAM_format:3601",
            PermissibleValue(
                text="EDAM_format:3601",
                title="pbm",
                description="""The PBM format is a lowest common denominator monochrome file format. It serves as the common language of a large family of bitmap image conversion filters."""))
        setattr(cls, "EDAM_format:3602",
            PermissibleValue(
                text="EDAM_format:3602",
                title="pgm",
                description="""It is designed to be extremely easy to learn and write programs for.
The PGM format is a lowest common denominator grayscale file format."""))
        setattr(cls, "EDAM_format:3603",
            PermissibleValue(
                text="EDAM_format:3603",
                title="PNG",
                description="""It iis expected to replace the Graphics Interchange Format (GIF).
PNG is a file format for image compression."""))
        setattr(cls, "EDAM_format:3604",
            PermissibleValue(
                text="EDAM_format:3604",
                title="SVG",
                description="""Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics with support for interactivity and animation.
The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999."""))
        setattr(cls, "EDAM_format:3605",
            PermissibleValue(
                text="EDAM_format:3605",
                title="rast",
                description="""Sun Raster is a raster graphics file format used on SunOS by Sun Microsystems.
The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999."""))
        setattr(cls, "EDAM_format:3606",
            PermissibleValue(
                text="EDAM_format:3606",
                title="Sequence quality report format (text)",
                description="Textual report format for sequence quality for reports from sequencing machines."))
        setattr(cls, "EDAM_format:3607",
            PermissibleValue(
                text="EDAM_format:3607",
                title="qual",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences).
Phred quality scores are defined as a property which is logarithmically related to the base-calling error probabilities."""))
        setattr(cls, "EDAM_format:3608",
            PermissibleValue(
                text="EDAM_format:3608",
                title="qualsolexa",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) for Solexa/Illumina 1.0 format.
Solexa/Illumina 1.0 format can encode a Solexa/Illumina quality score from -5 to 62 using ASCII 59 to 126 (although in raw read data Solexa scores from -5 to 40 only are expected)"""))
        setattr(cls, "EDAM_format:3609",
            PermissibleValue(
                text="EDAM_format:3609",
                title="qualillumina",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) from Illumina 1.5 and before Illumina 1.8.
Starting in Illumina 1.5 and before Illumina 1.8, the Phred scores 0 to 2 have a slightly different meaning. The values 0 and 1 are no longer used and the value 2, encoded by ASCII 66 \"B\", is used also at the end of reads as a Read Segment Quality Control Indicator."""))
        setattr(cls, "EDAM_format:3610",
            PermissibleValue(
                text="EDAM_format:3610",
                title="qualsolid",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) for SOLiD data.
For SOLiD data, the sequence is in color space, except the first position. The quality values are those of the Sanger format."""))
        setattr(cls, "EDAM_format:3611",
            PermissibleValue(
                text="EDAM_format:3611",
                title="qual454",
                description="""FASTQ format subset for Phred sequencing quality score data only (no sequences) from 454 sequencers."""))
        setattr(cls, "EDAM_format:3612",
            PermissibleValue(
                text="EDAM_format:3612",
                title="ENCODE peak format",
                description="""Format that covers both the broad peak format and narrow peak format from ENCODE.
Human ENCODE peak format."""))
        setattr(cls, "EDAM_format:3613",
            PermissibleValue(
                text="EDAM_format:3613",
                title="ENCODE narrow peak format",
                description="""Format that covers both the broad peak format and narrow peak format from ENCODE.
Human ENCODE narrow peak format."""))
        setattr(cls, "EDAM_format:3614",
            PermissibleValue(
                text="EDAM_format:3614",
                title="ENCODE broad peak format",
                description="Human ENCODE broad peak format."))
        setattr(cls, "EDAM_format:3615",
            PermissibleValue(
                text="EDAM_format:3615",
                title="bgzip",
                description="""BAM files are compressed using a variant of GZIP (GNU ZIP), into a format called BGZF (Blocked GNU Zip Format).
Blocked GNU Zip format."""))
        setattr(cls, "EDAM_format:3616",
            PermissibleValue(
                text="EDAM_format:3616",
                title="tabix",
                description="TAB-delimited genome position file index format."))
        setattr(cls, "EDAM_format:3617",
            PermissibleValue(
                text="EDAM_format:3617",
                title="Graph format",
                description="Data format for graph data."))
        setattr(cls, "EDAM_format:3618",
            PermissibleValue(
                text="EDAM_format:3618",
                title="xgmml",
                description="XML-based format used to store graph descriptions within Galaxy."))
        setattr(cls, "EDAM_format:3619",
            PermissibleValue(
                text="EDAM_format:3619",
                title="sif",
                description="""SIF (simple interaction file) Format - a network/pathway format used for instance in cytoscape."""))
        setattr(cls, "EDAM_format:3620",
            PermissibleValue(
                text="EDAM_format:3620",
                title="xlsx",
                description="""MS Excel spreadsheet format consisting of a set of XML documents stored in a ZIP-compressed file."""))
        setattr(cls, "EDAM_format:3621",
            PermissibleValue(
                text="EDAM_format:3621",
                title="SQLite format",
                description="Data format used by the SQLite database."))
        setattr(cls, "EDAM_format:3622",
            PermissibleValue(
                text="EDAM_format:3622",
                title="Gemini SQLite format",
                description="Data format used by the SQLite database conformant to the Gemini schema."))
        setattr(cls, "EDAM_format:3624",
            PermissibleValue(
                text="EDAM_format:3624",
                title="snpeffdb",
                description="An index of a genome database, indexed for use by the snpeff tool."))
        setattr(cls, "EDAM_format:3626",
            PermissibleValue(
                text="EDAM_format:3626",
                title="MAT",
                description="Binary format used by MATLAB files to store workspace variables."))
        setattr(cls, "EDAM_format:3650",
            PermissibleValue(
                text="EDAM_format:3650",
                title="NetCDF",
                description="""Format used by netCDF software library for writing and reading chromatography-MS data files. Also used to store trajectory atom coordinates information, such as the ones obtained by Molecular Dynamics simulations.
Network Common Data Form (NetCDF) library is supported by AMBER MD package from version 9."""))
        setattr(cls, "EDAM_format:3651",
            PermissibleValue(
                text="EDAM_format:3651",
                title="MGF",
                description="""Files includes *m*/*z*, intensity pairs separated by headers; headers can contain a bit more information, including search engine instructions.
Mascot Generic Format. Encodes multiple MS/MS spectra in a single file."""))
        setattr(cls, "EDAM_format:3652",
            PermissibleValue(
                text="EDAM_format:3652",
                title="dta",
                description="""Each file contains one header line for the known or assumed charge and the mass of the precursor peptide ion, calculated from the measured *m*/*z* and the charge. This one line was then followed by all the *m*/*z*, intensity pairs that represent the spectrum.
Spectral data format file where each spectrum is written to a separate file."""))
        setattr(cls, "EDAM_format:3653",
            PermissibleValue(
                text="EDAM_format:3653",
                title="pkl",
                description="""Differ from .dta only in subtleties of the header line format and content and support the added feature of being able to.
Spectral data file similar to dta."""))
        setattr(cls, "EDAM_format:3654",
            PermissibleValue(
                text="EDAM_format:3654",
                title="mzXML",
                description="""Common file format for proteomics mass spectrometric data developed at the Seattle Proteome Center/Institute for Systems Biology."""))
        setattr(cls, "EDAM_format:3655",
            PermissibleValue(
                text="EDAM_format:3655",
                title="pepXML",
                description="""Open data format for the storage, exchange, and processing of peptide sequence assignments of MS/MS scans, intended to provide a common data output format for many different MS/MS search engines and subsequent peptide-level analyses."""))
        setattr(cls, "EDAM_format:3657",
            PermissibleValue(
                text="EDAM_format:3657",
                title="GPML",
                description="""Graphical Pathway Markup Language (GPML) is an XML format used for exchanging biological pathways."""))
        setattr(cls, "EDAM_format:3665",
            PermissibleValue(
                text="EDAM_format:3665",
                title="K-mer countgraph",
                description="""A list of k-mers and their occurrences in a dataset. Can also be used as an implicit De Bruijn graph."""))
        setattr(cls, "EDAM_format:3681",
            PermissibleValue(
                text="EDAM_format:3681",
                title="mzTab",
                description="""For mass spectrometry-based chemical profiling data (including metabolomics), there is a derived (but incompatible) format mzTab-M (also named mzTab 2.0, http://edamontology.org/format_4058), and its lipidomics version mzTab-L (http://edamontology.org/format_4059).
For more detailed metadata, there are formats such as mzIdentML (http://edamontology.org/format_3247) and mzQuantML (http://edamontology.org/format_3248).
The reference implementation of mzTab in Java is https://github.com/PRIDE-Archive/jmzTab (maintenance stopped in 2022).
mzTab is a light-weight, tab-delimited format for mass spectrometry-based proteomics data.
mzTab is alternatively named mzTab 1.0, as opposed to mzTab 2.0 (and 2.1), which is the incompatible mzTab-M format for chemical profiling e.g. metabolomics."""))
        setattr(cls, "EDAM_format:3682",
            PermissibleValue(
                text="EDAM_format:3682",
                title="imzML metadata file",
                description="""imzML data are recorded in 2 files: '.imzXML' (this concept) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (http://edamontology.org/format_3839) is a binary file containing the mass spectra. This entry is for the metadata XML file.
imzML metadata is a data format for mass spectrometry imaging metadata."""))
        setattr(cls, "EDAM_format:3683",
            PermissibleValue(
                text="EDAM_format:3683",
                title="qcML",
                description="""The focus of qcML is towards mass spectrometry based proteomics, but the format is suitable for metabolomics and sequencing as well.
qcML is an XML format for quality-related data of mass spectrometry and other high-throughput measurements."""))
        setattr(cls, "EDAM_format:3684",
            PermissibleValue(
                text="EDAM_format:3684",
                title="PRIDE XML",
                description="""PRIDE XML is an XML format for mass spectra, peptide and protein identifications, and metadata about a corresponding measurement, sample, experiment."""))
        setattr(cls, "EDAM_format:3685",
            PermissibleValue(
                text="EDAM_format:3685",
                title="SED-ML",
                description="""Simulation Experiment Description Markup Language (SED-ML) is an XML format for encoding simulation setups, according to the MIASE (Minimum Information About a Simulation Experiment) requirements."""))
        setattr(cls, "EDAM_format:3686",
            PermissibleValue(
                text="EDAM_format:3686",
                title="COMBINE OMEX",
                description="""An OMEX file is a ZIP container that includes a manifest file, listing the content of the archive, an optional metadata file adding information about the archive and its content, and the files describing the model. OMEX is one of the standardised formats within COMBINE (Computational Modeling in Biology Network).
Open Modeling EXchange format (OMEX) is a ZIPped format for encapsulating all information necessary for a modeling and simulation project in systems biology."""))
        setattr(cls, "EDAM_format:3687",
            PermissibleValue(
                text="EDAM_format:3687",
                title="ISA-TAB",
                description="""ISA-TAB is based on MAGE-TAB. Other than tabular, the ISA model can also be represented in RDF, and in JSON (compliable with a set of defined JSON Schemata).
The Investigation / Study / Assay (ISA) tab-delimited (TAB) format incorporates metadata from experiments employing a combination of technologies."""))
        setattr(cls, "EDAM_format:3688",
            PermissibleValue(
                text="EDAM_format:3688",
                title="SBtab",
                description="SBtab is a tabular format for biochemical network models."))
        setattr(cls, "EDAM_format:3689",
            PermissibleValue(
                text="EDAM_format:3689",
                title="BCML",
                description="Biological Connection Markup Language (BCML) is an XML format for biological pathways."))
        setattr(cls, "EDAM_format:3690",
            PermissibleValue(
                text="EDAM_format:3690",
                title="BDML",
                description="""Biological Dynamics Markup Language (BDML) is an XML format for quantitative data describing biological dynamics."""))
        setattr(cls, "EDAM_format:3691",
            PermissibleValue(
                text="EDAM_format:3691",
                title="BEL",
                description="""Biological Expression Language (BEL) is a textual format for representing scientific findings in life sciences in a computable form."""))
        setattr(cls, "EDAM_format:3692",
            PermissibleValue(
                text="EDAM_format:3692",
                title="SBGN-ML",
                description="""SBGN-ML is an XML format for Systems Biology Graphical Notation (SBGN) diagrams of biological pathways or networks."""))
        setattr(cls, "EDAM_format:3693",
            PermissibleValue(
                text="EDAM_format:3693",
                title="AGP",
                description="""AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome)."""))
        setattr(cls, "EDAM_format:3696",
            PermissibleValue(
                text="EDAM_format:3696",
                title="PS",
                description="PostScript format."))
        setattr(cls, "EDAM_format:3698",
            PermissibleValue(
                text="EDAM_format:3698",
                title="SRA format",
                description="""SRA archive format (SRA) is the archive format used for input to the NCBI Sequence Read Archive."""))
        setattr(cls, "EDAM_format:3699",
            PermissibleValue(
                text="EDAM_format:3699",
                title="VDB",
                description="""VDB ('vertical database') is the native format used for export from the NCBI Sequence Read Archive."""))
        setattr(cls, "EDAM_format:3701",
            PermissibleValue(
                text="EDAM_format:3701",
                title="Sequin format",
                description="""A five-column, tab-delimited table of feature locations and qualifiers for importing annotation into an existing Sequin submission (an NCBI tool for submitting and updating GenBank entries)."""))
        setattr(cls, "EDAM_format:3702",
            PermissibleValue(
                text="EDAM_format:3702",
                title="MSF",
                description="""Proprietary mass-spectrometry format of Thermo Scientific's ProteomeDiscoverer software.
This format corresponds to an SQLite database, and you can look into the files with e.g. SQLiteStudio3. There are also some readers (http://doi.org/10.1021/pr2005154) and converters (http://doi.org/10.1016/j.jprot.2015.06.015) for this format available, which re-engineered the database schema, but there is no official DB schema specification of Thermo Scientific for the format."""))
        setattr(cls, "EDAM_format:3706",
            PermissibleValue(
                text="EDAM_format:3706",
                title="Biodiversity data format",
                description="Data format for biodiversity data."))
        setattr(cls, "EDAM_format:3708",
            PermissibleValue(
                text="EDAM_format:3708",
                title="ABCD format",
                description="""Exchange format of the Access to Biological Collections Data (ABCD) Schema; a standard for the access to and exchange of data about specimens and observations (primary biodiversity data)."""))
        setattr(cls, "EDAM_format:3709",
            PermissibleValue(
                text="EDAM_format:3709",
                title="GCT/Res format",
                description="""Tab-delimited text files of GenePattern that contain a column for each sample, a row for each gene, and an expression value for each gene in each sample."""))
        setattr(cls, "EDAM_format:3710",
            PermissibleValue(
                text="EDAM_format:3710",
                title="WIFF format",
                description="Mass spectrum file format from QSTAR and QTRAP instruments (ABI/Sciex)."))
        setattr(cls, "EDAM_format:3711",
            PermissibleValue(
                text="EDAM_format:3711",
                title="X!Tandem XML",
                description="""Output format used by X! series search engines that is based on the XML language BIOML."""))
        setattr(cls, "EDAM_format:3712",
            PermissibleValue(
                text="EDAM_format:3712",
                title="Thermo RAW",
                description="""Proprietary file format for mass spectrometry data from Thermo Scientific.
Proprietary format for which documentation is not available."""))
        setattr(cls, "EDAM_format:3713",
            PermissibleValue(
                text="EDAM_format:3713",
                title="Mascot .dat file",
                description="\"Raw\" result file from Mascot database search."))
        setattr(cls, "EDAM_format:3714",
            PermissibleValue(
                text="EDAM_format:3714",
                title="MaxQuant APL peaklist format",
                description="""Format of peak list files from Andromeda search engine (MaxQuant) that consist of arbitrarily many spectra."""))
        setattr(cls, "EDAM_format:3725",
            PermissibleValue(
                text="EDAM_format:3725",
                title="SBOL",
                description="""SBOL introduces a standardised format for the electronic exchange of information on the structural and functional aspects of biological designs.
Synthetic Biology Open Language (SBOL) is an XML format for the specification and exchange of biological design information in synthetic biology."""))
        setattr(cls, "EDAM_format:3726",
            PermissibleValue(
                text="EDAM_format:3726",
                title="PMML",
                description="""One or more mining models can be contained in a PMML document.
PMML uses XML to represent mining models. The structure of the models is described by an XML Schema."""))
        setattr(cls, "EDAM_format:3727",
            PermissibleValue(
                text="EDAM_format:3727",
                title="OME-TIFF",
                description="""An OME-TIFF dataset consists of one or more files in standard TIFF or BigTIFF format, with the file extension .ome.tif or .ome.tiff, and an identical (or in the case of multiple files, nearly identical) string of OME-XML metadata embedded in the ImageDescription tag of each file's first IFD (Image File Directory). BigTIFF file extensions are also permitted, with the file extension .ome.tf2, .ome.tf8 or .ome.btf, but note these file extensions are an addition to the original specification, and software using an older version of the specification may not be able to handle these file extensions.
Image file format used by the Open Microscopy Environment (OME).
OME develops open-source software and data format standards for the storage and manipulation of biological microscopy data. It is a joint project between universities, research establishments, industry and the software development community."""))
        setattr(cls, "EDAM_format:3728",
            PermissibleValue(
                text="EDAM_format:3728",
                title="LocARNA PP",
                description="""Format for multiple aligned or single sequences together with the probabilistic description of the (consensus) RNA secondary structure ensemble by probabilities of base pairs, base pair stackings, and base pairs and unpaired bases in the loop of base pairs.
The LocARNA PP format combines sequence or alignment information and (respectively, single or consensus) ensemble probabilities into an PP 2.0 record."""))
        setattr(cls, "EDAM_format:3729",
            PermissibleValue(
                text="EDAM_format:3729",
                title="dbGaP format",
                description="""Input format used by the Database of Genotypes and Phenotypes (dbGaP).
The Database of Genotypes and Phenotypes (dbGaP) is a National Institutes of Health (NIH) sponsored repository charged to archive, curate and distribute information produced by studies investigating the interaction of genotype and phenotype."""))
        setattr(cls, "EDAM_format:3746",
            PermissibleValue(
                text="EDAM_format:3746",
                title="BIOM format",
                description="""BIOM is a recognised standard for the Earth Microbiome Project, and is a project supported by Genomics Standards Consortium. Supported in QIIME, Mothur, MEGAN, etc.
The BIological Observation Matrix (BIOM) is a format for representing biological sample by observation contingency tables in broad areas of comparative omics. The primary use of this format is to represent OTU tables and metagenome tables."""))
        setattr(cls, "EDAM_format:3747",
            PermissibleValue(
                text="EDAM_format:3747",
                title="protXML",
                description="""A format for storage, exchange, and processing of protein identifications created from ms/ms-derived peptide sequence data.
No human-consumable information about this format is available (see http://tools.proteomecenter.org/wiki/index.php?title=Formats:protXML)."""))
        setattr(cls, "EDAM_format:3748",
            PermissibleValue(
                text="EDAM_format:3748",
                title="Linked data format",
                description="""A linked data format enables publishing structured data as linked data (Linked Data), so that the data can be interlinked and become more useful through semantic queries."""))
        setattr(cls, "EDAM_format:3749",
            PermissibleValue(
                text="EDAM_format:3749",
                title="JSON-LD",
                description="""JSON-LD, or JavaScript Object Notation for Linked Data, is a method of encoding Linked Data using JSON."""))
        setattr(cls, "EDAM_format:3750",
            PermissibleValue(
                text="EDAM_format:3750",
                title="YAML",
                description="""Data in YAML format can be serialised into text, or binary format.
YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.
YAML version 1.2 is a superset of JSON; prior versions were \"not strictly compatible\"."""))
        setattr(cls, "EDAM_format:3751",
            PermissibleValue(
                text="EDAM_format:3751",
                title="DSV",
                description="Tabular data represented as values in a text file delimited by some character."))
        setattr(cls, "EDAM_format:3752",
            PermissibleValue(
                text="EDAM_format:3752",
                title="CSV",
                description="Tabular data represented as comma-separated values in a text file."))
        setattr(cls, "EDAM_format:3758",
            PermissibleValue(
                text="EDAM_format:3758",
                title="SEQUEST .out file",
                description="\"Raw\" result file from SEQUEST database search."))
        setattr(cls, "EDAM_format:3764",
            PermissibleValue(
                text="EDAM_format:3764",
                title="idXML",
                description="""XML file format for files containing information about peptide identifications from mass spectrometry data analysis carried out with OpenMS."""))
        setattr(cls, "EDAM_format:3765",
            PermissibleValue(
                text="EDAM_format:3765",
                title="KNIME datatable format",
                description="Data table formatted such that it can be passed/streamed within the KNIME platform."))
        setattr(cls, "EDAM_format:3770",
            PermissibleValue(
                text="EDAM_format:3770",
                title="UniProtKB XML",
                description="""UniProtKB XML sequence features format is an XML format available for downloading UniProt entries."""))
        setattr(cls, "EDAM_format:3771",
            PermissibleValue(
                text="EDAM_format:3771",
                title="UniProtKB RDF",
                description="""UniProtKB RDF sequence features format is an RDF format available for downloading UniProt entries (in RDF/XML)."""))
        setattr(cls, "EDAM_format:3772",
            PermissibleValue(
                text="EDAM_format:3772",
                title="BioJSON (BioXSD)",
                description="""BioJSON is a BioXSD-schema-based JSON format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web applications and APIs, and object-oriented programming.
Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioJSON' is the JSON format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'."""))
        setattr(cls, "EDAM_format:3773",
            PermissibleValue(
                text="EDAM_format:3773",
                title="BioYAML",
                description="""BioYAML is a BioXSD-schema-based YAML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web APIs, human readability and editing, and object-oriented programming.
Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioYAML' is the YAML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'."""))
        setattr(cls, "EDAM_format:3774",
            PermissibleValue(
                text="EDAM_format:3774",
                title="BioJSON (Jalview)",
                description="""BioJSON is a JSON format of single multiple sequence alignments, with their annotations, features, and custom visualisation and application settings for the Jalview workbench."""))
        setattr(cls, "EDAM_format:3775",
            PermissibleValue(
                text="EDAM_format:3775",
                title="GSuite",
                description="""'GSuite' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GSuite' is the tabular format for an annotated collection of individual GTrack files.
GSuite is a tabular format for collections of genome or sequence feature tracks, suitable for integrative multi-track analysis. GSuite contains links to genome/sequence tracks, with additional metadata."""))
        setattr(cls, "EDAM_format:3776",
            PermissibleValue(
                text="EDAM_format:3776",
                title="BTrack",
                description="""'BTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'BTrack' is the binary, optionally compressed HDF5-based version of the GTrack and GSuite formats.
BTrack is an HDF5-based binary format for genome or sequence feature tracks and their collections, suitable for integrative multi-track analysis. BTrack is a binary, compressed alternative to the GTrack and GSuite formats."""))
        setattr(cls, "EDAM_format:3777",
            PermissibleValue(
                text="EDAM_format:3777",
                title="MCPD",
                description="""Multi-Crop Passport Descriptors is a format available in 2 successive versions, V.1 (FAO/IPGRI 2001) and V.2 (FAO/Bioversity 2012).
The FAO/Bioversity/IPGRI Multi-Crop Passport Descriptors (MCPD) is an international standard format for exchange of germplasm information."""))
        setattr(cls, "EDAM_format:3780",
            PermissibleValue(
                text="EDAM_format:3780",
                title="Annotated text format",
                description="""Data format of an annotated text, e.g. with recognised entities, concepts, and relations."""))
        setattr(cls, "EDAM_format:3781",
            PermissibleValue(
                text="EDAM_format:3781",
                title="PubAnnotation format",
                description="JSON format of annotated scientific text used by PubAnnotations and other tools."))
        setattr(cls, "EDAM_format:3782",
            PermissibleValue(
                text="EDAM_format:3782",
                title="BioC",
                description="""BioC is a standardised XML format for sharing and integrating text data and annotations."""))
        setattr(cls, "EDAM_format:3783",
            PermissibleValue(
                text="EDAM_format:3783",
                title="PubTator format",
                description="Native textual export format of annotated scientific text from PubTator."))
        setattr(cls, "EDAM_format:3784",
            PermissibleValue(
                text="EDAM_format:3784",
                title="Open Annotation format",
                description="""A format of text annotation using the linked-data Open Annotation Data Model, serialised typically in RDF or JSON-LD."""))
        setattr(cls, "EDAM_format:3785",
            PermissibleValue(
                text="EDAM_format:3785",
                title="BioNLP Shared Task format",
                description="""A family of similar formats of text annotation, used by BRAT and other tools, known as BioNLP Shared Task format (BioNLP 2009 Shared Task on Event Extraction, BioNLP Shared Task 2011, BioNLP Shared Task 2013), BRAT format, BRAT standoff format, and similar."""))
        setattr(cls, "EDAM_format:3787",
            PermissibleValue(
                text="EDAM_format:3787",
                title="Query language",
                description="A query language (format) for structured database queries."))
        setattr(cls, "EDAM_format:3788",
            PermissibleValue(
                text="EDAM_format:3788",
                title="SQL",
                description="""SQL (Structured Query Language) is the de-facto standard query language (format of queries) for querying and manipulating data in relational databases."""))
        setattr(cls, "EDAM_format:3789",
            PermissibleValue(
                text="EDAM_format:3789",
                title="XQuery",
                description="""XQuery (XML Query) is a query language (format of queries) for querying and manipulating structured and unstructured data, usually in the form of XML, text, and with vendor-specific extensions for other data formats (JSON, binary, etc.)."""))
        setattr(cls, "EDAM_format:3790",
            PermissibleValue(
                text="EDAM_format:3790",
                title="SPARQL",
                description="""SPARQL (SPARQL Protocol and RDF Query Language) is a semantic query language for querying and manipulating data stored in Resource Description Framework (RDF) format."""))
        setattr(cls, "EDAM_format:3804",
            PermissibleValue(
                text="EDAM_format:3804",
                title="xsd",
                description="XML format for XML Schema."))
        setattr(cls, "EDAM_format:3811",
            PermissibleValue(
                text="EDAM_format:3811",
                title="XMFA",
                description="""XMFA format stands for eXtended Multi-FastA format and is used to store collinear sub-alignments that constitute a single genome alignment."""))
        setattr(cls, "EDAM_format:3812",
            PermissibleValue(
                text="EDAM_format:3812",
                title="GEN",
                description="The GEN file format contains genetic data and describes SNPs."))
        setattr(cls, "EDAM_format:3813",
            PermissibleValue(
                text="EDAM_format:3813",
                title="SAMPLE file format",
                description="""The SAMPLE file format contains information about each individual i.e. individual IDs, covariates, phenotypes and missing data proportions, from a GWAS study."""))
        setattr(cls, "EDAM_format:3814",
            PermissibleValue(
                text="EDAM_format:3814",
                title="SDF",
                description="""SDF is one of a family of chemical-data file formats developed by MDL Information Systems; it is intended especially for structural information."""))
        setattr(cls, "EDAM_format:3815",
            PermissibleValue(
                text="EDAM_format:3815",
                title="Molfile",
                description="""An MDL Molfile is a file format for holding information about the atoms, bonds, connectivity and coordinates of a molecule."""))
        setattr(cls, "EDAM_format:3816",
            PermissibleValue(
                text="EDAM_format:3816",
                title="Mol2",
                description="""Complete, portable representation of a SYBYL molecule. ASCII file which contains all the information needed to reconstruct a SYBYL molecule."""))
        setattr(cls, "EDAM_format:3817",
            PermissibleValue(
                text="EDAM_format:3817",
                title="latex",
                description="""format for the LaTeX document preparation system.
uses the TeX typesetting program format"""))
        setattr(cls, "EDAM_format:3818",
            PermissibleValue(
                text="EDAM_format:3818",
                title="ELAND format",
                description="""Tab-delimited text file format used by Eland - the read-mapping program distributed by Illumina with its sequencing analysis pipeline - which maps short Solexa sequence reads to the human reference genome."""))
        setattr(cls, "EDAM_format:3819",
            PermissibleValue(
                text="EDAM_format:3819",
                title="Relaxed PHYLIP Interleaved",
                description="""It differs from Phylip Format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
Phylip multiple alignment sequence format, less stringent than PHYLIP format."""))
        setattr(cls, "EDAM_format:3820",
            PermissibleValue(
                text="EDAM_format:3820",
                title="Relaxed PHYLIP Sequential",
                description="""It differs from Phylip sequential format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
Phylip multiple alignment sequence format, less stringent than PHYLIP sequential format (format_1998)."""))
        setattr(cls, "EDAM_format:3821",
            PermissibleValue(
                text="EDAM_format:3821",
                title="VisML",
                description="Default XML format of VisANT, containing all the network information."))
        setattr(cls, "EDAM_format:3822",
            PermissibleValue(
                text="EDAM_format:3822",
                title="GML",
                description="""GML (Graph Modeling Language) is a text file format supporting network data with a very easy syntax. It is used by Graphlet, Pajek, yEd, LEDA and NetworkX."""))
        setattr(cls, "EDAM_format:3823",
            PermissibleValue(
                text="EDAM_format:3823",
                title="FASTG",
                description="""FASTG is a format for faithfully representing genome assemblies in the face of allelic polymorphism and assembly uncertainty.
It is called FASTG, like FASTA, but the G stands for \"graph\"."""))
        setattr(cls, "EDAM_format:3824",
            PermissibleValue(
                text="EDAM_format:3824",
                title="NMR data format",
                description="""Data format for raw data from a nuclear magnetic resonance (NMR) spectroscopy experiment."""))
        setattr(cls, "EDAM_format:3825",
            PermissibleValue(
                text="EDAM_format:3825",
                title="nmrML",
                description="""nmrML is an MSI supported XML-based open access format for metabolomics NMR raw and processed spectral data. It is accompanies by an nmrCV (controlled vocabulary) to allow ontology-based annotations."""))
        setattr(cls, "EDAM_format:3826",
            PermissibleValue(
                text="EDAM_format:3826",
                title="proBAM",
                description=""". proBAM is an adaptation of BAM (format_2572), which was extended to meet specific requirements entailed by proteomics data."""))
        setattr(cls, "EDAM_format:3827",
            PermissibleValue(
                text="EDAM_format:3827",
                title="proBED",
                description=""". proBED is an adaptation of BED (format_3003), which was extended to meet specific requirements entailed by proteomics data."""))
        setattr(cls, "EDAM_format:3828",
            PermissibleValue(
                text="EDAM_format:3828",
                title="Raw microarray data format",
                description="Data format for raw microarray data."))
        setattr(cls, "EDAM_format:3829",
            PermissibleValue(
                text="EDAM_format:3829",
                title="GPR",
                description="""GenePix Results (GPR) text file format developed by Axon Instruments that is used to save GenePix Results data."""))
        setattr(cls, "EDAM_format:3830",
            PermissibleValue(
                text="EDAM_format:3830",
                title="ARB",
                description="Binary format used by the ARB software suite."))
        setattr(cls, "EDAM_format:3832",
            PermissibleValue(
                text="EDAM_format:3832",
                title="consensusXML",
                description="OpenMS format for grouping features in one map or across several maps."))
        setattr(cls, "EDAM_format:3833",
            PermissibleValue(
                text="EDAM_format:3833",
                title="featureXML",
                description="OpenMS format for quantitation results (LC/MS features)."))
        setattr(cls, "EDAM_format:3834",
            PermissibleValue(
                text="EDAM_format:3834",
                title="mzData",
                description="""Now deprecated data format of the HUPO Proteomics Standards Initiative. Replaced by mzML (format_3244)."""))
        setattr(cls, "EDAM_format:3835",
            PermissibleValue(
                text="EDAM_format:3835",
                title="TIDE TXT",
                description="Format supported by the Tide tool for identifying peptides from tandem mass spectra."))
        setattr(cls, "EDAM_format:3836",
            PermissibleValue(
                text="EDAM_format:3836",
                title="BLAST XML v2 results format",
                description="XML format as produced by the NCBI Blast package v2."))
        setattr(cls, "EDAM_format:3838",
            PermissibleValue(
                text="EDAM_format:3838",
                title="pptx",
                description="Microsoft Powerpoint format."))
        setattr(cls, "EDAM_format:3839",
            PermissibleValue(
                text="EDAM_format:3839",
                title="ibd",
                description="""ibd is a data format for mass spectrometry imaging data.
imzML data is recorded in 2 files: '.imzXML' (http://edamontology.org/format_3682) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (this concept) is a binary file containing the mass spectra."""))
        setattr(cls, "EDAM_format:3841",
            PermissibleValue(
                text="EDAM_format:3841",
                title="NLP format",
                description="Data format used in Natural Language Processing."))
        setattr(cls, "EDAM_format:3843",
            PermissibleValue(
                text="EDAM_format:3843",
                title="BEAST",
                description="""XML input file format for BEAST Software (Bayesian Evolutionary Analysis Sampling Trees)."""))
        setattr(cls, "EDAM_format:3844",
            PermissibleValue(
                text="EDAM_format:3844",
                title="Chado-XML",
                description="Chado-XML format is a direct mapping of the Chado relational schema into XML."))
        setattr(cls, "EDAM_format:3845",
            PermissibleValue(
                text="EDAM_format:3845",
                title="HSAML",
                description="""An alignment format generated by PRANK/PRANKSTER consisting of four elements: newick, nodes, selection and model."""))
        setattr(cls, "EDAM_format:3846",
            PermissibleValue(
                text="EDAM_format:3846",
                title="InterProScan XML",
                description="Output xml file from the InterProScan sequence analysis application."))
        setattr(cls, "EDAM_format:3847",
            PermissibleValue(
                text="EDAM_format:3847",
                title="KGML",
                description="""The KEGG Markup Language (KGML) is an exchange format of the KEGG pathway maps, which is converted from internally used KGML+ (KGML+SVG) format."""))
        setattr(cls, "EDAM_format:3848",
            PermissibleValue(
                text="EDAM_format:3848",
                title="PubMed XML",
                description="XML format for collected entries from bibliographic databases MEDLINE and PubMed."))
        setattr(cls, "EDAM_format:3849",
            PermissibleValue(
                text="EDAM_format:3849",
                title="MSAML",
                description="A set of XML compliant markup components for describing multiple sequence alignments."))
        setattr(cls, "EDAM_format:3850",
            PermissibleValue(
                text="EDAM_format:3850",
                title="OrthoXML",
                description="""OrthoXML is designed broadly to allow the storage and comparison of orthology data from any ortholog database. It establishes a structure for describing orthology relationships while still allowing flexibility for database-specific information to be encapsulated in the same format."""))
        setattr(cls, "EDAM_format:3851",
            PermissibleValue(
                text="EDAM_format:3851",
                title="PSDML",
                description="""Tree structure of Protein Sequence Database Markup Language generated using Matra software."""))
        setattr(cls, "EDAM_format:3852",
            PermissibleValue(
                text="EDAM_format:3852",
                title="SeqXML",
                description="""SeqXML is an XML Schema to describe biological sequences, developed by the Stockholm Bioinformatics Centre."""))
        setattr(cls, "EDAM_format:3853",
            PermissibleValue(
                text="EDAM_format:3853",
                title="UniParc XML",
                description="XML format for the UniParc database."))
        setattr(cls, "EDAM_format:3854",
            PermissibleValue(
                text="EDAM_format:3854",
                title="UniRef XML",
                description="XML format for the UniRef reference clusters."))
        setattr(cls, "EDAM_format:3857",
            PermissibleValue(
                text="EDAM_format:3857",
                title="CWL",
                description="""Common Workflow Language (CWL) format for description of command-line tools and workflows."""))
        setattr(cls, "EDAM_format:3858",
            PermissibleValue(
                text="EDAM_format:3858",
                title="Waters RAW",
                description="""Proprietary file format for mass spectrometry data from Waters.
Proprietary format for which documentation is not available, but used by multiple tools."""))
        setattr(cls, "EDAM_format:3859",
            PermissibleValue(
                text="EDAM_format:3859",
                title="JCAMP-DX",
                description="""A standardized file format for data exchange in mass spectrometry, initially developed for infrared spectrometry.
JCAMP-DX is an ASCII based format and therefore not very compact even though it includes standards for file compression."""))
        setattr(cls, "EDAM_format:3862",
            PermissibleValue(
                text="EDAM_format:3862",
                title="NLP annotation format",
                description="An NLP format used for annotated textual documents."))
        setattr(cls, "EDAM_format:3863",
            PermissibleValue(
                text="EDAM_format:3863",
                title="NLP corpus format",
                description="NLP format used by a specific type of corpus (collection of texts)."))
        setattr(cls, "EDAM_format:3864",
            PermissibleValue(
                text="EDAM_format:3864",
                title="mirGFF3",
                description="""mirGFF3 is a common format for microRNA data resulting from small-RNA RNA-Seq workflows.
mirGFF3 is a specialisation of GFF3; produced by small-RNA-Seq analysis workflows, usable and convertible with the miRTop API (https://mirtop.readthedocs.io/en/latest/), and consumable by tools for downstream analysis."""))
        setattr(cls, "EDAM_format:3865",
            PermissibleValue(
                text="EDAM_format:3865",
                title="RNA annotation format",
                description="""A \"placeholder\" concept for formats of annotated RNA data, including e.g. microRNA and RNA-Seq data."""))
        setattr(cls, "EDAM_format:3866",
            PermissibleValue(
                text="EDAM_format:3866",
                title="Trajectory format",
                description="""File format to store trajectory information for a 3D structure .
Formats differ on what they are able to store (coordinates, velocities, topologies) and how they are storing it (raw, compressed, textual, binary)."""))
        setattr(cls, "EDAM_format:3867",
            PermissibleValue(
                text="EDAM_format:3867",
                title="Trajectory format (binary)",
                description="Binary file format to store trajectory information for a 3D structure ."))
        setattr(cls, "EDAM_format:3868",
            PermissibleValue(
                text="EDAM_format:3868",
                title="Trajectory format (text)",
                description="Textual file format to store trajectory information for a 3D structure ."))
        setattr(cls, "EDAM_format:3873",
            PermissibleValue(
                text="EDAM_format:3873",
                title="HDF",
                description="""HDF is currently supported by many commercial and non-commercial software platforms such as Java, MATLAB/Scilab, Octave, Python and R.
HDF is the name of a set of file formats and libraries designed to store and organize large amounts of numerical data, originally developed at the National Center for Supercomputing Applications at the University of Illinois."""))
        setattr(cls, "EDAM_format:3874",
            PermissibleValue(
                text="EDAM_format:3874",
                title="PCAzip",
                description="""PCAZip format is a binary compressed file to store atom coordinates based on Essential Dynamics (ED) and Principal Component Analysis (PCA).
The compression is made projecting the Cartesian snapshots collected along the trajectory into an orthogonal space defined by the most relevant eigenvectors obtained by diagonalization of the covariance matrix (PCA). In the compression/decompression process, part of the original information is lost, depending on the final number of eigenvectors chosen. However, with a reasonable choice of the set of eigenvectors the compression typically reduces the trajectory file to less than one tenth of their original size with very acceptable loss of information. Compression with PCAZip can only be applied to unsolvated structures."""))
        setattr(cls, "EDAM_format:3875",
            PermissibleValue(
                text="EDAM_format:3875",
                title="XTC",
                description="""Portable binary format for trajectories produced by GROMACS package.
XTC uses the External Data Representation (xdr) routines for writing and reading data which were created for the Unix Network File System (NFS). XTC files use a reduced precision (lossy) algorithm which works multiplying the coordinates by a scaling factor (typically 1000), so converting them to pm (GROMACS standard distance unit is nm). This allows an integer rounding of the values. Several other tricks are performed, such as making use of atom proximity information: atoms close in sequence are usually close in space (e.g. water molecules). That makes XTC format the most efficient in terms of disk usage, in most cases reducing by a factor of 2 the size of any other binary trajectory format."""))
        setattr(cls, "EDAM_format:3876",
            PermissibleValue(
                text="EDAM_format:3876",
                title="TNG",
                description="""Fully architecture-independent format, regarding both endianness and the ability to mix single/double precision trajectories and I/O libraries. Self-sufficient, it should not require any other files for reading, and all the data should be contained in a single file for easy transport. Temporal compression of data, improving the compression rate of the previous XTC format. Possibility to store meta-data with information about the simulation. Direct access to a particular frame. Efficient parallel I/O.
Trajectory Next Generation (TNG) is a format for storage of molecular simulation data. It is designed and implemented by the GROMACS development group, and it is called to be the substitute of the XTC format."""))
        setattr(cls, "EDAM_format:3877",
            PermissibleValue(
                text="EDAM_format:3877",
                title="XYZ",
                description="""The XYZ chemical file format is widely supported by many programs, although many slightly different XYZ file formats coexist (Tinker XYZ, UniChem XYZ, etc.). Basic information stored for each atom in the system are x, y and z coordinates and atom element/atomic number.
XYZ files are structured in this way: First line contains the number of atoms in the file. Second line contains a title, comment, or filename. Remaining lines contain atom information. Each line starts with the element symbol, followed by x, y and z coordinates in angstroms separated by whitespace. Multiple molecules or frames can be contained within one file, so it supports trajectory storage. XYZ files can be directly represented by a molecular viewer, as they contain all the basic information needed to build the 3D model."""))
        setattr(cls, "EDAM_format:3878",
            PermissibleValue(
                text="EDAM_format:3878",
                title="mdcrd",
                description="""AMBER trajectory (also called mdcrd), with 10 coordinates per line and format F8.3 (fixed point notation with field width 8 and 3 decimal places)."""))
        setattr(cls, "EDAM_format:3879",
            PermissibleValue(
                text="EDAM_format:3879",
                title="Topology format",
                description="""Format of topology files; containing the static information of a structure molecular system that is needed for a molecular simulation.
Many different file formats exist describing structural molecular topology. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS top, CHARMM psf, AMBER prmtop)."""))
        setattr(cls, "EDAM_format:3880",
            PermissibleValue(
                text="EDAM_format:3880",
                title="GROMACS top",
                description="""GROMACS MD package top textual files define an entire structure system topology, either directly, or by including itp files.
There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package."""))
        setattr(cls, "EDAM_format:3881",
            PermissibleValue(
                text="EDAM_format:3881",
                title="AMBER top",
                description="""AMBER Prmtop file (version 7) is a structure topology text file divided in several sections designed to be parsed easily using simple Fortran code. Each section contains particular topology information, such as atom name, charge, mass, angles, dihedrals, etc.
It can be modified manually, but as the size of the system increases, the hand-editing becomes increasingly complex. AMBER Parameter-Topology file format is used extensively by the AMBER software suite and is referred to as the Prmtop file for short.
version 7 is written to distinguish it from old versions of AMBER Prmtop. Similarly to HDF5, it is a completely different format, according to AMBER group: a drastic change to the file format occurred with the 2004 release of Amber 7 (http://ambermd.org/prmtop.pdf)"""))
        setattr(cls, "EDAM_format:3882",
            PermissibleValue(
                text="EDAM_format:3882",
                title="PSF",
                description="""The high similarity in the functional form of the two potential energy functions used by AMBER and CHARMM force-fields gives rise to the possible use of one force-field within the other MD engine. Therefore, the conversion of PSF files to AMBER Prmtop format is possible with the use of AMBER chamber (CHARMM - AMBER) program.
X-Plor Protein Structure Files (PSF) are structure topology files used by NAMD and CHARMM molecular simulations programs. PSF files contain six main sections of interest: atoms, bonds, angles, dihedrals, improper dihedrals (force terms used to maintain planarity) and cross-terms."""))
        setattr(cls, "EDAM_format:3883",
            PermissibleValue(
                text="EDAM_format:3883",
                title="GROMACS itp",
                description="""GROMACS itp files (include topology) contain structure topology information, and are typically included in GROMACS topology files (GROMACS top). Itp files are used to define individual (or multiple) components of a topology as a separate file. This is particularly useful if there is a molecule that is used frequently, and also reduces the size of the system topology file, splitting it in different parts.
GROMACS itp files are used also to define position restrictions on the molecule, or to define the force field parameters for a particular ligand."""))
        setattr(cls, "EDAM_format:3884",
            PermissibleValue(
                text="EDAM_format:3884",
                title="FF parameter format",
                description="""Format of force field parameter files, which store the set of parameters (charges, masses, radii, bond lengths, bond dihedrals, etc.) that are essential for the proper description and simulation of a molecular system.
Many different file formats exist describing force field parameters. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS itp, CHARMM rtf, AMBER off / frcmod)."""))
        setattr(cls, "EDAM_format:3885",
            PermissibleValue(
                text="EDAM_format:3885",
                title="BinPos",
                description="""It is basically a translation of the ASCII atom coordinate format to binary code. The only additional information stored is a magic number that identifies the BinPos format and the number of atoms per snapshot. The remainder is the chain of coordinates binary encoded. A drawback of this format is its architecture dependency. Integers and floats codification depends on the architecture, thus it needs to be converted if working in different platforms (little endian, big endian).
Scripps Research Institute BinPos format is a binary formatted file to store atom coordinates."""))
        setattr(cls, "EDAM_format:3886",
            PermissibleValue(
                text="EDAM_format:3886",
                title="RST",
                description="""AMBER coordinate/restart file with 6 coordinates per line and decimal format F12.7 (fixed point notation with field width 12 and 7 decimal places)."""))
        setattr(cls, "EDAM_format:3887",
            PermissibleValue(
                text="EDAM_format:3887",
                title="CHARMM rtf",
                description="""Format of CHARMM Residue Topology Files (RTF), which define groups by including the atoms, the properties of the group, and bond and charge information.
There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package."""))
        setattr(cls, "EDAM_format:3888",
            PermissibleValue(
                text="EDAM_format:3888",
                title="AMBER frcmod",
                description="""AMBER frcmod (Force field Modification) is a file format to store any modification to the standard force field needed for a particular molecule to be properly represented in the simulation."""))
        setattr(cls, "EDAM_format:3889",
            PermissibleValue(
                text="EDAM_format:3889",
                title="AMBER off",
                description="""AMBER Object File Format library files (OFF library files) store residue libraries (forcefield residue parameters)."""))
        setattr(cls, "EDAM_format:3906",
            PermissibleValue(
                text="EDAM_format:3906",
                title="NMReDATA",
                description="""MReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or \"NMReDATA\") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc.
NMReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or \"NMReDATA\") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc. Find more in the paper at https://doi.org/10.1002/mrc.4527."""))
        setattr(cls, "EDAM_format:3909",
            PermissibleValue(
                text="EDAM_format:3909",
                title="BpForms",
                description="""BpForms is a string format for concretely representing the primary structures of biopolymers, including DNA, RNA, and proteins that include non-canonical nucleic and amino acids. See https://www.bpforms.org for more information."""))
        setattr(cls, "EDAM_format:3910",
            PermissibleValue(
                text="EDAM_format:3910",
                title="trr",
                description="""Format of trr files that contain the trajectory of a simulation experiment used by GROMACS.
The first 4 bytes of any trr file containing 1993. See https://github.com/galaxyproject/galaxy/pull/6597/files#diff-409951594551183dbf886e24de6cb129R760"""))
        setattr(cls, "EDAM_format:3911",
            PermissibleValue(
                text="EDAM_format:3911",
                title="msh",
                description="""Mash sketch is a format for sequence / sequence checksum information. To make a sketch, each k-mer in a sequence is hashed, which creates a pseudo-random identifier. By sorting these hashes, a small subset from the top of the sorted list can represent the entire sequence."""))
        setattr(cls, "EDAM_format:3913",
            PermissibleValue(
                text="EDAM_format:3913",
                title="Loom",
                description="""The Loom file format is based on HDF5, a standard for storing large numerical datasets. The Loom format is designed to efficiently hold large omics datasets. Typically, such data takes the form of a large matrix of numbers, along with metadata for the rows and columns."""))
        setattr(cls, "EDAM_format:3915",
            PermissibleValue(
                text="EDAM_format:3915",
                title="Zarr",
                description="""The Zarr format is an implementation of chunked, compressed, N-dimensional arrays for storing data."""))
        setattr(cls, "EDAM_format:3916",
            PermissibleValue(
                text="EDAM_format:3916",
                title="MTX",
                description="""The Matrix Market matrix (MTX) format stores numerical or pattern matrices in a dense (array format) or sparse (coordinate format) representation."""))
        setattr(cls, "EDAM_format:3951",
            PermissibleValue(
                text="EDAM_format:3951",
                title="BcForms",
                description="""BcForms is a format for abstractly describing the molecular structure (atoms and bonds) of macromolecular complexes as a collection of subunits and crosslinks. Each subunit can be described with BpForms (http://edamontology.org/format_3909) or SMILES (http://edamontology.org/data_2301). BcForms uses an ontology of crosslinks to abstract the chemical details of crosslinks from the descriptions of complexes (see https://bpforms.org/crosslink.html).
BcForms is related to http://edamontology.org/format_3909. (BcForms uses BpForms to describe subunits which are DNA, RNA, or protein polymers.) However, that format isn't the parent of BcForms. BcForms is similarly related to SMILES (http://edamontology.org/data_2301)."""))
        setattr(cls, "EDAM_format:3956",
            PermissibleValue(
                text="EDAM_format:3956",
                title="N-Quads",
                description="""N-Quads is a line-based, plain text format for encoding an RDF dataset. It includes information about the graph each triple belongs to.
N-Quads should not be confused with N-Triples which does not contain graph information."""))
        setattr(cls, "EDAM_format:3969",
            PermissibleValue(
                text="EDAM_format:3969",
                title="Vega",
                description="""Vega is a visualization grammar, a declarative language for creating, saving, and sharing interactive visualization designs. With Vega, you can describe the visual appearance and interactive behavior of a visualization in a JSON format, and generate web-based views using Canvas or SVG."""))
        setattr(cls, "EDAM_format:3970",
            PermissibleValue(
                text="EDAM_format:3970",
                title="Vega-lite",
                description="""Vega-Lite is a high-level grammar of interactive graphics. It provides a concise JSON syntax for rapidly generating visualizations to support analysis. Vega-Lite specifications can be compiled to Vega specifications."""))
        setattr(cls, "EDAM_format:3971",
            PermissibleValue(
                text="EDAM_format:3971",
                title="NeuroML",
                description="A model description language for computational neuroscience."))
        setattr(cls, "EDAM_format:3972",
            PermissibleValue(
                text="EDAM_format:3972",
                title="BNGL",
                description="""BioNetGen is a format for the specification and simulation of rule-based models of biochemical systems, including signal transduction, metabolic, and genetic regulatory networks."""))
        setattr(cls, "EDAM_format:3973",
            PermissibleValue(
                text="EDAM_format:3973",
                title="Docker image",
                description="""A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. An image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel."""))
        setattr(cls, "EDAM_format:3975",
            PermissibleValue(
                text="EDAM_format:3975",
                title="GFA 1",
                description="""Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology."""))
        setattr(cls, "EDAM_format:3976",
            PermissibleValue(
                text="EDAM_format:3976",
                title="GFA 2",
                description="""Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology. GFA2 is an update of GFA1 which is not compatible with GFA1."""))
        setattr(cls, "EDAM_format:3977",
            PermissibleValue(
                text="EDAM_format:3977",
                title="ObjTables",
                description="""ObjTables is a toolkit for creating re-usable datasets that are both human and machine-readable, combining the ease of spreadsheets (e.g., Excel workbooks) with the rigor of schemas (classes, their attributes, the type of each attribute, and the possible relationships between instances of classes). ObjTables consists of a format for describing schemas for spreadsheets, numerous data types for science, a syntax for indicating the class and attribute represented by each table and column in a workbook, and software for using schemas to rigorously validate, merge, split, compare, and revision datasets."""))
        setattr(cls, "EDAM_format:3978",
            PermissibleValue(
                text="EDAM_format:3978",
                title="CONTIG",
                description="""The CONTIG format used for output of the SOAPdenovo alignment program. It contains contig sequences generated without using mate pair information."""))
        setattr(cls, "EDAM_format:3979",
            PermissibleValue(
                text="EDAM_format:3979",
                title="WEGO",
                description="""WEGO native format used by the Web Gene Ontology Annotation Plot application.   Tab-delimited format with gene names and others GO IDs (columns) with one annotation record per line."""))
        setattr(cls, "EDAM_format:3980",
            PermissibleValue(
                text="EDAM_format:3980",
                title="RPKM",
                description="""For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
Tab-delimited format for gene expression levels table, calculated as Reads Per Kilobase per Million (RPKM) mapped reads."""))
        setattr(cls, "EDAM_format:3981",
            PermissibleValue(
                text="EDAM_format:3981",
                title="TAR format",
                description="""For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
TAR archive file format generated by the Unix-based utility tar."""))
        setattr(cls, "EDAM_format:3982",
            PermissibleValue(
                text="EDAM_format:3982",
                title="CHAIN",
                description="""The CHAIN format describes a pairwise alignment that allow gaps in both sequences simultaneously and is used by the UCSC Genome Browser."""))
        setattr(cls, "EDAM_format:3983",
            PermissibleValue(
                text="EDAM_format:3983",
                title="NET",
                description="""The NET file format is used to describe the data that underlie the net alignment annotations in the UCSC Genome Browser."""))
        setattr(cls, "EDAM_format:3984",
            PermissibleValue(
                text="EDAM_format:3984",
                title="QMAP",
                description="Format of QMAP files generated for methylation data from an internal BGI pipeline."))
        setattr(cls, "EDAM_format:3985",
            PermissibleValue(
                text="EDAM_format:3985",
                title="gxformat2",
                description="An emerging format for high-level Galaxy workflow description."))
        setattr(cls, "EDAM_format:3986",
            PermissibleValue(
                text="EDAM_format:3986",
                title="WMV",
                description="""The proprietary native video format of various Microsoft programs such as Windows Media Player."""))
        setattr(cls, "EDAM_format:3987",
            PermissibleValue(
                text="EDAM_format:3987",
                title="ZIP format",
                description="""A ZIP file may contain one or more files or directories that may have been compressed.
ZIP is an archive file format that supports lossless data compression."""))
        setattr(cls, "EDAM_format:3988",
            PermissibleValue(
                text="EDAM_format:3988",
                title="LSM",
                description="""LSM files are the default data export for the Zeiss LSM series confocal microscopes (e.g. LSM 510, LSM 710). In addition to the image data, LSM files contain most imaging settings.
Zeiss' proprietary image format based on TIFF."""))
        setattr(cls, "EDAM_format:3989",
            PermissibleValue(
                text="EDAM_format:3989",
                title="GZIP format",
                description="GNU zip compressed file format common to Unix-based operating systems."))
        setattr(cls, "EDAM_format:3990",
            PermissibleValue(
                text="EDAM_format:3990",
                title="AVI",
                description="""Audio Video Interleaved (AVI) format is a multimedia container format for AVI files, that allows synchronous audio-with-video playback."""))
        setattr(cls, "EDAM_format:3991",
            PermissibleValue(
                text="EDAM_format:3991",
                title="TrackDB",
                description="A declaration file format for UCSC browsers track dataset display charateristics."))
        setattr(cls, "EDAM_format:3992",
            PermissibleValue(
                text="EDAM_format:3992",
                title="CIGAR format",
                description="""Compact Idiosyncratic Gapped Alignment Report format is a compressed (run-length encoded) pairwise alignment format. It is useful for representing long (e.g. genomic) pairwise alignments."""))
        setattr(cls, "EDAM_format:3993",
            PermissibleValue(
                text="EDAM_format:3993",
                title="Stereolithography format",
                description="""STL is a file format native to the stereolithography CAD software created by 3D Systems. The format is used to save and share surface-rendered 3D images and also for 3D printing."""))
        setattr(cls, "EDAM_format:3994",
            PermissibleValue(
                text="EDAM_format:3994",
                title="U3D",
                description="""U3D (Universal 3D) is a compressed file format and data structure for 3D computer graphics. It contains 3D model information such as triangle meshes, lighting, shading, motion data, lines and points with color and structure."""))
        setattr(cls, "EDAM_format:3995",
            PermissibleValue(
                text="EDAM_format:3995",
                title="Texture file format",
                description="""Bitmap image format used for storing textures.
Texture files can create the appearance of different surfaces and can be applied to both 2D and 3D objects. Note the file extension .tex is also used for LaTex documents which are a completely different format and they are NOT interchangeable."""))
        setattr(cls, "EDAM_format:3996",
            PermissibleValue(
                text="EDAM_format:3996",
                title="Python script",
                description="""Format for scripts writtenin Python - a widely used high-level programming language for general-purpose programming."""))
        setattr(cls, "EDAM_format:3997",
            PermissibleValue(
                text="EDAM_format:3997",
                title="MPEG-4",
                description="A digital multimedia container format most commonly used to store video and audio."))
        setattr(cls, "EDAM_format:3998",
            PermissibleValue(
                text="EDAM_format:3998",
                title="Perl script",
                description="""Format for scripts written in Perl - a family of high-level, general-purpose, interpreted, dynamic programming languages."""))
        setattr(cls, "EDAM_format:3999",
            PermissibleValue(
                text="EDAM_format:3999",
                title="R script",
                description="""Format for scripts written in the R language - an open source programming language and software environment for statistical computing and graphics that is supported by the R Foundation for Statistical Computing."""))
        setattr(cls, "EDAM_format:4000",
            PermissibleValue(
                text="EDAM_format:4000",
                title="R markdown",
                description="A file format for making dynamic documents (R Markdown scripts) with the R language."))
        setattr(cls, "EDAM_format:4002",
            PermissibleValue(
                text="EDAM_format:4002",
                title="pickle",
                description="""Format used by Python pickle module for serializing and de-serializing a Python object structure."""))
        setattr(cls, "EDAM_format:4003",
            PermissibleValue(
                text="EDAM_format:4003",
                title="NumPy format",
                description="""The standard binary file format used by NumPy - a fundamental package for scientific computing with Python - for persisting a single arbitrary NumPy array on disk. The format stores all of the shape and dtype information necessary to reconstruct the array correctly."""))
        setattr(cls, "EDAM_format:4004",
            PermissibleValue(
                text="EDAM_format:4004",
                title="SimTools repertoire file format",
                description="""Format of repertoire (archive) files that can be read by SimToolbox (a MATLAB toolbox for structured illumination fluorescence microscopy) or alternatively extracted with zip file archiver software."""))
        setattr(cls, "EDAM_format:4005",
            PermissibleValue(
                text="EDAM_format:4005",
                title="Configuration file format",
                description="""A configuration file used by various programs to store settings that are specific to their respective software."""))
        setattr(cls, "EDAM_format:4006",
            PermissibleValue(
                text="EDAM_format:4006",
                title="Zstandard format",
                description="Format used by the Zstandard real-time compression algorithm."))
        setattr(cls, "EDAM_format:4007",
            PermissibleValue(
                text="EDAM_format:4007",
                title="MATLAB script",
                description="The file format for MATLAB scripts or functions."))
        setattr(cls, "EDAM_format:4015",
            PermissibleValue(
                text="EDAM_format:4015",
                title="PEtab",
                description="A data format for specifying parameter estimation problems in systems biology."))
        setattr(cls, "EDAM_format:4018",
            PermissibleValue(
                text="EDAM_format:4018",
                title="gVCF",
                description="""Genomic Variant Call Format (gVCF) is a version of VCF that includes not only the positions that are variant when compared to a reference genome, but also the non-variant positions as ranges, including metrics of confidence that the positions in the range are actually non-variant e.g. minimum read-depth and genotype quality."""))
        setattr(cls, "EDAM_format:4023",
            PermissibleValue(
                text="EDAM_format:4023",
                title="cml",
                description="""Chemical Markup Language (CML) is an XML-based format for encoding detailed information about a wide range of chemical concepts."""))
        setattr(cls, "EDAM_format:4024",
            PermissibleValue(
                text="EDAM_format:4024",
                title="cif",
                description="""Crystallographic Information File (CIF) is a data exchange standard file format for Crystallographic Information and related Structural Science data."""))
        setattr(cls, "EDAM_format:4025",
            PermissibleValue(
                text="EDAM_format:4025",
                title="BioSimulators format for the specifications of biosimulation tools",
                description="""Format for describing the capabilities of a biosimulation tool including the modeling frameworks, simulation algorithms, and modeling formats that it supports, as well as metadata such as a list of the interfaces, programming languages, and operating systems supported by the tool; a link to download the tool; a list of the authors of the tool; and the license to the tool."""))
        setattr(cls, "EDAM_format:4026",
            PermissibleValue(
                text="EDAM_format:4026",
                title="BioSimulators standard for command-line interfaces for biosimulation tools",
                description="""Outlines the syntax and semantics of the input and output arguments for command-line interfaces for biosimulation tools."""))
        setattr(cls, "EDAM_format:4035",
            PermissibleValue(
                text="EDAM_format:4035",
                title="PQR",
                description="""Data format derived from the standard PDB format, which enables user to incorporate parameters for charge and radius to the existing PDB data file."""))
        setattr(cls, "EDAM_format:4036",
            PermissibleValue(
                text="EDAM_format:4036",
                title="PDBQT",
                description="""Data format used in AutoDock 4 for storing atomic coordinates, partial atomic charges and AutoDock atom types for both receptors and ligands."""))
        setattr(cls, "EDAM_format:4039",
            PermissibleValue(
                text="EDAM_format:4039",
                title="MSP",
                description="""MSP is a data format for mass spectrometry data.
NIST Text file format for storing MS∕MS spectra (m∕z and intensity of mass peaks) along with additional annotations for each spectrum. A single MSP file can thus contain single or multiple spectra. This format is frequently used to share spectra libraries."""))
        setattr(cls, "EDAM_format:4041",
            PermissibleValue(
                text="EDAM_format:4041",
                title="maDMP",
                description="A standard for DMPs developed by the Research Data Alliance"))
        setattr(cls, "EDAM_format:4048",
            PermissibleValue(
                text="EDAM_format:4048",
                title="Nextflow",
                description="""Nextflow is a workflow system for creating scalable, portable, and reproducible workflows.
This term covers all versions of Nextflow language specifications."""))
        setattr(cls, "EDAM_format:4049",
            PermissibleValue(
                text="EDAM_format:4049",
                title="Snakemake",
                description="""The Snakemake workflow management system is a tool to create reproducible and scalable data analyses."""))
        setattr(cls, "EDAM_format:4050",
            PermissibleValue(
                text="EDAM_format:4050",
                title="SDRF",
                description="Sample and Data Relationship File for a proteomics experiment."))
        setattr(cls, "EDAM_format:4058",
            PermissibleValue(
                text="EDAM_format:4058",
                title="mzTab-M",
                description="""The reference implementation of mzTab-M in Java is https://github.com/lifs-tools/jmzTab-m.
mzTab-M is a light-weight, tab-delimited format for mass spectrometry-based chemical profiling data, including metabolomics.
mzTab-M is alternatively named mzTab 2.0, but in 2025 there is a draft version 2.1 of mzTab-M.
mzTab-M is not compatible with mzTab (also named mzTab 1.0, for proteomics, http://edamontology.org/format_3681). Note: the repository, website, and file extension are the same for both formats."""))
        setattr(cls, "EDAM_format:4059",
            PermissibleValue(
                text="EDAM_format:4059",
                title="mzTab-L",
                description="""mzTab-L is a light-weight, tab-delimited format for mass spectrometry-based lipidomics data. It is a compatible version of mzTab-M, with additional rules and information standard (reporting guidelines)."""))

class EnumEDAMDataTypes(EnumDefinitionImpl):
    """
    Data types from the EDAM ontology.
    """
    _defn = EnumDefinition(
        name="EnumEDAMDataTypes",
        description="Data types from the EDAM ontology.",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "EDAM_data:0582",
            PermissibleValue(
                text="EDAM_data:0582",
                title="Ontology",
                description="""An ontology of biological or bioinformatics concepts and relations, a controlled vocabulary, structured glossary etc."""))
        setattr(cls, "EDAM_data:0842",
            PermissibleValue(
                text="EDAM_data:0842",
                title="Identifier",
                description="""A text token, number or something else which identifies an entity, but which may not be persistent (stable) or unique (the same identifier may identify multiple things)."""))
        setattr(cls, "EDAM_data:0844",
            PermissibleValue(
                text="EDAM_data:0844",
                title="Molecular mass",
                description="Mass of a molecule."))
        setattr(cls, "EDAM_data:0845",
            PermissibleValue(
                text="EDAM_data:0845",
                title="Molecular charge",
                description="Net charge of a molecule."))
        setattr(cls, "EDAM_data:0846",
            PermissibleValue(
                text="EDAM_data:0846",
                title="Chemical formula",
                description="A specification of a chemical structure."))
        setattr(cls, "EDAM_data:0847",
            PermissibleValue(
                text="EDAM_data:0847",
                title="QSAR descriptor",
                description="""A QSAR quantitative descriptor (name-value pair) of chemical structure.
QSAR descriptors have numeric values that quantify chemical information encoded in a symbolic representation of a molecule. They are used in quantitative structure activity relationship (QSAR) applications. Many subtypes of individual descriptors (not included in EDAM) cover various types of protein properties."""))
        setattr(cls, "EDAM_data:0849",
            PermissibleValue(
                text="EDAM_data:0849",
                title="Sequence record",
                description="A molecular sequence and associated metadata."))
        setattr(cls, "EDAM_data:0850",
            PermissibleValue(
                text="EDAM_data:0850",
                title="Sequence set",
                description="""A collection of one or typically multiple molecular sequences (which can include derived data or metadata) that do not (typically) correspond to molecular sequence database records or entries and which (typically) are derived from some analytical method.
An example is an alignment reference; one or a set of reference molecular sequences, structures, or profiles used for alignment of genomic, transcriptomic, or proteomic experimental data.
This concept may be used for arbitrary sequence sets and associated data arising from processing."""))
        setattr(cls, "EDAM_data:0856",
            PermissibleValue(
                text="EDAM_data:0856",
                title="Sequence feature source",
                description="""How the annotation of a sequence feature (for example in EMBL or Swiss-Prot) was derived.
This might be the name and version of a software tool, the name of a database, or 'curated' to indicate a manual annotation (made by a human)."""))
        setattr(cls, "EDAM_data:0857",
            PermissibleValue(
                text="EDAM_data:0857",
                title="Sequence search results",
                description="""A report of sequence hits and associated data from searching a database of sequences (for example a BLAST search). This will typically include a list of scores (often with statistical evaluation) and a set of alignments for the hits.
The score list includes the alignment score, percentage of the query sequence matched, length of the database sequence entry in this alignment, identifier of the database sequence entry, excerpt of the database sequence entry description etc."""))
        setattr(cls, "EDAM_data:0858",
            PermissibleValue(
                text="EDAM_data:0858",
                title="Sequence signature matches",
                description="""A \"profile-profile alignment\" is an alignment of two sequence profiles, each profile typically representing a sequence alignment.
A \"sequence-profile alignment\" is an alignment of one or more molecular sequence(s) to one or more sequence profile(s) (each profile typically representing a sequence alignment).
Report on the location of matches (\"hits\") between sequences, sequence profiles, motifs (conserved or functional patterns) and other types of sequence signatures.
This includes reports of hits from a search of a protein secondary or domain database. Data associated with the search or alignment might also be included, e.g. ranked list of best-scoring sequences, a graphical representation of scores etc."""))
        setattr(cls, "EDAM_data:0860",
            PermissibleValue(
                text="EDAM_data:0860",
                title="Sequence signature data",
                description="""Sequence signature data concerns specific or conserved pattern in molecular sequences and the classifiers used for their identification, including sequence motifs, profiles or other diagnostic element.
This can include metadata about a motif or sequence profile such as its name, length, technical details about the profile construction, and so on."""))
        setattr(cls, "EDAM_data:0862",
            PermissibleValue(
                text="EDAM_data:0862",
                title="Dotplot",
                description="""A dotplot of sequence similarities identified from word-matching or character comparison."""))
        setattr(cls, "EDAM_data:0863",
            PermissibleValue(
                text="EDAM_data:0863",
                title="Sequence alignment",
                description="Alignment of multiple molecular sequences."))
        setattr(cls, "EDAM_data:0865",
            PermissibleValue(
                text="EDAM_data:0865",
                title="Sequence similarity score",
                description="A value representing molecular sequence similarity."))
        setattr(cls, "EDAM_data:0867",
            PermissibleValue(
                text="EDAM_data:0867",
                title="Sequence alignment report",
                description="""An informative report of molecular sequence alignment-derived data or metadata.
Use this for any computer-generated reports on sequence alignments, and for general information (metadata) on a sequence alignment, such as a description, sequence identifiers and alignment score."""))
        setattr(cls, "EDAM_data:0870",
            PermissibleValue(
                text="EDAM_data:0870",
                title="Sequence distance matrix",
                description="""A matrix of estimated evolutionary distance between molecular sequences, such as is suitable for phylogenetic tree calculation.
Methods might perform character compatibility analysis or identify patterns of similarity in an alignment or data matrix."""))
        setattr(cls, "EDAM_data:0871",
            PermissibleValue(
                text="EDAM_data:0871",
                title="Phylogenetic character data",
                description="""As defined, this concept would also include molecular sequences, microsatellites, polymorphisms (RAPDs, RFLPs, or AFLPs), restriction sites and fragments
Basic character data from which a phylogenetic tree may be generated."""))
        setattr(cls, "EDAM_data:0872",
            PermissibleValue(
                text="EDAM_data:0872",
                title="Phylogenetic tree",
                description="""A phylogenetic tree is usually constructed from a set of sequences from which an alignment (or data matrix) is calculated. See also 'Phylogenetic tree image'.
The raw data (not just an image) from which a phylogenetic tree is directly generated or plotted, such as topology, lengths (in time or in expected amounts of variance) and a confidence interval for each length."""))
        setattr(cls, "EDAM_data:0874",
            PermissibleValue(
                text="EDAM_data:0874",
                title="Comparison matrix",
                description="""Matrix of integer or floating point numbers for amino acid or nucleotide sequence comparison.
The comparison matrix might include matrix name, optional comment, height and width (or size) of matrix, an index row/column (of characters) and data rows/columns (of integers or floats)."""))
        setattr(cls, "EDAM_data:0878",
            PermissibleValue(
                text="EDAM_data:0878",
                title="Protein secondary structure alignment",
                description="Alignment of the (1D representations of) secondary structure of two or more proteins."))
        setattr(cls, "EDAM_data:0880",
            PermissibleValue(
                text="EDAM_data:0880",
                title="RNA secondary structure",
                description="""An informative report of secondary structure (predicted or real) of an RNA molecule.
This includes thermodynamically stable or evolutionarily conserved structures such as knots, pseudoknots etc."""))
        setattr(cls, "EDAM_data:0881",
            PermissibleValue(
                text="EDAM_data:0881",
                title="RNA secondary structure alignment",
                description="""Alignment of the (1D representations of) secondary structure of two or more RNA molecules."""))
        setattr(cls, "EDAM_data:0883",
            PermissibleValue(
                text="EDAM_data:0883",
                title="Structure",
                description="""3D coordinate and associated data for a macromolecular tertiary (3D) structure or part of a structure.
The coordinate data may be predicted or real."""))
        setattr(cls, "EDAM_data:0886",
            PermissibleValue(
                text="EDAM_data:0886",
                title="Structure alignment",
                description="""A tertiary structure alignment will include the untransformed coordinates of one macromolecule, followed by the second (or subsequent) structure(s) with all the coordinates transformed (by rotation / translation) to give a superposition.
Alignment (superimposition) of molecular tertiary (3D) structures."""))
        setattr(cls, "EDAM_data:0887",
            PermissibleValue(
                text="EDAM_data:0887",
                title="Structure alignment report",
                description="""An informative report of molecular tertiary structure alignment-derived data.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:0888",
            PermissibleValue(
                text="EDAM_data:0888",
                title="Structure similarity score",
                description="""A value representing molecular structure similarity, measured from structure alignment or some other type of structure comparison."""))
        setattr(cls, "EDAM_data:0889",
            PermissibleValue(
                text="EDAM_data:0889",
                title="Structural profile",
                description="""Some type of structural (3D) profile or template (representing a structure or structure alignment)."""))
        setattr(cls, "EDAM_data:0890",
            PermissibleValue(
                text="EDAM_data:0890",
                title="Structural (3D) profile alignment",
                description="""A 3D profile-3D profile alignment (each profile representing structures or a structure alignment)."""))
        setattr(cls, "EDAM_data:0892",
            PermissibleValue(
                text="EDAM_data:0892",
                title="Protein sequence-structure scoring matrix",
                description="Matrix of values used for scoring sequence-structure compatibility."))
        setattr(cls, "EDAM_data:0893",
            PermissibleValue(
                text="EDAM_data:0893",
                title="Sequence-structure alignment",
                description="""An alignment of molecular sequence to structure (from threading sequence(s) through 3D structure or representation of structure(s))."""))
        setattr(cls, "EDAM_data:0896",
            PermissibleValue(
                text="EDAM_data:0896",
                title="Protein report",
                description="""An informative human-readable report about one or more specific protein molecules or protein structural domains, derived from analysis of primary (sequence or structural) data."""))
        setattr(cls, "EDAM_data:0897",
            PermissibleValue(
                text="EDAM_data:0897",
                title="Protein property",
                description="""A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a protein molecule or model.
This is a broad data type and is used a placeholder for other, more specific types. Data may be based on analysis of nucleic acid sequence or structural data, for example reports on the surface properties (shape, hydropathy, electrostatic patches etc) of a protein structure, protein flexibility or motion, and protein architecture (spatial arrangement of secondary structure)."""))
        setattr(cls, "EDAM_data:0905",
            PermissibleValue(
                text="EDAM_data:0905",
                title="Protein interaction raw data",
                description="""Protein-protein interaction data from for example yeast two-hybrid analysis, protein microarrays, immunoaffinity chromatography followed by mass spectrometry, phage display etc.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation."""))
        setattr(cls, "EDAM_data:0906",
            PermissibleValue(
                text="EDAM_data:0906",
                title="Protein interaction data",
                description="""Data concerning the interactions (predicted or known) within or between a protein, structural domain or part of a protein. This includes intra- and inter-residue contacts and distances, as well as interactions with other proteins and non-protein entities such as nucleic acid, metal atoms, water, ions etc."""))
        setattr(cls, "EDAM_data:0907",
            PermissibleValue(
                text="EDAM_data:0907",
                title="Protein family report",
                description="""An informative report on a specific protein family or other classification or group of protein sequences or structures."""))
        setattr(cls, "EDAM_data:0909",
            PermissibleValue(
                text="EDAM_data:0909",
                title="Vmax",
                description="""The maximum initial velocity or rate of a reaction. It is the limiting velocity as substrate concentrations get very large."""))
        setattr(cls, "EDAM_data:0910",
            PermissibleValue(
                text="EDAM_data:0910",
                title="Km",
                description="""Km is the concentration (usually in Molar units) of substrate that leads to half-maximal velocity of an enzyme-catalysed reaction."""))
        setattr(cls, "EDAM_data:0912",
            PermissibleValue(
                text="EDAM_data:0912",
                title="Nucleic acid property",
                description="""A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a nucleic acid molecule.
Nucleic acid structural properties stiffness, curvature, twist/roll data or other conformational parameters or properties.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:0914",
            PermissibleValue(
                text="EDAM_data:0914",
                title="Codon usage data",
                description="""Data derived from analysis of codon usage (typically a codon usage table) of DNA sequences.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:0916",
            PermissibleValue(
                text="EDAM_data:0916",
                title="Gene report",
                description="""A report on predicted or actual gene structure, regions which make an RNA product and features such as promoters, coding regions, splice sites etc.
This includes any report on a particular locus or gene. This might include the gene name, description, summary and so on. It can include details about the function of a gene, such as its encoded protein or a functional classification of the gene sequence along according to the encoded protein(s)."""))
        setattr(cls, "EDAM_data:0919",
            PermissibleValue(
                text="EDAM_data:0919",
                title="Chromosome report",
                description="""A human-readable collection of information about a specific chromosome.
This includes basic information. e.g. chromosome number, length, karyotype features, chromosome sequence etc."""))
        setattr(cls, "EDAM_data:0920",
            PermissibleValue(
                text="EDAM_data:0920",
                title="Genotype/phenotype report",
                description="""A human-readable collection of information about the set of genes (or allelic forms) present in an individual, organism or cell and associated with a specific physical characteristic, or a report concerning an organisms traits and phenotypes."""))
        setattr(cls, "EDAM_data:0924",
            PermissibleValue(
                text="EDAM_data:0924",
                title="Sequence trace",
                description="""Fluorescence trace data generated by an automated DNA sequencer, which can be interpreted as a molecular sequence (reads), given associated sequencing metadata such as base-call quality scores.
This is the raw data produced by a DNA sequencing machine."""))
        setattr(cls, "EDAM_data:0925",
            PermissibleValue(
                text="EDAM_data:0925",
                title="Sequence assembly",
                description="""An assembly of fragments of a (typically genomic) DNA sequence.
Typically, an assembly is a collection of contigs (for example ESTs and genomic DNA fragments) that are ordered, aligned and merged. Annotation of the assembled sequence might be included."""))
        setattr(cls, "EDAM_data:0926",
            PermissibleValue(
                text="EDAM_data:0926",
                title="RH scores",
                description="""Radiation Hybrid (RH) scores are used in Radiation Hybrid mapping.
Radiation hybrid scores (RH) scores for one or more markers."""))
        setattr(cls, "EDAM_data:0927",
            PermissibleValue(
                text="EDAM_data:0927",
                title="Genetic linkage report",
                description="""A human-readable collection of information about the linkage of alleles.
This includes linkage disequilibrium; the non-random association of alleles or polymorphisms at two or more loci (not necessarily on the same chromosome)."""))
        setattr(cls, "EDAM_data:0928",
            PermissibleValue(
                text="EDAM_data:0928",
                title="Gene expression profile",
                description="""Data quantifying the level of expression of (typically) multiple genes, derived for example from microarray experiments."""))
        setattr(cls, "EDAM_data:0937",
            PermissibleValue(
                text="EDAM_data:0937",
                title="Electron density map",
                description="X-ray crystallography data."))
        setattr(cls, "EDAM_data:0938",
            PermissibleValue(
                text="EDAM_data:0938",
                title="Raw NMR data",
                description="Nuclear magnetic resonance (NMR) raw data, typically for a protein."))
        setattr(cls, "EDAM_data:0939",
            PermissibleValue(
                text="EDAM_data:0939",
                title="CD spectra",
                description="""Protein secondary structure from protein coordinate or circular dichroism (CD) spectroscopic data."""))
        setattr(cls, "EDAM_data:0940",
            PermissibleValue(
                text="EDAM_data:0940",
                title="Volume map",
                description="Volume map data from electron microscopy."))
        setattr(cls, "EDAM_data:0942",
            PermissibleValue(
                text="EDAM_data:0942",
                title="2D PAGE image",
                description="Two-dimensional gel electrophoresis image."))
        setattr(cls, "EDAM_data:0943",
            PermissibleValue(
                text="EDAM_data:0943",
                title="Mass spectrum",
                description="Spectra from mass spectrometry."))
        setattr(cls, "EDAM_data:0944",
            PermissibleValue(
                text="EDAM_data:0944",
                title="Peptide mass fingerprint",
                description="""A molecular weight standard fingerprint is standard protonated molecular masses e.g. from trypsin (modified porcine trypsin, Promega) and keratin peptides.
A set of peptide masses (peptide mass fingerprint) from mass spectrometry."""))
        setattr(cls, "EDAM_data:0945",
            PermissibleValue(
                text="EDAM_data:0945",
                title="Peptide identification",
                description="""Protein or peptide identifications with evidence supporting the identifications, for example from comparing a peptide mass fingerprint (from mass spectrometry) to a sequence database, or the set of typical spectra one obtains when running a protein through a mass spectrometer."""))
        setattr(cls, "EDAM_data:0949",
            PermissibleValue(
                text="EDAM_data:0949",
                title="Workflow metadata",
                description="""Basic information, annotation or documentation concerning a workflow (but not the workflow itself)."""))
        setattr(cls, "EDAM_data:0950",
            PermissibleValue(
                text="EDAM_data:0950",
                title="Mathematical model",
                description="A biological model represented in mathematical terms."))
        setattr(cls, "EDAM_data:0951",
            PermissibleValue(
                text="EDAM_data:0951",
                title="Statistical estimate score",
                description="""A value representing estimated statistical significance of some observed data; typically sequence database hits."""))
        setattr(cls, "EDAM_data:0954",
            PermissibleValue(
                text="EDAM_data:0954",
                title="Database cross-mapping",
                description="""A mapping of the accession numbers (or other database identifier) of entries between (typically) two biological or biomedical databases.
The cross-mapping is typically a table where each row is an accession number and each column is a database being cross-referenced. The cells give the accession number or identifier of the corresponding entry in a database. If a cell in the table is not filled then no mapping could be found for the database. Additional information might be given on version, date etc."""))
        setattr(cls, "EDAM_data:0955",
            PermissibleValue(
                text="EDAM_data:0955",
                title="Data index",
                description="An index of data of biological relevance."))
        setattr(cls, "EDAM_data:0956",
            PermissibleValue(
                text="EDAM_data:0956",
                title="Data index report",
                description="""A human-readable collection of information concerning an analysis of an index of biological data."""))
        setattr(cls, "EDAM_data:0957",
            PermissibleValue(
                text="EDAM_data:0957",
                title="Database metadata",
                description="""Basic information on bioinformatics database(s) or other data sources such as name, type, description, URL etc."""))
        setattr(cls, "EDAM_data:0958",
            PermissibleValue(
                text="EDAM_data:0958",
                title="Tool metadata",
                description="""Basic information about one or more bioinformatics applications or packages, such as name, type, description, or other documentation."""))
        setattr(cls, "EDAM_data:0960",
            PermissibleValue(
                text="EDAM_data:0960",
                title="User metadata",
                description="""Textual metadata on a software author or end-user, for example a person or other software."""))
        setattr(cls, "EDAM_data:0962",
            PermissibleValue(
                text="EDAM_data:0962",
                title="Small molecule report",
                description="A human-readable collection of information about a specific chemical compound."))
        setattr(cls, "EDAM_data:0963",
            PermissibleValue(
                text="EDAM_data:0963",
                title="Cell line report",
                description="""A human-readable collection of information about a particular strain of organism cell line including plants, virus, fungi and bacteria. The data typically includes strain number, organism type, growth conditions, source and so on."""))
        setattr(cls, "EDAM_data:0966",
            PermissibleValue(
                text="EDAM_data:0966",
                title="Ontology term",
                description="A term (name) from an ontology."))
        setattr(cls, "EDAM_data:0967",
            PermissibleValue(
                text="EDAM_data:0967",
                title="Ontology concept data",
                description="Data concerning or derived from a concept from a biological ontology."))
        setattr(cls, "EDAM_data:0968",
            PermissibleValue(
                text="EDAM_data:0968",
                title="Keyword",
                description="""Boolean operators (AND, OR and NOT) and wildcard characters may be allowed.
Keyword(s) or phrase(s) used (typically) for text-searching purposes."""))
        setattr(cls, "EDAM_data:0970",
            PermissibleValue(
                text="EDAM_data:0970",
                title="Citation",
                description="""A bibliographic reference might include information such as authors, title, journal name, date and (possibly) a link to the abstract or full-text of the article if available.
Bibliographic data that uniquely identifies a scientific article, book or other published material."""))
        setattr(cls, "EDAM_data:0971",
            PermissibleValue(
                text="EDAM_data:0971",
                title="Article",
                description="A scientific text, typically a full text article from a scientific journal."))
        setattr(cls, "EDAM_data:0972",
            PermissibleValue(
                text="EDAM_data:0972",
                title="Text mining report",
                description="""A human-readable collection of information resulting from text mining.
A text mining abstract will typically include an annotated a list of words or sentences extracted from one or more scientific articles."""))
        setattr(cls, "EDAM_data:0976",
            PermissibleValue(
                text="EDAM_data:0976",
                title="Identifier (by type of entity)",
                description="""An identifier that identifies a particular type of data.
This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'."""))
        setattr(cls, "EDAM_data:0977",
            PermissibleValue(
                text="EDAM_data:0977",
                title="Tool identifier",
                description="An identifier of a bioinformatics tool, e.g. an application or web service."))
        setattr(cls, "EDAM_data:0982",
            PermissibleValue(
                text="EDAM_data:0982",
                title="Molecule identifier",
                description="Name or other identifier of a molecule."))
        setattr(cls, "EDAM_data:0983",
            PermissibleValue(
                text="EDAM_data:0983",
                title="Atom ID",
                description="Identifier (e.g. character symbol) of a specific atom."))
        setattr(cls, "EDAM_data:0984",
            PermissibleValue(
                text="EDAM_data:0984",
                title="Molecule name",
                description="Name of a specific molecule."))
        setattr(cls, "EDAM_data:0987",
            PermissibleValue(
                text="EDAM_data:0987",
                title="Chromosome name",
                description="Name of a chromosome."))
        setattr(cls, "EDAM_data:0988",
            PermissibleValue(
                text="EDAM_data:0988",
                title="Peptide identifier",
                description="Identifier of a peptide chain."))
        setattr(cls, "EDAM_data:0989",
            PermissibleValue(
                text="EDAM_data:0989",
                title="Protein identifier",
                description="Identifier of a protein."))
        setattr(cls, "EDAM_data:0990",
            PermissibleValue(
                text="EDAM_data:0990",
                title="Compound name",
                description="Unique name of a chemical compound."))
        setattr(cls, "EDAM_data:0991",
            PermissibleValue(
                text="EDAM_data:0991",
                title="Chemical registry number",
                description="Unique registry number of a chemical compound."))
        setattr(cls, "EDAM_data:0993",
            PermissibleValue(
                text="EDAM_data:0993",
                title="Drug identifier",
                description="Identifier of a drug."))
        setattr(cls, "EDAM_data:0994",
            PermissibleValue(
                text="EDAM_data:0994",
                title="Amino acid identifier",
                description="Identifier of an amino acid."))
        setattr(cls, "EDAM_data:0995",
            PermissibleValue(
                text="EDAM_data:0995",
                title="Nucleotide identifier",
                description="Name or other identifier of a nucleotide."))
        setattr(cls, "EDAM_data:0996",
            PermissibleValue(
                text="EDAM_data:0996",
                title="Monosaccharide identifier",
                description="Identifier of a monosaccharide."))
        setattr(cls, "EDAM_data:0997",
            PermissibleValue(
                text="EDAM_data:0997",
                title="Chemical name (ChEBI)",
                description="""This is the recommended chemical name for use for example in database annotation.
Unique name from Chemical Entities of Biological Interest (ChEBI) of a chemical compound."""))
        setattr(cls, "EDAM_data:0998",
            PermissibleValue(
                text="EDAM_data:0998",
                title="Chemical name (IUPAC)",
                description="IUPAC recommended name of a chemical compound."))
        setattr(cls, "EDAM_data:0999",
            PermissibleValue(
                text="EDAM_data:0999",
                title="Chemical name (INN)",
                description="""International Non-proprietary Name (INN or 'generic name') of a chemical compound, assigned by the World Health Organisation (WHO)."""))
        setattr(cls, "EDAM_data:1000",
            PermissibleValue(
                text="EDAM_data:1000",
                title="Chemical name (brand)",
                description="Brand name of a chemical compound."))
        setattr(cls, "EDAM_data:1001",
            PermissibleValue(
                text="EDAM_data:1001",
                title="Chemical name (synonymous)",
                description="Synonymous name of a chemical compound."))
        setattr(cls, "EDAM_data:1002",
            PermissibleValue(
                text="EDAM_data:1002",
                title="CAS number",
                description="""CAS registry number of a chemical compound; a unique numerical identifier of chemicals in the scientific literature, as assigned by the Chemical Abstracts Service."""))
        setattr(cls, "EDAM_data:1003",
            PermissibleValue(
                text="EDAM_data:1003",
                title="Chemical registry number (Beilstein)",
                description="Beilstein registry number of a chemical compound."))
        setattr(cls, "EDAM_data:1004",
            PermissibleValue(
                text="EDAM_data:1004",
                title="Chemical registry number (Gmelin)",
                description="Gmelin registry number of a chemical compound."))
        setattr(cls, "EDAM_data:1005",
            PermissibleValue(
                text="EDAM_data:1005",
                title="HET group name",
                description="3-letter code word for a ligand (HET group) from a PDB file, for example ATP."))
        setattr(cls, "EDAM_data:1006",
            PermissibleValue(
                text="EDAM_data:1006",
                title="Amino acid name",
                description="String of one or more ASCII characters representing an amino acid."))
        setattr(cls, "EDAM_data:1007",
            PermissibleValue(
                text="EDAM_data:1007",
                title="Nucleotide code",
                description="String of one or more ASCII characters representing a nucleotide."))
        setattr(cls, "EDAM_data:1008",
            PermissibleValue(
                text="EDAM_data:1008",
                title="Polypeptide chain ID",
                description="""Identifier of a polypeptide chain from a protein.
This is typically a character (for the chain) appended to a PDB identifier, e.g. 1cukA"""))
        setattr(cls, "EDAM_data:1009",
            PermissibleValue(
                text="EDAM_data:1009",
                title="Protein name",
                description="Name of a protein."))
        setattr(cls, "EDAM_data:1010",
            PermissibleValue(
                text="EDAM_data:1010",
                title="Enzyme identifier",
                description="Name or other identifier of an enzyme or record from a database of enzymes."))
        setattr(cls, "EDAM_data:1011",
            PermissibleValue(
                text="EDAM_data:1011",
                title="EC number",
                description="An Enzyme Commission (EC) number of an enzyme."))
        setattr(cls, "EDAM_data:1012",
            PermissibleValue(
                text="EDAM_data:1012",
                title="Enzyme name",
                description="Name of an enzyme."))
        setattr(cls, "EDAM_data:1013",
            PermissibleValue(
                text="EDAM_data:1013",
                title="Restriction enzyme name",
                description="Name of a restriction enzyme."))
        setattr(cls, "EDAM_data:1015",
            PermissibleValue(
                text="EDAM_data:1015",
                title="Sequence feature ID",
                description="""A unique identifier of molecular sequence feature, for example an ID of a feature that is unique within the scope of the GFF file."""))
        setattr(cls, "EDAM_data:1016",
            PermissibleValue(
                text="EDAM_data:1016",
                title="Sequence position",
                description="""A position of one or more points (base or residue) in a sequence, or part of such a specification."""))
        setattr(cls, "EDAM_data:1017",
            PermissibleValue(
                text="EDAM_data:1017",
                title="Sequence range",
                description="Specification of range(s) of sequence positions."))
        setattr(cls, "EDAM_data:1020",
            PermissibleValue(
                text="EDAM_data:1020",
                title="Sequence feature key",
                description="""A feature key indicates the biological nature of the feature or information about changes to or versions of the sequence.
The type of a sequence feature, typically a term or accession from the Sequence Ontology, for example an EMBL or Swiss-Prot sequence feature key."""))
        setattr(cls, "EDAM_data:1021",
            PermissibleValue(
                text="EDAM_data:1021",
                title="Sequence feature qualifier",
                description="""Feature qualifiers hold information about a feature beyond that provided by the feature key and location.
Typically one of the EMBL or Swiss-Prot feature qualifiers."""))
        setattr(cls, "EDAM_data:1022",
            PermissibleValue(
                text="EDAM_data:1022",
                title="Sequence feature label",
                description="""A feature label identifies a feature of a sequence database entry. When used with the database name and the entry's primary accession number, it is a unique identifier of that feature.
A name of a sequence feature, e.g. the name of a feature to be displayed to an end-user. Typically an EMBL or Swiss-Prot feature label."""))
        setattr(cls, "EDAM_data:1023",
            PermissibleValue(
                text="EDAM_data:1023",
                title="EMBOSS Uniform Feature Object",
                description="""The name of a sequence feature-containing entity adhering to the standard feature naming scheme used by all EMBOSS applications."""))
        setattr(cls, "EDAM_data:1025",
            PermissibleValue(
                text="EDAM_data:1025",
                title="Gene identifier",
                description="""An identifier of a gene, such as a name/symbol or a unique identifier of a gene in a database."""))
        setattr(cls, "EDAM_data:1026",
            PermissibleValue(
                text="EDAM_data:1026",
                title="Gene symbol",
                description="""The short name of a gene; a single word that does not contain white space characters. It is typically derived from the gene name."""))
        setattr(cls, "EDAM_data:1027",
            PermissibleValue(
                text="EDAM_data:1027",
                title="Gene ID (NCBI)",
                description="An NCBI unique identifier of a gene."))
        setattr(cls, "EDAM_data:1031",
            PermissibleValue(
                text="EDAM_data:1031",
                title="Gene ID (CGD)",
                description="Identifier of a gene or feature from the CGD database."))
        setattr(cls, "EDAM_data:1032",
            PermissibleValue(
                text="EDAM_data:1032",
                title="Gene ID (DictyBase)",
                description="Identifier of a gene from DictyBase."))
        setattr(cls, "EDAM_data:1033",
            PermissibleValue(
                text="EDAM_data:1033",
                title="Ensembl gene ID",
                description="Unique identifier for a gene (or other feature) from the Ensembl database."))
        setattr(cls, "EDAM_data:1034",
            PermissibleValue(
                text="EDAM_data:1034",
                title="Gene ID (SGD)",
                description="Identifier of an entry from the SGD database."))
        setattr(cls, "EDAM_data:1035",
            PermissibleValue(
                text="EDAM_data:1035",
                title="Gene ID (GeneDB)",
                description="Identifier of a gene from the GeneDB database."))
        setattr(cls, "EDAM_data:1036",
            PermissibleValue(
                text="EDAM_data:1036",
                title="TIGR identifier",
                description="Identifier of an entry from the TIGR database."))
        setattr(cls, "EDAM_data:1037",
            PermissibleValue(
                text="EDAM_data:1037",
                title="TAIR accession (gene)",
                description="Identifier of an gene from the TAIR database."))
        setattr(cls, "EDAM_data:1038",
            PermissibleValue(
                text="EDAM_data:1038",
                title="Protein domain ID",
                description="""Identifier of a protein structural domain.
This is typically a character or string concatenated with a PDB identifier and a chain identifier."""))
        setattr(cls, "EDAM_data:1039",
            PermissibleValue(
                text="EDAM_data:1039",
                title="SCOP domain identifier",
                description="Identifier of a protein domain (or other node) from the SCOP database."))
        setattr(cls, "EDAM_data:1040",
            PermissibleValue(
                text="EDAM_data:1040",
                title="CATH domain ID",
                description="Identifier of a protein domain from CATH."))
        setattr(cls, "EDAM_data:1041",
            PermissibleValue(
                text="EDAM_data:1041",
                title="SCOP concise classification string (sccs)",
                description="""A SCOP concise classification string (sccs) is a compact representation of a SCOP domain classification.
An scss includes the class (alphabetical), fold, superfamily and family (all numerical) to which a given domain belongs."""))
        setattr(cls, "EDAM_data:1042",
            PermissibleValue(
                text="EDAM_data:1042",
                title="SCOP sunid",
                description="""A sunid uniquely identifies an entry in the SCOP hierarchy, including leaves (the SCOP domains) and higher level nodes including entries corresponding to the protein level.
Unique identifier (number) of an entry in the SCOP hierarchy, for example 33229."""))
        setattr(cls, "EDAM_data:1043",
            PermissibleValue(
                text="EDAM_data:1043",
                title="CATH node ID",
                description="A code number identifying a node from the CATH database."))
        setattr(cls, "EDAM_data:1044",
            PermissibleValue(
                text="EDAM_data:1044",
                title="Kingdom name",
                description="The name of a biological kingdom (Bacteria, Archaea, or Eukaryotes)."))
        setattr(cls, "EDAM_data:1045",
            PermissibleValue(
                text="EDAM_data:1045",
                title="Species name",
                description="The name of a species (typically a taxonomic group) of organism."))
        setattr(cls, "EDAM_data:1046",
            PermissibleValue(
                text="EDAM_data:1046",
                title="Strain name",
                description="The name of a strain of an organism variant, typically a plant, virus or bacterium."))
        setattr(cls, "EDAM_data:1047",
            PermissibleValue(
                text="EDAM_data:1047",
                title="URI",
                description="A string of characters that name or otherwise identify a resource on the Internet."))
        setattr(cls, "EDAM_data:1048",
            PermissibleValue(
                text="EDAM_data:1048",
                title="Database ID",
                description="An identifier of a biological or bioinformatics database."))
        setattr(cls, "EDAM_data:1049",
            PermissibleValue(
                text="EDAM_data:1049",
                title="Directory name",
                description="The name of a directory."))
        setattr(cls, "EDAM_data:1050",
            PermissibleValue(
                text="EDAM_data:1050",
                title="File name",
                description="The name (or part of a name) of a file (of any type)."))
        setattr(cls, "EDAM_data:1051",
            PermissibleValue(
                text="EDAM_data:1051",
                title="Ontology name",
                description="Name of an ontology of biological or bioinformatics concepts and relations."))
        setattr(cls, "EDAM_data:1052",
            PermissibleValue(
                text="EDAM_data:1052",
                title="URL",
                description="A Uniform Resource Locator (URL)."))
        setattr(cls, "EDAM_data:1053",
            PermissibleValue(
                text="EDAM_data:1053",
                title="URN",
                description="A Uniform Resource Name (URN)."))
        setattr(cls, "EDAM_data:1055",
            PermissibleValue(
                text="EDAM_data:1055",
                title="LSID",
                description="""A Life Science Identifier (LSID) - a unique identifier of some data.
LSIDs provide a standard way to locate and describe data. An LSID is represented as a Uniform Resource Name (URN) with the following format: URN:LSID:<Authority>:<Namespace>:<ObjectID>[:<Version>]"""))
        setattr(cls, "EDAM_data:1056",
            PermissibleValue(
                text="EDAM_data:1056",
                title="Database name",
                description="The name of a biological or bioinformatics database."))
        setattr(cls, "EDAM_data:1058",
            PermissibleValue(
                text="EDAM_data:1058",
                title="Enumerated file name",
                description="The name of a file (of any type) with restricted possible values."))
        setattr(cls, "EDAM_data:1059",
            PermissibleValue(
                text="EDAM_data:1059",
                title="File name extension",
                description="""A file extension is the characters appearing after the final '.' in the file name.
The extension of a file name."""))
        setattr(cls, "EDAM_data:1060",
            PermissibleValue(
                text="EDAM_data:1060",
                title="File base name",
                description="""A file base name is the file name stripped of its directory specification and extension.
The base name of a file."""))
        setattr(cls, "EDAM_data:1061",
            PermissibleValue(
                text="EDAM_data:1061",
                title="QSAR descriptor name",
                description="Name of a QSAR descriptor."))
        setattr(cls, "EDAM_data:1063",
            PermissibleValue(
                text="EDAM_data:1063",
                title="Sequence identifier",
                description="An identifier of molecular sequence(s) or entries from a molecular sequence database."))
        setattr(cls, "EDAM_data:1064",
            PermissibleValue(
                text="EDAM_data:1064",
                title="Sequence set ID",
                description="An identifier of a set of molecular sequence(s)."))
        setattr(cls, "EDAM_data:1066",
            PermissibleValue(
                text="EDAM_data:1066",
                title="Sequence alignment ID",
                description="""Identifier of a molecular sequence alignment, for example a record from an alignment database."""))
        setattr(cls, "EDAM_data:1068",
            PermissibleValue(
                text="EDAM_data:1068",
                title="Phylogenetic tree ID",
                description="Identifier of a phylogenetic tree for example from a phylogenetic tree database."))
        setattr(cls, "EDAM_data:1069",
            PermissibleValue(
                text="EDAM_data:1069",
                title="Comparison matrix identifier",
                description="An identifier of a comparison matrix."))
        setattr(cls, "EDAM_data:1070",
            PermissibleValue(
                text="EDAM_data:1070",
                title="Structure ID",
                description="""A unique and persistent identifier of a molecular tertiary structure, typically an entry from a structure database."""))
        setattr(cls, "EDAM_data:1071",
            PermissibleValue(
                text="EDAM_data:1071",
                title="Structural (3D) profile ID",
                description="""Identifier or name of a structural (3D) profile or template (representing a structure or structure alignment)."""))
        setattr(cls, "EDAM_data:1072",
            PermissibleValue(
                text="EDAM_data:1072",
                title="Structure alignment ID",
                description="Identifier of an entry from a database of tertiary structure alignments."))
        setattr(cls, "EDAM_data:1073",
            PermissibleValue(
                text="EDAM_data:1073",
                title="Amino acid index ID",
                description="Identifier of an index of amino acid physicochemical and biochemical property data."))
        setattr(cls, "EDAM_data:1074",
            PermissibleValue(
                text="EDAM_data:1074",
                title="Protein interaction ID",
                description="""Identifier of a report of protein interactions from a protein interaction database (typically)."""))
        setattr(cls, "EDAM_data:1075",
            PermissibleValue(
                text="EDAM_data:1075",
                title="Protein family identifier",
                description="Identifier of a protein family."))
        setattr(cls, "EDAM_data:1076",
            PermissibleValue(
                text="EDAM_data:1076",
                title="Codon usage table name",
                description="Unique name of a codon usage table."))
        setattr(cls, "EDAM_data:1077",
            PermissibleValue(
                text="EDAM_data:1077",
                title="Transcription factor identifier",
                description="Identifier of a transcription factor (or a TF binding site)."))
        setattr(cls, "EDAM_data:1078",
            PermissibleValue(
                text="EDAM_data:1078",
                title="Experiment annotation ID",
                description="Identifier of an entry from a database of microarray data."))
        setattr(cls, "EDAM_data:1079",
            PermissibleValue(
                text="EDAM_data:1079",
                title="Electron microscopy model ID",
                description="Identifier of an entry from a database of electron microscopy data."))
        setattr(cls, "EDAM_data:1080",
            PermissibleValue(
                text="EDAM_data:1080",
                title="Gene expression report ID",
                description="""Accession of a report of gene expression (e.g. a gene expression profile) from a database."""))
        setattr(cls, "EDAM_data:1081",
            PermissibleValue(
                text="EDAM_data:1081",
                title="Genotype and phenotype annotation ID",
                description="Identifier of an entry from a database of genotypes and phenotypes."))
        setattr(cls, "EDAM_data:1082",
            PermissibleValue(
                text="EDAM_data:1082",
                title="Pathway or network identifier",
                description="Identifier of an entry from a database of biological pathways or networks."))
        setattr(cls, "EDAM_data:1083",
            PermissibleValue(
                text="EDAM_data:1083",
                title="Workflow ID",
                description="""Identifier of a biological or biomedical workflow, typically from a database of workflows."""))
        setattr(cls, "EDAM_data:1084",
            PermissibleValue(
                text="EDAM_data:1084",
                title="Data resource definition ID",
                description="Identifier of a data type definition from some provider."))
        setattr(cls, "EDAM_data:1085",
            PermissibleValue(
                text="EDAM_data:1085",
                title="Biological model ID",
                description="Identifier of a mathematical model, typically an entry from a database."))
        setattr(cls, "EDAM_data:1086",
            PermissibleValue(
                text="EDAM_data:1086",
                title="Compound identifier",
                description="Identifier of an entry from a database of chemicals."))
        setattr(cls, "EDAM_data:1087",
            PermissibleValue(
                text="EDAM_data:1087",
                title="Ontology concept ID",
                description="""A unique (typically numerical) identifier of a concept in an ontology of biological or bioinformatics concepts and relations."""))
        setattr(cls, "EDAM_data:1088",
            PermissibleValue(
                text="EDAM_data:1088",
                title="Article ID",
                description="Unique identifier of a scientific article."))
        setattr(cls, "EDAM_data:1089",
            PermissibleValue(
                text="EDAM_data:1089",
                title="FlyBase ID",
                description="Identifier of an object from the FlyBase database."))
        setattr(cls, "EDAM_data:1091",
            PermissibleValue(
                text="EDAM_data:1091",
                title="WormBase name",
                description="Name of an object from the WormBase database, usually a human-readable name."))
        setattr(cls, "EDAM_data:1092",
            PermissibleValue(
                text="EDAM_data:1092",
                title="WormBase class",
                description="""A WormBase class describes the type of object such as 'sequence' or 'protein'.
Class of an object from the WormBase database."""))
        setattr(cls, "EDAM_data:1093",
            PermissibleValue(
                text="EDAM_data:1093",
                title="Sequence accession",
                description="A persistent, unique identifier of a molecular sequence database entry."))
        setattr(cls, "EDAM_data:1095",
            PermissibleValue(
                text="EDAM_data:1095",
                title="EMBOSS Uniform Sequence Address",
                description="""The name of a sequence-based entity adhering to the standard sequence naming scheme used by all EMBOSS applications."""))
        setattr(cls, "EDAM_data:1096",
            PermissibleValue(
                text="EDAM_data:1096",
                title="Sequence accession (protein)",
                description="Accession number of a protein sequence database entry."))
        setattr(cls, "EDAM_data:1097",
            PermissibleValue(
                text="EDAM_data:1097",
                title="Sequence accession (nucleic acid)",
                description="Accession number of a nucleotide sequence database entry."))
        setattr(cls, "EDAM_data:1098",
            PermissibleValue(
                text="EDAM_data:1098",
                title="RefSeq accession",
                description="Accession number of a RefSeq database entry."))
        setattr(cls, "EDAM_data:1100",
            PermissibleValue(
                text="EDAM_data:1100",
                title="PIR identifier",
                description="An identifier of PIR sequence database entry."))
        setattr(cls, "EDAM_data:1102",
            PermissibleValue(
                text="EDAM_data:1102",
                title="Gramene primary identifier",
                description="Primary identifier of a Gramene database entry."))
        setattr(cls, "EDAM_data:1103",
            PermissibleValue(
                text="EDAM_data:1103",
                title="EMBL/GenBank/DDBJ ID",
                description="Identifier of a (nucleic acid) entry from the EMBL/GenBank/DDBJ databases."))
        setattr(cls, "EDAM_data:1104",
            PermissibleValue(
                text="EDAM_data:1104",
                title="Sequence cluster ID (UniGene)",
                description="A unique identifier of an entry (gene cluster) from the NCBI UniGene database."))
        setattr(cls, "EDAM_data:1105",
            PermissibleValue(
                text="EDAM_data:1105",
                title="dbEST accession",
                description="Identifier of a dbEST database entry."))
        setattr(cls, "EDAM_data:1106",
            PermissibleValue(
                text="EDAM_data:1106",
                title="dbSNP ID",
                description="Identifier of a dbSNP database entry."))
        setattr(cls, "EDAM_data:1112",
            PermissibleValue(
                text="EDAM_data:1112",
                title="Sequence cluster ID",
                description="An identifier of a cluster of molecular sequence(s)."))
        setattr(cls, "EDAM_data:1113",
            PermissibleValue(
                text="EDAM_data:1113",
                title="Sequence cluster ID (COG)",
                description="Unique identifier of an entry from the COG database."))
        setattr(cls, "EDAM_data:1114",
            PermissibleValue(
                text="EDAM_data:1114",
                title="Sequence motif identifier",
                description="Identifier of a sequence motif, for example an entry from a motif database."))
        setattr(cls, "EDAM_data:1115",
            PermissibleValue(
                text="EDAM_data:1115",
                title="Sequence profile ID",
                description="""A sequence profile typically represents a sequence alignment.
Identifier of a sequence profile."""))
        setattr(cls, "EDAM_data:1116",
            PermissibleValue(
                text="EDAM_data:1116",
                title="ELM ID",
                description="Identifier of an entry from the ELMdb database of protein functional sites."))
        setattr(cls, "EDAM_data:1117",
            PermissibleValue(
                text="EDAM_data:1117",
                title="Prosite accession number",
                description="Accession number of an entry from the Prosite database."))
        setattr(cls, "EDAM_data:1118",
            PermissibleValue(
                text="EDAM_data:1118",
                title="HMMER hidden Markov model ID",
                description="Unique identifier or name of a HMMER hidden Markov model."))
        setattr(cls, "EDAM_data:1119",
            PermissibleValue(
                text="EDAM_data:1119",
                title="JASPAR profile ID",
                description="Unique identifier or name of a profile from the JASPAR database."))
        setattr(cls, "EDAM_data:1123",
            PermissibleValue(
                text="EDAM_data:1123",
                title="TreeBASE study accession number",
                description="Accession number of an entry from the TreeBASE database."))
        setattr(cls, "EDAM_data:1124",
            PermissibleValue(
                text="EDAM_data:1124",
                title="TreeFam accession number",
                description="Accession number of an entry from the TreeFam database."))
        setattr(cls, "EDAM_data:1126",
            PermissibleValue(
                text="EDAM_data:1126",
                title="Comparison matrix name",
                description="""See for example http://www.ebi.ac.uk/Tools/webservices/help/matrix.
Unique name or identifier of a comparison matrix."""))
        setattr(cls, "EDAM_data:1127",
            PermissibleValue(
                text="EDAM_data:1127",
                title="PDB ID",
                description="""A PDB identification code which consists of 4 characters, the first of which is a digit in the range 0 - 9; the remaining 3 are alphanumeric, and letters are upper case only. (source: https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1996.pdf)
An identifier of an entry from the PDB database."""))
        setattr(cls, "EDAM_data:1128",
            PermissibleValue(
                text="EDAM_data:1128",
                title="AAindex ID",
                description="Identifier of an entry from the AAindex database."))
        setattr(cls, "EDAM_data:1129",
            PermissibleValue(
                text="EDAM_data:1129",
                title="BIND accession number",
                description="Accession number of an entry from the BIND database."))
        setattr(cls, "EDAM_data:1130",
            PermissibleValue(
                text="EDAM_data:1130",
                title="IntAct accession number",
                description="Accession number of an entry from the IntAct database."))
        setattr(cls, "EDAM_data:1131",
            PermissibleValue(
                text="EDAM_data:1131",
                title="Protein family name",
                description="Name of a protein family."))
        setattr(cls, "EDAM_data:1132",
            PermissibleValue(
                text="EDAM_data:1132",
                title="InterPro entry name",
                description="""Name of an InterPro entry, usually indicating the type of protein matches for that entry."""))
        setattr(cls, "EDAM_data:1133",
            PermissibleValue(
                text="EDAM_data:1133",
                title="InterPro accession",
                description="""Every InterPro entry has a unique accession number to provide a persistent citation of database records.
Primary accession number of an InterPro entry."""))
        setattr(cls, "EDAM_data:1134",
            PermissibleValue(
                text="EDAM_data:1134",
                title="InterPro secondary accession",
                description="Secondary accession number of an InterPro entry."))
        setattr(cls, "EDAM_data:1135",
            PermissibleValue(
                text="EDAM_data:1135",
                title="Gene3D ID",
                description="Unique identifier of an entry from the Gene3D database."))
        setattr(cls, "EDAM_data:1136",
            PermissibleValue(
                text="EDAM_data:1136",
                title="PIRSF ID",
                description="Unique identifier of an entry from the PIRSF database."))
        setattr(cls, "EDAM_data:1137",
            PermissibleValue(
                text="EDAM_data:1137",
                title="PRINTS code",
                description="The unique identifier of an entry in the PRINTS database."))
        setattr(cls, "EDAM_data:1138",
            PermissibleValue(
                text="EDAM_data:1138",
                title="Pfam accession number",
                description="Accession number of a Pfam entry."))
        setattr(cls, "EDAM_data:1139",
            PermissibleValue(
                text="EDAM_data:1139",
                title="SMART accession number",
                description="Accession number of an entry from the SMART database."))
        setattr(cls, "EDAM_data:1140",
            PermissibleValue(
                text="EDAM_data:1140",
                title="Superfamily hidden Markov model number",
                description="Unique identifier (number) of a hidden Markov model from the Superfamily database."))
        setattr(cls, "EDAM_data:1141",
            PermissibleValue(
                text="EDAM_data:1141",
                title="TIGRFam ID",
                description="Accession number of an entry (family) from the TIGRFam database."))
        setattr(cls, "EDAM_data:1142",
            PermissibleValue(
                text="EDAM_data:1142",
                title="ProDom accession number",
                description="""A ProDom domain family accession number.
ProDom is a protein domain family database."""))
        setattr(cls, "EDAM_data:1143",
            PermissibleValue(
                text="EDAM_data:1143",
                title="TRANSFAC accession number",
                description="Identifier of an entry from the TRANSFAC database."))
        setattr(cls, "EDAM_data:1144",
            PermissibleValue(
                text="EDAM_data:1144",
                title="ArrayExpress accession number",
                description="Accession number of an entry from the ArrayExpress database."))
        setattr(cls, "EDAM_data:1145",
            PermissibleValue(
                text="EDAM_data:1145",
                title="PRIDE experiment accession number",
                description="PRIDE experiment accession number."))
        setattr(cls, "EDAM_data:1146",
            PermissibleValue(
                text="EDAM_data:1146",
                title="EMDB ID",
                description="Identifier of an entry from the EMDB electron microscopy database."))
        setattr(cls, "EDAM_data:1147",
            PermissibleValue(
                text="EDAM_data:1147",
                title="GEO accession number",
                description="Accession number of an entry from the GEO database."))
        setattr(cls, "EDAM_data:1148",
            PermissibleValue(
                text="EDAM_data:1148",
                title="GermOnline ID",
                description="Identifier of an entry from the GermOnline database."))
        setattr(cls, "EDAM_data:1149",
            PermissibleValue(
                text="EDAM_data:1149",
                title="EMAGE ID",
                description="Identifier of an entry from the EMAGE database."))
        setattr(cls, "EDAM_data:1150",
            PermissibleValue(
                text="EDAM_data:1150",
                title="Disease ID",
                description="Accession number of an entry from a database of disease."))
        setattr(cls, "EDAM_data:1151",
            PermissibleValue(
                text="EDAM_data:1151",
                title="HGVbase ID",
                description="Identifier of an entry from the HGVbase database."))
        setattr(cls, "EDAM_data:1153",
            PermissibleValue(
                text="EDAM_data:1153",
                title="OMIM ID",
                description="Identifier of an entry from the OMIM database."))
        setattr(cls, "EDAM_data:1154",
            PermissibleValue(
                text="EDAM_data:1154",
                title="KEGG object identifier",
                description="""Unique identifier of an object from one of the KEGG databases (excluding the GENES division)."""))
        setattr(cls, "EDAM_data:1155",
            PermissibleValue(
                text="EDAM_data:1155",
                title="Pathway ID (reactome)",
                description="Identifier of an entry from the Reactome database."))
        setattr(cls, "EDAM_data:1157",
            PermissibleValue(
                text="EDAM_data:1157",
                title="Pathway ID (BioCyc)",
                description="Identifier of an pathway from the BioCyc biological pathways database."))
        setattr(cls, "EDAM_data:1158",
            PermissibleValue(
                text="EDAM_data:1158",
                title="Pathway ID (INOH)",
                description="Identifier of an entry from the INOH database."))
        setattr(cls, "EDAM_data:1159",
            PermissibleValue(
                text="EDAM_data:1159",
                title="Pathway ID (PATIKA)",
                description="Identifier of an entry from the PATIKA database."))
        setattr(cls, "EDAM_data:1160",
            PermissibleValue(
                text="EDAM_data:1160",
                title="Pathway ID (CPDB)",
                description="""Identifier of an entry from the CPDB (ConsensusPathDB) biological pathways database, which is an identifier from an external database integrated into CPDB.
This concept refers to identifiers used by the databases collated in CPDB; CPDB identifiers are not independently defined."""))
        setattr(cls, "EDAM_data:1161",
            PermissibleValue(
                text="EDAM_data:1161",
                title="Pathway ID (Panther)",
                description="Identifier of a biological pathway from the Panther Pathways database."))
        setattr(cls, "EDAM_data:1162",
            PermissibleValue(
                text="EDAM_data:1162",
                title="MIRIAM identifier",
                description="""This is the identifier used internally by MIRIAM for a data type.
Unique identifier of a MIRIAM data resource."""))
        setattr(cls, "EDAM_data:1163",
            PermissibleValue(
                text="EDAM_data:1163",
                title="MIRIAM data type name",
                description="The name of a data type from the MIRIAM database."))
        setattr(cls, "EDAM_data:1164",
            PermissibleValue(
                text="EDAM_data:1164",
                title="MIRIAM URI",
                description="""A MIRIAM URI consists of the URI of the MIRIAM data type (PubMed, UniProt etc) followed by the identifier of an element of that data type, for example PMID for a publication or an accession number for a GO term.
The URI (URL or URN) of a data entity from the MIRIAM database."""))
        setattr(cls, "EDAM_data:1165",
            PermissibleValue(
                text="EDAM_data:1165",
                title="MIRIAM data type primary name",
                description="""The primary name of a MIRIAM data type is taken from a controlled vocabulary.
The primary name of a data type from the MIRIAM database."""))
        setattr(cls, "EDAM_data:1166",
            PermissibleValue(
                text="EDAM_data:1166",
                title="MIRIAM data type synonymous name",
                description="""A synonymous name for a MIRIAM data type taken from a controlled vocabulary.
A synonymous name of a data type from the MIRIAM database."""))
        setattr(cls, "EDAM_data:1167",
            PermissibleValue(
                text="EDAM_data:1167",
                title="Taverna workflow ID",
                description="Unique identifier of a Taverna workflow."))
        setattr(cls, "EDAM_data:1170",
            PermissibleValue(
                text="EDAM_data:1170",
                title="Biological model name",
                description="Name of a biological (mathematical) model."))
        setattr(cls, "EDAM_data:1171",
            PermissibleValue(
                text="EDAM_data:1171",
                title="BioModel ID",
                description="Unique identifier of an entry from the BioModel database."))
        setattr(cls, "EDAM_data:1172",
            PermissibleValue(
                text="EDAM_data:1172",
                title="PubChem CID",
                description="""Chemical structure specified in PubChem Compound Identification (CID), a non-zero integer identifier for a unique chemical structure."""))
        setattr(cls, "EDAM_data:1173",
            PermissibleValue(
                text="EDAM_data:1173",
                title="ChemSpider ID",
                description="Identifier of an entry from the ChemSpider database."))
        setattr(cls, "EDAM_data:1174",
            PermissibleValue(
                text="EDAM_data:1174",
                title="ChEBI ID",
                description="Identifier of an entry from the ChEBI database."))
        setattr(cls, "EDAM_data:1175",
            PermissibleValue(
                text="EDAM_data:1175",
                title="BioPax concept ID",
                description="An identifier of a concept from the BioPax ontology."))
        setattr(cls, "EDAM_data:1176",
            PermissibleValue(
                text="EDAM_data:1176",
                title="GO concept ID",
                description="An identifier of a concept from The Gene Ontology."))
        setattr(cls, "EDAM_data:1177",
            PermissibleValue(
                text="EDAM_data:1177",
                title="MeSH concept ID",
                description="An identifier of a concept from the MeSH vocabulary."))
        setattr(cls, "EDAM_data:1178",
            PermissibleValue(
                text="EDAM_data:1178",
                title="HGNC concept ID",
                description="An identifier of a concept from the HGNC controlled vocabulary."))
        setattr(cls, "EDAM_data:1179",
            PermissibleValue(
                text="EDAM_data:1179",
                title="NCBI taxonomy ID",
                description="""A stable unique identifier for each taxon (for a species, a family, an order, or any other group in the NCBI taxonomy database."""))
        setattr(cls, "EDAM_data:1180",
            PermissibleValue(
                text="EDAM_data:1180",
                title="Plant Ontology concept ID",
                description="An identifier of a concept from the Plant Ontology (PO)."))
        setattr(cls, "EDAM_data:1181",
            PermissibleValue(
                text="EDAM_data:1181",
                title="UMLS concept ID",
                description="An identifier of a concept from the UMLS vocabulary."))
        setattr(cls, "EDAM_data:1182",
            PermissibleValue(
                text="EDAM_data:1182",
                title="FMA concept ID",
                description="""An identifier of a concept from Foundational Model of Anatomy.
Classifies anatomical entities according to their shared characteristics (genus) and distinguishing characteristics (differentia). Specifies the part-whole and spatial relationships of the entities, morphological transformation of the entities during prenatal development and the postnatal life cycle and principles, rules and definitions according to which classes and relationships in the other three components of FMA are represented."""))
        setattr(cls, "EDAM_data:1183",
            PermissibleValue(
                text="EDAM_data:1183",
                title="EMAP concept ID",
                description="An identifier of a concept from the EMAP mouse ontology."))
        setattr(cls, "EDAM_data:1184",
            PermissibleValue(
                text="EDAM_data:1184",
                title="ChEBI concept ID",
                description="An identifier of a concept from the ChEBI ontology."))
        setattr(cls, "EDAM_data:1185",
            PermissibleValue(
                text="EDAM_data:1185",
                title="MGED concept ID",
                description="An identifier of a concept from the MGED ontology."))
        setattr(cls, "EDAM_data:1186",
            PermissibleValue(
                text="EDAM_data:1186",
                title="myGrid concept ID",
                description="""An identifier of a concept from the myGrid ontology.
The ontology is provided as two components, the service ontology and the domain ontology. The domain ontology acts provides concepts for core bioinformatics data types and their relations. The service ontology describes the physical and operational features of web services."""))
        setattr(cls, "EDAM_data:1187",
            PermissibleValue(
                text="EDAM_data:1187",
                title="PubMed ID",
                description="PubMed unique identifier of an article."))
        setattr(cls, "EDAM_data:1188",
            PermissibleValue(
                text="EDAM_data:1188",
                title="DOI",
                description="Digital Object Identifier (DOI) of a published article."))
        setattr(cls, "EDAM_data:1189",
            PermissibleValue(
                text="EDAM_data:1189",
                title="Medline UI",
                description="""Medline UI (unique identifier) of an article.
The use of Medline UI has been replaced by the PubMed unique identifier."""))
        setattr(cls, "EDAM_data:1190",
            PermissibleValue(
                text="EDAM_data:1190",
                title="Tool name",
                description="The name of a computer package, application, method or function."))
        setattr(cls, "EDAM_data:1191",
            PermissibleValue(
                text="EDAM_data:1191",
                title="Tool name (signature)",
                description="""Signature methods from http://www.ebi.ac.uk/Tools/InterProScan/help.html#results include BlastProDom, FPrintScan, HMMPIR, HMMPfam, HMMSmart, HMMTigr, ProfileScan, ScanRegExp, SuperFamily and HAMAP.
The unique name of a signature (sequence classifier) method."""))
        setattr(cls, "EDAM_data:1192",
            PermissibleValue(
                text="EDAM_data:1192",
                title="Tool name (BLAST)",
                description="""The name of a BLAST tool.
This include 'blastn', 'blastp', 'blastx', 'tblastn' and 'tblastx'."""))
        setattr(cls, "EDAM_data:1193",
            PermissibleValue(
                text="EDAM_data:1193",
                title="Tool name (FASTA)",
                description="""The name of a FASTA tool.
This includes 'fasta3', 'fastx3', 'fasty3', 'fastf3', 'fasts3' and 'ssearch'."""))
        setattr(cls, "EDAM_data:1194",
            PermissibleValue(
                text="EDAM_data:1194",
                title="Tool name (EMBOSS)",
                description="The name of an EMBOSS application."))
        setattr(cls, "EDAM_data:1195",
            PermissibleValue(
                text="EDAM_data:1195",
                title="Tool name (EMBASSY package)",
                description="The name of an EMBASSY package."))
        setattr(cls, "EDAM_data:1201",
            PermissibleValue(
                text="EDAM_data:1201",
                title="QSAR descriptor (constitutional)",
                description="A QSAR constitutional descriptor."))
        setattr(cls, "EDAM_data:1202",
            PermissibleValue(
                text="EDAM_data:1202",
                title="QSAR descriptor (electronic)",
                description="A QSAR electronic descriptor."))
        setattr(cls, "EDAM_data:1203",
            PermissibleValue(
                text="EDAM_data:1203",
                title="QSAR descriptor (geometrical)",
                description="A QSAR geometrical descriptor."))
        setattr(cls, "EDAM_data:1204",
            PermissibleValue(
                text="EDAM_data:1204",
                title="QSAR descriptor (topological)",
                description="A QSAR topological descriptor."))
        setattr(cls, "EDAM_data:1205",
            PermissibleValue(
                text="EDAM_data:1205",
                title="QSAR descriptor (molecular)",
                description="A QSAR molecular descriptor."))
        setattr(cls, "EDAM_data:1233",
            PermissibleValue(
                text="EDAM_data:1233",
                title="Sequence set (protein)",
                description="""Any collection of multiple protein sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries."""))
        setattr(cls, "EDAM_data:1234",
            PermissibleValue(
                text="EDAM_data:1234",
                title="Sequence set (nucleic acid)",
                description="""Any collection of multiple nucleotide sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries."""))
        setattr(cls, "EDAM_data:1235",
            PermissibleValue(
                text="EDAM_data:1235",
                title="Sequence cluster",
                description="""A set of sequences that have been clustered or otherwise classified as belonging to a group including (typically) sequence cluster information.
The cluster might include sequences identifiers, short descriptions, alignment and summary information."""))
        setattr(cls, "EDAM_data:1238",
            PermissibleValue(
                text="EDAM_data:1238",
                title="Proteolytic digest",
                description="""A protein sequence cleaved into peptide fragments (by enzymatic or chemical cleavage) with fragment masses."""))
        setattr(cls, "EDAM_data:1239",
            PermissibleValue(
                text="EDAM_data:1239",
                title="Restriction digest",
                description="""Restriction digest fragments from digesting a nucleotide sequence with restriction sites using a restriction endonuclease."""))
        setattr(cls, "EDAM_data:1240",
            PermissibleValue(
                text="EDAM_data:1240",
                title="PCR primers",
                description="""Oligonucleotide primer(s) for PCR and DNA amplification, for example a minimal primer set."""))
        setattr(cls, "EDAM_data:1245",
            PermissibleValue(
                text="EDAM_data:1245",
                title="Sequence cluster (protein)",
                description="""A cluster of protein sequences.
The sequences are typically related, for example a family of sequences."""))
        setattr(cls, "EDAM_data:1246",
            PermissibleValue(
                text="EDAM_data:1246",
                title="Sequence cluster (nucleic acid)",
                description="""A cluster of nucleotide sequences.
The sequences are typically related, for example a family of sequences."""))
        setattr(cls, "EDAM_data:1249",
            PermissibleValue(
                text="EDAM_data:1249",
                title="Sequence length",
                description="""The size (length) of a sequence, subsequence or region in a sequence, or range(s) of lengths."""))
        setattr(cls, "EDAM_data:1254",
            PermissibleValue(
                text="EDAM_data:1254",
                title="Sequence property",
                description="""An informative report about non-positional sequence features, typically a report on general molecular sequence properties derived from sequence analysis."""))
        setattr(cls, "EDAM_data:1255",
            PermissibleValue(
                text="EDAM_data:1255",
                title="Sequence features",
                description="""Annotation of positional features of molecular sequence(s), i.e. that can be mapped to position(s) in the sequence.
This includes annotation of positional sequence features, organised into a standard feature table, or any other report of sequence features. General feature reports are a source of sequence feature table information although internal conversion would be required."""))
        setattr(cls, "EDAM_data:1259",
            PermissibleValue(
                text="EDAM_data:1259",
                title="Sequence complexity report",
                description="""A report on sequence complexity, for example low-complexity or repeat regions in sequences."""))
        setattr(cls, "EDAM_data:1260",
            PermissibleValue(
                text="EDAM_data:1260",
                title="Sequence ambiguity report",
                description="A report on ambiguity in molecular sequence(s)."))
        setattr(cls, "EDAM_data:1261",
            PermissibleValue(
                text="EDAM_data:1261",
                title="Sequence composition report",
                description="""A report (typically a table) on character or word composition / frequency of a molecular sequence(s)."""))
        setattr(cls, "EDAM_data:1262",
            PermissibleValue(
                text="EDAM_data:1262",
                title="Peptide molecular weight hits",
                description="""A report on peptide fragments of certain molecular weight(s) in one or more protein sequences."""))
        setattr(cls, "EDAM_data:1263",
            PermissibleValue(
                text="EDAM_data:1263",
                title="Base position variability plot",
                description="A plot of third base position variability in a nucleotide sequence."))
        setattr(cls, "EDAM_data:1265",
            PermissibleValue(
                text="EDAM_data:1265",
                title="Base frequencies table",
                description="A table of base frequencies of a nucleotide sequence."))
        setattr(cls, "EDAM_data:1266",
            PermissibleValue(
                text="EDAM_data:1266",
                title="Base word frequencies table",
                description="A table of word composition of a nucleotide sequence."))
        setattr(cls, "EDAM_data:1267",
            PermissibleValue(
                text="EDAM_data:1267",
                title="Amino acid frequencies table",
                description="A table of amino acid frequencies of a protein sequence."))
        setattr(cls, "EDAM_data:1268",
            PermissibleValue(
                text="EDAM_data:1268",
                title="Amino acid word frequencies table",
                description="A table of amino acid word composition of a protein sequence."))
        setattr(cls, "EDAM_data:1270",
            PermissibleValue(
                text="EDAM_data:1270",
                title="Feature table",
                description="Annotation of positional sequence features, organised into a standard feature table."))
        setattr(cls, "EDAM_data:1274",
            PermissibleValue(
                text="EDAM_data:1274",
                title="Map",
                description="""A map of (typically one) DNA sequence annotated with positional or non-positional features."""))
        setattr(cls, "EDAM_data:1276",
            PermissibleValue(
                text="EDAM_data:1276",
                title="Nucleic acid features",
                description="""An informative report on intrinsic positional features of a nucleotide sequence, formatted to be machine-readable.
This includes nucleotide sequence feature annotation in any known sequence feature table format and any other report of nucleic acid features."""))
        setattr(cls, "EDAM_data:1277",
            PermissibleValue(
                text="EDAM_data:1277",
                title="Protein features",
                description="""An informative report on intrinsic positional features of a protein sequence.
This includes protein sequence feature annotation in any known sequence feature table format and any other report of protein features."""))
        setattr(cls, "EDAM_data:1278",
            PermissibleValue(
                text="EDAM_data:1278",
                title="Genetic map",
                description="""A genetic (linkage) map indicates the proximity of two genes on a chromosome, whether two genes are linked and the frequency they are transmitted together to an offspring. They are limited to genetic markers of traits observable only in whole organisms.
A map showing the relative positions of genetic markers in a nucleic acid sequence, based on estimation of non-physical distance such as recombination frequencies."""))
        setattr(cls, "EDAM_data:1279",
            PermissibleValue(
                text="EDAM_data:1279",
                title="Sequence map",
                description="""A map of genetic markers in a contiguous, assembled genomic sequence, with the sizes and separation of markers measured in base pairs.
A sequence map typically includes annotation on significant subsequences such as contigs, haplotypes and genes. The contigs shown will (typically) be a set of small overlapping clones representing a complete chromosomal segment."""))
        setattr(cls, "EDAM_data:1280",
            PermissibleValue(
                text="EDAM_data:1280",
                title="Physical map",
                description="""A map of DNA (linear or circular) annotated with physical features or landmarks such as restriction sites, cloned DNA fragments, genes or genetic markers, along with the physical distances between them.
Distance in a physical map is measured in base pairs. A physical map might be ordered relative to a reference map (typically a genetic map) in the process of genome sequencing."""))
        setattr(cls, "EDAM_data:1283",
            PermissibleValue(
                text="EDAM_data:1283",
                title="Cytogenetic map",
                description="""A map showing banding patterns derived from direct observation of a stained chromosome.
This is the lowest-resolution physical map and can provide only rough estimates of physical (base pair) distances. Like a genetic map, they are limited to genetic markers of traits observable only in whole organisms."""))
        setattr(cls, "EDAM_data:1284",
            PermissibleValue(
                text="EDAM_data:1284",
                title="DNA transduction map",
                description="""A gene map showing distances between loci based on relative cotransduction frequencies."""))
        setattr(cls, "EDAM_data:1285",
            PermissibleValue(
                text="EDAM_data:1285",
                title="Gene map",
                description="""Sequence map of a single gene annotated with genetic features such as introns, exons, untranslated regions, polyA signals, promoters, enhancers and (possibly) mutations defining alleles of a gene."""))
        setattr(cls, "EDAM_data:1286",
            PermissibleValue(
                text="EDAM_data:1286",
                title="Plasmid map",
                description="Sequence map of a plasmid (circular DNA)."))
        setattr(cls, "EDAM_data:1288",
            PermissibleValue(
                text="EDAM_data:1288",
                title="Genome map",
                description="Sequence map of a whole genome."))
        setattr(cls, "EDAM_data:1289",
            PermissibleValue(
                text="EDAM_data:1289",
                title="Restriction map",
                description="""Image of the restriction enzyme cleavage sites (restriction sites) in a nucleic acid sequence."""))
        setattr(cls, "EDAM_data:1347",
            PermissibleValue(
                text="EDAM_data:1347",
                title="Dirichlet distribution",
                description="Dirichlet distribution used by hidden Markov model analysis programs."))
        setattr(cls, "EDAM_data:1352",
            PermissibleValue(
                text="EDAM_data:1352",
                title="Regular expression",
                description="Regular expression pattern."))
        setattr(cls, "EDAM_data:1353",
            PermissibleValue(
                text="EDAM_data:1353",
                title="Sequence motif",
                description="""Any specific or conserved pattern (typically expressed as a regular expression) in a molecular sequence."""))
        setattr(cls, "EDAM_data:1354",
            PermissibleValue(
                text="EDAM_data:1354",
                title="Sequence profile",
                description="Some type of statistical model representing a (typically multiple) sequence alignment."))
        setattr(cls, "EDAM_data:1355",
            PermissibleValue(
                text="EDAM_data:1355",
                title="Protein signature",
                description="An informative report about a specific or conserved protein sequence pattern."))
        setattr(cls, "EDAM_data:1361",
            PermissibleValue(
                text="EDAM_data:1361",
                title="Position frequency matrix",
                description="""A profile (typically representing a sequence alignment) that is a simple matrix of nucleotide (or amino acid) counts per position."""))
        setattr(cls, "EDAM_data:1362",
            PermissibleValue(
                text="EDAM_data:1362",
                title="Position weight matrix",
                description="""A profile (typically representing a sequence alignment) that is weighted matrix of nucleotide (or amino acid) counts per position.
Contributions of individual sequences to the matrix might be uneven (weighted)."""))
        setattr(cls, "EDAM_data:1363",
            PermissibleValue(
                text="EDAM_data:1363",
                title="Information content matrix",
                description="""A profile (typically representing a sequence alignment) derived from a matrix of nucleotide (or amino acid) counts per position that reflects information content at each position."""))
        setattr(cls, "EDAM_data:1364",
            PermissibleValue(
                text="EDAM_data:1364",
                title="Hidden Markov model",
                description="""A statistical Markov model of a system which is assumed to be a Markov process with unobserved (hidden) states. For example, a hidden Markov model representation of a set or alignment of sequences."""))
        setattr(cls, "EDAM_data:1365",
            PermissibleValue(
                text="EDAM_data:1365",
                title="Fingerprint",
                description="One or more fingerprints (sequence classifiers) as used in the PRINTS database."))
        setattr(cls, "EDAM_data:1381",
            PermissibleValue(
                text="EDAM_data:1381",
                title="Pair sequence alignment",
                description="Alignment of exactly two molecular sequences."))
        setattr(cls, "EDAM_data:1383",
            PermissibleValue(
                text="EDAM_data:1383",
                title="Nucleic acid sequence alignment",
                description="Alignment of multiple nucleotide sequences."))
        setattr(cls, "EDAM_data:1384",
            PermissibleValue(
                text="EDAM_data:1384",
                title="Protein sequence alignment",
                description="Alignment of multiple protein sequences."))
        setattr(cls, "EDAM_data:1385",
            PermissibleValue(
                text="EDAM_data:1385",
                title="Hybrid sequence alignment",
                description="""Alignment of multiple molecular sequences of different types.
Hybrid sequence alignments include for example genomic DNA to EST, cDNA or mRNA."""))
        setattr(cls, "EDAM_data:1394",
            PermissibleValue(
                text="EDAM_data:1394",
                title="Alignment score or penalty",
                description="""A simple floating point number defining the penalty for opening or extending a gap in an alignment."""))
        setattr(cls, "EDAM_data:1397",
            PermissibleValue(
                text="EDAM_data:1397",
                title="Gap opening penalty",
                description="A penalty for opening a gap in an alignment."))
        setattr(cls, "EDAM_data:1398",
            PermissibleValue(
                text="EDAM_data:1398",
                title="Gap extension penalty",
                description="A penalty for extending a gap in an alignment."))
        setattr(cls, "EDAM_data:1399",
            PermissibleValue(
                text="EDAM_data:1399",
                title="Gap separation penalty",
                description="A penalty for gaps that are close together in an alignment."))
        setattr(cls, "EDAM_data:1401",
            PermissibleValue(
                text="EDAM_data:1401",
                title="Match reward score",
                description="""The score for a 'match' used in various sequence database search applications with simple scoring schemes."""))
        setattr(cls, "EDAM_data:1402",
            PermissibleValue(
                text="EDAM_data:1402",
                title="Mismatch penalty score",
                description="""The score (penalty) for a 'mismatch' used in various alignment and sequence database search applications with simple scoring schemes."""))
        setattr(cls, "EDAM_data:1403",
            PermissibleValue(
                text="EDAM_data:1403",
                title="Drop off score",
                description="This is the threshold drop in score at which extension of word alignment is halted."))
        setattr(cls, "EDAM_data:1410",
            PermissibleValue(
                text="EDAM_data:1410",
                title="Terminal gap opening penalty",
                description="""A number defining the penalty for opening gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences."""))
        setattr(cls, "EDAM_data:1411",
            PermissibleValue(
                text="EDAM_data:1411",
                title="Terminal gap extension penalty",
                description="""A number defining the penalty for extending gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences."""))
        setattr(cls, "EDAM_data:1412",
            PermissibleValue(
                text="EDAM_data:1412",
                title="Sequence identity",
                description="""Sequence identity is the number (%) of matches (identical characters) in positions from an alignment of two molecular sequences."""))
        setattr(cls, "EDAM_data:1413",
            PermissibleValue(
                text="EDAM_data:1413",
                title="Sequence similarity",
                description="""Data Type is float probably.
Sequence similarity is the similarity (expressed as a percentage) of two molecular sequences calculated from their alignment, a scoring matrix for scoring characters substitutions and penalties for gap insertion and extension."""))
        setattr(cls, "EDAM_data:1426",
            PermissibleValue(
                text="EDAM_data:1426",
                title="Phylogenetic continuous quantitative data",
                description="Continuous quantitative data that may be read during phylogenetic tree calculation."))
        setattr(cls, "EDAM_data:1427",
            PermissibleValue(
                text="EDAM_data:1427",
                title="Phylogenetic discrete data",
                description="""Character data with discrete states that may be read during phylogenetic tree calculation."""))
        setattr(cls, "EDAM_data:1428",
            PermissibleValue(
                text="EDAM_data:1428",
                title="Phylogenetic character cliques",
                description="""One or more cliques of mutually compatible characters that are generated, for example from analysis of discrete character data, and are used to generate a phylogeny."""))
        setattr(cls, "EDAM_data:1429",
            PermissibleValue(
                text="EDAM_data:1429",
                title="Phylogenetic invariants",
                description="Phylogenetic invariants data for testing alternative tree topologies."))
        setattr(cls, "EDAM_data:1439",
            PermissibleValue(
                text="EDAM_data:1439",
                title="DNA substitution model",
                description="""A model of DNA substitution that explains a DNA sequence alignment, derived from phylogenetic tree analysis."""))
        setattr(cls, "EDAM_data:1442",
            PermissibleValue(
                text="EDAM_data:1442",
                title="Phylogenetic tree distances",
                description="Distances, such as Branch Score distance, between two or more phylogenetic trees."))
        setattr(cls, "EDAM_data:1444",
            PermissibleValue(
                text="EDAM_data:1444",
                title="Phylogenetic character contrasts",
                description="""Independent contrasts for characters used in a phylogenetic tree, or covariances, regressions and correlations between characters for those contrasts."""))
        setattr(cls, "EDAM_data:1448",
            PermissibleValue(
                text="EDAM_data:1448",
                title="Comparison matrix (nucleotide)",
                description="Matrix of integer or floating point numbers for nucleotide comparison."))
        setattr(cls, "EDAM_data:1449",
            PermissibleValue(
                text="EDAM_data:1449",
                title="Comparison matrix (amino acid)",
                description="Matrix of integer or floating point numbers for amino acid comparison."))
        setattr(cls, "EDAM_data:1459",
            PermissibleValue(
                text="EDAM_data:1459",
                title="Nucleic acid structure",
                description="3D coordinate and associated data for a nucleic acid tertiary (3D) structure."))
        setattr(cls, "EDAM_data:1460",
            PermissibleValue(
                text="EDAM_data:1460",
                title="Protein structure",
                description="""3D coordinate and associated data for a protein tertiary (3D) structure, or part of a structure, possibly in complex with other molecules."""))
        setattr(cls, "EDAM_data:1461",
            PermissibleValue(
                text="EDAM_data:1461",
                title="Protein-ligand complex",
                description="""The structure of a protein in complex with a ligand, typically a small molecule such as an enzyme substrate or cofactor, but possibly another macromolecule.
This includes interactions of proteins with atoms, ions and small molecules or macromolecules such as nucleic acids or other polypeptides. For stable inter-polypeptide interactions use 'Protein complex' instead."""))
        setattr(cls, "EDAM_data:1462",
            PermissibleValue(
                text="EDAM_data:1462",
                title="Carbohydrate structure",
                description="3D coordinate and associated data for a carbohydrate (3D) structure."))
        setattr(cls, "EDAM_data:1463",
            PermissibleValue(
                text="EDAM_data:1463",
                title="Small molecule structure",
                description="""3D coordinate and associated data for the (3D) structure of a small molecule, such as any common chemical compound."""))
        setattr(cls, "EDAM_data:1464",
            PermissibleValue(
                text="EDAM_data:1464",
                title="DNA structure",
                description="3D coordinate and associated data for a DNA tertiary (3D) structure."))
        setattr(cls, "EDAM_data:1465",
            PermissibleValue(
                text="EDAM_data:1465",
                title="RNA structure",
                description="3D coordinate and associated data for an RNA tertiary (3D) structure."))
        setattr(cls, "EDAM_data:1466",
            PermissibleValue(
                text="EDAM_data:1466",
                title="tRNA structure",
                description="""3D coordinate and associated data for a tRNA tertiary (3D) structure, including tmRNA, snoRNAs etc."""))
        setattr(cls, "EDAM_data:1467",
            PermissibleValue(
                text="EDAM_data:1467",
                title="Protein chain",
                description="""3D coordinate and associated data for the tertiary (3D) structure of a polypeptide chain."""))
        setattr(cls, "EDAM_data:1468",
            PermissibleValue(
                text="EDAM_data:1468",
                title="Protein domain",
                description="3D coordinate and associated data for the tertiary (3D) structure of a protein domain."))
        setattr(cls, "EDAM_data:1470",
            PermissibleValue(
                text="EDAM_data:1470",
                title="C-alpha trace",
                description="""3D coordinate and associated data for a protein tertiary (3D) structure (typically C-alpha atoms only).
C-beta atoms from amino acid side-chains may be included."""))
        setattr(cls, "EDAM_data:1479",
            PermissibleValue(
                text="EDAM_data:1479",
                title="Structure alignment (pair)",
                description="Alignment (superimposition) of exactly two molecular tertiary (3D) structures."))
        setattr(cls, "EDAM_data:1481",
            PermissibleValue(
                text="EDAM_data:1481",
                title="Protein structure alignment",
                description="Alignment (superimposition) of protein tertiary (3D) structures."))
        setattr(cls, "EDAM_data:1482",
            PermissibleValue(
                text="EDAM_data:1482",
                title="Nucleic acid structure alignment",
                description="Alignment (superimposition) of nucleic acid tertiary (3D) structures."))
        setattr(cls, "EDAM_data:1493",
            PermissibleValue(
                text="EDAM_data:1493",
                title="RNA structure alignment",
                description="Alignment (superimposition) of RNA tertiary (3D) structures."))
        setattr(cls, "EDAM_data:1494",
            PermissibleValue(
                text="EDAM_data:1494",
                title="Structural transformation matrix",
                description="""Matrix to transform (rotate/translate) 3D coordinates, typically the transformation necessary to superimpose two molecular structures."""))
        setattr(cls, "EDAM_data:1497",
            PermissibleValue(
                text="EDAM_data:1497",
                title="Root-mean-square deviation",
                description="""Root-mean-square deviation (RMSD) is calculated to measure the average distance between superimposed macromolecular coordinates."""))
        setattr(cls, "EDAM_data:1498",
            PermissibleValue(
                text="EDAM_data:1498",
                title="Tanimoto similarity score",
                description="""A ligand fingerprint is derived from ligand structural data from a Protein DataBank file. It reflects the elements or groups present or absent, covalent bonds and bond orders and the bonded environment in terms of SATIS codes and BLEEP atom types.
A measure of the similarity between two ligand fingerprints."""))
        setattr(cls, "EDAM_data:1499",
            PermissibleValue(
                text="EDAM_data:1499",
                title="3D-1D scoring matrix",
                description="""A matrix of 3D-1D scores reflecting the probability of amino acids to occur in different tertiary structural environments."""))
        setattr(cls, "EDAM_data:1501",
            PermissibleValue(
                text="EDAM_data:1501",
                title="Amino acid index",
                description="""A table of 20 numerical values which quantify a property (e.g. physicochemical or biochemical) of the common amino acids."""))
        setattr(cls, "EDAM_data:1502",
            PermissibleValue(
                text="EDAM_data:1502",
                title="Amino acid index (chemical classes)",
                description="""Chemical classification (small, aliphatic, aromatic, polar, charged etc) of amino acids."""))
        setattr(cls, "EDAM_data:1503",
            PermissibleValue(
                text="EDAM_data:1503",
                title="Amino acid pair-wise contact potentials",
                description="Statistical protein contact potentials."))
        setattr(cls, "EDAM_data:1505",
            PermissibleValue(
                text="EDAM_data:1505",
                title="Amino acid index (molecular weight)",
                description="Molecular weights of amino acids."))
        setattr(cls, "EDAM_data:1506",
            PermissibleValue(
                text="EDAM_data:1506",
                title="Amino acid index (hydropathy)",
                description="Hydrophobic, hydrophilic or charge properties of amino acids."))
        setattr(cls, "EDAM_data:1507",
            PermissibleValue(
                text="EDAM_data:1507",
                title="Amino acid index (White-Wimley data)",
                description="""Experimental free energy values for the water-interface and water-octanol transitions for the amino acids."""))
        setattr(cls, "EDAM_data:1508",
            PermissibleValue(
                text="EDAM_data:1508",
                title="Amino acid index (van der Waals radii)",
                description="Van der Waals radii of atoms for different amino acid residues."))
        setattr(cls, "EDAM_data:1519",
            PermissibleValue(
                text="EDAM_data:1519",
                title="Peptide molecular weights",
                description="""List of molecular weight(s) of one or more proteins or peptides, for example cut by proteolytic enzymes or reagents.
The report might include associated data such as frequency of peptide fragment molecular weights."""))
        setattr(cls, "EDAM_data:1520",
            PermissibleValue(
                text="EDAM_data:1520",
                title="Peptide hydrophobic moment",
                description="""Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation.
Report on the hydrophobic moment of a polypeptide sequence."""))
        setattr(cls, "EDAM_data:1521",
            PermissibleValue(
                text="EDAM_data:1521",
                title="Protein aliphatic index",
                description="""The aliphatic index is the relative protein volume occupied by aliphatic side chains.
The aliphatic index of a protein."""))
        setattr(cls, "EDAM_data:1522",
            PermissibleValue(
                text="EDAM_data:1522",
                title="Protein sequence hydropathy plot",
                description="""A protein sequence with annotation on hydrophobic or hydrophilic / charged regions, hydrophobicity plot etc.
Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation."""))
        setattr(cls, "EDAM_data:1523",
            PermissibleValue(
                text="EDAM_data:1523",
                title="Protein charge plot",
                description="""A plot of the mean charge of the amino acids within a window of specified length as the window is moved along a protein sequence."""))
        setattr(cls, "EDAM_data:1524",
            PermissibleValue(
                text="EDAM_data:1524",
                title="Protein solubility",
                description="The solubility or atomic solvation energy of a protein sequence or structure."))
        setattr(cls, "EDAM_data:1525",
            PermissibleValue(
                text="EDAM_data:1525",
                title="Protein crystallizability",
                description="Data on the crystallizability of a protein sequence."))
        setattr(cls, "EDAM_data:1526",
            PermissibleValue(
                text="EDAM_data:1526",
                title="Protein globularity",
                description="Data on the stability, intrinsic disorder or globularity of a protein sequence."))
        setattr(cls, "EDAM_data:1527",
            PermissibleValue(
                text="EDAM_data:1527",
                title="Protein titration curve",
                description="The titration curve of a protein."))
        setattr(cls, "EDAM_data:1528",
            PermissibleValue(
                text="EDAM_data:1528",
                title="Protein isoelectric point",
                description="The isoelectric point of one proteins."))
        setattr(cls, "EDAM_data:1529",
            PermissibleValue(
                text="EDAM_data:1529",
                title="Protein pKa value",
                description="The pKa value of a protein."))
        setattr(cls, "EDAM_data:1530",
            PermissibleValue(
                text="EDAM_data:1530",
                title="Protein hydrogen exchange rate",
                description="The hydrogen exchange rate of a protein."))
        setattr(cls, "EDAM_data:1531",
            PermissibleValue(
                text="EDAM_data:1531",
                title="Protein extinction coefficient",
                description="The extinction coefficient of a protein."))
        setattr(cls, "EDAM_data:1532",
            PermissibleValue(
                text="EDAM_data:1532",
                title="Protein optical density",
                description="The optical density of a protein."))
        setattr(cls, "EDAM_data:1534",
            PermissibleValue(
                text="EDAM_data:1534",
                title="Peptide immunogenicity data",
                description="""An report on allergenicity / immunogenicity of peptides and proteins.
This includes data on peptide ligands that elicit an immune response (immunogens), allergic cross-reactivity, predicted antigenicity (Hopp and Woods plot) etc. These data are useful in the development of peptide-specific antibodies or multi-epitope vaccines. Methods might use sequence data (for example motifs) and / or structural data."""))
        setattr(cls, "EDAM_data:1537",
            PermissibleValue(
                text="EDAM_data:1537",
                title="Protein structure report",
                description="""A human-readable collection of information about one or more specific protein 3D structure(s) or structural domains."""))
        setattr(cls, "EDAM_data:1539",
            PermissibleValue(
                text="EDAM_data:1539",
                title="Protein structural quality report",
                description="""Model validation might involve checks for atomic packing, steric clashes, agreement with electron density maps etc.
Report on the quality of a protein three-dimensional model."""))
        setattr(cls, "EDAM_data:1542",
            PermissibleValue(
                text="EDAM_data:1542",
                title="Protein solvent accessibility",
                description="""Data on the solvent accessible or buried surface area of a protein structure.
This concept covers definitions of the protein surface, interior and interfaces, accessible and buried residues, surface accessible pockets, interior inaccessible cavities etc."""))
        setattr(cls, "EDAM_data:1544",
            PermissibleValue(
                text="EDAM_data:1544",
                title="Ramachandran plot",
                description="Phi/psi angle data or a Ramachandran plot of a protein structure."))
        setattr(cls, "EDAM_data:1545",
            PermissibleValue(
                text="EDAM_data:1545",
                title="Protein dipole moment",
                description="Data on the net charge distribution (dipole moment) of a protein structure."))
        setattr(cls, "EDAM_data:1546",
            PermissibleValue(
                text="EDAM_data:1546",
                title="Protein distance matrix",
                description="""A matrix of distances between amino acid residues (for example the C-alpha atoms) in a protein structure."""))
        setattr(cls, "EDAM_data:1547",
            PermissibleValue(
                text="EDAM_data:1547",
                title="Protein contact map",
                description="An amino acid residue contact map for a protein structure."))
        setattr(cls, "EDAM_data:1548",
            PermissibleValue(
                text="EDAM_data:1548",
                title="Protein residue 3D cluster",
                description="""Report on clusters of contacting residues in protein structures such as a key structural residue network."""))
        setattr(cls, "EDAM_data:1549",
            PermissibleValue(
                text="EDAM_data:1549",
                title="Protein hydrogen bonds",
                description="Patterns of hydrogen bonding in protein structures."))
        setattr(cls, "EDAM_data:1566",
            PermissibleValue(
                text="EDAM_data:1566",
                title="Protein-ligand interaction report",
                description="An informative report on protein-ligand (small molecule) interaction(s)."))
        setattr(cls, "EDAM_data:1583",
            PermissibleValue(
                text="EDAM_data:1583",
                title="Nucleic acid melting profile",
                description="""A melting (stability) profile calculated the free energy required to unwind and separate the nucleic acid strands, plotted for sliding windows over a sequence.
Data on the dissociation characteristics of a double-stranded nucleic acid molecule (DNA or a DNA/RNA hybrid) during heating.
Nucleic acid melting curve: a melting curve of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the proportion of nucleic acid which are double-stranded versus temperature.
Nucleic acid probability profile: a probability profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the probability of a base pair not being melted (i.e. remaining as double-stranded DNA) at a specified temperature
Nucleic acid stitch profile: stitch profile of hybridised or double stranded nucleic acid (DNA or RNA/DNA). A stitch profile diagram shows partly melted DNA conformations (with probabilities) at a range of temperatures. For example, a stitch profile might show possible loop openings with their location, size, probability and fluctuations at a given temperature.
Nucleic acid temperature profile: a temperature profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Plots melting temperature versus base position."""))
        setattr(cls, "EDAM_data:1584",
            PermissibleValue(
                text="EDAM_data:1584",
                title="Nucleic acid enthalpy",
                description="Enthalpy of hybridised or double stranded nucleic acid (DNA or RNA/DNA)."))
        setattr(cls, "EDAM_data:1585",
            PermissibleValue(
                text="EDAM_data:1585",
                title="Nucleic acid entropy",
                description="Entropy of hybridised or double stranded nucleic acid (DNA or RNA/DNA)."))
        setattr(cls, "EDAM_data:1588",
            PermissibleValue(
                text="EDAM_data:1588",
                title="DNA base pair stacking energies data",
                description="DNA base pair stacking energies data."))
        setattr(cls, "EDAM_data:1589",
            PermissibleValue(
                text="EDAM_data:1589",
                title="DNA base pair twist angle data",
                description="DNA base pair twist angle data."))
        setattr(cls, "EDAM_data:1590",
            PermissibleValue(
                text="EDAM_data:1590",
                title="DNA base trimer roll angles data",
                description="DNA base trimer roll angles data."))
        setattr(cls, "EDAM_data:1595",
            PermissibleValue(
                text="EDAM_data:1595",
                title="Base pairing probability matrix dotplot",
                description="""Dotplot of RNA base pairing probability matrix.
Such as generated by the Vienna package."""))
        setattr(cls, "EDAM_data:1596",
            PermissibleValue(
                text="EDAM_data:1596",
                title="Nucleic acid folding report",
                description="""A human-readable collection of information about RNA/DNA folding, minimum folding energies for DNA or RNA sequences, energy landscape of RNA mutants etc."""))
        setattr(cls, "EDAM_data:1597",
            PermissibleValue(
                text="EDAM_data:1597",
                title="Codon usage table",
                description="""A codon usage table might include the codon usage table name, optional comments and a table with columns for codons and corresponding codon usage data. A genetic code can be extracted from or represented by a codon usage table.
Table of codon usage data calculated from one or more nucleic acid sequences."""))
        setattr(cls, "EDAM_data:1598",
            PermissibleValue(
                text="EDAM_data:1598",
                title="Genetic code",
                description="""A genetic code for an organism.
A genetic code need not include detailed codon usage information."""))
        setattr(cls, "EDAM_data:1600",
            PermissibleValue(
                text="EDAM_data:1600",
                title="Codon usage bias plot",
                description="""A plot of the synonymous codon usage calculated for windows over a nucleotide sequence."""))
        setattr(cls, "EDAM_data:1602",
            PermissibleValue(
                text="EDAM_data:1602",
                title="Codon usage fraction difference",
                description="The differences in codon usage fractions between two codon usage tables."))
        setattr(cls, "EDAM_data:1621",
            PermissibleValue(
                text="EDAM_data:1621",
                title="Pharmacogenomic test report",
                description="""A human-readable collection of information about the influence of genotype on drug response.
The report might correlate gene expression or single-nucleotide polymorphisms with drug efficacy or toxicity."""))
        setattr(cls, "EDAM_data:1622",
            PermissibleValue(
                text="EDAM_data:1622",
                title="Disease report",
                description="""A human-readable collection of information about a specific disease.
For example, an informative report on a specific tumor including nature and origin of the sample, anatomic site, organ or tissue, tumor type, including morphology and/or histologic type, and so on."""))
        setattr(cls, "EDAM_data:1636",
            PermissibleValue(
                text="EDAM_data:1636",
                title="Heat map",
                description="""A graphical 2D tabular representation of expression data, typically derived from an omics experiment. A heat map is a table where rows and columns correspond to different features and contexts (for example, cells or samples) and the cell colour represents the level of expression of a gene that context."""))
        setattr(cls, "EDAM_data:1667",
            PermissibleValue(
                text="EDAM_data:1667",
                title="E-value",
                description="""A simple floating point number defining the lower or upper limit of an expectation value (E-value).
An expectation value (E-Value) is the expected number of observations which are at least as extreme as observations expected to occur by random chance. The E-value describes the number of hits with a given score or better that are expected to occur at random when searching a database of a particular size. It decreases exponentially with the score (S) of a hit. A low E value indicates a more significant score."""))
        setattr(cls, "EDAM_data:1668",
            PermissibleValue(
                text="EDAM_data:1668",
                title="Z-value",
                description="""A z-value might be specified as a threshold for reporting hits from database searches.
The z-value is the number of standard deviations a data value is above or below a mean value."""))
        setattr(cls, "EDAM_data:1669",
            PermissibleValue(
                text="EDAM_data:1669",
                title="P-value",
                description="""A z-value might be specified as a threshold for reporting hits from database searches.
The P-value is the probability of obtaining by random chance a result that is at least as extreme as an observed result, assuming a NULL hypothesis is true."""))
        setattr(cls, "EDAM_data:1689",
            PermissibleValue(
                text="EDAM_data:1689",
                title="Username",
                description="A username on a computer system or a website."))
        setattr(cls, "EDAM_data:1690",
            PermissibleValue(
                text="EDAM_data:1690",
                title="Password",
                description="A password on a computer system, or a website."))
        setattr(cls, "EDAM_data:1691",
            PermissibleValue(
                text="EDAM_data:1691",
                title="Email address",
                description="A valid email address of an end-user."))
        setattr(cls, "EDAM_data:1692",
            PermissibleValue(
                text="EDAM_data:1692",
                title="Person name",
                description="The name of a person."))
        setattr(cls, "EDAM_data:1696",
            PermissibleValue(
                text="EDAM_data:1696",
                title="Drug report",
                description="""A drug structure relationship map is report (typically a map diagram) of drug structure relationships.
A human-readable collection of information about a specific drug."""))
        setattr(cls, "EDAM_data:1707",
            PermissibleValue(
                text="EDAM_data:1707",
                title="Phylogenetic tree image",
                description="""An image (for viewing or printing) of a phylogenetic tree including (typically) a plot of rooted or unrooted phylogenies, cladograms, circular trees or phenograms and associated information.
See also 'Phylogenetic tree'"""))
        setattr(cls, "EDAM_data:1708",
            PermissibleValue(
                text="EDAM_data:1708",
                title="RNA secondary structure image",
                description="Image of RNA secondary structure, knots, pseudoknots etc."))
        setattr(cls, "EDAM_data:1709",
            PermissibleValue(
                text="EDAM_data:1709",
                title="Protein secondary structure image",
                description="Image of protein secondary structure."))
        setattr(cls, "EDAM_data:1710",
            PermissibleValue(
                text="EDAM_data:1710",
                title="Structure image",
                description="Image of one or more molecular tertiary (3D) structures."))
        setattr(cls, "EDAM_data:1711",
            PermissibleValue(
                text="EDAM_data:1711",
                title="Sequence alignment image",
                description="""Image of two or more aligned molecular sequences possibly annotated with alignment features."""))
        setattr(cls, "EDAM_data:1712",
            PermissibleValue(
                text="EDAM_data:1712",
                title="Chemical structure image",
                description="""An image of the structure of a small chemical compound.
The molecular identifier and formula are typically included."""))
        setattr(cls, "EDAM_data:1713",
            PermissibleValue(
                text="EDAM_data:1713",
                title="Fate map",
                description="""A fate map is a plan of early stage of an embryo such as a blastula, showing areas that are significance to development."""))
        setattr(cls, "EDAM_data:1714",
            PermissibleValue(
                text="EDAM_data:1714",
                title="Microarray spots image",
                description="An image of spots from a microarray experiment."))
        setattr(cls, "EDAM_data:1731",
            PermissibleValue(
                text="EDAM_data:1731",
                title="Ontology concept definition",
                description="The definition of a concept from an ontology."))
        setattr(cls, "EDAM_data:1742",
            PermissibleValue(
                text="EDAM_data:1742",
                title="PDB residue number",
                description="A residue identifier (a string) from a PDB file."))
        setattr(cls, "EDAM_data:1743",
            PermissibleValue(
                text="EDAM_data:1743",
                title="Atomic coordinate",
                description="Cartesian coordinate of an atom (in a molecular structure)."))
        setattr(cls, "EDAM_data:1748",
            PermissibleValue(
                text="EDAM_data:1748",
                title="PDB atom name",
                description="Identifier (a string) of a specific atom from a PDB file for a molecular structure."))
        setattr(cls, "EDAM_data:1755",
            PermissibleValue(
                text="EDAM_data:1755",
                title="Protein atom",
                description="""Data on a single atom from a protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation."""))
        setattr(cls, "EDAM_data:1756",
            PermissibleValue(
                text="EDAM_data:1756",
                title="Protein residue",
                description="""Data on a single amino acid residue position in a protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation."""))
        setattr(cls, "EDAM_data:1757",
            PermissibleValue(
                text="EDAM_data:1757",
                title="Atom name",
                description="Name of an atom."))
        setattr(cls, "EDAM_data:1758",
            PermissibleValue(
                text="EDAM_data:1758",
                title="PDB residue name",
                description="Three-letter amino acid residue names as used in PDB files."))
        setattr(cls, "EDAM_data:1759",
            PermissibleValue(
                text="EDAM_data:1759",
                title="PDB model number",
                description="Identifier of a model structure from a PDB file."))
        setattr(cls, "EDAM_data:1771",
            PermissibleValue(
                text="EDAM_data:1771",
                title="Sequence version",
                description="Information on an molecular sequence version."))
        setattr(cls, "EDAM_data:1772",
            PermissibleValue(
                text="EDAM_data:1772",
                title="Score",
                description="""A numerical value, that is some type of scored value arising for example from a prediction method."""))
        setattr(cls, "EDAM_data:1794",
            PermissibleValue(
                text="EDAM_data:1794",
                title="Gene ID (PlasmoDB)",
                description="Identifier of a gene from PlasmoDB Plasmodium Genome Resource."))
        setattr(cls, "EDAM_data:1795",
            PermissibleValue(
                text="EDAM_data:1795",
                title="Gene ID (EcoGene)",
                description="Identifier of a gene from EcoGene Database."))
        setattr(cls, "EDAM_data:1796",
            PermissibleValue(
                text="EDAM_data:1796",
                title="Gene ID (FlyBase)",
                description="Gene identifier from FlyBase database."))
        setattr(cls, "EDAM_data:1802",
            PermissibleValue(
                text="EDAM_data:1802",
                title="Gene ID (Gramene)",
                description="Gene identifier from Gramene database."))
        setattr(cls, "EDAM_data:1803",
            PermissibleValue(
                text="EDAM_data:1803",
                title="Gene ID (Virginia microbial)",
                description="Gene identifier from Virginia Bioinformatics Institute microbial database."))
        setattr(cls, "EDAM_data:1804",
            PermissibleValue(
                text="EDAM_data:1804",
                title="Gene ID (SGN)",
                description="Gene identifier from Sol Genomics Network."))
        setattr(cls, "EDAM_data:1805",
            PermissibleValue(
                text="EDAM_data:1805",
                title="Gene ID (WormBase)",
                description="Gene identifier used by WormBase database."))
        setattr(cls, "EDAM_data:1807",
            PermissibleValue(
                text="EDAM_data:1807",
                title="ORF name",
                description="The name of an open reading frame attributed by a sequencing project."))
        setattr(cls, "EDAM_data:1855",
            PermissibleValue(
                text="EDAM_data:1855",
                title="Clone ID",
                description="An identifier of a clone (cloned molecular sequence) from a database."))
        setattr(cls, "EDAM_data:1856",
            PermissibleValue(
                text="EDAM_data:1856",
                title="PDB insertion code",
                description="""An insertion code (part of the residue number) for an amino acid residue from a PDB file."""))
        setattr(cls, "EDAM_data:1857",
            PermissibleValue(
                text="EDAM_data:1857",
                title="Atomic occupancy",
                description="""The fraction of an atom type present at a site in a molecular structure.
The sum of the occupancies of all the atom types at a site should not normally significantly exceed 1.0."""))
        setattr(cls, "EDAM_data:1858",
            PermissibleValue(
                text="EDAM_data:1858",
                title="Isotropic B factor",
                description="Isotropic B factor (atomic displacement parameter) for an atom from a PDB file."))
        setattr(cls, "EDAM_data:1859",
            PermissibleValue(
                text="EDAM_data:1859",
                title="Deletion map",
                description="""A cytogenetic map is built from a set of mutant cell lines with sub-chromosomal deletions and a reference wild-type line ('genome deletion panel'). The panel is used to map markers onto the genome by comparing mutant to wild-type banding patterns. Markers are linked (occur in the same deleted region) if they share the same banding pattern (presence or absence) as the deletion panel.
A cytogenetic map showing chromosome banding patterns in mutant cell lines relative to the wild type."""))
        setattr(cls, "EDAM_data:1860",
            PermissibleValue(
                text="EDAM_data:1860",
                title="QTL map",
                description="""A genetic map which shows the approximate location of quantitative trait loci (QTL) between two or more markers."""))
        setattr(cls, "EDAM_data:1863",
            PermissibleValue(
                text="EDAM_data:1863",
                title="Haplotype map",
                description="""A map of haplotypes in a genome or other sequence, describing common patterns of genetic variation."""))
        setattr(cls, "EDAM_data:1867",
            PermissibleValue(
                text="EDAM_data:1867",
                title="Protein fold name",
                description="The name of a protein fold."))
        setattr(cls, "EDAM_data:1868",
            PermissibleValue(
                text="EDAM_data:1868",
                title="Taxon",
                description="""For a complete list of taxonomic ranks see https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary.
The name of a group of organisms belonging to the same taxonomic rank."""))
        setattr(cls, "EDAM_data:1869",
            PermissibleValue(
                text="EDAM_data:1869",
                title="Organism identifier",
                description="A unique identifier of a (group of) organisms."))
        setattr(cls, "EDAM_data:1870",
            PermissibleValue(
                text="EDAM_data:1870",
                title="Genus name",
                description="The name of a genus of organism."))
        setattr(cls, "EDAM_data:1872",
            PermissibleValue(
                text="EDAM_data:1872",
                title="Taxonomic classification",
                description="""Name components correspond to levels in a taxonomic hierarchy (e.g. 'Genus', 'Species', etc.) Meta information such as a reference where the name was defined and a date might be included.
The full name for a group of organisms, reflecting their biological classification and (usually) conforming to a standard nomenclature."""))
        setattr(cls, "EDAM_data:1873",
            PermissibleValue(
                text="EDAM_data:1873",
                title="iHOP organism ID",
                description="A unique identifier for an organism used in the iHOP database."))
        setattr(cls, "EDAM_data:1874",
            PermissibleValue(
                text="EDAM_data:1874",
                title="Genbank common name",
                description="Common name for an organism as used in the GenBank database."))
        setattr(cls, "EDAM_data:1875",
            PermissibleValue(
                text="EDAM_data:1875",
                title="NCBI taxon",
                description="The name of a taxon from the NCBI taxonomy database."))
        setattr(cls, "EDAM_data:1881",
            PermissibleValue(
                text="EDAM_data:1881",
                title="Author ID",
                description="Information on the authors of a published work."))
        setattr(cls, "EDAM_data:1882",
            PermissibleValue(
                text="EDAM_data:1882",
                title="DragonDB author identifier",
                description="An identifier representing an author in the DragonDB database."))
        setattr(cls, "EDAM_data:1883",
            PermissibleValue(
                text="EDAM_data:1883",
                title="Annotated URI",
                description="A URI along with annotation describing the data found at the address."))
        setattr(cls, "EDAM_data:1885",
            PermissibleValue(
                text="EDAM_data:1885",
                title="Gene ID (GeneFarm)",
                description="Identifier of a gene from the GeneFarm database."))
        setattr(cls, "EDAM_data:1886",
            PermissibleValue(
                text="EDAM_data:1886",
                title="Blattner number",
                description="The blattner identifier for a gene."))
        setattr(cls, "EDAM_data:1891",
            PermissibleValue(
                text="EDAM_data:1891",
                title="iHOP symbol",
                description="A unique identifier of a protein or gene used in the iHOP database."))
        setattr(cls, "EDAM_data:1893",
            PermissibleValue(
                text="EDAM_data:1893",
                title="Locus ID",
                description="""A unique name or other identifier of a genetic locus, typically conforming to a scheme that names loci (such as predicted genes) depending on their position in a molecular sequence, for example a completely sequenced genome or chromosome."""))
        setattr(cls, "EDAM_data:1895",
            PermissibleValue(
                text="EDAM_data:1895",
                title="Locus ID (AGI)",
                description="Locus identifier for Arabidopsis Genome Initiative (TAIR, TIGR and MIPS databases)."))
        setattr(cls, "EDAM_data:1896",
            PermissibleValue(
                text="EDAM_data:1896",
                title="Locus ID (ASPGD)",
                description="Identifier for loci from ASPGD (Aspergillus Genome Database)."))
        setattr(cls, "EDAM_data:1897",
            PermissibleValue(
                text="EDAM_data:1897",
                title="Locus ID (MGG)",
                description="Identifier for loci from Magnaporthe grisea Database at the Broad Institute."))
        setattr(cls, "EDAM_data:1898",
            PermissibleValue(
                text="EDAM_data:1898",
                title="Locus ID (CGD)",
                description="Identifier for loci from CGD (Candida Genome Database)."))
        setattr(cls, "EDAM_data:1899",
            PermissibleValue(
                text="EDAM_data:1899",
                title="Locus ID (CMR)",
                description="""Locus identifier for Comprehensive Microbial Resource at the J. Craig Venter Institute."""))
        setattr(cls, "EDAM_data:1900",
            PermissibleValue(
                text="EDAM_data:1900",
                title="NCBI locus tag",
                description="Identifier for loci from NCBI database."))
        setattr(cls, "EDAM_data:1901",
            PermissibleValue(
                text="EDAM_data:1901",
                title="Locus ID (SGD)",
                description="Identifier for loci from SGD (Saccharomyces Genome Database)."))
        setattr(cls, "EDAM_data:1902",
            PermissibleValue(
                text="EDAM_data:1902",
                title="Locus ID (MMP)",
                description="Identifier of loci from Maize Mapping Project."))
        setattr(cls, "EDAM_data:1903",
            PermissibleValue(
                text="EDAM_data:1903",
                title="Locus ID (DictyBase)",
                description="Identifier of locus from DictyBase (Dictyostelium discoideum)."))
        setattr(cls, "EDAM_data:1904",
            PermissibleValue(
                text="EDAM_data:1904",
                title="Locus ID (EntrezGene)",
                description="Identifier of a locus from EntrezGene database."))
        setattr(cls, "EDAM_data:1905",
            PermissibleValue(
                text="EDAM_data:1905",
                title="Locus ID (MaizeGDB)",
                description="Identifier of locus from MaizeGDB (Maize genome database)."))
        setattr(cls, "EDAM_data:1907",
            PermissibleValue(
                text="EDAM_data:1907",
                title="Gene ID (KOME)",
                description="Identifier of a gene from the KOME database."))
        setattr(cls, "EDAM_data:1908",
            PermissibleValue(
                text="EDAM_data:1908",
                title="Locus ID (Tropgene)",
                description="Identifier of a locus from the Tropgene database."))
        setattr(cls, "EDAM_data:1916",
            PermissibleValue(
                text="EDAM_data:1916",
                title="Alignment",
                description="An alignment of molecular sequences, structures or profiles derived from them."))
        setattr(cls, "EDAM_data:1917",
            PermissibleValue(
                text="EDAM_data:1917",
                title="Atomic property",
                description="Data for an atom (in a molecular structure)."))
        setattr(cls, "EDAM_data:2007",
            PermissibleValue(
                text="EDAM_data:2007",
                title="UniProt keyword",
                description="""A word or phrase that can appear in the keywords field (KW line) of entries from the UniProt database."""))
        setattr(cls, "EDAM_data:2012",
            PermissibleValue(
                text="EDAM_data:2012",
                title="Sequence coordinates",
                description="""A position in a map (for example a genetic map), either a single position (point) or a region / interval.
This includes positions in genomes based on a reference sequence. A position may be specified for any mappable object, i.e. anything that may have positional information such as a physical position in a chromosome. Data might include sequence region name, strand, coordinate system name, assembly name, start position and end position."""))
        setattr(cls, "EDAM_data:2016",
            PermissibleValue(
                text="EDAM_data:2016",
                title="Amino acid property",
                description="""Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all amino acids."""))
        setattr(cls, "EDAM_data:2019",
            PermissibleValue(
                text="EDAM_data:2019",
                title="Map data",
                description="""Data describing a molecular map (genetic or physical) or a set of such maps, including various attributes of, data extracted from or derived from the analysis of them, but excluding the map(s) themselves. This includes metadata for map sets that share a common set of features which are mapped."""))
        setattr(cls, "EDAM_data:2024",
            PermissibleValue(
                text="EDAM_data:2024",
                title="Enzyme kinetics data",
                description="""Data concerning chemical reaction(s) catalysed by enzyme(s).
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2025",
            PermissibleValue(
                text="EDAM_data:2025",
                title="Michaelis Menten plot",
                description="""A plot giving an approximation of the kinetics of an enzyme-catalysed reaction, assuming simple kinetics (i.e. no intermediate or product inhibition, allostericity or cooperativity). It plots initial reaction rate to the substrate concentration (S) from which the maximum rate (vmax) is apparent."""))
        setattr(cls, "EDAM_data:2026",
            PermissibleValue(
                text="EDAM_data:2026",
                title="Hanes Woolf plot",
                description="""A plot based on the Michaelis Menten equation of enzyme kinetics plotting the ratio of the initial substrate concentration (S) against the reaction velocity (v)."""))
        setattr(cls, "EDAM_data:2042",
            PermissibleValue(
                text="EDAM_data:2042",
                title="Evidence",
                description="""Typically a human-readable summary of body of facts or information indicating why a statement is true or valid. This may include a computational prediction, laboratory experiment, literature reference etc."""))
        setattr(cls, "EDAM_data:2044",
            PermissibleValue(
                text="EDAM_data:2044",
                title="Sequence",
                description="""One or more molecular sequences, possibly with associated annotation.
This concept is a placeholder of concepts for primary sequence data including raw sequences and sequence records. It should not normally be used for derivatives such as sequence alignments, motifs or profiles."""))
        setattr(cls, "EDAM_data:2048",
            PermissibleValue(
                text="EDAM_data:2048",
                title="Report",
                description="""A human-readable collection of information including annotation on a biological entity or phenomena, computer-generated reports of analysis of primary data (e.g. sequence or structural), and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
You can use this term by default for any textual report, in case you can't find another, more specific term. Reports may be generated automatically or collated by hand and can include metadata on the origin, source, history, ownership or location of some thing."""))
        setattr(cls, "EDAM_data:2050",
            PermissibleValue(
                text="EDAM_data:2050",
                title="Molecular property (general)",
                description="General data for a molecule."))
        setattr(cls, "EDAM_data:2070",
            PermissibleValue(
                text="EDAM_data:2070",
                title="Sequence motif (nucleic acid)",
                description="A nucleotide sequence motif."))
        setattr(cls, "EDAM_data:2071",
            PermissibleValue(
                text="EDAM_data:2071",
                title="Sequence motif (protein)",
                description="An amino acid sequence motif."))
        setattr(cls, "EDAM_data:2080",
            PermissibleValue(
                text="EDAM_data:2080",
                title="Database search results",
                description="A report of hits from searching a database of some type."))
        setattr(cls, "EDAM_data:2082",
            PermissibleValue(
                text="EDAM_data:2082",
                title="Matrix",
                description="""An array of numerical values.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2084",
            PermissibleValue(
                text="EDAM_data:2084",
                title="Nucleic acid report",
                description="""A human-readable collection of information about one or more specific nucleic acid molecules."""))
        setattr(cls, "EDAM_data:2085",
            PermissibleValue(
                text="EDAM_data:2085",
                title="Structure report",
                description="""A human-readable collection of information about one or more molecular tertiary (3D) structures. It might include annotation on the structure, a computer-generated report of analysis of structural data, and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself."""))
        setattr(cls, "EDAM_data:2087",
            PermissibleValue(
                text="EDAM_data:2087",
                title="Molecular property",
                description="""A report on the physical (e.g. structural) or chemical properties of molecules, or parts of a molecule."""))
        setattr(cls, "EDAM_data:2088",
            PermissibleValue(
                text="EDAM_data:2088",
                title="DNA base structural data",
                description="Structural data for DNA base pairs or runs of bases, such as energy or angle data."))
        setattr(cls, "EDAM_data:2091",
            PermissibleValue(
                text="EDAM_data:2091",
                title="Accession",
                description="""A persistent (stable) and unique identifier, typically identifying an object (entry) from a database."""))
        setattr(cls, "EDAM_data:2093",
            PermissibleValue(
                text="EDAM_data:2093",
                title="Data reference",
                description="""A list of database accessions or identifiers are usually included.
Reference to a dataset (or a cross-reference between two datasets), typically one or more entries in a biological database or ontology."""))
        setattr(cls, "EDAM_data:2098",
            PermissibleValue(
                text="EDAM_data:2098",
                title="Job identifier",
                description="An identifier of a submitted job."))
        setattr(cls, "EDAM_data:2099",
            PermissibleValue(
                text="EDAM_data:2099",
                title="Name",
                description="A name of a thing, which need not necessarily uniquely identify it."))
        setattr(cls, "EDAM_data:2101",
            PermissibleValue(
                text="EDAM_data:2101",
                title="Account authentication",
                description="""Authentication data usually used to log in into an account on an information system such as a web application or a database."""))
        setattr(cls, "EDAM_data:2102",
            PermissibleValue(
                text="EDAM_data:2102",
                title="KEGG organism code",
                description="A three-letter code used in the KEGG databases to uniquely identify organisms."))
        setattr(cls, "EDAM_data:2104",
            PermissibleValue(
                text="EDAM_data:2104",
                title="BioCyc ID",
                description="Identifier of an object from one of the BioCyc databases."))
        setattr(cls, "EDAM_data:2105",
            PermissibleValue(
                text="EDAM_data:2105",
                title="Compound ID (BioCyc)",
                description="Identifier of a compound from the BioCyc chemical compounds database."))
        setattr(cls, "EDAM_data:2106",
            PermissibleValue(
                text="EDAM_data:2106",
                title="Reaction ID (BioCyc)",
                description="Identifier of a biological reaction from the BioCyc reactions database."))
        setattr(cls, "EDAM_data:2107",
            PermissibleValue(
                text="EDAM_data:2107",
                title="Enzyme ID (BioCyc)",
                description="Identifier of an enzyme from the BioCyc enzymes database."))
        setattr(cls, "EDAM_data:2108",
            PermissibleValue(
                text="EDAM_data:2108",
                title="Reaction ID",
                description="Identifier of a biological reaction from a database."))
        setattr(cls, "EDAM_data:2109",
            PermissibleValue(
                text="EDAM_data:2109",
                title="Identifier (hybrid)",
                description="""An identifier that is re-used for data objects of fundamentally different types (typically served from a single database).
This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'."""))
        setattr(cls, "EDAM_data:2110",
            PermissibleValue(
                text="EDAM_data:2110",
                title="Molecular property identifier",
                description="Identifier of a molecular property."))
        setattr(cls, "EDAM_data:2111",
            PermissibleValue(
                text="EDAM_data:2111",
                title="Codon usage table ID",
                description="Identifier of a codon usage table, for example a genetic code."))
        setattr(cls, "EDAM_data:2112",
            PermissibleValue(
                text="EDAM_data:2112",
                title="FlyBase primary identifier",
                description="Primary identifier of an object from the FlyBase database."))
        setattr(cls, "EDAM_data:2113",
            PermissibleValue(
                text="EDAM_data:2113",
                title="WormBase identifier",
                description="Identifier of an object from the WormBase database."))
        setattr(cls, "EDAM_data:2114",
            PermissibleValue(
                text="EDAM_data:2114",
                title="WormBase wormpep ID",
                description="Protein identifier used by WormBase database."))
        setattr(cls, "EDAM_data:2117",
            PermissibleValue(
                text="EDAM_data:2117",
                title="Map identifier",
                description="An identifier of a map of a molecular sequence."))
        setattr(cls, "EDAM_data:2118",
            PermissibleValue(
                text="EDAM_data:2118",
                title="Person identifier",
                description="""An identifier of a software end-user on a website or a database (typically a person or an entity)."""))
        setattr(cls, "EDAM_data:2119",
            PermissibleValue(
                text="EDAM_data:2119",
                title="Nucleic acid identifier",
                description="Name or other identifier of a nucleic acid molecule."))
        setattr(cls, "EDAM_data:2127",
            PermissibleValue(
                text="EDAM_data:2127",
                title="Genetic code identifier",
                description="An identifier of a genetic code."))
        setattr(cls, "EDAM_data:2128",
            PermissibleValue(
                text="EDAM_data:2128",
                title="Genetic code name",
                description="Informal name for a genetic code, typically an organism name."))
        setattr(cls, "EDAM_data:2129",
            PermissibleValue(
                text="EDAM_data:2129",
                title="File format name",
                description="Name of a file format such as HTML, PNG, PDF, EMBL, GenBank and so on."))
        setattr(cls, "EDAM_data:2131",
            PermissibleValue(
                text="EDAM_data:2131",
                title="Operating system name",
                description="Name of a computer operating system such as Linux, PC or Mac."))
        setattr(cls, "EDAM_data:2133",
            PermissibleValue(
                text="EDAM_data:2133",
                title="Logical operator",
                description="A logical operator such as OR, AND, XOR, and NOT."))
        setattr(cls, "EDAM_data:2137",
            PermissibleValue(
                text="EDAM_data:2137",
                title="Gap penalty",
                description="A penalty for introducing or extending a gap in an alignment."))
        setattr(cls, "EDAM_data:2139",
            PermissibleValue(
                text="EDAM_data:2139",
                title="Nucleic acid melting temperature",
                description="""A temperature concerning nucleic acid denaturation, typically the temperature at which the two strands of a hybridised or double stranded nucleic acid (DNA or RNA/DNA) molecule separate."""))
        setattr(cls, "EDAM_data:2140",
            PermissibleValue(
                text="EDAM_data:2140",
                title="Concentration",
                description="The concentration of a chemical compound."))
        setattr(cls, "EDAM_data:2154",
            PermissibleValue(
                text="EDAM_data:2154",
                title="Sequence name",
                description="Any arbitrary name of a molecular sequence."))
        setattr(cls, "EDAM_data:2160",
            PermissibleValue(
                text="EDAM_data:2160",
                title="Fickett testcode plot",
                description="""A plot of Fickett testcode statistic (identifying protein coding regions) in a nucleotide sequences."""))
        setattr(cls, "EDAM_data:2161",
            PermissibleValue(
                text="EDAM_data:2161",
                title="Sequence similarity plot",
                description="""A plot of sequence similarities identified from word-matching or character comparison.
Use this concept for calculated substitution rates, relative site variability, data on sites with biased properties, highly conserved or very poorly conserved sites, regions, blocks etc."""))
        setattr(cls, "EDAM_data:2162",
            PermissibleValue(
                text="EDAM_data:2162",
                title="Helical wheel",
                description="""An image of peptide sequence sequence looking down the axis of the helix for highlighting amphipathicity and other properties."""))
        setattr(cls, "EDAM_data:2163",
            PermissibleValue(
                text="EDAM_data:2163",
                title="Helical net",
                description="""An image of peptide sequence sequence in a simple 3,4,3,4 repeating pattern that emulates at a simple level the arrangement of residues around an alpha helix.
Useful for highlighting amphipathicity and other properties."""))
        setattr(cls, "EDAM_data:2165",
            PermissibleValue(
                text="EDAM_data:2165",
                title="Protein ionisation curve",
                description="A plot of pK versus pH for a protein."))
        setattr(cls, "EDAM_data:2166",
            PermissibleValue(
                text="EDAM_data:2166",
                title="Sequence composition plot",
                description="A plot of character or word composition / frequency of a molecular sequence."))
        setattr(cls, "EDAM_data:2167",
            PermissibleValue(
                text="EDAM_data:2167",
                title="Nucleic acid density plot",
                description="Density plot (of base composition) for a nucleotide sequence."))
        setattr(cls, "EDAM_data:2168",
            PermissibleValue(
                text="EDAM_data:2168",
                title="Sequence trace image",
                description="""Image of a sequence trace (nucleotide sequence versus probabilities of each of the 4 bases)."""))
        setattr(cls, "EDAM_data:2174",
            PermissibleValue(
                text="EDAM_data:2174",
                title="FlyBase secondary identifier",
                description="""Secondary identifier are used to handle entries that were merged with or split from other entries in the database.
Secondary identifier of an object from the FlyBase database."""))
        setattr(cls, "EDAM_data:2190",
            PermissibleValue(
                text="EDAM_data:2190",
                title="Sequence checksum",
                description="""A fixed-size datum calculated (by using a hash function) for a molecular sequence, typically for purposes of error detection or indexing."""))
        setattr(cls, "EDAM_data:2193",
            PermissibleValue(
                text="EDAM_data:2193",
                title="Database entry metadata",
                description="Basic information on any arbitrary database entry."))
        setattr(cls, "EDAM_data:2208",
            PermissibleValue(
                text="EDAM_data:2208",
                title="Plasmid identifier",
                description="An identifier of a plasmid in a database."))
        setattr(cls, "EDAM_data:2209",
            PermissibleValue(
                text="EDAM_data:2209",
                title="Mutation ID",
                description="A unique identifier of a specific mutation catalogued in a database."))
        setattr(cls, "EDAM_data:2216",
            PermissibleValue(
                text="EDAM_data:2216",
                title="Codon number",
                description="The number of a codon, for instance, at which a mutation is located."))
        setattr(cls, "EDAM_data:2219",
            PermissibleValue(
                text="EDAM_data:2219",
                title="Database field name",
                description="The name of a field in a database."))
        setattr(cls, "EDAM_data:2220",
            PermissibleValue(
                text="EDAM_data:2220",
                title="Sequence cluster ID (SYSTERS)",
                description="Unique identifier of a sequence cluster from the SYSTERS database."))
        setattr(cls, "EDAM_data:2223",
            PermissibleValue(
                text="EDAM_data:2223",
                title="Ontology metadata",
                description="Data concerning a biological ontology."))
        setattr(cls, "EDAM_data:2253",
            PermissibleValue(
                text="EDAM_data:2253",
                title="Data resource definition name",
                description="The name of a data type."))
        setattr(cls, "EDAM_data:2254",
            PermissibleValue(
                text="EDAM_data:2254",
                title="OBO file format name",
                description="Name of an OBO file format such as OBO-XML, plain and so on."))
        setattr(cls, "EDAM_data:2285",
            PermissibleValue(
                text="EDAM_data:2285",
                title="Gene ID (MIPS)",
                description="Identifier for genetic elements in MIPS database."))
        setattr(cls, "EDAM_data:2290",
            PermissibleValue(
                text="EDAM_data:2290",
                title="EMBL accession",
                description="An accession number of an entry from the EMBL sequence database."))
        setattr(cls, "EDAM_data:2291",
            PermissibleValue(
                text="EDAM_data:2291",
                title="UniProt ID",
                description="An identifier of a polypeptide in the UniProt database."))
        setattr(cls, "EDAM_data:2292",
            PermissibleValue(
                text="EDAM_data:2292",
                title="GenBank accession",
                description="Accession number of an entry from the GenBank sequence database."))
        setattr(cls, "EDAM_data:2293",
            PermissibleValue(
                text="EDAM_data:2293",
                title="Gramene secondary identifier",
                description="Secondary (internal) identifier of a Gramene database entry."))
        setattr(cls, "EDAM_data:2294",
            PermissibleValue(
                text="EDAM_data:2294",
                title="Sequence variation ID",
                description="An identifier of an entry from a database of molecular sequence variation."))
        setattr(cls, "EDAM_data:2295",
            PermissibleValue(
                text="EDAM_data:2295",
                title="Gene ID",
                description="""A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol."""))
        setattr(cls, "EDAM_data:2297",
            PermissibleValue(
                text="EDAM_data:2297",
                title="Gene ID (ECK)",
                description="Identifier of an E. coli K-12 gene from EcoGene Database."))
        setattr(cls, "EDAM_data:2298",
            PermissibleValue(
                text="EDAM_data:2298",
                title="Gene ID (HGNC)",
                description="Identifier for a gene approved by the HUGO Gene Nomenclature Committee."))
        setattr(cls, "EDAM_data:2299",
            PermissibleValue(
                text="EDAM_data:2299",
                title="Gene name",
                description="""The name of a gene, (typically) assigned by a person and/or according to a naming scheme. It may contain white space characters and is typically more intuitive and readable than a gene symbol. It (typically) may be used to identify similar genes in different species and to derive a gene symbol."""))
        setattr(cls, "EDAM_data:2301",
            PermissibleValue(
                text="EDAM_data:2301",
                title="SMILES string",
                description="A specification of a chemical structure in SMILES format."))
        setattr(cls, "EDAM_data:2302",
            PermissibleValue(
                text="EDAM_data:2302",
                title="STRING ID",
                description="""Unique identifier of an entry from the STRING database of protein-protein interactions."""))
        setattr(cls, "EDAM_data:2309",
            PermissibleValue(
                text="EDAM_data:2309",
                title="Reaction ID (SABIO-RK)",
                description="Identifier of a biological reaction from the SABIO-RK reactions database."))
        setattr(cls, "EDAM_data:2313",
            PermissibleValue(
                text="EDAM_data:2313",
                title="Carbohydrate report",
                description="""A human-readable collection of information about one or more specific carbohydrate 3D structure(s)."""))
        setattr(cls, "EDAM_data:2314",
            PermissibleValue(
                text="EDAM_data:2314",
                title="GI number",
                description="""A series of digits that are assigned consecutively to each sequence record processed by NCBI. The GI number bears no resemblance to the Accession number of the sequence record.
Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record."""))
        setattr(cls, "EDAM_data:2315",
            PermissibleValue(
                text="EDAM_data:2315",
                title="NCBI version",
                description="""An identifier assigned to sequence records processed by NCBI, made of the accession number of the database record followed by a dot and a version number.
Nucleotide sequence version contains two letters followed by six digits, a dot, and a version number (or for older nucleotide sequence records, the format is one letter followed by five digits, a dot, and a version number). Protein sequence version contains three letters followed by five digits, a dot, and a version number."""))
        setattr(cls, "EDAM_data:2316",
            PermissibleValue(
                text="EDAM_data:2316",
                title="Cell line name",
                description="The name of a cell line."))
        setattr(cls, "EDAM_data:2317",
            PermissibleValue(
                text="EDAM_data:2317",
                title="Cell line name (exact)",
                description="The exact name of a cell line."))
        setattr(cls, "EDAM_data:2318",
            PermissibleValue(
                text="EDAM_data:2318",
                title="Cell line name (truncated)",
                description="The truncated name of a cell line."))
        setattr(cls, "EDAM_data:2319",
            PermissibleValue(
                text="EDAM_data:2319",
                title="Cell line name (no punctuation)",
                description="The name of a cell line without any punctuation."))
        setattr(cls, "EDAM_data:2320",
            PermissibleValue(
                text="EDAM_data:2320",
                title="Cell line name (assonant)",
                description="The assonant name of a cell line."))
        setattr(cls, "EDAM_data:2321",
            PermissibleValue(
                text="EDAM_data:2321",
                title="Enzyme ID",
                description="A unique, persistent identifier of an enzyme."))
        setattr(cls, "EDAM_data:2325",
            PermissibleValue(
                text="EDAM_data:2325",
                title="REBASE enzyme number",
                description="Identifier of an enzyme from the REBASE enzymes database."))
        setattr(cls, "EDAM_data:2326",
            PermissibleValue(
                text="EDAM_data:2326",
                title="DrugBank ID",
                description="Unique identifier of a drug from the DrugBank database."))
        setattr(cls, "EDAM_data:2327",
            PermissibleValue(
                text="EDAM_data:2327",
                title="GI number (protein)",
                description="""A unique identifier assigned to NCBI protein sequence records.
Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record."""))
        setattr(cls, "EDAM_data:2335",
            PermissibleValue(
                text="EDAM_data:2335",
                title="Bit score",
                description="""A score derived from the alignment of two sequences, which is then normalised with respect to the scoring system.
Bit scores are normalised with respect to the scoring system and therefore can be used to compare alignment scores from different searches."""))
        setattr(cls, "EDAM_data:2337",
            PermissibleValue(
                text="EDAM_data:2337",
                title="Resource metadata",
                description="""Data concerning or describing some core computational resource, as distinct from primary data. This includes metadata on the origin, source, history, ownership or location of some thing.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2338",
            PermissibleValue(
                text="EDAM_data:2338",
                title="Ontology identifier",
                description="Any arbitrary identifier of an ontology."))
        setattr(cls, "EDAM_data:2339",
            PermissibleValue(
                text="EDAM_data:2339",
                title="Ontology concept name",
                description="The name of a concept in an ontology."))
        setattr(cls, "EDAM_data:2340",
            PermissibleValue(
                text="EDAM_data:2340",
                title="Genome build identifier",
                description="An identifier of a build of a particular genome."))
        setattr(cls, "EDAM_data:2342",
            PermissibleValue(
                text="EDAM_data:2342",
                title="Pathway or network name",
                description="The name of a biological pathway or network."))
        setattr(cls, "EDAM_data:2343",
            PermissibleValue(
                text="EDAM_data:2343",
                title="Pathway ID (KEGG)",
                description="Identifier of a pathway from the KEGG pathway database."))
        setattr(cls, "EDAM_data:2344",
            PermissibleValue(
                text="EDAM_data:2344",
                title="Pathway ID (NCI-Nature)",
                description="Identifier of a pathway from the NCI-Nature pathway database."))
        setattr(cls, "EDAM_data:2345",
            PermissibleValue(
                text="EDAM_data:2345",
                title="Pathway ID (ConsensusPathDB)",
                description="Identifier of a pathway from the ConsensusPathDB pathway database."))
        setattr(cls, "EDAM_data:2346",
            PermissibleValue(
                text="EDAM_data:2346",
                title="Sequence cluster ID (UniRef)",
                description="Unique identifier of an entry from the UniRef database."))
        setattr(cls, "EDAM_data:2347",
            PermissibleValue(
                text="EDAM_data:2347",
                title="Sequence cluster ID (UniRef100)",
                description="Unique identifier of an entry from the UniRef100 database."))
        setattr(cls, "EDAM_data:2348",
            PermissibleValue(
                text="EDAM_data:2348",
                title="Sequence cluster ID (UniRef90)",
                description="Unique identifier of an entry from the UniRef90 database."))
        setattr(cls, "EDAM_data:2349",
            PermissibleValue(
                text="EDAM_data:2349",
                title="Sequence cluster ID (UniRef50)",
                description="Unique identifier of an entry from the UniRef50 database."))
        setattr(cls, "EDAM_data:2353",
            PermissibleValue(
                text="EDAM_data:2353",
                title="Ontology data",
                description="""Data concerning or derived from an ontology.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2354",
            PermissibleValue(
                text="EDAM_data:2354",
                title="RNA family report",
                description="""A human-readable collection of information about a specific RNA family or other group of classified RNA sequences."""))
        setattr(cls, "EDAM_data:2355",
            PermissibleValue(
                text="EDAM_data:2355",
                title="RNA family identifier",
                description="""Identifier of an RNA family, typically an entry from a RNA sequence classification database."""))
        setattr(cls, "EDAM_data:2356",
            PermissibleValue(
                text="EDAM_data:2356",
                title="RFAM accession",
                description="Stable accession number of an entry (RNA family) from the RFAM database."))
        setattr(cls, "EDAM_data:2362",
            PermissibleValue(
                text="EDAM_data:2362",
                title="Sequence accession (hybrid)",
                description="Accession number of a nucleotide or protein sequence database entry."))
        setattr(cls, "EDAM_data:2365",
            PermissibleValue(
                text="EDAM_data:2365",
                title="Pathway or network accession",
                description="""A persistent, unique identifier of a biological pathway or network (typically a database entry)."""))
        setattr(cls, "EDAM_data:2366",
            PermissibleValue(
                text="EDAM_data:2366",
                title="Secondary structure alignment",
                description="Alignment of the (1D representations of) secondary structure of two or more molecules."))
        setattr(cls, "EDAM_data:2367",
            PermissibleValue(
                text="EDAM_data:2367",
                title="ASTD ID",
                description="Identifier of an object from the ASTD database."))
        setattr(cls, "EDAM_data:2368",
            PermissibleValue(
                text="EDAM_data:2368",
                title="ASTD ID (exon)",
                description="Identifier of an exon from the ASTD database."))
        setattr(cls, "EDAM_data:2369",
            PermissibleValue(
                text="EDAM_data:2369",
                title="ASTD ID (intron)",
                description="Identifier of an intron from the ASTD database."))
        setattr(cls, "EDAM_data:2370",
            PermissibleValue(
                text="EDAM_data:2370",
                title="ASTD ID (polya)",
                description="Identifier of a polyA signal from the ASTD database."))
        setattr(cls, "EDAM_data:2371",
            PermissibleValue(
                text="EDAM_data:2371",
                title="ASTD ID (tss)",
                description="Identifier of a transcription start site from the ASTD database."))
        setattr(cls, "EDAM_data:2373",
            PermissibleValue(
                text="EDAM_data:2373",
                title="Spot ID",
                description="Unique identifier of a spot from a two-dimensional (protein) gel."))
        setattr(cls, "EDAM_data:2374",
            PermissibleValue(
                text="EDAM_data:2374",
                title="Spot serial number",
                description="""Unique identifier of a spot from a two-dimensional (protein) gel in the SWISS-2DPAGE database."""))
        setattr(cls, "EDAM_data:2375",
            PermissibleValue(
                text="EDAM_data:2375",
                title="Spot ID (HSC-2DPAGE)",
                description="""Unique identifier of a spot from a two-dimensional (protein) gel from a HSC-2DPAGE database."""))
        setattr(cls, "EDAM_data:2379",
            PermissibleValue(
                text="EDAM_data:2379",
                title="Strain identifier",
                description="Identifier of a strain of an organism variant, typically a plant, virus or bacterium."))
        setattr(cls, "EDAM_data:2380",
            PermissibleValue(
                text="EDAM_data:2380",
                title="CABRI accession",
                description="A unique identifier of an item from the CABRI database."))
        setattr(cls, "EDAM_data:2382",
            PermissibleValue(
                text="EDAM_data:2382",
                title="Genotype experiment ID",
                description="Identifier of an entry from a database of genotype experiment metadata."))
        setattr(cls, "EDAM_data:2383",
            PermissibleValue(
                text="EDAM_data:2383",
                title="EGA accession",
                description="Identifier of an entry from the EGA database."))
        setattr(cls, "EDAM_data:2384",
            PermissibleValue(
                text="EDAM_data:2384",
                title="IPI protein ID",
                description="""Identifier of a protein entry catalogued in the International Protein Index (IPI) database."""))
        setattr(cls, "EDAM_data:2385",
            PermissibleValue(
                text="EDAM_data:2385",
                title="RefSeq accession (protein)",
                description="Accession number of a protein from the RefSeq database."))
        setattr(cls, "EDAM_data:2386",
            PermissibleValue(
                text="EDAM_data:2386",
                title="EPD ID",
                description="Identifier of an entry (promoter) from the EPD database."))
        setattr(cls, "EDAM_data:2387",
            PermissibleValue(
                text="EDAM_data:2387",
                title="TAIR accession",
                description="Identifier of an entry from the TAIR database."))
        setattr(cls, "EDAM_data:2388",
            PermissibleValue(
                text="EDAM_data:2388",
                title="TAIR accession (At gene)",
                description="Identifier of an Arabidopsis thaliana gene from the TAIR database."))
        setattr(cls, "EDAM_data:2389",
            PermissibleValue(
                text="EDAM_data:2389",
                title="UniSTS accession",
                description="Identifier of an entry from the UniSTS database."))
        setattr(cls, "EDAM_data:2390",
            PermissibleValue(
                text="EDAM_data:2390",
                title="UNITE accession",
                description="Identifier of an entry from the UNITE database."))
        setattr(cls, "EDAM_data:2391",
            PermissibleValue(
                text="EDAM_data:2391",
                title="UTR accession",
                description="Identifier of an entry from the UTR database."))
        setattr(cls, "EDAM_data:2392",
            PermissibleValue(
                text="EDAM_data:2392",
                title="UniParc accession",
                description="Accession number of a UniParc (protein sequence) database entry."))
        setattr(cls, "EDAM_data:2393",
            PermissibleValue(
                text="EDAM_data:2393",
                title="mFLJ/mKIAA number",
                description="Identifier of an entry from the Rouge or HUGE databases."))
        setattr(cls, "EDAM_data:2398",
            PermissibleValue(
                text="EDAM_data:2398",
                title="Ensembl protein ID",
                description="Unique identifier for a protein from the Ensembl database."))
        setattr(cls, "EDAM_data:2523",
            PermissibleValue(
                text="EDAM_data:2523",
                title="Phylogenetic data",
                description="""Data concerning phylogeny, typically of molecular sequences, including reports of information concerning or derived from a phylogenetic tree, or from comparing two or more phylogenetic trees.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2526",
            PermissibleValue(
                text="EDAM_data:2526",
                title="Text data",
                description="""Data concerning, extracted from, or derived from the analysis of a scientific text (or texts) such as a full text article from a scientific journal.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation. It includes concepts that are best described as scientific text or closely concerned with or derived from text."""))
        setattr(cls, "EDAM_data:2530",
            PermissibleValue(
                text="EDAM_data:2530",
                title="Organism report",
                description="A human-readable collection of information about a specific organism."))
        setattr(cls, "EDAM_data:2531",
            PermissibleValue(
                text="EDAM_data:2531",
                title="Protocol",
                description="""A human-readable collection of information about about how a scientific experiment or analysis was carried out that results in a specific set of data or results used for further analysis or to test a specific hypothesis."""))
        setattr(cls, "EDAM_data:2534",
            PermissibleValue(
                text="EDAM_data:2534",
                title="Sequence attribute",
                description="An attribute of a molecular sequence, possibly in reference to some other sequence."))
        setattr(cls, "EDAM_data:2535",
            PermissibleValue(
                text="EDAM_data:2535",
                title="Sequence tag profile",
                description="""Output from a serial analysis of gene expression (SAGE), massively parallel signature sequencing (MPSS) or sequencing by synthesis (SBS) experiment. In all cases this is a list of short sequence tags and the number of times it is observed.
SAGE, MPSS and SBS experiments are usually performed to study gene expression. The sequence tags are typically subsequently annotated (after a database search) with the mRNA (and therefore gene) the tag was extracted from.
This includes tag to gene assignments (tag mapping) of SAGE, MPSS and SBS data. Typically this is the sequencing-based expression profile annotated with gene identifiers."""))
        setattr(cls, "EDAM_data:2536",
            PermissibleValue(
                text="EDAM_data:2536",
                title="Mass spectrometry data",
                description="Data concerning a mass spectrometry measurement."))
        setattr(cls, "EDAM_data:2537",
            PermissibleValue(
                text="EDAM_data:2537",
                title="Protein structure raw data",
                description="""Raw data from experimental methods for determining protein structure.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation."""))
        setattr(cls, "EDAM_data:2538",
            PermissibleValue(
                text="EDAM_data:2538",
                title="Mutation identifier",
                description="An identifier of a mutation."))
        setattr(cls, "EDAM_data:2563",
            PermissibleValue(
                text="EDAM_data:2563",
                title="Amino acid name (single letter)",
                description="Single letter amino acid identifier, e.g. G."))
        setattr(cls, "EDAM_data:2564",
            PermissibleValue(
                text="EDAM_data:2564",
                title="Amino acid name (three letter)",
                description="Three letter amino acid identifier, e.g. GLY."))
        setattr(cls, "EDAM_data:2565",
            PermissibleValue(
                text="EDAM_data:2565",
                title="Amino acid name (full name)",
                description="Full name of an amino acid, e.g. Glycine."))
        setattr(cls, "EDAM_data:2576",
            PermissibleValue(
                text="EDAM_data:2576",
                title="Toxin identifier",
                description="Identifier of a toxin."))
        setattr(cls, "EDAM_data:2578",
            PermissibleValue(
                text="EDAM_data:2578",
                title="ArachnoServer ID",
                description="Unique identifier of a toxin from the ArachnoServer database."))
        setattr(cls, "EDAM_data:2580",
            PermissibleValue(
                text="EDAM_data:2580",
                title="BindingDB Monomer ID",
                description="Unique identifier of a monomer from the BindingDB database."))
        setattr(cls, "EDAM_data:2582",
            PermissibleValue(
                text="EDAM_data:2582",
                title="GO concept ID (biological process)",
                description="An identifier of a 'biological process' concept from the the Gene Ontology."))
        setattr(cls, "EDAM_data:2583",
            PermissibleValue(
                text="EDAM_data:2583",
                title="GO concept ID (molecular function)",
                description="An identifier of a 'molecular function' concept from the the Gene Ontology."))
        setattr(cls, "EDAM_data:2586",
            PermissibleValue(
                text="EDAM_data:2586",
                title="Northern blot image",
                description="An image arising from a Northern Blot experiment."))
        setattr(cls, "EDAM_data:2587",
            PermissibleValue(
                text="EDAM_data:2587",
                title="Blot ID",
                description="Unique identifier of a blot from a Northern Blot."))
        setattr(cls, "EDAM_data:2588",
            PermissibleValue(
                text="EDAM_data:2588",
                title="BlotBase blot ID",
                description="Unique identifier of a blot from a Northern Blot from the BlotBase database."))
        setattr(cls, "EDAM_data:2589",
            PermissibleValue(
                text="EDAM_data:2589",
                title="Hierarchy",
                description="""Raw data on a biological hierarchy, describing the hierarchy proper, hierarchy components and possibly associated annotation."""))
        setattr(cls, "EDAM_data:2591",
            PermissibleValue(
                text="EDAM_data:2591",
                title="Brite hierarchy ID",
                description="Identifier of an entry from the Brite database of biological hierarchies."))
        setattr(cls, "EDAM_data:2593",
            PermissibleValue(
                text="EDAM_data:2593",
                title="BRENDA organism ID",
                description="A unique identifier for an organism used in the BRENDA database."))
        setattr(cls, "EDAM_data:2594",
            PermissibleValue(
                text="EDAM_data:2594",
                title="UniGene taxon",
                description="The name of a taxon using the controlled vocabulary of the UniGene database."))
        setattr(cls, "EDAM_data:2595",
            PermissibleValue(
                text="EDAM_data:2595",
                title="UTRdb taxon",
                description="The name of a taxon using the controlled vocabulary of the UTRdb database."))
        setattr(cls, "EDAM_data:2596",
            PermissibleValue(
                text="EDAM_data:2596",
                title="Catalogue ID",
                description="An identifier of a catalogue of biological resources."))
        setattr(cls, "EDAM_data:2597",
            PermissibleValue(
                text="EDAM_data:2597",
                title="CABRI catalogue name",
                description="The name of a catalogue of biological resources from the CABRI database."))
        setattr(cls, "EDAM_data:2600",
            PermissibleValue(
                text="EDAM_data:2600",
                title="Pathway or network",
                description="""Primary data about a specific biological pathway or network (the nodes and connections within the pathway or network)."""))
        setattr(cls, "EDAM_data:2603",
            PermissibleValue(
                text="EDAM_data:2603",
                title="Expression data",
                description="""Image, hybridisation or some other data arising from a study of feature/molecule expression, typically profiling or quantification."""))
        setattr(cls, "EDAM_data:2605",
            PermissibleValue(
                text="EDAM_data:2605",
                title="Compound ID (KEGG)",
                description="Unique identifier of a chemical compound from the KEGG database."))
        setattr(cls, "EDAM_data:2606",
            PermissibleValue(
                text="EDAM_data:2606",
                title="RFAM name",
                description="Name (not necessarily stable) an entry (RNA family) from the RFAM database."))
        setattr(cls, "EDAM_data:2608",
            PermissibleValue(
                text="EDAM_data:2608",
                title="Reaction ID (KEGG)",
                description="Identifier of a biological reaction from the KEGG reactions database."))
        setattr(cls, "EDAM_data:2609",
            PermissibleValue(
                text="EDAM_data:2609",
                title="Drug ID (KEGG)",
                description="Unique identifier of a drug from the KEGG Drug database."))
        setattr(cls, "EDAM_data:2610",
            PermissibleValue(
                text="EDAM_data:2610",
                title="Ensembl ID",
                description="Identifier of an entry (exon, gene, transcript or protein) from the Ensembl database."))
        setattr(cls, "EDAM_data:2611",
            PermissibleValue(
                text="EDAM_data:2611",
                title="ICD identifier",
                description="""An identifier of a disease from the International Classification of Diseases (ICD) database."""))
        setattr(cls, "EDAM_data:2612",
            PermissibleValue(
                text="EDAM_data:2612",
                title="Sequence cluster ID (CluSTr)",
                description="Unique identifier of a sequence cluster from the CluSTr database."))
        setattr(cls, "EDAM_data:2613",
            PermissibleValue(
                text="EDAM_data:2613",
                title="KEGG Glycan ID",
                description="""Unique identifier of a glycan ligand from the KEGG GLYCAN database (a subset of KEGG LIGAND)."""))
        setattr(cls, "EDAM_data:2614",
            PermissibleValue(
                text="EDAM_data:2614",
                title="TCDB ID",
                description="""A unique identifier of a family from the transport classification database (TCDB) of membrane transport proteins.
OBO file for regular expression."""))
        setattr(cls, "EDAM_data:2615",
            PermissibleValue(
                text="EDAM_data:2615",
                title="MINT ID",
                description="Unique identifier of an entry from the MINT database of protein-protein interactions."))
        setattr(cls, "EDAM_data:2616",
            PermissibleValue(
                text="EDAM_data:2616",
                title="DIP ID",
                description="Unique identifier of an entry from the DIP database of protein-protein interactions."))
        setattr(cls, "EDAM_data:2617",
            PermissibleValue(
                text="EDAM_data:2617",
                title="Signaling Gateway protein ID",
                description="""Unique identifier of a protein listed in the UCSD-Nature Signaling Gateway Molecule Pages database."""))
        setattr(cls, "EDAM_data:2618",
            PermissibleValue(
                text="EDAM_data:2618",
                title="Protein modification ID",
                description="Identifier of a protein modification catalogued in a database."))
        setattr(cls, "EDAM_data:2619",
            PermissibleValue(
                text="EDAM_data:2619",
                title="RESID ID",
                description="Identifier of a protein modification catalogued in the RESID database."))
        setattr(cls, "EDAM_data:2620",
            PermissibleValue(
                text="EDAM_data:2620",
                title="RGD ID",
                description="Identifier of an entry from the RGD database."))
        setattr(cls, "EDAM_data:2621",
            PermissibleValue(
                text="EDAM_data:2621",
                title="TAIR accession (protein)",
                description="Identifier of a protein sequence from the TAIR database."))
        setattr(cls, "EDAM_data:2622",
            PermissibleValue(
                text="EDAM_data:2622",
                title="Compound ID (HMDB)",
                description="Identifier of a small molecule metabolite from the Human Metabolome Database (HMDB)."))
        setattr(cls, "EDAM_data:2625",
            PermissibleValue(
                text="EDAM_data:2625",
                title="LIPID MAPS ID",
                description="Identifier of an entry from the LIPID MAPS database."))
        setattr(cls, "EDAM_data:2626",
            PermissibleValue(
                text="EDAM_data:2626",
                title="PeptideAtlas ID",
                description="Identifier of a peptide from the PeptideAtlas peptide databases."))
        setattr(cls, "EDAM_data:2628",
            PermissibleValue(
                text="EDAM_data:2628",
                title="BioGRID interaction ID",
                description="A unique identifier of an interaction from the BioGRID database."))
        setattr(cls, "EDAM_data:2629",
            PermissibleValue(
                text="EDAM_data:2629",
                title="Enzyme ID (MEROPS)",
                description="Unique identifier of a peptidase enzyme from the MEROPS database."))
        setattr(cls, "EDAM_data:2630",
            PermissibleValue(
                text="EDAM_data:2630",
                title="Mobile genetic element ID",
                description="An identifier of a mobile genetic element."))
        setattr(cls, "EDAM_data:2631",
            PermissibleValue(
                text="EDAM_data:2631",
                title="ACLAME ID",
                description="An identifier of a mobile genetic element from the Aclame database."))
        setattr(cls, "EDAM_data:2632",
            PermissibleValue(
                text="EDAM_data:2632",
                title="SGD ID",
                description="Identifier of an entry from the Saccharomyces genome database (SGD)."))
        setattr(cls, "EDAM_data:2633",
            PermissibleValue(
                text="EDAM_data:2633",
                title="Book ID",
                description="Unique identifier of a book."))
        setattr(cls, "EDAM_data:2634",
            PermissibleValue(
                text="EDAM_data:2634",
                title="ISBN",
                description="The International Standard Book Number (ISBN) is for identifying printed books."))
        setattr(cls, "EDAM_data:2635",
            PermissibleValue(
                text="EDAM_data:2635",
                title="Compound ID (3DMET)",
                description="Identifier of a metabolite from the 3DMET database."))
        setattr(cls, "EDAM_data:2636",
            PermissibleValue(
                text="EDAM_data:2636",
                title="MatrixDB interaction ID",
                description="A unique identifier of an interaction from the MatrixDB database."))
        setattr(cls, "EDAM_data:2637",
            PermissibleValue(
                text="EDAM_data:2637",
                title="cPath ID",
                description="""A unique identifier for pathways, reactions, complexes and small molecules from the cPath (Pathway Commons) database.
These identifiers are unique within the cPath database, however, they are not stable between releases."""))
        setattr(cls, "EDAM_data:2638",
            PermissibleValue(
                text="EDAM_data:2638",
                title="PubChem bioassay ID",
                description="Identifier of an assay from the PubChem database."))
        setattr(cls, "EDAM_data:2639",
            PermissibleValue(
                text="EDAM_data:2639",
                title="PubChem ID",
                description="Identifier of an entry from the PubChem database."))
        setattr(cls, "EDAM_data:2641",
            PermissibleValue(
                text="EDAM_data:2641",
                title="Reaction ID (MACie)",
                description="Identifier of an enzyme reaction mechanism from the MACie database."))
        setattr(cls, "EDAM_data:2642",
            PermissibleValue(
                text="EDAM_data:2642",
                title="Gene ID (miRBase)",
                description="Identifier for a gene from the miRBase database."))
        setattr(cls, "EDAM_data:2643",
            PermissibleValue(
                text="EDAM_data:2643",
                title="Gene ID (ZFIN)",
                description="Identifier for a gene from the Zebrafish information network genome (ZFIN) database."))
        setattr(cls, "EDAM_data:2644",
            PermissibleValue(
                text="EDAM_data:2644",
                title="Reaction ID (Rhea)",
                description="Identifier of an enzyme-catalysed reaction from the Rhea database."))
        setattr(cls, "EDAM_data:2645",
            PermissibleValue(
                text="EDAM_data:2645",
                title="Pathway ID (Unipathway)",
                description="Identifier of a biological pathway from the Unipathway database."))
        setattr(cls, "EDAM_data:2646",
            PermissibleValue(
                text="EDAM_data:2646",
                title="Compound ID (ChEMBL)",
                description="Identifier of a small molecular from the ChEMBL database."))
        setattr(cls, "EDAM_data:2647",
            PermissibleValue(
                text="EDAM_data:2647",
                title="LGICdb identifier",
                description="Unique identifier of an entry from the Ligand-gated ion channel (LGICdb) database."))
        setattr(cls, "EDAM_data:2648",
            PermissibleValue(
                text="EDAM_data:2648",
                title="Reaction kinetics ID (SABIO-RK)",
                description="""Identifier of a biological reaction (kinetics entry) from the SABIO-RK reactions database."""))
        setattr(cls, "EDAM_data:2649",
            PermissibleValue(
                text="EDAM_data:2649",
                title="PharmGKB ID",
                description="""Identifier of an entry from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB)."""))
        setattr(cls, "EDAM_data:2650",
            PermissibleValue(
                text="EDAM_data:2650",
                title="Pathway ID (PharmGKB)",
                description="""Identifier of a pathway from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB)."""))
        setattr(cls, "EDAM_data:2651",
            PermissibleValue(
                text="EDAM_data:2651",
                title="Disease ID (PharmGKB)",
                description="""Identifier of a disease from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB)."""))
        setattr(cls, "EDAM_data:2652",
            PermissibleValue(
                text="EDAM_data:2652",
                title="Drug ID (PharmGKB)",
                description="""Identifier of a drug from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB)."""))
        setattr(cls, "EDAM_data:2653",
            PermissibleValue(
                text="EDAM_data:2653",
                title="Drug ID (TTD)",
                description="Identifier of a drug from the Therapeutic Target Database (TTD)."))
        setattr(cls, "EDAM_data:2654",
            PermissibleValue(
                text="EDAM_data:2654",
                title="Target ID (TTD)",
                description="Identifier of a target protein from the Therapeutic Target Database (TTD)."))
        setattr(cls, "EDAM_data:2655",
            PermissibleValue(
                text="EDAM_data:2655",
                title="Cell type identifier",
                description="A unique identifier of a type or group of cells."))
        setattr(cls, "EDAM_data:2656",
            PermissibleValue(
                text="EDAM_data:2656",
                title="NeuronDB ID",
                description="A unique identifier of a neuron from the NeuronDB database."))
        setattr(cls, "EDAM_data:2657",
            PermissibleValue(
                text="EDAM_data:2657",
                title="NeuroMorpho ID",
                description="A unique identifier of a neuron from the NeuroMorpho database."))
        setattr(cls, "EDAM_data:2658",
            PermissibleValue(
                text="EDAM_data:2658",
                title="Compound ID (ChemIDplus)",
                description="Identifier of a chemical from the ChemIDplus database."))
        setattr(cls, "EDAM_data:2659",
            PermissibleValue(
                text="EDAM_data:2659",
                title="Pathway ID (SMPDB)",
                description="Identifier of a pathway from the Small Molecule Pathway Database (SMPDB)."))
        setattr(cls, "EDAM_data:2660",
            PermissibleValue(
                text="EDAM_data:2660",
                title="BioNumbers ID",
                description="""Identifier of an entry from the BioNumbers database of key numbers and associated data in molecular biology."""))
        setattr(cls, "EDAM_data:2662",
            PermissibleValue(
                text="EDAM_data:2662",
                title="T3DB ID",
                description="Unique identifier of a toxin from the Toxin and Toxin Target Database (T3DB) database."))
        setattr(cls, "EDAM_data:2663",
            PermissibleValue(
                text="EDAM_data:2663",
                title="Carbohydrate identifier",
                description="Identifier of a carbohydrate."))
        setattr(cls, "EDAM_data:2664",
            PermissibleValue(
                text="EDAM_data:2664",
                title="GlycomeDB ID",
                description="Identifier of an entry from the GlycomeDB database."))
        setattr(cls, "EDAM_data:2665",
            PermissibleValue(
                text="EDAM_data:2665",
                title="LipidBank ID",
                description="Identifier of an entry from the LipidBank database."))
        setattr(cls, "EDAM_data:2666",
            PermissibleValue(
                text="EDAM_data:2666",
                title="CDD ID",
                description="Identifier of a conserved domain from the Conserved Domain Database."))
        setattr(cls, "EDAM_data:2667",
            PermissibleValue(
                text="EDAM_data:2667",
                title="MMDB ID",
                description="An identifier of an entry from the MMDB database."))
        setattr(cls, "EDAM_data:2668",
            PermissibleValue(
                text="EDAM_data:2668",
                title="iRefIndex ID",
                description="""Unique identifier of an entry from the iRefIndex database of protein-protein interactions."""))
        setattr(cls, "EDAM_data:2669",
            PermissibleValue(
                text="EDAM_data:2669",
                title="ModelDB ID",
                description="Unique identifier of an entry from the ModelDB database."))
        setattr(cls, "EDAM_data:2670",
            PermissibleValue(
                text="EDAM_data:2670",
                title="Pathway ID (DQCS)",
                description="""Identifier of a signaling pathway from the Database of Quantitative Cellular Signaling (DQCS)."""))
        setattr(cls, "EDAM_data:2700",
            PermissibleValue(
                text="EDAM_data:2700",
                title="CATH identifier",
                description="Identifier of a protein domain (or other node) from the CATH database."))
        setattr(cls, "EDAM_data:2701",
            PermissibleValue(
                text="EDAM_data:2701",
                title="CATH node ID (family)",
                description="A code number identifying a family from the CATH database."))
        setattr(cls, "EDAM_data:2702",
            PermissibleValue(
                text="EDAM_data:2702",
                title="Enzyme ID (CAZy)",
                description="Identifier of an enzyme from the CAZy enzymes database."))
        setattr(cls, "EDAM_data:2704",
            PermissibleValue(
                text="EDAM_data:2704",
                title="Clone ID (IMAGE)",
                description="""A unique identifier assigned by the I.M.A.G.E. consortium to a clone (cloned molecular sequence)."""))
        setattr(cls, "EDAM_data:2705",
            PermissibleValue(
                text="EDAM_data:2705",
                title="GO concept ID (cellular component)",
                description="An identifier of a 'cellular component' concept from the Gene Ontology."))
        setattr(cls, "EDAM_data:2706",
            PermissibleValue(
                text="EDAM_data:2706",
                title="Chromosome name (BioCyc)",
                description="Name of a chromosome as used in the BioCyc database."))
        setattr(cls, "EDAM_data:2709",
            PermissibleValue(
                text="EDAM_data:2709",
                title="CleanEx entry name",
                description="An identifier of a gene expression profile from the CleanEx database."))
        setattr(cls, "EDAM_data:2710",
            PermissibleValue(
                text="EDAM_data:2710",
                title="CleanEx dataset code",
                description="""An identifier of (typically a list of) gene expression experiments catalogued in the CleanEx database."""))
        setattr(cls, "EDAM_data:2711",
            PermissibleValue(
                text="EDAM_data:2711",
                title="Genome report",
                description="A human-readable collection of information concerning a genome as a whole."))
        setattr(cls, "EDAM_data:2713",
            PermissibleValue(
                text="EDAM_data:2713",
                title="Protein ID (CORUM)",
                description="Unique identifier for a protein complex from the CORUM database."))
        setattr(cls, "EDAM_data:2714",
            PermissibleValue(
                text="EDAM_data:2714",
                title="CDD PSSM-ID",
                description="Unique identifier of a position-specific scoring matrix from the CDD database."))
        setattr(cls, "EDAM_data:2715",
            PermissibleValue(
                text="EDAM_data:2715",
                title="Protein ID (CuticleDB)",
                description="Unique identifier for a protein from the CuticleDB database."))
        setattr(cls, "EDAM_data:2716",
            PermissibleValue(
                text="EDAM_data:2716",
                title="DBD ID",
                description="Identifier of a predicted transcription factor from the DBD database."))
        setattr(cls, "EDAM_data:2717",
            PermissibleValue(
                text="EDAM_data:2717",
                title="Oligonucleotide probe annotation",
                description="General annotation on an oligonucleotide probe, or a set of probes."))
        setattr(cls, "EDAM_data:2718",
            PermissibleValue(
                text="EDAM_data:2718",
                title="Oligonucleotide ID",
                description="Identifier of an oligonucleotide from a database."))
        setattr(cls, "EDAM_data:2719",
            PermissibleValue(
                text="EDAM_data:2719",
                title="dbProbe ID",
                description="Identifier of an oligonucleotide probe from the dbProbe database."))
        setattr(cls, "EDAM_data:2720",
            PermissibleValue(
                text="EDAM_data:2720",
                title="Dinucleotide property",
                description="Physicochemical property data for one or more dinucleotides."))
        setattr(cls, "EDAM_data:2721",
            PermissibleValue(
                text="EDAM_data:2721",
                title="DiProDB ID",
                description="Identifier of an dinucleotide property from the DiProDB database."))
        setattr(cls, "EDAM_data:2723",
            PermissibleValue(
                text="EDAM_data:2723",
                title="Protein ID (DisProt)",
                description="Unique identifier for a protein from the DisProt database."))
        setattr(cls, "EDAM_data:2725",
            PermissibleValue(
                text="EDAM_data:2725",
                title="Ensembl transcript ID",
                description="Unique identifier for a gene transcript from the Ensembl database."))
        setattr(cls, "EDAM_data:2727",
            PermissibleValue(
                text="EDAM_data:2727",
                title="Promoter ID",
                description="An identifier of a promoter of a gene that is catalogued in a database."))
        setattr(cls, "EDAM_data:2728",
            PermissibleValue(
                text="EDAM_data:2728",
                title="EST accession",
                description="Identifier of an EST sequence."))
        setattr(cls, "EDAM_data:2729",
            PermissibleValue(
                text="EDAM_data:2729",
                title="COGEME EST ID",
                description="Identifier of an EST sequence from the COGEME database."))
        setattr(cls, "EDAM_data:2730",
            PermissibleValue(
                text="EDAM_data:2730",
                title="COGEME unisequence ID",
                description="""A unisequence is a single sequence assembled from ESTs.
Identifier of a unisequence from the COGEME database."""))
        setattr(cls, "EDAM_data:2731",
            PermissibleValue(
                text="EDAM_data:2731",
                title="Protein family ID (GeneFarm)",
                description="Accession number of an entry (protein family) from the GeneFarm database."))
        setattr(cls, "EDAM_data:2732",
            PermissibleValue(
                text="EDAM_data:2732",
                title="Family name",
                description="The name of a family of organism."))
        setattr(cls, "EDAM_data:2736",
            PermissibleValue(
                text="EDAM_data:2736",
                title="Sequence feature ID (SwissRegulon)",
                description="""A feature identifier as used in the SwissRegulon database.
This can be name of a gene, the ID of a TFBS, or genomic coordinates in form \"chr:start..end\"."""))
        setattr(cls, "EDAM_data:2737",
            PermissibleValue(
                text="EDAM_data:2737",
                title="FIG ID",
                description="""A FIG ID consists of four parts: a prefix, genome id, locus type and id number.
A unique identifier of gene in the NMPDR database."""))
        setattr(cls, "EDAM_data:2738",
            PermissibleValue(
                text="EDAM_data:2738",
                title="Gene ID (Xenbase)",
                description="A unique identifier of gene in the Xenbase database."))
        setattr(cls, "EDAM_data:2739",
            PermissibleValue(
                text="EDAM_data:2739",
                title="Gene ID (Genolist)",
                description="A unique identifier of gene in the Genolist database."))
        setattr(cls, "EDAM_data:2741",
            PermissibleValue(
                text="EDAM_data:2741",
                title="ABS ID",
                description="Identifier of an entry (promoter) from the ABS database."))
        setattr(cls, "EDAM_data:2742",
            PermissibleValue(
                text="EDAM_data:2742",
                title="AraC-XylS ID",
                description="Identifier of a transcription factor from the AraC-XylS database."))
        setattr(cls, "EDAM_data:2744",
            PermissibleValue(
                text="EDAM_data:2744",
                title="Locus ID (PseudoCAP)",
                description="Identifier of a locus from the PseudoCAP database."))
        setattr(cls, "EDAM_data:2745",
            PermissibleValue(
                text="EDAM_data:2745",
                title="Locus ID (UTR)",
                description="Identifier of a locus from the UTR database."))
        setattr(cls, "EDAM_data:2746",
            PermissibleValue(
                text="EDAM_data:2746",
                title="MonosaccharideDB ID",
                description="Unique identifier of a monosaccharide from the MonosaccharideDB database."))
        setattr(cls, "EDAM_data:2749",
            PermissibleValue(
                text="EDAM_data:2749",
                title="Genome identifier",
                description="An identifier of a particular genome."))
        setattr(cls, "EDAM_data:2752",
            PermissibleValue(
                text="EDAM_data:2752",
                title="GlycoMap ID",
                description="Identifier of an entry from the GlycoMapsDB (Glycosciences.de) database."))
        setattr(cls, "EDAM_data:2753",
            PermissibleValue(
                text="EDAM_data:2753",
                title="Carbohydrate conformational map",
                description="A conformational energy map of the glycosidic linkages in a carbohydrate molecule."))
        setattr(cls, "EDAM_data:2755",
            PermissibleValue(
                text="EDAM_data:2755",
                title="Transcription factor name",
                description="The name of a transcription factor."))
        setattr(cls, "EDAM_data:2756",
            PermissibleValue(
                text="EDAM_data:2756",
                title="TCID",
                description="""Identifier of a membrane transport proteins from the transport classification database (TCDB)."""))
        setattr(cls, "EDAM_data:2757",
            PermissibleValue(
                text="EDAM_data:2757",
                title="Pfam domain name",
                description="Name of a domain from the Pfam database."))
        setattr(cls, "EDAM_data:2758",
            PermissibleValue(
                text="EDAM_data:2758",
                title="Pfam clan ID",
                description="Accession number of a Pfam clan."))
        setattr(cls, "EDAM_data:2759",
            PermissibleValue(
                text="EDAM_data:2759",
                title="Gene ID (VectorBase)",
                description="Identifier for a gene from the VectorBase database."))
        setattr(cls, "EDAM_data:2761",
            PermissibleValue(
                text="EDAM_data:2761",
                title="UTRSite ID",
                description="""Identifier of an entry from the UTRSite database of regulatory motifs in eukaryotic UTRs."""))
        setattr(cls, "EDAM_data:2762",
            PermissibleValue(
                text="EDAM_data:2762",
                title="Sequence signature report",
                description="""An informative report about a specific or conserved pattern in a molecular sequence, such as its context in genes or proteins, its role, origin or method of construction, etc."""))
        setattr(cls, "EDAM_data:2764",
            PermissibleValue(
                text="EDAM_data:2764",
                title="Protein name (UniProt)",
                description="Official name of a protein as used in the UniProt database."))
        setattr(cls, "EDAM_data:2766",
            PermissibleValue(
                text="EDAM_data:2766",
                title="HAMAP ID",
                description="Name of a protein family from the HAMAP database."))
        setattr(cls, "EDAM_data:2769",
            PermissibleValue(
                text="EDAM_data:2769",
                title="Transcript ID",
                description="Identifier of a RNA transcript."))
        setattr(cls, "EDAM_data:2770",
            PermissibleValue(
                text="EDAM_data:2770",
                title="HIT ID",
                description="Identifier of an RNA transcript from the H-InvDB database."))
        setattr(cls, "EDAM_data:2771",
            PermissibleValue(
                text="EDAM_data:2771",
                title="HIX ID",
                description="A unique identifier of gene cluster in the H-InvDB database."))
        setattr(cls, "EDAM_data:2772",
            PermissibleValue(
                text="EDAM_data:2772",
                title="HPA antibody id",
                description="Identifier of a antibody from the HPA database."))
        setattr(cls, "EDAM_data:2773",
            PermissibleValue(
                text="EDAM_data:2773",
                title="IMGT/HLA ID",
                description="""Identifier of a human major histocompatibility complex (HLA) or other protein from the IMGT/HLA database."""))
        setattr(cls, "EDAM_data:2774",
            PermissibleValue(
                text="EDAM_data:2774",
                title="Gene ID (JCVI)",
                description="A unique identifier of gene assigned by the J. Craig Venter Institute (JCVI)."))
        setattr(cls, "EDAM_data:2775",
            PermissibleValue(
                text="EDAM_data:2775",
                title="Kinase name",
                description="The name of a kinase protein."))
        setattr(cls, "EDAM_data:2776",
            PermissibleValue(
                text="EDAM_data:2776",
                title="ConsensusPathDB entity ID",
                description="Identifier of a physical entity from the ConsensusPathDB database."))
        setattr(cls, "EDAM_data:2777",
            PermissibleValue(
                text="EDAM_data:2777",
                title="ConsensusPathDB entity name",
                description="Name of a physical entity from the ConsensusPathDB database."))
        setattr(cls, "EDAM_data:2778",
            PermissibleValue(
                text="EDAM_data:2778",
                title="CCAP strain number",
                description="The number of a strain of algae and protozoa from the CCAP database."))
        setattr(cls, "EDAM_data:2779",
            PermissibleValue(
                text="EDAM_data:2779",
                title="Stock number",
                description="An identifier of stock from a catalogue of biological resources."))
        setattr(cls, "EDAM_data:2780",
            PermissibleValue(
                text="EDAM_data:2780",
                title="Stock number (TAIR)",
                description="A stock number from The Arabidopsis information resource (TAIR)."))
        setattr(cls, "EDAM_data:2781",
            PermissibleValue(
                text="EDAM_data:2781",
                title="REDIdb ID",
                description="Identifier of an entry from the RNA editing database (REDIdb)."))
        setattr(cls, "EDAM_data:2782",
            PermissibleValue(
                text="EDAM_data:2782",
                title="SMART domain name",
                description="Name of a domain from the SMART database."))
        setattr(cls, "EDAM_data:2783",
            PermissibleValue(
                text="EDAM_data:2783",
                title="Protein family ID (PANTHER)",
                description="Accession number of an entry (family) from the PANTHER database."))
        setattr(cls, "EDAM_data:2784",
            PermissibleValue(
                text="EDAM_data:2784",
                title="RNAVirusDB ID",
                description="""A unique identifier for a virus from the RNAVirusDB database.
Could list (or reference) other taxa here from https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary."""))
        setattr(cls, "EDAM_data:2785",
            PermissibleValue(
                text="EDAM_data:2785",
                title="Virus identifier",
                description="An accession of annotation on a (group of) viruses (catalogued in a database)."))
        setattr(cls, "EDAM_data:2786",
            PermissibleValue(
                text="EDAM_data:2786",
                title="NCBI Genome Project ID",
                description="An identifier of a genome project assigned by NCBI."))
        setattr(cls, "EDAM_data:2787",
            PermissibleValue(
                text="EDAM_data:2787",
                title="NCBI genome accession",
                description="A unique identifier of a whole genome assigned by the NCBI."))
        setattr(cls, "EDAM_data:2789",
            PermissibleValue(
                text="EDAM_data:2789",
                title="Protein ID (TopDB)",
                description="Unique identifier for a membrane protein from the TopDB database."))
        setattr(cls, "EDAM_data:2790",
            PermissibleValue(
                text="EDAM_data:2790",
                title="Gel ID",
                description="Identifier of a two-dimensional (protein) gel."))
        setattr(cls, "EDAM_data:2791",
            PermissibleValue(
                text="EDAM_data:2791",
                title="Reference map name (SWISS-2DPAGE)",
                description="Name of a reference map gel from the SWISS-2DPAGE database."))
        setattr(cls, "EDAM_data:2792",
            PermissibleValue(
                text="EDAM_data:2792",
                title="Protein ID (PeroxiBase)",
                description="Unique identifier for a peroxidase protein from the PeroxiBase database."))
        setattr(cls, "EDAM_data:2793",
            PermissibleValue(
                text="EDAM_data:2793",
                title="SISYPHUS ID",
                description="Identifier of an entry from the SISYPHUS database of tertiary structure alignments."))
        setattr(cls, "EDAM_data:2794",
            PermissibleValue(
                text="EDAM_data:2794",
                title="ORF ID",
                description="Accession of an open reading frame (catalogued in a database)."))
        setattr(cls, "EDAM_data:2795",
            PermissibleValue(
                text="EDAM_data:2795",
                title="ORF identifier",
                description="An identifier of an open reading frame."))
        setattr(cls, "EDAM_data:2796",
            PermissibleValue(
                text="EDAM_data:2796",
                title="LINUCS ID",
                description="Identifier of an entry from the GlycosciencesDB database."))
        setattr(cls, "EDAM_data:2797",
            PermissibleValue(
                text="EDAM_data:2797",
                title="Protein ID (LGICdb)",
                description="Unique identifier for a ligand-gated ion channel protein from the LGICdb database."))
        setattr(cls, "EDAM_data:2798",
            PermissibleValue(
                text="EDAM_data:2798",
                title="MaizeDB ID",
                description="Identifier of an EST sequence from the MaizeDB database."))
        setattr(cls, "EDAM_data:2799",
            PermissibleValue(
                text="EDAM_data:2799",
                title="Gene ID (MfunGD)",
                description="A unique identifier of gene in the MfunGD database."))
        setattr(cls, "EDAM_data:2800",
            PermissibleValue(
                text="EDAM_data:2800",
                title="Orpha number",
                description="An identifier of a disease from the Orpha database."))
        setattr(cls, "EDAM_data:2802",
            PermissibleValue(
                text="EDAM_data:2802",
                title="Protein ID (EcID)",
                description="Unique identifier for a protein from the EcID database."))
        setattr(cls, "EDAM_data:2803",
            PermissibleValue(
                text="EDAM_data:2803",
                title="Clone ID (RefSeq)",
                description="A unique identifier of a cDNA molecule catalogued in the RefSeq database."))
        setattr(cls, "EDAM_data:2804",
            PermissibleValue(
                text="EDAM_data:2804",
                title="Protein ID (ConoServer)",
                description="Unique identifier for a cone snail toxin protein from the ConoServer database."))
        setattr(cls, "EDAM_data:2805",
            PermissibleValue(
                text="EDAM_data:2805",
                title="GeneSNP ID",
                description="Identifier of a GeneSNP database entry."))
        setattr(cls, "EDAM_data:2812",
            PermissibleValue(
                text="EDAM_data:2812",
                title="Lipid identifier",
                description="Identifier of a lipid."))
        setattr(cls, "EDAM_data:2835",
            PermissibleValue(
                text="EDAM_data:2835",
                title="Gene ID (VBASE2)",
                description="Identifier for a gene from the VBASE2 database."))
        setattr(cls, "EDAM_data:2836",
            PermissibleValue(
                text="EDAM_data:2836",
                title="DPVweb ID",
                description="A unique identifier for a virus from the DPVweb database."))
        setattr(cls, "EDAM_data:2837",
            PermissibleValue(
                text="EDAM_data:2837",
                title="Pathway ID (BioSystems)",
                description="Identifier of a pathway from the BioSystems pathway database."))
        setattr(cls, "EDAM_data:2849",
            PermissibleValue(
                text="EDAM_data:2849",
                title="Abstract",
                description="An abstract of a scientific article."))
        setattr(cls, "EDAM_data:2850",
            PermissibleValue(
                text="EDAM_data:2850",
                title="Lipid structure",
                description="3D coordinate and associated data for a lipid structure."))
        setattr(cls, "EDAM_data:2851",
            PermissibleValue(
                text="EDAM_data:2851",
                title="Drug structure",
                description="3D coordinate and associated data for the (3D) structure of a drug."))
        setattr(cls, "EDAM_data:2852",
            PermissibleValue(
                text="EDAM_data:2852",
                title="Toxin structure",
                description="3D coordinate and associated data for the (3D) structure of a toxin."))
        setattr(cls, "EDAM_data:2854",
            PermissibleValue(
                text="EDAM_data:2854",
                title="Position-specific scoring matrix",
                description="""A simple matrix of numbers, where each value (or column of values) is derived derived from analysis of the corresponding position in a sequence alignment."""))
        setattr(cls, "EDAM_data:2855",
            PermissibleValue(
                text="EDAM_data:2855",
                title="Distance matrix",
                description="""A matrix of distances between molecular entities, where a value (distance) is (typically) derived from comparison of two entities and reflects their similarity."""))
        setattr(cls, "EDAM_data:2856",
            PermissibleValue(
                text="EDAM_data:2856",
                title="Structural distance matrix",
                description="Distances (values representing similarity) between a group of molecular structures."))
        setattr(cls, "EDAM_data:2858",
            PermissibleValue(
                text="EDAM_data:2858",
                title="Ontology concept",
                description="""A concept from a biological ontology.
This includes any fields from the concept definition such as concept name, definition, comments and so on."""))
        setattr(cls, "EDAM_data:2865",
            PermissibleValue(
                text="EDAM_data:2865",
                title="Codon usage bias",
                description="""A numerical measure of differences in the frequency of occurrence of synonymous codons in DNA sequences."""))
        setattr(cls, "EDAM_data:2870",
            PermissibleValue(
                text="EDAM_data:2870",
                title="Radiation hybrid map",
                description="""A map showing distance between genetic markers estimated by radiation-induced breaks in a chromosome.
The radiation method can break very closely linked markers providing a more detailed map. Most genetic markers and subsequences may be located to a defined map position and with a more precise estimates of distance than a linkage map."""))
        setattr(cls, "EDAM_data:2872",
            PermissibleValue(
                text="EDAM_data:2872",
                title="ID list",
                description="""A simple list of data identifiers (such as database accessions), possibly with additional basic information on the addressed data."""))
        setattr(cls, "EDAM_data:2873",
            PermissibleValue(
                text="EDAM_data:2873",
                title="Phylogenetic gene frequencies data",
                description="Gene frequencies data that may be read during phylogenetic tree calculation."))
        setattr(cls, "EDAM_data:2877",
            PermissibleValue(
                text="EDAM_data:2877",
                title="Protein complex",
                description="""3D coordinate and associated data for a multi-protein complex; two or more polypeptides chains in a stable, functional association with one another."""))
        setattr(cls, "EDAM_data:2878",
            PermissibleValue(
                text="EDAM_data:2878",
                title="Protein structural motif",
                description="""3D coordinate and associated data for a protein (3D) structural motif; any group of contiguous or non-contiguous amino acid residues but typically those forming a feature with a structural or functional role."""))
        setattr(cls, "EDAM_data:2879",
            PermissibleValue(
                text="EDAM_data:2879",
                title="Lipid report",
                description="""A human-readable collection of information about one or more specific lipid 3D structure(s)."""))
        setattr(cls, "EDAM_data:2884",
            PermissibleValue(
                text="EDAM_data:2884",
                title="Plot",
                description="""Biological data that has been plotted as a graph of some type, or plotting instructions for rendering such a graph."""))
        setattr(cls, "EDAM_data:2886",
            PermissibleValue(
                text="EDAM_data:2886",
                title="Protein sequence record",
                description="A protein sequence and associated metadata."))
        setattr(cls, "EDAM_data:2887",
            PermissibleValue(
                text="EDAM_data:2887",
                title="Nucleic acid sequence record",
                description="A nucleic acid sequence and associated metadata."))
        setattr(cls, "EDAM_data:2891",
            PermissibleValue(
                text="EDAM_data:2891",
                title="Biological model accession",
                description="Accession of a mathematical model, typically an entry from a database."))
        setattr(cls, "EDAM_data:2892",
            PermissibleValue(
                text="EDAM_data:2892",
                title="Cell type name",
                description="The name of a type or group of cells."))
        setattr(cls, "EDAM_data:2893",
            PermissibleValue(
                text="EDAM_data:2893",
                title="Cell type accession",
                description="Accession of a type or group of cells (catalogued in a database)."))
        setattr(cls, "EDAM_data:2894",
            PermissibleValue(
                text="EDAM_data:2894",
                title="Compound accession",
                description="Accession of an entry from a database of chemicals."))
        setattr(cls, "EDAM_data:2895",
            PermissibleValue(
                text="EDAM_data:2895",
                title="Drug accession",
                description="Accession of a drug."))
        setattr(cls, "EDAM_data:2896",
            PermissibleValue(
                text="EDAM_data:2896",
                title="Toxin name",
                description="Name of a toxin."))
        setattr(cls, "EDAM_data:2897",
            PermissibleValue(
                text="EDAM_data:2897",
                title="Toxin accession",
                description="Accession of a toxin (catalogued in a database)."))
        setattr(cls, "EDAM_data:2898",
            PermissibleValue(
                text="EDAM_data:2898",
                title="Monosaccharide accession",
                description="Accession of a monosaccharide (catalogued in a database)."))
        setattr(cls, "EDAM_data:2899",
            PermissibleValue(
                text="EDAM_data:2899",
                title="Drug name",
                description="Common name of a drug."))
        setattr(cls, "EDAM_data:2900",
            PermissibleValue(
                text="EDAM_data:2900",
                title="Carbohydrate accession",
                description="Accession of an entry from a database of carbohydrates."))
        setattr(cls, "EDAM_data:2901",
            PermissibleValue(
                text="EDAM_data:2901",
                title="Molecule accession",
                description="Accession of a specific molecule (catalogued in a database)."))
        setattr(cls, "EDAM_data:2902",
            PermissibleValue(
                text="EDAM_data:2902",
                title="Data resource definition accession",
                description="Accession of a data definition (catalogued in a database)."))
        setattr(cls, "EDAM_data:2903",
            PermissibleValue(
                text="EDAM_data:2903",
                title="Genome accession",
                description="An accession of a particular genome (in a database)."))
        setattr(cls, "EDAM_data:2904",
            PermissibleValue(
                text="EDAM_data:2904",
                title="Map accession",
                description="An accession of a map of a molecular sequence (deposited in a database)."))
        setattr(cls, "EDAM_data:2905",
            PermissibleValue(
                text="EDAM_data:2905",
                title="Lipid accession",
                description="Accession of an entry from a database of lipids."))
        setattr(cls, "EDAM_data:2906",
            PermissibleValue(
                text="EDAM_data:2906",
                title="Peptide ID",
                description="Accession of a peptide deposited in a database."))
        setattr(cls, "EDAM_data:2907",
            PermissibleValue(
                text="EDAM_data:2907",
                title="Protein accession",
                description="Accession of a protein deposited in a database."))
        setattr(cls, "EDAM_data:2908",
            PermissibleValue(
                text="EDAM_data:2908",
                title="Organism accession",
                description="An accession of annotation on a (group of) organisms (catalogued in a database)."))
        setattr(cls, "EDAM_data:2909",
            PermissibleValue(
                text="EDAM_data:2909",
                title="Organism name",
                description="The name of an organism (or group of organisms)."))
        setattr(cls, "EDAM_data:2910",
            PermissibleValue(
                text="EDAM_data:2910",
                title="Protein family accession",
                description="Accession of a protein family (that is deposited in a database)."))
        setattr(cls, "EDAM_data:2911",
            PermissibleValue(
                text="EDAM_data:2911",
                title="Transcription factor accession",
                description="Accession of an entry from a database of transcription factors or binding sites."))
        setattr(cls, "EDAM_data:2912",
            PermissibleValue(
                text="EDAM_data:2912",
                title="Strain accession",
                description="""Accession number of a strain of an organism variant, typically a plant, virus or bacterium."""))
        setattr(cls, "EDAM_data:2914",
            PermissibleValue(
                text="EDAM_data:2914",
                title="Sequence features metadata",
                description="Metadata on sequence features."))
        setattr(cls, "EDAM_data:2915",
            PermissibleValue(
                text="EDAM_data:2915",
                title="Gramene identifier",
                description="Identifier of a Gramene database entry."))
        setattr(cls, "EDAM_data:2916",
            PermissibleValue(
                text="EDAM_data:2916",
                title="DDBJ accession",
                description="An identifier of an entry from the DDBJ sequence database."))
        setattr(cls, "EDAM_data:2917",
            PermissibleValue(
                text="EDAM_data:2917",
                title="ConsensusPathDB identifier",
                description="An identifier of an entity from the ConsensusPathDB database."))
        setattr(cls, "EDAM_data:2955",
            PermissibleValue(
                text="EDAM_data:2955",
                title="Sequence report",
                description="""An informative report of information about molecular sequence(s), including basic information (metadata), and reports generated from molecular sequence analysis, including positional features and non-positional properties."""))
        setattr(cls, "EDAM_data:2956",
            PermissibleValue(
                text="EDAM_data:2956",
                title="Protein secondary structure",
                description="""Data concerning the properties or features of one or more protein secondary structures."""))
        setattr(cls, "EDAM_data:2957",
            PermissibleValue(
                text="EDAM_data:2957",
                title="Hopp and Woods plot",
                description="A Hopp and Woods plot of predicted antigenicity of a peptide or protein."))
        setattr(cls, "EDAM_data:2968",
            PermissibleValue(
                text="EDAM_data:2968",
                title="Image",
                description="""Data (typically biological or biomedical) that has been rendered into an image, typically for display on screen."""))
        setattr(cls, "EDAM_data:2969",
            PermissibleValue(
                text="EDAM_data:2969",
                title="Sequence image",
                description="Image of a molecular sequence, possibly with sequence features or properties shown."))
        setattr(cls, "EDAM_data:2970",
            PermissibleValue(
                text="EDAM_data:2970",
                title="Protein hydropathy data",
                description="A report on protein properties concerning hydropathy."))
        setattr(cls, "EDAM_data:2976",
            PermissibleValue(
                text="EDAM_data:2976",
                title="Protein sequence",
                description="One or more protein sequences, possibly with associated annotation."))
        setattr(cls, "EDAM_data:2977",
            PermissibleValue(
                text="EDAM_data:2977",
                title="Nucleic acid sequence",
                description="One or more nucleic acid sequences, possibly with associated annotation."))
        setattr(cls, "EDAM_data:2978",
            PermissibleValue(
                text="EDAM_data:2978",
                title="Reaction data",
                description="""Data concerning a biochemical reaction, typically data and more general annotation on the kinetics of enzyme-catalysed reaction.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:2979",
            PermissibleValue(
                text="EDAM_data:2979",
                title="Peptide property",
                description="Data concerning small peptides."))
        setattr(cls, "EDAM_data:2984",
            PermissibleValue(
                text="EDAM_data:2984",
                title="Pathway or network report",
                description="""An informative report concerning or derived from the analysis of a biological pathway or network, such as a map (diagram) or annotation."""))
        setattr(cls, "EDAM_data:2985",
            PermissibleValue(
                text="EDAM_data:2985",
                title="Nucleic acid thermodynamic data",
                description="A thermodynamic or kinetic property of a nucleic acid molecule."))
        setattr(cls, "EDAM_data:2991",
            PermissibleValue(
                text="EDAM_data:2991",
                title="Protein geometry data",
                description="""Geometry data for a protein structure, for example bond lengths, bond angles, torsion angles, chiralities, planaraties etc."""))
        setattr(cls, "EDAM_data:2992",
            PermissibleValue(
                text="EDAM_data:2992",
                title="Protein structure image",
                description="An image of protein structure."))
        setattr(cls, "EDAM_data:2994",
            PermissibleValue(
                text="EDAM_data:2994",
                title="Phylogenetic character weights",
                description="""Weights for sequence positions or characters in phylogenetic analysis where zero is defined as unweighted."""))
        setattr(cls, "EDAM_data:3002",
            PermissibleValue(
                text="EDAM_data:3002",
                title="Annotation track",
                description="""Annotation of one particular positional feature on a biomolecular (typically genome) sequence, suitable for import and display in a genome browser."""))
        setattr(cls, "EDAM_data:3021",
            PermissibleValue(
                text="EDAM_data:3021",
                title="UniProt accession",
                description="Accession number of a UniProt (protein sequence) database entry."))
        setattr(cls, "EDAM_data:3022",
            PermissibleValue(
                text="EDAM_data:3022",
                title="NCBI genetic code ID",
                description="Identifier of a genetic code in the NCBI list of genetic codes."))
        setattr(cls, "EDAM_data:3025",
            PermissibleValue(
                text="EDAM_data:3025",
                title="Ontology concept identifier",
                description="""Identifier of a concept in an ontology of biological or bioinformatics concepts and relations."""))
        setattr(cls, "EDAM_data:3028",
            PermissibleValue(
                text="EDAM_data:3028",
                title="Taxonomy",
                description="""Data concerning the classification, identification and naming of organisms.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:3029",
            PermissibleValue(
                text="EDAM_data:3029",
                title="Protein ID (EMBL/GenBank/DDBJ)",
                description="""EMBL/GENBANK/DDBJ coding feature protein identifier, issued by International collaborators.
This qualifier consists of a stable ID portion (3+5 format with 3 position letters and 5 numbers) plus a version number after the decimal point. When the protein sequence encoded by the CDS changes, only the version number of the /protein_id value is incremented; the stable part of the /protein_id remains unchanged and as a result will permanently be associated with a given protein; this qualifier is valid only on CDS features which translate into a valid protein."""))
        setattr(cls, "EDAM_data:3034",
            PermissibleValue(
                text="EDAM_data:3034",
                title="Sequence feature identifier",
                description="Name or other identifier of molecular sequence feature(s)."))
        setattr(cls, "EDAM_data:3035",
            PermissibleValue(
                text="EDAM_data:3035",
                title="Structure identifier",
                description="""An identifier of a molecular tertiary structure, typically an entry from a structure database."""))
        setattr(cls, "EDAM_data:3036",
            PermissibleValue(
                text="EDAM_data:3036",
                title="Matrix identifier",
                description="An identifier of an array of numerical values, such as a comparison matrix."))
        setattr(cls, "EDAM_data:3103",
            PermissibleValue(
                text="EDAM_data:3103",
                title="ATC code",
                description="""Unique identifier of a drug conforming to the Anatomical Therapeutic Chemical (ATC) Classification System, a drug classification system controlled by the WHO Collaborating Centre for Drug Statistics Methodology (WHOCC)."""))
        setattr(cls, "EDAM_data:3104",
            PermissibleValue(
                text="EDAM_data:3104",
                title="UNII",
                description="""A unique, unambiguous, alphanumeric identifier of a chemical substance as catalogued by the Substance Registration System of the Food and Drug Administration (FDA)."""))
        setattr(cls, "EDAM_data:3106",
            PermissibleValue(
                text="EDAM_data:3106",
                title="System metadata",
                description="Metadata concerning the software, hardware or other aspects of a computer system."))
        setattr(cls, "EDAM_data:3108",
            PermissibleValue(
                text="EDAM_data:3108",
                title="Experimental measurement",
                description="""Raw data such as measurements or other results from laboratory experiments, as generated from laboratory hardware.
This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation."""))
        setattr(cls, "EDAM_data:3110",
            PermissibleValue(
                text="EDAM_data:3110",
                title="Raw microarray data",
                description="""Raw data (typically MIAME-compliant) for hybridisations from a microarray experiment.
Such data as found in Affymetrix CEL or GPR files."""))
        setattr(cls, "EDAM_data:3111",
            PermissibleValue(
                text="EDAM_data:3111",
                title="Processed microarray data",
                description="""Data generated from processing and analysis of probe set data from a microarray experiment.
Such data as found in Affymetrix .CHP files or data from other software such as RMA or dChip."""))
        setattr(cls, "EDAM_data:3112",
            PermissibleValue(
                text="EDAM_data:3112",
                title="Gene expression matrix",
                description="""The final processed (normalised) data for a set of hybridisations in a microarray experiment.
This combines data from all hybridisations."""))
        setattr(cls, "EDAM_data:3113",
            PermissibleValue(
                text="EDAM_data:3113",
                title="Sample annotation",
                description="""Annotation on a biological sample, for example experimental factors and their values.
This might include compound and dose in a dose response experiment."""))
        setattr(cls, "EDAM_data:3115",
            PermissibleValue(
                text="EDAM_data:3115",
                title="Microarray metadata",
                description="""Annotation on the array itself used in a microarray experiment.
This might include gene identifiers, genomic coordinates, probe oligonucleotide sequences etc."""))
        setattr(cls, "EDAM_data:3117",
            PermissibleValue(
                text="EDAM_data:3117",
                title="Microarray hybridisation data",
                description="Data concerning the hybridisations measured during a microarray experiment."))
        setattr(cls, "EDAM_data:3128",
            PermissibleValue(
                text="EDAM_data:3128",
                title="Nucleic acid structure report",
                description="""A human-readable collection of information about regions within a nucleic acid sequence which form secondary or tertiary (3D) structures.
The report may be based on analysis of nucleic acid sequence or structural data, or any annotation or information about specific nucleic acid 3D structure(s) or such structures in general."""))
        setattr(cls, "EDAM_data:3134",
            PermissibleValue(
                text="EDAM_data:3134",
                title="Gene transcript report",
                description="""An informative report on features of a messenger RNA (mRNA) molecules including precursor RNA, primary (unprocessed) transcript and fully processed molecules. This includes reports on a specific gene transcript, clone or EST.
This includes 5'untranslated region (5'UTR), coding sequences (CDS), exons, intervening sequences (intron) and 3'untranslated regions (3'UTR)."""))
        setattr(cls, "EDAM_data:3148",
            PermissibleValue(
                text="EDAM_data:3148",
                title="Gene family report",
                description="""A human-readable collection of information about a particular family of genes, typically a set of genes with similar sequence that originate from duplication of a common ancestor gene, or any other classification of nucleic acid sequences or structures that reflects gene structure.
This includes reports on on gene homologues between species."""))
        setattr(cls, "EDAM_data:3153",
            PermissibleValue(
                text="EDAM_data:3153",
                title="Protein image",
                description="An image of a protein."))
        setattr(cls, "EDAM_data:3181",
            PermissibleValue(
                text="EDAM_data:3181",
                title="Sequence assembly report",
                description="""An informative report about a DNA sequence assembly.
This might include an overall quality assessment of the assembly and summary statistics including counts, average length and number of bases for reads, matches and non-matches, contigs, reads in pairs etc."""))
        setattr(cls, "EDAM_data:3210",
            PermissibleValue(
                text="EDAM_data:3210",
                title="Genome index",
                description="""An index of a genome sequence.
Many sequence alignment tasks involving many or very large sequences rely on a precomputed index of the sequence to accelerate the alignment."""))
        setattr(cls, "EDAM_data:3236",
            PermissibleValue(
                text="EDAM_data:3236",
                title="Cytoband position",
                description="""Information might include start and end position in a chromosome sequence, chromosome identifier, name of band and so on.
The position of a cytogenetic band in a genome."""))
        setattr(cls, "EDAM_data:3238",
            PermissibleValue(
                text="EDAM_data:3238",
                title="Cell type ontology ID",
                description="Cell type ontology concept ID."))
        setattr(cls, "EDAM_data:3241",
            PermissibleValue(
                text="EDAM_data:3241",
                title="Kinetic model",
                description="Mathematical model of a network, that contains biochemical kinetics."))
        setattr(cls, "EDAM_data:3264",
            PermissibleValue(
                text="EDAM_data:3264",
                title="COSMIC ID",
                description="Identifier of a COSMIC database entry."))
        setattr(cls, "EDAM_data:3265",
            PermissibleValue(
                text="EDAM_data:3265",
                title="HGMD ID",
                description="Identifier of a HGMD database entry."))
        setattr(cls, "EDAM_data:3266",
            PermissibleValue(
                text="EDAM_data:3266",
                title="Sequence assembly ID",
                description="Unique identifier of sequence assembly."))
        setattr(cls, "EDAM_data:3270",
            PermissibleValue(
                text="EDAM_data:3270",
                title="Ensembl gene tree ID",
                description="Unique identifier for a gene tree from the Ensembl database."))
        setattr(cls, "EDAM_data:3271",
            PermissibleValue(
                text="EDAM_data:3271",
                title="Gene tree",
                description="A phylogenetic tree that is an estimate of the character's phylogeny."))
        setattr(cls, "EDAM_data:3272",
            PermissibleValue(
                text="EDAM_data:3272",
                title="Species tree",
                description="""A phylogenetic tree that reflects phylogeny of the taxa from which the characters (used in calculating the tree) were sampled."""))
        setattr(cls, "EDAM_data:3273",
            PermissibleValue(
                text="EDAM_data:3273",
                title="Sample ID",
                description="Name or other identifier of an entry from a biosample database."))
        setattr(cls, "EDAM_data:3274",
            PermissibleValue(
                text="EDAM_data:3274",
                title="MGI accession",
                description="Identifier of an object from the MGI database."))
        setattr(cls, "EDAM_data:3275",
            PermissibleValue(
                text="EDAM_data:3275",
                title="Phenotype name",
                description="Name of a phenotype."))
        setattr(cls, "EDAM_data:3354",
            PermissibleValue(
                text="EDAM_data:3354",
                title="Transition matrix",
                description="""A HMM transition matrix contains the probabilities of switching from one HMM state to another.
Consider for example an HMM with two states (AT-rich and GC-rich). The transition matrix will hold the probabilities of switching from the AT-rich to the GC-rich state, and vica versa."""))
        setattr(cls, "EDAM_data:3355",
            PermissibleValue(
                text="EDAM_data:3355",
                title="Emission matrix",
                description="""A HMM emission matrix holds the probabilities of choosing the four nucleotides (A, C, G and T) in each of the states of a HMM.
Consider for example an HMM with two states (AT-rich and GC-rich). The emission matrix holds the probabilities of choosing each of the four nucleotides (A, C, G and T) in the AT-rich state and in the GC-rich state."""))
        setattr(cls, "EDAM_data:3358",
            PermissibleValue(
                text="EDAM_data:3358",
                title="Format identifier",
                description="An identifier of a data format."))
        setattr(cls, "EDAM_data:3424",
            PermissibleValue(
                text="EDAM_data:3424",
                title="Raw image",
                description="Raw biological or biomedical image generated by some experimental technique."))
        setattr(cls, "EDAM_data:3425",
            PermissibleValue(
                text="EDAM_data:3425",
                title="Carbohydrate property",
                description="""Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all carbohydrates."""))
        setattr(cls, "EDAM_data:3442",
            PermissibleValue(
                text="EDAM_data:3442",
                title="MRI image",
                description="""An imaging technique that uses magnetic fields and radiowaves to form images, typically to investigate the anatomy and physiology of the human body."""))
        setattr(cls, "EDAM_data:3449",
            PermissibleValue(
                text="EDAM_data:3449",
                title="Cell migration track image",
                description="An image from a cell migration track assay."))
        setattr(cls, "EDAM_data:3451",
            PermissibleValue(
                text="EDAM_data:3451",
                title="Rate of association",
                description="Rate of association of a protein with another protein or some other molecule."))
        setattr(cls, "EDAM_data:3479",
            PermissibleValue(
                text="EDAM_data:3479",
                title="Gene order",
                description="""Multiple gene identifiers in a specific order.
Such data are often used for genome rearrangement tools and phylogenetic tree labeling."""))
        setattr(cls, "EDAM_data:3483",
            PermissibleValue(
                text="EDAM_data:3483",
                title="Spectrum",
                description="""The spectrum of frequencies of electromagnetic radiation emitted from a molecule as a result of some spectroscopy experiment."""))
        setattr(cls, "EDAM_data:3488",
            PermissibleValue(
                text="EDAM_data:3488",
                title="NMR spectrum",
                description="Spectral information for a molecule from a nuclear magnetic resonance experiment."))
        setattr(cls, "EDAM_data:3492",
            PermissibleValue(
                text="EDAM_data:3492",
                title="Nucleic acid signature",
                description="An informative report about a specific or conserved nucleic acid sequence pattern."))
        setattr(cls, "EDAM_data:3494",
            PermissibleValue(
                text="EDAM_data:3494",
                title="DNA sequence",
                description="A DNA sequence."))
        setattr(cls, "EDAM_data:3495",
            PermissibleValue(
                text="EDAM_data:3495",
                title="RNA sequence",
                description="An RNA sequence."))
        setattr(cls, "EDAM_data:3498",
            PermissibleValue(
                text="EDAM_data:3498",
                title="Sequence variations",
                description="""Data on gene sequence variations resulting large-scale genotyping and DNA sequencing projects.
Variations are stored along with a reference genome."""))
        setattr(cls, "EDAM_data:3505",
            PermissibleValue(
                text="EDAM_data:3505",
                title="Bibliography",
                description="A list of publications such as scientic papers or books."))
        setattr(cls, "EDAM_data:3509",
            PermissibleValue(
                text="EDAM_data:3509",
                title="Ontology mapping",
                description="A mapping of supplied textual terms or phrases to ontology concepts (URIs)."))
        setattr(cls, "EDAM_data:3546",
            PermissibleValue(
                text="EDAM_data:3546",
                title="Image metadata",
                description="""Any data concerning a specific biological or biomedical image.
This can include basic provenance and technical information about the image, scientific annotation and so on."""))
        setattr(cls, "EDAM_data:3558",
            PermissibleValue(
                text="EDAM_data:3558",
                title="Clinical trial report",
                description="A human-readable collection of information concerning a clinical trial."))
        setattr(cls, "EDAM_data:3567",
            PermissibleValue(
                text="EDAM_data:3567",
                title="Reference sample report",
                description="A report about a biosample."))
        setattr(cls, "EDAM_data:3568",
            PermissibleValue(
                text="EDAM_data:3568",
                title="Gene Expression Atlas Experiment ID",
                description="Accession number of an entry from the Gene Expression Atlas."))
        setattr(cls, "EDAM_data:3667",
            PermissibleValue(
                text="EDAM_data:3667",
                title="Disease identifier",
                description="Identifier of an entry from a database of disease."))
        setattr(cls, "EDAM_data:3668",
            PermissibleValue(
                text="EDAM_data:3668",
                title="Disease name",
                description="The name of some disease."))
        setattr(cls, "EDAM_data:3669",
            PermissibleValue(
                text="EDAM_data:3669",
                title="Learning material",
                description="""Learning material is a document or another digital object that is designed for learning (educational, training) purposes."""))
        setattr(cls, "EDAM_data:3670",
            PermissibleValue(
                text="EDAM_data:3670",
                title="Online course",
                description="A training course available for use on the Web."))
        setattr(cls, "EDAM_data:3671",
            PermissibleValue(
                text="EDAM_data:3671",
                title="Text",
                description="""Any free or plain text, typically for human consumption and in English. Can instantiate also as a textual search query."""))
        setattr(cls, "EDAM_data:3707",
            PermissibleValue(
                text="EDAM_data:3707",
                title="Biodiversity data",
                description="Machine-readable biodiversity data."))
        setattr(cls, "EDAM_data:3716",
            PermissibleValue(
                text="EDAM_data:3716",
                title="Biosafety report",
                description="A human-readable collection of information concerning biosafety data."))
        setattr(cls, "EDAM_data:3717",
            PermissibleValue(
                text="EDAM_data:3717",
                title="Isolation report",
                description="A report about any kind of isolation of biological material."))
        setattr(cls, "EDAM_data:3718",
            PermissibleValue(
                text="EDAM_data:3718",
                title="Pathogenicity report",
                description="Information about the ability of an organism to cause disease in a corresponding host."))
        setattr(cls, "EDAM_data:3719",
            PermissibleValue(
                text="EDAM_data:3719",
                title="Biosafety classification",
                description="""Information about the biosafety classification of an organism according to corresponding law."""))
        setattr(cls, "EDAM_data:3720",
            PermissibleValue(
                text="EDAM_data:3720",
                title="Geographic location",
                description="""A report about localisation of the isolaton of biological material e.g. country or coordinates."""))
        setattr(cls, "EDAM_data:3721",
            PermissibleValue(
                text="EDAM_data:3721",
                title="Isolation source",
                description="""A report about any kind of isolation source of biological material e.g. blood, water, soil."""))
        setattr(cls, "EDAM_data:3722",
            PermissibleValue(
                text="EDAM_data:3722",
                title="Physiology parameter",
                description="""Experimentally determined parameter of the physiology of an organism, e.g. substrate spectrum."""))
        setattr(cls, "EDAM_data:3723",
            PermissibleValue(
                text="EDAM_data:3723",
                title="Morphology parameter",
                description="""Experimentally determined parameter of the morphology of an organism, e.g. size & shape."""))
        setattr(cls, "EDAM_data:3724",
            PermissibleValue(
                text="EDAM_data:3724",
                title="Cultivation parameter",
                description="Experimental determined parameter for the cultivation of an organism."))
        setattr(cls, "EDAM_data:3732",
            PermissibleValue(
                text="EDAM_data:3732",
                title="Sequencing metadata name",
                description="""Data concerning a sequencing experiment, that may be specified as an input to some tool."""))
        setattr(cls, "EDAM_data:3733",
            PermissibleValue(
                text="EDAM_data:3733",
                title="Flow cell identifier",
                description="""A flow cell is used to immobilise, amplify and sequence millions of molecules at once. In Illumina machines, a flowcell is composed of 8 \"lanes\" which allows 8 experiments in a single analysis.
An identifier of a flow cell of a sequencing machine."""))
        setattr(cls, "EDAM_data:3734",
            PermissibleValue(
                text="EDAM_data:3734",
                title="Lane identifier",
                description="""An identifier of a lane within a flow cell of a sequencing machine, within which millions of sequences are immobilised, amplified and sequenced."""))
        setattr(cls, "EDAM_data:3735",
            PermissibleValue(
                text="EDAM_data:3735",
                title="Run number",
                description="""A number corresponding to the number of an analysis performed by a sequencing machine. For example, if it's the 13th analysis, the run is 13."""))
        setattr(cls, "EDAM_data:3736",
            PermissibleValue(
                text="EDAM_data:3736",
                title="Ecological data",
                description="""Data concerning ecology; for example measurements and reports from the study of interactions among organisms and their environment.
This is a broad data type and is used a placeholder for other, more specific types."""))
        setattr(cls, "EDAM_data:3737",
            PermissibleValue(
                text="EDAM_data:3737",
                title="Alpha diversity data",
                description="The mean species diversity in sites or habitats at a local scale."))
        setattr(cls, "EDAM_data:3738",
            PermissibleValue(
                text="EDAM_data:3738",
                title="Beta diversity data",
                description="The ratio between regional and local species diversity."))
        setattr(cls, "EDAM_data:3739",
            PermissibleValue(
                text="EDAM_data:3739",
                title="Gamma diversity data",
                description="The total species diversity in a landscape."))
        setattr(cls, "EDAM_data:3743",
            PermissibleValue(
                text="EDAM_data:3743",
                title="Ordination plot",
                description="""A plot in which community data (e.g. species abundance data) is summarised. Similar species and samples are plotted close together, and dissimilar species and samples are plotted placed far apart."""))
        setattr(cls, "EDAM_data:3753",
            PermissibleValue(
                text="EDAM_data:3753",
                title="Over-representation data",
                description="""A ranked list of categories (usually ontology concepts), each associated with a statistical metric of over-/under-representation within the studied data."""))
        setattr(cls, "EDAM_data:3754",
            PermissibleValue(
                text="EDAM_data:3754",
                title="GO-term enrichment data",
                description="""A ranked list of Gene Ontology concepts, each associated with a p-value, concerning or derived from the analysis of e.g. a set of genes or proteins."""))
        setattr(cls, "EDAM_data:3756",
            PermissibleValue(
                text="EDAM_data:3756",
                title="Localisation score",
                description="""Score for localization of one or more post-translational modifications in peptide sequence measured by mass spectrometry."""))
        setattr(cls, "EDAM_data:3757",
            PermissibleValue(
                text="EDAM_data:3757",
                title="Unimod ID",
                description="Identifier of a protein modification catalogued in the Unimod database."))
        setattr(cls, "EDAM_data:3759",
            PermissibleValue(
                text="EDAM_data:3759",
                title="ProteomeXchange ID",
                description="""Identifier for mass spectrometry proteomics data in the proteomexchange.org repository."""))
        setattr(cls, "EDAM_data:3768",
            PermissibleValue(
                text="EDAM_data:3768",
                title="Clustered expression profiles",
                description="Groupings of expression profiles according to a clustering algorithm."))
        setattr(cls, "EDAM_data:3769",
            PermissibleValue(
                text="EDAM_data:3769",
                title="BRENDA ontology concept ID",
                description="An identifier of a concept from the BRENDA ontology."))
        setattr(cls, "EDAM_data:3779",
            PermissibleValue(
                text="EDAM_data:3779",
                title="Annotated text",
                description="""A text (such as a scientific article), annotated with notes, data and metadata, such as recognised entities, concepts, and their relations."""))
        setattr(cls, "EDAM_data:3786",
            PermissibleValue(
                text="EDAM_data:3786",
                title="Query script",
                description="A structured query, in form of a script, that defines a database search task."))
        setattr(cls, "EDAM_data:3805",
            PermissibleValue(
                text="EDAM_data:3805",
                title="3D EM Map",
                description="Structural 3D model (volume map) from electron microscopy."))
        setattr(cls, "EDAM_data:3806",
            PermissibleValue(
                text="EDAM_data:3806",
                title="3D EM Mask",
                description="""Annotation on a structural 3D EM Map from electron microscopy. This might include one or several locations in the map of the known features of a particular macromolecule."""))
        setattr(cls, "EDAM_data:3807",
            PermissibleValue(
                text="EDAM_data:3807",
                title="EM Movie",
                description="Raw DDD movie acquisition from electron microscopy."))
        setattr(cls, "EDAM_data:3808",
            PermissibleValue(
                text="EDAM_data:3808",
                title="EM Micrograph",
                description="Raw acquisition from electron microscopy or average of an aligned DDD movie."))
        setattr(cls, "EDAM_data:3842",
            PermissibleValue(
                text="EDAM_data:3842",
                title="Molecular simulation data",
                description="""Data coming from molecular simulations, computer \"experiments\" on model molecules.
Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic)."""))
        setattr(cls, "EDAM_data:3856",
            PermissibleValue(
                text="EDAM_data:3856",
                title="RNA central ID",
                description="""Identifier of an entry from the RNA central database of annotated human miRNAs.
There are canonical and taxon-specific forms of RNAcentral ID. Canonical form e.g. urs_9or10digits identifies an RNA sequence (within the RNA central database) which may appear in multiple sequences. Taxon-specific form identifies a sequence in the specific taxon (e.g. urs_9or10digits_taxonID)."""))
        setattr(cls, "EDAM_data:3861",
            PermissibleValue(
                text="EDAM_data:3861",
                title="Electronic health record",
                description="""A human-readable systematic collection of patient (or population) health information in a digital format."""))
        setattr(cls, "EDAM_data:3869",
            PermissibleValue(
                text="EDAM_data:3869",
                title="Simulation",
                description="""Data coming from molecular simulations, computer \"experiments\" on model molecules. Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic)."""))
        setattr(cls, "EDAM_data:3870",
            PermissibleValue(
                text="EDAM_data:3870",
                title="Trajectory data",
                description="""Dynamic information of a structure molecular system coming from a molecular simulation: XYZ 3D coordinates (sometimes with their associated velocities) for every atom along time."""))
        setattr(cls, "EDAM_data:3871",
            PermissibleValue(
                text="EDAM_data:3871",
                title="Forcefield parameters",
                description="""Force field parameters: charges, masses, radii, bond lengths, bond dihedrals, etc. define the structural molecular system, and are essential for the proper description and simulation of a molecular system."""))
        setattr(cls, "EDAM_data:3872",
            PermissibleValue(
                text="EDAM_data:3872",
                title="Topology data",
                description="""Static information of a structure molecular system that is needed for a molecular simulation: the list of atoms, their non-bonded parameters for Van der Waals and electrostatic interactions, and the complete connectivity in terms of bonds, angles and dihedrals."""))
        setattr(cls, "EDAM_data:3905",
            PermissibleValue(
                text="EDAM_data:3905",
                title="Histogram",
                description="""Visualization of distribution of quantitative data, e.g. expression data, by histograms, violin plots and density plots."""))
        setattr(cls, "EDAM_data:3914",
            PermissibleValue(
                text="EDAM_data:3914",
                title="Quality control report",
                description="Report of the quality control review that was made of factors involved in a procedure."))
        setattr(cls, "EDAM_data:3917",
            PermissibleValue(
                text="EDAM_data:3917",
                title="Count matrix",
                description="""A table of unnormalized values representing summarised read counts per genomic region (e.g. gene, transcript, peak)."""))
        setattr(cls, "EDAM_data:3924",
            PermissibleValue(
                text="EDAM_data:3924",
                title="DNA structure alignment",
                description="Alignment (superimposition) of DNA tertiary (3D) structures."))
        setattr(cls, "EDAM_data:3932",
            PermissibleValue(
                text="EDAM_data:3932",
                title="Q-value",
                description="""A score derived from the P-value to ensure correction for multiple tests. The Q-value provides an estimate of the positive False Discovery Rate (pFDR), i.e. the rate of false positives among all the cases reported positive: pFDR = FP / (FP + TP).
Q-values are widely used in high-throughput data analysis (e.g. detection of differentially expressed genes from transcriptome data)."""))
        setattr(cls, "EDAM_data:3949",
            PermissibleValue(
                text="EDAM_data:3949",
                title="Profile HMM",
                description="""A profile HMM is a variant of a Hidden Markov model that is derived specifically from a set of (aligned) biological sequences. Profile HMMs provide the basis for a position-specific scoring system, which can be used to align sequences and search databases for related sequences."""))
        setattr(cls, "EDAM_data:3952",
            PermissibleValue(
                text="EDAM_data:3952",
                title="Pathway ID (WikiPathways)",
                description="Identifier of a pathway from the WikiPathways pathway database."))
        setattr(cls, "EDAM_data:3953",
            PermissibleValue(
                text="EDAM_data:3953",
                title="Pathway overrepresentation data",
                description="""A ranked list of pathways, each associated with z-score, p-value or similar, concerning or derived from the analysis of e.g. a set of genes or proteins."""))
        setattr(cls, "EDAM_data:4022",
            PermissibleValue(
                text="EDAM_data:4022",
                title="ORCID Identifier",
                description="""Identifier of a researcher registered with the ORCID database. Used to identify author IDs."""))
        setattr(cls, "EDAM_data:4040",
            PermissibleValue(
                text="EDAM_data:4040",
                title="Data management plan",
                description="""Data management plan is a document describing the data management of a project or an organisation, including acquisition, reuse, structure, processing, storage, documentation, sharing, and preservation of data. This may include budgeting for these operations."""))

class EnumFileHashType(EnumDefinitionImpl):
    """
    Types of file hashes supported.
    """
    md5 = PermissibleValue(
        text="md5",
        title="MD5")
    etag = PermissibleValue(
        text="etag",
        title="ETag")
    sha1 = PermissibleValue(
        text="sha1",
        title="SHA-1")

    _defn = EnumDefinition(
        name="EnumFileHashType",
        description="Types of file hashes supported.",
    )

# Slots
class slots:
    pass

slots.requiredClass__id = Slot(uri=CAM.id, name="requiredClass__id", curie=CAM.curie('id'),
                   model_uri=CAM.requiredClass__id, domain=None, range=Optional[str])

slots.requiredClass__full_name = Slot(uri=CAM.full_name, name="requiredClass__full_name", curie=CAM.curie('full_name'),
                   model_uri=CAM.requiredClass__full_name, domain=None, range=Optional[str])

slots.requiredClass__aliases = Slot(uri=CAM.aliases, name="requiredClass__aliases", curie=CAM.curie('aliases'),
                   model_uri=CAM.requiredClass__aliases, domain=None, range=Optional[str])

slots.requiredClass__phone = Slot(uri=CAM.phone, name="requiredClass__phone", curie=CAM.curie('phone'),
                   model_uri=CAM.requiredClass__phone, domain=None, range=Optional[str])

slots.requiredClass__age = Slot(uri=CAM.age, name="requiredClass__age", curie=CAM.curie('age'),
                   model_uri=CAM.requiredClass__age, domain=None, range=Optional[str])
