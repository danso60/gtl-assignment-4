from app import db, CountryHealthReport

db.create_all()

Ghana = CountryHealthReport('Ghana',12000,	11000,	400,600)
Egypt = CountryHealthReport('Egypt',13300,	12000,	300,	1000)
South_Africa = CountryHealthReport('South Africa',20000,15000,500, 4500)
db.session.add_all([Ghana,Egypt, South_Africa])

db.session.commit()
