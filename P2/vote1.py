import sys

def candidates(ballots):
    candidates_list = []
    for item in ballots:
        if item not in candidates_list:
            candidates_list.append(item)
    return candidates_list

def voteCount(candidate,ballots):
    count = 0
    for items in ballots:
        if items == candidate:
            count += 1
    return count

def voteCounts(candidates,ballots):    
    numVoteCandidate = []
    for item in candidates:
        tuple = (voteCount(item,ballots),item)
        numVoteCandidate.append(tuple)
    return numVoteCandidate


def winners(voteCounts):
    voteCounts.sort(reverse=True)
    winnerList = voteCounts[0]
    allWinners = [x for x in voteCounts if winnerList[0] in x]
    for x in allWinners:
        print ("Winner: ", x[1])
  
def main():
    with open(str(sys.argv[1]), 'r') as f:
        data_of_votes = (f.read()).split('\n')
    print ("Votes: ", data_of_votes )
    (winners(voteCounts(candidates(data_of_votes),data_of_votes)))
main()



    
     
    



