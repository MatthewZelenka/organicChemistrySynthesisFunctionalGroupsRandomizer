import random

organicsList = {
    "alkane": 50,
    "haloalkane": 68,
    "alkene": 70,
    "dihaloakane": 40,
    "primary alcohol": 40,
    "secondary alcohol": 40,
    "ketone": 40,
    "aldehyde": 40,
    "carboxylic acid": 40,
    "ester": 40,
    "amide": 40,
    "nitril": 40,
    "ether": 40,
    "primary amine": 40,
    "secondary amine": 40,
}

startingOrganicsWithWeights = { # all weights should add to 100. alkane 50% of the time rest are divided equally
    "alkane": 50,
    "haloalkane": 50/11,
    "alkene": 50/11,
    "primary alcohol": 50/11,
    "secondary alcohol": 50/11,
    "ketone": 50/11,
    "aldehyde": 50/11,
    "carboxylic acid": 50/11,
    "ester": 50/11,
    "amide": 50/11,
    "ether": 50/11,
    "primary amine": 50/11,
}

endingOrganicsWithWeights = { # all weights should add to 100. alkane 1% of the time rest are divided equally
    "alkane": 1,
    "haloalkane": 9,
    "alkene": 9,
    "dihaloakane": 9,
    "primary alcohol": 9,
    "secondary alcohol": 9,
    "ketone": 9,
    "aldehyde": 9,
    "carboxylic acid": 9,
    "ester": 9,
    "amide": 9,
    "nitril": 9,
    "ether": 9,
    "primary amine": 9,
    "secondary amine": 9,
}

while True:
    Starting = ""
    Ending = ""
    while Starting == Ending:
        Starting = random.choices(list(startingOrganicsWithWeights), weights=list(startingOrganicsWithWeights.values()))[0]
        Ending = random.choices(list(endingOrganicsWithWeights), weights=list(endingOrganicsWithWeights.values()))[0]
    print("Turn %s into %s" % (Starting, Ending))
    c = input("Enter Q to quit anything else to continue: ")
    if c.upper() == "Q":
        break