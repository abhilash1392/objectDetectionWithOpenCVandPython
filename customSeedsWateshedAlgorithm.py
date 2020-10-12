import cv2
import matplotlib.pyplot as plt 
import numpy as np 
from matplotlib import cm



road=cv2.imread(r'/home/abhilash/Coding/computervision/objectDetectionWithOpenCVandPython/DATA/road_image.jpg')
roadCopy=np.copy(road)


markerImage=np.zeros(road.shape[:2],dtype=np.int32)
segments=np.zeros(road.shape,dtype=np.uint8)


def create_rgb(i):
    return tuple(np.array(cm.tab10(i)[:3])*255)



colors=[]
for i in range(10):
    colors.append(create_rgb(i))



###
# GLOBAL VARIABLES
# COLOR CHOICE
nMarkers=10
currentMarker=1
marksUpdated=False


# DEF Mouse Callback function
def mouse_callback(event,x,y,flags,param):
    global marks_updated

    if event ==cv2.EVENT_LBUTTONDOWN:
        cv2.circle(markerImage,(x,y),10,(currentMarker),-1)
        cv2.circle(roadCopy,(x,y),10,colors[currentMarker],-1)
        marksUpdated=True



# WHILE TRUE
cv2.namedWindow('Road Image')
cv2.setMouseCallback('Road Image',mouse_callback)

while True:
    cv2.imshow('Watershed Segments',segments)
    cv2.imshow('Road Image',roadCopy)

    # CLOSE ALL WINDOWS
    k=cv2.waitKey(1)

    if k==27:
        break
    # CLEARING ALL COLORS C KEY
    elif k==ord('c'):
        roadCopy=road.copy()
        markerImage=np.zeros(road.shape[:2],dtype=np.int32)
        segments=np.zeros(road.shape,dtype=np.uint8)
    # Update the color choice
    elif k>0 and chr(k).isdigit():
        currentMarker=int(chr(k))

    if marksUpdated:
        markerImageCopy=markerImage.copy()
        cv2.watershed(road,markerImageCopy)

        segments=np.zeros(road.shape,dtype=np.uint8)

        for colorInd in nMarkers:
            segments[markerImageCopy==(colorInd)]=colors[colorInd] 




cv2.destroyAllWindows()