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
    "PrimaryMailingAddressSame": "123 Main Street",
    "PrimaryMailingAddressStreet1": "123 Main Street",
    "PrimaryMailingAddressStreet2": "123 Main Street",
    "PrimaryMailingAddressAptNo": "Apt. 10",
    "PrimaryMailingAddressCity": "Honolulu",
    "PrimaryMailingAddressState": {
        "Full": "Hawaii",
        "Abbreviated": "HI"
    },
    "PrimaryMailingAddressZip": "96813",

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
    "SigningWitness1Address": "345 Queen Street",
    "SigningWitness2Address": "345 Queen Street",

    "ApplicableStateLaw": {
        "Hawaii",
        "California",
    },
    #This TrustType needs a lot of work...
    "TrustType": {
        "Disclaimer",
        "Clayton",
        "A-B",
        "A-B-C",
        "Skip Spouse",
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
    "TrustSpecialNeedsDialog": "Text...",

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
