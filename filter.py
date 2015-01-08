import json
#parameters: list of new loans, list of filter criteria
#returns list of loan ids to buy

#criteria format: "attribute","comparator","value"
#comparator: <, >, ==, for numbers, "in" for strings
def applyCriteria(newLoans,criteria):
    goodLoans = []
    for loan in newLoans:
        continueFilterBool = true
        for filter in criteria:
            attribute = filter[0]
            comparator = filter[1]
            value = filter[2]
            loanValue = loan[attribute]
            if comparator == "<":
                if !(loanValue < value):
                    continueFilterBool = false
            else if comparator == ">":
                if !(loanValue > value):
                    continueFilterBool = false
            else if comparator == "==":
                if !(loanValue == value):
                    continueFilterValue = false
            else if comparator == "in":
                if loanValue not in value:
                    continueFilterValue = false
            if !continueFilterBool:
                break;
        if continueFilterBool:
            goodLoans.append(loan["id"])
    return goodLoans
