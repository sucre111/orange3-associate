from orangecontrib.associate import slpgrowth



transactions = [('a', 'b', 'c'), ('b'), ('a'), ('a', 'c', 'd'), ('b', 'c'), ('b', 'c')]
transactions = [(1, 2, 3), (2,), (1, 4), (1, 3, 4), (2, 3), (2, 3)]

# fg_input = itemmining.get_fptree(transactions, min_support=2)
# report = itemmining.fpgrowth(fg_input, min_support=2)
slg_input = slpgrowth.frequent_itemsets(transactions, 1, 3)
itemset = list(slg_input)
print(itemset)
print(len(itemset))
