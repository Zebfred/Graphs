
def earliest_ancestor(ancestors, starting_node):
    # build graph
    verts = {}
    for anc in ancestors:
        if anc[1] not in verts: 
            verts[anc[1]] = set([anc[0]])
        else:
            verts[anc[1]].add(anc[0])

    #dft 
    stack = []
    max_path = []

    stack.append([starting_node])

    while len(stack) > 0:
        current_path = stack.pop()
        current_node = current_path[-1]

        try:
            neighs = verts[current_node]
        except:
            if len(current_path) > len(max_path):
                max_path = current_path
            continue

        for neigh in neighs:
            stack.append(current_path + [neigh])

    if max_path[-1] == starting_node:
        return -1

    return max_path[-1]