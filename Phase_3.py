def partitionRatings():
    full = []   # First we initialize the full data list.
    f = open("u.data", "r")
    line = f.readline().rstrip()
    # Then we scan through the file and build the full data list.
    while line:
        user, movie, rating, time = map(int, line.split("\t"))
        full.append((user, movie, rating))
        line = f.readline().rstrip()
    f.close()
    training = full[:]
    test = []
    for x in range(2000):
        i = randint(0, len(training)-1)
        test.append(training.pop(i))
    return training, test

def createTrainingRatingsList(rawRatings, numUsers, numItems):
    # First rLu is initialized to a list full of empty dictionaries.
    rLu = []
    for i in range(numUsers):
        rLu.append({})
    
    # Then rLm is initialized the same way.    
    rLm = []
    for i in range(numItems):
        rLm.append({})
        
    # Then it will iterate through the rawRatings list, adding each rating
    # to the appropriate user and movie dictionaries.
    for item in rawRatings:
        # item[0] is the user ID, item[1] the movie ID, item[2] the rating.
        rLu[item[0] - 1][item[1]] = item[2]
        rLm[item[1] - 1][item[0]] = item[2]
    return rLu, rLm

def evaluateCF(testSet, rLu):
    neighborDict = buildNeighborsDict(rLu, 5)
    actual_over_four=0.0
    actual_over_threefive=0.0
    predicted_over_four=0.0
    predicted_over_threefive=0.0
    
    for item in testSet:
        user = item[0]
        movie = item[1]
        actual_rating = item[2]
        predicted_rating = predictedRating(user, movie, rLu, 
                                           neighborDict[user])
        #print predicted_rating, actual_rating
        if actual_rating >= 4:
            actual_over_four = actual_over_four + 1
            if predicted_rating >= 3.5: 
                predicted_over_threefive = predicted_over_threefive + 1
        if predicted_rating >= 4:
            predicted_over_four = predicted_over_four + 1
            if actual_rating >= 3.5:
                actual_over_threefive = actual_over_threefive + 1
    precision = float(actual_over_threefive) / float(predicted_over_four)
    recall = float(predicted_over_threefive) / float(actual_over_four)
    return precision, recall

def buildNeighborsDict(userRatings, n):
    neighborsDict = {}
    for userID in range(1, 944):
        neighborsDict[userID] = kNearestNeighbours(userID, userRatings, n)
    return neighborsDict

