import cv2
import mediapipe as mp
import pyautogui
import time
marking = True
while True:
    if (marking == True) :
        cam = cv2.VideoCapture(0)
        face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        screen_w, screen_h = pyautogui.size()
        while marking == True:
            _, frame = cam.read()
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = face_mesh.process(rgb_frame)
            landmark_points = output.multi_face_landmarks
            frame_h, frame_w, _ = frame.shape
            if landmark_points:
                landmarks = landmark_points[0].landmark
                mouth = [landmarks[15], landmarks[13]]
                for landmark in mouth:
                    x = int(landmark.x * frame_w)

                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 254))
                if (mouth[0].y - mouth[1].y) > 0.16:
                    marking = False
                    print("b")
                    pyautogui.sleep(0.2)

            cv2.imshow('Mouth Controll For Activition', frame)
            cv2.waitKey(1)

    else :
        cam = cv2.VideoCapture(0)
        face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
        screen_w, screen_h = pyautogui.size()
        while marking == False:
            _, frame = cam.read()
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            output = face_mesh.process(rgb_frame)
            landmark_points = output.multi_face_landmarks
            frame_h, frame_w, _ = frame.shape
            if landmark_points:
                landmarks = landmark_points[0].landmark
                mouth = [landmarks[15], landmarks[13]]
                for id, landmark in enumerate(landmarks[474:478]):
                    x = int(landmark.x * frame_w)

                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 0))
                    if id == 1:
                        screen_x = screen_w / frame_w * x
                        screen_y = screen_h / frame_h * y
                        pyautogui.moveTo(screen_x, screen_y)
                left = [landmarks[153], landmarks[158]]
                right = [landmarks[380], landmarks[385]]
                for landmark in left:
                    x = int(landmark.x * frame_w)

                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 255))
                if (left[0].y - left[1].y) < 0.006:
                    pyautogui.doubleClick()
                    pyautogui.sleep(0.2)
                for landmark in right:
                    x = int(landmark.x * frame_w)

                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 253))
                if (right[0].y - right[1].y) < 0.004:
                    pyautogui.rightClick()
                    pyautogui.sleep(0.2)
                for landmark in mouth:
                    x = int(landmark.x * frame_w)

                    y = int(landmark.y * frame_h)
                    cv2.circle(frame, (x, y), 3, (0, 255, 254))
                if (mouth[0].y - mouth[1].y) > 0.16:
                    marking = True
                    conter = 0
                    conter = conter + 1
                    print(conter)
                    pyautogui.sleep(0.2)

            cv2.imshow('Eye Control cursor ', frame)
            cv2.waitKey(1)
    time.sleep(4)
