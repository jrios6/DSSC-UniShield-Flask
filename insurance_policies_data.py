
item1 = dict()
item1["url"] = "../static/img/term_life.jpeg"
item1["title"] = "Term Life Insurance"
item1["htitle"] = "#Term Life Insurance"
item1["summary"] = "Term pays out the sum assured in the event of death, terminal illness or total and permanent disability (TPD before age 65) during the term of the policy."
item1["coverage"] = "$3000 or $1500 sum assured"
item1["pricing"] = "Starting from $31/yr"

item2 = dict()
item2["url"] = "../static/img/personal_accident.jpeg"
item2["title"] = "Personal Accident Insurance"
item2["htitle"] = "#Personal Accident Insurance"
item2["summary"] = "Personal accident plans gives you comprehensive financial protection in times of needs. The policy includes accidental death and accidental permanent disablement cover, a lump sum bereavement grant, as well as hospitalisation allowance. "
item2["coverage"] = "$3000 or $1500 sum assured"
item2["pricing"] = "Starting from $31/yr"

item3 = dict()
item3["url"] = "../static/img/mosquito.jpeg"
item3["title"] = "Mosquito Insurance"
item3["htitle"] = "#Mosquito Insurance"
item3["summary"] = "Protection against Dengue fever, Zika fever, Chikungunya fever, Malaria & Yellow fever"
item3["coverage"] = "$3000 or $1500 sum assured"
item3["pricing"] = "Starting from $31/yr"

RECOMMENDED_POLICIES = [item1, item2, item3]


cp1 = dict()
cp1["id"] = "PA1"
cp1["id2"] = "PA2"
cp1["title"] = "Personal Accident"
cp1["status"] = "Covered"
cp1["coverage-you"] = "$12000"
cp1["coverage-others"] = "$40000"

cp2 = dict()
cp2["id"] = "D1"
cp2["id2"] = "D2"
cp2["title"] = "Death"
cp2["status"] = "Covered"
cp2["coverage-you"] = "$4000"
cp2["coverage-others"] = "$19000"

cp3 = dict()
cp3["id"] = "TL1"
cp3["id2"] = "TL2"
cp3["title"] = "Term Life"
cp3["status"] = "Covered"
cp3["coverage-you"] = "$5000"
cp3["coverage-others"] = "$60000"

cp4 = dict()
cp4["id"] = "ML1"
cp4["id2"] = "ML2"
cp4["title"] = "Mosquito"
cp4["status"] = "Uncovered"
cp4["coverage-you"] = "$3000"
cp4["coverage-others"] = "$1000"


CURRENT_POLICIES = [cp1, cp2, cp3, cp4]
