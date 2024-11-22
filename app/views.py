import csv
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from app.models import Business, Symptom
from app.database import get_db

router = APIRouter()

#route decoder 
@router.post("/import")
# handles file uploads & a SQLAlchemy session (db).
async def import_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    #check if the input file is csv or no
    if not file.filename.endswith(".csv"):
        raise HTTPException(status_code=400, detail="The file must be a CSV.")

    #reading & parsing csv
    content = await file.read()
    #here it is decodingg to string type
    data = content.decode("utf-8").splitlines()
    #comparing as key & value pairs
    reader = csv.DictReader(data)

    #loop through each row in the CSV
    for row in reader:
        #extractdata from the row
        business_id = int(row["Business ID"])
        business_name = row["Business Name"]
        symptom_code = row["Symptom Code"]
        symptom_name = row["Symptom Name"]
        #having 0 or 1
        symptom_diagnostic = row["Symptom Diagnostic"].strip().lower() in ("true", "yes")

        #checking if the business already exists
        business = db.query(Business).filter(Business.id == business_id).first()
        if not business:
            #creating a new business if it doesn't exist
            business = Business(id=business_id, name=business_name)
            db.add(business)
            db.commit()
            db.refresh(business)

        #adding the symptom
        symptom = Symptom(
            code=symptom_code,
            name=symptom_name,
            diagnostic=symptom_diagnostic,
            business_id=business.id,
        )
        db.add(symptom)
        db.commit()
    return {"message": "Data imported successfully"}


@router.get("/data")
def get_data(
    business_id: int = None,
    diagnostic: bool = None,
    db: Session = Depends(get_db)
):
    query = db.query(Business, Symptom).join(Symptom, Business.id == Symptom.business_id)
    
    #applying filters
    if business_id:
        query = query.filter(Business.id == business_id)
    if diagnostic is not None:
        query = query.filter(Symptom.diagnostic == diagnostic)

    result = []
    for business, symptom in query.all():
        result.append({
            "Business ID": business.id,
            "Business Name": business.name,
            "Symptom Code": symptom.code,
            "Symptom Name": symptom.name,
            "Symptom Diagnostic": symptom.diagnostic
        })

    return result
