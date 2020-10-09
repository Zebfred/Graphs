from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
trav_path = []
move_stack = []
visited = set()
graph = {
    0:{'n':'?','s':'?','w':'?','e':'?'}
}

opposites = {
    'n':'s',
    'e':'w',
    's':'n',
    'w':'e'
}

while len(graph) < 500:
    le = len(graph)
    
    # chooses direction
    exits = player.current_room.get_exits()
    if len(trav_path) == 0:
        direction = exits[random.randint(0,len(exits)-1)]
    else:
        while True:
            direction = exits[random.randint(0,len(exits)-1)]
            #direction != opposites[trav_path[-1]]

            #if direction picked is not backwards and not already explored
            if direction != opposites[trav_path[-1]]:
                break

    prev_room = player.current_room.id

    #add to path and move_stack
    trav_path.append(direction)
    move_stack.append(direction)
    visited.add(player.current_room.id)


    #move player
    print('move', direction)
    player.travel(direction)
    current_room = player.current_room.id

    #updat graph
    graph[prev_room][direction] = player.current_room.id
    if current_room not in visited:
        exits = player.current_room.get_exits()
        graph[current_room] = {}
        for route in exits:
            graph[current_room][route] = "?"
    graph[current_room][opposites[direction]] = prev_room
    print(current_room)
    print(graph[current_room])

    #If only exit is back the way you came
    if len(player.current_room.get_exits()) == 1 and current_room != 0:
        visited.add(player.current_room.id)
        while True:
            last_dir = move_stack.pop()
            direction = opposites[last_dir]
            trav_path.append(direction)
            print('move', direction)
            player.travel(direction)


            current_room = player.current_room.id
            print(current_room, 'backtrack')
            print(graph[current_room])
            print(move_stack)
            if '?' in graph[current_room].values() or len(graph) == 500:
                print('stop_backtrack')
                break





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in trav_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(trav_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
player.current_room.print_room_description(player)
while True:
    cmds = input("-> ").lower().split(" ")
    if cmds[0] in ["n", "s", "e", "w"]:
        player.travel(cmds[0], True)
    elif cmds[0] == "q":
        break
    else:
        print("I did not understand that command.")
