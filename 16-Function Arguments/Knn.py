import math
import operator

def euclideanDistance(point1, point2):
    distance = 0.0
    for i in range(len(point1)):
        distance += (point1[i] - point2[i]) ** 2
    return math.sqrt(distance)

def getNeighbors(trainingSet, testInstance, k):
    distances = []
    for i in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[i])
        distances.append((i, dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for i in range(k):
        neighbors.append(distances[i][0])
    return neighbors

def getResponse(neighbors, trainingLabels):
    classVotes = {}
    for i in range(len(neighbors)):
        response = trainingLabels[neighbors[i]]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

# example usage
trainingSet = [[2, 1, 0], [4, 1, 0], [6, 3, 1], [8, 3, 1]]
trainingLabels = [0, 0, 1, 1]
testInstance = [5, 2]
k = 3
neighbors = getNeighbors(trainingSet, testInstance, k)
prediction = getResponse(neighbors, trainingLabels)
print('Predicted label: ' + str(prediction))
