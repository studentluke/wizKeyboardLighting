from cuesdk import *
import time
import mss
import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt


sdk = CueSdk()



def getAll(r,g,b, a):
    all = []
    for i in range (1,190):
        all.append(CorsairLedColor(i,r,g,b,a))
    return all







def main():
    loop_time = time.time()
    myDevices = []
    testStorm = cv2.imread("storm13.png")

    def on_state_changed(evt):
        print(evt.state)
        # the app must wait for CSS_Connected event before proceeding
        if evt.state == CorsairSessionState.CSS_Connected:
            
            devices, err = sdk.get_devices(
                CorsairDeviceFilter(
                    device_type_mask=CorsairDeviceType.CDT_All))
            if err == CorsairError.CE_Success and devices:
                for d in devices:
                    print(d.device_id)
                    myDevices.append(d)
                    stormLED(myDevices[0].device_id)
                    iceLED(myDevices[0].device_id)
            else:
                print(err)

    err = sdk.connect(on_state_changed)
    if err != CorsairError.CE_Success:
        print("\nERROR: Unable to connect to iCUE")
        print(err)
        sys.exit()
    


    with mss.mss() as sct:
        monitor = sct.monitors[1]
        left = monitor['left'] + monitor['width'] * 40 // 100  # 25% from the left
        top = monitor['top'] + monitor['height'] * 45 // 100  # 25% from the top
            
        right = monitor['width'] * 47 // 100 # to right side
        lower = monitor['height'] * 60 // 100# to bottom
        spot1 = (left, top, right, lower)

        left = monitor['left'] + monitor['width'] * 20 // 100  # 25% from the leftt
        top = monitor['top'] + monitor['height'] * 40 // 100  # 25% from the top
            
        right = monitor['width'] * 40 // 100 # to right side
        lower = monitor['height'] * 70 // 100# to bottom
        spot2 = (left, top, right, lower)


        left = monitor['left'] + monitor['width'] * 20 // 100  # 25% from the left
        top = monitor['top'] + monitor['height'] * 20 // 100  # 25% from the top
            
        right = monitor['width'] * 40 // 100 # to right side
        lower = monitor['height'] * 50 // 100# to bottom
        spot3 = (left, top, right, lower)


        left = monitor['left'] + monitor['width'] * 30 // 100  # 25% from the leftt
        top = monitor['top'] + monitor['height'] * 10 // 100  # 25% from the top
            
        right = monitor['width'] * 50 // 100 # to right side
        lower = monitor['height'] * 40 // 100# to bottom
        spot4 = (left, top, right, lower)

        spots = [spot1,spot2,spot3,spot4]
        place = 0
        i = 0

        while(True):
            # time.sleep(.25)
            if(place >= len(spots)):
                place = 0
            
            im = np.array(sct.grab(spots[place]))
            # cv2.imwrite('screenshot'+str(i)+'.png',im)
            # i+=1
            #im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

            # Initiate SIFT detector
            sift = cv2.SIFT_create()
            # find the keypoints and descriptors with SIFT
            kp2, des2 = sift.detectAndCompute(testStorm,None)
            kp1, des1 = sift.detectAndCompute(im,None)
            # BFMatcher with default params
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1,des2,k=2)

            # Apply ratio test
            good = []
            for m,n in matches:
                if m.distance < 0.75*n.distance:
                    good.append([m])

            # cv2.imshow('Computer Vision', im)
           

            # if(len(good) > 20):
            #     stormLED(myDevices[0].device_id)
            #     cv2.imwrite('match'+str(i)+'.png',im)
            #     i+=1
            #     print(str(i) + ". " + str(len(good)))
            #     img3 = cv2.drawMatchesKnn(testStorm,kp1,im,kp2,good,None,flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
            #     plt.imshow(img3),plt.show()
            #     time.sleep(5)
            #     #place+= 1

            

            #print(len(good))   
            
            
            # print('FPS {}'.format((1/ (time.time() - loop_time))))
            
            
            # loop_time = time.time()
            
           
            

            if cv2.waitKey(1) == ord('q'):
                cv2.destroyAllWindows()
                break

            
            
        
            

   

def stormLED(id):
    lightningBright = [CorsairLedColor(CorsairLedId_Keyboard.CLK_F2,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F5,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F9,255,255,0,255),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_2,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_6,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_0,255,255,0,255), 
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_Q,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_T,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,255,255,0,255),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_W,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_Y,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_P,255,255,0,255),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_E,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_BracketLeft,255,255,0,255),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_S,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_SemicolonAndColon,255,255,0,255),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_Z,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_B,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_PeriodAndBiggerThan,255,255,0,255)]

    lightningNormal = [CorsairLedColor(CorsairLedId_Keyboard.CLK_F2,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F5,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F9,255,255,0,100),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_2,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_6,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_0,255,255,0,100), 
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_Q,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_T,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,255,255,0,100),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_W,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_Y,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_P,255,255,0,100),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_E,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_BracketLeft,255,255,0,100),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_S,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_SemicolonAndColon,255,255,0,100),
                    CorsairLedColor(CorsairLedId_Keyboard.CLK_Z,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_B,255,255,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_PeriodAndBiggerThan,255,255,0,100)]
    finalImBright = []

    finalImNormal = []
    # purple fill the board
    for i in range(15):
        sdk.set_led_colors(id, [CorsairLedColor(1+i, 255,0,255,50), CorsairLedColor(14+i, 255,0,255,50), CorsairLedColor(28+i, 255,0,255,100),CorsairLedColor(41+i, 255,0,255,50), CorsairLedColor(55+i, 255,0,255,50), CorsairLedColor(68+i, 255,0,255,50)])
        if (i==6):
            sdk.set_led_colors(id, [CorsairLedColor(129, 255,0,255,50)])
            finalImNormal.append(CorsairLedColor(129, 255,0,255,50))
            finalImBright.append(CorsairLedColor(129, 255,0,255,50))
        # add each key and color so we know what final image will look like
        finalImNormal.append(CorsairLedColor(14+i, 255,0,255,50))
        finalImNormal.append(CorsairLedColor(28+i, 255,0,255,50))
        finalImNormal.append(CorsairLedColor(41+i, 255,0,255,50))
        finalImNormal.append(CorsairLedColor(55+i, 255,0,255,50))
        finalImNormal.append(CorsairLedColor(68+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(1+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(14+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(28+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(41+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(55+i, 255,0,255,50))
        finalImBright.append(CorsairLedColor(68+i, 255,0,255,50))
        #sleep for delay
        time.sleep(0.05)



    finalImNormal.extend(lightningNormal)
    finalImBright.extend(lightningBright)
    #sdk.set_led_colors(id,[CorsairLedColor(1,250,250,51,255)])
    #lightning bolts for keyboard
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F2,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F5,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F9,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_2,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_6,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_0,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_Q,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_T,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_W,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_Y,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_P,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_E,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_BracketLeft,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_S,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_SemicolonAndColon,255,255,0,255)])
    time.sleep(0.075)
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_Z,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_B,255,255,0,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_PeriodAndBiggerThan,255,255,0,255)])
    time.sleep(0.2)

    sdk.set_led_colors(id,finalImNormal)
    time.sleep(0.1)
    sdk.set_led_colors(id,finalImBright)
    time.sleep(0.1)
    sdk.set_led_colors(id,finalImNormal)
    time.sleep(0.1)
    sdk.set_led_colors(id,finalImBright)
    time.sleep(0.1)
    sdk.set_led_colors(id,finalImNormal)
    time.sleep(0.1)
    sdk.set_led_colors(id,finalImBright)
    time.sleep(0.1)

    sdk.set_led_colors(id, getAll(0,0,0,0))

def iceLED(id):
    # on lights
    snowFirst = []
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F1,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F6,173,216,230,255)])
    time.sleep(0.1)

    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F1,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F6,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_2,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_7,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F4,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F9,173,216,230,255)])

    time.sleep(0.1)

    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F4,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F9,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_2,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_7,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_W,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_4,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_EqualsAndPlus,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F3,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F7,173,216,230,255)])

    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_W,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_4,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_EqualsAndPlus,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F3,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F7,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_S,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_R,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_BracketLeft,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_5,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_9,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F2,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F5,173,216,230,255)])

    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_S,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_R,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_BracketLeft,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_5,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_9,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F2,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F5,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_X,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_N,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_ApostropheAndDoubleQuote,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_T,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_I,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_4,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_7,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F1,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_F8,173,216,230,255)])

    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_X,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_N,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_ApostropheAndDoubleQuote,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_T,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_I,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_4,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_7,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F1,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_F8,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_Space,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_RightAlt,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_C,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_PeriodAndBiggerThan,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_G,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_K,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_R,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_1,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_0,173,216,230,255)])


    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_G,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_K,0,0,0,100), CorsairLedColor(CorsairLedId_Keyboard.CLK_PeriodAndBiggerThan,0,0,0,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_R,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,0,0,0,100)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_1,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_0,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_C,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_CommaAndLessThan,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_V,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_B,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_N,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_M,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_J,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_Q,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,173,216,230,255)])

    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_Q,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_F,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_G,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_H,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_J,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_K,173,216,230,255)])
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_S,173,216,230,255)])

    time.sleep(0.1)
    # off lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_S,0,0,0,100),CorsairLedColor(CorsairLedId_Keyboard.CLK_O,0,0,0,100)])

    #on lights
    sdk.set_led_colors(id,[CorsairLedColor(CorsairLedId_Keyboard.CLK_T,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_Y,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_U,173,216,230,255),CorsairLedColor(CorsairLedId_Keyboard.CLK_I,173,216,230,255)])
    time.sleep(0.07)

    sdk.set_led_colors(id, [CorsairLedColor(CorsairLedId_Keyboard.CLK_LeftCtrl,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_LeftGui,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_LeftAlt,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_LeftCtrl,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_RightGui,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_RightCtrl,173,216,230,255), CorsairLedColor(CorsairLedId_Keyboard.CLK_Fn,173,216,230,255), CorsairLedColor(74,173,216,230,255)])
    for j in range(9):
        i = j* -7
        sdk.set_led_colors(id, [ CorsairLedColor(55 + i,173,216,230,255), CorsairLedColor(56 + i,173,216,230,255), CorsairLedColor(57 + i,173,216,230,255), CorsairLedColor(58 + i,173,216,230,255), CorsairLedColor(59 + i,173,216,230,255), CorsairLedColor(60 + i,173,216,230,255), CorsairLedColor(61 + i,173,216,230,255), CorsairLedColor(62 + i,173,216,230,255), CorsairLedColor(63 + i,173,216,230,255), CorsairLedColor(64 + i,173,216,230,255), CorsairLedColor(65 + i,173,216,230,255), CorsairLedColor(66 + i,173,216,230,255), CorsairLedColor(67 + i,173,216,230,255)])
        time.sleep(0.04)
    sdk.set_led_colors(id, getAll(0,0,0,0))
         




if __name__ == "__main__":

    main()
    input()  # wait for <Enter>


