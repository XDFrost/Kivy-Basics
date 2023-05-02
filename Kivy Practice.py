from kivy.graphics.vertex_instructions import Rectangle, Ellipse, Line
from kivy.graphics.context_instructions import Color
from kivy.app import App
from kivy.metrics import dp
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.properties import Clock

class WidgetsEx(GridLayout):
    count = 1
    count_enabled = BooleanProperty(False)                                          # WITH BooleanProperty, WE CAN USE count_enabled IN THE kv FILE
    my_text = StringProperty("1")                                                   # TO CHANGE THE TEXT OF LABEL/BUTTON etc..
    text_input = StringProperty("Luffy")                                            # Hi! IS NOW THE DEFAULT TEXT

    # slider_value_txt = StringProperty("Value")

    def on_button_click(self):
        print("Button Clicked")
        if self.count_enabled == True:                                              # IF ToggleButton IS ON, ONLY THEN SIMPLE BUTTON CAN BE PRESSED
            self.count = self.count + 1
            self.my_text = str(
                self.count)                                                         # WHEN on_button_click FUNCTION IS CALLED, NEW my_text IS TAKEN INTO CONSIDERATION AND THEREFORE LABEL TEXT IS CHANGED; WITHOUT self, my_text ACTS LIKE A LOCAL VARIABLE AND WON'T WORK
    def toogle_button_state(self,
                            Widget):                                                # Widget - NAME OF ToggleButton; SINCE WE HAVE self IN kv FILE, WE GET WIDGET PARAMETER
        print("Toogle state: " + Widget.state)                                      # state - STRING OF CHARACTER
        if Widget.state == "normal":                                                # normal - ToggleButton IS NOT PRESSED/ToggleButton IS OFF
            Widget.text = "OFF"                                                     # Widget.text - TEXT OF ToggleButton
            self.count_enabled = False
        else:
            Widget.text = "ON"
            self.count_enabled = True

    def switch_button_activity(self, Widget):                                       # SINCE WE HAVE self IN kv FILE, WE GOT WIDGET PARAMETER
        print("Switch: " + str(
            Widget.active))                                                         # active PROPERTY IS BOOLEAN NOT STRING, SO str IS USED TO CONVERT IT INTO STRING

    # def slider_value(self, Widget):
    # print("Slider: " + str(int(Widget.value)))
    # self.slider_value_txt = str(int(Widget.value))

    def on_text_validate(self, widget):
        self.text_input = widget.text                                               # .text WILL ENABLE US TO WRITE TEXT


class StackLayoutEx(StackLayout):

    def __init__(self, **kwargs):                                                   # SYNTAX
        super().__init__(**kwargs)                                                  # BASIC STRUCTURE FOR CONSTRUCTOR/SYNTAX
        # self.orientation = "lr-bt"
        for i in range(0, 100):                                                     # CREATING MULTIPLE BUTTONS
            # size = dp(100) + i * 10
            size = dp(100)
            b = Button(text=str(i + 1), size_hint=(None, None), size=(
            size, size))                                                            # b IS ADDED FIRST BECAUSE PYTHON FILE CODE IS FIRST COMPILED COMPARED TO KV FILE
            self.add_widget(b)


# class GridLayoutEx(GridLayout):                                                   # IF I DON'T WANT TO WRITE THE CODE HERE, I'LL COMMENT THE SPECIFIC PART AND USE DECORATOR IN KV FILE
#     pass


class AnchorLayoutEx(AnchorLayout):
    pass


class BoxLayoutEx(BoxLayout):
    pass


# def __init__(self, **kwargs):                                                     # SYNTAX
#     super().__init__(**kwargs)                                                    # SYNTAX
#     self.orientation = "vertical"
#     b1 = Button(text="A")
#     b2 = Button(text="B")
#     b3 = Button(text="C")
#
#     self.add_widgets(b1)
#     self.add_widgets(b2)
#     self.add_widgets(b3) 


class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass


class CanvasEx1(Widget):
    pass


class CanvasEx2(Widget):
    pass


class CanvasEx3(Widget):
    pass


class CanvasEx4(Widget):
    def __init__(self, **kwargs):                                            # SYNATX
        super().__init__(**kwargs)                                           # SYNTAX
        with self.canvas:                                                    # SYNTAX TO WRITE IF YOU WANT TO USE A CANVAS
            Line(points=(100, 100, 400, 500), width=2)                       # Line INSTRUCTION WITH points PROPERTY
            Color(0, 1, 0)
            Line(circle=(400, 200, 80),
                 width=2)                                                    # WILL GIVE ERROR IF = ISN'T USED AFTER circle BECAUSE circle IS A PROPERTY
            Line(rectangle=(500, 450, 150, 100), width=2)
            self.rect = Rectangle(pos=(600, 200), size=(150,
                                                        100))                # WILL GIVE A COLOR FILLED RECTANGLE; rect IS A VARIABLE; rect IS A INSTANCE VARIABLE BECAUSE self IS USED AND THEREFORE IT CAN BE USED IN ANOTHER FUNCTION OF THE SAME CLASS

    def button_click(self):
        # print("Roronoa Zoro")
        # self.rect.pos = (100, 100)                                         # POSITION OF COLOURED RECTANGLE WILL CHANGE WHEN THE BUTTON IS PRESSED
        x, y = self.rect.pos                                                 # x, y - POSITIONS OF THE RECTANGLE
        w, h = self.rect.size                                                # w - WIDTH OF THE RECTANGLE, h - HEIGHT OF THE RECTANGLE
        increment = dp(10)
        diff = self.width - (
                    x + w)                                                   # diff IS THE POSITION OF THE RIGHT BOTTOM POINT, i.e. WINDIW WIDTH - [POSITION OF LEFT BOTTOM POINT (x) + WIDTH OF THE RECTANGLE (w)]
        if diff < increment:
            increment = diff                                                 # i.e. IF THE POSITION OF THE RIGHT BOTTOM POINT TO THE WINDOW IS LESS THAN 10 DP THAN INCREMENT WILL BE THE REMAINING SPACE BETWEEN WINDOW AND RIGHT BOTTOM POINT
        x = x + increment                                                    # WHENEVER THW BUTTON IS PRESSED, 10 DP IS ADDED TO X
        self.rect.pos = (x, y)                                               # WILL MOVE THE RECTANGLE TO 10 DP TOWARDS RIGHT
        # self.rect.pos[0] += 5                                              # IS NOT POSSIBLE BECAUSE TUPLE IS IMMUTABLE
        if x == self.width:
            self.button_click = False


class CanvasEx5(Widget):
    def __init__(self, **kwargs):                                            # SYNTAX
        super().__init__(**kwargs)                                           # SYNTAX
        self.ball_size = dp(50)
        self.vx = dp(3)                                                      # SPEED OF BALL IN X AXIS
        self.vy = dp(4)                                                      # SPEED OF BALL IN Y AXIS
        with self.canvas:
            self.ball = Ellipse(pos=(100, 100), size=(self.ball_size, self.ball_size))       # WE CAN'T WRITE self.centre IN THE pos ARGUEMENT TO GET THE BALL IN CENTRE BECAUSE IN __init__ FUNCTION BY DEFAULT, SIZE IS 100 DP
        # Clock.schedule_interval(self.update, 1)                            # Clock WILL CALL THE FUNCTION REGULARLY; 1 IS TIME INTERVAL OR SPEED OF BALL i.e. 1 TIME PER SECOND
        Clock.schedule_interval(self.update, 1 / 60)                         # 1/60 IS 60 FRAMES PER SECOND

    def on_size(self, *args):
        # print("on size:  " + str(self.width) + "," + str(self.height))                             # WLL PRINT THE SIZE OF THE WINDOW
        # self.ball.pos = self.center                                                                # BALL IS STILL NOT IN CENTER BECAUSE THE POSITION IS BOTTOM LEFT POINT
        self.ball.pos = (self.center_x - self.ball_size / 2, self.center_y - self.ball_size / 2)

    def update(self, dt):                                                                            # EVERY FUNCTION CALLED WITH schedule NEED TO HAVE THE PARAMETER DELTA-TIME(dt)
        # print("Update")
        x, y = self.ball.pos
        x = x + self.vx                                                                              # LOWER LEFT PART OF THE BALL; BALL CHANGES ITS POSITION WITH SAME SPEED
        y = y + self.vy                                                                              # LOWER LEFT PART OF THE BALL; BALL CHANGES ITS POSITION WITH SAME SPEED
        if y + self.ball_size > self.height:                                                         # IF LOWER LEFT PART OF THE BALL + BALL SIZE > HEIGHT OF THE WINDOW THEN..
            y = self.height - self.ball_size                                                         # HEIGHT OF WINDOW - SIZE OF BALL
            self.vy = - self.vy
        if x + self.ball_size > self.width:
            x = self.width - self.ball_size
            self.vx = - self.vx
        if y < 0:
            y = 0
            self.vy = - self.vy
        if x < 0:
            x = 0
            self.vx = - self.vx

        self.ball.pos = (x, y)                                                                       # WE CAN CHANGE THE SPEED BY CHANGING THE INCREMENT VALUE


class CanvasEx6(Widget):
    pass


class CanvasEx7(BoxLayout):
    pass


TheLabApp().run()
