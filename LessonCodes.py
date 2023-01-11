votes = "RLLLLLLRRRRRLLLLLLRLRRIRLRRIRLLRIR"
vote_dict = {}
for el in votes:
    if not el in vote_dict.keys():
        vote_dict[el] = 1
    else:
        vote_dict[el] += 1
print(vote_dict)
vds = sorted(vote_dict.items(), key=lambda x: x[1])
print(vds)
