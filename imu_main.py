from imu import MPU6050  #https://github.com/micropython-IMU/micropython-mpu9x50
from time import sleep
from machine import Pin, I2C
import tm1637


i2c = I2C(scl = Pin(18), sda= Pin(19))
tm_display = tm1637.TM1637(clk=Pin(27), dio=Pin(26))
tm_display.show('0000') #display the number 10 on the display
tm.write(clear)
imu = MPU6050(i2c)

count = 0
RED_PIN = 26
led1 = Pin(RED_PIN, Pin.OUT)


status = False
# Temperature display
print("Temperature: ", round(imu.temperature,2), "°C")


while True:
    sleep(3)
    acceleration = imu.accel
    gyroscope = imu.gyro
    print(status)
    print ("Acceleration x: ", round(acceleration.x,2), " y:", round(acceleration.y,2),
           "z: ", round(acceleration.z,2))

    print ("gyroscope x: ", round(gyroscope.x,2), " y:", round(gyroscope.y,2),
           "z: ", round(gyroscope.z,2))

# data interpretation (accelerometer)
     
      
    if (acceleration.x < 0 and  status == False):
       # measure = measure + 1
        print("Hit Hit Takling opstået")
        
        status = True
        tm.write(clear)
        led1.on()
        count = count + 1
        print("Takling nr:  ", + count," opstået")
        
       
    if (acceleration.x < 0 and status == True):
        
        continue
        
    elif acceleration.x > 0 and status == True:
        tm_display.show(str(count))
        
        #sleep(1)
        led1.off()
        status = False
       # print("measure is ", measure)
        
    



# data interpretation (gyroscope)



  
