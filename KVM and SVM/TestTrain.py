import random

def testTrain(xTrain, yTrain):
    random.seed(10)



    total = int(len(yTrain)*0.20)
    disease1 = total
    disease2 = total
    disease3 = total
    healthy = total
    
    disease1Bacteria = []
    disease2Bacteria = []
    disease3Bacteria = []
    healthyBacteria = []


    for i in range(len(yTrain)):

        if (yTrain[i] == 'Disease-1') and disease1 > 0:
            disease1Bacteria.append(xTrain[i])
            disease1 -= 1
        elif (yTrain[i] == 'Disease-2') and disease2 > 0:
            disease2Bacteria.append(xTrain[i])
            disease2 -= 1
        elif (yTrain[i] == 'Disease-3') and disease3 > 0:
            disease3Bacteria.append(xTrain[i])
            disease3 -= 1
        elif (yTrain[i] == 'Healthy') and healthy > 0:
            healthyBacteria.append(xTrain[i])
            healthy -= 1

        if (disease1 == 0 and disease2 == 0 and disease3 == 0 and healthy == 0):
            break
    
    if (len(disease1Bacteria) < total):
        toDo1 = total - len(disease1Bacteria)
        for i in range(toDo1):
            disease1Bacteria.append(disease1Bacteria[random.randint(0,len(disease1Bacteria))].copy())


    if (len(disease2Bacteria) < total):
        toDo2 = total - len(disease2Bacteria)
        for i in range(toDo2):
            disease2Bacteria.append(disease2Bacteria[random.randint(0,len(disease2Bacteria))].copy())


    if (len(disease3Bacteria) < total):
        toDo3 = total - len(disease3Bacteria)
        for i in range(toDo3):
            disease3Bacteria.append(disease3Bacteria[random.randint(0,len(disease3Bacteria))].copy())

    yTrainOut = []
    for i in range(len(disease1Bacteria)):
        yTrainOut.append('Disease-1')
    
    for i in range(len(disease2Bacteria)):
        yTrainOut.append('Disease-2')
    
    for i in range(len(disease3Bacteria)):
        yTrainOut.append('Disease-3')
    for i in range(len(healthyBacteria)):
        yTrainOut.append('Healthy')


    xTrainOut = disease1Bacteria + disease2Bacteria + disease3Bacteria + healthyBacteria 

    return xTrainOut, yTrainOut


    


