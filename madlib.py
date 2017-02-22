noun_list = []
adj_list = []

noun = input('Please give me a noun: >')
noun_list.append(noun)

adj = input('Please give me an adjective: >')
adj_list.append(adj)

noun = input('Please give me another noun: >')
noun_list.append(noun)

print(noun_list)
print(adj_list)

print('The ' + noun_list[0] + ' jumped over the ' + adj_list[0] + ' ' + noun_list[1] + '.')