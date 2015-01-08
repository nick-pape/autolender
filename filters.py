ACTIVE_FILTERS = [sample]

sample = [
	("grade","in",["C","D","E","F","G"]),
	("inqLast6Mths","==",0),
	("annualInc",">=",75000),
	("purpose","in",[	"DEBT_CONSOLIDATION",
						"HOME_IMPROVEMENT",
						"MOVING"])
]