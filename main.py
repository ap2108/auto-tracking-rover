from ESPSocket import ESPSocket
from pynput.keyboard import Listener
import time

ESP_IP = "192.168.29.84"
ESP_PORT = 1235
PACKET_DELAY = 0.05 

max_speed = 255
curvature = 100
manual = True

pressed_keys = set()
speeds = [0, 0, True]

def on_press(key):
    try:
        if key.char not in pressed_keys:
            pressed_keys.add(key.char)
    except:
        pass

def on_release(key):
    try:
        if key.char in pressed_keys:
            pressed_keys.remove(key.char)
    except:
        pass

es = ESPSocket(ESP_IP, ESP_PORT)

def calculateSpeeds():
    pass


def main():
    Listener(on_press=on_press, on_release=on_release).start()
        
    while True:
        if(es.error):
            es.pair()
            continue
                
        if manual:
            if 'w' in pressed_keys:
                speeds = [max_speed, max_speed, True]
                if 'a' in pressed_keys:
                    speeds[0] = max_speed-curvature
                if 'd' in pressed_keys:
                    speeds[1] = max_speed-curvature

            elif 's' in pressed_keys:
                speeds = [max_speed, max_speed, False]
                if 'a' in pressed_keys:
                    speeds[0] = max_speed-curvature
                if 'd' in pressed_keys:
                    speeds[1] = max_speed-curvature

            else:
                speeds = [0, 0, True] 

        else:
            speeds = calculateSpeeds()
        
        es.setWheelSpeed(*speeds)
        time.sleep(PACKET_DELAY)
        
if __name__ == "__main__":
    main()