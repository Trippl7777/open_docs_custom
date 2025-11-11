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
        "Grantor",
        "Settlor",
        "Trustor"
    },
    "TrustDate": "January 1, 2025",
    "SigningDate": datetime.today().strftime("%B %d, %Y"),
    "TrustStateLaw": {
        "Hawaii",
        "California",
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
        "One",
        "Two",
        "Three",
        "Four",
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
        "Isaiah",
        "David",
        "Laurie"
    },
    "SigningNotaryExpiration": {
        "Isaiah": "Aug. 25, 2028",
        "David": "Jan. 1, 2028",
        "Laurie": "Jan 1, 2028"
    },



}

# Render and save the document
doc.render(context)
doc.save("SingleEP_rendered_test.docx")
print("Document generated.")
