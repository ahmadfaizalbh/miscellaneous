def cardboard_intersection(cardboards):
    result = []
    for i,(x1, x2, h) in enumerate(cardboards):
        bottom = True
        bottom_pos = 0
        top = True
        for j,(x_1, x_2, h_) in enumerate(cardboards):
            if i!=j:
                if  x_1<=x2<=x_2:
                    if h<=h_:
                        if x2<x_2 or j>i:
                            bottom = False
                    elif x2!=x_2 and bottom_pos<h_:
                        bottom_pos=h_
                    elif x2==x_2 and j>i:
                        bottom = False
                if x_1<=x1<=x_2 and h<=h_:
                    if x_1<x1 or h<h_ or j>i:
                        top = False
                
        if top:
            result.append((x1,h))
        if bottom:
            result.append((x2,bottom_pos))
    result.sort()
    return result




if __name__ == "__main__":
    
    cardboards1 = [(1,5,10),(4,6,8),(10,15,10),(11,12,8)]
    print("Input 1:", cardboards1)
    print("Output 1:", cardboard_intersection(cardboards1))

    print("-"*30)
    
    cardboards2 = [(1,10,4),(1,8,6),(1,6,8)]
    print("Input 2:", cardboards2)
    print("Output 2:", cardboard_intersection(cardboards2))
    
    print("-"*30)
    
    cardboards3 = [(0,6,2),(5,10,8),(7,8,12)]
    print("Input 3:", cardboards3)
    print("Output 3:", cardboard_intersection(cardboards3))
    
    print("-"*30)
    
    cardboards4 = [(0,6,2)]
    print("Input 4:", cardboards4)
    print("Output 4:", cardboard_intersection(cardboards4))
    
    print("-"*30)
    
    cardboards5 = [(0,6,2),(0,6,3)]
    print("Input 5:", cardboards5)
    print("Output 5:", cardboard_intersection(cardboards5))
    
    print("-"*30)
    
    cardboards6 = [(0,6,3),(0,6,2)]
    print("Input 6:", cardboards6)
    print("Output 6:", cardboard_intersection(cardboards6))
    


                
        
    
