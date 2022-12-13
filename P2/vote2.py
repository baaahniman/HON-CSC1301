import sys

def candidates(ballots):
  candidates_list_updated = [items for sublist in ballots for items in sublist]
  candidates_set = set(candidates_list_updated)
  list_candidate = list(candidates_set)
  return list_candidate
        
def voteCount(candidate,votes):
  count = 0
  for items in votes:
      if items == candidate:
       count += 1
  return count

def eliminate(candidate,ballots):
  eliminated_list = list(ballots)
  for items in eliminated_list:
    for sub_items in items:
      if sub_items == candidate:
        items.remove(sub_items)
  return eliminated_list

def remove_empty_ballot(ballots):
  no_empty_list = (list(filter(lambda x: x, ballots)))
  return no_empty_list

def rank_first_preferences(ballots):
  list_ballots = list(ballots)
  list_first = list([item[0] for item in list_ballots])
  list_pair = list()
  for item in list_first:
    count = list_first.count(item)
    pair = count, item
    list_pair.append(pair) 
  set_pair = set(list_pair)
  list_pair = list(set_pair)
  list_pair.sort()
  return list_pair

def find_lowest(ranks):
  loser_list = ranks[0]
  losers = [item for item in ranks if loser_list[0] in item]
  all_losers = [candidate[1] for candidate in losers]
  return all_losers

def single_or_no_candidate(ballots):
  opened_ballots = [items for sublist in ballots for items in sublist]
  if len(opened_ballots) == 0:
    return True
  else:
    iterator = iter(opened_ballots)
    first = next(iterator)
    return all(first == x for x in opened_ballots)

def main():
  with open(str(sys.argv[1]), 'r') as f:
    data = f.read().split('\n')
  ballots = list()
  for items in data:
    comma_split = items.split(',')
    ballots.append(comma_split)
  print("Ballots: ",ballots)   
  
  while not single_or_no_candidate(ballots):
    rank = rank_first_preferences(ballots)
    lowest = find_lowest(rank)
    if len(lowest) == len(ballots[0]):
      break
    else:
      for index in range(len(lowest)):
        candidate_to_drop = eliminate(lowest[index],ballots)
    ballots = remove_empty_ballot(candidate_to_drop)
  updated_ballots = remove_empty_ballot(ballots)
  for index in range(len(updated_ballots[0])):
    print("Winner: ",updated_ballots[0][index])
  
main()

  
  
  
