This program helps to control working of recirculators in waiting hall of railway stations.
It recognizes human bodies using camera and if there are too many people, recirculator turns on.



Before using this program, install libraries: pyserial, opencv-python, numpy for python

To set up the program, edit file settings.py:

variable:                  values:                  description:
PIN1, PIN2                 1-13(int)                number of Arduino pins where relay is connected
NUMBER_OF PEOPLE_1, 2      int                      amount of people to turn on the 1 and 2 relay
SAVE_VIDEO                 True, False (bool)       video from camera saves to file output.avi if True
DISPLAY_VIDEO              True, False (bool)       displays the video from camera if True
PRINT_DATA                 True, False (bool)       prints the amount of people if True
SAVE_DATA                  True, False (bool)       saves date, time and amount of people to output.txt
TIMER                      float                    time in minutes, how often the Arduino can turn on/off relay
DELAY                      float                    time in seconds, how often camera takes photos processes it,
                                                        big value saves resources but reduces the accuracy



Description of functions:

  arduino_board.py: works with Arduino board.
    connect(com): connects Arduino to the computer to com port, returns board: pyfirmata2.Arduino.
	send_to_board(board, mode,pin,  value=0): sends data to com port
    set_pin(board, pin): sets pin on Arduino as OUTPUT
	digitalWrite(board, pin, value): writes value to digital pin on the Arduino.

  image.py: works with camera, image drawing.
    prepare(): runs one in the beginning, connects the camera and if necessary creates file output.avi, returns: cap - camera, out - for writing in output.avi.
    draw_boxes(frame - camera shot, boxes: np.array - list of detected people on frame): draws rectangles around detected people on frame.
    display_image(frame - camera shot): draws the window and the image.
    close(cap - camera, out - for output.txt): runs once in the end, disconnects the camera, closes window, saves output.txt if necessary.

  people_data.py: works with information about amount of people.
    people_amounts[]: saves the amount of detected people on each frame, its average is used as the value of amount of people, refreshes  every <settings.TIMER> minutes.
    average(): returns the average of people_amounts[].
    refresh(delta_time: difference between time in current moment and previous): refreshes people_amounts[] and writes to output.txt if necessary.
