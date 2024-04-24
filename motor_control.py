
# Below imports all neccessary packages to make this Python Script run
import time
import board
from adafruit_motor import stepper
from adafruit_motorkit import MotorKit

# Below initialises the variable kit to be our I2C Connected Adafruit Motor HAT. If stacking Multiple
kit = MotorKit(i2c = board.I2C())

# Initialize variables
num_players = 0
num_cards = 52
game_over = 0

# Functions
def shoot_card():
	kit.motor1.throttle = 1.0
	time.sleep(10)
	kit.motor1.throttle = -0.5
	time.sleep(0.15)
	kit.motor1.throttle = 0

def next_player(num_players):
	turn_size = int(600/num_players)
	for i in range(turn_size):
		kit.stepper2.onestep()
		time.sleep(0.0025)

# Get inputs from player
while(num_players <= 0 or num_players > 8):
	num_players = int(input("Enter number of players: "))
	if (num_players <= 0):
		print("Not enough players")
	if(num_players > 8):
		print("Too many players")


# Start game
while(game_over == 0):
	for i in range(num_players):
		shoot_card()
		time.sleep(0.5)
		#next_player(num_players)
		time.sleep(0.5)
	game_over = 1
