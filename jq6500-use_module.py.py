import jq6500 
import time 
import serial

if __name__ == "__main__":

    jq = jq6500.JQ6500()
    jq.volume_level(30)    
    jq.playTrack(1)
    time.sleep(3)
    jq.volume_level(20)    
    jq.playTrack(1)
    time.sleep(3)
    jq.volume_level(30)    
    jq.playTrack(1)
