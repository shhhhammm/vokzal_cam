import cv2
import numpy as np
import arduino_test
import image
import settings
import people_data
import time

board = arduino_test.connect(settings.COM)
time.sleep(2)
arduino_test.set_pin(settings.PIN1)
arduino_test.set_pin(settings.PIN2)

# initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

cap, out = image.prepare()

previous_time = time.time()
while True:
    time.sleep(settings.DELAY)
    current_time = time.time()

    people_data.refresh(current_time - previous_time)
    ret, frame = cap.read()

    # prepare image for better recognition
    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    # detect people in the image
    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    people_data.people_amounts.append(len(boxes))

    if current_time - previous_time >= settings.TIMER:
        if people_data.average() >= settings.NUMBER_OF_PEOPLE_1:
            arduino_test.digitalWrite(board, settings.PIN1, 1)
        else:
            arduino_test.digitalWrite(board,settings.PIN1,  0)
        if people_data.average() >= settings.NUMBER_OF_PEOPLE_2:
            arduino_test.digitalWrite(board, settings.PIN2, 1)
        else:
            arduino_test.digitalWrite(board, settings.PIN2, 0)
        previous_time = time.time()

    image.draw_boxes(frame, boxes)
    if settings.SAVE_VIDEO:
        out.write(frame.astype('uint8'))

    if settings.DISPLAY_VIDEO:
        image.display_image(frame)

    if settings.PRINT_DATA:
        print(people_data.average())

    if cv2.waitKey(1) == 27:  # if pressed button is Esc
        break

image.close(cap, out)
