import sys, uselect
from machine import ADC, I2C, Pin, UART
from time import sleep
import umqtt_robust2 as mqtt
import tm1637

tm_batteri = tm1637.TM1637(clk=Pin(27), dio=Pin(26))
tm_batteri.show('0000') #display the number 10 on the display
analog_pin = ADC(Pin(32))        # The battery status ADC object
analog_pin.atten(ADC.ATTN_11DB)
Batteri_scal = 3.3 / 4095
min_volt = 6.0
max_volt = 8.4

while True:
     sleep(2)
     analog_val = analog_pin.read()
     print("Analog målt værdi: ", analog_val)
     målt_spaending = analog_val * Batteri_scal # Baud 4095 Volt 3.3v for Esp32 analog Vpin.
     print("Målt spænding er: ", målt_spaending)
     batteri_spaending = målt_spaending * 2.5 # y=ax+b da vi kender x og y kan vi udregne a og for at finde ud ad om det var større eller laver end forventet
     print("spaending er: ", batteri_spaending)
     battery_percentage = batteri_spaending * 41.67-250  # a= 42.67 b= -250, 8.4 er max spænding for de 2 batterier i serie
     print("percentage is: ",battery_percentage)
     tm_batteri.show(battery_percentage)
     mqtt.web_print(int(battery_percentage),'abdi001/feeds/Battery')