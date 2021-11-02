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
    "alkene": 25/6,
    "haloalkane": 25/6,
    "alkene": 25/6,
    "primary alcohol": 25/6,
    "secondary alcohol": 25/6,
    "ketone": 25/6,
    "aldehyde": 25/6,
    "carboxylic acid": 25/6,
    "ester": 25/6,
    "amide": 25/6,
    "ether": 25/6,
    "primary amine": 25/6,
}

endingOrganicsWithWeights = { # all weights should add to 100. alkane 1% of the time rest are divided equally
    "alkane": 1,
    "alkene": 33/5,
    "haloalkane": 33/5,
    "alkene": 33/5,
    "dihaloakane": 33/5,
    "primary alcohol": 33/5,
    "secondary alcohol": 33/5,
    "ketone": 33/5,
    "aldehyde": 33/5,
    "carboxylic acid": 33/5,
    "ester": 33/5,
    "amide": 33/5,
    "nitril": 33/5,
    "ether": 33/5,
    "primary amine": 33/5,
    "secondary amine": 33/5,
}

while True:
    Starting = random.choices(list(startingOrganicsWithWeights), weights=list(startingOrganicsWithWeights.values()))[0]
    Ending = random.choices(list(endingOrganicsWithWeights), weights=list(endingOrganicsWithWeights.values()))[0]
    if Starting == Ending:
        continue
    print("Turn %s into %s" % (Starting, Ending))
    c = input("Enter Q to quit anything else to continue: ")
    if c.upper() == "Q":
        break