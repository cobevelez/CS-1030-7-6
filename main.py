def name_pyramid(name):
    
    for i in range(1, len(name) + 1):
        
        print(name[:i])


user_name = input("Enter your name: ")
name_pyramid(user_name)



def mini_golf_score():
    
    num_holes = int(input("How many holes did you play: "))
    total_hits = 0
    
    
    for i in range(1, num_holes + 1):
        hits = int(input(f"Enter hits for hole {i}: "))
        total_hits += hits
    
    
    print(f"Total Hits: {total_hits}")


mini_golf_score()