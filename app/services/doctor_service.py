doctors = [
    {
        "id": 1,
        "name": "Dr. Rahul Sharma",
        "specialization": "Cardiologist",
        "experience": "10 Years",
        "availability": {
            "start": "10:00",
            "end": "16:00"
        }
    },
    {
        "id": 2,
        "name": "Dr. Priya Mehta",
        "specialization": "Dermatologist",
        "experience": "7 Years",
        "availability": {
            "start": "11:00",
            "end": "15:00"
        }
    }
]

def get_doctors():
    return doctors

def get_doctor_by_id(doc_id):
    return next((d for d in doctors if d["id"] == doc_id), None)
