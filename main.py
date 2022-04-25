import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(1)  # on capture les images grace a notre camera

mpMain = mp.solutions.hands
hands = mpMain.Hands()  # on cree l'objet main
mpDessin = mp.solutions.drawing_utils  # objets pour dessiner la main

pTime = 0
cTime = 0

while True:
    success, img = cap.read()  # instance, on le lit
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # On convertie l'image RGB pour quil puisse le  lire
    results = hands.process(imgRGB)  # methode pour proceder l'image recu
    print(results.multi_hand_landmarks) #affiche ou est placer ma main

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDessin.draw_landmarks(img, handLms, mpMain.HAND_CONNECTIONS)        ## on dessine des points sur la main et on les relies pour une seul main

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime                   #afficher les fps

    cv2.putText(img,str(int(fps)),(10,70), cv2.FONT_HERSHEY_PLAIN,3,(255,255,0),3)  #on affiche les fps dans la came
    cv2.putText(img, str('IA EYUB C'), (10, 100), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)

    cv2.imshow("Image", img)  # on l'affecte
    cv2.waitKey(1)  # on lance la camera tant que
