from docxtpl import DocxTemplate
from datetime import datetime
from test import user, address



# Load your Jinja2-compatible Word document
doc = DocxTemplate(r"C:\Users\tripp\PycharmProjects\PythonProject\.venv\SingleEP_jinja_template1.docx")


# Define the test data context
context = {
    "PrimaryNameSigningUse": "test signer",
    "PrimaryNameFull": "Johnathan A. Doe",
    "PrimaryNameLast": "Doe",
    "PrimaryGender": "Mr.",
    "EPType": {
        "StandardWillPackage": True,
        "Trust": True,
        "POWill": False
    },
    "TrustName": "The Doe Family Trust",
    "SigningDate": datetime.today().strftime("%B %d, %Y"),
    "ResponsibleAttorney": {
        "Name": "Jane Lawyer",
        "FirmName": "Lawyer & Co.",
        "Email": "jane.lawyer@lawyerco.com"
    },
    "OfficeCityandCounty": {
        "SigningCity": "Honolulu"
    },
    "Offices":
        {
        "Maui": "123 Trust Way, Suite 100, Honolulu, HI",
        "HNL":"test",
        "BigIsland": "test"},
    "PRTitle": "The Doe Family Trust",
    "TrustStateLaw": "Hawaii",
    "TrustFundLifeInsurance": {
        "Primary"
    },
    "TrustFundRetirement": {
        "Primary": True,
        "Contingent": True
    },
    "TrustProtector": True,
    "PrimaryGST": True
}

# Render and save the document
doc.render(context)
doc.save("SingleEP_rendered_test.docx")
print("Document generated.")
