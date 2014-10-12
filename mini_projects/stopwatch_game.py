# template for "Stopwatch: The Game"
import simplegui
# define global variables

time = 0
# time measured in tenths of a sec, i.e. time = 10, represents 1 sec
started = False
minute = 0
second = 0
tenth_of_second = 0
total_stops = 0
successful_stops = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def was_successful(time):
    global successful_stops
    if time == 0:
        successful_stops += 1

def format(t):
    global time, minute, second, tenth_of_second
    minute = t // 600
    second = (t - (minute * 600)) // 10
    tenth_of_second = (t - (minute * 600) - (second * 10))
    A = str(minute)
    BC = (str(int(second)) if second >= 10 else str(0)+str(int(second)))
    D = str(int(tenth_of_second))
    clock = A+":"+BC+"."+D
    return clock

# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button():
    global started
    timer.start()
    started = True

def stop_button():
    global started, successful_stops, total_stops, tenth_of_second
    if started == True:
        timer.stop()
        total_stops += 1
        was_successful(tenth_of_second)
        started = False

def reset_button():
    global time, total_stops, successful_stops
    timer.stop()
    started = False
    time = 0
    total_stops = 0
    successful_stops = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    ''' Time is measured in tenths of a second'''
    global time
    time += 1
    print time

# define draw handler
def draw_handler(canvas):
    global time, successful_stops, total_stops
    formatted_time = format(time)
    game_counter = str(successful_stops) + "/" + str(total_stops)
    canvas.draw_text(formatted_time, [120, 140], 24, 'Green')
    canvas.draw_text("mins, secs, tenths", [90, 160], 18, 'Green')
    canvas.draw_text(game_counter, [245, 25], 18, 'Red')
    canvas.draw_text("wins / tries", [215, 45], 18, 'Red')

def draw_game_counter(canvas):
    global successful_stops, total_stops
    game_counter = str(successful_stops) + "/" + str(total_stops)
    canvas.draw_text(game_counter, [250, 25], 18, 'Red')

# create frame
frame = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
button1 = frame.add_button('Start', start_button, 50)
button2 = frame.add_button('Stop', stop_button, 50)
button3 = frame.add_button('Reset', reset_button, 50)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
# start frame
frame.start()

# Please remember to review the grading rubric
