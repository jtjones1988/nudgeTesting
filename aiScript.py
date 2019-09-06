import numpy as np
import random
import time

# industryActions = np.array['buildRoad', 'buildFactory', 'harvestResources' ]
# militaryActions = np.array['createArmy', 'buildFortification', 'buildTank']
# scienceActions = np.array['researchMilitary', 'researchIndy', 'researchEco']
# ecoActions = np.array['buildFarm', 'buildTradeHub', 'buildMarket']

# #simple AI: take all the nudge values and get percent values corresponding
# #need decision tree
# def chooseActionPath(nudgeValues):



def buildHarvester():

    if resource >= 5:
        global harvesters
        harvesters += 1
        # print("Harvester built. Harvesters: " + str(harvesters))
    else:
        harvestResource()
    return
    

def harvestResource():

    if harvesters > 0:
        global resource
        resource += harvesters
        # print("Harvested resource. Resources: " + str(resource))
    else:
        buildHarvester()


def makeArmy():

    if resource >= 10:
        global army
        army += 1
        # print("Army Created. Army count: " + str(army))
    else:
        harvestResource()


def attack():
    if army > 0:
        # print('Attacking with strength: ' + str(army))
        global health
        health -= army
        # print('Health remaining: ' + str(health))
        # if health <= 0:
            # print('Victory in ' + str(turns) + ' turns!')
            # quit()
    else:
            makeArmy()


def test(h, a):
    
    turns = 0
    while health > 0:
        
        if harvesters < h:
            buildHarvester()
        elif army < a:
            makeArmy()
        else:
            attack()
        
        turns += 1
        time.sleep(.01)

    return turns


for x in range(1, 11):
    for y in range(1, 11):
        army = 0
        resource = 0
        harvesters = 1
        health = 10
        tmpTurns = test(x, y)
        print(str(x) + ' harvesters. ' + str(y) + ' army count. ' + str(tmpTurns) + ' turns.' )