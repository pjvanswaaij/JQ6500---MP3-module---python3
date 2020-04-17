import serial
 
 
class JQ6500:
  def __init__(self):
    self.ser = serial.Serial(port="/dev/ttyS0")
    self.ser.baudrate = 9600
 

  def sendCmd(self, cmd):
     self.ser.write(cmd)
 
 
  def next(self):
    cmd = b'\x7E\x02\x01\xEF'
    self.sendCmd(cmd)
 
 
  def pre(self):
    cmd = b'\x7E\x02\x02\xEF'
    self.sendCmd(cmd)
 
 
  def playTrack(self, track):
    cmd = bytearray(6)		
    cmd[0] = 0x7E		#start byte	
    cmd[1] = 0x04		#bytes that will be sent from now on !!including end byte!!
    cmd[2] = 0x03               #command byte, in this case select track to play
    cmd[3] = (track // 256)     #high byte of track number
    cmd[4] = (track % 256)	#low byte of track number
    cmd[5] = 0xEF   		#end byte	
    self.sendCmd(cmd)

  def volume_level(self, volume):
    print(volume)
    cmd = bytearray(5)
    cmd[0] = 0x7E	#start byte
    cmd[1] = 0x03	#bytes that will be sent !!including end byte!!
    cmd[2] = 0x06       #command byte, in this case volume; See https://sparks.gogo.co.nz/jq6500/serial.html
    cmd[3] = volume     #byte for volume (0-30)
    cmd[4] = 0xEF       #End byte
    self.sendCmd(cmd)
