from flask import Blueprint, render_template, request, redirect, url_for, session
from .services.doctor_service import get_doctors, get_doctor_by_id
from .services.slot_service import generate_slots
from flask import current_app

main_bp = Blueprint("main", __name__)

# Home Page - Doctor List
@main_bp.route("/")
def home():
    current_app.logger.info("Doctor page accessed")
    doctors = get_doctors()
    return render_template("home.html", doctors=doctors)

# Doctor Details + Slots
@main_bp.route("/doctor/<int:doctor_id>")
def doctor_details(doctor_id):
    doctor = get_doctor_by_id(doctor_id)

    if not doctor:
        return "Doctor not found", 404

    slots = generate_slots(
        doctor["availability"]["start"],
        doctor["availability"]["end"]
    )

    session["doctor"] = doctor        # store doctor in session
    return render_template("doctor_details.html", doctor=doctor, slots=slots)

# Patient Form Page
@main_bp.route("/book", methods=["GET", "POST"])
def book():
    if request.method == "GET":
        slot = request.args.get("slot")

        if not slot or "doctor" not in session:
            return redirect(url_for("main.home"))

        session["slot"] = slot
        return render_template("patient_form.html")

    # POST request - form submit
    name = request.form.get("name")
    age = request.form.get("age")
    phone = request.form.get("phone")

    # Validation basic
    if not name or not age or not phone:
        error = "All fields are required"
        return render_template("patient_form.html", error=error)

    session["patient"] = {
        "name": name,
        "age": age,
        "phone": phone
    }

    return redirect(url_for("main.confirm"))

# Confirm Page
@main_bp.route("/confirm")
def confirm():
    if "doctor" not in session or "slot" not in session or "patient" not in session:
        return redirect(url_for("main.home"))

    return render_template(
        "confirm.html",
        doctor=session["doctor"],
        slot=session["slot"],
        patient=session["patient"]
    )
