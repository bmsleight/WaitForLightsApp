from browser import document, alert, html, timer, window
from random import randint


# Globals
tick_timer = None

def log_debug(log):
#    document["log"] <= log + "\n"
    document["log"] <= log 

class Demand():
    def __init__(self):
        self.state = "off"
    def set(self, state):
        if state == "off":
            self.state = "off"
        if state == "on" and self.state is not "block":
            self.state = "on"
        if state == "block":
            self.state = "block"
    
class Lights():
    def __init__(self, signals="pedx"):
        self.events = []
        self.demand = Demand()
        self.sounds = {'ped': html.AUDIO(src='sounds/bleeplq.mp3'),
                       'rag': html.AUDIO(src='sounds/trafficlq.mp3'),
                       'demand': html.AUDIO(src='sounds/clicklq.mp3')
                       }
        self.sounds['rag'].play()
        self.startup()
        self.set_demand("off")
    def next(self):
        if self.events:
            self.set_signals(self.events.pop(0))
            return True
        else:
            if self.demand.state == "on":
                self.pedx()
                return True
            return False
    def startup(self):
        self.events = [{'ped': 'ped_red','rag':'rag_amber'},
                       {'ped': 'ped_red','rag':'rag_amber'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red-amber'},
                       {'ped': 'ped_red','rag':'rag_red-amber'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'}
                       ]
    def pedx(self):
        self.events = [{'ped': 'ped_red','rag':'rag_amber'},
                       {'ped': 'ped_red','rag':'rag_amber'},
                       {'ped': 'ped_red','rag':'rag_amber'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_green','rag':'rag_red'},
                       {'ped': 'ped_green','rag':'rag_red'},
                       {'ped': 'ped_green','rag':'rag_red'},
                       {'ped': 'ped_black','rag':'rag_red'},
                       {'ped': 'ped_black','rag':'rag_red'},
                       {'ped': 'ped_black','rag':'rag_red'},
                       {'ped': 'ped_black','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red'},
                       {'ped': 'ped_red','rag':'rag_red-amber'},
                       {'ped': 'ped_red','rag':'rag_red-amber'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'},
                       {'ped': 'ped_red','rag':'rag_green'}
                       ]
    def set_signal(self, signal, img):
        document[signal].clear()
        document[signal] <= html.IMG(src="images/" + img + ".jpg", Class="u-max-full-width")
    def set_demand(self, state):
        self.demand.set(state)
        self.set_signal('pushbutton', "pb_" + self.demand.state)
    def set_signals(self, signal):
        # pushbutton
        if signal['ped'] == 'ped_green':
           # Block pb
            self.set_demand('block')
        if self.demand.state == "block" and signal['ped'] == 'ped_black':
            self.set_demand('off')
        self.set_signal('ped', signal['ped'])
        self.set_signal('rag', signal['rag'])
        #Sounds
        if signal['rag'] == 'rag_green':
            lights.sounds['rag'].play()
        if signal['rag'] == 'rag_red':
            lights.sounds['rag'].pause()
            lights.sounds['rag'].currentTime = 0
        if signal['ped'] == 'ped_green':
            lights.sounds['ped'].currentTime = 0
            lights.sounds['ped'].play()
        if signal['ped'] == 'ped_black':
            lights.sounds['ped'].pause()
            lights.sounds['ped'].currentTime = 0

def tick():
    lights.next()

def push_button(event):
    lights.set_demand("on")
    lights.sounds['demand'].play()
#    vibrate(200)

def init():
    document['pushbutton'].bind("click", push_button)
    tick_timer = timer.set_interval(tick, 1000)

#vibrate = window.navigator.vibrate
lights = Lights()
init()
