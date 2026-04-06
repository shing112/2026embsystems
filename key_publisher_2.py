#!/usr/bin/env python3

import rospy
import keyboard
from std_msgs.msg import String

def main():
    rospy.init_node('key_publisher_node')
    pub = rospy.Publisher('/key_input', String, queue_size=10)

    print("""
         w
    a    s    d
         x
    s : stop   q : quit
    """)

    while not rospy.is_shutdown():

        if keyboard.is_pressed('q'):
            print("프로그램 종료")
            break

        elif keyboard.is_pressed('w'):
            msg = 'w'
            pub.publish(msg)
            print(f"전송 : {msg}")
            rospy.sleep(0.1)  # 키 입력 감지 후 잠시 대기

        elif keyboard.is_pressed('a'):
            msg = 'a'
            pub.publish(msg)
            print(f"전송 : {msg}")
            rospy.sleep(0.1)  # 키 입력 감지 후 잠시 대기


        elif keyboard.is_pressed('s'):
            msg = 's'
            pub.publish(msg)
            print(f"전송 : {msg}")
            rospy.sleep(0.1)  # 키 입력 감지 후 잠시 대기

        elif keyboard.is_pressed('d'):
            msg = 'd'
            pub.publish(msg)
            print(f"전송 : {msg}")

        elif keyboard.is_pressed('x'):
            msg = 'x'
            pub.publish(msg)
            print(f"전송 : {msg}")
            rospy.sleep(0.1)  # 키 입력 감지 후 잠시 대기

        else:
            print("잘못된 입력 → 프로그램 종료")
            break


if __name__ == '__main__':
    main()
