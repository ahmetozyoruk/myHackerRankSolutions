    seaLevel = 0
    valleyTraverse = 0
    valleyEnter = False
    for step in path:
        if step=='U':
            seaLevel = seaLevel + 1
        elif step=='D':
            seaLevel = seaLevel - 1
            
        if seaLevel<0:
            valleyEnter = True
            
        if valleyEnter and seaLevel==0:
            valleyTraverse += 1
            valleyEnter = False
        
    return valleyTraverse

