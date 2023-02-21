import pygame, math

def getAnglBetwObjNPoi(anchor, point, correctionAngle):
# Gets the angle between an object and a point
# Correction angle from 0 degrees(pointing right) in original sprited
    relX, relY = point[0] - anchor[0], point[1] - anchor[1]
    return (180 / math.pi) * -math.atan2(relY, relX) - correctionAngle

def moveToTarget(point, speed, target):
# Function that'll move a rect closer to a given point
    newPos = []
    for i in range(2):
# If the point has to go backward to get to the point
        if point[i] > target[i]:
            if point[i] - speed > target[i]:
                newPos.append(point[i] - speed)
            else:
# This'll snap to the point if the speed overshoots
                newPos.append(target[i])
        elif point[i] < target[i]:
            if point[i] + speed < target[i]:
                newPos.append(point[i] + speed)
            else:
                newPos.append(target[i])
        else:
            newPos.append(point[i])
    return tuple(newPos)

def getDisBetwPoints(p1,p2):
    if p1[0] - p2[0] < 0:
        xDiff = -(p1[0] - p2[0])
    else:
        xDiff = -(p1[0] - p2[0])
    if p1[1] - p2[1] < 0:
        yDiff = -(p1[1] - p2[1])
    else:
        yDiff = -(p1[1] - p2[1])
    return xDiff, yDiff

def debug(info, screen,x = 10, y = 10):
    font = pygame.font.Font(None, 30)
    for i in range(len(info)):
        debugSurf = font.render(str(info[i]), True, "White")
        debugRect = debugSurf.get_rect(topleft = (x,y))
        screen.blit(debugSurf, debugRect)
        y += 40

def getCornerPoints(initPoint,width,height):
    points = []
    points.append(initPoint) # (Topleft)
    points.append((initPoint[0] + width,initPoint[1])) # (Topright)
    points.append((initPoint[0] + width,initPoint[1] + height)) # (Bottomright)
    points.append((initPoint[0],initPoint[1] + height)) # (Bottomleft)
    return tuple(points)
