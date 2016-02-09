#!/usr/bin/python
# template for "Stopwatch: The Game"
import simplegui

# define global variables
COUNTER = "0:00.0"
NUMBER = 0
SUC_STOP = 0
TOL_STOP = 0
FLAG = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(val):
    minutes = str(int(val) / 600)
    seconds = str((int(val) % 600) / 10.0)
    if len(seconds) != 4:
        seconds = str(0 * (4 - len(seconds))) + seconds
    return minutes + ":" + seconds
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    global FLAG
    global COUNTER   
    if COUNTER == "9:59.0":
       reset_handler()
    FLAG = True
    timer.start()

def stop_handler():
    global COUNTER
    global SUC_STOP
    global TOL_STOP
    global FLAG
    timer.stop()
    if FLAG:
        TOL_STOP += 1
        if str(COUNTER)[-1] == "0":
            SUC_STOP += 1
    FLAG = False

def reset_handler():
    global NUMBER
    global COUNTER
    global SUC_STOP
    global TOL_STOP
    timer.stop()
    NUMBER = 0
    COUNTER = "0:00.0"
    SUC_STOP = 0
    TOL_STOP = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global NUMBER
    global COUNTER
    global FLAG
    NUMBER += 1
    COUNTER = format(NUMBER)
    if COUNTER == "9:59.0":
       timer.stop()
       FLAG = False

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(COUNTER, [80, 120], 30, "White")
    canvas.draw_text(str(SUC_STOP) + "/"+ str(TOL_STOP), 
                     [200, 50], 30, "White")
    
# create frame
frame = simplegui.create_frame("Time", 300, 200)
timer = simplegui.create_timer(1, timer_handler)

# register event handlers
frame.set_draw_handler(draw_handler)
frame.add_button("Start", start_handler)
frame.add_button("Stop", stop_handler)
frame.add_button("Reset", reset_handler)

# start frame
frame.start()
