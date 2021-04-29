
#Let's learn about list comprehensions! You are given three integers x, y and z representing the dimensions of a cuboid along 
#with an integer n. Print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of  is not equal to n. 


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    result = []
    
    for x1 in range(x+1):
        for y1 in range(y+1):
            for z1 in range(z+1):
                if x1 + y1 + z1 != n:
                    obj = [x1, y1, z1]
                    result.append(obj)
                    
    print(result)
                
    max_x = 5
    max_y = 5
    max_z = 5
    n = 5

    result = [
        [x, y, z] for x in range(max_x) for y in range(max_y) for z in range(max_z) if (x + y + z) != n
    ]       
          