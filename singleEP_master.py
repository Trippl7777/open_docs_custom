from msilib.schema import Class

from docxtpl import DocxTemplate
from datetime import datetime

# Load your Jinja2-compatible Word document
doc = DocxTemplate(r"SingleEP_jinja_template1.docx")


# Define the test data context
context = {
    #Client Name Section
    "PrimaryNameSigningUse": "test signer",
    "PrimaryNameFull": "Johnathan A. Doe",
    "PrimaryNameLast": "Doe",
    "PrimaryGender": {
            "Mr.",
            "Mrs.",
            "They"
    },
    #Attorney Name Section
    "ResponsibleAttorney": {
        "Name": "Jane Lawyer",
        "Initials": "IAC",
        "FirmName": "Lawyer & Co.",
        "Email": "jane.lawyer@lawyerco.com"
    },
    #Address Section
    "OfficeCityandCounty": {
        "SigningCity": "Honolulu",
        "SigningState": "Hawaii"
    },
    "OfficeAddressCenter": {
        "Honolulu": "123 Trust Way, Suite 100, Honolulu, HI",
        "Maui": "123 Trust Way, Suite 100, Wailuku, HI",
        "Kauai": "123 Trust Way, Suite 100, Lihue, HI",
        "Hilo": "123 Trust Way, Suite 100, Hilo, HI",
        "Kona": "123 Trust Way, Suite 100, Kona, HI"
    },
    "PrimaryMailingAddress": {
        "PrimaryMailingAddressStreet1": "123 Main Street",
        "PrimaryMailingAddressStreet2": "123 Main Street",
        "PrimaryMailingAddressAptNo": "Apt. 10",
        "PrimaryMailingAddressCity": "Honolulu",
        "PrimaryMailingAddressState": {
                "PrimaryMailingAddressStateFull": "Hawaii",
                "PrimaryMailingAddressStateAbbreviated": "HI"
        },
        "PrimaryMailingAddressZip": "96813",
    },

    #Trust Details Section
    "EPType": {
        "StandardWillPackage": True,
        "Trust": True,
        "POWill": False
    },
    "TrustName": "The Doe Family Trust",
    "TrusteeNameType": {
        "Grantor": "Grantor",
        "Settlor": "Settlor",
        "Trustor": "Trustor",
    },
    "TrustDate": datetime.today().strftime("%B %d, %Y"),
    "SigningDate": datetime.today().strftime("%B %d, %Y"),
    "SigningWitness1": "Witness 1",
    "SigningWitness2": "Witness 2",
    "SigningWitness1Address": {
        "SigningWitness1street1": "123 Main St",
        "SigningWitness1street2": "123 Main St",
        "SigningWitness1AptNo": "Apt. 10",
        "SigningWitness1city": "Honolulu",
        "SigningWitness1state": "HI",
        "SigningWitness1zip": "96815"
    },
    "SigningWitness2Address": {
        "SigningWitness2street": "123 Main St",
        "SigningWitness2street2": "123 Main St",
        "SigningWitness2AptNo": "Apt. 10",
        "SigningWitness2city": "Honolulu",
        "SigningWitness2state": "HI",
        "SigningWitness2zip": "96815"
    },
    "ApplicableStateLaw": {
        "Hawaii",
        "California",
    },
    "TrustType": {
        "Disclaimer": {
            "Yes": True,
            "No": False,
        },
        "Clayton": {
            "Yes": True,
            "No": False,
        },
        "A-B": {
            "Yes": True,
            "No": False,
        },
        "A-B-C": {
            "Yes": True,
            "No": False,
        },
        "Skip Spouse": {
            "Yes": True,
            "No": False,
        },
    },
    "PRTitle": "The Doe Family Trust",
    "TrustFundLifeInsurance": {
        "Primary"
    },
    "TrustFundRetirement": {
        "Primary": True,
        "Contingent": True
    },
    "TrustProtector": True,
    "PrimaryGST": True,
    "TrustorIsSoleTrustee": {
        "Yes": True,
        "No": False,
    },
    "TrustAmendment": {
        "Yes": True,
        "No": False,
    },
    "TrustAmendmentNumber": {
        "One": "One",
        "Two": "Two",
        "Three": "Three",
    },
    "PrimaryGiftOfCash": {
        "Yes": True,
        "No": False,
    },
    "PrimaryGiftOfCashDialog": "Text...",
    "PrimaryRightToReside": {
        "Yes": True,
        "No": False,
    },
    "PrimaryRightToResideDialog": "Text...",
    "PrimaryGiftOfRealProperty": {
        "Yes": True,
        "No": False,
    },
    "PrimaryGiftOfRealPropertyDialog": "Text...",
    "PrimaryGiftOfOtherProperty": {
        "Yes": True,
        "No": False,
    },
    "PrimaryGiftOfOtherPropertyDialog": "Text...",
    "TrustSpecialNeeds": {
        "Yes": True,
        "No": False,
    },
    "TrustSpecialNeedsDialog": {
        "Yes": True,
        "No": False,
    },
    "IntentionallyOmitBeneficiary": {
        "Yes": True,
        "No": False,
    },
    "ContinuingTrust": {
        "Yes": True,
        "No": False,
    },
    "GST": {
        "Yes": True,
        "No": False,
    },
    "5and5Power": {
        "Yes": True,
        "No": False,
    },
    "TrustPrimaryBeneficiaryLifeInsurance": {
        "Yes": True,
        "No": False,
    },
    "TrustPrimaryBeneficiaryRetirement": {
        "Yes": True,
        "No": False,
    },
    "TrustContingentBeneficiaryRetirement": {
        "Yes": True,
        "No": False,
    },
    "RetirementAccumulationTrust": {
        "Yes": True,
        "No": False,
    },

    #Special Trust Terms
    "DrugAbuseTesting": {
        "Yes": True,
        "No": False,
    },
    "DivorceProtection": {
        "Yes": True,
        "No": False,
    },

    #Special Trust Types
    "PetTrust": {
        "Yes": True,
        "No": False,
    },
    "SpecialNeedsTrust": {
        "Yes": True,
        "No": False,
    },
    "GunTrust": {
        "Yes": True,
        "No": False,
    },
    "QDOTrust": {
        "Yes": True,
        "No": False,
    },
    "TrusteeSellAllRealProperty": {
        "Yes": True,
        "No": False,
    },
    "TrusteeSellResidenceOnly": {
        "Yes": True,
        "No": False,
    },
    "RightToReside": {
        "Yes": True,
        "No": False,
    },
    "RealPropertyMaintanceFund": {
        "exists": True,
        "percent": 95
    },

    #Children Section
    "DeceasedChildren": {
        "Yes": True,
        "No": False,
    },
    "NumberOfChildren": {
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
    },

    #Notary Section
    "SigningNotary": {
        "Isaiah Cureton": "Isaiah Cureton",
        "David Bernstein": "David Bernstein",
        "Laurie Cheu": "Laurie Cheu",
    },
    "SigningNotaryExpiration": {
        "Isaiah": "Notary Expires: Aug. 25, 2028",
        "David": "Notary Expires: Jan. 1, 2028",
        "Laurie": "Notary Expires: Jan 1, 2028"
    },
    "SigningNotaryState": {
        "Hawaii": "State of Hawaii",
        "California": "State of California",
    },

    #Important People Section
    "ImportantPeople": {
        "ImportantPerson1": "Jon Doe1",
        "ImportantPerson2": "Jon Doe2",
        "ImportantPerson3": "Jon Doe3",
        "ImportantPerson4": "Jon Doe4",
        "ImportantPerson5": "Jon Doe5",
        "ImportantPerson6": "Jon Doe6",
        "ImportantPerson7": "Jon Doe7",
    },
    "ImportantPeopleRelationship": {
        "Me": "Me",
        "Spouse/Partner": "Spouse/Partner",
        "JointChild": "Joint Child of me and my Spouse/Partner",
        "MySeperateChild": "My Seperate Child",
        "StepOrFosterChild": "My Step/Foster Child",
        "Grandchild": "Grandchild",
        "Parent": "Parent",
        "Grandparent": "Grandparent",
        "GreatGrandparent": "Great Grandparent",
        "Sibling": "Sibling",
        "Cousin": "Cousin",
        "Aunt": "Aunt",
        "Uncle": "Uncle",
        "NeiceOrNephew": "Neice/Nephew",
        "Oranization": "Oranization",
        "Other": "?",
    },
    "ImportantPeopleLiving?": {
        "Yes": True,
        "No": False,
    },

    #Fee's Section
    "FeeRetainer": "$0.00",
    "FeeTotal": "$0.00",



}

# Render and save the document
doc.render(context)
doc.save("SingleEP_rendered_test.docx")
print("Document generated.")
