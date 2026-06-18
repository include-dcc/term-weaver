from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.11.0"
version = "None"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'default_prefix': 'cam',
     'default_range': 'string',
     'description': 'LinkML Schema for the Common Access Model Expanded Enums',
     'id': 'https://includedcc.org/cam-expanded-enums',
     'imports': ['linkml:types',
                 'EnumDataUsePermission',
                 'EnumDataUseModifier',
                 'EnumProgram',
                 'EnumResearchDomain',
                 'EnumParticipantLifespanStage',
                 'EnumStudyDesign',
                 'EnumClinicalDataSourceType',
                 'EnumDataCategory',
                 'EnumSubjectType',
                 'EnumSex',
                 'EnumRace',
                 'EnumEthnicity',
                 'EnumVitalStatus',
                 'EnumNull',
                 'EnumFamilyType',
                 'EnumConsanguinityAssertion',
                 'EnumAssertionProvenance',
                 'EnumAvailabilityStatus',
                 'EnumSampleCollectionMethod',
                 'EnumSite',
                 'EnumSpatialQualifiers',
                 'EnumLaterality',
                 'EnumEDAMFormats',
                 'EnumEDAMDataTypes',
                 'EnumFileHashType'],
     'license': 'MIT',
     'name': 'cam-expanded-enums',
     'prefixes': {'DUO': {'prefix_prefix': 'DUO',
                          'prefix_reference': 'http://purl.obolibrary.org/obo/DUO_'},
                  'HP': {'prefix_prefix': 'HP',
                         'prefix_reference': 'http://purl.obolibrary.org/obo/HP_'},
                  'MONDO': {'prefix_prefix': 'MONDO',
                            'prefix_reference': 'http://purl.obolibrary.org/obo/MONDO_'},
                  'NCIT': {'prefix_prefix': 'NCIT',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/NCIT_'},
                  'PATO': {'prefix_prefix': 'PATO',
                           'prefix_reference': 'http://purl.obolibrary.org/obo/PATO_'},
                  'cam': {'prefix_prefix': 'cam',
                          'prefix_reference': 'https://includedcc.org/common-access-model/'},
                  'cdc_race_eth': {'prefix_prefix': 'cdc_race_eth',
                                   'prefix_reference': 'urn:oid:2.16.840.1.113883.6.238/'},
                  'hl7_null': {'prefix_prefix': 'hl7_null',
                               'prefix_reference': 'http://terminology.hl7.org/CodeSystem/v3-NullFlavor/'},
                  'ig2_biospecimen_availability': {'prefix_prefix': 'ig2_biospecimen_availability',
                                                   'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/biospecimen-availability/'},
                  'ig2dac': {'prefix_prefix': 'ig2dac',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-code/'},
                  'ig2dat': {'prefix_prefix': 'ig2dat',
                             'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-access-type/'},
                  'ig_dob_method': {'prefix_prefix': 'ig_dob_method',
                                    'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/research-data-date-of-birth-method/'},
                  'igcondtype': {'prefix_prefix': 'igcondtype',
                                 'prefix_reference': 'https://nih-ncpi.github.io/ncpi-fhir-ig-2/CodeSystem/condition-type/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'mesh': {'prefix_prefix': 'mesh',
                           'prefix_reference': 'http://id.nlm.nih.gov/mesh/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'snomed_ct': {'prefix_prefix': 'snomed_ct',
                                'prefix_reference': 'http://snomed.info/id/'}},
     'see_also': ['https://includedcc.github.io/common-access-model'],
     'source_file': 'src/cam_expanded_enums/schema/cam_expanded_enums.yaml',
     'title': 'Common Access Model Expanded Enums'} )

class EnumDataUsePermission(str, Enum):
    """
    Data Use Ontology (DUO) terms for data use permissions.
    """
    no_restriction = "DUO:0000004"
    """
    This data use permission indicates there is no restriction on use.
    """
    health_or_medical_or_biomedical_research = "DUO:0000006"
    """
    This data use permission indicates that use is allowed for health/medical/biomedical purposes; does not include the study of population origins or ancestry.
    """
    disease_specific_research = "DUO:0000007"
    """
    This data use permission indicates that use is allowed provided it is related to the specified disease.
    This term should be coupled with a term describing a disease from an ontology to specify the disease the restriction applies to. 

    DUO recommends MONDO be used, to provide the basis for automated evaluation. For more information see https://github.com/EBISPOT/DUO/blob/master/MONDO_Overview.md

    Other resources, such as the Disease Ontology, HPO, SNOMED-CT or others, can also be used. When those other resources are being used, this may require an extra mapping step to leverage automated matching algorithms.
    """
    population_origins_or_ancestry_research_only = "DUO:0000011"
    """
    This data use permission indicates that use of the data is limited to the study of population origins or ancestry.
    """
    general_research_use = "DUO:0000042"
    """
    This data use permission indicates that use is allowed for general research use for any research purpose.
    This includes but is not limited to: health/medical/biomedical purposes, fundamental biology research, the study of population origins or ancestry, statistical methods and algorithms development, and social-sciences research.
    """


class EnumDataUseModifier(str, Enum):
    """
    Data Use Ontology (DUO) terms for data use modifiers.
    """
    population_origins_or_ancestry_research_prohibited = "DUO:00000044"
    """
    This data use modifier indicates use for purposes of population, origin, or ancestry research is prohibited.
    """
    research_specific_restrictions = "DUO:0000012"
    """
    This data use modifier indicates that use is limited to studies of a certain research type.
    """
    no_general_methods_research = "DUO:0000015"
    """
    This data use modifier indicates that use does not allow methods development research (e.g., development of software or algorithms).
    """
    genetic_studies_only = "DUO:0000016"
    """
    This data use modifier indicates that use is limited to genetic studies only (i.e., studies that include genotype research alone or both genotype and phenotype research, but not phenotype research exclusively)
    """
    not_for_profit_non_commercial_use_only = "DUO:0000018"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organizations and not-for-profit use, non-commercial use.
    """
    publication_required = "DUO:0000019"
    """
    This data use modifier indicates that requestor agrees to make results of studies using the data available to the larger scientific community.
    """
    collaboration_required = "DUO:0000020"
    """
    This could be coupled with a string describing the primary study investigator(s).
    This data use modifier indicates that the requestor must agree to collaboration with the primary study investigator(s).
    """
    ethics_approval_required = "DUO:0000021"
    """
    This data use modifier indicates that the requestor must provide documentation of local IRB/ERB approval.
    """
    geographical_restriction = "DUO:0000022"
    """
    This data use modifier indicates that use is limited to within a specific geographic region.
    This should be coupled with an ontology term describing the geographical location the restriction applies to.
    """
    publication_moratorium = "DUO:0000024"
    """
    This data use modifier indicates that requestor agrees not to publish results of studies until a specific date.
    This should be coupled with a date specified as ISO8601
    """
    time_limit_on_use = "DUO:0000025"
    """
    This data use modifier indicates that use is approved for a specific number of months.
    This should be coupled with an integer value indicating the number of months.
    """
    user_specific_restriction = "DUO:0000026"
    """
    This data use modifier indicates that use is limited to use by approved users.
    """
    project_specific_restriction = "DUO:0000027"
    """
    This data use modifier indicates that use is limited to use within an approved project.
    """
    institution_specific_restriction = "DUO:0000028"
    """
    This data use modifier indicates that use is limited to use within an approved institution.
    """
    return_to_database_or_resource = "DUO:0000029"
    """
    This data use modifier indicates that the requestor must return derived/enriched data to the database/resource.
    """
    clinical_care_use = "DUO:0000043"
    """
    Clinical Care is defined as Health care or services provided at home, in a healthcare facility or hospital. Data may be used for clinical decision making.
    This data use modifier indicates that use is allowed for clinical use and care.
    """
    not_for_profit_organisation_use_only = "DUO:0000045"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit organizations.
    """
    non_commercial_use_only = "DUO:0000046"
    """
    This data use modifier indicates that use of the data is limited to not-for-profit use.
    This indicates that data can be used by commercial organisations for research purposes, but not commercial purposes.
    """


class EnumProgram(str, Enum):
    """
    Funding programs relevant to inform operations.
    """
    INCLUDE = "include"
    KF = "kf"
    Other = "other"


class EnumResearchDomain(str, Enum):
    """
    Domains of Research used to find studies.
    """
    Behavior_and_Behavior_Mechanisms = "behavior_and_behavior_mechanisms"
    Congenital_Heart_Defects = "congenital_heart_defects"
    Immune_System_Diseases = "immune_system_diseases"
    Hematologic_Diseases = "hematologic_diseases"
    Neurodevelopment = "neurodevelopment"
    Sleep_Wake_Disorders = "sleep_wake_disorders"
    All_Co_occurring_Conditions = "all_co_occurring_conditions"
    Physical_Fitness = "physical_fitness"
    Other = "other"


class EnumParticipantLifespanStage(str, Enum):
    """
    Stages of life during which participants may be recruited.
    """
    Fetal = "fetal"
    """
    Before birth
    """
    Neonatal = "neonatal"
    """
    0-28 days old
    """
    Pediatric = "pediatric"
    """
    Birth-17 years old
    """
    Adult = "adult"
    """
    18+ years old
    """


class EnumStudyDesign(str, Enum):
    """
    Approaches for collecting data, investigating interventions, and/or analyzing data.
    """
    Case_Control = "case_control"
    Case_Set = "case_set"
    Control_Set = "control_set"
    Clinical_Trial = "clinical_trial"
    Cross_Sectional = "cross_sectional"
    FamilySOLIDUSTwinsSOLIDUSTrios = "family_twins_trios"
    Interventional = "interventional"
    Longitudinal = "longitudinal"
    Trial_Readiness_Study = "trial_readiness_study"
    Tumor_vs_Matched_Normal = "tumor_vs_matched_normal"


class EnumClinicalDataSourceType(str, Enum):
    """
    Approaches to ascertain clinical information about a participant.
    """
    Medical_Record = "medical_record"
    """
    Data obtained directly from medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """
    Unknown = "unknown"


class EnumDataCategory(str, Enum):
    """
    Categories of data which may be collected about participants.
    """
    Unharmonized_DemographicSOLIDUSClinical_Data = "unharmonized_demographic_clinical_data"
    Harmonized_DemographicSOLIDUSClinical_Data = "harmonized_demographic_clinical_data"
    Genomics = "genomics"
    Transcriptomics = "transcriptomics"
    Epigenomics = "epigenomics"
    Proteomics = "proteomics"
    Metabolomics = "metabolomics"
    CognitiveSOLIDUSBehavioral = "cognitive_behavioral"
    Immune_Profiling = "immune_profiling"
    Imaging = "imaging"
    Microbiome = "microbiome"
    Fitness = "fitness"
    Physical_Activity = "physical_activity"
    Other = "other"
    Sleep_Study = "sleep_study"


class EnumSubjectType(str, Enum):
    """
    Types of Subject entities
    """
    participant = "participant"
    """
    Study participant with consent, assent, or waiver of consent.
    """
    non_participant = "non_participant"
    """
    An individual associated with a study who was not explictly consented, eg, the subject of a reported family history.
    """
    cell_line = "cell_line"
    """
    Cell Line
    """
    animal_model = "animal_model"
    """
    Animal model
    """
    group = "group"
    """
    A group of individuals or entities.
    """
    other = "other"
    """
    A different entity type- ideally this will be resolved!
    """


class EnumSex(str, Enum):
    """
    Subject Sex
    """
    Female = "female"
    Male = "male"
    Other = "other"
    Unknown = "unknown"


class EnumRace(str, Enum):
    """
    Participant Race
    """
    American_Indian_or_Alaska_Native = "american_indian_or_alaska_native"
    Asian = "asian"
    Black_or_African_American = "black_or_african_american"
    More_than_one_race = "more_than_one_race"
    Native_Hawaiian_or_Other_Pacific_Islander = "native_hawaiian_or_other_pacific_islander"
    Other = "other"
    White = "white"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"
    East_Asian = "east_asian"
    """
    UK only; do not use for US data
    """
    Latin_American = "latin_american"
    """
    UK only; do not use for US data
    """
    Middle_Eastern_or_North_African = "middle_eastern_or_north_african"
    """
    UK only; do not use for US data
    """
    South_Asian = "south_asian"
    """
    UK only; do not use for US data
    """


class EnumEthnicity(str, Enum):
    """
    Participant ethnicity, specific to Hispanic or Latino.
    """
    Hispanic_or_Latino = "hispanic_or_latino"
    Not_Hispanic_or_Latino = "not_hispanic_or_latino"
    Prefer_not_to_answer = "prefer_not_to_answer"
    Unknown = "unknown"


class EnumVitalStatus(str, Enum):
    """
    Descriptions of a Subject's vital status
    """
    Dead = "dead"
    Alive = "alive"


class EnumNull(str, Enum):
    """
    Base enumeration providing null options.
    """
    Unknown = "unknown"


class EnumFamilyType(str, Enum):
    """
    Enumerations describing research family type
    """
    Control_only = "control_only"
    """
    Control Only
    """
    Duo = "duo"
    """
    Duo
    """
    Proband_only = "proband_only"
    """
    Proband Only
    """
    Trio = "trio"
    """
    Trio (2 parents and affected child)
    """
    TrioPLUS_SIGN = "trio_plus"
    """
    2 Parents and 2 or more children
    """


class EnumConsanguinityAssertion(str, Enum):
    """
    Asserts known or suspected consanguinity in this study family
    """
    not_suspected = "not_suspected"
    """
    Not suspected
    """
    suspected = "suspected"
    """
    Suspected
    """
    known_present = "known_present"
    """
    Known Present
    """
    unknown = "unknown"
    """
    Unknown
    """


class EnumAssertionProvenance(str, Enum):
    """
    Possible data sources for assertions.
    """
    Medical_Record = "medical_record"
    """
    Data obtained from a medical record
    """
    Investigator_Assessment = "investigator_assessment"
    """
    Data obtained by examination, interview, etc. with investigator
    """
    Participant_or_Caregiver_Report = "participant_or_caregiver_report"
    """
    Data obtained from survey, questionnaire, etc. filled out by participant or caregiver
    """
    Other = "other"
    """
    Data obtained from other source, such as tissue bank
    """


class EnumAvailabilityStatus(str, Enum):
    """
    Is the biospecimen available for use?
    """
    Available = "available"
    """
    Biospecimen is Available
    """
    Unavailable = "unavailable"
    """
    Biospecimen is Unavailable
    """


class EnumSampleCollectionMethod(str):
    """
    The approach used to collect the biospecimen. [LOINC](https://loinc.org) is recommended.
    """
    pass


class EnumSite(str):
    """
    The location of the specimen collection. [SNOMED Body Site](https://hl7.org/fhir/R4B/valueset-body-site.html) is recommended.
    """
    pass


class EnumSpatialQualifiers(str, Enum):
    """
    Any spatial/location qualifiers.
    """
    Topographical_modifier_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:106233006"
    """
    Topographical modifier (qualifier value)
    """
    Long_axis = "SNOMED:103339001"
    Short_axis = "SNOMED:103340004"
    Off_axis = "SNOMED:103341000"
    Mid_longitudinal = "SNOMED:103342007"
    Parasagittal = "SNOMED:103343002"
    Transvesical = "SNOMED:103344008"
    Transthecal = "SNOMED:103345009"
    Transsplenic = "SNOMED:103346005"
    Transrenal = "SNOMED:103347001"
    Transpleural = "SNOMED:103348006"
    Transpancreatic = "SNOMED:103349003"
    Transgastric = "SNOMED:103353001"
    Transmural = "SNOMED:103354007"
    Capsular = "SNOMED:11070000"
    Arcuate = "SNOMED:1146002"
    Intermediate = "SNOMED:11896004"
    Non_adjacent = "SNOMED:1217011006"
    Intra_articular = "SNOMED:131183008"
    Area_of_defined_region = "SNOMED:131184002"
    Vertical_long_axis = "SNOMED:131185001"
    Horizontal_long_axis = "SNOMED:131186000"
    Major_Axis = "SNOMED:131187009"
    Minor_Axis = "SNOMED:131188004"
    Perpendicular_axis = "SNOMED:131189007"
    Radius = "SNOMED:131190003"
    Perimeter = "SNOMED:131191004"
    Peripheral = "SNOMED:14414005"
    Angular = "SNOMED:1483009"
    Juxta_posed = "SNOMED:18769003"
    Hemispheric = "SNOMED:21006006"
    Over = "SNOMED:21481007"
    Horizontal = "SNOMED:24020000"
    Right_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:24028007"
    """
    Right (qualifier value)
    """
    Axial = "SNOMED:24422004"
    Horizontal___3_and_9 = "SNOMED:255527003"
    Horizontal_and_vertical = "SNOMED:255528008"
    Mediolateral = "SNOMED:261129000"
    Central = "SNOMED:26216008"
    Superficial = "SNOMED:26283006"
    Bony_extra_articular = "SNOMED:263687007"
    Bony_intra_articular = "SNOMED:263688002"
    Lateral_to_the_left = "SNOMED:264731004"
    Lateral_to_the_right = "SNOMED:264732006"
    Linear_longitudinal = "SNOMED:264733001"
    Linear_transverse = "SNOMED:264737000"
    Posterolateral_to_the_left = "SNOMED:264741001"
    Posterolateral_to_the_right = "SNOMED:264742008"
    Horizontal_cleavage = "SNOMED:264839005"
    Triangular = "SNOMED:27237009"
    Rhomboid = "SNOMED:28241006"
    Right_curve = "SNOMED:28947002"
    Sagittal = "SNOMED:30730003"
    Quadrangular = "SNOMED:30899007"
    Portal = "SNOMED:32381004"
    Preaxial = "SNOMED:32400000"
    Vertical = "SNOMED:33096000"
    Efferent = "SNOMED:33843005"
    Behind = "SNOMED:350722008"
    Below = "SNOMED:351726001"
    Supra_ = "SNOMED:352730000"
    Upward = "SNOMED:353734004"
    Circular = "SNOMED:354652004"
    Surrounding = "SNOMED:355648006"
    Anterolateral = "SNOMED:37197008"
    Longitudinal = "SNOMED:38717003"
    Bent = "SNOMED:39187007"
    Proximal = "SNOMED:40415009"
    Regional = "SNOMED:410674003"
    Surface = "SNOMED:410679008"
    Area = "SNOMED:42798000"
    Apical = "SNOMED:43674008"
    Cylindrical = "SNOMED:45226003"
    Distal = "SNOMED:46053002"
    Left_curve = "SNOMED:47021000"
    Lateral = "SNOMED:49370004"
    Afferent = "SNOMED:49530007"
    Linear = "SNOMED:50009006"
    Stellate = "SNOMED:50362007"
    Junctional = "SNOMED:50974003"
    Right_and_left = "SNOMED:51440002"
    Remote = "SNOMED:5686001"
    Square = "SNOMED:56924007"
    Along_edge = "SNOMED:57183005"
    Basal = "SNOMED:57195005"
    Rectangular = "SNOMED:59410002"
    Curved = "SNOMED:60301000"
    Postaxial = "SNOMED:60583000"
    Subcapsular = "SNOMED:61397002"
    Sectional = "SNOMED:62083003"
    Segmental = "SNOMED:62372003"
    Transverse = "SNOMED:62824007"
    Cephalic = "SNOMED:66787007"
    Gutter = "SNOMED:68493006"
    Extracellular = "SNOMED:69320009"
    Saccular = "SNOMED:69389007"
    Incisal = "SNOMED:710097009"
    Occlusal = "SNOMED:710098004"
    Mesial = "SNOMED:710099007"
    Left_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:7771000"
    """
    Left (qualifier value)
    """
    Deep = "SNOMED:795002"
    Coronal = "SNOMED:81654009"
    Intracellular = "SNOMED:83167003"
    Straddling = "SNOMED:84177009"
    Extra_articular = "SNOMED:87687004"
    Posterolateral = "SNOMED:90069004"
    Relative_sites_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:272424004"
    """
    Relative sites (qualifier value)
    """
    Marginal = "SNOMED:112233002"
    Intercostal = "SNOMED:1197041002"
    Intralobular = "SNOMED:1285325005"
    Anatomical_reference_point_of_right_atrium = "SNOMED:128590009"
    Inlet_projection = "SNOMED:1362012009"
    Unilobar = "SNOMED:1363295008"
    Ipsilateral_multilobar = "SNOMED:1363296009"
    Side = "SNOMED:182353008"
    Sublingual = "SNOMED:225780003"
    Intra_arterial = "SNOMED:229801003"
    Ipsilateral = "SNOMED:255208005"
    Contralateral = "SNOMED:255209002"
    Inframammary = "SNOMED:255348000"
    Panretinal = "SNOMED:255472009"
    Left_upper_segment = "SNOMED:255482005"
    Lower_segment = "SNOMED:255486008"
    Right_lower_segment = "SNOMED:255496004"
    Right_upper_segment = "SNOMED:255499006"
    Upper_segment = "SNOMED:255501003"
    Underlay = "SNOMED:255546002"
    Overlay = "SNOMED:255547006"
    Sandwich_graft = "SNOMED:255548001"
    Anterior = "SNOMED:255549009"
    Anterior_to_epiglottis = "SNOMED:255550009"
    Posterior = "SNOMED:255551008"
    Posterior_to_epiglottis = "SNOMED:255552001"
    Dorsal = "SNOMED:255554000"
    Intracerebral = "SNOMED:255557007"
    Intragastric = "SNOMED:255558002"
    Intramuscular = "SNOMED:255559005"
    Intravenous = "SNOMED:255560000"
    Medial = "SNOMED:255561001"
    Mid = "SNOMED:255562008"
    Mid_zone = "SNOMED:255563003"
    Perivascular = "SNOMED:255564009"
    Peripapillary = "SNOMED:255565005"
    Postauricular = "SNOMED:255567002"
    Retrosternal = "SNOMED:255568007"
    Suprasternal = "SNOMED:255569004"
    Palatal_lingual = "SNOMED:255579002"
    Septal = "SNOMED:255584008"
    Drug_in_contact_with_skin = "SNOMED:255690001"
    Via_collaterals = "SNOMED:258186003"
    Via_native_vessel___graft_impaired = "SNOMED:258187007"
    Via_native_vessel___graft_occluded = "SNOMED:258188002"
    Via_skip_graft = "SNOMED:258189005"
    Supratentorial = "SNOMED:258329003"
    Infratentorial = "SNOMED:258330008"
    Interdental = "SNOMED:260240005"
    number_1_oAPOSTROPHEclock_position = "SNOMED:260318004"
    number_1FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260319007"
    number_10_oAPOSTROPHEclock_position = "SNOMED:260322009"
    number_10FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260323004"
    number_11_oAPOSTROPHEclock_position = "SNOMED:260324005"
    number_11FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260325006"
    number_12_oAPOSTROPHEclock_position = "SNOMED:260326007"
    number_12FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260327003"
    number_2_oAPOSTROPHEclock_position = "SNOMED:260328008"
    number_2FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260329000"
    number_3_oAPOSTROPHEclock_position = "SNOMED:260330005"
    number_3FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260331009"
    number_4_oAPOSTROPHEclock_position = "SNOMED:260333007"
    number_4FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260334001"
    number_5_oAPOSTROPHEclock_position = "SNOMED:260335000"
    number_5FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260336004"
    number_6_oAPOSTROPHEclock_position = "SNOMED:260337008"
    number_6FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260338003"
    number_7_oAPOSTROPHEclock_position = "SNOMED:260339006"
    number_7FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260340008"
    number_8_oAPOSTROPHEclock_position = "SNOMED:260341007"
    number_8FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260342000"
    number_9_oAPOSTROPHEclock_position = "SNOMED:260343005"
    number_9FULL_STOP30_oAPOSTROPHEclock_position = "SNOMED:260344004"
    Projection = "SNOMED:260419006"
    Left_lateral_oblique = "SNOMED:260421001"
    C1_C2_left_oblique = "SNOMED:260422008"
    Right_lateral_oblique = "SNOMED:260424009"
    C1_C2_right_oblique = "SNOMED:260425005"
    Medial_oblique = "SNOMED:260426006"
    Oblique_lateral = "SNOMED:260427002"
    Mandible_X_ray___lateral_oblique = "SNOMED:260428007"
    Anteroposterior_left_lateral_decubitus = "SNOMED:260430009"
    C1_C2_left_lateral = "SNOMED:260431008"
    Left_true_lateral = "SNOMED:260432001"
    Anteroposterior_right_lateral_decubitus = "SNOMED:260434000"
    C1_C2_right_lateral = "SNOMED:260435004"
    Right_true_lateral = "SNOMED:260436003"
    Lateral_vertical_beam = "SNOMED:260437007"
    Lateral_horizontal_beam = "SNOMED:260438002"
    Lateral_inverted = "SNOMED:260439005"
    True_lateral_of_mandible = "SNOMED:260440007"
    Frog_lateral = "SNOMED:260441006"
    Erect_lateral = "SNOMED:260442004"
    Anteroposterior_inverted = "SNOMED:260443009"
    Rotated_posteroanterior = "SNOMED:260444003"
    Posteroanterior_20_degree = "SNOMED:260445002"
    Posteroanterior_in_ulnar_deviation = "SNOMED:260446001"
    Penetrated_posteroanterior = "SNOMED:260447005"
    Lordotic_projection = "SNOMED:260450008"
    Supine_decubitus = "SNOMED:260451007"
    Decubitus = "SNOMED:260452000"
    InternalSOLIDUSexternal_rotation = "SNOMED:260453005"
    number_45_degree_projection = "SNOMED:260454004"
    Head_and_neck_projection = "SNOMED:260455003"
    Slit_TowneAPOSTROPHEs = "SNOMED:260458001"
    Reverse_TowneAPOSTROPHEs = "SNOMED:260459009"
    Slit_35_degree_fronto_occipital = "SNOMED:260460004"
    Vertex_projection = "SNOMED:260461000"
    Left_StenverAPOSTROPHEs = "SNOMED:260463002"
    Right_StenverAPOSTROPHEs = "SNOMED:260464008"
    Occipitofrontal_projection = "SNOMED:260465009"
    Occipitomental_projection = "SNOMED:260466005"
    Occipitomental___erect = "SNOMED:260467001"
    Occipitomental___tilted = "SNOMED:260468006"
    Occipitomental___prone = "SNOMED:260469003"
    Occipitomental___15_degree = "SNOMED:260470002"
    Occipitomental___30_degree = "SNOMED:260471003"
    Occipitomental___45_degree = "SNOMED:260472005"
    Waters___35_degree_tilt_to_radiographic_baseline = "SNOMED:260473000"
    Submentovertical_reduced_exposure_for_zygomatic_arches = "SNOMED:260475007"
    Slit_submentovertical = "SNOMED:260476008"
    DentalSOLIDUSoral_projection = "SNOMED:260477004"
    Body___molar = "SNOMED:260478009"
    Body___premolar = "SNOMED:260479001"
    Ramus_projection = "SNOMED:260481004"
    Bimolar_projection = "SNOMED:260482006"
    Transpharyngeal_projection = "SNOMED:260483001"
    Transmaxillary_projection = "SNOMED:260484007"
    Temporomandibular_joint_setting = "SNOMED:260485008"
    Maxillary_sinus_setting = "SNOMED:260486009"
    Dental_panoramic = "SNOMED:260487000"
    Implant_setting_projection = "SNOMED:260489002"
    Segmental_setting = "SNOMED:260490006"
    Axial_view_for_sesamoid_bones = "SNOMED:260491005"
    BrewertonAPOSTROPHEs_projection = "SNOMED:260492003"
    Harris_Beath_axial_projection = "SNOMED:260493008"
    Intercondylar_projection = "SNOMED:260494002"
    Judet_projection = "SNOMED:260496000"
    Mortice_projection = "SNOMED:260497009"
    Occlusal_projection = "SNOMED:260499007"
    Projected_oblique_occlusal = "SNOMED:260500003"
    Lower_true_occlusal = "SNOMED:260501004"
    Power_grip_series = "SNOMED:260502006"
    Radial_head_projection = "SNOMED:260503001"
    Skyline_projection = "SNOMED:260504007"
    Van_Rosen_projection = "SNOMED:260506009"
    Via_body_reference_line = "SNOMED:260514003"
    Extracorporeal = "SNOMED:260520002"
    Internal = "SNOMED:260521003"
    Median = "SNOMED:260528009"
    Vectors = "SNOMED:260529001"
    Via_body_region = "SNOMED:260530006"
    Thoracoabdominal = "SNOMED:260532003"
    Lateral_extrapleural = "SNOMED:260535001"
    Nasopancreatic = "SNOMED:260541008"
    Endobronchial = "SNOMED:260544000"
    Orogastric = "SNOMED:260549005"
    Via_cardiovascular_system = "SNOMED:260568008"
    Via_superficialized_vessel_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:260602004"
    Postaural_approach = "SNOMED:260620008"
    Sublabial_transseptal = "SNOMED:260637001"
    Extraperitoneal = "SNOMED:260641002"
    Retroperitoneal = "SNOMED:260642009"
    Venovenous = "SNOMED:260668002"
    Anterior_dorsal = "SNOMED:261045000"
    Aortocoronary = "SNOMED:261052003"
    Arterio_arterial = "SNOMED:261054002"
    Arteriovenous = "SNOMED:261055001"
    Between_intestinal_loops = "SNOMED:261057009"
    Bicoronal = "SNOMED:261059007"
    Circumareolar = "SNOMED:261065007"
    Dorsal_part = "SNOMED:261067004"
    Epicardial = "SNOMED:261073003"
    External = "SNOMED:261074009"
    Extra_amniotic = "SNOMED:261075005"
    Extracoronal = "SNOMED:261076006"
    Inferior = "SNOMED:261089000"
    Into_urinary_bladder = "SNOMED:261094000"
    Into_ureter = "SNOMED:261095004"
    Intracoronal = "SNOMED:261097007"
    Intraperitoneal = "SNOMED:261100002"
    Intravascular = "SNOMED:261101003"
    Laryngotracheal = "SNOMED:261117009"
    Lateral_part = "SNOMED:261119007"
    Lower = "SNOMED:261122009"
    Lower_anterior = "SNOMED:261123004"
    Medial_part = "SNOMED:261128008"
    Midaxillary = "SNOMED:261131009"
    Midclavicular = "SNOMED:261132002"
    Middle_third = "SNOMED:261133007"
    Mural = "SNOMED:261136004"
    Musculocutaneous = "SNOMED:261137008"
    Para_aortic = "SNOMED:261146002"
    Paracolic = "SNOMED:261147006"
    Paraspinal = "SNOMED:261148001"
    Parasternal = "SNOMED:261149009"
    Penis_and_urinary_bladder_neck = "SNOMED:261154000"
    Periadrenal = "SNOMED:261156003"
    Posterior_dorsal = "SNOMED:261165005"
    Proximal_third = "SNOMED:261172006"
    Retrocecal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:261174007"
    Retroduodenal = "SNOMED:261175008"
    Tracheobronchial = "SNOMED:261181000"
    Upper = "SNOMED:261183002"
    Upper_anterior = "SNOMED:261184008"
    Venoarterial = "SNOMED:261185009"
    Ventral_part = "SNOMED:261186005"
    Distal_third = "SNOMED:261411001"
    Transpulmonary_annulus = "SNOMED:261446009"
    Via_intrapulmonary_trunk_tunnel = "SNOMED:261466000"
    Via_orbitotomy = "SNOMED:261469007"
    Deep_to_rectus_abdominis = "SNOMED:261760007"
    Exteriorized_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:261788001"
    From_existing_graft_to_coronary_artery = "SNOMED:261799004"
    Intracervical = "SNOMED:261847009"
    Internally_to_bladder = "SNOMED:261851006"
    Mixed_venoarterial_and_venovenous = "SNOMED:261945002"
    Muscle_fibers_only_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:261964008"
    Neuromuscular_junction_only = "SNOMED:261980003"
    Dominant_side = "SNOMED:262379005"
    Non_dominant_side = "SNOMED:262458006"
    Anocutaneous = "SNOMED:263672002"
    Anovestibular = "SNOMED:263674001"
    Foraminal = "SNOMED:263759007"
    Left_side_by_side = "SNOMED:263794000"
    Left_sided = "SNOMED:263795004"
    Panacinar = "SNOMED:263830001"
    Panlobular = "SNOMED:263831002"
    Periacinar = "SNOMED:263838008"
    Prevascular = "SNOMED:263846009"
    Proximal_acinar = "SNOMED:263848005"
    Separate = "SNOMED:263869007"
    Subcutaneous = "SNOMED:263887005"
    Above_middle_turbinate = "SNOMED:263938007"
    Anterior_segment = "SNOMED:263942005"
    Anterior_wall = "SNOMED:263943000"
    Periorbital = "SNOMED:263952009"
    Perioral = "SNOMED:263953004"
    Atlantoaxial = "SNOMED:263955006"
    Between_left_common_carotid_and_brachiocephalic_arteries = "SNOMED:263958008"
    Between_left_subclavian_and_common_carotid_arteries = "SNOMED:263959000"
    Bronchocutaneous = "SNOMED:263965000"
    Bronchopleural = "SNOMED:263966004"
    Centriacinar = "SNOMED:263969006"
    Centrilobular = "SNOMED:263970007"
    Cervicothoracic = "SNOMED:263974003"
    Cervicothoracolumbar = "SNOMED:263975002"
    Distal_to_left_subclavian_artery = "SNOMED:263981005"
    Duodenoduodenal = "SNOMED:263990003"
    Duodenojejunal = "SNOMED:263991004"
    Extrafoveal = "SNOMED:263996009"
    Extraureteric = "SNOMED:263997000"
    Extravaginal = "SNOMED:263998005"
    From_anterosuperior_superior_bridging_leaflet_commissure = "SNOMED:263999002"
    From_left_inferior_bridging_leaflet_lateral_commissure = "SNOMED:264000000"
    From_left_septal_commissure = "SNOMED:264001001"
    From_left_superior_bridging_leaflet_lateral_commissure = "SNOMED:264002008"
    From_left_ventricular_component = "SNOMED:264004009"
    From_right_anterosuperior_inferior_commissure = "SNOMED:264005005"
    From_right_inferior_bridging_leaflet_inferior_commissure = "SNOMED:264006006"
    From_right_septal_commissure = "SNOMED:264007002"
    From_right_ventricular_component = "SNOMED:264008007"
    Gastroduodenal = "SNOMED:264011008"
    Gastrogastric = "SNOMED:264012001"
    Hepatopleural = "SNOMED:264015004"
    Ileocecal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264023002"
    Ileocolic = "SNOMED:264024008"
    Iliofemoral_vein_zone = "SNOMED:264025009"
    Ileo_ileal = "SNOMED:264026005"
    Ileorectal = "SNOMED:264027001"
    In_joint = "SNOMED:264030008"
    In_situ = "SNOMED:264031007"
    Infracardiac = "SNOMED:264034004"
    Infravesical = "SNOMED:264035003"
    Interchordal = "SNOMED:264040006"
    Interdigital = "SNOMED:264041005"
    Intervertebral = "SNOMED:264042003"
    Intraligamentous = "SNOMED:264043008"
    Intracardiac = "SNOMED:264044002"
    Intraluminal = "SNOMED:264045001"
    Intramammary = "SNOMED:264046000"
    Intrapulmonary = "SNOMED:264047009"
    Intravaginal = "SNOMED:264049007"
    Lateral_column = "SNOMED:264056001"
    Lateral_segment = "SNOMED:264060003"
    Left_anterior = "SNOMED:264065008"
    Left_lateral_wall = "SNOMED:264067000"
    Left_lower_segment = "SNOMED:264068005"
    Lower_left_parasternal = "SNOMED:264076007"
    Lower_third = "SNOMED:264081003"
    Lumbosacral = "SNOMED:264083000"
    Medial_segment = "SNOMED:264096004"
    Midtarsal = "SNOMED:264103001"
    Paravertebral = "SNOMED:264107000"
    Esophagocolonic_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264110007"
    Esophagogastric_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264111006"
    Esophagojejunal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264112004"
    Ostium = "SNOMED:264114003"
    Paraesophageal_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264117005"
    Paraduodenal = "SNOMED:264118000"
    Parafoveal = "SNOMED:264119008"
    Paramacular = "SNOMED:264121003"
    Paraseptal = "SNOMED:264123000"
    Paraumbilical = "SNOMED:264124006"
    Paravascular = "SNOMED:264126008"
    Paraovarian = "SNOMED:264127004"
    Paratracheal = "SNOMED:264128009"
    Peri_intestinal = "SNOMED:264131005"
    Perianal = "SNOMED:264133008"
    Perihepatic = "SNOMED:264136000"
    Perinephric = "SNOMED:264137009"
    Peripancreatic = "SNOMED:264139007"
    Perisplenic = "SNOMED:264142001"
    Posterior_pole = "SNOMED:264153007"
    Posterior_segment = "SNOMED:264154001"
    Posterior_wall = "SNOMED:264159006"
    Rectocloacal = "SNOMED:264168008"
    Rectocutaneous = "SNOMED:264169000"
    Rectourethral = "SNOMED:264170004"
    Rectovaginal = "SNOMED:264171000"
    Rectovesical = "SNOMED:264172007"
    Rectovulval = "SNOMED:264173002"
    Retromammary = "SNOMED:264174008"
    Retrocolumellar = "SNOMED:264175009"
    Right_anterior = "SNOMED:264176005"
    Right_lateral_wall = "SNOMED:264178006"
    Right_side_by_side = "SNOMED:264179003"
    Right_sided = "SNOMED:264180000"
    Segment = "SNOMED:264193005"
    Sternocostal = "SNOMED:264201006"
    Subaortic = "SNOMED:264202004"
    Subareolar = "SNOMED:264205002"
    Subconjunctival = "SNOMED:264206001"
    Subcostal = "SNOMED:264208000"
    Subfoveal = "SNOMED:264209008"
    Superficial_to_rectus_abdominis = "SNOMED:264216009"
    Superior = "SNOMED:264217000"
    Supraumbilical = "SNOMED:264221007"
    Supracardiac = "SNOMED:264222000"
    Supraglottic = "SNOMED:264224004"
    Suprahepatic = "SNOMED:264225003"
    Tarsometatarsal = "SNOMED:264227006"
    Thoracolumbar = "SNOMED:264232007"
    Upper_left_parasternal = "SNOMED:264245006"
    Upper_third = "SNOMED:264253003"
    Cholecystoduodenal = "SNOMED:264261008"
    Cholecystenteric_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:264262001"
    Cholecystogastric = "SNOMED:264263006"
    Choledochoduodenal = "SNOMED:264264000"
    Colocolic = "SNOMED:264266003"
    Colorectal = "SNOMED:264267007"
    Epitrochlear = "SNOMED:264463009"
    Under_inferior_bridging_leaflet = "SNOMED:264940008"
    Under_superior_bridging_leaflet = "SNOMED:264941007"
    Onlay = "SNOMED:272288000"
    General_site_descriptor = "SNOMED:272425003"
    Anatomical_part_descriptor = "SNOMED:272427006"
    Anatomical_third = "SNOMED:272428001"
    Part_structure = "SNOMED:272429009"
    Column_structure = "SNOMED:272430004"
    Segment_structure = "SNOMED:272431000"
    Wall_structure = "SNOMED:272432007"
    Anatomical_relationship_descriptor = "SNOMED:272434008"
    Centri_location = "SNOMED:272435009"
    Circum_location = "SNOMED:272436005"
    Extra_location = "SNOMED:272437001"
    Extrapleural = "SNOMED:272438006"
    Infra_location = "SNOMED:272439003"
    Inter_location = "SNOMED:272440001"
    Intra_location = "SNOMED:272441002"
    Mid_location = "SNOMED:272442009"
    Pan_location = "SNOMED:272443004"
    Para_location = "SNOMED:272444005"
    Per_location = "SNOMED:272446007"
    Peri_location = "SNOMED:272447003"
    Post_location = "SNOMED:272448008"
    Pre_location = "SNOMED:272449000"
    Retro_location = "SNOMED:272450000"
    Sub_location = "SNOMED:272451001"
    Supra_location = "SNOMED:272452008"
    Inferosuperior_projection = "SNOMED:272455005"
    Apical_projection = "SNOMED:272456006"
    Vertical_projection = "SNOMED:272457002"
    Prone_projection = "SNOMED:272458007"
    Supine_projection = "SNOMED:272459004"
    Anterior_projection = "SNOMED:272460009"
    Right_posterior_projection = "SNOMED:272461008"
    Left_posterior_projection = "SNOMED:272462001"
    Perorbital_projection = "SNOMED:272464000"
    Temporomandibular_joint_projection = "SNOMED:272465004"
    Optic_foramen_projection = "SNOMED:272466003"
    Lateral_facial_skeleton_projection = "SNOMED:272467007"
    Ear_projection = "SNOMED:272468002"
    Mid_face_projection = "SNOMED:272469005"
    Cervical_spine_projection = "SNOMED:272470006"
    Macro_projection = "SNOMED:272472003"
    Outlet_projection = "SNOMED:272473008"
    SwimmerAPOSTROPHEs_projection = "SNOMED:272474002"
    Tibial_tuberosity_projection = "SNOMED:272475001"
    Transthoracic_projection = "SNOMED:272476000"
    Transcranial_projection = "SNOMED:272478004"
    Posteroanterior_projection = "SNOMED:272479007"
    Horizontal_projection = "SNOMED:272480005"
    Erect_projection = "SNOMED:272481009"
    Adduction_projection = "SNOMED:272482002"
    True_projection = "SNOMED:272483007"
    Contralateral_projection = "SNOMED:272484001"
    Clockface_position = "SNOMED:272485000"
    Trans_direction = "SNOMED:272486004"
    Into_structure = "SNOMED:272487008"
    From_structure = "SNOMED:272488003"
    Via_values = "SNOMED:272489006"
    Via_incision = "SNOMED:272496008"
    Epi_location = "SNOMED:276749003"
    Overlapping_sites = "SNOMED:276825009"
    Aortoiliac = "SNOMED:276979001"
    Endo_location = "SNOMED:277292000"
    Deep_locations = "SNOMED:277407002"
    Superficial_locations = "SNOMED:277409004"
    Anterior_locations = "SNOMED:277410009"
    Posterior_locations = "SNOMED:277411008"
    Proximal_locations = "SNOMED:277412001"
    Distal_locations = "SNOMED:277413006"
    Between_locations = "SNOMED:277414000"
    Above_locations = "SNOMED:277415004"
    Right_posterior = "SNOMED:277593009"
    Left_posterior = "SNOMED:277594003"
    Intrastomal = "SNOMED:277681008"
    Tubo_ovarian = "SNOMED:277685004"
    Peritubular = "SNOMED:277686003"
    Sidedness = "SNOMED:277806003"
    Limited_structures = "SNOMED:278227002"
    Posterior_projection = "SNOMED:278255003"
    Abduction_projection = "SNOMED:278267001"
    Transorbital_projection = "SNOMED:278318001"
    Periumbilical = "SNOMED:278701003"
    Transumbilical = "SNOMED:278702005"
    Subcuticular = "SNOMED:285418008"
    Orthotopic = "SNOMED:298107004"
    Heterotopic = "SNOMED:298108009"
    Ectopic = "SNOMED:298109001"
    Subfascial = "SNOMED:303218009"
    Intracranial = "SNOMED:303231004"
    Extracranial = "SNOMED:303232006"
    Subcranial = "SNOMED:303483009"
    Transannular = "SNOMED:304047000"
    Endocardial = "SNOMED:304059001"
    Low___site_descriptor = "SNOMED:306766009"
    High___site_descriptor = "SNOMED:306767000"
    Periapical = "SNOMED:312206004"
    Caudal = "SNOMED:3583002"
    Intracavitary = "SNOMED:373863008"
    Collateral_branch_of_vessel = "SNOMED:397406000"
    Vessel_origin = "SNOMED:397421006"
    Intrauterine = "SNOMED:398236008"
    Five_chamber_view = "SNOMED:398994001"
    Leonard_George_projection = "SNOMED:398996004"
    Right_ventricular_inflow_tract_view = "SNOMED:398998003"
    Mayer_projection = "SNOMED:399000008"
    Posterior_emissive_projection = "SNOMED:399001007"
    Nolke_projection = "SNOMED:399002000"
    Hughston_projection = "SNOMED:399003005"
    Oblique_axial_projection = "SNOMED:399004004"
    Miller_projection = "SNOMED:399005003"
    Left_posterior_oblique_projection = "SNOMED:399006002"
    Axillary_tail_mammography_view = "SNOMED:399011000"
    Medial_lateral_emissive_projection = "SNOMED:399012007"
    Chassard_Lapin_projection = "SNOMED:399013002"
    Pirie_projection = "SNOMED:399022001"
    May_projection = "SNOMED:399024000"
    Ischerwood_projection = "SNOMED:399025004"
    Zanelli_projection = "SNOMED:399026003"
    Clements_projection = "SNOMED:399028002"
    Frontal_projection = "SNOMED:399033003"
    Parasternal_short_axis_view_at_the_mitral_valve_level = "SNOMED:399036006"
    Lewis_projection = "SNOMED:399037002"
    Right_posterior_oblique_projection = "SNOMED:399038007"
    Cardiac_imaging_views = "SNOMED:399043000"
    Postero_anterior_oblique_projection = "SNOMED:399059000"
    Axial_projection = "SNOMED:399061009"
    Causton_projection = "SNOMED:399065000"
    Lateral_projection = "SNOMED:399067008"
    Plantodorsal_projection = "SNOMED:399071006"
    Fuchs_projection = "SNOMED:399073009"
    Left_anterior_oblique_emissive_projection = "SNOMED:399074003"
    Right_posterior_oblique_emissive_projection = "SNOMED:399075002"
    Kuchendorf_projection = "SNOMED:399080006"
    Gaynor_Hart_projection = "SNOMED:399082003"
    Hsieh_projection = "SNOMED:399083008"
    Oblique_axial_emissive_projection = "SNOMED:399089007"
    Staunig_projection = "SNOMED:399098005"
    Latero_medial_oblique_projection = "SNOMED:399099002"
    Cranio_caudal_projection_exaggerated_medially = "SNOMED:399101009"
    Friedman_projection = "SNOMED:399103007"
    Suprasternal_long_axis_view = "SNOMED:399106004"
    Right_anterior_oblique_emissive_projection = "SNOMED:399108003"
    Tangential_projection = "SNOMED:399110001"
    Eponymous_projection = "SNOMED:399113004"
    Left_lateral_emissive_projection = "SNOMED:399118008"
    Twining_projection = "SNOMED:399125001"
    Teufel_projection = "SNOMED:399127009"
    Holly_projection = "SNOMED:399129007"
    West_Point_projection = "SNOMED:399130002"
    Frontal_oblique_axial_projection = "SNOMED:399132005"
    Left_anterior_oblique_projection = "SNOMED:399135007"
    Left_posterior_oblique_emissive_projection = "SNOMED:399136008"
    Penner_projection = "SNOMED:399138009"
    Parasternal_long_axis_view = "SNOMED:399139001"
    Albers_Schönberg_projection = "SNOMED:399142007"
    Suprasternal_short_axis_view = "SNOMED:399145009"
    Grashey_projection = "SNOMED:399146005"
    Chamberlain_projection = "SNOMED:399148006"
    Kandel_projection = "SNOMED:399152006"
    Laquerriere_Pierquin_projection = "SNOMED:399156009"
    NorgaardAPOSTROPHEs_projection = "SNOMED:399157000"
    Latero_medial_oblique_emissive_projection = "SNOMED:399159002"
    Frontal_oblique_projection = "SNOMED:399160007"
    Cleavage_mammography_view = "SNOMED:399161006"
    Cranio_caudal_projection = "SNOMED:399162004"
    Magnified_projection = "SNOMED:399163009"
    Hough_projection = "SNOMED:399168000"
    Lauenstein_projection = "SNOMED:399169008"
    Ottonello_projection = "SNOMED:399171008"
    Left_lateral_projection = "SNOMED:399173006"
    Lawrence_projection = "SNOMED:399179005"
    Pawlow_projection = "SNOMED:399181007"
    Oblique_projection = "SNOMED:399182000"
    Left_oblique_projection = "SNOMED:399184004"
    Superolateral_to_inferomedial_oblique_projection = "SNOMED:399188001"
    Cranio_caudal_projection_exaggerated_laterally = "SNOMED:399192008"
    Right_ventricular_outflow_tract_view = "SNOMED:399195005"
    Caudo_cranial_projection = "SNOMED:399196006"
    Right_lateral_projection = "SNOMED:399198007"
    Henschen_projection = "SNOMED:399199004"
    Subcostal_short_axis_view = "SNOMED:399200001"
    Judd_projection = "SNOMED:399201002"
    Law_projection = "SNOMED:399206007"
    Camp_Coventry_projection = "SNOMED:399212002"
    Apical_four_chamber_view = "SNOMED:399214001"
    Wigby_Taylor_projection = "SNOMED:399215000"
    Arcelin_projection = "SNOMED:399218003"
    Oblique_caudo_cranial_projection = "SNOMED:399225005"
    Kemp_Harper_projection = "SNOMED:399227002"
    Apical_two_chamber_view = "SNOMED:399232001"
    Rhese_projection = "SNOMED:399234000"
    Right_oblique_projection = "SNOMED:399236003"
    Alexander_projection = "SNOMED:399237007"
    Parasternal_short_axis_view_at_the_aortic_valve_level = "SNOMED:399239005"
    Titterington_projection = "SNOMED:399241006"
    Acanthioparietal_projection = "SNOMED:399242004"
    Settegast_projection = "SNOMED:399243009"
    Cleaves_projection = "SNOMED:399245002"
    Blackett_Healy_projection = "SNOMED:399246001"
    Tarrant_projection = "SNOMED:399247005"
    Lorenz_projection = "SNOMED:399251007"
    Submentovertical_projection = "SNOMED:399255003"
    Mediolateral_projection = "SNOMED:399260004"
    Beclere_projection = "SNOMED:399263002"
    Exaggerated_cranio_caudal_projection = "SNOMED:399265009"
    Medio_lateral_oblique_emissive_projection = "SNOMED:399268006"
    TowneAPOSTROPHEs_projection = "SNOMED:399270002"
    Parasternal_short_axis_view_at_the_papillary_muscle_level = "SNOMED:399271003"
    Parietoacanthial_projection = "SNOMED:399272005"
    Sagittal_oblique_axial_emissive_projection = "SNOMED:399273000"
    Hickey_projection = "SNOMED:399277004"
    Cahoon_projection = "SNOMED:399278009"
    Kasabach_projection = "SNOMED:399280003"
    Fleischner_projection = "SNOMED:399281004"
    Merchant_projection = "SNOMED:399284007"
    Holmblad_projection = "SNOMED:399285008"
    Oblique_cranio_caudal_projection = "SNOMED:399288005"
    Schüller_projection = "SNOMED:399290006"
    Stecher_projection = "SNOMED:399292003"
    Taylor_projection = "SNOMED:399296000"
    Right_lateral_emissive_projection = "SNOMED:399297009"
    Lateral_medial_emissive_projection = "SNOMED:399300004"
    Dunlap_projection = "SNOMED:399303002"
    Parasternal_short_axis_view = "SNOMED:399306005"
    Lindblom_projection = "SNOMED:399308006"
    Subcostal_long_axis_view = "SNOMED:399310008"
    Grandy_projection = "SNOMED:399311007"
    Antero_posterior_oblique_projection = "SNOMED:399312000"
    Swanson_projection = "SNOMED:399313005"
    Parieto_orbital_projection = "SNOMED:399316002"
    Kovacs_projection = "SNOMED:399318001"
    Clements_Nakayama_projection = "SNOMED:399320003"
    Anterior_emissive_projection = "SNOMED:399321004"
    Sagittal_oblique_axial_projection = "SNOMED:399325008"
    Low_Beer_projection = "SNOMED:399327000"
    Valdini_projection = "SNOMED:399330007"
    Kurzbauer_projection = "SNOMED:399332004"
    Dorsoplantar_projection = "SNOMED:399335002"
    Apical_long_axis = "SNOMED:399339008"
    Haas_projection = "SNOMED:399341009"
    Lilienfeld_projection = "SNOMED:399342002"
    Broden_projection = "SNOMED:399344001"
    Antero_posterior_projection = "SNOMED:399348003"
    StenverAPOSTROPHEs_projection = "SNOMED:399349006"
    Orbito_parietal_projection = "SNOMED:399351005"
    Lateral_medial_projection = "SNOMED:399352003"
    Chausse_projection = "SNOMED:399355001"
    Right_anterior_oblique_projection = "SNOMED:399356000"
    Caldwell_projection = "SNOMED:399358004"
    Verticosubmental_projection = "SNOMED:399360002"
    Nuclear_medicine_projection = "SNOMED:399361003"
    Bertel_projection = "SNOMED:399362005"
    Pearson_projection = "SNOMED:399365007"
    Medio_lateral_oblique_projection = "SNOMED:399368009"
    Lysholm_projection = "SNOMED:399370000"
    Parasternal_short_axis_view_at_the_level_of_the_mitral_chords = "SNOMED:399371001"
    Ferguson_projection = "SNOMED:399372008"
    Midline_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:399488007"
    """
    Midline (qualifier value)
    """
    Cranial_LAO = "SNOMED:408723005"
    Caudal_LAO = "SNOMED:408724004"
    Cranial_RAO = "SNOMED:408725003"
    Caudal_RAO = "SNOMED:408726002"
    Bottom = "SNOMED:421610009"
    Top = "SNOMED:421812003"
    Rafert_Long_projection = "SNOMED:422534007"
    Moore_projection = "SNOMED:422568001"
    Apple_projection = "SNOMED:422670003"
    Neer_projection = "SNOMED:422795009"
    Burman_projection = "SNOMED:422861003"
    Stryker_projection = "SNOMED:422954003"
    Wolf_projection = "SNOMED:422996004"
    Colcher_Sussman_projection = "SNOMED:423091003"
    Rafer_projection = "SNOMED:423720000"
    Hirtz_Modification_projection = "SNOMED:424086005"
    Eraso_Modification_projection = "SNOMED:424655003"
    Danelius_Miller_projection = "SNOMED:424811006"
    Fisk_projection = "SNOMED:424962005"
    Kite_projection = "SNOMED:425030002"
    Robert_projection = "SNOMED:425035007"
    Rosenberg_projection = "SNOMED:425042007"
    Folio_projection = "SNOMED:425157002"
    Garth_projection = "SNOMED:425188003"
    Dorsopalmar_projection = "SNOMED:441505008"
    Inferomedial_to_superolateral_oblique_view = "SNOMED:441555000"
    Dorso_ventral_projection = "SNOMED:441672003"
    Mammography_view = "SNOMED:441753009"
    Stereoscopic_view = "SNOMED:442361004"
    Ventro_dorsal_projection = "SNOMED:442441009"
    Axillary_tissue_mammography_view = "SNOMED:442580003"
    Nipple_in_profile_mammography_view = "SNOMED:442581004"
    Infra_mammary_fold_mammography_view = "SNOMED:442593008"
    Right_stereoscopic_view = "SNOMED:442594002"
    Left_stereoscopic_view = "SNOMED:442640004"
    Stereoscopic_view_incremented_from_baseline = "SNOMED:442653001"
    Stereoscopic_view_decremented_from_baseline = "SNOMED:442667005"
    Parasternal_long_axis_view_of_right_ventricular_inflow_tract = "SNOMED:443082005"
    Parasternal_long_axis_view_of_right_ventricular_outflow_tract = "SNOMED:443083000"
    Subcostal_view_of_cardiac_outlets_directed_anteriorly = "SNOMED:443100003"
    Subcostal_short_axis_view_at_papillary_muscle_level = "SNOMED:443160001"
    Suprasternal_coronal_view = "SNOMED:443162009"
    Suprasternal_sagittal_view = "SNOMED:443163004"
    Transgastric_short_axis_view = "SNOMED:443293000"
    Intramedullary = "SNOMED:443459002"
    Subcostal_short_axis_view_at_mitral_valve_level = "SNOMED:443499004"
    Subcostal_short_axis_view_at_venous_inflow_level = "SNOMED:443500008"
    Suprasternal_long_axis_view_of_aortic_arch = "SNOMED:443562002"
    Subcostal_short_axis_view_at_aortic_valve_level = "SNOMED:443609003"
    Subcostal_oblique_coronal_view = "SNOMED:443640005"
    Transesophageal_four_chamber_view_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:443662005"
    Transesophageal_short_axis_view_LEFT_PARENTHESISqualifier_valueRIGHT_PARENTHESIS = "SNOMED:443698002"
    Contiguous = "SNOMED:65424008"
    Unilateral = "SNOMED:66459002"
    Common = "SNOMED:72906007"
    Dorsoventral = "SNOMED:741000124103"
    Dorsolateral = "SNOMED:761000124104"
    Ventrolateral = "SNOMED:771000124106"
    Palmar = "SNOMED:781000124109"


class EnumLaterality(str):
    """
    Laterality information for the site
    """
    pass


class EnumEDAMFormats(str, Enum):
    """
    Data formats from the EDAM ontology.
    """
    Format = "EDAM:format_1915"
    """
    Format
    """
    SMILES = "EDAM_format:1196"
    """
    Chemical structure specified in Simplified Molecular Input Line Entry System (SMILES) line notation.
    """
    InChI = "EDAM_format:1197"
    """
    Chemical structure specified in IUPAC International Chemical Identifier (InChI) line notation.
    """
    mf = "EDAM_format:1198"
    """
    Chemical structure specified by Molecular Formula (MF), including a count of each element in a compound.
    The general MF query format consists of a series of valid atomic symbols, with an optional number or range.
    """
    InChIKey = "EDAM_format:1199"
    """
    An InChIKey identifier is not human- nor machine-readable but is more suitable for web searches than an InChI chemical structure specification.
    The InChIKey (hashed InChI) is a fixed length (25 character) condensed digital representation of an InChI chemical structure specification. It uniquely identifies a chemical compound.
    """
    smarts = "EDAM_format:1200"
    """
    SMILES ARbitrary Target Specification (SMARTS) format for chemical structure specification, which is a subset of the SMILES line notation.
    """
    unambiguous_pure = "EDAM_format:1206"
    """
    Alphabet for a molecular sequence with possible unknown positions but without ambiguity or non-sequence characters.
    """
    nucleotide = "EDAM_format:1207"
    """
    Alphabet for a nucleotide sequence with possible ambiguity, unknown positions and non-sequence characters.
    Non-sequence characters may be used for example for gaps.
    """
    protein = "EDAM_format:1208"
    """
    Alphabet for a protein sequence with possible ambiguity, unknown positions and non-sequence characters.
    Non-sequence characters may be used for gaps and translation stop.
    """
    consensus = "EDAM_format:1209"
    """
    Alphabet for the consensus of two or more molecular sequences.
    """
    pure_nucleotide = "EDAM_format:1210"
    """
    Alphabet for a nucleotide sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_nucleotide = "EDAM_format:1211"
    """
    Alphabet for a nucleotide sequence (characters ACGTU only) with possible unknown positions but without ambiguity or non-sequence characters .
    """
    dna = "EDAM_format:1212"
    """
    Alphabet for a DNA sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    rna = "EDAM_format:1213"
    """
    Alphabet for an RNA sequence with possible ambiguity, unknown positions and non-sequence characters.
    """
    unambiguous_pure_dna = "EDAM_format:1214"
    """
    Alphabet for a DNA sequence (characters ACGT only) with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_dna = "EDAM_format:1215"
    """
    Alphabet for a DNA sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_rna_sequence = "EDAM_format:1216"
    """
    Alphabet for an RNA sequence (characters ACGU only) with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_rna = "EDAM_format:1217"
    """
    Alphabet for an RNA sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    unambiguous_pure_protein = "EDAM_format:1218"
    """
    Alphabet for any protein sequence with possible unknown positions but without ambiguity or non-sequence characters.
    """
    pure_protein = "EDAM_format:1219"
    """
    Alphabet for any protein sequence with possible ambiguity and unknown positions but without non-sequence characters.
    """
    EMBL_feature_location = "EDAM_format:1248"
    """
    Format for sequence positions (feature location) as used in DDBJ/EMBL/GenBank database.
    """
    quicktandem = "EDAM_format:1295"
    """
    Report format for tandem repeats in a nucleotide sequence (format generated by the Sanger Centre quicktandem program).
    """
    Sanger_inverted_repeats = "EDAM_format:1296"
    """
    Report format for inverted repeats in a nucleotide sequence (format generated by the Sanger Centre inverted program).
    """
    EMBOSS_repeat = "EDAM_format:1297"
    """
    Report format for tandem repeats in a sequence (an EMBOSS report format).
    """
    est2genome_format = "EDAM_format:1316"
    """
    Format of a report on exon-intron structure generated by EMBOSS est2genome.
    """
    restrict_format = "EDAM_format:1318"
    """
    Report format for restriction enzyme recognition sites used by EMBOSS restrict program.
    """
    restover_format = "EDAM_format:1319"
    """
    Report format for restriction enzyme recognition sites used by EMBOSS restover program.
    """
    REBASE_restriction_sites = "EDAM_format:1320"
    """
    Report format for restriction enzyme recognition sites used by REBASE database.
    """
    FASTA_search_results_format = "EDAM_format:1332"
    """
    Format of results of a sequence database search using FASTA.
    This includes (typically) score data, alignment data and a histogram (of observed and expected distribution of E values.)
    """
    BLAST_results = "EDAM_format:1333"
    """
    Format of results of a sequence database search using some variant of BLAST.
    This includes score data, alignment data and summary table.
    """
    mspcrunch = "EDAM_format:1334"
    """
    Format of results of a sequence database search using some variant of MSPCrunch.
    """
    Smith_Waterman_format = "EDAM_format:1335"
    """
    Format of results of a sequence database search using some variant of Smith Waterman.
    """
    dhf = "EDAM_format:1336"
    """
    Format of EMBASSY domain hits file (DHF) of hits (sequences) with domain classification information.
    The hits are relatives to a SCOP or CATH family and are found from a search of a sequence database.
    """
    lhf = "EDAM_format:1337"
    """
    Format of EMBASSY ligand hits file (LHF) of database hits (sequences) with ligand classification information.
    The hits are putative ligand-binding sequences and are found from a search of a sequence database.
    """
    InterPro_hits_format = "EDAM_format:1341"
    """
    Results format for searches of the InterPro database.
    """
    InterPro_protein_view_report_format = "EDAM_format:1342"
    """
    Format of results of a search of the InterPro database showing matches of query protein sequence(s) to InterPro entries.
    The report includes a classification of regions in a query protein sequence which are assigned to a known InterPro protein family or group.
    """
    InterPro_match_table_format = "EDAM_format:1343"
    """
    Format of results of a search of the InterPro database showing matches between protein sequence(s) and signatures for an InterPro entry.
    The table presents matches between query proteins (rows) and signature methods (columns) for this entry. Alternatively the sequence(s) might be from from the InterPro entry itself. The match position in the protein sequence and match status (true positive, false positive etc) are indicated.
    """
    HMMER_Dirichlet_prior = "EDAM_format:1349"
    """
    Dirichlet distribution HMMER format.
    """
    MEME_Dirichlet_prior = "EDAM_format:1350"
    """
    Dirichlet distribution MEME format.
    """
    HMMER_emission_and_transition = "EDAM_format:1351"
    """
    Format of a report from the HMMER package on the emission and transition counts of a hidden Markov model.
    """
    prosite_pattern = "EDAM_format:1356"
    """
    Format of a regular expression pattern from the Prosite database.
    """
    EMBOSS_sequence_pattern = "EDAM_format:1357"
    """
    Format of an EMBOSS sequence pattern.
    """
    meme_motif = "EDAM_format:1360"
    """
    A motif in the format generated by the MEME program.
    """
    prosite_profile = "EDAM_format:1366"
    """
    Sequence profile (sequence classifier) format used in the PROSITE database.
    """
    JASPAR_format = "EDAM_format:1367"
    """
    A profile (sequence classifier) in the format used in the JASPAR database.
    """
    MEME_background_Markov_model = "EDAM_format:1369"
    """
    Format of the model of random sequences used by MEME.
    """
    HMMER_format = "EDAM_format:1370"
    """
    Format of a hidden Markov model representation used by the HMMER package.
    """
    HMMER_aln = "EDAM_format:1391"
    """
    FASTA-style format for multiple sequences aligned by HMMER package to an HMM.
    """
    DIALIGN_format = "EDAM_format:1392"
    """
    Format of multiple sequences aligned by DIALIGN package.
    """
    daf = "EDAM_format:1393"
    """
    EMBASSY 'domain alignment file' (DAF) format, containing a sequence alignment of protein domains belonging to the same SCOP or CATH family.
    The format is clustal-like and includes annotation of domain family classification information.
    """
    Sequence_MEME_profile_alignment = "EDAM_format:1419"
    """
    Format for alignment of molecular sequences to MEME profiles (position-dependent scoring matrices) as generated by the MAST tool from the MEME package.
    """
    HMMER_profile_alignment_LEFT_PARENTHESISsequences_versus_HMMsRIGHT_PARENTHESIS = "EDAM_format:1421"
    """
    Format used by the HMMER package for an alignment of a sequence against a hidden Markov model database.
    """
    HMMER_profile_alignment_LEFT_PARENTHESISHMM_versus_sequencesRIGHT_PARENTHESIS = "EDAM_format:1422"
    """
    Format used by the HMMER package for of an alignment of a hidden Markov model against a sequence database.
    """
    Phylip_distance_matrix = "EDAM_format:1423"
    """
    Data Type must include the distance matrix, probably as pairs of sequence identifiers with a distance (integer or float).
    Format of PHYLIP phylogenetic distance matrix data.
    """
    ClustalW_dendrogram = "EDAM_format:1424"
    """
    Dendrogram (tree file) format generated by ClustalW.
    """
    Phylip_tree_raw = "EDAM_format:1425"
    """
    Raw data file format used by Phylip from which a phylogenetic tree is directly generated or plotted.
    """
    Phylip_continuous_quantitative_characters = "EDAM_format:1430"
    """
    PHYLIP file format for continuous quantitative character data.
    """
    Phylip_character_frequencies_format = "EDAM_format:1432"
    """
    PHYLIP file format for phylogenetics character frequency data.
    """
    Phylip_discrete_states_format = "EDAM_format:1433"
    """
    Format of PHYLIP discrete states data.
    """
    Phylip_cliques_format = "EDAM_format:1434"
    """
    Format of PHYLIP cliques data.
    """
    Phylip_tree_format = "EDAM_format:1435"
    """
    Phylogenetic tree data format used by the PHYLIP program.
    """
    TreeBASE_format = "EDAM_format:1436"
    """
    The format of an entry from the TreeBASE database of phylogenetic data.
    """
    TreeFam_format = "EDAM_format:1437"
    """
    The format of an entry from the TreeFam database of phylogenetic data.
    """
    Phylip_tree_distance_format = "EDAM_format:1445"
    """
    Format for distances, such as Branch Score distance, between two or more phylogenetic trees as used by the Phylip package.
    """
    dssp = "EDAM_format:1454"
    """
    Format of an entry from the DSSP database (Dictionary of Secondary Structure in Proteins).
    The DSSP database is built using the DSSP application which defines secondary structure, geometrical features and solvent exposure of proteins, given atomic coordinates in PDB format.
    """
    hssp = "EDAM_format:1455"
    """
    Entry format of the HSSP database (Homology-derived Secondary Structure in Proteins).
    """
    Dot_bracket_format = "EDAM_format:1457"
    """
    Format of RNA secondary structure in dot-bracket notation, originally generated by the Vienna RNA package/server.
    """
    Vienna_local_RNA_secondary_structure_format = "EDAM_format:1458"
    """
    Format of local RNA secondary structure components with free energy values, generated by the Vienna RNA package/server.
    """
    PDB_database_entry_format = "EDAM_format:1475"
    """
    Format of an entry (or part of an entry) from the PDB database.
    """
    PDB = "EDAM_format:1476"
    """
    Entry format of PDB database in PDB format.
    """
    mmCIF = "EDAM_format:1477"
    """
    Entry format of PDB database in mmCIF format.
    """
    PDBML = "EDAM_format:1478"
    """
    Entry format of PDB database in PDBML (XML) format.
    """
    aaindex = "EDAM_format:1504"
    """
    Amino acid index format used by the AAindex database.
    """
    Pcons_report_format = "EDAM_format:1551"
    """
    Format of output of the Pcons Model Quality Assessment Program (MQAP).
    Pcons ranks protein models by assessing their quality based on the occurrence of recurring common three-dimensional structural patterns. Pcons returns a score reflecting the overall global quality and a score for each individual residue in the protein reflecting the local residue quality.
    """
    ProQ_report_format = "EDAM_format:1552"
    """
    Format of output of the ProQ protein model quality predictor.
    ProQ is a neural network-based predictor that predicts the quality of a protein model based on the number of structural features.
    """
    findkm = "EDAM_format:1582"
    """
    A report format for the kinetics of enzyme-catalysed reaction(s) in a format generated by EMBOSS findkm. This includes Michaelis Menten plot, Hanes Woolf plot, Michaelis Menten constant (Km) and maximum velocity (Vmax).
    """
    Primer3_primer = "EDAM_format:1627"
    """
    Report format on PCR primers and hybridisation oligos as generated by Whitehead primer3 program.
    """
    ABI = "EDAM_format:1628"
    """
    A format of raw sequence read data from an Applied Biosystems sequencing machine.
    """
    mira = "EDAM_format:1629"
    """
    Format of MIRA sequence trace information file.
    """
    CAF = "EDAM_format:1630"
    """
    Common Assembly Format (CAF). A sequence assembly format including contigs, base-call qualities, and other metadata.
    """
    EXP = "EDAM_format:1631"
    """
    Sequence assembly project file EXP format.
    """
    SCF = "EDAM_format:1632"
    """
    Staden Chromatogram Files format (SCF) of base-called sequence reads, qualities, and other metadata.
    """
    PHD = "EDAM_format:1633"
    """
    PHD sequence trace format to store serialised chromatogram data (reads).
    """
    dat = "EDAM_format:1637"
    """
    Format of Affymetrix data file of raw image data.
    """
    cel = "EDAM_format:1638"
    """
    Format of Affymetrix data file of information about (raw) expression levels of the individual probes.
    """
    affymetrix = "EDAM_format:1639"
    """
    Format of affymetrix gene cluster files (hc-genes.txt, hc-chips.txt) from hierarchical clustering.
    """
    affymetrix_exp = "EDAM_format:1641"
    """
    Affymetrix data file format for information about experimental conditions and protocols.
    """
    CHP = "EDAM_format:1644"
    """
    Format of Affymetrix data file of information about (normalised) expression levels of the individual probes.
    """
    Taverna_workflow_format = "EDAM_format:1665"
    """
    Format of Taverna workflows.
    """
    HET_group_dictionary_entry_format = "EDAM_format:1705"
    """
    The format of an entry from the HET group dictionary (HET groups from PDB files).
    """
    PubMed_citation = "EDAM_format:1734"
    """
    Format of bibliographic reference as used by the PubMed database.
    """
    Medline_Display_Format = "EDAM_format:1735"
    """
    Bibliographic reference information including citation information is included
    Format for abstracts of scientific articles from the Medline database.
    """
    CiteXplore_core = "EDAM_format:1736"
    """
    CiteXplore 'core' citation format including title, journal, authors and abstract.
    """
    CiteXplore_all = "EDAM_format:1737"
    """
    CiteXplore 'all' citation format includes all known details such as Mesh terms and cross-references.
    """
    pmc = "EDAM_format:1739"
    """
    Article format of the PubMed Central database.
    """
    iHOP_format = "EDAM_format:1740"
    """
    The format of iHOP (Information Hyperlinked over Proteins) text-mining result.
    """
    OSCAR_format = "EDAM_format:1741"
    """
    OSCAR (Open-Source Chemistry Analysis Routines) software performs chemistry-specific parsing of chemical documents. It attempts to identify chemical names, ontology concepts, and chemical data from a document.
    OSCAR format of annotated chemical text.
    """
    PlasMapper_TextMap = "EDAM_format:1861"
    """
    Map of a plasmid (circular DNA) in PlasMapper TextMap format.
    """
    newick = "EDAM_format:1910"
    """
    Phylogenetic tree Newick (text) format.
    """
    TreeCon_format = "EDAM_format:1911"
    """
    Phylogenetic tree TreeCon (text) format.
    """
    Nexus_format = "EDAM_format:1912"
    """
    Phylogenetic tree Nexus (text) format.
    """
    Sequence_record_format = "EDAM_format:1919"
    """
    Data format for a molecular sequence record.
    """
    Sequence_feature_annotation_format = "EDAM_format:1920"
    """
    Data format for molecular sequence feature information.
    """
    Alignment_format = "EDAM_format:1921"
    """
    Data format for molecular sequence alignment information.
    """
    acedb = "EDAM_format:1923"
    """
    ACEDB sequence format.
    """
    codata = "EDAM_format:1925"
    """
    Codata entry format.
    """
    dbid = "EDAM_format:1926"
    """
    Fasta format variant with database name before ID.
    """
    EMBL_format = "EDAM_format:1927"
    """
    EMBL entry format.
    """
    Staden_experiment_format = "EDAM_format:1928"
    """
    Staden experiment file format.
    """
    FASTA = "EDAM_format:1929"
    """
    FASTA format including NCBI-style IDs.
    """
    FASTQ = "EDAM_format:1930"
    """
    FASTQ short read format ignoring quality scores.
    """
    FASTQ_illumina = "EDAM_format:1931"
    """
    FASTQ Illumina 1.3 short read format.
    """
    FASTQ_sanger = "EDAM_format:1932"
    """
    FASTQ short read format with phred quality.
    """
    FASTQ_solexa = "EDAM_format:1933"
    """
    FASTQ Solexa/Illumina 1.0 short read format.
    """
    fitch_program = "EDAM_format:1934"
    """
    Fitch program format.
    """
    GCG = "EDAM_format:1935"
    """
    GCG SSF (single sequence file) file format.
    GCG sequence file format.
    """
    GenBank_format = "EDAM_format:1936"
    """
    Genbank entry format.
    """
    genpept = "EDAM_format:1937"
    """
    Currently identical to refseqp format
    Genpept protein entry format.
    """
    GFF2_seq = "EDAM_format:1938"
    """
    GFF feature file format with sequence in the header.
    """
    GFF3_seq = "EDAM_format:1939"
    """
    GFF3 feature file format with sequence.
    """
    giFASTA_format = "EDAM_format:1940"
    """
    FASTA sequence format including NCBI-style GIs.
    """
    hennig86 = "EDAM_format:1941"
    """
    Hennig86 output sequence format.
    """
    ig = "EDAM_format:1942"
    """
    Intelligenetics sequence format.
    """
    igstrict = "EDAM_format:1943"
    """
    Intelligenetics sequence format (strict version).
    """
    jackknifer = "EDAM_format:1944"
    """
    Jackknifer interleaved and non-interleaved sequence format.
    """
    mase_format = "EDAM_format:1945"
    """
    Mase program sequence format.
    """
    mega_seq = "EDAM_format:1946"
    """
    Mega interleaved and non-interleaved sequence format.
    """
    GCG_MSF = "EDAM_format:1947"
    """
    GCG MSF (multiple sequence file) file format.
    """
    nbrfSOLIDUSpir = "EDAM_format:1948"
    """
    NBRF/PIR entry sequence format.
    """
    nexus_seq = "EDAM_format:1949"
    """
    Nexus/paup interleaved sequence format.
    """
    pdbatom = "EDAM_format:1950"
    """
    PDB sequence format (ATOM lines).
    pdb format in EMBOSS.
    """
    pdbatomnuc = "EDAM_format:1951"
    """
    PDB nucleotide sequence format (ATOM lines).
    pdbnuc format in EMBOSS.
    """
    pdbseqresnuc = "EDAM_format:1952"
    """
    PDB nucleotide sequence format (SEQRES lines).
    pdbnucseq format in EMBOSS.
    """
    pdbseqres = "EDAM_format:1953"
    """
    PDB sequence format (SEQRES lines).
    pdbseq format in EMBOSS.
    """
    Pearson_format = "EDAM_format:1954"
    """
    Plain old FASTA sequence format (unspecified format for IDs).
    """
    raw = "EDAM_format:1957"
    """
    Raw sequence format with no non-sequence characters.
    """
    refseqp = "EDAM_format:1958"
    """
    Currently identical to genpept format
    Refseq protein entry sequence format.
    """
    Staden_format = "EDAM_format:1960"
    """
    Staden suite sequence format.
    """
    Stockholm_format = "EDAM_format:1961"
    """
    Stockholm multiple sequence alignment format (used by Pfam and Rfam).
    """
    strider_format = "EDAM_format:1962"
    """
    DNA strider output sequence format.
    """
    UniProtKB_format = "EDAM_format:1963"
    """
    UniProtKB entry sequence format.
    """
    plain_text_format_LEFT_PARENTHESISunformattedRIGHT_PARENTHESIS = "EDAM_format:1964"
    """
    Plain text sequence format (essentially unformatted).
    """
    ASNFULL_STOP1_sequence_format = "EDAM_format:1966"
    """
    NCBI ASN.1-based sequence format.
    """
    DAS_format = "EDAM_format:1967"
    """
    DAS sequence (XML) format (any type).
    """
    dasdna = "EDAM_format:1968"
    """
    DAS sequence (XML) format (nucleotide-only).
    The use of this format is deprecated.
    """
    debug_seq = "EDAM_format:1969"
    """
    EMBOSS debugging trace sequence format of full internal data content.
    """
    jackknifernon = "EDAM_format:1970"
    """
    Jackknifer output sequence non-interleaved format.
    """
    NCBI_format = "EDAM_format:1972"
    """
    NCBI FASTA sequence format with NCBI-style IDs.
    There are several variants of this.
    """
    nexusnon = "EDAM_format:1973"
    """
    Nexus/paup non-interleaved sequence format.
    """
    GFF2 = "EDAM_format:1974"
    """
    General Feature Format (GFF) of sequence features.
    """
    GFF3 = "EDAM_format:1975"
    """
    Generic Feature Format version 3 (GFF3) of sequence features.
    """
    DASGFF = "EDAM_format:1978"
    """
    DAS GFF (XML) feature format.
    """
    debug_feat = "EDAM_format:1979"
    """
    EMBOSS debugging trace feature format of full internal data content.
    """
    ClustalW_format = "EDAM_format:1982"
    """
    ClustalW format for (aligned) sequences.
    """
    debug = "EDAM_format:1983"
    """
    EMBOSS alignment format for debugging trace of full internal data content.
    """
    FASTA_aln = "EDAM_format:1984"
    """
    Fasta format for (aligned) sequences.
    """
    markx0 = "EDAM_format:1985"
    """
    Pearson MARKX0 alignment format.
    """
    markx1 = "EDAM_format:1986"
    """
    Pearson MARKX1 alignment format.
    """
    markx10 = "EDAM_format:1987"
    """
    Pearson MARKX10 alignment format.
    """
    markx2 = "EDAM_format:1988"
    """
    Pearson MARKX2 alignment format.
    """
    markx3 = "EDAM_format:1989"
    """
    Pearson MARKX3 alignment format.
    """
    match = "EDAM_format:1990"
    """
    Alignment format for start and end of matches between sequence pairs.
    """
    mega = "EDAM_format:1991"
    """
    Mega format for (typically aligned) sequences.
    """
    meganon = "EDAM_format:1992"
    """
    Mega non-interleaved format for (typically aligned) sequences.
    """
    pair = "EDAM_format:1996"
    """
    EMBOSS simple sequence pairwise alignment format.
    """
    PHYLIP_format = "EDAM_format:1997"
    """
    Phylip format for (aligned) sequences.
    """
    PHYLIP_sequential = "EDAM_format:1998"
    """
    Phylip non-interleaved format for (aligned) sequences.
    """
    scores_format = "EDAM_format:1999"
    """
    Alignment format for score values for pairs of sequences.
    """
    selex = "EDAM_format:2000"
    """
    SELEX format for (aligned) sequences.
    """
    EMBOSS_simple_format = "EDAM_format:2001"
    """
    EMBOSS simple multiple alignment format.
    """
    srs_format = "EDAM_format:2002"
    """
    Simple multiple sequence (alignment) format for SRS.
    """
    srspair = "EDAM_format:2003"
    """
    Simple sequence pair (alignment) format for SRS.
    """
    T_Coffee_format = "EDAM_format:2004"
    """
    T-Coffee program alignment format.
    """
    TreeCon_seq = "EDAM_format:2005"
    """
    Treecon format for (aligned) sequences.
    """
    Phylogenetic_tree_format = "EDAM_format:2006"
    """
    Data format for a phylogenetic tree.
    """
    Biological_pathway_or_network_format = "EDAM_format:2013"
    """
    Data format for a biological pathway or network.
    """
    Sequence_profile_alignment_format = "EDAM_format:2014"
    """
    Data format for a sequence-profile alignment.
    """
    Amino_acid_index_format = "EDAM_format:2017"
    """
    Data format for an amino acid index.
    """
    Article_format = "EDAM_format:2020"
    """
    Data format for a full-text scientific article.
    """
    Text_mining_report_format = "EDAM_format:2021"
    """
    Data format of a report from text mining.
    """
    Enzyme_kinetics_report_format = "EDAM_format:2027"
    """
    Data format for reports on enzyme kinetics.
    """
    Chemical_data_format = "EDAM_format:2030"
    """
    Format of a report on a chemical compound.
    """
    Gene_annotation_format = "EDAM_format:2031"
    """
    Format of a report on a particular locus, gene, gene system or groups of genes.
    """
    Workflow_format = "EDAM_format:2032"
    """
    Format of a workflow.
    """
    Tertiary_structure_format = "EDAM_format:2033"
    """
    Data format for a molecular tertiary structure.
    """
    Chemical_formula_format = "EDAM_format:2035"
    """
    Text format of a chemical formula.
    """
    Phylogenetic_character_data_format = "EDAM_format:2036"
    """
    Format of raw (unplotted) phylogenetic data.
    """
    Phylogenetic_continuous_quantitative_character_format = "EDAM_format:2037"
    """
    Format of phylogenetic continuous quantitative character data.
    """
    Phylogenetic_discrete_states_format = "EDAM_format:2038"
    """
    Format of phylogenetic discrete states data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESIScliquesRIGHT_PARENTHESIS_format = "EDAM_format:2039"
    """
    Format of phylogenetic cliques data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESISinvariantsRIGHT_PARENTHESIS_format = "EDAM_format:2040"
    """
    Format of phylogenetic invariants data.
    """
    Phylogenetic_tree_report_LEFT_PARENTHESIStree_distancesRIGHT_PARENTHESIS_format = "EDAM_format:2049"
    """
    Format for phylogenetic tree distance data.
    """
    Protein_family_report_format = "EDAM_format:2052"
    """
    Format for reports on a protein family.
    """
    Protein_interaction_format = "EDAM_format:2054"
    """
    Format for molecular interaction data.
    """
    Sequence_assembly_format = "EDAM_format:2055"
    """
    Format for sequence assembly data.
    """
    Microarray_experiment_data_format = "EDAM_format:2056"
    """
    Format for information about a microarray experimental per se (not the data generated from that experiment).
    """
    Sequence_trace_format = "EDAM_format:2057"
    """
    Format for sequence trace data (i.e. including base call information).
    """
    Gene_expression_report_format = "EDAM_format:2058"
    """
    Format of a file of gene expression data, e.g. a gene expression matrix or profile.
    """
    Map_format = "EDAM_format:2060"
    """
    Format of a map of (typically one) molecular sequence annotated with features.
    """
    Nucleic_acid_features_LEFT_PARENTHESISprimersRIGHT_PARENTHESIS_format = "EDAM_format:2061"
    """
    Format of a report on PCR primers or hybridisation oligos in a nucleic acid sequence.
    """
    Protein_report_format = "EDAM_format:2062"
    """
    Format of a report of general information about a specific protein.
    """
    number_3D_1D_scoring_matrix_format = "EDAM_format:2064"
    """
    Format of a matrix of 3D-1D scores (amino acid environment probabilities).
    """
    Protein_structure_report_LEFT_PARENTHESISquality_evaluationRIGHT_PARENTHESIS_format = "EDAM_format:2065"
    """
    Format of a report on the quality of a protein three-dimensional model.
    """
    Database_hits_LEFT_PARENTHESISsequenceRIGHT_PARENTHESIS_format = "EDAM_format:2066"
    """
    Format of a report on sequence hits and associated data from searching a sequence database.
    """
    Sequence_distance_matrix_format = "EDAM_format:2067"
    """
    Format of a matrix of genetic distances between molecular sequences.
    """
    Sequence_motif_format = "EDAM_format:2068"
    """
    Format of a sequence motif.
    """
    Sequence_profile_format = "EDAM_format:2069"
    """
    Format of a sequence profile.
    """
    Hidden_Markov_model_format = "EDAM_format:2072"
    """
    Format of a hidden Markov model.
    """
    Dirichlet_distribution_format = "EDAM_format:2074"
    """
    Data format of a dirichlet distribution.
    """
    HMM_emission_and_transition_counts_format = "EDAM_format:2075"
    """
    Data format for the emission and transition counts of a hidden Markov model.
    """
    RNA_secondary_structure_format = "EDAM_format:2076"
    """
    Format for secondary structure (predicted or real) of an RNA molecule.
    """
    Protein_secondary_structure_format = "EDAM_format:2077"
    """
    Format for secondary structure (predicted or real) of a protein molecule.
    """
    Sequence_range_format = "EDAM_format:2078"
    """
    Format used to specify range(s) of sequence positions.
    """
    pure = "EDAM_format:2094"
    """
    Alphabet for molecular sequence with possible unknown positions but without non-sequence characters.
    """
    unpure = "EDAM_format:2095"
    """
    Alphabet for a molecular sequence with possible unknown positions but possibly with non-sequence characters.
    """
    unambiguous_sequence = "EDAM_format:2096"
    """
    Alphabet for a molecular sequence with possible unknown positions but without ambiguity characters.
    """
    ambiguous = "EDAM_format:2097"
    """
    Alphabet for a molecular sequence with possible unknown positions and possible ambiguity characters.
    """
    Sequence_features_LEFT_PARENTHESISrepeatsRIGHT_PARENTHESIS_format = "EDAM_format:2155"
    """
    Format used for map of repeats in molecular (typically nucleotide) sequences.
    """
    Nucleic_acid_features_LEFT_PARENTHESISrestriction_sitesRIGHT_PARENTHESIS_format = "EDAM_format:2158"
    """
    Format used for report on restriction enzyme recognition sites in nucleotide sequences.
    """
    Sequence_cluster_format = "EDAM_format:2170"
    """
    Format used for clusters of molecular sequences.
    """
    Sequence_cluster_format_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_format:2171"
    """
    Format used for clusters of protein sequences.
    """
    Sequence_cluster_format_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "EDAM_format:2172"
    """
    Format used for clusters of nucleotide sequences.
    """
    EMBL_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2181"
    """
    A text format resembling EMBL entry format.
    This concept may be used for the many non-standard EMBL-like text formats.
    """
    FASTQ_like_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2182"
    """
    A text format resembling FASTQ short read format.
    This concept may be used for non-standard FASTQ short read-like formats.
    """
    EMBLXML = "EDAM_format:2183"
    """
    XML format for EMBL entries.
    """
    cdsxml = "EDAM_format:2184"
    """
    Specific XML format for EMBL entries (only uses certain sections).
    """
    INSDSeq = "EDAM_format:2185"
    """
    INSDSeq provides the elements of a sequence as presented in the GenBank/EMBL/DDBJ-style flatfile formats, with a small amount of additional structure.
    """
    geneseq = "EDAM_format:2186"
    """
    Geneseq sequence format.
    """
    UniProt_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2187"
    """
    A text sequence format resembling uniprotkb entry format.
    """
    medline = "EDAM_format:2194"
    """
    Abstract format used by MedLine database.
    """
    Ontology_format = "EDAM_format:2195"
    """
    Format used for ontologies.
    """
    OBO_format = "EDAM_format:2196"
    """
    A serialisation format conforming to the Open Biomedical Ontologies (OBO) model.
    """
    OWL_format = "EDAM_format:2197"
    """
    A serialisation format conforming to the Web Ontology Language (OWL) model.
    """
    FASTA_like_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2200"
    """
    A text format resembling FASTA format.
    This concept may also be used for the many non-standard FASTA-like formats.
    """
    EMBL_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2204"
    """
    An XML format for EMBL entries.
    This is a placeholder for other more specific concepts. It should not normally be used for annotation.
    """
    GenBank_like_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2205"
    """
    A text format resembling GenBank entry (plain text) format.
    This concept may be used for the non-standard GenBank-like text formats.
    """
    Sequence_feature_table_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2206"
    """
    Text format for a sequence feature table.
    """
    STRING_entry_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2304"
    """
    Entry format (XML) for the STRING database of protein interaction.
    """
    GFF = "EDAM_format:2305"
    """
    GFF feature format (of indeterminate version).
    """
    GTF = "EDAM_format:2306"
    """
    Gene Transfer Format (GTF), a restricted version of GFF.
    """
    FASTA_HTML = "EDAM_format:2310"
    """
    FASTA format wrapped in HTML elements.
    """
    EMBL_HTML = "EDAM_format:2311"
    """
    EMBL entry format wrapped in HTML elements.
    """
    Textual_format = "EDAM_format:2330"
    """
    Data in text format can be compressed into binary format, or can be a value of an XML element or attribute. Markup formats are not considered textual (or more precisely, not plain-textual).
    Textual format.
    """
    HTML = "EDAM_format:2331"
    """
    HTML format.
    """
    XML = "EDAM_format:2332"
    """
    Data in XML format can be serialised into text, or binary format.
    eXtensible Markup Language (XML) format.
    """
    Binary_format = "EDAM_format:2333"
    """
    Binary format.
    Only specific native binary formats are listed under 'Binary format' in EDAM. Generic binary formats - such as any data being zipped, or any XML data being serialised into the Efficient XML Interchange (EXI) format - are not modelled in EDAM. Refer to http://wsio.org/compression_004.
    """
    Format_LEFT_PARENTHESISby_type_of_dataRIGHT_PARENTHESIS = "EDAM_format:2350"
    """
    A placeholder concept for visual navigation by dividing data formats by the content of the data that is represented.
    This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. The concept branch under 'Format (typed)' provides an alternative organisation of the concepts nested under the other top-level branches ('Binary', 'HTML', 'RDF', 'Text' and 'XML'. All concepts under here are already included under those branches.
    """
    BioXSD_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2352"
    """
    'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioXSD in XML' is the XML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.
    BioXSD-schema-based XML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, Web services, and object-oriented programming.
    """
    RDF_format = "EDAM_format:2376"
    """
    A serialisation format conforming to the Resource Description Framework (RDF) model.
    """
    GenBank_HTML = "EDAM_format:2532"
    """
    Genbank entry format wrapped in HTML elements.
    """
    EMBL_like_format = "EDAM_format:2543"
    """
    A format resembling EMBL entry (plain text) format.
    This concept may be used for the many non-standard EMBL-like formats.
    """
    FASTQ_like_format = "EDAM_format:2545"
    """
    A format resembling FASTQ short read format.
    This concept may be used for non-standard FASTQ short read-like formats.
    """
    FASTA_like = "EDAM_format:2546"
    """
    A format resembling FASTA format.
    This concept may be used for the many non-standard FASTA-like formats.
    """
    uniprotkb_like_format = "EDAM_format:2547"
    """
    A sequence format resembling uniprotkb entry format.
    """
    Sequence_feature_table_format = "EDAM_format:2548"
    """
    Format for a sequence feature table.
    """
    OBO = "EDAM_format:2549"
    """
    OBO ontology text format.
    """
    OBO_XML = "EDAM_format:2550"
    """
    OBO ontology XML format.
    """
    Sequence_record_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2551"
    """
    Data format for a molecular sequence record (text).
    """
    Sequence_record_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2552"
    """
    Data format for a molecular sequence record (XML).
    """
    Sequence_feature_table_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2553"
    """
    XML format for a sequence feature table.
    """
    Alignment_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2554"
    """
    Text format for molecular sequence alignment information.
    """
    Alignment_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2555"
    """
    XML format for molecular sequence alignment information.
    """
    Phylogenetic_tree_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2556"
    """
    Text format for a phylogenetic tree.
    """
    Phylogenetic_tree_format_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2557"
    """
    XML format for a phylogenetic tree.
    """
    EMBL_like_LEFT_PARENTHESISXMLRIGHT_PARENTHESIS = "EDAM_format:2558"
    """
    An XML format resembling EMBL entry format.
    This concept may be used for the any non-standard EMBL-like XML formats.
    """
    GenBank_like_format = "EDAM_format:2559"
    """
    A format resembling GenBank entry (plain text) format.
    This concept may be used for the non-standard GenBank-like formats.
    """
    Sequence_assembly_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:2561"
    """
    Text format for sequence assembly data.
    """
    completely_unambiguous = "EDAM_format:2566"
    """
    Alphabet for a molecular sequence without any unknown positions or ambiguity characters.
    """
    completely_unambiguous_pure = "EDAM_format:2567"
    """
    Alphabet for a molecular sequence without unknown positions, ambiguity or non-sequence characters.
    """
    completely_unambiguous_pure_nucleotide = "EDAM_format:2568"
    """
    Alphabet for a nucleotide sequence (characters ACGTU only) without unknown positions, ambiguity or non-sequence characters .
    """
    completely_unambiguous_pure_dna = "EDAM_format:2569"
    """
    Alphabet for a DNA sequence (characters ACGT only) without unknown positions, ambiguity or non-sequence characters.
    """
    completely_unambiguous_pure_rna_sequence = "EDAM_format:2570"
    """
    Alphabet for an RNA sequence (characters ACGU only) without unknown positions, ambiguity or non-sequence characters.
    """
    Raw_sequence_format = "EDAM_format:2571"
    """
    Format of a raw molecular sequence (i.e. the alphabet used).
    """
    BAM = "EDAM_format:2572"
    """
    BAM format, the binary, BGZF-formatted compressed version of SAM format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
    """
    SAM = "EDAM_format:2573"
    """
    Sequence Alignment/Map (SAM) format for alignment of nucleotide sequences (e.g. sequencing reads) to (a) reference sequence(s). May contain base-call and alignment qualities and other data.
    The format supports short and long reads (up to 128Mbp) produced by different sequencing platforms and is used to hold mapped data within the GATK and across the Broad Institute, the Sanger Centre, and throughout the 1000 Genomes project.
    """
    SBML = "EDAM_format:2585"
    """
    Systems Biology Markup Language (SBML), the standard XML format for models of biological processes such as for example metabolism, cell signaling, and gene regulation.
    """
    completely_unambiguous_pure_protein = "EDAM_format:2607"
    """
    Alphabet for any protein sequence without unknown positions, ambiguity or non-sequence characters.
    """
    Bibliographic_reference_format = "EDAM_format:2848"
    """
    Format of a bibliographic reference.
    """
    Sequence_annotation_track_format = "EDAM_format:2919"
    """
    Format of a sequence annotation track.
    """
    Alignment_format_LEFT_PARENTHESISpair_onlyRIGHT_PARENTHESIS = "EDAM_format:2920"
    """
    Data format for molecular sequence alignment information that can hold sequence alignment(s) of only 2 sequences.
    """
    Sequence_variation_annotation_format = "EDAM_format:2921"
    """
    Format of sequence variation annotation.
    """
    markx0_variant = "EDAM_format:2922"
    """
    Some variant of Pearson MARKX alignment format.
    """
    mega_variant = "EDAM_format:2923"
    """
    Some variant of Mega format for (typically aligned) sequences.
    """
    Phylip_format_variant = "EDAM_format:2924"
    """
    Some variant of Phylip format for (aligned) sequences.
    """
    AB1 = "EDAM_format:3000"
    """
    AB1 binary format of raw DNA sequence reads (output of Applied Biosystems' sequencing analysis software). Contains an electropherogram and the DNA base sequence.
    AB1 uses the generic binary Applied Biosystems, Inc. Format (ABIF).
    """
    ACE = "EDAM_format:3001"
    """
    ACE sequence assembly format including contigs, base-call qualities, and other metadata (version Aug 1998 and onwards).
    """
    BED = "EDAM_format:3003"
    """
    BED detail format includes 2 additional columns (http://genome.ucsc.edu/FAQ/FAQformat#format1.7) and BED 15 includes 3 additional columns for experiment scores (http://genomewiki.ucsc.edu/index.php/Microarray_track).
    Browser Extensible Data (BED) format of sequence annotation track, typically to be displayed in a genome browser.
    """
    bigBed = "EDAM_format:3004"
    """
    bigBed format for large sequence annotation tracks, similar to textual BED format.
    """
    WIG = "EDAM_format:3005"
    """
    Wiggle format (WIG) of a sequence annotation track that consists of a value for each sequence position. Typically to be displayed in a genome browser.
    """
    bigWig = "EDAM_format:3006"
    """
    bigWig format for large sequence annotation tracks that consist of a value for each sequence position. Similar to textual WIG format.
    """
    PSL = "EDAM_format:3007"
    """
    PSL format of alignments, typically generated by BLAT or psLayout. Can be displayed in a genome browser like a sequence annotation track.
    """
    MAF = "EDAM_format:3008"
    """
    Multiple Alignment Format (MAF) supporting alignments of whole genomes with rearrangements, directions, multiple pieces to the alignment, and so forth.
    Typically generated by Multiz and TBA aligners; can be displayed in a genome browser like a sequence annotation track. This should not be confused with MIRA Assembly Format or Mutation Annotation Format.
    """
    number_2bit = "EDAM_format:3009"
    """
    2bit binary format of nucleotide sequences using 2 bits per nucleotide. In addition encodes unknown nucleotides and lower-case 'masking'.
    """
    FULL_STOPnib = "EDAM_format:3010"
    """
    .nib (nibble) binary format of a nucleotide sequence using 4 bits per nucleotide (including unknown) and its lower-case 'masking'.
    """
    genePred = "EDAM_format:3011"
    """
    genePred format has 3 main variations (http://genome.ucsc.edu/FAQ/FAQformat#format9 http://www.broadinstitute.org/software/igv/genePred). They reflect UCSC Browser DB tables.
    genePred table format for gene prediction tracks.
    """
    pgSnp = "EDAM_format:3012"
    """
    Personal Genome SNP (pgSnp) format for sequence variation tracks (indels and polymorphisms), supported by the UCSC Genome Browser.
    """
    axt = "EDAM_format:3013"
    """
    axt format of alignments, typically produced from BLASTZ.
    """
    LAV = "EDAM_format:3014"
    """
    LAV format of alignments generated by BLASTZ and LASTZ.
    """
    Pileup = "EDAM_format:3015"
    """
    Pileup format of alignment of sequences (e.g. sequencing reads) to (a) reference sequence(s). Contains aligned bases per base of the reference sequence(s).
    """
    VCF = "EDAM_format:3016"
    """
    1000 Genomes Project has its own specification for encoding structural variations in VCF (https://www.internationalgenome.org/wiki/Analysis/Variant%20Call%20Format/VCF%20(Variant%20Call%20Format)%20version%204.0/encoding-structural-variants). This is based on VCF version 4.0 and not directly compatible with VCF version 4.3.
    Variant Call Format (VCF) is tabular format for storing genomic sequence variations.
    """
    SRF = "EDAM_format:3017"
    """
    Sequence Read Format (SRF) of sequence trace data. Supports submission to the NCBI Short Read Archive.
    """
    ZTR = "EDAM_format:3018"
    """
    ZTR format for storing chromatogram data from DNA sequencing instruments.
    """
    GVF = "EDAM_format:3019"
    """
    Genome Variation Format (GVF). A GFF3-compatible format with defined header and attribute tags for sequence variation.
    """
    BCF = "EDAM_format:3020"
    """
    BCF is the binary version of Variant Call Format (VCF) for sequence variation (indels, polymorphisms, structural variation).
    """
    Matrix_format = "EDAM_format:3033"
    """
    Format of a matrix (array) of numerical values.
    """
    Protein_domain_classification_format = "EDAM_format:3097"
    """
    Format of data concerning the classification of the sequences and/or structures of protein structural domain(s).
    """
    Raw_SCOP_domain_classification_format = "EDAM_format:3098"
    """
    Format of raw SCOP domain classification data files.
    These are the parsable data files provided by SCOP.
    """
    Raw_CATH_domain_classification_format = "EDAM_format:3099"
    """
    Format of raw CATH domain classification data files.
    These are the parsable data files provided by CATH.
    """
    CATH_domain_report_format = "EDAM_format:3100"
    """
    Format of summary of domain classification information for a CATH domain.
    The report (for example http://www.cathdb.info/domain/1cukA01) includes CATH codes for levels in the hierarchy for the domain, level descriptions and relevant data and links.
    """
    SBRML = "EDAM_format:3155"
    """
    Systems Biology Result Markup Language (SBRML), the standard XML format for simulated or calculated results (e.g. trajectories) of systems biology models.
    """
    BioPAX = "EDAM_format:3156"
    """
    BioPAX is an exchange format for pathway data, with its data model defined in OWL.
    """
    EBI_Application_Result_XML = "EDAM_format:3157"
    """
    EBI Application Result XML is a format returned by sequence similarity search Web services at EBI.
    """
    PSI_MI_XML_LEFT_PARENTHESISMIFRIGHT_PARENTHESIS = "EDAM_format:3158"
    """
    XML Molecular Interaction Format (MIF), standardised by HUPO PSI MI.
    """
    phyloXML = "EDAM_format:3159"
    """
    phyloXML is a standardised XML format for phylogenetic trees, networks, and associated data.
    """
    NeXML = "EDAM_format:3160"
    """
    NeXML is a standardised XML format for rich phyloinformatic data.
    """
    MAGE_ML = "EDAM_format:3161"
    """
    MAGE-ML XML format for microarray expression data, standardised by MGED (now FGED).
    """
    MAGE_TAB = "EDAM_format:3162"
    """
    MAGE-TAB textual format for microarray expression data, standardised by MGED (now FGED).
    """
    GCDML = "EDAM_format:3163"
    """
    GCDML XML format for genome and metagenome metadata according to MIGS/MIMS/MIMARKS information standards, standardised by the Genomic Standards Consortium (GSC).
    """
    GTrack = "EDAM_format:3164"
    """
    'GTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GTrack' is the tabular format for representing features of sequences and genomes.
    GTrack is a generic and optimised tabular format for genome or sequence feature tracks. GTrack unifies the power of other track formats (e.g. GFF3, BED, WIG), and while optimised in size, adds more flexibility, customisation, and automation ("machine understandability").
    """
    Biological_pathway_or_network_report_format = "EDAM_format:3166"
    """
    Data format for a report of information derived from a biological pathway or network.
    """
    Experiment_annotation_format = "EDAM_format:3167"
    """
    Data format for annotation on a laboratory experiment.
    """
    Cytoband_format = "EDAM_format:3235"
    """
    Cytoband format for chromosome cytobands.
    Reflects a UCSC Browser DB table.
    """
    CopasiML = "EDAM_format:3239"
    """
    CopasiML, the native format of COPASI.
    """
    CellML = "EDAM_format:3240"
    """
    CellML, the format for mathematical models of biological and other networks.
    """
    PSI_MI_TAB_LEFT_PARENTHESISMITABRIGHT_PARENTHESIS = "EDAM_format:3242"
    """
    Tabular Molecular Interaction format (MITAB), standardised by HUPO PSI MI.
    """
    PSI_PAR = "EDAM_format:3243"
    """
    Protein affinity format (PSI-PAR), standardised by HUPO PSI MI. It is compatible with PSI MI XML (MIF) and uses the same XML Schema.
    """
    mzML = "EDAM_format:3244"
    """
    mzML format for raw spectrometer output data, standardised by HUPO PSI MSS.
    mzML is the successor and unifier of the mzData format developed by PSI and mzXML developed at the Seattle Proteome Center.
    """
    Mass_spectrometry_data_format = "EDAM_format:3245"
    """
    Format for mass pectra and derived data, include peptide sequences etc.
    """
    TraML = "EDAM_format:3246"
    """
    TraML (Transition Markup Language) is the format for mass spectrometry transitions, standardised by HUPO PSI MSS.
    """
    mzIdentML = "EDAM_format:3247"
    """
    mzIdentML is the exchange format for peptides and proteins identified from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of proteomics search engines.
    """
    mzQuantML = "EDAM_format:3248"
    """
    mzQuantML is the format for quantitation values associated with peptides, proteins and small molecules from mass spectra, standardised by HUPO PSI PI. It can be used for outputs of quantitation software for proteomics.
    """
    GelML = "EDAM_format:3249"
    """
    GelML is the format for describing the process of gel electrophoresis, standardised by HUPO PSI PS.
    """
    spML = "EDAM_format:3250"
    """
    spML is the format for describing proteomics sample processing, other than using gels, prior to mass spectrometric protein identification, standardised by HUPO PSI PS. It may also be applicable for metabolomics.
    """
    OWL_Functional_Syntax = "EDAM_format:3252"
    """
    A human-readable encoding for the Web Ontology Language (OWL).
    """
    Manchester_OWL_Syntax = "EDAM_format:3253"
    """
    A syntax for writing OWL class expressions.
    This format was influenced by the OWL Abstract Syntax and the DL style syntax.
    """
    KRSS2_Syntax = "EDAM_format:3254"
    """
    A superset of the "Description-Logic Knowledge Representation System Specification from the KRSS Group of the ARPA Knowledge Sharing Effort".
    This format is used in Protege 4.
    """
    Turtle = "EDAM_format:3255"
    """
    The SPARQL Query Language incorporates a very similar syntax.
    The Terse RDF Triple Language (Turtle) is a human-friendly serialisation format for RDF (Resource Description Framework) graphs.
    """
    N_Triples = "EDAM_format:3256"
    """
    A plain text serialisation format for RDF (Resource Description Framework) graphs, and a subset of the Turtle (Terse RDF Triple Language) format.
    N-Triples should not be confused with Notation 3 which is a superset of Turtle.
    """
    Notation3 = "EDAM_format:3257"
    """
    A shorthand non-XML serialisation of Resource Description Framework model, designed with human-readability in mind.
    """
    RDFSOLIDUSXML = "EDAM_format:3261"
    """
    RDF/XML can be used as a standard serialisation syntax for OWL DL, but not for OWL Full.
    Resource Description Framework (RDF) XML format.
    """
    OWLSOLIDUSXML = "EDAM_format:3262"
    """
    OWL ontology XML serialisation format.
    """
    A2M = "EDAM_format:3281"
    """
    The A2M format is used as the primary format for multiple alignments of protein or nucleic-acid sequences in the SAM suite of tools. It is a small modification of FASTA format for sequences and is compatible with most tools that read FASTA.
    """
    SFF = "EDAM_format:3284"
    """
    Standard flowgram format (SFF) is a binary file format used to encode results of pyrosequencing from the 454 Life Sciences platform for high-throughput sequencing.
    """
    MAP = "EDAM_format:3285"
    """
    The MAP file describes SNPs and is used by the Plink package.
    """
    PED = "EDAM_format:3286"
    """
    The PED file describes individuals and genetic data and is used by the Plink package.
    """
    Individual_genetic_data_format = "EDAM_format:3287"
    """
    Data format for a metadata on an individual and their genetic data.
    """
    PEDSOLIDUSMAP = "EDAM_format:3288"
    """
    The PED/MAP file describes data used by the Plink package.
    """
    CT = "EDAM_format:3309"
    """
    File format of a CT (Connectivity Table) file from the RNAstructure package.
    """
    SS = "EDAM_format:3310"
    """
    XRNA old input style format.
    """
    RNAML = "EDAM_format:3311"
    """
    RNA Markup Language.
    """
    GDE = "EDAM_format:3312"
    """
    Format for the Genetic Data Environment (GDE).
    """
    BLC = "EDAM_format:3313"
    """
    A multiple alignment in vertical format, as used in the AMPS (Alignment of Multiple Protein Sequences) package.
    """
    Data_index_format = "EDAM_format:3326"
    """
    Format of a data index of some type.
    """
    BAI = "EDAM_format:3327"
    """
    BAM indexing format.
    """
    HMMER2 = "EDAM_format:3328"
    """
    HMMER profile HMM file for HMMER versions 2.x.
    """
    HMMER3 = "EDAM_format:3329"
    """
    HMMER profile HMM file for HMMER versions 3.x.
    """
    PO = "EDAM_format:3330"
    """
    PO is the output format of Partial Order Alignment program (POA) performing Multiple Sequence Alignment (MSA).
    """
    BLAST_XML_results_format = "EDAM_format:3331"
    """
    XML format as produced by the NCBI Blast package.
    """
    CRAM = "EDAM_format:3462"
    """
    Reference-based compression of alignment format.
    """
    JSON = "EDAM_format:3464"
    """
    JavaScript Object Notation format; a lightweight, text-based format to represent tree-structured data using key-value pairs.
    """
    EPS = "EDAM_format:3466"
    """
    Encapsulated PostScript format.
    """
    GIF = "EDAM_format:3467"
    """
    Graphics Interchange Format.
    """
    xls = "EDAM_format:3468"
    """
    Microsoft Excel spreadsheet format.
    """
    TSV = "EDAM_format:3475"
    """
    Tabular data represented as tab-separated values in a text file.
    """
    Cytoscape_input_file_format = "EDAM_format:3477"
    """
    Format of the cytoscape input file of gene expression ratios or values are specified over one or more experiments.
    """
    ebwt = "EDAM_format:3484"
    """
    Bowtie format for indexed reference genome for "small" genomes.
    """
    RSF = "EDAM_format:3485"
    """
    RSF-format files contain one or more sequences that may or may not be related. In addition to the sequence data, each sequence can be annotated with descriptive sequence information (from the GCG manual).
    Rich sequence format.
    """
    GCG_format_variant = "EDAM_format:3486"
    """
    Some format based on the GCG format.
    """
    BSML = "EDAM_format:3487"
    """
    Bioinformatics Sequence Markup Language format.
    """
    ebwtl = "EDAM_format:3491"
    """
    Bowtie format for indexed reference genome for "large" genomes.
    """
    Ensembl_variation_file_format = "EDAM_format:3499"
    """
    Ensembl standard format for variation data.
    """
    docx = "EDAM_format:3506"
    """
    Microsoft Word format.
    """
    Document_format = "EDAM_format:3507"
    """
    Format of documents including word processor, spreadsheet and presentation.
    """
    PDF = "EDAM_format:3508"
    """
    Portable Document Format.
    """
    Image_format = "EDAM_format:3547"
    """
    Format used for images and image metadata.
    """
    DICOM_format = "EDAM_format:3548"
    """
    Medical image format corresponding to the Digital Imaging and Communications in Medicine (DICOM) standard.
    """
    nii = "EDAM_format:3549"
    """
    An open file format from the Neuroimaging Informatics Technology Initiative (NIfTI) commonly used to store brain imaging data obtained using Magnetic Resonance Imaging (MRI) methods.
    """
    mhd = "EDAM_format:3550"
    """
    Text-based tagged file format for medical images generated using the MetaImage software package.
    """
    nrrd = "EDAM_format:3551"
    """
    Nearly Raw Rasta Data format designed to support scientific visualisation and image processing involving N-dimensional raster data.
    """
    R_file_format = "EDAM_format:3554"
    """
    File format used for scripts written in the R programming language for execution within the R software environment, typically for statistical computation and graphics.
    """
    SPSS = "EDAM_format:3555"
    """
    File format used for scripts for the Statistical Package for the Social Sciences.
    """
    MHTML = "EDAM_format:3556"
    """
    MHTML is not strictly an HTML format, it is encoded as an HTML email message (although with multipart/related instead of multipart/alternative). It, however, contains the main HTML block as its core, and thus it is for practical reasons included in EDAM as a specialisation of 'HTML'.
    MIME HTML format for Web pages, which can include external resources, including images, Flash animations and so on.
    """
    IDAT = "EDAM_format:3578"
    """
    Proprietary file format for (raw) BeadArray data used by genomewide profiling platforms from Illumina Inc. This format is output directly from the scanner and stores summary intensities for each probe-type on an array.
    """
    JPG = "EDAM_format:3579"
    """
    Joint Picture Group file format for lossy graphics file.
    Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type.
    """
    rcc = "EDAM_format:3580"
    """
    Reporter Code Count-A data file (.csv) output by the Nanostring nCounter Digital Analyzer, which contains gene sample information, probe information and probe counts.
    """
    arff = "EDAM_format:3581"
    """
    ARFF (Attribute-Relation File Format) is an ASCII text file format that describes a list of instances sharing a set of attributes.
    This file format is for machine learning.
    """
    afg = "EDAM_format:3582"
    """
    AFG is a single text-based file assembly format that holds read and consensus information together.
    """
    bedgraph = "EDAM_format:3583"
    """
    Holds a tab-delimited chromosome /start /end / datavalue dataset.
    The bedGraph format allows display of continuous-valued data in track format. This display type is useful for probability scores and transcriptome data.
    """
    bedstrict = "EDAM_format:3584"
    """
    Browser Extensible Data (BED) format of sequence annotation track that strictly does not contain non-standard fields beyond the first 3 columns.
    Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not.
    """
    bed6 = "EDAM_format:3585"
    """
    BED file format where each feature is described by chromosome, start, end, name, score, and strand.
    Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 6
    """
    bed12 = "EDAM_format:3586"
    """
    A BED file where each feature is described by all twelve columns.
    Tab delimited data in strict BED format - no non-standard columns allowed; column count forced to 12
    """
    chrominfo = "EDAM_format:3587"
    """
    Galaxy allows BED files to contain non-standard fields beyond the first 3 columns, some other implementations do not.
    Tabular format of chromosome names and sizes used by Galaxy.
    """
    customtrack = "EDAM_format:3588"
    """
    Custom Sequence annotation track format used by Galaxy.
    Used for tracks/track views within galaxy.
    """
    csfasta = "EDAM_format:3589"
    """
    Color space FASTA format sequence variant.
    FASTA format extended for color space information.
    """
    HDF5 = "EDAM_format:3590"
    """
    An HDF5 file appears to the user as a directed graph. The nodes of this graph are the higher-level HDF5 objects that are exposed by the HDF5 APIs: Groups, Datasets, Named datatypes. Currently supported by the Python MDTraj package.
    HDF5 is a data model, library, and file format for storing and managing data, based on Hierarchical Data Format (HDF).
    HDF5 is the new version, according to the HDF group, a completely different technology (https://support.hdfgroup.org/products/hdf4/ compared to HDF.
    """
    TIFF = "EDAM_format:3591"
    """
    A versatile bitmap format.
    The TIFF format is perhaps the most versatile and diverse bitmap format in existence. Its extensible nature and support for numerous data compression schemes allow developers to customize the TIFF format to fit any peculiar data storage needs.
    """
    BMP = "EDAM_format:3592"
    """
    Although it is based on Windows internal bitmap data structures, it is supported by many non-Windows and non-PC applications.
    Standard bitmap storage format in the Microsoft Windows environment.
    """
    im = "EDAM_format:3593"
    """
    IFUNC library reads and writes most uncompressed interchange versions of this format.
    IM is a format used by LabEye and other applications based on the IFUNC image processing library.
    """
    pcd = "EDAM_format:3594"
    """
    PCD was developed by Kodak. A PCD file contains five different resolution (ranging from low to high) of a slide or film negative. Due to it PCD is often used by many photographers and graphics professionals for high-end printed applications.
    Photo CD format, which is the highest resolution format for images on a CD.
    """
    pcx = "EDAM_format:3595"
    """
    PCX is an image file format that uses a simple form of run-length encoding. It is lossless.
    """
    ppm = "EDAM_format:3596"
    """
    The PPM format is a lowest common denominator color image file format.
    """
    psd = "EDAM_format:3597"
    """
    PSD (Photoshop Document) is a proprietary file that allows the user to work with the images' individual layers even after the file has been saved.
    """
    xbm = "EDAM_format:3598"
    """
    The XBM format was replaced by XPM for X11 in 1989.
    X BitMap is a plain text binary image format used by the X Window System used for storing cursor and icon bitmaps used in the X GUI.
    """
    xpm = "EDAM_format:3599"
    """
    Sequence of segments with markers. Begins with byte of 0xFF and follows by marker type.
    X PixMap (XPM) is an image file format used by the X Window System, it is intended primarily for creating icon pixmaps, and supports transparent pixels.
    """
    rgb = "EDAM_format:3600"
    """
    RGB file format is the native raster graphics file format for Silicon Graphics workstations.
    """
    pbm = "EDAM_format:3601"
    """
    The PBM format is a lowest common denominator monochrome file format. It serves as the common language of a large family of bitmap image conversion filters.
    """
    pgm = "EDAM_format:3602"
    """
    It is designed to be extremely easy to learn and write programs for.
    The PGM format is a lowest common denominator grayscale file format.
    """
    PNG = "EDAM_format:3603"
    """
    It iis expected to replace the Graphics Interchange Format (GIF).
    PNG is a file format for image compression.
    """
    SVG = "EDAM_format:3604"
    """
    Scalable Vector Graphics (SVG) is an XML-based vector image format for two-dimensional graphics with support for interactivity and animation.
    The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.
    """
    rast = "EDAM_format:3605"
    """
    Sun Raster is a raster graphics file format used on SunOS by Sun Microsystems.
    The SVG specification is an open standard developed by the World Wide Web Consortium (W3C) since 1999.
    """
    Sequence_quality_report_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:3606"
    """
    Textual report format for sequence quality for reports from sequencing machines.
    """
    qual = "EDAM_format:3607"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences).
    Phred quality scores are defined as a property which is logarithmically related to the base-calling error probabilities.
    """
    qualsolexa = "EDAM_format:3608"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) for Solexa/Illumina 1.0 format.
    Solexa/Illumina 1.0 format can encode a Solexa/Illumina quality score from -5 to 62 using ASCII 59 to 126 (although in raw read data Solexa scores from -5 to 40 only are expected)
    """
    qualillumina = "EDAM_format:3609"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) from Illumina 1.5 and before Illumina 1.8.
    Starting in Illumina 1.5 and before Illumina 1.8, the Phred scores 0 to 2 have a slightly different meaning. The values 0 and 1 are no longer used and the value 2, encoded by ASCII 66 "B", is used also at the end of reads as a Read Segment Quality Control Indicator.
    """
    qualsolid = "EDAM_format:3610"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) for SOLiD data.
    For SOLiD data, the sequence is in color space, except the first position. The quality values are those of the Sanger format.
    """
    qual454 = "EDAM_format:3611"
    """
    FASTQ format subset for Phred sequencing quality score data only (no sequences) from 454 sequencers.
    """
    ENCODE_peak_format = "EDAM_format:3612"
    """
    Format that covers both the broad peak format and narrow peak format from ENCODE.
    Human ENCODE peak format.
    """
    ENCODE_narrow_peak_format = "EDAM_format:3613"
    """
    Format that covers both the broad peak format and narrow peak format from ENCODE.
    Human ENCODE narrow peak format.
    """
    ENCODE_broad_peak_format = "EDAM_format:3614"
    """
    Human ENCODE broad peak format.
    """
    bgzip = "EDAM_format:3615"
    """
    BAM files are compressed using a variant of GZIP (GNU ZIP), into a format called BGZF (Blocked GNU Zip Format).
    Blocked GNU Zip format.
    """
    tabix = "EDAM_format:3616"
    """
    TAB-delimited genome position file index format.
    """
    Graph_format = "EDAM_format:3617"
    """
    Data format for graph data.
    """
    xgmml = "EDAM_format:3618"
    """
    XML-based format used to store graph descriptions within Galaxy.
    """
    sif = "EDAM_format:3619"
    """
    SIF (simple interaction file) Format - a network/pathway format used for instance in cytoscape.
    """
    xlsx = "EDAM_format:3620"
    """
    MS Excel spreadsheet format consisting of a set of XML documents stored in a ZIP-compressed file.
    """
    SQLite_format = "EDAM_format:3621"
    """
    Data format used by the SQLite database.
    """
    Gemini_SQLite_format = "EDAM_format:3622"
    """
    Data format used by the SQLite database conformant to the Gemini schema.
    """
    snpeffdb = "EDAM_format:3624"
    """
    An index of a genome database, indexed for use by the snpeff tool.
    """
    MAT = "EDAM_format:3626"
    """
    Binary format used by MATLAB files to store workspace variables.
    """
    NetCDF = "EDAM_format:3650"
    """
    Format used by netCDF software library for writing and reading chromatography-MS data files. Also used to store trajectory atom coordinates information, such as the ones obtained by Molecular Dynamics simulations.
    Network Common Data Form (NetCDF) library is supported by AMBER MD package from version 9.
    """
    MGF = "EDAM_format:3651"
    """
    Files includes *m*/*z*, intensity pairs separated by headers; headers can contain a bit more information, including search engine instructions.
    Mascot Generic Format. Encodes multiple MS/MS spectra in a single file.
    """
    dta = "EDAM_format:3652"
    """
    Each file contains one header line for the known or assumed charge and the mass of the precursor peptide ion, calculated from the measured *m*/*z* and the charge. This one line was then followed by all the *m*/*z*, intensity pairs that represent the spectrum.
    Spectral data format file where each spectrum is written to a separate file.
    """
    pkl = "EDAM_format:3653"
    """
    Differ from .dta only in subtleties of the header line format and content and support the added feature of being able to.
    Spectral data file similar to dta.
    """
    mzXML = "EDAM_format:3654"
    """
    Common file format for proteomics mass spectrometric data developed at the Seattle Proteome Center/Institute for Systems Biology.
    """
    pepXML = "EDAM_format:3655"
    """
    Open data format for the storage, exchange, and processing of peptide sequence assignments of MS/MS scans, intended to provide a common data output format for many different MS/MS search engines and subsequent peptide-level analyses.
    """
    GPML = "EDAM_format:3657"
    """
    Graphical Pathway Markup Language (GPML) is an XML format used for exchanging biological pathways.
    """
    K_mer_countgraph = "EDAM_format:3665"
    """
    A list of k-mers and their occurrences in a dataset. Can also be used as an implicit De Bruijn graph.
    """
    mzTab = "EDAM_format:3681"
    """
    For mass spectrometry-based chemical profiling data (including metabolomics), there is a derived (but incompatible) format mzTab-M (also named mzTab 2.0, http://edamontology.org/format_4058), and its lipidomics version mzTab-L (http://edamontology.org/format_4059).
    For more detailed metadata, there are formats such as mzIdentML (http://edamontology.org/format_3247) and mzQuantML (http://edamontology.org/format_3248).
    The reference implementation of mzTab in Java is https://github.com/PRIDE-Archive/jmzTab (maintenance stopped in 2022).
    mzTab is a light-weight, tab-delimited format for mass spectrometry-based proteomics data.
    mzTab is alternatively named mzTab 1.0, as opposed to mzTab 2.0 (and 2.1), which is the incompatible mzTab-M format for chemical profiling e.g. metabolomics.
    """
    imzML_metadata_file = "EDAM_format:3682"
    """
    imzML data are recorded in 2 files: '.imzXML' (this concept) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (http://edamontology.org/format_3839) is a binary file containing the mass spectra. This entry is for the metadata XML file.
    imzML metadata is a data format for mass spectrometry imaging metadata.
    """
    qcML = "EDAM_format:3683"
    """
    The focus of qcML is towards mass spectrometry based proteomics, but the format is suitable for metabolomics and sequencing as well.
    qcML is an XML format for quality-related data of mass spectrometry and other high-throughput measurements.
    """
    PRIDE_XML = "EDAM_format:3684"
    """
    PRIDE XML is an XML format for mass spectra, peptide and protein identifications, and metadata about a corresponding measurement, sample, experiment.
    """
    SED_ML = "EDAM_format:3685"
    """
    Simulation Experiment Description Markup Language (SED-ML) is an XML format for encoding simulation setups, according to the MIASE (Minimum Information About a Simulation Experiment) requirements.
    """
    COMBINE_OMEX = "EDAM_format:3686"
    """
    An OMEX file is a ZIP container that includes a manifest file, listing the content of the archive, an optional metadata file adding information about the archive and its content, and the files describing the model. OMEX is one of the standardised formats within COMBINE (Computational Modeling in Biology Network).
    Open Modeling EXchange format (OMEX) is a ZIPped format for encapsulating all information necessary for a modeling and simulation project in systems biology.
    """
    ISA_TAB = "EDAM_format:3687"
    """
    ISA-TAB is based on MAGE-TAB. Other than tabular, the ISA model can also be represented in RDF, and in JSON (compliable with a set of defined JSON Schemata).
    The Investigation / Study / Assay (ISA) tab-delimited (TAB) format incorporates metadata from experiments employing a combination of technologies.
    """
    SBtab = "EDAM_format:3688"
    """
    SBtab is a tabular format for biochemical network models.
    """
    BCML = "EDAM_format:3689"
    """
    Biological Connection Markup Language (BCML) is an XML format for biological pathways.
    """
    BDML = "EDAM_format:3690"
    """
    Biological Dynamics Markup Language (BDML) is an XML format for quantitative data describing biological dynamics.
    """
    BEL = "EDAM_format:3691"
    """
    Biological Expression Language (BEL) is a textual format for representing scientific findings in life sciences in a computable form.
    """
    SBGN_ML = "EDAM_format:3692"
    """
    SBGN-ML is an XML format for Systems Biology Graphical Notation (SBGN) diagrams of biological pathways or networks.
    """
    AGP = "EDAM_format:3693"
    """
    AGP is a tabular format for a sequence assembly (a contig, a scaffold/supercontig, or a chromosome).
    """
    PS = "EDAM_format:3696"
    """
    PostScript format.
    """
    SRA_format = "EDAM_format:3698"
    """
    SRA archive format (SRA) is the archive format used for input to the NCBI Sequence Read Archive.
    """
    VDB = "EDAM_format:3699"
    """
    VDB ('vertical database') is the native format used for export from the NCBI Sequence Read Archive.
    """
    Sequin_format = "EDAM_format:3701"
    """
    A five-column, tab-delimited table of feature locations and qualifiers for importing annotation into an existing Sequin submission (an NCBI tool for submitting and updating GenBank entries).
    """
    MSF = "EDAM_format:3702"
    """
    Proprietary mass-spectrometry format of Thermo Scientific's ProteomeDiscoverer software.
    This format corresponds to an SQLite database, and you can look into the files with e.g. SQLiteStudio3. There are also some readers (http://doi.org/10.1021/pr2005154) and converters (http://doi.org/10.1016/j.jprot.2015.06.015) for this format available, which re-engineered the database schema, but there is no official DB schema specification of Thermo Scientific for the format.
    """
    Biodiversity_data_format = "EDAM_format:3706"
    """
    Data format for biodiversity data.
    """
    ABCD_format = "EDAM_format:3708"
    """
    Exchange format of the Access to Biological Collections Data (ABCD) Schema; a standard for the access to and exchange of data about specimens and observations (primary biodiversity data).
    """
    GCTSOLIDUSRes_format = "EDAM_format:3709"
    """
    Tab-delimited text files of GenePattern that contain a column for each sample, a row for each gene, and an expression value for each gene in each sample.
    """
    WIFF_format = "EDAM_format:3710"
    """
    Mass spectrum file format from QSTAR and QTRAP instruments (ABI/Sciex).
    """
    XEXCLAMATION_MARKTandem_XML = "EDAM_format:3711"
    """
    Output format used by X! series search engines that is based on the XML language BIOML.
    """
    Thermo_RAW = "EDAM_format:3712"
    """
    Proprietary file format for mass spectrometry data from Thermo Scientific.
    Proprietary format for which documentation is not available.
    """
    Mascot_FULL_STOPdat_file = "EDAM_format:3713"
    """
    "Raw" result file from Mascot database search.
    """
    MaxQuant_APL_peaklist_format = "EDAM_format:3714"
    """
    Format of peak list files from Andromeda search engine (MaxQuant) that consist of arbitrarily many spectra.
    """
    SBOL = "EDAM_format:3725"
    """
    SBOL introduces a standardised format for the electronic exchange of information on the structural and functional aspects of biological designs.
    Synthetic Biology Open Language (SBOL) is an XML format for the specification and exchange of biological design information in synthetic biology.
    """
    PMML = "EDAM_format:3726"
    """
    One or more mining models can be contained in a PMML document.
    PMML uses XML to represent mining models. The structure of the models is described by an XML Schema.
    """
    OME_TIFF = "EDAM_format:3727"
    """
    An OME-TIFF dataset consists of one or more files in standard TIFF or BigTIFF format, with the file extension .ome.tif or .ome.tiff, and an identical (or in the case of multiple files, nearly identical) string of OME-XML metadata embedded in the ImageDescription tag of each file's first IFD (Image File Directory). BigTIFF file extensions are also permitted, with the file extension .ome.tf2, .ome.tf8 or .ome.btf, but note these file extensions are an addition to the original specification, and software using an older version of the specification may not be able to handle these file extensions.
    Image file format used by the Open Microscopy Environment (OME).
    OME develops open-source software and data format standards for the storage and manipulation of biological microscopy data. It is a joint project between universities, research establishments, industry and the software development community.
    """
    LocARNA_PP = "EDAM_format:3728"
    """
    Format for multiple aligned or single sequences together with the probabilistic description of the (consensus) RNA secondary structure ensemble by probabilities of base pairs, base pair stackings, and base pairs and unpaired bases in the loop of base pairs.
    The LocARNA PP format combines sequence or alignment information and (respectively, single or consensus) ensemble probabilities into an PP 2.0 record.
    """
    dbGaP_format = "EDAM_format:3729"
    """
    Input format used by the Database of Genotypes and Phenotypes (dbGaP).
    The Database of Genotypes and Phenotypes (dbGaP) is a National Institutes of Health (NIH) sponsored repository charged to archive, curate and distribute information produced by studies investigating the interaction of genotype and phenotype.
    """
    BIOM_format = "EDAM_format:3746"
    """
    BIOM is a recognised standard for the Earth Microbiome Project, and is a project supported by Genomics Standards Consortium. Supported in QIIME, Mothur, MEGAN, etc.
    The BIological Observation Matrix (BIOM) is a format for representing biological sample by observation contingency tables in broad areas of comparative omics. The primary use of this format is to represent OTU tables and metagenome tables.
    """
    protXML = "EDAM_format:3747"
    """
    A format for storage, exchange, and processing of protein identifications created from ms/ms-derived peptide sequence data.
    No human-consumable information about this format is available (see http://tools.proteomecenter.org/wiki/index.php?title=Formats:protXML).
    """
    Linked_data_format = "EDAM_format:3748"
    """
    A linked data format enables publishing structured data as linked data (Linked Data), so that the data can be interlinked and become more useful through semantic queries.
    """
    JSON_LD = "EDAM_format:3749"
    """
    JSON-LD, or JavaScript Object Notation for Linked Data, is a method of encoding Linked Data using JSON.
    """
    YAML = "EDAM_format:3750"
    """
    Data in YAML format can be serialised into text, or binary format.
    YAML (YAML Ain't Markup Language) is a human-readable tree-structured data serialisation language.
    YAML version 1.2 is a superset of JSON; prior versions were "not strictly compatible".
    """
    DSV = "EDAM_format:3751"
    """
    Tabular data represented as values in a text file delimited by some character.
    """
    CSV = "EDAM_format:3752"
    """
    Tabular data represented as comma-separated values in a text file.
    """
    SEQUEST_FULL_STOPout_file = "EDAM_format:3758"
    """
    "Raw" result file from SEQUEST database search.
    """
    idXML = "EDAM_format:3764"
    """
    XML file format for files containing information about peptide identifications from mass spectrometry data analysis carried out with OpenMS.
    """
    KNIME_datatable_format = "EDAM_format:3765"
    """
    Data table formatted such that it can be passed/streamed within the KNIME platform.
    """
    UniProtKB_XML = "EDAM_format:3770"
    """
    UniProtKB XML sequence features format is an XML format available for downloading UniProt entries.
    """
    UniProtKB_RDF = "EDAM_format:3771"
    """
    UniProtKB RDF sequence features format is an RDF format available for downloading UniProt entries (in RDF/XML).
    """
    BioJSON_LEFT_PARENTHESISBioXSDRIGHT_PARENTHESIS = "EDAM_format:3772"
    """
    BioJSON is a BioXSD-schema-based JSON format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web applications and APIs, and object-oriented programming.
    Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioJSON' is the JSON format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.
    """
    BioYAML = "EDAM_format:3773"
    """
    BioYAML is a BioXSD-schema-based YAML format of sequence-based data and some other common data - sequence records, alignments, feature records, references to resources, and more - optimised for integrative bioinformatics, web APIs, human readability and editing, and object-oriented programming.
    Work in progress. 'BioXSD' belongs to the 'BioXSD|GTrack' ecosystem of generic formats. 'BioYAML' is the YAML format based on the common, unified 'BioXSD data model', a.k.a. 'BioXSD|BioJSON|BioYAML'.
    """
    BioJSON_LEFT_PARENTHESISJalviewRIGHT_PARENTHESIS = "EDAM_format:3774"
    """
    BioJSON is a JSON format of single multiple sequence alignments, with their annotations, features, and custom visualisation and application settings for the Jalview workbench.
    """
    GSuite = "EDAM_format:3775"
    """
    'GSuite' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'GSuite' is the tabular format for an annotated collection of individual GTrack files.
    GSuite is a tabular format for collections of genome or sequence feature tracks, suitable for integrative multi-track analysis. GSuite contains links to genome/sequence tracks, with additional metadata.
    """
    BTrack = "EDAM_format:3776"
    """
    'BTrack' belongs to the 'BioXSD|GTrack' ecosystem of generic formats, and particular to its subset, the 'GTrack ecosystem' (GTrack, GSuite, BTrack). 'BTrack' is the binary, optionally compressed HDF5-based version of the GTrack and GSuite formats.
    BTrack is an HDF5-based binary format for genome or sequence feature tracks and their collections, suitable for integrative multi-track analysis. BTrack is a binary, compressed alternative to the GTrack and GSuite formats.
    """
    MCPD = "EDAM_format:3777"
    """
    Multi-Crop Passport Descriptors is a format available in 2 successive versions, V.1 (FAO/IPGRI 2001) and V.2 (FAO/Bioversity 2012).
    The FAO/Bioversity/IPGRI Multi-Crop Passport Descriptors (MCPD) is an international standard format for exchange of germplasm information.
    """
    Annotated_text_format = "EDAM_format:3780"
    """
    Data format of an annotated text, e.g. with recognised entities, concepts, and relations.
    """
    PubAnnotation_format = "EDAM_format:3781"
    """
    JSON format of annotated scientific text used by PubAnnotations and other tools.
    """
    BioC = "EDAM_format:3782"
    """
    BioC is a standardised XML format for sharing and integrating text data and annotations.
    """
    PubTator_format = "EDAM_format:3783"
    """
    Native textual export format of annotated scientific text from PubTator.
    """
    Open_Annotation_format = "EDAM_format:3784"
    """
    A format of text annotation using the linked-data Open Annotation Data Model, serialised typically in RDF or JSON-LD.
    """
    BioNLP_Shared_Task_format = "EDAM_format:3785"
    """
    A family of similar formats of text annotation, used by BRAT and other tools, known as BioNLP Shared Task format (BioNLP 2009 Shared Task on Event Extraction, BioNLP Shared Task 2011, BioNLP Shared Task 2013), BRAT format, BRAT standoff format, and similar.
    """
    Query_language = "EDAM_format:3787"
    """
    A query language (format) for structured database queries.
    """
    SQL = "EDAM_format:3788"
    """
    SQL (Structured Query Language) is the de-facto standard query language (format of queries) for querying and manipulating data in relational databases.
    """
    XQuery = "EDAM_format:3789"
    """
    XQuery (XML Query) is a query language (format of queries) for querying and manipulating structured and unstructured data, usually in the form of XML, text, and with vendor-specific extensions for other data formats (JSON, binary, etc.).
    """
    SPARQL = "EDAM_format:3790"
    """
    SPARQL (SPARQL Protocol and RDF Query Language) is a semantic query language for querying and manipulating data stored in Resource Description Framework (RDF) format.
    """
    xsd = "EDAM_format:3804"
    """
    XML format for XML Schema.
    """
    XMFA = "EDAM_format:3811"
    """
    XMFA format stands for eXtended Multi-FastA format and is used to store collinear sub-alignments that constitute a single genome alignment.
    """
    GEN = "EDAM_format:3812"
    """
    The GEN file format contains genetic data and describes SNPs.
    """
    SAMPLE_file_format = "EDAM_format:3813"
    """
    The SAMPLE file format contains information about each individual i.e. individual IDs, covariates, phenotypes and missing data proportions, from a GWAS study.
    """
    SDF = "EDAM_format:3814"
    """
    SDF is one of a family of chemical-data file formats developed by MDL Information Systems; it is intended especially for structural information.
    """
    Molfile = "EDAM_format:3815"
    """
    An MDL Molfile is a file format for holding information about the atoms, bonds, connectivity and coordinates of a molecule.
    """
    Mol2 = "EDAM_format:3816"
    """
    Complete, portable representation of a SYBYL molecule. ASCII file which contains all the information needed to reconstruct a SYBYL molecule.
    """
    latex = "EDAM_format:3817"
    """
    format for the LaTeX document preparation system.
    uses the TeX typesetting program format
    """
    ELAND_format = "EDAM_format:3818"
    """
    Tab-delimited text file format used by Eland - the read-mapping program distributed by Illumina with its sequencing analysis pipeline - which maps short Solexa sequence reads to the human reference genome.
    """
    Relaxed_PHYLIP_Interleaved = "EDAM_format:3819"
    """
    It differs from Phylip Format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
    Phylip multiple alignment sequence format, less stringent than PHYLIP format.
    """
    Relaxed_PHYLIP_Sequential = "EDAM_format:3820"
    """
    It differs from Phylip sequential format (format_1997) on length of the ID sequence. There no length restrictions on the ID, but whitespaces aren't allowed in the sequence ID/Name because one space separates the longest ID and the beginning of the sequence. Sequences IDs must be padded to the longest ID length.
    Phylip multiple alignment sequence format, less stringent than PHYLIP sequential format (format_1998).
    """
    VisML = "EDAM_format:3821"
    """
    Default XML format of VisANT, containing all the network information.
    """
    GML = "EDAM_format:3822"
    """
    GML (Graph Modeling Language) is a text file format supporting network data with a very easy syntax. It is used by Graphlet, Pajek, yEd, LEDA and NetworkX.
    """
    FASTG = "EDAM_format:3823"
    """
    FASTG is a format for faithfully representing genome assemblies in the face of allelic polymorphism and assembly uncertainty.
    It is called FASTG, like FASTA, but the G stands for "graph".
    """
    NMR_data_format = "EDAM_format:3824"
    """
    Data format for raw data from a nuclear magnetic resonance (NMR) spectroscopy experiment.
    """
    nmrML = "EDAM_format:3825"
    """
    nmrML is an MSI supported XML-based open access format for metabolomics NMR raw and processed spectral data. It is accompanies by an nmrCV (controlled vocabulary) to allow ontology-based annotations.
    """
    proBAM = "EDAM_format:3826"
    """
    . proBAM is an adaptation of BAM (format_2572), which was extended to meet specific requirements entailed by proteomics data.
    """
    proBED = "EDAM_format:3827"
    """
    . proBED is an adaptation of BED (format_3003), which was extended to meet specific requirements entailed by proteomics data.
    """
    Raw_microarray_data_format = "EDAM_format:3828"
    """
    Data format for raw microarray data.
    """
    GPR = "EDAM_format:3829"
    """
    GenePix Results (GPR) text file format developed by Axon Instruments that is used to save GenePix Results data.
    """
    ARB = "EDAM_format:3830"
    """
    Binary format used by the ARB software suite.
    """
    consensusXML = "EDAM_format:3832"
    """
    OpenMS format for grouping features in one map or across several maps.
    """
    featureXML = "EDAM_format:3833"
    """
    OpenMS format for quantitation results (LC/MS features).
    """
    mzData = "EDAM_format:3834"
    """
    Now deprecated data format of the HUPO Proteomics Standards Initiative. Replaced by mzML (format_3244).
    """
    TIDE_TXT = "EDAM_format:3835"
    """
    Format supported by the Tide tool for identifying peptides from tandem mass spectra.
    """
    BLAST_XML_v2_results_format = "EDAM_format:3836"
    """
    XML format as produced by the NCBI Blast package v2.
    """
    pptx = "EDAM_format:3838"
    """
    Microsoft Powerpoint format.
    """
    ibd = "EDAM_format:3839"
    """
    ibd is a data format for mass spectrometry imaging data.
    imzML data is recorded in 2 files: '.imzXML' (http://edamontology.org/format_3682) is a metadata XML file based on mzML by HUPO-PSI, and '.ibd' (this concept) is a binary file containing the mass spectra.
    """
    NLP_format = "EDAM_format:3841"
    """
    Data format used in Natural Language Processing.
    """
    BEAST = "EDAM_format:3843"
    """
    XML input file format for BEAST Software (Bayesian Evolutionary Analysis Sampling Trees).
    """
    Chado_XML = "EDAM_format:3844"
    """
    Chado-XML format is a direct mapping of the Chado relational schema into XML.
    """
    HSAML = "EDAM_format:3845"
    """
    An alignment format generated by PRANK/PRANKSTER consisting of four elements: newick, nodes, selection and model.
    """
    InterProScan_XML = "EDAM_format:3846"
    """
    Output xml file from the InterProScan sequence analysis application.
    """
    KGML = "EDAM_format:3847"
    """
    The KEGG Markup Language (KGML) is an exchange format of the KEGG pathway maps, which is converted from internally used KGML+ (KGML+SVG) format.
    """
    PubMed_XML = "EDAM_format:3848"
    """
    XML format for collected entries from bibliographic databases MEDLINE and PubMed.
    """
    MSAML = "EDAM_format:3849"
    """
    A set of XML compliant markup components for describing multiple sequence alignments.
    """
    OrthoXML = "EDAM_format:3850"
    """
    OrthoXML is designed broadly to allow the storage and comparison of orthology data from any ortholog database. It establishes a structure for describing orthology relationships while still allowing flexibility for database-specific information to be encapsulated in the same format.
    """
    PSDML = "EDAM_format:3851"
    """
    Tree structure of Protein Sequence Database Markup Language generated using Matra software.
    """
    SeqXML = "EDAM_format:3852"
    """
    SeqXML is an XML Schema to describe biological sequences, developed by the Stockholm Bioinformatics Centre.
    """
    UniParc_XML = "EDAM_format:3853"
    """
    XML format for the UniParc database.
    """
    UniRef_XML = "EDAM_format:3854"
    """
    XML format for the UniRef reference clusters.
    """
    CWL = "EDAM_format:3857"
    """
    Common Workflow Language (CWL) format for description of command-line tools and workflows.
    """
    Waters_RAW = "EDAM_format:3858"
    """
    Proprietary file format for mass spectrometry data from Waters.
    Proprietary format for which documentation is not available, but used by multiple tools.
    """
    JCAMP_DX = "EDAM_format:3859"
    """
    A standardized file format for data exchange in mass spectrometry, initially developed for infrared spectrometry.
    JCAMP-DX is an ASCII based format and therefore not very compact even though it includes standards for file compression.
    """
    NLP_annotation_format = "EDAM_format:3862"
    """
    An NLP format used for annotated textual documents.
    """
    NLP_corpus_format = "EDAM_format:3863"
    """
    NLP format used by a specific type of corpus (collection of texts).
    """
    mirGFF3 = "EDAM_format:3864"
    """
    mirGFF3 is a common format for microRNA data resulting from small-RNA RNA-Seq workflows.
    mirGFF3 is a specialisation of GFF3; produced by small-RNA-Seq analysis workflows, usable and convertible with the miRTop API (https://mirtop.readthedocs.io/en/latest/), and consumable by tools for downstream analysis.
    """
    RNA_annotation_format = "EDAM_format:3865"
    """
    A "placeholder" concept for formats of annotated RNA data, including e.g. microRNA and RNA-Seq data.
    """
    Trajectory_format = "EDAM_format:3866"
    """
    File format to store trajectory information for a 3D structure .
    Formats differ on what they are able to store (coordinates, velocities, topologies) and how they are storing it (raw, compressed, textual, binary).
    """
    Trajectory_format_LEFT_PARENTHESISbinaryRIGHT_PARENTHESIS = "EDAM_format:3867"
    """
    Binary file format to store trajectory information for a 3D structure .
    """
    Trajectory_format_LEFT_PARENTHESIStextRIGHT_PARENTHESIS = "EDAM_format:3868"
    """
    Textual file format to store trajectory information for a 3D structure .
    """
    HDF = "EDAM_format:3873"
    """
    HDF is currently supported by many commercial and non-commercial software platforms such as Java, MATLAB/Scilab, Octave, Python and R.
    HDF is the name of a set of file formats and libraries designed to store and organize large amounts of numerical data, originally developed at the National Center for Supercomputing Applications at the University of Illinois.
    """
    PCAzip = "EDAM_format:3874"
    """
    PCAZip format is a binary compressed file to store atom coordinates based on Essential Dynamics (ED) and Principal Component Analysis (PCA).
    The compression is made projecting the Cartesian snapshots collected along the trajectory into an orthogonal space defined by the most relevant eigenvectors obtained by diagonalization of the covariance matrix (PCA). In the compression/decompression process, part of the original information is lost, depending on the final number of eigenvectors chosen. However, with a reasonable choice of the set of eigenvectors the compression typically reduces the trajectory file to less than one tenth of their original size with very acceptable loss of information. Compression with PCAZip can only be applied to unsolvated structures.
    """
    XTC = "EDAM_format:3875"
    """
    Portable binary format for trajectories produced by GROMACS package.
    XTC uses the External Data Representation (xdr) routines for writing and reading data which were created for the Unix Network File System (NFS). XTC files use a reduced precision (lossy) algorithm which works multiplying the coordinates by a scaling factor (typically 1000), so converting them to pm (GROMACS standard distance unit is nm). This allows an integer rounding of the values. Several other tricks are performed, such as making use of atom proximity information: atoms close in sequence are usually close in space (e.g. water molecules). That makes XTC format the most efficient in terms of disk usage, in most cases reducing by a factor of 2 the size of any other binary trajectory format.
    """
    TNG = "EDAM_format:3876"
    """
    Fully architecture-independent format, regarding both endianness and the ability to mix single/double precision trajectories and I/O libraries. Self-sufficient, it should not require any other files for reading, and all the data should be contained in a single file for easy transport. Temporal compression of data, improving the compression rate of the previous XTC format. Possibility to store meta-data with information about the simulation. Direct access to a particular frame. Efficient parallel I/O.
    Trajectory Next Generation (TNG) is a format for storage of molecular simulation data. It is designed and implemented by the GROMACS development group, and it is called to be the substitute of the XTC format.
    """
    XYZ = "EDAM_format:3877"
    """
    The XYZ chemical file format is widely supported by many programs, although many slightly different XYZ file formats coexist (Tinker XYZ, UniChem XYZ, etc.). Basic information stored for each atom in the system are x, y and z coordinates and atom element/atomic number.
    XYZ files are structured in this way: First line contains the number of atoms in the file. Second line contains a title, comment, or filename. Remaining lines contain atom information. Each line starts with the element symbol, followed by x, y and z coordinates in angstroms separated by whitespace. Multiple molecules or frames can be contained within one file, so it supports trajectory storage. XYZ files can be directly represented by a molecular viewer, as they contain all the basic information needed to build the 3D model.
    """
    mdcrd = "EDAM_format:3878"
    """
    AMBER trajectory (also called mdcrd), with 10 coordinates per line and format F8.3 (fixed point notation with field width 8 and 3 decimal places).
    """
    Topology_format = "EDAM_format:3879"
    """
    Format of topology files; containing the static information of a structure molecular system that is needed for a molecular simulation.
    Many different file formats exist describing structural molecular topology. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS top, CHARMM psf, AMBER prmtop).
    """
    GROMACS_top = "EDAM_format:3880"
    """
    GROMACS MD package top textual files define an entire structure system topology, either directly, or by including itp files.
    There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package.
    """
    AMBER_top = "EDAM_format:3881"
    """
    AMBER Prmtop file (version 7) is a structure topology text file divided in several sections designed to be parsed easily using simple Fortran code. Each section contains particular topology information, such as atom name, charge, mass, angles, dihedrals, etc.
    It can be modified manually, but as the size of the system increases, the hand-editing becomes increasingly complex. AMBER Parameter-Topology file format is used extensively by the AMBER software suite and is referred to as the Prmtop file for short.
    version 7 is written to distinguish it from old versions of AMBER Prmtop. Similarly to HDF5, it is a completely different format, according to AMBER group: a drastic change to the file format occurred with the 2004 release of Amber 7 (http://ambermd.org/prmtop.pdf)
    """
    PSF = "EDAM_format:3882"
    """
    The high similarity in the functional form of the two potential energy functions used by AMBER and CHARMM force-fields gives rise to the possible use of one force-field within the other MD engine. Therefore, the conversion of PSF files to AMBER Prmtop format is possible with the use of AMBER chamber (CHARMM - AMBER) program.
    X-Plor Protein Structure Files (PSF) are structure topology files used by NAMD and CHARMM molecular simulations programs. PSF files contain six main sections of interest: atoms, bonds, angles, dihedrals, improper dihedrals (force terms used to maintain planarity) and cross-terms.
    """
    GROMACS_itp = "EDAM_format:3883"
    """
    GROMACS itp files (include topology) contain structure topology information, and are typically included in GROMACS topology files (GROMACS top). Itp files are used to define individual (or multiple) components of a topology as a separate file. This is particularly useful if there is a molecule that is used frequently, and also reduces the size of the system topology file, splitting it in different parts.
    GROMACS itp files are used also to define position restrictions on the molecule, or to define the force field parameters for a particular ligand.
    """
    FF_parameter_format = "EDAM_format:3884"
    """
    Format of force field parameter files, which store the set of parameters (charges, masses, radii, bond lengths, bond dihedrals, etc.) that are essential for the proper description and simulation of a molecular system.
    Many different file formats exist describing force field parameters. Typically, each MD package or simulation software works with their own implementation (e.g. GROMACS itp, CHARMM rtf, AMBER off / frcmod).
    """
    BinPos = "EDAM_format:3885"
    """
    It is basically a translation of the ASCII atom coordinate format to binary code. The only additional information stored is a magic number that identifies the BinPos format and the number of atoms per snapshot. The remainder is the chain of coordinates binary encoded. A drawback of this format is its architecture dependency. Integers and floats codification depends on the architecture, thus it needs to be converted if working in different platforms (little endian, big endian).
    Scripps Research Institute BinPos format is a binary formatted file to store atom coordinates.
    """
    RST = "EDAM_format:3886"
    """
    AMBER coordinate/restart file with 6 coordinates per line and decimal format F12.7 (fixed point notation with field width 12 and 7 decimal places).
    """
    CHARMM_rtf = "EDAM_format:3887"
    """
    Format of CHARMM Residue Topology Files (RTF), which define groups by including the atoms, the properties of the group, and bond and charge information.
    There is currently no tool available for conversion between GROMACS topology format and other formats, due to the internal differences in both approaches. There is, however, a method to convert small molecules parameterized with AMBER force-field into GROMACS format, allowing simulations of these systems with GROMACS MD package.
    """
    AMBER_frcmod = "EDAM_format:3888"
    """
    AMBER frcmod (Force field Modification) is a file format to store any modification to the standard force field needed for a particular molecule to be properly represented in the simulation.
    """
    AMBER_off = "EDAM_format:3889"
    """
    AMBER Object File Format library files (OFF library files) store residue libraries (forcefield residue parameters).
    """
    NMReDATA = "EDAM_format:3906"
    """
    MReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or "NMReDATA") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc.
    NMReData is a text based data standard for processed NMR data. It is relying on SDF molecule data and allows to store assignments of NMR peaks to molecule features. The NMR-extracted data (or "NMReDATA") includes: Chemical shift,scalar coupling, 2D correlation, assignment, etc. Find more in the paper at https://doi.org/10.1002/mrc.4527.
    """
    BpForms = "EDAM_format:3909"
    """
    BpForms is a string format for concretely representing the primary structures of biopolymers, including DNA, RNA, and proteins that include non-canonical nucleic and amino acids. See https://www.bpforms.org for more information.
    """
    trr = "EDAM_format:3910"
    """
    Format of trr files that contain the trajectory of a simulation experiment used by GROMACS.
    The first 4 bytes of any trr file containing 1993. See https://github.com/galaxyproject/galaxy/pull/6597/files#diff-409951594551183dbf886e24de6cb129R760
    """
    msh = "EDAM_format:3911"
    """
    Mash sketch is a format for sequence / sequence checksum information. To make a sketch, each k-mer in a sequence is hashed, which creates a pseudo-random identifier. By sorting these hashes, a small subset from the top of the sorted list can represent the entire sequence.
    """
    Loom = "EDAM_format:3913"
    """
    The Loom file format is based on HDF5, a standard for storing large numerical datasets. The Loom format is designed to efficiently hold large omics datasets. Typically, such data takes the form of a large matrix of numbers, along with metadata for the rows and columns.
    """
    Zarr = "EDAM_format:3915"
    """
    The Zarr format is an implementation of chunked, compressed, N-dimensional arrays for storing data.
    """
    MTX = "EDAM_format:3916"
    """
    The Matrix Market matrix (MTX) format stores numerical or pattern matrices in a dense (array format) or sparse (coordinate format) representation.
    """
    BcForms = "EDAM_format:3951"
    """
    BcForms is a format for abstractly describing the molecular structure (atoms and bonds) of macromolecular complexes as a collection of subunits and crosslinks. Each subunit can be described with BpForms (http://edamontology.org/format_3909) or SMILES (http://edamontology.org/data_2301). BcForms uses an ontology of crosslinks to abstract the chemical details of crosslinks from the descriptions of complexes (see https://bpforms.org/crosslink.html).
    BcForms is related to http://edamontology.org/format_3909. (BcForms uses BpForms to describe subunits which are DNA, RNA, or protein polymers.) However, that format isn't the parent of BcForms. BcForms is similarly related to SMILES (http://edamontology.org/data_2301).
    """
    N_Quads = "EDAM_format:3956"
    """
    N-Quads is a line-based, plain text format for encoding an RDF dataset. It includes information about the graph each triple belongs to.
    N-Quads should not be confused with N-Triples which does not contain graph information.
    """
    Vega = "EDAM_format:3969"
    """
    Vega is a visualization grammar, a declarative language for creating, saving, and sharing interactive visualization designs. With Vega, you can describe the visual appearance and interactive behavior of a visualization in a JSON format, and generate web-based views using Canvas or SVG.
    """
    Vega_lite = "EDAM_format:3970"
    """
    Vega-Lite is a high-level grammar of interactive graphics. It provides a concise JSON syntax for rapidly generating visualizations to support analysis. Vega-Lite specifications can be compiled to Vega specifications.
    """
    NeuroML = "EDAM_format:3971"
    """
    A model description language for computational neuroscience.
    """
    BNGL = "EDAM_format:3972"
    """
    BioNetGen is a format for the specification and simulation of rule-based models of biochemical systems, including signal transduction, metabolic, and genetic regulatory networks.
    """
    Docker_image = "EDAM_format:3973"
    """
    A Docker image is a file, comprised of multiple layers, that is used to execute code in a Docker container. An image is essentially built from the instructions for a complete and executable version of an application, which relies on the host OS kernel.
    """
    GFA_1 = "EDAM_format:3975"
    """
    Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology.
    """
    GFA_2 = "EDAM_format:3976"
    """
    Graphical Fragment Assembly captures sequence graphs as the product of an assembly, a representation of variation in genomes, splice graphs in genes, or even overlap between reads from long-read sequencing technology. GFA2 is an update of GFA1 which is not compatible with GFA1.
    """
    ObjTables = "EDAM_format:3977"
    """
    ObjTables is a toolkit for creating re-usable datasets that are both human and machine-readable, combining the ease of spreadsheets (e.g., Excel workbooks) with the rigor of schemas (classes, their attributes, the type of each attribute, and the possible relationships between instances of classes). ObjTables consists of a format for describing schemas for spreadsheets, numerous data types for science, a syntax for indicating the class and attribute represented by each table and column in a workbook, and software for using schemas to rigorously validate, merge, split, compare, and revision datasets.
    """
    CONTIG = "EDAM_format:3978"
    """
    The CONTIG format used for output of the SOAPdenovo alignment program. It contains contig sequences generated without using mate pair information.
    """
    WEGO = "EDAM_format:3979"
    """
    WEGO native format used by the Web Gene Ontology Annotation Plot application.   Tab-delimited format with gene names and others GO IDs (columns) with one annotation record per line.
    """
    RPKM = "EDAM_format:3980"
    """
    For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
    Tab-delimited format for gene expression levels table, calculated as Reads Per Kilobase per Million (RPKM) mapped reads.
    """
    TAR_format = "EDAM_format:3981"
    """
    For example a 1kb transcript with 1000 alignments in a sample of 10 million reads (out of which 8 million reads can be mapped) will have RPKM = 1000/(1 * 8) = 125
    TAR archive file format generated by the Unix-based utility tar.
    """
    CHAIN = "EDAM_format:3982"
    """
    The CHAIN format describes a pairwise alignment that allow gaps in both sequences simultaneously and is used by the UCSC Genome Browser.
    """
    NET = "EDAM_format:3983"
    """
    The NET file format is used to describe the data that underlie the net alignment annotations in the UCSC Genome Browser.
    """
    QMAP = "EDAM_format:3984"
    """
    Format of QMAP files generated for methylation data from an internal BGI pipeline.
    """
    gxformat2 = "EDAM_format:3985"
    """
    An emerging format for high-level Galaxy workflow description.
    """
    WMV = "EDAM_format:3986"
    """
    The proprietary native video format of various Microsoft programs such as Windows Media Player.
    """
    ZIP_format = "EDAM_format:3987"
    """
    A ZIP file may contain one or more files or directories that may have been compressed.
    ZIP is an archive file format that supports lossless data compression.
    """
    LSM = "EDAM_format:3988"
    """
    LSM files are the default data export for the Zeiss LSM series confocal microscopes (e.g. LSM 510, LSM 710). In addition to the image data, LSM files contain most imaging settings.
    Zeiss' proprietary image format based on TIFF.
    """
    GZIP_format = "EDAM_format:3989"
    """
    GNU zip compressed file format common to Unix-based operating systems.
    """
    AVI = "EDAM_format:3990"
    """
    Audio Video Interleaved (AVI) format is a multimedia container format for AVI files, that allows synchronous audio-with-video playback.
    """
    TrackDB = "EDAM_format:3991"
    """
    A declaration file format for UCSC browsers track dataset display charateristics.
    """
    CIGAR_format = "EDAM_format:3992"
    """
    Compact Idiosyncratic Gapped Alignment Report format is a compressed (run-length encoded) pairwise alignment format. It is useful for representing long (e.g. genomic) pairwise alignments.
    """
    Stereolithography_format = "EDAM_format:3993"
    """
    STL is a file format native to the stereolithography CAD software created by 3D Systems. The format is used to save and share surface-rendered 3D images and also for 3D printing.
    """
    U3D = "EDAM_format:3994"
    """
    U3D (Universal 3D) is a compressed file format and data structure for 3D computer graphics. It contains 3D model information such as triangle meshes, lighting, shading, motion data, lines and points with color and structure.
    """
    Texture_file_format = "EDAM_format:3995"
    """
    Bitmap image format used for storing textures.
    Texture files can create the appearance of different surfaces and can be applied to both 2D and 3D objects. Note the file extension .tex is also used for LaTex documents which are a completely different format and they are NOT interchangeable.
    """
    Python_script = "EDAM_format:3996"
    """
    Format for scripts writtenin Python - a widely used high-level programming language for general-purpose programming.
    """
    MPEG_4 = "EDAM_format:3997"
    """
    A digital multimedia container format most commonly used to store video and audio.
    """
    Perl_script = "EDAM_format:3998"
    """
    Format for scripts written in Perl - a family of high-level, general-purpose, interpreted, dynamic programming languages.
    """
    R_script = "EDAM_format:3999"
    """
    Format for scripts written in the R language - an open source programming language and software environment for statistical computing and graphics that is supported by the R Foundation for Statistical Computing.
    """
    R_markdown = "EDAM_format:4000"
    """
    A file format for making dynamic documents (R Markdown scripts) with the R language.
    """
    pickle = "EDAM_format:4002"
    """
    Format used by Python pickle module for serializing and de-serializing a Python object structure.
    """
    NumPy_format = "EDAM_format:4003"
    """
    The standard binary file format used by NumPy - a fundamental package for scientific computing with Python - for persisting a single arbitrary NumPy array on disk. The format stores all of the shape and dtype information necessary to reconstruct the array correctly.
    """
    SimTools_repertoire_file_format = "EDAM_format:4004"
    """
    Format of repertoire (archive) files that can be read by SimToolbox (a MATLAB toolbox for structured illumination fluorescence microscopy) or alternatively extracted with zip file archiver software.
    """
    Configuration_file_format = "EDAM_format:4005"
    """
    A configuration file used by various programs to store settings that are specific to their respective software.
    """
    Zstandard_format = "EDAM_format:4006"
    """
    Format used by the Zstandard real-time compression algorithm.
    """
    MATLAB_script = "EDAM_format:4007"
    """
    The file format for MATLAB scripts or functions.
    """
    PEtab = "EDAM_format:4015"
    """
    A data format for specifying parameter estimation problems in systems biology.
    """
    gVCF = "EDAM_format:4018"
    """
    Genomic Variant Call Format (gVCF) is a version of VCF that includes not only the positions that are variant when compared to a reference genome, but also the non-variant positions as ranges, including metrics of confidence that the positions in the range are actually non-variant e.g. minimum read-depth and genotype quality.
    """
    cml = "EDAM_format:4023"
    """
    Chemical Markup Language (CML) is an XML-based format for encoding detailed information about a wide range of chemical concepts.
    """
    cif = "EDAM_format:4024"
    """
    Crystallographic Information File (CIF) is a data exchange standard file format for Crystallographic Information and related Structural Science data.
    """
    BioSimulators_format_for_the_specifications_of_biosimulation_tools = "EDAM_format:4025"
    """
    Format for describing the capabilities of a biosimulation tool including the modeling frameworks, simulation algorithms, and modeling formats that it supports, as well as metadata such as a list of the interfaces, programming languages, and operating systems supported by the tool; a link to download the tool; a list of the authors of the tool; and the license to the tool.
    """
    BioSimulators_standard_for_command_line_interfaces_for_biosimulation_tools = "EDAM_format:4026"
    """
    Outlines the syntax and semantics of the input and output arguments for command-line interfaces for biosimulation tools.
    """
    PQR = "EDAM_format:4035"
    """
    Data format derived from the standard PDB format, which enables user to incorporate parameters for charge and radius to the existing PDB data file.
    """
    PDBQT = "EDAM_format:4036"
    """
    Data format used in AutoDock 4 for storing atomic coordinates, partial atomic charges and AutoDock atom types for both receptors and ligands.
    """
    MSP = "EDAM_format:4039"
    """
    MSP is a data format for mass spectrometry data.
    NIST Text file format for storing MS∕MS spectra (m∕z and intensity of mass peaks) along with additional annotations for each spectrum. A single MSP file can thus contain single or multiple spectra. This format is frequently used to share spectra libraries.
    """
    maDMP = "EDAM_format:4041"
    """
    A standard for DMPs developed by the Research Data Alliance
    """
    Nextflow = "EDAM_format:4048"
    """
    Nextflow is a workflow system for creating scalable, portable, and reproducible workflows.
    This term covers all versions of Nextflow language specifications.
    """
    Snakemake = "EDAM_format:4049"
    """
    The Snakemake workflow management system is a tool to create reproducible and scalable data analyses.
    """
    SDRF = "EDAM_format:4050"
    """
    Sample and Data Relationship File for a proteomics experiment.
    """
    mzTab_M = "EDAM_format:4058"
    """
    The reference implementation of mzTab-M in Java is https://github.com/lifs-tools/jmzTab-m.
    mzTab-M is a light-weight, tab-delimited format for mass spectrometry-based chemical profiling data, including metabolomics.
    mzTab-M is alternatively named mzTab 2.0, but in 2025 there is a draft version 2.1 of mzTab-M.
    mzTab-M is not compatible with mzTab (also named mzTab 1.0, for proteomics, http://edamontology.org/format_3681). Note: the repository, website, and file extension are the same for both formats.
    """
    mzTab_L = "EDAM_format:4059"
    """
    mzTab-L is a light-weight, tab-delimited format for mass spectrometry-based lipidomics data. It is a compatible version of mzTab-M, with additional rules and information standard (reporting guidelines).
    """


class EnumEDAMDataTypes(str, Enum):
    """
    Data types from the EDAM ontology.
    """
    Ontology = "EDAM_data:0582"
    """
    An ontology of biological or bioinformatics concepts and relations, a controlled vocabulary, structured glossary etc.
    """
    Identifier = "EDAM_data:0842"
    """
    A text token, number or something else which identifies an entity, but which may not be persistent (stable) or unique (the same identifier may identify multiple things).
    """
    Molecular_mass = "EDAM_data:0844"
    """
    Mass of a molecule.
    """
    Molecular_charge = "EDAM_data:0845"
    """
    Net charge of a molecule.
    """
    Chemical_formula = "EDAM_data:0846"
    """
    A specification of a chemical structure.
    """
    QSAR_descriptor = "EDAM_data:0847"
    """
    A QSAR quantitative descriptor (name-value pair) of chemical structure.
    QSAR descriptors have numeric values that quantify chemical information encoded in a symbolic representation of a molecule. They are used in quantitative structure activity relationship (QSAR) applications. Many subtypes of individual descriptors (not included in EDAM) cover various types of protein properties.
    """
    Sequence_record = "EDAM_data:0849"
    """
    A molecular sequence and associated metadata.
    """
    Sequence_set = "EDAM_data:0850"
    """
    A collection of one or typically multiple molecular sequences (which can include derived data or metadata) that do not (typically) correspond to molecular sequence database records or entries and which (typically) are derived from some analytical method.
    An example is an alignment reference; one or a set of reference molecular sequences, structures, or profiles used for alignment of genomic, transcriptomic, or proteomic experimental data.
    This concept may be used for arbitrary sequence sets and associated data arising from processing.
    """
    Sequence_feature_source = "EDAM_data:0856"
    """
    How the annotation of a sequence feature (for example in EMBL or Swiss-Prot) was derived.
    This might be the name and version of a software tool, the name of a database, or 'curated' to indicate a manual annotation (made by a human).
    """
    Sequence_search_results = "EDAM_data:0857"
    """
    A report of sequence hits and associated data from searching a database of sequences (for example a BLAST search). This will typically include a list of scores (often with statistical evaluation) and a set of alignments for the hits.
    The score list includes the alignment score, percentage of the query sequence matched, length of the database sequence entry in this alignment, identifier of the database sequence entry, excerpt of the database sequence entry description etc.
    """
    Sequence_signature_matches = "EDAM_data:0858"
    """
    A "profile-profile alignment" is an alignment of two sequence profiles, each profile typically representing a sequence alignment.
    A "sequence-profile alignment" is an alignment of one or more molecular sequence(s) to one or more sequence profile(s) (each profile typically representing a sequence alignment).
    Report on the location of matches ("hits") between sequences, sequence profiles, motifs (conserved or functional patterns) and other types of sequence signatures.
    This includes reports of hits from a search of a protein secondary or domain database. Data associated with the search or alignment might also be included, e.g. ranked list of best-scoring sequences, a graphical representation of scores etc.
    """
    Sequence_signature_data = "EDAM_data:0860"
    """
    Sequence signature data concerns specific or conserved pattern in molecular sequences and the classifiers used for their identification, including sequence motifs, profiles or other diagnostic element.
    This can include metadata about a motif or sequence profile such as its name, length, technical details about the profile construction, and so on.
    """
    Dotplot = "EDAM_data:0862"
    """
    A dotplot of sequence similarities identified from word-matching or character comparison.
    """
    Sequence_alignment = "EDAM_data:0863"
    """
    Alignment of multiple molecular sequences.
    """
    Sequence_similarity_score = "EDAM_data:0865"
    """
    A value representing molecular sequence similarity.
    """
    Sequence_alignment_report = "EDAM_data:0867"
    """
    An informative report of molecular sequence alignment-derived data or metadata.
    Use this for any computer-generated reports on sequence alignments, and for general information (metadata) on a sequence alignment, such as a description, sequence identifiers and alignment score.
    """
    Sequence_distance_matrix = "EDAM_data:0870"
    """
    A matrix of estimated evolutionary distance between molecular sequences, such as is suitable for phylogenetic tree calculation.
    Methods might perform character compatibility analysis or identify patterns of similarity in an alignment or data matrix.
    """
    Phylogenetic_character_data = "EDAM_data:0871"
    """
    As defined, this concept would also include molecular sequences, microsatellites, polymorphisms (RAPDs, RFLPs, or AFLPs), restriction sites and fragments
    Basic character data from which a phylogenetic tree may be generated.
    """
    Phylogenetic_tree = "EDAM_data:0872"
    """
    A phylogenetic tree is usually constructed from a set of sequences from which an alignment (or data matrix) is calculated. See also 'Phylogenetic tree image'.
    The raw data (not just an image) from which a phylogenetic tree is directly generated or plotted, such as topology, lengths (in time or in expected amounts of variance) and a confidence interval for each length.
    """
    Comparison_matrix = "EDAM_data:0874"
    """
    Matrix of integer or floating point numbers for amino acid or nucleotide sequence comparison.
    The comparison matrix might include matrix name, optional comment, height and width (or size) of matrix, an index row/column (of characters) and data rows/columns (of integers or floats).
    """
    Protein_secondary_structure_alignment = "EDAM_data:0878"
    """
    Alignment of the (1D representations of) secondary structure of two or more proteins.
    """
    RNA_secondary_structure = "EDAM_data:0880"
    """
    An informative report of secondary structure (predicted or real) of an RNA molecule.
    This includes thermodynamically stable or evolutionarily conserved structures such as knots, pseudoknots etc.
    """
    RNA_secondary_structure_alignment = "EDAM_data:0881"
    """
    Alignment of the (1D representations of) secondary structure of two or more RNA molecules.
    """
    Structure = "EDAM_data:0883"
    """
    3D coordinate and associated data for a macromolecular tertiary (3D) structure or part of a structure.
    The coordinate data may be predicted or real.
    """
    Structure_alignment = "EDAM_data:0886"
    """
    A tertiary structure alignment will include the untransformed coordinates of one macromolecule, followed by the second (or subsequent) structure(s) with all the coordinates transformed (by rotation / translation) to give a superposition.
    Alignment (superimposition) of molecular tertiary (3D) structures.
    """
    Structure_alignment_report = "EDAM_data:0887"
    """
    An informative report of molecular tertiary structure alignment-derived data.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Structure_similarity_score = "EDAM_data:0888"
    """
    A value representing molecular structure similarity, measured from structure alignment or some other type of structure comparison.
    """
    Structural_profile = "EDAM_data:0889"
    """
    Some type of structural (3D) profile or template (representing a structure or structure alignment).
    """
    Structural_LEFT_PARENTHESIS3DRIGHT_PARENTHESIS_profile_alignment = "EDAM_data:0890"
    """
    A 3D profile-3D profile alignment (each profile representing structures or a structure alignment).
    """
    Protein_sequence_structure_scoring_matrix = "EDAM_data:0892"
    """
    Matrix of values used for scoring sequence-structure compatibility.
    """
    Sequence_structure_alignment = "EDAM_data:0893"
    """
    An alignment of molecular sequence to structure (from threading sequence(s) through 3D structure or representation of structure(s)).
    """
    Protein_report = "EDAM_data:0896"
    """
    An informative human-readable report about one or more specific protein molecules or protein structural domains, derived from analysis of primary (sequence or structural) data.
    """
    Protein_property = "EDAM_data:0897"
    """
    A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a protein molecule or model.
    This is a broad data type and is used a placeholder for other, more specific types. Data may be based on analysis of nucleic acid sequence or structural data, for example reports on the surface properties (shape, hydropathy, electrostatic patches etc) of a protein structure, protein flexibility or motion, and protein architecture (spatial arrangement of secondary structure).
    """
    Protein_interaction_raw_data = "EDAM_data:0905"
    """
    Protein-protein interaction data from for example yeast two-hybrid analysis, protein microarrays, immunoaffinity chromatography followed by mass spectrometry, phage display etc.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.
    """
    Protein_interaction_data = "EDAM_data:0906"
    """
    Data concerning the interactions (predicted or known) within or between a protein, structural domain or part of a protein. This includes intra- and inter-residue contacts and distances, as well as interactions with other proteins and non-protein entities such as nucleic acid, metal atoms, water, ions etc.
    """
    Protein_family_report = "EDAM_data:0907"
    """
    An informative report on a specific protein family or other classification or group of protein sequences or structures.
    """
    Vmax = "EDAM_data:0909"
    """
    The maximum initial velocity or rate of a reaction. It is the limiting velocity as substrate concentrations get very large.
    """
    Km = "EDAM_data:0910"
    """
    Km is the concentration (usually in Molar units) of substrate that leads to half-maximal velocity of an enzyme-catalysed reaction.
    """
    Nucleic_acid_property = "EDAM_data:0912"
    """
    A report of primarily non-positional data describing intrinsic physical, chemical or other properties of a nucleic acid molecule.
    Nucleic acid structural properties stiffness, curvature, twist/roll data or other conformational parameters or properties.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Codon_usage_data = "EDAM_data:0914"
    """
    Data derived from analysis of codon usage (typically a codon usage table) of DNA sequences.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Gene_report = "EDAM_data:0916"
    """
    A report on predicted or actual gene structure, regions which make an RNA product and features such as promoters, coding regions, splice sites etc.
    This includes any report on a particular locus or gene. This might include the gene name, description, summary and so on. It can include details about the function of a gene, such as its encoded protein or a functional classification of the gene sequence along according to the encoded protein(s).
    """
    Chromosome_report = "EDAM_data:0919"
    """
    A human-readable collection of information about a specific chromosome.
    This includes basic information. e.g. chromosome number, length, karyotype features, chromosome sequence etc.
    """
    GenotypeSOLIDUSphenotype_report = "EDAM_data:0920"
    """
    A human-readable collection of information about the set of genes (or allelic forms) present in an individual, organism or cell and associated with a specific physical characteristic, or a report concerning an organisms traits and phenotypes.
    """
    Sequence_trace = "EDAM_data:0924"
    """
    Fluorescence trace data generated by an automated DNA sequencer, which can be interpreted as a molecular sequence (reads), given associated sequencing metadata such as base-call quality scores.
    This is the raw data produced by a DNA sequencing machine.
    """
    Sequence_assembly = "EDAM_data:0925"
    """
    An assembly of fragments of a (typically genomic) DNA sequence.
    Typically, an assembly is a collection of contigs (for example ESTs and genomic DNA fragments) that are ordered, aligned and merged. Annotation of the assembled sequence might be included.
    """
    RH_scores = "EDAM_data:0926"
    """
    Radiation Hybrid (RH) scores are used in Radiation Hybrid mapping.
    Radiation hybrid scores (RH) scores for one or more markers.
    """
    Genetic_linkage_report = "EDAM_data:0927"
    """
    A human-readable collection of information about the linkage of alleles.
    This includes linkage disequilibrium; the non-random association of alleles or polymorphisms at two or more loci (not necessarily on the same chromosome).
    """
    Gene_expression_profile = "EDAM_data:0928"
    """
    Data quantifying the level of expression of (typically) multiple genes, derived for example from microarray experiments.
    """
    Electron_density_map = "EDAM_data:0937"
    """
    X-ray crystallography data.
    """
    Raw_NMR_data = "EDAM_data:0938"
    """
    Nuclear magnetic resonance (NMR) raw data, typically for a protein.
    """
    CD_spectra = "EDAM_data:0939"
    """
    Protein secondary structure from protein coordinate or circular dichroism (CD) spectroscopic data.
    """
    Volume_map = "EDAM_data:0940"
    """
    Volume map data from electron microscopy.
    """
    number_2D_PAGE_image = "EDAM_data:0942"
    """
    Two-dimensional gel electrophoresis image.
    """
    Mass_spectrum = "EDAM_data:0943"
    """
    Spectra from mass spectrometry.
    """
    Peptide_mass_fingerprint = "EDAM_data:0944"
    """
    A molecular weight standard fingerprint is standard protonated molecular masses e.g. from trypsin (modified porcine trypsin, Promega) and keratin peptides.
    A set of peptide masses (peptide mass fingerprint) from mass spectrometry.
    """
    Peptide_identification = "EDAM_data:0945"
    """
    Protein or peptide identifications with evidence supporting the identifications, for example from comparing a peptide mass fingerprint (from mass spectrometry) to a sequence database, or the set of typical spectra one obtains when running a protein through a mass spectrometer.
    """
    Workflow_metadata = "EDAM_data:0949"
    """
    Basic information, annotation or documentation concerning a workflow (but not the workflow itself).
    """
    Mathematical_model = "EDAM_data:0950"
    """
    A biological model represented in mathematical terms.
    """
    Statistical_estimate_score = "EDAM_data:0951"
    """
    A value representing estimated statistical significance of some observed data; typically sequence database hits.
    """
    Database_cross_mapping = "EDAM_data:0954"
    """
    A mapping of the accession numbers (or other database identifier) of entries between (typically) two biological or biomedical databases.
    The cross-mapping is typically a table where each row is an accession number and each column is a database being cross-referenced. The cells give the accession number or identifier of the corresponding entry in a database. If a cell in the table is not filled then no mapping could be found for the database. Additional information might be given on version, date etc.
    """
    Data_index = "EDAM_data:0955"
    """
    An index of data of biological relevance.
    """
    Data_index_report = "EDAM_data:0956"
    """
    A human-readable collection of information concerning an analysis of an index of biological data.
    """
    Database_metadata = "EDAM_data:0957"
    """
    Basic information on bioinformatics database(s) or other data sources such as name, type, description, URL etc.
    """
    Tool_metadata = "EDAM_data:0958"
    """
    Basic information about one or more bioinformatics applications or packages, such as name, type, description, or other documentation.
    """
    User_metadata = "EDAM_data:0960"
    """
    Textual metadata on a software author or end-user, for example a person or other software.
    """
    Small_molecule_report = "EDAM_data:0962"
    """
    A human-readable collection of information about a specific chemical compound.
    """
    Cell_line_report = "EDAM_data:0963"
    """
    A human-readable collection of information about a particular strain of organism cell line including plants, virus, fungi and bacteria. The data typically includes strain number, organism type, growth conditions, source and so on.
    """
    Ontology_term = "EDAM_data:0966"
    """
    A term (name) from an ontology.
    """
    Ontology_concept_data = "EDAM_data:0967"
    """
    Data concerning or derived from a concept from a biological ontology.
    """
    Keyword = "EDAM_data:0968"
    """
    Boolean operators (AND, OR and NOT) and wildcard characters may be allowed.
    Keyword(s) or phrase(s) used (typically) for text-searching purposes.
    """
    Citation = "EDAM_data:0970"
    """
    A bibliographic reference might include information such as authors, title, journal name, date and (possibly) a link to the abstract or full-text of the article if available.
    Bibliographic data that uniquely identifies a scientific article, book or other published material.
    """
    Article = "EDAM_data:0971"
    """
    A scientific text, typically a full text article from a scientific journal.
    """
    Text_mining_report = "EDAM_data:0972"
    """
    A human-readable collection of information resulting from text mining.
    A text mining abstract will typically include an annotated a list of words or sentences extracted from one or more scientific articles.
    """
    Identifier_LEFT_PARENTHESISby_type_of_entityRIGHT_PARENTHESIS = "EDAM_data:0976"
    """
    An identifier that identifies a particular type of data.
    This concept exists only to assist EDAM maintenance and navigation in graphical browsers. It does not add semantic information. This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'.
    """
    Tool_identifier = "EDAM_data:0977"
    """
    An identifier of a bioinformatics tool, e.g. an application or web service.
    """
    Molecule_identifier = "EDAM_data:0982"
    """
    Name or other identifier of a molecule.
    """
    Atom_ID = "EDAM_data:0983"
    """
    Identifier (e.g. character symbol) of a specific atom.
    """
    Molecule_name = "EDAM_data:0984"
    """
    Name of a specific molecule.
    """
    Chromosome_name = "EDAM_data:0987"
    """
    Name of a chromosome.
    """
    Peptide_identifier = "EDAM_data:0988"
    """
    Identifier of a peptide chain.
    """
    Protein_identifier = "EDAM_data:0989"
    """
    Identifier of a protein.
    """
    Compound_name = "EDAM_data:0990"
    """
    Unique name of a chemical compound.
    """
    Chemical_registry_number = "EDAM_data:0991"
    """
    Unique registry number of a chemical compound.
    """
    Drug_identifier = "EDAM_data:0993"
    """
    Identifier of a drug.
    """
    Amino_acid_identifier = "EDAM_data:0994"
    """
    Identifier of an amino acid.
    """
    Nucleotide_identifier = "EDAM_data:0995"
    """
    Name or other identifier of a nucleotide.
    """
    Monosaccharide_identifier = "EDAM_data:0996"
    """
    Identifier of a monosaccharide.
    """
    Chemical_name_LEFT_PARENTHESISChEBIRIGHT_PARENTHESIS = "EDAM_data:0997"
    """
    This is the recommended chemical name for use for example in database annotation.
    Unique name from Chemical Entities of Biological Interest (ChEBI) of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISIUPACRIGHT_PARENTHESIS = "EDAM_data:0998"
    """
    IUPAC recommended name of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISINNRIGHT_PARENTHESIS = "EDAM_data:0999"
    """
    International Non-proprietary Name (INN or 'generic name') of a chemical compound, assigned by the World Health Organisation (WHO).
    """
    Chemical_name_LEFT_PARENTHESISbrandRIGHT_PARENTHESIS = "EDAM_data:1000"
    """
    Brand name of a chemical compound.
    """
    Chemical_name_LEFT_PARENTHESISsynonymousRIGHT_PARENTHESIS = "EDAM_data:1001"
    """
    Synonymous name of a chemical compound.
    """
    CAS_number = "EDAM_data:1002"
    """
    CAS registry number of a chemical compound; a unique numerical identifier of chemicals in the scientific literature, as assigned by the Chemical Abstracts Service.
    """
    Chemical_registry_number_LEFT_PARENTHESISBeilsteinRIGHT_PARENTHESIS = "EDAM_data:1003"
    """
    Beilstein registry number of a chemical compound.
    """
    Chemical_registry_number_LEFT_PARENTHESISGmelinRIGHT_PARENTHESIS = "EDAM_data:1004"
    """
    Gmelin registry number of a chemical compound.
    """
    HET_group_name = "EDAM_data:1005"
    """
    3-letter code word for a ligand (HET group) from a PDB file, for example ATP.
    """
    Amino_acid_name = "EDAM_data:1006"
    """
    String of one or more ASCII characters representing an amino acid.
    """
    Nucleotide_code = "EDAM_data:1007"
    """
    String of one or more ASCII characters representing a nucleotide.
    """
    Polypeptide_chain_ID = "EDAM_data:1008"
    """
    Identifier of a polypeptide chain from a protein.
    This is typically a character (for the chain) appended to a PDB identifier, e.g. 1cukA
    """
    Protein_name = "EDAM_data:1009"
    """
    Name of a protein.
    """
    Enzyme_identifier = "EDAM_data:1010"
    """
    Name or other identifier of an enzyme or record from a database of enzymes.
    """
    EC_number = "EDAM_data:1011"
    """
    An Enzyme Commission (EC) number of an enzyme.
    """
    Enzyme_name = "EDAM_data:1012"
    """
    Name of an enzyme.
    """
    Restriction_enzyme_name = "EDAM_data:1013"
    """
    Name of a restriction enzyme.
    """
    Sequence_feature_ID = "EDAM_data:1015"
    """
    A unique identifier of molecular sequence feature, for example an ID of a feature that is unique within the scope of the GFF file.
    """
    Sequence_position = "EDAM_data:1016"
    """
    A position of one or more points (base or residue) in a sequence, or part of such a specification.
    """
    Sequence_range = "EDAM_data:1017"
    """
    Specification of range(s) of sequence positions.
    """
    Sequence_feature_key = "EDAM_data:1020"
    """
    A feature key indicates the biological nature of the feature or information about changes to or versions of the sequence.
    The type of a sequence feature, typically a term or accession from the Sequence Ontology, for example an EMBL or Swiss-Prot sequence feature key.
    """
    Sequence_feature_qualifier = "EDAM_data:1021"
    """
    Feature qualifiers hold information about a feature beyond that provided by the feature key and location.
    Typically one of the EMBL or Swiss-Prot feature qualifiers.
    """
    Sequence_feature_label = "EDAM_data:1022"
    """
    A feature label identifies a feature of a sequence database entry. When used with the database name and the entry's primary accession number, it is a unique identifier of that feature.
    A name of a sequence feature, e.g. the name of a feature to be displayed to an end-user. Typically an EMBL or Swiss-Prot feature label.
    """
    EMBOSS_Uniform_Feature_Object = "EDAM_data:1023"
    """
    The name of a sequence feature-containing entity adhering to the standard feature naming scheme used by all EMBOSS applications.
    """
    Gene_identifier = "EDAM_data:1025"
    """
    An identifier of a gene, such as a name/symbol or a unique identifier of a gene in a database.
    """
    Gene_symbol = "EDAM_data:1026"
    """
    The short name of a gene; a single word that does not contain white space characters. It is typically derived from the gene name.
    """
    Gene_ID_LEFT_PARENTHESISNCBIRIGHT_PARENTHESIS = "EDAM_data:1027"
    """
    An NCBI unique identifier of a gene.
    """
    Gene_ID_LEFT_PARENTHESISCGDRIGHT_PARENTHESIS = "EDAM_data:1031"
    """
    Identifier of a gene or feature from the CGD database.
    """
    Gene_ID_LEFT_PARENTHESISDictyBaseRIGHT_PARENTHESIS = "EDAM_data:1032"
    """
    Identifier of a gene from DictyBase.
    """
    Ensembl_gene_ID = "EDAM_data:1033"
    """
    Unique identifier for a gene (or other feature) from the Ensembl database.
    """
    Gene_ID_LEFT_PARENTHESISSGDRIGHT_PARENTHESIS = "EDAM_data:1034"
    """
    Identifier of an entry from the SGD database.
    """
    Gene_ID_LEFT_PARENTHESISGeneDBRIGHT_PARENTHESIS = "EDAM_data:1035"
    """
    Identifier of a gene from the GeneDB database.
    """
    TIGR_identifier = "EDAM_data:1036"
    """
    Identifier of an entry from the TIGR database.
    """
    TAIR_accession_LEFT_PARENTHESISgeneRIGHT_PARENTHESIS = "EDAM_data:1037"
    """
    Identifier of an gene from the TAIR database.
    """
    Protein_domain_ID = "EDAM_data:1038"
    """
    Identifier of a protein structural domain.
    This is typically a character or string concatenated with a PDB identifier and a chain identifier.
    """
    SCOP_domain_identifier = "EDAM_data:1039"
    """
    Identifier of a protein domain (or other node) from the SCOP database.
    """
    CATH_domain_ID = "EDAM_data:1040"
    """
    Identifier of a protein domain from CATH.
    """
    SCOP_concise_classification_string_LEFT_PARENTHESISsccsRIGHT_PARENTHESIS = "EDAM_data:1041"
    """
    A SCOP concise classification string (sccs) is a compact representation of a SCOP domain classification.
    An scss includes the class (alphabetical), fold, superfamily and family (all numerical) to which a given domain belongs.
    """
    SCOP_sunid = "EDAM_data:1042"
    """
    A sunid uniquely identifies an entry in the SCOP hierarchy, including leaves (the SCOP domains) and higher level nodes including entries corresponding to the protein level.
    Unique identifier (number) of an entry in the SCOP hierarchy, for example 33229.
    """
    CATH_node_ID = "EDAM_data:1043"
    """
    A code number identifying a node from the CATH database.
    """
    Kingdom_name = "EDAM_data:1044"
    """
    The name of a biological kingdom (Bacteria, Archaea, or Eukaryotes).
    """
    Species_name = "EDAM_data:1045"
    """
    The name of a species (typically a taxonomic group) of organism.
    """
    Strain_name = "EDAM_data:1046"
    """
    The name of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    URI = "EDAM_data:1047"
    """
    A string of characters that name or otherwise identify a resource on the Internet.
    """
    Database_ID = "EDAM_data:1048"
    """
    An identifier of a biological or bioinformatics database.
    """
    Directory_name = "EDAM_data:1049"
    """
    The name of a directory.
    """
    File_name = "EDAM_data:1050"
    """
    The name (or part of a name) of a file (of any type).
    """
    Ontology_name = "EDAM_data:1051"
    """
    Name of an ontology of biological or bioinformatics concepts and relations.
    """
    URL = "EDAM_data:1052"
    """
    A Uniform Resource Locator (URL).
    """
    URN = "EDAM_data:1053"
    """
    A Uniform Resource Name (URN).
    """
    LSID = "EDAM_data:1055"
    """
    A Life Science Identifier (LSID) - a unique identifier of some data.
    LSIDs provide a standard way to locate and describe data. An LSID is represented as a Uniform Resource Name (URN) with the following format: URN:LSID:<Authority>:<Namespace>:<ObjectID>[:<Version>]
    """
    Database_name = "EDAM_data:1056"
    """
    The name of a biological or bioinformatics database.
    """
    Enumerated_file_name = "EDAM_data:1058"
    """
    The name of a file (of any type) with restricted possible values.
    """
    File_name_extension = "EDAM_data:1059"
    """
    A file extension is the characters appearing after the final '.' in the file name.
    The extension of a file name.
    """
    File_base_name = "EDAM_data:1060"
    """
    A file base name is the file name stripped of its directory specification and extension.
    The base name of a file.
    """
    QSAR_descriptor_name = "EDAM_data:1061"
    """
    Name of a QSAR descriptor.
    """
    Sequence_identifier = "EDAM_data:1063"
    """
    An identifier of molecular sequence(s) or entries from a molecular sequence database.
    """
    Sequence_set_ID = "EDAM_data:1064"
    """
    An identifier of a set of molecular sequence(s).
    """
    Sequence_alignment_ID = "EDAM_data:1066"
    """
    Identifier of a molecular sequence alignment, for example a record from an alignment database.
    """
    Phylogenetic_tree_ID = "EDAM_data:1068"
    """
    Identifier of a phylogenetic tree for example from a phylogenetic tree database.
    """
    Comparison_matrix_identifier = "EDAM_data:1069"
    """
    An identifier of a comparison matrix.
    """
    Structure_ID = "EDAM_data:1070"
    """
    A unique and persistent identifier of a molecular tertiary structure, typically an entry from a structure database.
    """
    Structural_LEFT_PARENTHESIS3DRIGHT_PARENTHESIS_profile_ID = "EDAM_data:1071"
    """
    Identifier or name of a structural (3D) profile or template (representing a structure or structure alignment).
    """
    Structure_alignment_ID = "EDAM_data:1072"
    """
    Identifier of an entry from a database of tertiary structure alignments.
    """
    Amino_acid_index_ID = "EDAM_data:1073"
    """
    Identifier of an index of amino acid physicochemical and biochemical property data.
    """
    Protein_interaction_ID = "EDAM_data:1074"
    """
    Identifier of a report of protein interactions from a protein interaction database (typically).
    """
    Protein_family_identifier = "EDAM_data:1075"
    """
    Identifier of a protein family.
    """
    Codon_usage_table_name = "EDAM_data:1076"
    """
    Unique name of a codon usage table.
    """
    Transcription_factor_identifier = "EDAM_data:1077"
    """
    Identifier of a transcription factor (or a TF binding site).
    """
    Experiment_annotation_ID = "EDAM_data:1078"
    """
    Identifier of an entry from a database of microarray data.
    """
    Electron_microscopy_model_ID = "EDAM_data:1079"
    """
    Identifier of an entry from a database of electron microscopy data.
    """
    Gene_expression_report_ID = "EDAM_data:1080"
    """
    Accession of a report of gene expression (e.g. a gene expression profile) from a database.
    """
    Genotype_and_phenotype_annotation_ID = "EDAM_data:1081"
    """
    Identifier of an entry from a database of genotypes and phenotypes.
    """
    Pathway_or_network_identifier = "EDAM_data:1082"
    """
    Identifier of an entry from a database of biological pathways or networks.
    """
    Workflow_ID = "EDAM_data:1083"
    """
    Identifier of a biological or biomedical workflow, typically from a database of workflows.
    """
    Data_resource_definition_ID = "EDAM_data:1084"
    """
    Identifier of a data type definition from some provider.
    """
    Biological_model_ID = "EDAM_data:1085"
    """
    Identifier of a mathematical model, typically an entry from a database.
    """
    Compound_identifier = "EDAM_data:1086"
    """
    Identifier of an entry from a database of chemicals.
    """
    Ontology_concept_ID = "EDAM_data:1087"
    """
    A unique (typically numerical) identifier of a concept in an ontology of biological or bioinformatics concepts and relations.
    """
    Article_ID = "EDAM_data:1088"
    """
    Unique identifier of a scientific article.
    """
    FlyBase_ID = "EDAM_data:1089"
    """
    Identifier of an object from the FlyBase database.
    """
    WormBase_name = "EDAM_data:1091"
    """
    Name of an object from the WormBase database, usually a human-readable name.
    """
    WormBase_class = "EDAM_data:1092"
    """
    A WormBase class describes the type of object such as 'sequence' or 'protein'.
    Class of an object from the WormBase database.
    """
    Sequence_accession = "EDAM_data:1093"
    """
    A persistent, unique identifier of a molecular sequence database entry.
    """
    EMBOSS_Uniform_Sequence_Address = "EDAM_data:1095"
    """
    The name of a sequence-based entity adhering to the standard sequence naming scheme used by all EMBOSS applications.
    """
    Sequence_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:1096"
    """
    Accession number of a protein sequence database entry.
    """
    Sequence_accession_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "EDAM_data:1097"
    """
    Accession number of a nucleotide sequence database entry.
    """
    RefSeq_accession = "EDAM_data:1098"
    """
    Accession number of a RefSeq database entry.
    """
    PIR_identifier = "EDAM_data:1100"
    """
    An identifier of PIR sequence database entry.
    """
    Gramene_primary_identifier = "EDAM_data:1102"
    """
    Primary identifier of a Gramene database entry.
    """
    EMBLSOLIDUSGenBankSOLIDUSDDBJ_ID = "EDAM_data:1103"
    """
    Identifier of a (nucleic acid) entry from the EMBL/GenBank/DDBJ databases.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniGeneRIGHT_PARENTHESIS = "EDAM_data:1104"
    """
    A unique identifier of an entry (gene cluster) from the NCBI UniGene database.
    """
    dbEST_accession = "EDAM_data:1105"
    """
    Identifier of a dbEST database entry.
    """
    dbSNP_ID = "EDAM_data:1106"
    """
    Identifier of a dbSNP database entry.
    """
    Sequence_cluster_ID = "EDAM_data:1112"
    """
    An identifier of a cluster of molecular sequence(s).
    """
    Sequence_cluster_ID_LEFT_PARENTHESISCOGRIGHT_PARENTHESIS = "EDAM_data:1113"
    """
    Unique identifier of an entry from the COG database.
    """
    Sequence_motif_identifier = "EDAM_data:1114"
    """
    Identifier of a sequence motif, for example an entry from a motif database.
    """
    Sequence_profile_ID = "EDAM_data:1115"
    """
    A sequence profile typically represents a sequence alignment.
    Identifier of a sequence profile.
    """
    ELM_ID = "EDAM_data:1116"
    """
    Identifier of an entry from the ELMdb database of protein functional sites.
    """
    Prosite_accession_number = "EDAM_data:1117"
    """
    Accession number of an entry from the Prosite database.
    """
    HMMER_hidden_Markov_model_ID = "EDAM_data:1118"
    """
    Unique identifier or name of a HMMER hidden Markov model.
    """
    JASPAR_profile_ID = "EDAM_data:1119"
    """
    Unique identifier or name of a profile from the JASPAR database.
    """
    TreeBASE_study_accession_number = "EDAM_data:1123"
    """
    Accession number of an entry from the TreeBASE database.
    """
    TreeFam_accession_number = "EDAM_data:1124"
    """
    Accession number of an entry from the TreeFam database.
    """
    Comparison_matrix_name = "EDAM_data:1126"
    """
    See for example http://www.ebi.ac.uk/Tools/webservices/help/matrix.
    Unique name or identifier of a comparison matrix.
    """
    PDB_ID = "EDAM_data:1127"
    """
    A PDB identification code which consists of 4 characters, the first of which is a digit in the range 0 - 9; the remaining 3 are alphanumeric, and letters are upper case only. (source: https://cdn.rcsb.org/wwpdb/docs/documentation/file-format/PDB_format_1996.pdf)
    An identifier of an entry from the PDB database.
    """
    AAindex_ID = "EDAM_data:1128"
    """
    Identifier of an entry from the AAindex database.
    """
    BIND_accession_number = "EDAM_data:1129"
    """
    Accession number of an entry from the BIND database.
    """
    IntAct_accession_number = "EDAM_data:1130"
    """
    Accession number of an entry from the IntAct database.
    """
    Protein_family_name = "EDAM_data:1131"
    """
    Name of a protein family.
    """
    InterPro_entry_name = "EDAM_data:1132"
    """
    Name of an InterPro entry, usually indicating the type of protein matches for that entry.
    """
    InterPro_accession = "EDAM_data:1133"
    """
    Every InterPro entry has a unique accession number to provide a persistent citation of database records.
    Primary accession number of an InterPro entry.
    """
    InterPro_secondary_accession = "EDAM_data:1134"
    """
    Secondary accession number of an InterPro entry.
    """
    Gene3D_ID = "EDAM_data:1135"
    """
    Unique identifier of an entry from the Gene3D database.
    """
    PIRSF_ID = "EDAM_data:1136"
    """
    Unique identifier of an entry from the PIRSF database.
    """
    PRINTS_code = "EDAM_data:1137"
    """
    The unique identifier of an entry in the PRINTS database.
    """
    Pfam_accession_number = "EDAM_data:1138"
    """
    Accession number of a Pfam entry.
    """
    SMART_accession_number = "EDAM_data:1139"
    """
    Accession number of an entry from the SMART database.
    """
    Superfamily_hidden_Markov_model_number = "EDAM_data:1140"
    """
    Unique identifier (number) of a hidden Markov model from the Superfamily database.
    """
    TIGRFam_ID = "EDAM_data:1141"
    """
    Accession number of an entry (family) from the TIGRFam database.
    """
    ProDom_accession_number = "EDAM_data:1142"
    """
    A ProDom domain family accession number.
    ProDom is a protein domain family database.
    """
    TRANSFAC_accession_number = "EDAM_data:1143"
    """
    Identifier of an entry from the TRANSFAC database.
    """
    ArrayExpress_accession_number = "EDAM_data:1144"
    """
    Accession number of an entry from the ArrayExpress database.
    """
    PRIDE_experiment_accession_number = "EDAM_data:1145"
    """
    PRIDE experiment accession number.
    """
    EMDB_ID = "EDAM_data:1146"
    """
    Identifier of an entry from the EMDB electron microscopy database.
    """
    GEO_accession_number = "EDAM_data:1147"
    """
    Accession number of an entry from the GEO database.
    """
    GermOnline_ID = "EDAM_data:1148"
    """
    Identifier of an entry from the GermOnline database.
    """
    EMAGE_ID = "EDAM_data:1149"
    """
    Identifier of an entry from the EMAGE database.
    """
    Disease_ID = "EDAM_data:1150"
    """
    Accession number of an entry from a database of disease.
    """
    HGVbase_ID = "EDAM_data:1151"
    """
    Identifier of an entry from the HGVbase database.
    """
    OMIM_ID = "EDAM_data:1153"
    """
    Identifier of an entry from the OMIM database.
    """
    KEGG_object_identifier = "EDAM_data:1154"
    """
    Unique identifier of an object from one of the KEGG databases (excluding the GENES division).
    """
    Pathway_ID_LEFT_PARENTHESISreactomeRIGHT_PARENTHESIS = "EDAM_data:1155"
    """
    Identifier of an entry from the Reactome database.
    """
    Pathway_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "EDAM_data:1157"
    """
    Identifier of an pathway from the BioCyc biological pathways database.
    """
    Pathway_ID_LEFT_PARENTHESISINOHRIGHT_PARENTHESIS = "EDAM_data:1158"
    """
    Identifier of an entry from the INOH database.
    """
    Pathway_ID_LEFT_PARENTHESISPATIKARIGHT_PARENTHESIS = "EDAM_data:1159"
    """
    Identifier of an entry from the PATIKA database.
    """
    Pathway_ID_LEFT_PARENTHESISCPDBRIGHT_PARENTHESIS = "EDAM_data:1160"
    """
    Identifier of an entry from the CPDB (ConsensusPathDB) biological pathways database, which is an identifier from an external database integrated into CPDB.
    This concept refers to identifiers used by the databases collated in CPDB; CPDB identifiers are not independently defined.
    """
    Pathway_ID_LEFT_PARENTHESISPantherRIGHT_PARENTHESIS = "EDAM_data:1161"
    """
    Identifier of a biological pathway from the Panther Pathways database.
    """
    MIRIAM_identifier = "EDAM_data:1162"
    """
    This is the identifier used internally by MIRIAM for a data type.
    Unique identifier of a MIRIAM data resource.
    """
    MIRIAM_data_type_name = "EDAM_data:1163"
    """
    The name of a data type from the MIRIAM database.
    """
    MIRIAM_URI = "EDAM_data:1164"
    """
    A MIRIAM URI consists of the URI of the MIRIAM data type (PubMed, UniProt etc) followed by the identifier of an element of that data type, for example PMID for a publication or an accession number for a GO term.
    The URI (URL or URN) of a data entity from the MIRIAM database.
    """
    MIRIAM_data_type_primary_name = "EDAM_data:1165"
    """
    The primary name of a MIRIAM data type is taken from a controlled vocabulary.
    The primary name of a data type from the MIRIAM database.
    """
    MIRIAM_data_type_synonymous_name = "EDAM_data:1166"
    """
    A synonymous name for a MIRIAM data type taken from a controlled vocabulary.
    A synonymous name of a data type from the MIRIAM database.
    """
    Taverna_workflow_ID = "EDAM_data:1167"
    """
    Unique identifier of a Taverna workflow.
    """
    Biological_model_name = "EDAM_data:1170"
    """
    Name of a biological (mathematical) model.
    """
    BioModel_ID = "EDAM_data:1171"
    """
    Unique identifier of an entry from the BioModel database.
    """
    PubChem_CID = "EDAM_data:1172"
    """
    Chemical structure specified in PubChem Compound Identification (CID), a non-zero integer identifier for a unique chemical structure.
    """
    ChemSpider_ID = "EDAM_data:1173"
    """
    Identifier of an entry from the ChemSpider database.
    """
    ChEBI_ID = "EDAM_data:1174"
    """
    Identifier of an entry from the ChEBI database.
    """
    BioPax_concept_ID = "EDAM_data:1175"
    """
    An identifier of a concept from the BioPax ontology.
    """
    GO_concept_ID = "EDAM_data:1176"
    """
    An identifier of a concept from The Gene Ontology.
    """
    MeSH_concept_ID = "EDAM_data:1177"
    """
    An identifier of a concept from the MeSH vocabulary.
    """
    HGNC_concept_ID = "EDAM_data:1178"
    """
    An identifier of a concept from the HGNC controlled vocabulary.
    """
    NCBI_taxonomy_ID = "EDAM_data:1179"
    """
    A stable unique identifier for each taxon (for a species, a family, an order, or any other group in the NCBI taxonomy database.
    """
    Plant_Ontology_concept_ID = "EDAM_data:1180"
    """
    An identifier of a concept from the Plant Ontology (PO).
    """
    UMLS_concept_ID = "EDAM_data:1181"
    """
    An identifier of a concept from the UMLS vocabulary.
    """
    FMA_concept_ID = "EDAM_data:1182"
    """
    An identifier of a concept from Foundational Model of Anatomy.
    Classifies anatomical entities according to their shared characteristics (genus) and distinguishing characteristics (differentia). Specifies the part-whole and spatial relationships of the entities, morphological transformation of the entities during prenatal development and the postnatal life cycle and principles, rules and definitions according to which classes and relationships in the other three components of FMA are represented.
    """
    EMAP_concept_ID = "EDAM_data:1183"
    """
    An identifier of a concept from the EMAP mouse ontology.
    """
    ChEBI_concept_ID = "EDAM_data:1184"
    """
    An identifier of a concept from the ChEBI ontology.
    """
    MGED_concept_ID = "EDAM_data:1185"
    """
    An identifier of a concept from the MGED ontology.
    """
    myGrid_concept_ID = "EDAM_data:1186"
    """
    An identifier of a concept from the myGrid ontology.
    The ontology is provided as two components, the service ontology and the domain ontology. The domain ontology acts provides concepts for core bioinformatics data types and their relations. The service ontology describes the physical and operational features of web services.
    """
    PubMed_ID = "EDAM_data:1187"
    """
    PubMed unique identifier of an article.
    """
    DOI = "EDAM_data:1188"
    """
    Digital Object Identifier (DOI) of a published article.
    """
    Medline_UI = "EDAM_data:1189"
    """
    Medline UI (unique identifier) of an article.
    The use of Medline UI has been replaced by the PubMed unique identifier.
    """
    Tool_name = "EDAM_data:1190"
    """
    The name of a computer package, application, method or function.
    """
    Tool_name_LEFT_PARENTHESISsignatureRIGHT_PARENTHESIS = "EDAM_data:1191"
    """
    Signature methods from http://www.ebi.ac.uk/Tools/InterProScan/help.html#results include BlastProDom, FPrintScan, HMMPIR, HMMPfam, HMMSmart, HMMTigr, ProfileScan, ScanRegExp, SuperFamily and HAMAP.
    The unique name of a signature (sequence classifier) method.
    """
    Tool_name_LEFT_PARENTHESISBLASTRIGHT_PARENTHESIS = "EDAM_data:1192"
    """
    The name of a BLAST tool.
    This include 'blastn', 'blastp', 'blastx', 'tblastn' and 'tblastx'.
    """
    Tool_name_LEFT_PARENTHESISFASTARIGHT_PARENTHESIS = "EDAM_data:1193"
    """
    The name of a FASTA tool.
    This includes 'fasta3', 'fastx3', 'fasty3', 'fastf3', 'fasts3' and 'ssearch'.
    """
    Tool_name_LEFT_PARENTHESISEMBOSSRIGHT_PARENTHESIS = "EDAM_data:1194"
    """
    The name of an EMBOSS application.
    """
    Tool_name_LEFT_PARENTHESISEMBASSY_packageRIGHT_PARENTHESIS = "EDAM_data:1195"
    """
    The name of an EMBASSY package.
    """
    QSAR_descriptor_LEFT_PARENTHESISconstitutionalRIGHT_PARENTHESIS = "EDAM_data:1201"
    """
    A QSAR constitutional descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISelectronicRIGHT_PARENTHESIS = "EDAM_data:1202"
    """
    A QSAR electronic descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISgeometricalRIGHT_PARENTHESIS = "EDAM_data:1203"
    """
    A QSAR geometrical descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESIStopologicalRIGHT_PARENTHESIS = "EDAM_data:1204"
    """
    A QSAR topological descriptor.
    """
    QSAR_descriptor_LEFT_PARENTHESISmolecularRIGHT_PARENTHESIS = "EDAM_data:1205"
    """
    A QSAR molecular descriptor.
    """
    Sequence_set_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:1233"
    """
    Any collection of multiple protein sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.
    """
    Sequence_set_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "EDAM_data:1234"
    """
    Any collection of multiple nucleotide sequences and associated metadata that do not (typically) correspond to common sequence database records or database entries.
    """
    Sequence_cluster = "EDAM_data:1235"
    """
    A set of sequences that have been clustered or otherwise classified as belonging to a group including (typically) sequence cluster information.
    The cluster might include sequences identifiers, short descriptions, alignment and summary information.
    """
    Proteolytic_digest = "EDAM_data:1238"
    """
    A protein sequence cleaved into peptide fragments (by enzymatic or chemical cleavage) with fragment masses.
    """
    Restriction_digest = "EDAM_data:1239"
    """
    Restriction digest fragments from digesting a nucleotide sequence with restriction sites using a restriction endonuclease.
    """
    PCR_primers = "EDAM_data:1240"
    """
    Oligonucleotide primer(s) for PCR and DNA amplification, for example a minimal primer set.
    """
    Sequence_cluster_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:1245"
    """
    A cluster of protein sequences.
    The sequences are typically related, for example a family of sequences.
    """
    Sequence_cluster_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "EDAM_data:1246"
    """
    A cluster of nucleotide sequences.
    The sequences are typically related, for example a family of sequences.
    """
    Sequence_length = "EDAM_data:1249"
    """
    The size (length) of a sequence, subsequence or region in a sequence, or range(s) of lengths.
    """
    Sequence_property = "EDAM_data:1254"
    """
    An informative report about non-positional sequence features, typically a report on general molecular sequence properties derived from sequence analysis.
    """
    Sequence_features = "EDAM_data:1255"
    """
    Annotation of positional features of molecular sequence(s), i.e. that can be mapped to position(s) in the sequence.
    This includes annotation of positional sequence features, organised into a standard feature table, or any other report of sequence features. General feature reports are a source of sequence feature table information although internal conversion would be required.
    """
    Sequence_complexity_report = "EDAM_data:1259"
    """
    A report on sequence complexity, for example low-complexity or repeat regions in sequences.
    """
    Sequence_ambiguity_report = "EDAM_data:1260"
    """
    A report on ambiguity in molecular sequence(s).
    """
    Sequence_composition_report = "EDAM_data:1261"
    """
    A report (typically a table) on character or word composition / frequency of a molecular sequence(s).
    """
    Peptide_molecular_weight_hits = "EDAM_data:1262"
    """
    A report on peptide fragments of certain molecular weight(s) in one or more protein sequences.
    """
    Base_position_variability_plot = "EDAM_data:1263"
    """
    A plot of third base position variability in a nucleotide sequence.
    """
    Base_frequencies_table = "EDAM_data:1265"
    """
    A table of base frequencies of a nucleotide sequence.
    """
    Base_word_frequencies_table = "EDAM_data:1266"
    """
    A table of word composition of a nucleotide sequence.
    """
    Amino_acid_frequencies_table = "EDAM_data:1267"
    """
    A table of amino acid frequencies of a protein sequence.
    """
    Amino_acid_word_frequencies_table = "EDAM_data:1268"
    """
    A table of amino acid word composition of a protein sequence.
    """
    Feature_table = "EDAM_data:1270"
    """
    Annotation of positional sequence features, organised into a standard feature table.
    """
    Map = "EDAM_data:1274"
    """
    A map of (typically one) DNA sequence annotated with positional or non-positional features.
    """
    Nucleic_acid_features = "EDAM_data:1276"
    """
    An informative report on intrinsic positional features of a nucleotide sequence, formatted to be machine-readable.
    This includes nucleotide sequence feature annotation in any known sequence feature table format and any other report of nucleic acid features.
    """
    Protein_features = "EDAM_data:1277"
    """
    An informative report on intrinsic positional features of a protein sequence.
    This includes protein sequence feature annotation in any known sequence feature table format and any other report of protein features.
    """
    Genetic_map = "EDAM_data:1278"
    """
    A genetic (linkage) map indicates the proximity of two genes on a chromosome, whether two genes are linked and the frequency they are transmitted together to an offspring. They are limited to genetic markers of traits observable only in whole organisms.
    A map showing the relative positions of genetic markers in a nucleic acid sequence, based on estimation of non-physical distance such as recombination frequencies.
    """
    Sequence_map = "EDAM_data:1279"
    """
    A map of genetic markers in a contiguous, assembled genomic sequence, with the sizes and separation of markers measured in base pairs.
    A sequence map typically includes annotation on significant subsequences such as contigs, haplotypes and genes. The contigs shown will (typically) be a set of small overlapping clones representing a complete chromosomal segment.
    """
    Physical_map = "EDAM_data:1280"
    """
    A map of DNA (linear or circular) annotated with physical features or landmarks such as restriction sites, cloned DNA fragments, genes or genetic markers, along with the physical distances between them.
    Distance in a physical map is measured in base pairs. A physical map might be ordered relative to a reference map (typically a genetic map) in the process of genome sequencing.
    """
    Cytogenetic_map = "EDAM_data:1283"
    """
    A map showing banding patterns derived from direct observation of a stained chromosome.
    This is the lowest-resolution physical map and can provide only rough estimates of physical (base pair) distances. Like a genetic map, they are limited to genetic markers of traits observable only in whole organisms.
    """
    DNA_transduction_map = "EDAM_data:1284"
    """
    A gene map showing distances between loci based on relative cotransduction frequencies.
    """
    Gene_map = "EDAM_data:1285"
    """
    Sequence map of a single gene annotated with genetic features such as introns, exons, untranslated regions, polyA signals, promoters, enhancers and (possibly) mutations defining alleles of a gene.
    """
    Plasmid_map = "EDAM_data:1286"
    """
    Sequence map of a plasmid (circular DNA).
    """
    Genome_map = "EDAM_data:1288"
    """
    Sequence map of a whole genome.
    """
    Restriction_map = "EDAM_data:1289"
    """
    Image of the restriction enzyme cleavage sites (restriction sites) in a nucleic acid sequence.
    """
    Dirichlet_distribution = "EDAM_data:1347"
    """
    Dirichlet distribution used by hidden Markov model analysis programs.
    """
    Regular_expression = "EDAM_data:1352"
    """
    Regular expression pattern.
    """
    Sequence_motif = "EDAM_data:1353"
    """
    Any specific or conserved pattern (typically expressed as a regular expression) in a molecular sequence.
    """
    Sequence_profile = "EDAM_data:1354"
    """
    Some type of statistical model representing a (typically multiple) sequence alignment.
    """
    Protein_signature = "EDAM_data:1355"
    """
    An informative report about a specific or conserved protein sequence pattern.
    """
    Position_frequency_matrix = "EDAM_data:1361"
    """
    A profile (typically representing a sequence alignment) that is a simple matrix of nucleotide (or amino acid) counts per position.
    """
    Position_weight_matrix = "EDAM_data:1362"
    """
    A profile (typically representing a sequence alignment) that is weighted matrix of nucleotide (or amino acid) counts per position.
    Contributions of individual sequences to the matrix might be uneven (weighted).
    """
    Information_content_matrix = "EDAM_data:1363"
    """
    A profile (typically representing a sequence alignment) derived from a matrix of nucleotide (or amino acid) counts per position that reflects information content at each position.
    """
    Hidden_Markov_model = "EDAM_data:1364"
    """
    A statistical Markov model of a system which is assumed to be a Markov process with unobserved (hidden) states. For example, a hidden Markov model representation of a set or alignment of sequences.
    """
    Fingerprint = "EDAM_data:1365"
    """
    One or more fingerprints (sequence classifiers) as used in the PRINTS database.
    """
    Pair_sequence_alignment = "EDAM_data:1381"
    """
    Alignment of exactly two molecular sequences.
    """
    Nucleic_acid_sequence_alignment = "EDAM_data:1383"
    """
    Alignment of multiple nucleotide sequences.
    """
    Protein_sequence_alignment = "EDAM_data:1384"
    """
    Alignment of multiple protein sequences.
    """
    Hybrid_sequence_alignment = "EDAM_data:1385"
    """
    Alignment of multiple molecular sequences of different types.
    Hybrid sequence alignments include for example genomic DNA to EST, cDNA or mRNA.
    """
    Alignment_score_or_penalty = "EDAM_data:1394"
    """
    A simple floating point number defining the penalty for opening or extending a gap in an alignment.
    """
    Gap_opening_penalty = "EDAM_data:1397"
    """
    A penalty for opening a gap in an alignment.
    """
    Gap_extension_penalty = "EDAM_data:1398"
    """
    A penalty for extending a gap in an alignment.
    """
    Gap_separation_penalty = "EDAM_data:1399"
    """
    A penalty for gaps that are close together in an alignment.
    """
    Match_reward_score = "EDAM_data:1401"
    """
    The score for a 'match' used in various sequence database search applications with simple scoring schemes.
    """
    Mismatch_penalty_score = "EDAM_data:1402"
    """
    The score (penalty) for a 'mismatch' used in various alignment and sequence database search applications with simple scoring schemes.
    """
    Drop_off_score = "EDAM_data:1403"
    """
    This is the threshold drop in score at which extension of word alignment is halted.
    """
    Terminal_gap_opening_penalty = "EDAM_data:1410"
    """
    A number defining the penalty for opening gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.
    """
    Terminal_gap_extension_penalty = "EDAM_data:1411"
    """
    A number defining the penalty for extending gaps at the termini of an alignment, either from the N/C terminal of protein or 5'/3' terminal of nucleotide sequences.
    """
    Sequence_identity = "EDAM_data:1412"
    """
    Sequence identity is the number (%) of matches (identical characters) in positions from an alignment of two molecular sequences.
    """
    Sequence_similarity = "EDAM_data:1413"
    """
    Data Type is float probably.
    Sequence similarity is the similarity (expressed as a percentage) of two molecular sequences calculated from their alignment, a scoring matrix for scoring characters substitutions and penalties for gap insertion and extension.
    """
    Phylogenetic_continuous_quantitative_data = "EDAM_data:1426"
    """
    Continuous quantitative data that may be read during phylogenetic tree calculation.
    """
    Phylogenetic_discrete_data = "EDAM_data:1427"
    """
    Character data with discrete states that may be read during phylogenetic tree calculation.
    """
    Phylogenetic_character_cliques = "EDAM_data:1428"
    """
    One or more cliques of mutually compatible characters that are generated, for example from analysis of discrete character data, and are used to generate a phylogeny.
    """
    Phylogenetic_invariants = "EDAM_data:1429"
    """
    Phylogenetic invariants data for testing alternative tree topologies.
    """
    DNA_substitution_model = "EDAM_data:1439"
    """
    A model of DNA substitution that explains a DNA sequence alignment, derived from phylogenetic tree analysis.
    """
    Phylogenetic_tree_distances = "EDAM_data:1442"
    """
    Distances, such as Branch Score distance, between two or more phylogenetic trees.
    """
    Phylogenetic_character_contrasts = "EDAM_data:1444"
    """
    Independent contrasts for characters used in a phylogenetic tree, or covariances, regressions and correlations between characters for those contrasts.
    """
    Comparison_matrix_LEFT_PARENTHESISnucleotideRIGHT_PARENTHESIS = "EDAM_data:1448"
    """
    Matrix of integer or floating point numbers for nucleotide comparison.
    """
    Comparison_matrix_LEFT_PARENTHESISamino_acidRIGHT_PARENTHESIS = "EDAM_data:1449"
    """
    Matrix of integer or floating point numbers for amino acid comparison.
    """
    Nucleic_acid_structure = "EDAM_data:1459"
    """
    3D coordinate and associated data for a nucleic acid tertiary (3D) structure.
    """
    Protein_structure = "EDAM_data:1460"
    """
    3D coordinate and associated data for a protein tertiary (3D) structure, or part of a structure, possibly in complex with other molecules.
    """
    Protein_ligand_complex = "EDAM_data:1461"
    """
    The structure of a protein in complex with a ligand, typically a small molecule such as an enzyme substrate or cofactor, but possibly another macromolecule.
    This includes interactions of proteins with atoms, ions and small molecules or macromolecules such as nucleic acids or other polypeptides. For stable inter-polypeptide interactions use 'Protein complex' instead.
    """
    Carbohydrate_structure = "EDAM_data:1462"
    """
    3D coordinate and associated data for a carbohydrate (3D) structure.
    """
    Small_molecule_structure = "EDAM_data:1463"
    """
    3D coordinate and associated data for the (3D) structure of a small molecule, such as any common chemical compound.
    """
    DNA_structure = "EDAM_data:1464"
    """
    3D coordinate and associated data for a DNA tertiary (3D) structure.
    """
    RNA_structure = "EDAM_data:1465"
    """
    3D coordinate and associated data for an RNA tertiary (3D) structure.
    """
    tRNA_structure = "EDAM_data:1466"
    """
    3D coordinate and associated data for a tRNA tertiary (3D) structure, including tmRNA, snoRNAs etc.
    """
    Protein_chain = "EDAM_data:1467"
    """
    3D coordinate and associated data for the tertiary (3D) structure of a polypeptide chain.
    """
    Protein_domain = "EDAM_data:1468"
    """
    3D coordinate and associated data for the tertiary (3D) structure of a protein domain.
    """
    C_alpha_trace = "EDAM_data:1470"
    """
    3D coordinate and associated data for a protein tertiary (3D) structure (typically C-alpha atoms only).
    C-beta atoms from amino acid side-chains may be included.
    """
    Structure_alignment_LEFT_PARENTHESISpairRIGHT_PARENTHESIS = "EDAM_data:1479"
    """
    Alignment (superimposition) of exactly two molecular tertiary (3D) structures.
    """
    Protein_structure_alignment = "EDAM_data:1481"
    """
    Alignment (superimposition) of protein tertiary (3D) structures.
    """
    Nucleic_acid_structure_alignment = "EDAM_data:1482"
    """
    Alignment (superimposition) of nucleic acid tertiary (3D) structures.
    """
    RNA_structure_alignment = "EDAM_data:1493"
    """
    Alignment (superimposition) of RNA tertiary (3D) structures.
    """
    Structural_transformation_matrix = "EDAM_data:1494"
    """
    Matrix to transform (rotate/translate) 3D coordinates, typically the transformation necessary to superimpose two molecular structures.
    """
    Root_mean_square_deviation = "EDAM_data:1497"
    """
    Root-mean-square deviation (RMSD) is calculated to measure the average distance between superimposed macromolecular coordinates.
    """
    Tanimoto_similarity_score = "EDAM_data:1498"
    """
    A ligand fingerprint is derived from ligand structural data from a Protein DataBank file. It reflects the elements or groups present or absent, covalent bonds and bond orders and the bonded environment in terms of SATIS codes and BLEEP atom types.
    A measure of the similarity between two ligand fingerprints.
    """
    number_3D_1D_scoring_matrix = "EDAM_data:1499"
    """
    A matrix of 3D-1D scores reflecting the probability of amino acids to occur in different tertiary structural environments.
    """
    Amino_acid_index = "EDAM_data:1501"
    """
    A table of 20 numerical values which quantify a property (e.g. physicochemical or biochemical) of the common amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISchemical_classesRIGHT_PARENTHESIS = "EDAM_data:1502"
    """
    Chemical classification (small, aliphatic, aromatic, polar, charged etc) of amino acids.
    """
    Amino_acid_pair_wise_contact_potentials = "EDAM_data:1503"
    """
    Statistical protein contact potentials.
    """
    Amino_acid_index_LEFT_PARENTHESISmolecular_weightRIGHT_PARENTHESIS = "EDAM_data:1505"
    """
    Molecular weights of amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESIShydropathyRIGHT_PARENTHESIS = "EDAM_data:1506"
    """
    Hydrophobic, hydrophilic or charge properties of amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISWhite_Wimley_dataRIGHT_PARENTHESIS = "EDAM_data:1507"
    """
    Experimental free energy values for the water-interface and water-octanol transitions for the amino acids.
    """
    Amino_acid_index_LEFT_PARENTHESISvan_der_Waals_radiiRIGHT_PARENTHESIS = "EDAM_data:1508"
    """
    Van der Waals radii of atoms for different amino acid residues.
    """
    Peptide_molecular_weights = "EDAM_data:1519"
    """
    List of molecular weight(s) of one or more proteins or peptides, for example cut by proteolytic enzymes or reagents.
    The report might include associated data such as frequency of peptide fragment molecular weights.
    """
    Peptide_hydrophobic_moment = "EDAM_data:1520"
    """
    Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation.
    Report on the hydrophobic moment of a polypeptide sequence.
    """
    Protein_aliphatic_index = "EDAM_data:1521"
    """
    The aliphatic index is the relative protein volume occupied by aliphatic side chains.
    The aliphatic index of a protein.
    """
    Protein_sequence_hydropathy_plot = "EDAM_data:1522"
    """
    A protein sequence with annotation on hydrophobic or hydrophilic / charged regions, hydrophobicity plot etc.
    Hydrophobic moment is a peptides hydrophobicity measured for different angles of rotation.
    """
    Protein_charge_plot = "EDAM_data:1523"
    """
    A plot of the mean charge of the amino acids within a window of specified length as the window is moved along a protein sequence.
    """
    Protein_solubility = "EDAM_data:1524"
    """
    The solubility or atomic solvation energy of a protein sequence or structure.
    """
    Protein_crystallizability = "EDAM_data:1525"
    """
    Data on the crystallizability of a protein sequence.
    """
    Protein_globularity = "EDAM_data:1526"
    """
    Data on the stability, intrinsic disorder or globularity of a protein sequence.
    """
    Protein_titration_curve = "EDAM_data:1527"
    """
    The titration curve of a protein.
    """
    Protein_isoelectric_point = "EDAM_data:1528"
    """
    The isoelectric point of one proteins.
    """
    Protein_pKa_value = "EDAM_data:1529"
    """
    The pKa value of a protein.
    """
    Protein_hydrogen_exchange_rate = "EDAM_data:1530"
    """
    The hydrogen exchange rate of a protein.
    """
    Protein_extinction_coefficient = "EDAM_data:1531"
    """
    The extinction coefficient of a protein.
    """
    Protein_optical_density = "EDAM_data:1532"
    """
    The optical density of a protein.
    """
    Peptide_immunogenicity_data = "EDAM_data:1534"
    """
    An report on allergenicity / immunogenicity of peptides and proteins.
    This includes data on peptide ligands that elicit an immune response (immunogens), allergic cross-reactivity, predicted antigenicity (Hopp and Woods plot) etc. These data are useful in the development of peptide-specific antibodies or multi-epitope vaccines. Methods might use sequence data (for example motifs) and / or structural data.
    """
    Protein_structure_report = "EDAM_data:1537"
    """
    A human-readable collection of information about one or more specific protein 3D structure(s) or structural domains.
    """
    Protein_structural_quality_report = "EDAM_data:1539"
    """
    Model validation might involve checks for atomic packing, steric clashes, agreement with electron density maps etc.
    Report on the quality of a protein three-dimensional model.
    """
    Protein_solvent_accessibility = "EDAM_data:1542"
    """
    Data on the solvent accessible or buried surface area of a protein structure.
    This concept covers definitions of the protein surface, interior and interfaces, accessible and buried residues, surface accessible pockets, interior inaccessible cavities etc.
    """
    Ramachandran_plot = "EDAM_data:1544"
    """
    Phi/psi angle data or a Ramachandran plot of a protein structure.
    """
    Protein_dipole_moment = "EDAM_data:1545"
    """
    Data on the net charge distribution (dipole moment) of a protein structure.
    """
    Protein_distance_matrix = "EDAM_data:1546"
    """
    A matrix of distances between amino acid residues (for example the C-alpha atoms) in a protein structure.
    """
    Protein_contact_map = "EDAM_data:1547"
    """
    An amino acid residue contact map for a protein structure.
    """
    Protein_residue_3D_cluster = "EDAM_data:1548"
    """
    Report on clusters of contacting residues in protein structures such as a key structural residue network.
    """
    Protein_hydrogen_bonds = "EDAM_data:1549"
    """
    Patterns of hydrogen bonding in protein structures.
    """
    Protein_ligand_interaction_report = "EDAM_data:1566"
    """
    An informative report on protein-ligand (small molecule) interaction(s).
    """
    Nucleic_acid_melting_profile = "EDAM_data:1583"
    """
    A melting (stability) profile calculated the free energy required to unwind and separate the nucleic acid strands, plotted for sliding windows over a sequence.
    Data on the dissociation characteristics of a double-stranded nucleic acid molecule (DNA or a DNA/RNA hybrid) during heating.
    Nucleic acid melting curve: a melting curve of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the proportion of nucleic acid which are double-stranded versus temperature.
    Nucleic acid probability profile: a probability profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Shows the probability of a base pair not being melted (i.e. remaining as double-stranded DNA) at a specified temperature
    Nucleic acid stitch profile: stitch profile of hybridised or double stranded nucleic acid (DNA or RNA/DNA). A stitch profile diagram shows partly melted DNA conformations (with probabilities) at a range of temperatures. For example, a stitch profile might show possible loop openings with their location, size, probability and fluctuations at a given temperature.
    Nucleic acid temperature profile: a temperature profile of a double-stranded nucleic acid molecule (DNA or DNA/RNA). Plots melting temperature versus base position.
    """
    Nucleic_acid_enthalpy = "EDAM_data:1584"
    """
    Enthalpy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).
    """
    Nucleic_acid_entropy = "EDAM_data:1585"
    """
    Entropy of hybridised or double stranded nucleic acid (DNA or RNA/DNA).
    """
    DNA_base_pair_stacking_energies_data = "EDAM_data:1588"
    """
    DNA base pair stacking energies data.
    """
    DNA_base_pair_twist_angle_data = "EDAM_data:1589"
    """
    DNA base pair twist angle data.
    """
    DNA_base_trimer_roll_angles_data = "EDAM_data:1590"
    """
    DNA base trimer roll angles data.
    """
    Base_pairing_probability_matrix_dotplot = "EDAM_data:1595"
    """
    Dotplot of RNA base pairing probability matrix.
    Such as generated by the Vienna package.
    """
    Nucleic_acid_folding_report = "EDAM_data:1596"
    """
    A human-readable collection of information about RNA/DNA folding, minimum folding energies for DNA or RNA sequences, energy landscape of RNA mutants etc.
    """
    Codon_usage_table = "EDAM_data:1597"
    """
    A codon usage table might include the codon usage table name, optional comments and a table with columns for codons and corresponding codon usage data. A genetic code can be extracted from or represented by a codon usage table.
    Table of codon usage data calculated from one or more nucleic acid sequences.
    """
    Genetic_code = "EDAM_data:1598"
    """
    A genetic code for an organism.
    A genetic code need not include detailed codon usage information.
    """
    Codon_usage_bias_plot = "EDAM_data:1600"
    """
    A plot of the synonymous codon usage calculated for windows over a nucleotide sequence.
    """
    Codon_usage_fraction_difference = "EDAM_data:1602"
    """
    The differences in codon usage fractions between two codon usage tables.
    """
    Pharmacogenomic_test_report = "EDAM_data:1621"
    """
    A human-readable collection of information about the influence of genotype on drug response.
    The report might correlate gene expression or single-nucleotide polymorphisms with drug efficacy or toxicity.
    """
    Disease_report = "EDAM_data:1622"
    """
    A human-readable collection of information about a specific disease.
    For example, an informative report on a specific tumor including nature and origin of the sample, anatomic site, organ or tissue, tumor type, including morphology and/or histologic type, and so on.
    """
    Heat_map = "EDAM_data:1636"
    """
    A graphical 2D tabular representation of expression data, typically derived from an omics experiment. A heat map is a table where rows and columns correspond to different features and contexts (for example, cells or samples) and the cell colour represents the level of expression of a gene that context.
    """
    E_value = "EDAM_data:1667"
    """
    A simple floating point number defining the lower or upper limit of an expectation value (E-value).
    An expectation value (E-Value) is the expected number of observations which are at least as extreme as observations expected to occur by random chance. The E-value describes the number of hits with a given score or better that are expected to occur at random when searching a database of a particular size. It decreases exponentially with the score (S) of a hit. A low E value indicates a more significant score.
    """
    Z_value = "EDAM_data:1668"
    """
    A z-value might be specified as a threshold for reporting hits from database searches.
    The z-value is the number of standard deviations a data value is above or below a mean value.
    """
    P_value = "EDAM_data:1669"
    """
    A z-value might be specified as a threshold for reporting hits from database searches.
    The P-value is the probability of obtaining by random chance a result that is at least as extreme as an observed result, assuming a NULL hypothesis is true.
    """
    Username = "EDAM_data:1689"
    """
    A username on a computer system or a website.
    """
    Password = "EDAM_data:1690"
    """
    A password on a computer system, or a website.
    """
    Email_address = "EDAM_data:1691"
    """
    A valid email address of an end-user.
    """
    Person_name = "EDAM_data:1692"
    """
    The name of a person.
    """
    Drug_report = "EDAM_data:1696"
    """
    A drug structure relationship map is report (typically a map diagram) of drug structure relationships.
    A human-readable collection of information about a specific drug.
    """
    Phylogenetic_tree_image = "EDAM_data:1707"
    """
    An image (for viewing or printing) of a phylogenetic tree including (typically) a plot of rooted or unrooted phylogenies, cladograms, circular trees or phenograms and associated information.
    See also 'Phylogenetic tree'
    """
    RNA_secondary_structure_image = "EDAM_data:1708"
    """
    Image of RNA secondary structure, knots, pseudoknots etc.
    """
    Protein_secondary_structure_image = "EDAM_data:1709"
    """
    Image of protein secondary structure.
    """
    Structure_image = "EDAM_data:1710"
    """
    Image of one or more molecular tertiary (3D) structures.
    """
    Sequence_alignment_image = "EDAM_data:1711"
    """
    Image of two or more aligned molecular sequences possibly annotated with alignment features.
    """
    Chemical_structure_image = "EDAM_data:1712"
    """
    An image of the structure of a small chemical compound.
    The molecular identifier and formula are typically included.
    """
    Fate_map = "EDAM_data:1713"
    """
    A fate map is a plan of early stage of an embryo such as a blastula, showing areas that are significance to development.
    """
    Microarray_spots_image = "EDAM_data:1714"
    """
    An image of spots from a microarray experiment.
    """
    Ontology_concept_definition = "EDAM_data:1731"
    """
    The definition of a concept from an ontology.
    """
    PDB_residue_number = "EDAM_data:1742"
    """
    A residue identifier (a string) from a PDB file.
    """
    Atomic_coordinate = "EDAM_data:1743"
    """
    Cartesian coordinate of an atom (in a molecular structure).
    """
    PDB_atom_name = "EDAM_data:1748"
    """
    Identifier (a string) of a specific atom from a PDB file for a molecular structure.
    """
    Protein_atom = "EDAM_data:1755"
    """
    Data on a single atom from a protein structure.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.
    """
    Protein_residue = "EDAM_data:1756"
    """
    Data on a single amino acid residue position in a protein structure.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.
    """
    Atom_name = "EDAM_data:1757"
    """
    Name of an atom.
    """
    PDB_residue_name = "EDAM_data:1758"
    """
    Three-letter amino acid residue names as used in PDB files.
    """
    PDB_model_number = "EDAM_data:1759"
    """
    Identifier of a model structure from a PDB file.
    """
    Sequence_version = "EDAM_data:1771"
    """
    Information on an molecular sequence version.
    """
    Score = "EDAM_data:1772"
    """
    A numerical value, that is some type of scored value arising for example from a prediction method.
    """
    Gene_ID_LEFT_PARENTHESISPlasmoDBRIGHT_PARENTHESIS = "EDAM_data:1794"
    """
    Identifier of a gene from PlasmoDB Plasmodium Genome Resource.
    """
    Gene_ID_LEFT_PARENTHESISEcoGeneRIGHT_PARENTHESIS = "EDAM_data:1795"
    """
    Identifier of a gene from EcoGene Database.
    """
    Gene_ID_LEFT_PARENTHESISFlyBaseRIGHT_PARENTHESIS = "EDAM_data:1796"
    """
    Gene identifier from FlyBase database.
    """
    Gene_ID_LEFT_PARENTHESISGrameneRIGHT_PARENTHESIS = "EDAM_data:1802"
    """
    Gene identifier from Gramene database.
    """
    Gene_ID_LEFT_PARENTHESISVirginia_microbialRIGHT_PARENTHESIS = "EDAM_data:1803"
    """
    Gene identifier from Virginia Bioinformatics Institute microbial database.
    """
    Gene_ID_LEFT_PARENTHESISSGNRIGHT_PARENTHESIS = "EDAM_data:1804"
    """
    Gene identifier from Sol Genomics Network.
    """
    Gene_ID_LEFT_PARENTHESISWormBaseRIGHT_PARENTHESIS = "EDAM_data:1805"
    """
    Gene identifier used by WormBase database.
    """
    ORF_name = "EDAM_data:1807"
    """
    The name of an open reading frame attributed by a sequencing project.
    """
    Clone_ID = "EDAM_data:1855"
    """
    An identifier of a clone (cloned molecular sequence) from a database.
    """
    PDB_insertion_code = "EDAM_data:1856"
    """
    An insertion code (part of the residue number) for an amino acid residue from a PDB file.
    """
    Atomic_occupancy = "EDAM_data:1857"
    """
    The fraction of an atom type present at a site in a molecular structure.
    The sum of the occupancies of all the atom types at a site should not normally significantly exceed 1.0.
    """
    Isotropic_B_factor = "EDAM_data:1858"
    """
    Isotropic B factor (atomic displacement parameter) for an atom from a PDB file.
    """
    Deletion_map = "EDAM_data:1859"
    """
    A cytogenetic map is built from a set of mutant cell lines with sub-chromosomal deletions and a reference wild-type line ('genome deletion panel'). The panel is used to map markers onto the genome by comparing mutant to wild-type banding patterns. Markers are linked (occur in the same deleted region) if they share the same banding pattern (presence or absence) as the deletion panel.
    A cytogenetic map showing chromosome banding patterns in mutant cell lines relative to the wild type.
    """
    QTL_map = "EDAM_data:1860"
    """
    A genetic map which shows the approximate location of quantitative trait loci (QTL) between two or more markers.
    """
    Haplotype_map = "EDAM_data:1863"
    """
    A map of haplotypes in a genome or other sequence, describing common patterns of genetic variation.
    """
    Protein_fold_name = "EDAM_data:1867"
    """
    The name of a protein fold.
    """
    Taxon = "EDAM_data:1868"
    """
    For a complete list of taxonomic ranks see https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary.
    The name of a group of organisms belonging to the same taxonomic rank.
    """
    Organism_identifier = "EDAM_data:1869"
    """
    A unique identifier of a (group of) organisms.
    """
    Genus_name = "EDAM_data:1870"
    """
    The name of a genus of organism.
    """
    Taxonomic_classification = "EDAM_data:1872"
    """
    Name components correspond to levels in a taxonomic hierarchy (e.g. 'Genus', 'Species', etc.) Meta information such as a reference where the name was defined and a date might be included.
    The full name for a group of organisms, reflecting their biological classification and (usually) conforming to a standard nomenclature.
    """
    iHOP_organism_ID = "EDAM_data:1873"
    """
    A unique identifier for an organism used in the iHOP database.
    """
    Genbank_common_name = "EDAM_data:1874"
    """
    Common name for an organism as used in the GenBank database.
    """
    NCBI_taxon = "EDAM_data:1875"
    """
    The name of a taxon from the NCBI taxonomy database.
    """
    Author_ID = "EDAM_data:1881"
    """
    Information on the authors of a published work.
    """
    DragonDB_author_identifier = "EDAM_data:1882"
    """
    An identifier representing an author in the DragonDB database.
    """
    Annotated_URI = "EDAM_data:1883"
    """
    A URI along with annotation describing the data found at the address.
    """
    Gene_ID_LEFT_PARENTHESISGeneFarmRIGHT_PARENTHESIS = "EDAM_data:1885"
    """
    Identifier of a gene from the GeneFarm database.
    """
    Blattner_number = "EDAM_data:1886"
    """
    The blattner identifier for a gene.
    """
    iHOP_symbol = "EDAM_data:1891"
    """
    A unique identifier of a protein or gene used in the iHOP database.
    """
    Locus_ID = "EDAM_data:1893"
    """
    A unique name or other identifier of a genetic locus, typically conforming to a scheme that names loci (such as predicted genes) depending on their position in a molecular sequence, for example a completely sequenced genome or chromosome.
    """
    Locus_ID_LEFT_PARENTHESISAGIRIGHT_PARENTHESIS = "EDAM_data:1895"
    """
    Locus identifier for Arabidopsis Genome Initiative (TAIR, TIGR and MIPS databases).
    """
    Locus_ID_LEFT_PARENTHESISASPGDRIGHT_PARENTHESIS = "EDAM_data:1896"
    """
    Identifier for loci from ASPGD (Aspergillus Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISMGGRIGHT_PARENTHESIS = "EDAM_data:1897"
    """
    Identifier for loci from Magnaporthe grisea Database at the Broad Institute.
    """
    Locus_ID_LEFT_PARENTHESISCGDRIGHT_PARENTHESIS = "EDAM_data:1898"
    """
    Identifier for loci from CGD (Candida Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISCMRRIGHT_PARENTHESIS = "EDAM_data:1899"
    """
    Locus identifier for Comprehensive Microbial Resource at the J. Craig Venter Institute.
    """
    NCBI_locus_tag = "EDAM_data:1900"
    """
    Identifier for loci from NCBI database.
    """
    Locus_ID_LEFT_PARENTHESISSGDRIGHT_PARENTHESIS = "EDAM_data:1901"
    """
    Identifier for loci from SGD (Saccharomyces Genome Database).
    """
    Locus_ID_LEFT_PARENTHESISMMPRIGHT_PARENTHESIS = "EDAM_data:1902"
    """
    Identifier of loci from Maize Mapping Project.
    """
    Locus_ID_LEFT_PARENTHESISDictyBaseRIGHT_PARENTHESIS = "EDAM_data:1903"
    """
    Identifier of locus from DictyBase (Dictyostelium discoideum).
    """
    Locus_ID_LEFT_PARENTHESISEntrezGeneRIGHT_PARENTHESIS = "EDAM_data:1904"
    """
    Identifier of a locus from EntrezGene database.
    """
    Locus_ID_LEFT_PARENTHESISMaizeGDBRIGHT_PARENTHESIS = "EDAM_data:1905"
    """
    Identifier of locus from MaizeGDB (Maize genome database).
    """
    Gene_ID_LEFT_PARENTHESISKOMERIGHT_PARENTHESIS = "EDAM_data:1907"
    """
    Identifier of a gene from the KOME database.
    """
    Locus_ID_LEFT_PARENTHESISTropgeneRIGHT_PARENTHESIS = "EDAM_data:1908"
    """
    Identifier of a locus from the Tropgene database.
    """
    Alignment = "EDAM_data:1916"
    """
    An alignment of molecular sequences, structures or profiles derived from them.
    """
    Atomic_property = "EDAM_data:1917"
    """
    Data for an atom (in a molecular structure).
    """
    UniProt_keyword = "EDAM_data:2007"
    """
    A word or phrase that can appear in the keywords field (KW line) of entries from the UniProt database.
    """
    Sequence_coordinates = "EDAM_data:2012"
    """
    A position in a map (for example a genetic map), either a single position (point) or a region / interval.
    This includes positions in genomes based on a reference sequence. A position may be specified for any mappable object, i.e. anything that may have positional information such as a physical position in a chromosome. Data might include sequence region name, strand, coordinate system name, assembly name, start position and end position.
    """
    Amino_acid_property = "EDAM_data:2016"
    """
    Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all amino acids.
    """
    Map_data = "EDAM_data:2019"
    """
    Data describing a molecular map (genetic or physical) or a set of such maps, including various attributes of, data extracted from or derived from the analysis of them, but excluding the map(s) themselves. This includes metadata for map sets that share a common set of features which are mapped.
    """
    Enzyme_kinetics_data = "EDAM_data:2024"
    """
    Data concerning chemical reaction(s) catalysed by enzyme(s).
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Michaelis_Menten_plot = "EDAM_data:2025"
    """
    A plot giving an approximation of the kinetics of an enzyme-catalysed reaction, assuming simple kinetics (i.e. no intermediate or product inhibition, allostericity or cooperativity). It plots initial reaction rate to the substrate concentration (S) from which the maximum rate (vmax) is apparent.
    """
    Hanes_Woolf_plot = "EDAM_data:2026"
    """
    A plot based on the Michaelis Menten equation of enzyme kinetics plotting the ratio of the initial substrate concentration (S) against the reaction velocity (v).
    """
    Evidence = "EDAM_data:2042"
    """
    Typically a human-readable summary of body of facts or information indicating why a statement is true or valid. This may include a computational prediction, laboratory experiment, literature reference etc.
    """
    Sequence = "EDAM_data:2044"
    """
    One or more molecular sequences, possibly with associated annotation.
    This concept is a placeholder of concepts for primary sequence data including raw sequences and sequence records. It should not normally be used for derivatives such as sequence alignments, motifs or profiles.
    """
    Report = "EDAM_data:2048"
    """
    A human-readable collection of information including annotation on a biological entity or phenomena, computer-generated reports of analysis of primary data (e.g. sequence or structural), and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
    You can use this term by default for any textual report, in case you can't find another, more specific term. Reports may be generated automatically or collated by hand and can include metadata on the origin, source, history, ownership or location of some thing.
    """
    Molecular_property_LEFT_PARENTHESISgeneralRIGHT_PARENTHESIS = "EDAM_data:2050"
    """
    General data for a molecule.
    """
    Sequence_motif_LEFT_PARENTHESISnucleic_acidRIGHT_PARENTHESIS = "EDAM_data:2070"
    """
    A nucleotide sequence motif.
    """
    Sequence_motif_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:2071"
    """
    An amino acid sequence motif.
    """
    Database_search_results = "EDAM_data:2080"
    """
    A report of hits from searching a database of some type.
    """
    Matrix = "EDAM_data:2082"
    """
    An array of numerical values.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Nucleic_acid_report = "EDAM_data:2084"
    """
    A human-readable collection of information about one or more specific nucleic acid molecules.
    """
    Structure_report = "EDAM_data:2085"
    """
    A human-readable collection of information about one or more molecular tertiary (3D) structures. It might include annotation on the structure, a computer-generated report of analysis of structural data, and metadata (data about primary data) or any other free (essentially unformatted) text, as distinct from the primary data itself.
    """
    Molecular_property = "EDAM_data:2087"
    """
    A report on the physical (e.g. structural) or chemical properties of molecules, or parts of a molecule.
    """
    DNA_base_structural_data = "EDAM_data:2088"
    """
    Structural data for DNA base pairs or runs of bases, such as energy or angle data.
    """
    Accession = "EDAM_data:2091"
    """
    A persistent (stable) and unique identifier, typically identifying an object (entry) from a database.
    """
    Data_reference = "EDAM_data:2093"
    """
    A list of database accessions or identifiers are usually included.
    Reference to a dataset (or a cross-reference between two datasets), typically one or more entries in a biological database or ontology.
    """
    Job_identifier = "EDAM_data:2098"
    """
    An identifier of a submitted job.
    """
    Name = "EDAM_data:2099"
    """
    A name of a thing, which need not necessarily uniquely identify it.
    """
    Account_authentication = "EDAM_data:2101"
    """
    Authentication data usually used to log in into an account on an information system such as a web application or a database.
    """
    KEGG_organism_code = "EDAM_data:2102"
    """
    A three-letter code used in the KEGG databases to uniquely identify organisms.
    """
    BioCyc_ID = "EDAM_data:2104"
    """
    Identifier of an object from one of the BioCyc databases.
    """
    Compound_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "EDAM_data:2105"
    """
    Identifier of a compound from the BioCyc chemical compounds database.
    """
    Reaction_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "EDAM_data:2106"
    """
    Identifier of a biological reaction from the BioCyc reactions database.
    """
    Enzyme_ID_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "EDAM_data:2107"
    """
    Identifier of an enzyme from the BioCyc enzymes database.
    """
    Reaction_ID = "EDAM_data:2108"
    """
    Identifier of a biological reaction from a database.
    """
    Identifier_LEFT_PARENTHESIShybridRIGHT_PARENTHESIS = "EDAM_data:2109"
    """
    An identifier that is re-used for data objects of fundamentally different types (typically served from a single database).
    This branch provides an alternative organisation of the concepts nested under 'Accession' and 'Name'. All concepts under here are already included under 'Accession' or 'Name'.
    """
    Molecular_property_identifier = "EDAM_data:2110"
    """
    Identifier of a molecular property.
    """
    Codon_usage_table_ID = "EDAM_data:2111"
    """
    Identifier of a codon usage table, for example a genetic code.
    """
    FlyBase_primary_identifier = "EDAM_data:2112"
    """
    Primary identifier of an object from the FlyBase database.
    """
    WormBase_identifier = "EDAM_data:2113"
    """
    Identifier of an object from the WormBase database.
    """
    WormBase_wormpep_ID = "EDAM_data:2114"
    """
    Protein identifier used by WormBase database.
    """
    Map_identifier = "EDAM_data:2117"
    """
    An identifier of a map of a molecular sequence.
    """
    Person_identifier = "EDAM_data:2118"
    """
    An identifier of a software end-user on a website or a database (typically a person or an entity).
    """
    Nucleic_acid_identifier = "EDAM_data:2119"
    """
    Name or other identifier of a nucleic acid molecule.
    """
    Genetic_code_identifier = "EDAM_data:2127"
    """
    An identifier of a genetic code.
    """
    Genetic_code_name = "EDAM_data:2128"
    """
    Informal name for a genetic code, typically an organism name.
    """
    File_format_name = "EDAM_data:2129"
    """
    Name of a file format such as HTML, PNG, PDF, EMBL, GenBank and so on.
    """
    Operating_system_name = "EDAM_data:2131"
    """
    Name of a computer operating system such as Linux, PC or Mac.
    """
    Logical_operator = "EDAM_data:2133"
    """
    A logical operator such as OR, AND, XOR, and NOT.
    """
    Gap_penalty = "EDAM_data:2137"
    """
    A penalty for introducing or extending a gap in an alignment.
    """
    Nucleic_acid_melting_temperature = "EDAM_data:2139"
    """
    A temperature concerning nucleic acid denaturation, typically the temperature at which the two strands of a hybridised or double stranded nucleic acid (DNA or RNA/DNA) molecule separate.
    """
    Concentration = "EDAM_data:2140"
    """
    The concentration of a chemical compound.
    """
    Sequence_name = "EDAM_data:2154"
    """
    Any arbitrary name of a molecular sequence.
    """
    Fickett_testcode_plot = "EDAM_data:2160"
    """
    A plot of Fickett testcode statistic (identifying protein coding regions) in a nucleotide sequences.
    """
    Sequence_similarity_plot = "EDAM_data:2161"
    """
    A plot of sequence similarities identified from word-matching or character comparison.
    Use this concept for calculated substitution rates, relative site variability, data on sites with biased properties, highly conserved or very poorly conserved sites, regions, blocks etc.
    """
    Helical_wheel = "EDAM_data:2162"
    """
    An image of peptide sequence sequence looking down the axis of the helix for highlighting amphipathicity and other properties.
    """
    Helical_net = "EDAM_data:2163"
    """
    An image of peptide sequence sequence in a simple 3,4,3,4 repeating pattern that emulates at a simple level the arrangement of residues around an alpha helix.
    Useful for highlighting amphipathicity and other properties.
    """
    Protein_ionisation_curve = "EDAM_data:2165"
    """
    A plot of pK versus pH for a protein.
    """
    Sequence_composition_plot = "EDAM_data:2166"
    """
    A plot of character or word composition / frequency of a molecular sequence.
    """
    Nucleic_acid_density_plot = "EDAM_data:2167"
    """
    Density plot (of base composition) for a nucleotide sequence.
    """
    Sequence_trace_image = "EDAM_data:2168"
    """
    Image of a sequence trace (nucleotide sequence versus probabilities of each of the 4 bases).
    """
    FlyBase_secondary_identifier = "EDAM_data:2174"
    """
    Secondary identifier are used to handle entries that were merged with or split from other entries in the database.
    Secondary identifier of an object from the FlyBase database.
    """
    Sequence_checksum = "EDAM_data:2190"
    """
    A fixed-size datum calculated (by using a hash function) for a molecular sequence, typically for purposes of error detection or indexing.
    """
    Database_entry_metadata = "EDAM_data:2193"
    """
    Basic information on any arbitrary database entry.
    """
    Plasmid_identifier = "EDAM_data:2208"
    """
    An identifier of a plasmid in a database.
    """
    Mutation_ID = "EDAM_data:2209"
    """
    A unique identifier of a specific mutation catalogued in a database.
    """
    Codon_number = "EDAM_data:2216"
    """
    The number of a codon, for instance, at which a mutation is located.
    """
    Database_field_name = "EDAM_data:2219"
    """
    The name of a field in a database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISSYSTERSRIGHT_PARENTHESIS = "EDAM_data:2220"
    """
    Unique identifier of a sequence cluster from the SYSTERS database.
    """
    Ontology_metadata = "EDAM_data:2223"
    """
    Data concerning a biological ontology.
    """
    Data_resource_definition_name = "EDAM_data:2253"
    """
    The name of a data type.
    """
    OBO_file_format_name = "EDAM_data:2254"
    """
    Name of an OBO file format such as OBO-XML, plain and so on.
    """
    Gene_ID_LEFT_PARENTHESISMIPSRIGHT_PARENTHESIS = "EDAM_data:2285"
    """
    Identifier for genetic elements in MIPS database.
    """
    EMBL_accession = "EDAM_data:2290"
    """
    An accession number of an entry from the EMBL sequence database.
    """
    UniProt_ID = "EDAM_data:2291"
    """
    An identifier of a polypeptide in the UniProt database.
    """
    GenBank_accession = "EDAM_data:2292"
    """
    Accession number of an entry from the GenBank sequence database.
    """
    Gramene_secondary_identifier = "EDAM_data:2293"
    """
    Secondary (internal) identifier of a Gramene database entry.
    """
    Sequence_variation_ID = "EDAM_data:2294"
    """
    An identifier of an entry from a database of molecular sequence variation.
    """
    Gene_ID = "EDAM_data:2295"
    """
    A unique (and typically persistent) identifier of a gene in a database, that is (typically) different to the gene name/symbol.
    """
    Gene_ID_LEFT_PARENTHESISECKRIGHT_PARENTHESIS = "EDAM_data:2297"
    """
    Identifier of an E. coli K-12 gene from EcoGene Database.
    """
    Gene_ID_LEFT_PARENTHESISHGNCRIGHT_PARENTHESIS = "EDAM_data:2298"
    """
    Identifier for a gene approved by the HUGO Gene Nomenclature Committee.
    """
    Gene_name = "EDAM_data:2299"
    """
    The name of a gene, (typically) assigned by a person and/or according to a naming scheme. It may contain white space characters and is typically more intuitive and readable than a gene symbol. It (typically) may be used to identify similar genes in different species and to derive a gene symbol.
    """
    SMILES_string = "EDAM_data:2301"
    """
    A specification of a chemical structure in SMILES format.
    """
    STRING_ID = "EDAM_data:2302"
    """
    Unique identifier of an entry from the STRING database of protein-protein interactions.
    """
    Reaction_ID_LEFT_PARENTHESISSABIO_RKRIGHT_PARENTHESIS = "EDAM_data:2309"
    """
    Identifier of a biological reaction from the SABIO-RK reactions database.
    """
    Carbohydrate_report = "EDAM_data:2313"
    """
    A human-readable collection of information about one or more specific carbohydrate 3D structure(s).
    """
    GI_number = "EDAM_data:2314"
    """
    A series of digits that are assigned consecutively to each sequence record processed by NCBI. The GI number bears no resemblance to the Accession number of the sequence record.
    Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record.
    """
    NCBI_version = "EDAM_data:2315"
    """
    An identifier assigned to sequence records processed by NCBI, made of the accession number of the database record followed by a dot and a version number.
    Nucleotide sequence version contains two letters followed by six digits, a dot, and a version number (or for older nucleotide sequence records, the format is one letter followed by five digits, a dot, and a version number). Protein sequence version contains three letters followed by five digits, a dot, and a version number.
    """
    Cell_line_name = "EDAM_data:2316"
    """
    The name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESISexactRIGHT_PARENTHESIS = "EDAM_data:2317"
    """
    The exact name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESIStruncatedRIGHT_PARENTHESIS = "EDAM_data:2318"
    """
    The truncated name of a cell line.
    """
    Cell_line_name_LEFT_PARENTHESISno_punctuationRIGHT_PARENTHESIS = "EDAM_data:2319"
    """
    The name of a cell line without any punctuation.
    """
    Cell_line_name_LEFT_PARENTHESISassonantRIGHT_PARENTHESIS = "EDAM_data:2320"
    """
    The assonant name of a cell line.
    """
    Enzyme_ID = "EDAM_data:2321"
    """
    A unique, persistent identifier of an enzyme.
    """
    REBASE_enzyme_number = "EDAM_data:2325"
    """
    Identifier of an enzyme from the REBASE enzymes database.
    """
    DrugBank_ID = "EDAM_data:2326"
    """
    Unique identifier of a drug from the DrugBank database.
    """
    GI_number_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:2327"
    """
    A unique identifier assigned to NCBI protein sequence records.
    Nucleotide sequence GI number is shown in the VERSION field of the database record. Protein sequence GI number is shown in the CDS/db_xref field of a nucleotide database record, and the VERSION field of a protein database record.
    """
    Bit_score = "EDAM_data:2335"
    """
    A score derived from the alignment of two sequences, which is then normalised with respect to the scoring system.
    Bit scores are normalised with respect to the scoring system and therefore can be used to compare alignment scores from different searches.
    """
    Resource_metadata = "EDAM_data:2337"
    """
    Data concerning or describing some core computational resource, as distinct from primary data. This includes metadata on the origin, source, history, ownership or location of some thing.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Ontology_identifier = "EDAM_data:2338"
    """
    Any arbitrary identifier of an ontology.
    """
    Ontology_concept_name = "EDAM_data:2339"
    """
    The name of a concept in an ontology.
    """
    Genome_build_identifier = "EDAM_data:2340"
    """
    An identifier of a build of a particular genome.
    """
    Pathway_or_network_name = "EDAM_data:2342"
    """
    The name of a biological pathway or network.
    """
    Pathway_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "EDAM_data:2343"
    """
    Identifier of a pathway from the KEGG pathway database.
    """
    Pathway_ID_LEFT_PARENTHESISNCI_NatureRIGHT_PARENTHESIS = "EDAM_data:2344"
    """
    Identifier of a pathway from the NCI-Nature pathway database.
    """
    Pathway_ID_LEFT_PARENTHESISConsensusPathDBRIGHT_PARENTHESIS = "EDAM_data:2345"
    """
    Identifier of a pathway from the ConsensusPathDB pathway database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRefRIGHT_PARENTHESIS = "EDAM_data:2346"
    """
    Unique identifier of an entry from the UniRef database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef100RIGHT_PARENTHESIS = "EDAM_data:2347"
    """
    Unique identifier of an entry from the UniRef100 database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef90RIGHT_PARENTHESIS = "EDAM_data:2348"
    """
    Unique identifier of an entry from the UniRef90 database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISUniRef50RIGHT_PARENTHESIS = "EDAM_data:2349"
    """
    Unique identifier of an entry from the UniRef50 database.
    """
    Ontology_data = "EDAM_data:2353"
    """
    Data concerning or derived from an ontology.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    RNA_family_report = "EDAM_data:2354"
    """
    A human-readable collection of information about a specific RNA family or other group of classified RNA sequences.
    """
    RNA_family_identifier = "EDAM_data:2355"
    """
    Identifier of an RNA family, typically an entry from a RNA sequence classification database.
    """
    RFAM_accession = "EDAM_data:2356"
    """
    Stable accession number of an entry (RNA family) from the RFAM database.
    """
    Sequence_accession_LEFT_PARENTHESIShybridRIGHT_PARENTHESIS = "EDAM_data:2362"
    """
    Accession number of a nucleotide or protein sequence database entry.
    """
    Pathway_or_network_accession = "EDAM_data:2365"
    """
    A persistent, unique identifier of a biological pathway or network (typically a database entry).
    """
    Secondary_structure_alignment = "EDAM_data:2366"
    """
    Alignment of the (1D representations of) secondary structure of two or more molecules.
    """
    ASTD_ID = "EDAM_data:2367"
    """
    Identifier of an object from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISexonRIGHT_PARENTHESIS = "EDAM_data:2368"
    """
    Identifier of an exon from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISintronRIGHT_PARENTHESIS = "EDAM_data:2369"
    """
    Identifier of an intron from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESISpolyaRIGHT_PARENTHESIS = "EDAM_data:2370"
    """
    Identifier of a polyA signal from the ASTD database.
    """
    ASTD_ID_LEFT_PARENTHESIStssRIGHT_PARENTHESIS = "EDAM_data:2371"
    """
    Identifier of a transcription start site from the ASTD database.
    """
    Spot_ID = "EDAM_data:2373"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel.
    """
    Spot_serial_number = "EDAM_data:2374"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel in the SWISS-2DPAGE database.
    """
    Spot_ID_LEFT_PARENTHESISHSC_2DPAGERIGHT_PARENTHESIS = "EDAM_data:2375"
    """
    Unique identifier of a spot from a two-dimensional (protein) gel from a HSC-2DPAGE database.
    """
    Strain_identifier = "EDAM_data:2379"
    """
    Identifier of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    CABRI_accession = "EDAM_data:2380"
    """
    A unique identifier of an item from the CABRI database.
    """
    Genotype_experiment_ID = "EDAM_data:2382"
    """
    Identifier of an entry from a database of genotype experiment metadata.
    """
    EGA_accession = "EDAM_data:2383"
    """
    Identifier of an entry from the EGA database.
    """
    IPI_protein_ID = "EDAM_data:2384"
    """
    Identifier of a protein entry catalogued in the International Protein Index (IPI) database.
    """
    RefSeq_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:2385"
    """
    Accession number of a protein from the RefSeq database.
    """
    EPD_ID = "EDAM_data:2386"
    """
    Identifier of an entry (promoter) from the EPD database.
    """
    TAIR_accession = "EDAM_data:2387"
    """
    Identifier of an entry from the TAIR database.
    """
    TAIR_accession_LEFT_PARENTHESISAt_geneRIGHT_PARENTHESIS = "EDAM_data:2388"
    """
    Identifier of an Arabidopsis thaliana gene from the TAIR database.
    """
    UniSTS_accession = "EDAM_data:2389"
    """
    Identifier of an entry from the UniSTS database.
    """
    UNITE_accession = "EDAM_data:2390"
    """
    Identifier of an entry from the UNITE database.
    """
    UTR_accession = "EDAM_data:2391"
    """
    Identifier of an entry from the UTR database.
    """
    UniParc_accession = "EDAM_data:2392"
    """
    Accession number of a UniParc (protein sequence) database entry.
    """
    mFLJSOLIDUSmKIAA_number = "EDAM_data:2393"
    """
    Identifier of an entry from the Rouge or HUGE databases.
    """
    Ensembl_protein_ID = "EDAM_data:2398"
    """
    Unique identifier for a protein from the Ensembl database.
    """
    Phylogenetic_data = "EDAM_data:2523"
    """
    Data concerning phylogeny, typically of molecular sequences, including reports of information concerning or derived from a phylogenetic tree, or from comparing two or more phylogenetic trees.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Text_data = "EDAM_data:2526"
    """
    Data concerning, extracted from, or derived from the analysis of a scientific text (or texts) such as a full text article from a scientific journal.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation. It includes concepts that are best described as scientific text or closely concerned with or derived from text.
    """
    Organism_report = "EDAM_data:2530"
    """
    A human-readable collection of information about a specific organism.
    """
    Protocol = "EDAM_data:2531"
    """
    A human-readable collection of information about about how a scientific experiment or analysis was carried out that results in a specific set of data or results used for further analysis or to test a specific hypothesis.
    """
    Sequence_attribute = "EDAM_data:2534"
    """
    An attribute of a molecular sequence, possibly in reference to some other sequence.
    """
    Sequence_tag_profile = "EDAM_data:2535"
    """
    Output from a serial analysis of gene expression (SAGE), massively parallel signature sequencing (MPSS) or sequencing by synthesis (SBS) experiment. In all cases this is a list of short sequence tags and the number of times it is observed.
    SAGE, MPSS and SBS experiments are usually performed to study gene expression. The sequence tags are typically subsequently annotated (after a database search) with the mRNA (and therefore gene) the tag was extracted from.
    This includes tag to gene assignments (tag mapping) of SAGE, MPSS and SBS data. Typically this is the sequencing-based expression profile annotated with gene identifiers.
    """
    Mass_spectrometry_data = "EDAM_data:2536"
    """
    Data concerning a mass spectrometry measurement.
    """
    Protein_structure_raw_data = "EDAM_data:2537"
    """
    Raw data from experimental methods for determining protein structure.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.
    """
    Mutation_identifier = "EDAM_data:2538"
    """
    An identifier of a mutation.
    """
    Amino_acid_name_LEFT_PARENTHESISsingle_letterRIGHT_PARENTHESIS = "EDAM_data:2563"
    """
    Single letter amino acid identifier, e.g. G.
    """
    Amino_acid_name_LEFT_PARENTHESISthree_letterRIGHT_PARENTHESIS = "EDAM_data:2564"
    """
    Three letter amino acid identifier, e.g. GLY.
    """
    Amino_acid_name_LEFT_PARENTHESISfull_nameRIGHT_PARENTHESIS = "EDAM_data:2565"
    """
    Full name of an amino acid, e.g. Glycine.
    """
    Toxin_identifier = "EDAM_data:2576"
    """
    Identifier of a toxin.
    """
    ArachnoServer_ID = "EDAM_data:2578"
    """
    Unique identifier of a toxin from the ArachnoServer database.
    """
    BindingDB_Monomer_ID = "EDAM_data:2580"
    """
    Unique identifier of a monomer from the BindingDB database.
    """
    GO_concept_ID_LEFT_PARENTHESISbiological_processRIGHT_PARENTHESIS = "EDAM_data:2582"
    """
    An identifier of a 'biological process' concept from the the Gene Ontology.
    """
    GO_concept_ID_LEFT_PARENTHESISmolecular_functionRIGHT_PARENTHESIS = "EDAM_data:2583"
    """
    An identifier of a 'molecular function' concept from the the Gene Ontology.
    """
    Northern_blot_image = "EDAM_data:2586"
    """
    An image arising from a Northern Blot experiment.
    """
    Blot_ID = "EDAM_data:2587"
    """
    Unique identifier of a blot from a Northern Blot.
    """
    BlotBase_blot_ID = "EDAM_data:2588"
    """
    Unique identifier of a blot from a Northern Blot from the BlotBase database.
    """
    Hierarchy = "EDAM_data:2589"
    """
    Raw data on a biological hierarchy, describing the hierarchy proper, hierarchy components and possibly associated annotation.
    """
    Brite_hierarchy_ID = "EDAM_data:2591"
    """
    Identifier of an entry from the Brite database of biological hierarchies.
    """
    BRENDA_organism_ID = "EDAM_data:2593"
    """
    A unique identifier for an organism used in the BRENDA database.
    """
    UniGene_taxon = "EDAM_data:2594"
    """
    The name of a taxon using the controlled vocabulary of the UniGene database.
    """
    UTRdb_taxon = "EDAM_data:2595"
    """
    The name of a taxon using the controlled vocabulary of the UTRdb database.
    """
    Catalogue_ID = "EDAM_data:2596"
    """
    An identifier of a catalogue of biological resources.
    """
    CABRI_catalogue_name = "EDAM_data:2597"
    """
    The name of a catalogue of biological resources from the CABRI database.
    """
    Pathway_or_network = "EDAM_data:2600"
    """
    Primary data about a specific biological pathway or network (the nodes and connections within the pathway or network).
    """
    Expression_data = "EDAM_data:2603"
    """
    Image, hybridisation or some other data arising from a study of feature/molecule expression, typically profiling or quantification.
    """
    Compound_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "EDAM_data:2605"
    """
    Unique identifier of a chemical compound from the KEGG database.
    """
    RFAM_name = "EDAM_data:2606"
    """
    Name (not necessarily stable) an entry (RNA family) from the RFAM database.
    """
    Reaction_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "EDAM_data:2608"
    """
    Identifier of a biological reaction from the KEGG reactions database.
    """
    Drug_ID_LEFT_PARENTHESISKEGGRIGHT_PARENTHESIS = "EDAM_data:2609"
    """
    Unique identifier of a drug from the KEGG Drug database.
    """
    Ensembl_ID = "EDAM_data:2610"
    """
    Identifier of an entry (exon, gene, transcript or protein) from the Ensembl database.
    """
    ICD_identifier = "EDAM_data:2611"
    """
    An identifier of a disease from the International Classification of Diseases (ICD) database.
    """
    Sequence_cluster_ID_LEFT_PARENTHESISCluSTrRIGHT_PARENTHESIS = "EDAM_data:2612"
    """
    Unique identifier of a sequence cluster from the CluSTr database.
    """
    KEGG_Glycan_ID = "EDAM_data:2613"
    """
    Unique identifier of a glycan ligand from the KEGG GLYCAN database (a subset of KEGG LIGAND).
    """
    TCDB_ID = "EDAM_data:2614"
    """
    A unique identifier of a family from the transport classification database (TCDB) of membrane transport proteins.
    OBO file for regular expression.
    """
    MINT_ID = "EDAM_data:2615"
    """
    Unique identifier of an entry from the MINT database of protein-protein interactions.
    """
    DIP_ID = "EDAM_data:2616"
    """
    Unique identifier of an entry from the DIP database of protein-protein interactions.
    """
    Signaling_Gateway_protein_ID = "EDAM_data:2617"
    """
    Unique identifier of a protein listed in the UCSD-Nature Signaling Gateway Molecule Pages database.
    """
    Protein_modification_ID = "EDAM_data:2618"
    """
    Identifier of a protein modification catalogued in a database.
    """
    RESID_ID = "EDAM_data:2619"
    """
    Identifier of a protein modification catalogued in the RESID database.
    """
    RGD_ID = "EDAM_data:2620"
    """
    Identifier of an entry from the RGD database.
    """
    TAIR_accession_LEFT_PARENTHESISproteinRIGHT_PARENTHESIS = "EDAM_data:2621"
    """
    Identifier of a protein sequence from the TAIR database.
    """
    Compound_ID_LEFT_PARENTHESISHMDBRIGHT_PARENTHESIS = "EDAM_data:2622"
    """
    Identifier of a small molecule metabolite from the Human Metabolome Database (HMDB).
    """
    LIPID_MAPS_ID = "EDAM_data:2625"
    """
    Identifier of an entry from the LIPID MAPS database.
    """
    PeptideAtlas_ID = "EDAM_data:2626"
    """
    Identifier of a peptide from the PeptideAtlas peptide databases.
    """
    BioGRID_interaction_ID = "EDAM_data:2628"
    """
    A unique identifier of an interaction from the BioGRID database.
    """
    Enzyme_ID_LEFT_PARENTHESISMEROPSRIGHT_PARENTHESIS = "EDAM_data:2629"
    """
    Unique identifier of a peptidase enzyme from the MEROPS database.
    """
    Mobile_genetic_element_ID = "EDAM_data:2630"
    """
    An identifier of a mobile genetic element.
    """
    ACLAME_ID = "EDAM_data:2631"
    """
    An identifier of a mobile genetic element from the Aclame database.
    """
    SGD_ID = "EDAM_data:2632"
    """
    Identifier of an entry from the Saccharomyces genome database (SGD).
    """
    Book_ID = "EDAM_data:2633"
    """
    Unique identifier of a book.
    """
    ISBN = "EDAM_data:2634"
    """
    The International Standard Book Number (ISBN) is for identifying printed books.
    """
    Compound_ID_LEFT_PARENTHESIS3DMETRIGHT_PARENTHESIS = "EDAM_data:2635"
    """
    Identifier of a metabolite from the 3DMET database.
    """
    MatrixDB_interaction_ID = "EDAM_data:2636"
    """
    A unique identifier of an interaction from the MatrixDB database.
    """
    cPath_ID = "EDAM_data:2637"
    """
    A unique identifier for pathways, reactions, complexes and small molecules from the cPath (Pathway Commons) database.
    These identifiers are unique within the cPath database, however, they are not stable between releases.
    """
    PubChem_bioassay_ID = "EDAM_data:2638"
    """
    Identifier of an assay from the PubChem database.
    """
    PubChem_ID = "EDAM_data:2639"
    """
    Identifier of an entry from the PubChem database.
    """
    Reaction_ID_LEFT_PARENTHESISMACieRIGHT_PARENTHESIS = "EDAM_data:2641"
    """
    Identifier of an enzyme reaction mechanism from the MACie database.
    """
    Gene_ID_LEFT_PARENTHESISmiRBaseRIGHT_PARENTHESIS = "EDAM_data:2642"
    """
    Identifier for a gene from the miRBase database.
    """
    Gene_ID_LEFT_PARENTHESISZFINRIGHT_PARENTHESIS = "EDAM_data:2643"
    """
    Identifier for a gene from the Zebrafish information network genome (ZFIN) database.
    """
    Reaction_ID_LEFT_PARENTHESISRheaRIGHT_PARENTHESIS = "EDAM_data:2644"
    """
    Identifier of an enzyme-catalysed reaction from the Rhea database.
    """
    Pathway_ID_LEFT_PARENTHESISUnipathwayRIGHT_PARENTHESIS = "EDAM_data:2645"
    """
    Identifier of a biological pathway from the Unipathway database.
    """
    Compound_ID_LEFT_PARENTHESISChEMBLRIGHT_PARENTHESIS = "EDAM_data:2646"
    """
    Identifier of a small molecular from the ChEMBL database.
    """
    LGICdb_identifier = "EDAM_data:2647"
    """
    Unique identifier of an entry from the Ligand-gated ion channel (LGICdb) database.
    """
    Reaction_kinetics_ID_LEFT_PARENTHESISSABIO_RKRIGHT_PARENTHESIS = "EDAM_data:2648"
    """
    Identifier of a biological reaction (kinetics entry) from the SABIO-RK reactions database.
    """
    PharmGKB_ID = "EDAM_data:2649"
    """
    Identifier of an entry from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Pathway_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "EDAM_data:2650"
    """
    Identifier of a pathway from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Disease_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "EDAM_data:2651"
    """
    Identifier of a disease from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Drug_ID_LEFT_PARENTHESISPharmGKBRIGHT_PARENTHESIS = "EDAM_data:2652"
    """
    Identifier of a drug from the pharmacogenetics and pharmacogenomics knowledge base (PharmGKB).
    """
    Drug_ID_LEFT_PARENTHESISTTDRIGHT_PARENTHESIS = "EDAM_data:2653"
    """
    Identifier of a drug from the Therapeutic Target Database (TTD).
    """
    Target_ID_LEFT_PARENTHESISTTDRIGHT_PARENTHESIS = "EDAM_data:2654"
    """
    Identifier of a target protein from the Therapeutic Target Database (TTD).
    """
    Cell_type_identifier = "EDAM_data:2655"
    """
    A unique identifier of a type or group of cells.
    """
    NeuronDB_ID = "EDAM_data:2656"
    """
    A unique identifier of a neuron from the NeuronDB database.
    """
    NeuroMorpho_ID = "EDAM_data:2657"
    """
    A unique identifier of a neuron from the NeuroMorpho database.
    """
    Compound_ID_LEFT_PARENTHESISChemIDplusRIGHT_PARENTHESIS = "EDAM_data:2658"
    """
    Identifier of a chemical from the ChemIDplus database.
    """
    Pathway_ID_LEFT_PARENTHESISSMPDBRIGHT_PARENTHESIS = "EDAM_data:2659"
    """
    Identifier of a pathway from the Small Molecule Pathway Database (SMPDB).
    """
    BioNumbers_ID = "EDAM_data:2660"
    """
    Identifier of an entry from the BioNumbers database of key numbers and associated data in molecular biology.
    """
    T3DB_ID = "EDAM_data:2662"
    """
    Unique identifier of a toxin from the Toxin and Toxin Target Database (T3DB) database.
    """
    Carbohydrate_identifier = "EDAM_data:2663"
    """
    Identifier of a carbohydrate.
    """
    GlycomeDB_ID = "EDAM_data:2664"
    """
    Identifier of an entry from the GlycomeDB database.
    """
    LipidBank_ID = "EDAM_data:2665"
    """
    Identifier of an entry from the LipidBank database.
    """
    CDD_ID = "EDAM_data:2666"
    """
    Identifier of a conserved domain from the Conserved Domain Database.
    """
    MMDB_ID = "EDAM_data:2667"
    """
    An identifier of an entry from the MMDB database.
    """
    iRefIndex_ID = "EDAM_data:2668"
    """
    Unique identifier of an entry from the iRefIndex database of protein-protein interactions.
    """
    ModelDB_ID = "EDAM_data:2669"
    """
    Unique identifier of an entry from the ModelDB database.
    """
    Pathway_ID_LEFT_PARENTHESISDQCSRIGHT_PARENTHESIS = "EDAM_data:2670"
    """
    Identifier of a signaling pathway from the Database of Quantitative Cellular Signaling (DQCS).
    """
    CATH_identifier = "EDAM_data:2700"
    """
    Identifier of a protein domain (or other node) from the CATH database.
    """
    CATH_node_ID_LEFT_PARENTHESISfamilyRIGHT_PARENTHESIS = "EDAM_data:2701"
    """
    A code number identifying a family from the CATH database.
    """
    Enzyme_ID_LEFT_PARENTHESISCAZyRIGHT_PARENTHESIS = "EDAM_data:2702"
    """
    Identifier of an enzyme from the CAZy enzymes database.
    """
    Clone_ID_LEFT_PARENTHESISIMAGERIGHT_PARENTHESIS = "EDAM_data:2704"
    """
    A unique identifier assigned by the I.M.A.G.E. consortium to a clone (cloned molecular sequence).
    """
    GO_concept_ID_LEFT_PARENTHESIScellular_componentRIGHT_PARENTHESIS = "EDAM_data:2705"
    """
    An identifier of a 'cellular component' concept from the Gene Ontology.
    """
    Chromosome_name_LEFT_PARENTHESISBioCycRIGHT_PARENTHESIS = "EDAM_data:2706"
    """
    Name of a chromosome as used in the BioCyc database.
    """
    CleanEx_entry_name = "EDAM_data:2709"
    """
    An identifier of a gene expression profile from the CleanEx database.
    """
    CleanEx_dataset_code = "EDAM_data:2710"
    """
    An identifier of (typically a list of) gene expression experiments catalogued in the CleanEx database.
    """
    Genome_report = "EDAM_data:2711"
    """
    A human-readable collection of information concerning a genome as a whole.
    """
    Protein_ID_LEFT_PARENTHESISCORUMRIGHT_PARENTHESIS = "EDAM_data:2713"
    """
    Unique identifier for a protein complex from the CORUM database.
    """
    CDD_PSSM_ID = "EDAM_data:2714"
    """
    Unique identifier of a position-specific scoring matrix from the CDD database.
    """
    Protein_ID_LEFT_PARENTHESISCuticleDBRIGHT_PARENTHESIS = "EDAM_data:2715"
    """
    Unique identifier for a protein from the CuticleDB database.
    """
    DBD_ID = "EDAM_data:2716"
    """
    Identifier of a predicted transcription factor from the DBD database.
    """
    Oligonucleotide_probe_annotation = "EDAM_data:2717"
    """
    General annotation on an oligonucleotide probe, or a set of probes.
    """
    Oligonucleotide_ID = "EDAM_data:2718"
    """
    Identifier of an oligonucleotide from a database.
    """
    dbProbe_ID = "EDAM_data:2719"
    """
    Identifier of an oligonucleotide probe from the dbProbe database.
    """
    Dinucleotide_property = "EDAM_data:2720"
    """
    Physicochemical property data for one or more dinucleotides.
    """
    DiProDB_ID = "EDAM_data:2721"
    """
    Identifier of an dinucleotide property from the DiProDB database.
    """
    Protein_ID_LEFT_PARENTHESISDisProtRIGHT_PARENTHESIS = "EDAM_data:2723"
    """
    Unique identifier for a protein from the DisProt database.
    """
    Ensembl_transcript_ID = "EDAM_data:2725"
    """
    Unique identifier for a gene transcript from the Ensembl database.
    """
    Promoter_ID = "EDAM_data:2727"
    """
    An identifier of a promoter of a gene that is catalogued in a database.
    """
    EST_accession = "EDAM_data:2728"
    """
    Identifier of an EST sequence.
    """
    COGEME_EST_ID = "EDAM_data:2729"
    """
    Identifier of an EST sequence from the COGEME database.
    """
    COGEME_unisequence_ID = "EDAM_data:2730"
    """
    A unisequence is a single sequence assembled from ESTs.
    Identifier of a unisequence from the COGEME database.
    """
    Protein_family_ID_LEFT_PARENTHESISGeneFarmRIGHT_PARENTHESIS = "EDAM_data:2731"
    """
    Accession number of an entry (protein family) from the GeneFarm database.
    """
    Family_name = "EDAM_data:2732"
    """
    The name of a family of organism.
    """
    Sequence_feature_ID_LEFT_PARENTHESISSwissRegulonRIGHT_PARENTHESIS = "EDAM_data:2736"
    """
    A feature identifier as used in the SwissRegulon database.
    This can be name of a gene, the ID of a TFBS, or genomic coordinates in form "chr:start..end".
    """
    FIG_ID = "EDAM_data:2737"
    """
    A FIG ID consists of four parts: a prefix, genome id, locus type and id number.
    A unique identifier of gene in the NMPDR database.
    """
    Gene_ID_LEFT_PARENTHESISXenbaseRIGHT_PARENTHESIS = "EDAM_data:2738"
    """
    A unique identifier of gene in the Xenbase database.
    """
    Gene_ID_LEFT_PARENTHESISGenolistRIGHT_PARENTHESIS = "EDAM_data:2739"
    """
    A unique identifier of gene in the Genolist database.
    """
    ABS_ID = "EDAM_data:2741"
    """
    Identifier of an entry (promoter) from the ABS database.
    """
    AraC_XylS_ID = "EDAM_data:2742"
    """
    Identifier of a transcription factor from the AraC-XylS database.
    """
    Locus_ID_LEFT_PARENTHESISPseudoCAPRIGHT_PARENTHESIS = "EDAM_data:2744"
    """
    Identifier of a locus from the PseudoCAP database.
    """
    Locus_ID_LEFT_PARENTHESISUTRRIGHT_PARENTHESIS = "EDAM_data:2745"
    """
    Identifier of a locus from the UTR database.
    """
    MonosaccharideDB_ID = "EDAM_data:2746"
    """
    Unique identifier of a monosaccharide from the MonosaccharideDB database.
    """
    Genome_identifier = "EDAM_data:2749"
    """
    An identifier of a particular genome.
    """
    GlycoMap_ID = "EDAM_data:2752"
    """
    Identifier of an entry from the GlycoMapsDB (Glycosciences.de) database.
    """
    Carbohydrate_conformational_map = "EDAM_data:2753"
    """
    A conformational energy map of the glycosidic linkages in a carbohydrate molecule.
    """
    Transcription_factor_name = "EDAM_data:2755"
    """
    The name of a transcription factor.
    """
    TCID = "EDAM_data:2756"
    """
    Identifier of a membrane transport proteins from the transport classification database (TCDB).
    """
    Pfam_domain_name = "EDAM_data:2757"
    """
    Name of a domain from the Pfam database.
    """
    Pfam_clan_ID = "EDAM_data:2758"
    """
    Accession number of a Pfam clan.
    """
    Gene_ID_LEFT_PARENTHESISVectorBaseRIGHT_PARENTHESIS = "EDAM_data:2759"
    """
    Identifier for a gene from the VectorBase database.
    """
    UTRSite_ID = "EDAM_data:2761"
    """
    Identifier of an entry from the UTRSite database of regulatory motifs in eukaryotic UTRs.
    """
    Sequence_signature_report = "EDAM_data:2762"
    """
    An informative report about a specific or conserved pattern in a molecular sequence, such as its context in genes or proteins, its role, origin or method of construction, etc.
    """
    Protein_name_LEFT_PARENTHESISUniProtRIGHT_PARENTHESIS = "EDAM_data:2764"
    """
    Official name of a protein as used in the UniProt database.
    """
    HAMAP_ID = "EDAM_data:2766"
    """
    Name of a protein family from the HAMAP database.
    """
    Transcript_ID = "EDAM_data:2769"
    """
    Identifier of a RNA transcript.
    """
    HIT_ID = "EDAM_data:2770"
    """
    Identifier of an RNA transcript from the H-InvDB database.
    """
    HIX_ID = "EDAM_data:2771"
    """
    A unique identifier of gene cluster in the H-InvDB database.
    """
    HPA_antibody_id = "EDAM_data:2772"
    """
    Identifier of a antibody from the HPA database.
    """
    IMGTSOLIDUSHLA_ID = "EDAM_data:2773"
    """
    Identifier of a human major histocompatibility complex (HLA) or other protein from the IMGT/HLA database.
    """
    Gene_ID_LEFT_PARENTHESISJCVIRIGHT_PARENTHESIS = "EDAM_data:2774"
    """
    A unique identifier of gene assigned by the J. Craig Venter Institute (JCVI).
    """
    Kinase_name = "EDAM_data:2775"
    """
    The name of a kinase protein.
    """
    ConsensusPathDB_entity_ID = "EDAM_data:2776"
    """
    Identifier of a physical entity from the ConsensusPathDB database.
    """
    ConsensusPathDB_entity_name = "EDAM_data:2777"
    """
    Name of a physical entity from the ConsensusPathDB database.
    """
    CCAP_strain_number = "EDAM_data:2778"
    """
    The number of a strain of algae and protozoa from the CCAP database.
    """
    Stock_number = "EDAM_data:2779"
    """
    An identifier of stock from a catalogue of biological resources.
    """
    Stock_number_LEFT_PARENTHESISTAIRRIGHT_PARENTHESIS = "EDAM_data:2780"
    """
    A stock number from The Arabidopsis information resource (TAIR).
    """
    REDIdb_ID = "EDAM_data:2781"
    """
    Identifier of an entry from the RNA editing database (REDIdb).
    """
    SMART_domain_name = "EDAM_data:2782"
    """
    Name of a domain from the SMART database.
    """
    Protein_family_ID_LEFT_PARENTHESISPANTHERRIGHT_PARENTHESIS = "EDAM_data:2783"
    """
    Accession number of an entry (family) from the PANTHER database.
    """
    RNAVirusDB_ID = "EDAM_data:2784"
    """
    A unique identifier for a virus from the RNAVirusDB database.
    Could list (or reference) other taxa here from https://www.phenoscape.org/wiki/Taxonomic_Rank_Vocabulary.
    """
    Virus_identifier = "EDAM_data:2785"
    """
    An accession of annotation on a (group of) viruses (catalogued in a database).
    """
    NCBI_Genome_Project_ID = "EDAM_data:2786"
    """
    An identifier of a genome project assigned by NCBI.
    """
    NCBI_genome_accession = "EDAM_data:2787"
    """
    A unique identifier of a whole genome assigned by the NCBI.
    """
    Protein_ID_LEFT_PARENTHESISTopDBRIGHT_PARENTHESIS = "EDAM_data:2789"
    """
    Unique identifier for a membrane protein from the TopDB database.
    """
    Gel_ID = "EDAM_data:2790"
    """
    Identifier of a two-dimensional (protein) gel.
    """
    Reference_map_name_LEFT_PARENTHESISSWISS_2DPAGERIGHT_PARENTHESIS = "EDAM_data:2791"
    """
    Name of a reference map gel from the SWISS-2DPAGE database.
    """
    Protein_ID_LEFT_PARENTHESISPeroxiBaseRIGHT_PARENTHESIS = "EDAM_data:2792"
    """
    Unique identifier for a peroxidase protein from the PeroxiBase database.
    """
    SISYPHUS_ID = "EDAM_data:2793"
    """
    Identifier of an entry from the SISYPHUS database of tertiary structure alignments.
    """
    ORF_ID = "EDAM_data:2794"
    """
    Accession of an open reading frame (catalogued in a database).
    """
    ORF_identifier = "EDAM_data:2795"
    """
    An identifier of an open reading frame.
    """
    LINUCS_ID = "EDAM_data:2796"
    """
    Identifier of an entry from the GlycosciencesDB database.
    """
    Protein_ID_LEFT_PARENTHESISLGICdbRIGHT_PARENTHESIS = "EDAM_data:2797"
    """
    Unique identifier for a ligand-gated ion channel protein from the LGICdb database.
    """
    MaizeDB_ID = "EDAM_data:2798"
    """
    Identifier of an EST sequence from the MaizeDB database.
    """
    Gene_ID_LEFT_PARENTHESISMfunGDRIGHT_PARENTHESIS = "EDAM_data:2799"
    """
    A unique identifier of gene in the MfunGD database.
    """
    Orpha_number = "EDAM_data:2800"
    """
    An identifier of a disease from the Orpha database.
    """
    Protein_ID_LEFT_PARENTHESISEcIDRIGHT_PARENTHESIS = "EDAM_data:2802"
    """
    Unique identifier for a protein from the EcID database.
    """
    Clone_ID_LEFT_PARENTHESISRefSeqRIGHT_PARENTHESIS = "EDAM_data:2803"
    """
    A unique identifier of a cDNA molecule catalogued in the RefSeq database.
    """
    Protein_ID_LEFT_PARENTHESISConoServerRIGHT_PARENTHESIS = "EDAM_data:2804"
    """
    Unique identifier for a cone snail toxin protein from the ConoServer database.
    """
    GeneSNP_ID = "EDAM_data:2805"
    """
    Identifier of a GeneSNP database entry.
    """
    Lipid_identifier = "EDAM_data:2812"
    """
    Identifier of a lipid.
    """
    Gene_ID_LEFT_PARENTHESISVBASE2RIGHT_PARENTHESIS = "EDAM_data:2835"
    """
    Identifier for a gene from the VBASE2 database.
    """
    DPVweb_ID = "EDAM_data:2836"
    """
    A unique identifier for a virus from the DPVweb database.
    """
    Pathway_ID_LEFT_PARENTHESISBioSystemsRIGHT_PARENTHESIS = "EDAM_data:2837"
    """
    Identifier of a pathway from the BioSystems pathway database.
    """
    Abstract = "EDAM_data:2849"
    """
    An abstract of a scientific article.
    """
    Lipid_structure = "EDAM_data:2850"
    """
    3D coordinate and associated data for a lipid structure.
    """
    Drug_structure = "EDAM_data:2851"
    """
    3D coordinate and associated data for the (3D) structure of a drug.
    """
    Toxin_structure = "EDAM_data:2852"
    """
    3D coordinate and associated data for the (3D) structure of a toxin.
    """
    Position_specific_scoring_matrix = "EDAM_data:2854"
    """
    A simple matrix of numbers, where each value (or column of values) is derived derived from analysis of the corresponding position in a sequence alignment.
    """
    Distance_matrix = "EDAM_data:2855"
    """
    A matrix of distances between molecular entities, where a value (distance) is (typically) derived from comparison of two entities and reflects their similarity.
    """
    Structural_distance_matrix = "EDAM_data:2856"
    """
    Distances (values representing similarity) between a group of molecular structures.
    """
    Ontology_concept = "EDAM_data:2858"
    """
    A concept from a biological ontology.
    This includes any fields from the concept definition such as concept name, definition, comments and so on.
    """
    Codon_usage_bias = "EDAM_data:2865"
    """
    A numerical measure of differences in the frequency of occurrence of synonymous codons in DNA sequences.
    """
    Radiation_hybrid_map = "EDAM_data:2870"
    """
    A map showing distance between genetic markers estimated by radiation-induced breaks in a chromosome.
    The radiation method can break very closely linked markers providing a more detailed map. Most genetic markers and subsequences may be located to a defined map position and with a more precise estimates of distance than a linkage map.
    """
    ID_list = "EDAM_data:2872"
    """
    A simple list of data identifiers (such as database accessions), possibly with additional basic information on the addressed data.
    """
    Phylogenetic_gene_frequencies_data = "EDAM_data:2873"
    """
    Gene frequencies data that may be read during phylogenetic tree calculation.
    """
    Protein_complex = "EDAM_data:2877"
    """
    3D coordinate and associated data for a multi-protein complex; two or more polypeptides chains in a stable, functional association with one another.
    """
    Protein_structural_motif = "EDAM_data:2878"
    """
    3D coordinate and associated data for a protein (3D) structural motif; any group of contiguous or non-contiguous amino acid residues but typically those forming a feature with a structural or functional role.
    """
    Lipid_report = "EDAM_data:2879"
    """
    A human-readable collection of information about one or more specific lipid 3D structure(s).
    """
    Plot = "EDAM_data:2884"
    """
    Biological data that has been plotted as a graph of some type, or plotting instructions for rendering such a graph.
    """
    Protein_sequence_record = "EDAM_data:2886"
    """
    A protein sequence and associated metadata.
    """
    Nucleic_acid_sequence_record = "EDAM_data:2887"
    """
    A nucleic acid sequence and associated metadata.
    """
    Biological_model_accession = "EDAM_data:2891"
    """
    Accession of a mathematical model, typically an entry from a database.
    """
    Cell_type_name = "EDAM_data:2892"
    """
    The name of a type or group of cells.
    """
    Cell_type_accession = "EDAM_data:2893"
    """
    Accession of a type or group of cells (catalogued in a database).
    """
    Compound_accession = "EDAM_data:2894"
    """
    Accession of an entry from a database of chemicals.
    """
    Drug_accession = "EDAM_data:2895"
    """
    Accession of a drug.
    """
    Toxin_name = "EDAM_data:2896"
    """
    Name of a toxin.
    """
    Toxin_accession = "EDAM_data:2897"
    """
    Accession of a toxin (catalogued in a database).
    """
    Monosaccharide_accession = "EDAM_data:2898"
    """
    Accession of a monosaccharide (catalogued in a database).
    """
    Drug_name = "EDAM_data:2899"
    """
    Common name of a drug.
    """
    Carbohydrate_accession = "EDAM_data:2900"
    """
    Accession of an entry from a database of carbohydrates.
    """
    Molecule_accession = "EDAM_data:2901"
    """
    Accession of a specific molecule (catalogued in a database).
    """
    Data_resource_definition_accession = "EDAM_data:2902"
    """
    Accession of a data definition (catalogued in a database).
    """
    Genome_accession = "EDAM_data:2903"
    """
    An accession of a particular genome (in a database).
    """
    Map_accession = "EDAM_data:2904"
    """
    An accession of a map of a molecular sequence (deposited in a database).
    """
    Lipid_accession = "EDAM_data:2905"
    """
    Accession of an entry from a database of lipids.
    """
    Peptide_ID = "EDAM_data:2906"
    """
    Accession of a peptide deposited in a database.
    """
    Protein_accession = "EDAM_data:2907"
    """
    Accession of a protein deposited in a database.
    """
    Organism_accession = "EDAM_data:2908"
    """
    An accession of annotation on a (group of) organisms (catalogued in a database).
    """
    Organism_name = "EDAM_data:2909"
    """
    The name of an organism (or group of organisms).
    """
    Protein_family_accession = "EDAM_data:2910"
    """
    Accession of a protein family (that is deposited in a database).
    """
    Transcription_factor_accession = "EDAM_data:2911"
    """
    Accession of an entry from a database of transcription factors or binding sites.
    """
    Strain_accession = "EDAM_data:2912"
    """
    Accession number of a strain of an organism variant, typically a plant, virus or bacterium.
    """
    Sequence_features_metadata = "EDAM_data:2914"
    """
    Metadata on sequence features.
    """
    Gramene_identifier = "EDAM_data:2915"
    """
    Identifier of a Gramene database entry.
    """
    DDBJ_accession = "EDAM_data:2916"
    """
    An identifier of an entry from the DDBJ sequence database.
    """
    ConsensusPathDB_identifier = "EDAM_data:2917"
    """
    An identifier of an entity from the ConsensusPathDB database.
    """
    Sequence_report = "EDAM_data:2955"
    """
    An informative report of information about molecular sequence(s), including basic information (metadata), and reports generated from molecular sequence analysis, including positional features and non-positional properties.
    """
    Protein_secondary_structure = "EDAM_data:2956"
    """
    Data concerning the properties or features of one or more protein secondary structures.
    """
    Hopp_and_Woods_plot = "EDAM_data:2957"
    """
    A Hopp and Woods plot of predicted antigenicity of a peptide or protein.
    """
    Image = "EDAM_data:2968"
    """
    Data (typically biological or biomedical) that has been rendered into an image, typically for display on screen.
    """
    Sequence_image = "EDAM_data:2969"
    """
    Image of a molecular sequence, possibly with sequence features or properties shown.
    """
    Protein_hydropathy_data = "EDAM_data:2970"
    """
    A report on protein properties concerning hydropathy.
    """
    Protein_sequence = "EDAM_data:2976"
    """
    One or more protein sequences, possibly with associated annotation.
    """
    Nucleic_acid_sequence = "EDAM_data:2977"
    """
    One or more nucleic acid sequences, possibly with associated annotation.
    """
    Reaction_data = "EDAM_data:2978"
    """
    Data concerning a biochemical reaction, typically data and more general annotation on the kinetics of enzyme-catalysed reaction.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Peptide_property = "EDAM_data:2979"
    """
    Data concerning small peptides.
    """
    Pathway_or_network_report = "EDAM_data:2984"
    """
    An informative report concerning or derived from the analysis of a biological pathway or network, such as a map (diagram) or annotation.
    """
    Nucleic_acid_thermodynamic_data = "EDAM_data:2985"
    """
    A thermodynamic or kinetic property of a nucleic acid molecule.
    """
    Protein_geometry_data = "EDAM_data:2991"
    """
    Geometry data for a protein structure, for example bond lengths, bond angles, torsion angles, chiralities, planaraties etc.
    """
    Protein_structure_image = "EDAM_data:2992"
    """
    An image of protein structure.
    """
    Phylogenetic_character_weights = "EDAM_data:2994"
    """
    Weights for sequence positions or characters in phylogenetic analysis where zero is defined as unweighted.
    """
    Annotation_track = "EDAM_data:3002"
    """
    Annotation of one particular positional feature on a biomolecular (typically genome) sequence, suitable for import and display in a genome browser.
    """
    UniProt_accession = "EDAM_data:3021"
    """
    Accession number of a UniProt (protein sequence) database entry.
    """
    NCBI_genetic_code_ID = "EDAM_data:3022"
    """
    Identifier of a genetic code in the NCBI list of genetic codes.
    """
    Ontology_concept_identifier = "EDAM_data:3025"
    """
    Identifier of a concept in an ontology of biological or bioinformatics concepts and relations.
    """
    Taxonomy = "EDAM_data:3028"
    """
    Data concerning the classification, identification and naming of organisms.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Protein_ID_LEFT_PARENTHESISEMBLSOLIDUSGenBankSOLIDUSDDBJRIGHT_PARENTHESIS = "EDAM_data:3029"
    """
    EMBL/GENBANK/DDBJ coding feature protein identifier, issued by International collaborators.
    This qualifier consists of a stable ID portion (3+5 format with 3 position letters and 5 numbers) plus a version number after the decimal point. When the protein sequence encoded by the CDS changes, only the version number of the /protein_id value is incremented; the stable part of the /protein_id remains unchanged and as a result will permanently be associated with a given protein; this qualifier is valid only on CDS features which translate into a valid protein.
    """
    Sequence_feature_identifier = "EDAM_data:3034"
    """
    Name or other identifier of molecular sequence feature(s).
    """
    Structure_identifier = "EDAM_data:3035"
    """
    An identifier of a molecular tertiary structure, typically an entry from a structure database.
    """
    Matrix_identifier = "EDAM_data:3036"
    """
    An identifier of an array of numerical values, such as a comparison matrix.
    """
    ATC_code = "EDAM_data:3103"
    """
    Unique identifier of a drug conforming to the Anatomical Therapeutic Chemical (ATC) Classification System, a drug classification system controlled by the WHO Collaborating Centre for Drug Statistics Methodology (WHOCC).
    """
    UNII = "EDAM_data:3104"
    """
    A unique, unambiguous, alphanumeric identifier of a chemical substance as catalogued by the Substance Registration System of the Food and Drug Administration (FDA).
    """
    System_metadata = "EDAM_data:3106"
    """
    Metadata concerning the software, hardware or other aspects of a computer system.
    """
    Experimental_measurement = "EDAM_data:3108"
    """
    Raw data such as measurements or other results from laboratory experiments, as generated from laboratory hardware.
    This is a broad data type and is used a placeholder for other, more specific types. It is primarily intended to help navigation of EDAM and would not typically be used for annotation.
    """
    Raw_microarray_data = "EDAM_data:3110"
    """
    Raw data (typically MIAME-compliant) for hybridisations from a microarray experiment.
    Such data as found in Affymetrix CEL or GPR files.
    """
    Processed_microarray_data = "EDAM_data:3111"
    """
    Data generated from processing and analysis of probe set data from a microarray experiment.
    Such data as found in Affymetrix .CHP files or data from other software such as RMA or dChip.
    """
    Gene_expression_matrix = "EDAM_data:3112"
    """
    The final processed (normalised) data for a set of hybridisations in a microarray experiment.
    This combines data from all hybridisations.
    """
    Sample_annotation = "EDAM_data:3113"
    """
    Annotation on a biological sample, for example experimental factors and their values.
    This might include compound and dose in a dose response experiment.
    """
    Microarray_metadata = "EDAM_data:3115"
    """
    Annotation on the array itself used in a microarray experiment.
    This might include gene identifiers, genomic coordinates, probe oligonucleotide sequences etc.
    """
    Microarray_hybridisation_data = "EDAM_data:3117"
    """
    Data concerning the hybridisations measured during a microarray experiment.
    """
    Nucleic_acid_structure_report = "EDAM_data:3128"
    """
    A human-readable collection of information about regions within a nucleic acid sequence which form secondary or tertiary (3D) structures.
    The report may be based on analysis of nucleic acid sequence or structural data, or any annotation or information about specific nucleic acid 3D structure(s) or such structures in general.
    """
    Gene_transcript_report = "EDAM_data:3134"
    """
    An informative report on features of a messenger RNA (mRNA) molecules including precursor RNA, primary (unprocessed) transcript and fully processed molecules. This includes reports on a specific gene transcript, clone or EST.
    This includes 5'untranslated region (5'UTR), coding sequences (CDS), exons, intervening sequences (intron) and 3'untranslated regions (3'UTR).
    """
    Gene_family_report = "EDAM_data:3148"
    """
    A human-readable collection of information about a particular family of genes, typically a set of genes with similar sequence that originate from duplication of a common ancestor gene, or any other classification of nucleic acid sequences or structures that reflects gene structure.
    This includes reports on on gene homologues between species.
    """
    Protein_image = "EDAM_data:3153"
    """
    An image of a protein.
    """
    Sequence_assembly_report = "EDAM_data:3181"
    """
    An informative report about a DNA sequence assembly.
    This might include an overall quality assessment of the assembly and summary statistics including counts, average length and number of bases for reads, matches and non-matches, contigs, reads in pairs etc.
    """
    Genome_index = "EDAM_data:3210"
    """
    An index of a genome sequence.
    Many sequence alignment tasks involving many or very large sequences rely on a precomputed index of the sequence to accelerate the alignment.
    """
    Cytoband_position = "EDAM_data:3236"
    """
    Information might include start and end position in a chromosome sequence, chromosome identifier, name of band and so on.
    The position of a cytogenetic band in a genome.
    """
    Cell_type_ontology_ID = "EDAM_data:3238"
    """
    Cell type ontology concept ID.
    """
    Kinetic_model = "EDAM_data:3241"
    """
    Mathematical model of a network, that contains biochemical kinetics.
    """
    COSMIC_ID = "EDAM_data:3264"
    """
    Identifier of a COSMIC database entry.
    """
    HGMD_ID = "EDAM_data:3265"
    """
    Identifier of a HGMD database entry.
    """
    Sequence_assembly_ID = "EDAM_data:3266"
    """
    Unique identifier of sequence assembly.
    """
    Ensembl_gene_tree_ID = "EDAM_data:3270"
    """
    Unique identifier for a gene tree from the Ensembl database.
    """
    Gene_tree = "EDAM_data:3271"
    """
    A phylogenetic tree that is an estimate of the character's phylogeny.
    """
    Species_tree = "EDAM_data:3272"
    """
    A phylogenetic tree that reflects phylogeny of the taxa from which the characters (used in calculating the tree) were sampled.
    """
    Sample_ID = "EDAM_data:3273"
    """
    Name or other identifier of an entry from a biosample database.
    """
    MGI_accession = "EDAM_data:3274"
    """
    Identifier of an object from the MGI database.
    """
    Phenotype_name = "EDAM_data:3275"
    """
    Name of a phenotype.
    """
    Transition_matrix = "EDAM_data:3354"
    """
    A HMM transition matrix contains the probabilities of switching from one HMM state to another.
    Consider for example an HMM with two states (AT-rich and GC-rich). The transition matrix will hold the probabilities of switching from the AT-rich to the GC-rich state, and vica versa.
    """
    Emission_matrix = "EDAM_data:3355"
    """
    A HMM emission matrix holds the probabilities of choosing the four nucleotides (A, C, G and T) in each of the states of a HMM.
    Consider for example an HMM with two states (AT-rich and GC-rich). The emission matrix holds the probabilities of choosing each of the four nucleotides (A, C, G and T) in the AT-rich state and in the GC-rich state.
    """
    Format_identifier = "EDAM_data:3358"
    """
    An identifier of a data format.
    """
    Raw_image = "EDAM_data:3424"
    """
    Raw biological or biomedical image generated by some experimental technique.
    """
    Carbohydrate_property = "EDAM_data:3425"
    """
    Data concerning the intrinsic physical (e.g. structural) or chemical properties of one, more or all carbohydrates.
    """
    MRI_image = "EDAM_data:3442"
    """
    An imaging technique that uses magnetic fields and radiowaves to form images, typically to investigate the anatomy and physiology of the human body.
    """
    Cell_migration_track_image = "EDAM_data:3449"
    """
    An image from a cell migration track assay.
    """
    Rate_of_association = "EDAM_data:3451"
    """
    Rate of association of a protein with another protein or some other molecule.
    """
    Gene_order = "EDAM_data:3479"
    """
    Multiple gene identifiers in a specific order.
    Such data are often used for genome rearrangement tools and phylogenetic tree labeling.
    """
    Spectrum = "EDAM_data:3483"
    """
    The spectrum of frequencies of electromagnetic radiation emitted from a molecule as a result of some spectroscopy experiment.
    """
    NMR_spectrum = "EDAM_data:3488"
    """
    Spectral information for a molecule from a nuclear magnetic resonance experiment.
    """
    Nucleic_acid_signature = "EDAM_data:3492"
    """
    An informative report about a specific or conserved nucleic acid sequence pattern.
    """
    DNA_sequence = "EDAM_data:3494"
    """
    A DNA sequence.
    """
    RNA_sequence = "EDAM_data:3495"
    """
    An RNA sequence.
    """
    Sequence_variations = "EDAM_data:3498"
    """
    Data on gene sequence variations resulting large-scale genotyping and DNA sequencing projects.
    Variations are stored along with a reference genome.
    """
    Bibliography = "EDAM_data:3505"
    """
    A list of publications such as scientic papers or books.
    """
    Ontology_mapping = "EDAM_data:3509"
    """
    A mapping of supplied textual terms or phrases to ontology concepts (URIs).
    """
    Image_metadata = "EDAM_data:3546"
    """
    Any data concerning a specific biological or biomedical image.
    This can include basic provenance and technical information about the image, scientific annotation and so on.
    """
    Clinical_trial_report = "EDAM_data:3558"
    """
    A human-readable collection of information concerning a clinical trial.
    """
    Reference_sample_report = "EDAM_data:3567"
    """
    A report about a biosample.
    """
    Gene_Expression_Atlas_Experiment_ID = "EDAM_data:3568"
    """
    Accession number of an entry from the Gene Expression Atlas.
    """
    Disease_identifier = "EDAM_data:3667"
    """
    Identifier of an entry from a database of disease.
    """
    Disease_name = "EDAM_data:3668"
    """
    The name of some disease.
    """
    Learning_material = "EDAM_data:3669"
    """
    Learning material is a document or another digital object that is designed for learning (educational, training) purposes.
    """
    Online_course = "EDAM_data:3670"
    """
    A training course available for use on the Web.
    """
    Text = "EDAM_data:3671"
    """
    Any free or plain text, typically for human consumption and in English. Can instantiate also as a textual search query.
    """
    Biodiversity_data = "EDAM_data:3707"
    """
    Machine-readable biodiversity data.
    """
    Biosafety_report = "EDAM_data:3716"
    """
    A human-readable collection of information concerning biosafety data.
    """
    Isolation_report = "EDAM_data:3717"
    """
    A report about any kind of isolation of biological material.
    """
    Pathogenicity_report = "EDAM_data:3718"
    """
    Information about the ability of an organism to cause disease in a corresponding host.
    """
    Biosafety_classification = "EDAM_data:3719"
    """
    Information about the biosafety classification of an organism according to corresponding law.
    """
    Geographic_location = "EDAM_data:3720"
    """
    A report about localisation of the isolaton of biological material e.g. country or coordinates.
    """
    Isolation_source = "EDAM_data:3721"
    """
    A report about any kind of isolation source of biological material e.g. blood, water, soil.
    """
    Physiology_parameter = "EDAM_data:3722"
    """
    Experimentally determined parameter of the physiology of an organism, e.g. substrate spectrum.
    """
    Morphology_parameter = "EDAM_data:3723"
    """
    Experimentally determined parameter of the morphology of an organism, e.g. size & shape.
    """
    Cultivation_parameter = "EDAM_data:3724"
    """
    Experimental determined parameter for the cultivation of an organism.
    """
    Sequencing_metadata_name = "EDAM_data:3732"
    """
    Data concerning a sequencing experiment, that may be specified as an input to some tool.
    """
    Flow_cell_identifier = "EDAM_data:3733"
    """
    A flow cell is used to immobilise, amplify and sequence millions of molecules at once. In Illumina machines, a flowcell is composed of 8 "lanes" which allows 8 experiments in a single analysis.
    An identifier of a flow cell of a sequencing machine.
    """
    Lane_identifier = "EDAM_data:3734"
    """
    An identifier of a lane within a flow cell of a sequencing machine, within which millions of sequences are immobilised, amplified and sequenced.
    """
    Run_number = "EDAM_data:3735"
    """
    A number corresponding to the number of an analysis performed by a sequencing machine. For example, if it's the 13th analysis, the run is 13.
    """
    Ecological_data = "EDAM_data:3736"
    """
    Data concerning ecology; for example measurements and reports from the study of interactions among organisms and their environment.
    This is a broad data type and is used a placeholder for other, more specific types.
    """
    Alpha_diversity_data = "EDAM_data:3737"
    """
    The mean species diversity in sites or habitats at a local scale.
    """
    Beta_diversity_data = "EDAM_data:3738"
    """
    The ratio between regional and local species diversity.
    """
    Gamma_diversity_data = "EDAM_data:3739"
    """
    The total species diversity in a landscape.
    """
    Ordination_plot = "EDAM_data:3743"
    """
    A plot in which community data (e.g. species abundance data) is summarised. Similar species and samples are plotted close together, and dissimilar species and samples are plotted placed far apart.
    """
    Over_representation_data = "EDAM_data:3753"
    """
    A ranked list of categories (usually ontology concepts), each associated with a statistical metric of over-/under-representation within the studied data.
    """
    GO_term_enrichment_data = "EDAM_data:3754"
    """
    A ranked list of Gene Ontology concepts, each associated with a p-value, concerning or derived from the analysis of e.g. a set of genes or proteins.
    """
    Localisation_score = "EDAM_data:3756"
    """
    Score for localization of one or more post-translational modifications in peptide sequence measured by mass spectrometry.
    """
    Unimod_ID = "EDAM_data:3757"
    """
    Identifier of a protein modification catalogued in the Unimod database.
    """
    ProteomeXchange_ID = "EDAM_data:3759"
    """
    Identifier for mass spectrometry proteomics data in the proteomexchange.org repository.
    """
    Clustered_expression_profiles = "EDAM_data:3768"
    """
    Groupings of expression profiles according to a clustering algorithm.
    """
    BRENDA_ontology_concept_ID = "EDAM_data:3769"
    """
    An identifier of a concept from the BRENDA ontology.
    """
    Annotated_text = "EDAM_data:3779"
    """
    A text (such as a scientific article), annotated with notes, data and metadata, such as recognised entities, concepts, and their relations.
    """
    Query_script = "EDAM_data:3786"
    """
    A structured query, in form of a script, that defines a database search task.
    """
    number_3D_EM_Map = "EDAM_data:3805"
    """
    Structural 3D model (volume map) from electron microscopy.
    """
    number_3D_EM_Mask = "EDAM_data:3806"
    """
    Annotation on a structural 3D EM Map from electron microscopy. This might include one or several locations in the map of the known features of a particular macromolecule.
    """
    EM_Movie = "EDAM_data:3807"
    """
    Raw DDD movie acquisition from electron microscopy.
    """
    EM_Micrograph = "EDAM_data:3808"
    """
    Raw acquisition from electron microscopy or average of an aligned DDD movie.
    """
    Molecular_simulation_data = "EDAM_data:3842"
    """
    Data coming from molecular simulations, computer "experiments" on model molecules.
    Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic).
    """
    RNA_central_ID = "EDAM_data:3856"
    """
    Identifier of an entry from the RNA central database of annotated human miRNAs.
    There are canonical and taxon-specific forms of RNAcentral ID. Canonical form e.g. urs_9or10digits identifies an RNA sequence (within the RNA central database) which may appear in multiple sequences. Taxon-specific form identifies a sequence in the specific taxon (e.g. urs_9or10digits_taxonID).
    """
    Electronic_health_record = "EDAM_data:3861"
    """
    A human-readable systematic collection of patient (or population) health information in a digital format.
    """
    Simulation = "EDAM_data:3869"
    """
    Data coming from molecular simulations, computer "experiments" on model molecules. Typically formed by two separated but indivisible pieces of information: topology data (static) and trajectory data (dynamic).
    """
    Trajectory_data = "EDAM_data:3870"
    """
    Dynamic information of a structure molecular system coming from a molecular simulation: XYZ 3D coordinates (sometimes with their associated velocities) for every atom along time.
    """
    Forcefield_parameters = "EDAM_data:3871"
    """
    Force field parameters: charges, masses, radii, bond lengths, bond dihedrals, etc. define the structural molecular system, and are essential for the proper description and simulation of a molecular system.
    """
    Topology_data = "EDAM_data:3872"
    """
    Static information of a structure molecular system that is needed for a molecular simulation: the list of atoms, their non-bonded parameters for Van der Waals and electrostatic interactions, and the complete connectivity in terms of bonds, angles and dihedrals.
    """
    Histogram = "EDAM_data:3905"
    """
    Visualization of distribution of quantitative data, e.g. expression data, by histograms, violin plots and density plots.
    """
    Quality_control_report = "EDAM_data:3914"
    """
    Report of the quality control review that was made of factors involved in a procedure.
    """
    Count_matrix = "EDAM_data:3917"
    """
    A table of unnormalized values representing summarised read counts per genomic region (e.g. gene, transcript, peak).
    """
    DNA_structure_alignment = "EDAM_data:3924"
    """
    Alignment (superimposition) of DNA tertiary (3D) structures.
    """
    Q_value = "EDAM_data:3932"
    """
    A score derived from the P-value to ensure correction for multiple tests. The Q-value provides an estimate of the positive False Discovery Rate (pFDR), i.e. the rate of false positives among all the cases reported positive: pFDR = FP / (FP + TP).
    Q-values are widely used in high-throughput data analysis (e.g. detection of differentially expressed genes from transcriptome data).
    """
    Profile_HMM = "EDAM_data:3949"
    """
    A profile HMM is a variant of a Hidden Markov model that is derived specifically from a set of (aligned) biological sequences. Profile HMMs provide the basis for a position-specific scoring system, which can be used to align sequences and search databases for related sequences.
    """
    Pathway_ID_LEFT_PARENTHESISWikiPathwaysRIGHT_PARENTHESIS = "EDAM_data:3952"
    """
    Identifier of a pathway from the WikiPathways pathway database.
    """
    Pathway_overrepresentation_data = "EDAM_data:3953"
    """
    A ranked list of pathways, each associated with z-score, p-value or similar, concerning or derived from the analysis of e.g. a set of genes or proteins.
    """
    ORCID_Identifier = "EDAM_data:4022"
    """
    Identifier of a researcher registered with the ORCID database. Used to identify author IDs.
    """
    Data_management_plan = "EDAM_data:4040"
    """
    Data management plan is a document describing the data management of a project or an organisation, including acquisition, reuse, structure, processing, storage, documentation, sharing, and preservation of data. This may include budgeting for these operations.
    """


class EnumFileHashType(str, Enum):
    """
    Types of file hashes supported.
    """
    MD5 = "md5"
    ETag = "etag"
    SHA_1 = "sha1"



class RequiredClass(ConfiguredBaseModel):
    """
    This is a placeholder class to satisfy the LinkML requirement of at least one class and is not otherwise used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'from_schema': 'https://includedcc.org/cam-expanded-enums'})

    id: Optional[str] = Field(default=None, description="""Unique identifier""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    full_name: Optional[str] = Field(default=None, description="""Full name""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    aliases: Optional[str] = Field(default=None, description="""Aliases""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    phone: Optional[str] = Field(default=None, description="""Phone number""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })
    age: Optional[str] = Field(default=None, description="""Age""", json_schema_extra = { "linkml_meta": {'domain_of': ['RequiredClass']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
RequiredClass.model_rebuild()
