import umqtt_robust2 as mqtt
from machine import Pin
from machine import PWM
from time import sleep
# Her kan i placere globale varibaler, og instanser af klasser

BUZZ_PIN = 26
buzzer_pin = Pin(BUZZ_PIN, Pin.OUT)
pwm_buzz = PWM(buzzer_pin)

def buzzer(buzzer_PWM_object, frequency, sound_duration, silence_duration):
    buzzer_PWM_object.duty(512)
    buzzer_PWM_object.freq(frequency)
    sleep(sound_duration)
    buzzer_PWM_object.duty(0)
    sleep(silence_duration)
    
buzzer(pwm_buzz, 262, 0.2, 0.2)
buzzer(pwm_buzz, 294, 0.4, 0.3)

while True:
    try:
        if mqtt.besked == "1":
            print("Spiller tone!")
            buzzer(pwm_buzz, 440, 0.5, 0.5)
        
        if len(mqtt.besked) != 0: # Her nulstilles indkommende beskeder
            mqtt.besked = ""
            
        mqtt.sync_with_adafruitIO() # igangsæt at sende og modtage data med Adafruit IO             
        #sleep(1) # Udkommentér denne og næste linje for at se visuelt output
        #print(".", end = '') # printer et punktum til shell, uden et enter        
    
    except KeyboardInterrupt: # Stopper programmet når der trykkes Ctrl + c
        print('Ctrl-C pressed...exiting')
        mqtt.c.disconnect()
        mqtt.sys.exit()
