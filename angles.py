print(' ANGLES ')
print()
print(""" YOU CAN  ENTER ANY ANGLE DEGREE FROM 0-360 AND YOU WILL COME TO KNOW IT'S ANGLE NAME:
 ACUTE ANGLE
 OBTUSE ANGLE
 RIGHT ANGLE
 STRAIGHT ANGLE
 REFLEX ANGLE
 FULL ROTATION ANGLE
      """)
      
while True:
    print()
    ang = float(input(" ENTER THE DEGREE OF ANGLE: "))
    print()
    if ang<90:
        print(""" Acute Angle
     Any angle that is less than 90° is an acute angle. """)
    elif ang==90:
        print(""" Right Angle
     If the angle formed between two rays is exactly 90° then it is called a right angle or a 90° angle. """)
    elif ang>90 and ang<180:
        print(""" Obtuse Angle
     Any angle that is greater than 90° but less than 180° is an obtuse angle. """)
    elif ang==180:
        print(""" Straight Angle
     As the name suggests, a straight angle is a straight line, and the angle formed between two rays is exactly equal to 180°. """)
    elif ang>180 and ang<360:
        print(""" Reflex Angle
     An angle that is greater than 180° and less than 360° is called a reflex angle. """)
    elif ang==360:
        print(""" Full Rotation Angle
     A full rotation angle is formed when one of the arms of the angle goes on a complete rotation or makes a 360°. """)
    else:
        print(" PLEASE TRY AGAIN! ")
    print()
    yn = input(" DO YOU WANT TO USE THE APP AGAIN(Y/N): ")
    if yn.lower()=="y" or yn.lower()=="yes":
        print()
    elif yn.lower()=="n" or yn.lower()=="no":
        quit()
    else:
        print(" PLEASE TRY AGAIN! ")
        print()
        yn = input(" DO YOU WANT TO USE THE APP AGAIN(Y/N): ")
        if yn.lower()=="y" or yn.lower()=="yes":
            print()
        elif yn.lower()=="n" or yn.lower()=="no":
            quit()
    
    
