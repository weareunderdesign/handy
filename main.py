import cv2
from hand_api import HandAPI
from surface_api import SurfaceAPI

cap = cv2.VideoCapture(0) 
cap.set(cv2.CAP_PROP_FPS, 20)

hand_api = HandAPI()
surface_api = SurfaceAPI()

def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hand_api.handle_click(x, y)

cv2.namedWindow('Hand and Surface Tracking')
cv2.setMouseCallback('Hand and Surface Tracking', mouse_callback)

while cap.isOpened():
    success, image = cap.read()
    if not success:
        print("Failed to get frame from camera")
        continue
    
    image = cv2.flip(image, 1)
    
    surface_api.detect_surface(image)
    image = surface_api.highlight_surface(image)
    image = hand_api.process_image(image)

    cv2.imshow('Hand and Surface Tracking', image)
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()