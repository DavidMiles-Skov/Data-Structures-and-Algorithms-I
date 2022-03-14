bridges = [
    "AaB",
    "AbB",
    "AcD",
    "AdC",
    "AeC",
    "BfD",
    "CgD"
]

 
# Generating all possible walks

def gen_walks(area, bridges = bridges):
    walks = []
    def make_walks(area=area, walked = None, bridges_crossed=None):
        walked = walked or area
        bridges_crossed = bridges_crossed or ()
        # Retrieving all possible bridges
        possible_bridges = [b for b in bridges if area in b and b not in bridges_crossed]
        # Determine if walk has ended
        if possible_bridges == []:
            walks.append(walked)
        # Walk to adjacent area and call make_walks
        for bridge in possible_bridges:
            bridge_area = bridge[1:] if bridge[0] == area else bridge[1::-1]
            make_walks(area=bridge_area[-1],
                       walked = walked+bridge_area,
                       bridges_crossed = (bridge,*bridges_crossed)
            )
    make_walks()
    return walks

walk_dict = {}
for i in ["A", "B", "C", "D"]:
    walk_dict[i] = gen_walks(i)
x=walk_dict
y = 0
for i in ["A", "B", "C", "D"]:
    y += len(x[i])
print(y)