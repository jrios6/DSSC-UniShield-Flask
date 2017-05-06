
item1 = dict()
item1["url"] = "../static/img/term_life.jpeg"
item1["title"] = "Term Life Insurance"
item1["htitle"] = "#Term Life Insurance"
item1["summary"] = "Term Life Insurance pays out the sum assured in the event of death, terminal illness or total and permanent disability (TPD before age 65) during the term of the policy."
item1["coverage"] = "$3000 or $1500 sum assured"
item1["pricing"] = "Starting from $30/yr"
item1["recommend"] = "Recommended because of dependents"

item2 = dict()
item2["url"] = "../static/img/personal_accident.jpeg"
item2["title"] = "Personal Accident Insurance"
item2["htitle"] = "#Personal Accident Insurance"
item2["summary"] = "The personal accident plan gives you comprehensive financial protection in times of needs. The policy includes accidental death and accidental permanent disablement cover, a lump sum bereavement grant, as well as hospitalisation allowance. "
item2["coverage"] = "$3000 or $1500 sum assured"
item2["pricing"] = "Starting from $40/yr"
item2["recommend"] = "Recommended because of past history of accidents"

item3 = dict()
item3["url"] = "../static/img/mosquito.jpeg"
item3["title"] = "Mosquito Insurance"
item3["htitle"] = "#Mosquito Insurance"
item3["summary"] = "The mosquito insurance plan gives you protection against dengue fever, Zika fever, Chikungunya fever, malaria & yellow fever."
item3["coverage"] = "$3000 or $1500 sum assured"
item3["pricing"] = "Starting from $15/yr"
item3["recommend"] = "Recommended because of Dengue Danger Level of home address"

item4 = dict()
item4["url"] = "../static/img/mosquito.jpeg"
item4["title"] = "Hospitalisation Insurance"
item4["htitle"] = "#Hospitalisation Insurance"
item4["summary"] = "The hospitalisastion insurance keeps you protected so you don't have to worry about anything! "
item4["coverage"] = "$5000 or $7500 sum assured"
item4["pricing"] = "Starting from $18/yr"
item4["recommend"] = "Recommended because of recent medical history"

item5 = dict()
item5["url"] = "../static/img/bike.png"
item5["title"] = "Disability Insurance"
item5["htitle"] = "#Disability Insurance"
item5["summary"] = "The disability insurance covers you in every possible situation "
item5["coverage"] = "$7500 or $10000 sum assured"
item5["pricing"] = "Starting from $20/yr"
item5["recommend"] = "Recommended because prevention is always better than cure"

RECOMMENDED_POLICIES = [item1, item2, item3]
RECOMMENDED_POLICIES1 = [item4, item5]


cp1 = dict()
cp1["id"] = "PA1"
cp1["id2"] = "PA2"
cp1["title"] = "Death"
cp1["url"] = "../static/img/death.png"
cp1["status"] = "Covered"
cp1["coverage-you"] = "$32,000"
cp1["coverage-others"] = "$32,000"

cp2 = dict()
cp2["id"] = "D1"
cp2["id2"] = "D2"
cp2["title"] = "Personal Accident"
cp2["url"] = "../static/img/accident.png"
cp2["status"] = "Covered"
cp2["coverage-you"] = "$18,000"
cp2["coverage-others"] = "$18,500"

cp3 = dict()
cp3["id"] = "TL1"
cp3["id2"] = "TL2"
cp3["title"] = "Permanent Disability"
cp3["url"] = "../static/img/disability.png"
cp3["status"] = "Covered"
cp3["coverage-you"] = "$40,000"
cp3["coverage-others"] = "$40,000"

cp4 = dict()
cp4["id"] = "ML1"
cp4["id2"] = "ML2"
cp4["title"] = "Hospitalisation"
cp4["url"] = "../static/img/hospital.png"
cp4["status"] = "Covered"
cp4["coverage-you"] = "$3,000"
cp4["coverage-others"] = "$2,500"

cp5 = dict()
cp5["id"] = "AL1"
cp5["id2"] = "AL2"
cp5["title"] = "Temporary Disability"
cp5["url"] = "../static/img/broken.png"
cp5["status"] = "Undercovered"
cp5["coverage-you"] = "$2,000"
cp5["coverage-others"] = "$5,000"

cp6 = dict()
cp6["id"] = "BL1"
cp6["id2"] = "BL2"
cp6["title"] = "Dengue Fever"
cp6["url"] = "../static/img/mozzy.png"
cp6["status"] = "Uncovered"
cp6["coverage-you"] = "None"
cp6["coverage-others"] = "$1,000"

cp7 = dict()
cp7["id"] = "CL1"
cp7["id2"] = "CL2"
cp7["title"] = "Mobility"
cp7["url"] = "../static/img/mobility.png"
cp7["status"] = "Uncovered"
cp7["coverage-you"] = "None"
cp7["coverage-others"] = "$2,000"


CURRENT_POLICIES = [cp1, cp2, cp3, cp4, cp5, cp6, cp7]
