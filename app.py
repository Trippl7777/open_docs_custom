from flask import Flask, render_template, request, send_file, redirect, url_for
from docxtpl import DocxTemplate
from datetime import datetime
from io import BytesIO

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/generate", methods=["POST"])
def generate():
    form = request.form

    context = {
        "PrimaryNameSigningUse": form.get("PrimaryNameSigningUse"),
        "PrimaryNameFull": form.get("PrimaryNameFull"),
        "PrimaryNameLast": form.get("PrimaryNameLast"),
        "PrimaryGender": form.get("PrimaryGender"),
        "EPType": {
            "StandardWillPackage": "StandardWillPackage" in form,
            "Trust": "Trust" in form,
            "POWill": "POWill" in form
        },
        "TrustName": form.get("TrustName"),
        "SigningDate": form.get("SigningDate") or datetime.today().strftime("%B %d, %Y"),
        "ResponsibleAttorney": {
            "Name": form.get("AttorneyName"),
            "FirmName": form.get("FirmName"),
            "Email": form.get("AttorneyEmail")
        },
        "OfficeCityandCounty": {
            "SigningCity": form.get("SigningCity")
        },
        "Offices": {
            "Maui": form.get("OfficeMaui"),
            "HNL": form.get("OfficeHNL"),
            "BigIsland": form.get("OfficeBigIsland")
        },
        "PRTitle": form.get("PRTitle"),
        "TrustStateLaw": form.get("TrustStateLaw"),
        "TrustFundLifeInsurance": {"Primary"},
        "TrustFundRetirement": {
            "Primary": "RetirementPrimary" in form,
            "Contingent": "RetirementContingent" in form
        },
        "TrustProtector": "TrustProtector" in form,
        "PrimaryGST": "PrimaryGST" in form
    }

    doc = DocxTemplate("SingleEP_jinja_template1.docx")
    doc.render(context)

    output_stream = BytesIO()
    doc.save(output_stream)
    output_stream.seek(0)

    return send_file(
        output_stream,
        as_attachment=True,
        download_name=f"{context['PrimaryNameLast'] or 'Document'}_rendered.docx",
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    )

if __name__ == "__main__":
    app.run(debug=True)
