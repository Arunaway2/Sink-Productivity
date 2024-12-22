Sink Productivity
ME 100 Electronics for the Internet of Things
Authors
Arun Yadavalli
Sink Productivity System Report Contents
Contents
1 Introduction 2
2 Design and Implementation 2
2.1 Components and Technologies Used . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Logic behind Components . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.3 System Logic . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
3 Results and Insights 3
3.1 User Positioning Feedback . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
4 Limitations 3
5 Future Improvements 3
5.1 Resolving Wi-Fi Issues . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
5.2 Water Usage Tracking . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
6 Project Resources 4
7 Conclusion 4
References 5
1
Sink Productivity System Report
1 Introduction
Sink Productivity is a simple system designed to monitor and improve how users spend their time at the sink.
It uses simple components connected through reliable communication protocols and basic forms of feedback
to help guide users to form positive habits around the sink.
The device aims to:
• Encourage proper hygiene by ensuring handwashing meets CDC recommendations.
• Promote efficient water use by notifying users of excessive dishwashing durations.
• Provide real-time audio feedback to keep users optimally positioned at the sink.
The device leverages ultrasonic sensors, ESP-NOW communication, Wi-Fi communication, and a buzzer
to monitor user behavior and provide both real-time feedback and directed messages to users.
2 Design and Implementation
2.1 Components and Technologies Used
• Ultrasonic Sensor (HC-SR04): Measures distance from the user to the sink.
• ESP-NOW Communication Protocol: Facilitates wireless communication between sensor and actuator
modules.
• PWM Signal Buzzer: Provides auditory feedback for real-time alerts.
• Umail package: Provides convenient way to write code to send emails to users.
2.2 Logic behind Components
Firstly, the HC-SR04 ultrasonic sensor’s role is to measure the distance between the user and the sink. This
sensor is effective for tasks like detecting the user’s proximity to the sink, which is essential for distinguishing
between handwashing and dishwashing activities. Given that the two tasks involve different durations and
user positions at the sink, the ultrasonic sensor gives precise and real-time data on the user’s distance.
The HC-SR04 was picked since it is reliable and, most importantly, free. The sensor’s 2 cm to 400 cm
range, with an accuracy of about 3 mm, is suitable for detecting the user’s proximity at typical sink distances.
Moreover, it provides a non-invasive and easy-to-implement solution for continuous distance measurement in
real-time, ensuring that the system can respond to user actions promptly.
The PWM buzzer’s role is to provide auditory feedback to users, guiding them toward desired behav-
iors. Given that the project focuses on habit formation and user positioning, the buzzer serves a dual
purpose—delivering both negative and positive feedback. The buzzer emits unpleasant feedback when the
user is incorrectly positioned, serving as a corrective measure, and it activates at varying frequencies to indi-
cate different levels of urgency (e.g., reminding users to wash hands or signaling excessive time spent washing
dishes).
The buzzer was picked since it gave a simple and reliable mode of auditory feedback. Its simplicity and
ease of integration into the system’s design make it a very practical solution without adding complexity or
high costs (Free).
2.3 System Logic
• Sensor Module: Continuously measures user distance from the sink and sends data to the actuator
module every 0.01 seconds.
• Actuator Module:
– Processes distance data in real-time.
2
Sink Productivity System Report
– Differentiates between tasks based on time thresholds.
– Activates the buzzer at different frequencies to indicate positional feedback.
– Tracks user’s duration washing as well as time of washing.
– Sends notifications to warn against water wastage after 6 minutes of dishwashing.
The device distinguished between handwashing and dishwashing activities based on the time spent near
the sink:
• Handwashing: Users staying at the sink for less than 30 seconds were classified as washing hands. A
prompt reminded them to wash for at least 20 seconds if necessary.
• Dishwashing: Users remaining at the sink for over 30 seconds were categorized as washing dishes. Alerts
were triggered if the duration exceeded 6 minutes.
3 Results and Insights
Sink Productivity’s basic PWM buzzer system works accurately, notifying users of improper positioning
relative to the sink. This functionality encourages positive habits by promoting single stays, thereby ensuring
an efficient use of the sink.
3.1 User Positioning Feedback
The system promotes habit formation by reinforcing positive behaviors and discouraging negative ones.
By incorporating habit stacking (a technique where you attach a new habit to one you already engage
in consistently), users can seamlessly integrate proper sink usage into their daily routines alongside other
established habits. The buzzer provides immediate unpleasant auditory feedback, utilizing what psychologists
refer to as operant conditioning (a scientifically-backed learning process where behaviors are influenced by
rewards or punishments) to discourage improper positioning at the sink. This real-time correction reinforces
the desired behavior of maintaining an optimal stance for efficiency and ergonomics. Additionally, a newly
introduced reward system offers positive reinforcement by delivering an uplifting and encouraging message to
users who consistently maintain optimal behavior. Email notifications act as a form of delayed reinforcement,
leveraging accountability to influence long-term habits. By warning users about excessive time spent washing
dishes, these notifications serve as reminders to conserve water and adopt more mindful practices. Together,
these mechanisms align with behavioral reinforcement theories to drive positive change.
4 Limitations
Even after adding a script that repeatedly tries connecting to the Wi-Fi, I ran into Wi-Fi internal errors, and
the issues limited the ability to provide some intended features such as sending emails with analytics of the
users washing as well messages. Despite changing from Berkeley-IoT to my hotspot, module functionality
remained unresolved.
5 Future Improvements
5.1 Resolving Wi-Fi Issues
• Test alternative hardware or firmware to address compatibility and interference problems.
• Implement robust debugging methods to identify and fix configuration errors.
3
Sink Productivity System Report 5.2 Water Usage Tracking
5.2 Water Usage Tracking
• Integrate an AdaFruit water flow sensor to provide real-time consumption data, complementing time-
based notifications.
• Encourage conservation by visualizing water usage patterns.
6 Project Resources
Project Video: (Insert link to prototype video)
Code Repository: (Insert link to MicroPython code)
Final Presentation Slides: (Insert link to slides)
Team Member: Arun Yadavalli (Solo Project)
7 Conclusion
The Sink Productivity Device successfully demonstrates how IoT technologies can promote efficient water
use and better hygiene practices. While hardware limitations restricted full implementation of advanced
features, the project highlights the potential for real-time feedback to shape everyday behaviors. This project
provided a valuable learning experience in IoT development, communication protocols, and user-centered
design. Thank you for the opportunity to explore this concept, and best wishes for a successful winter break!
4
Sink Productivity System Report References
References
[1] “Apa Dictionary of Psychology.” American Psychological Association, dictionary.apa.org/operant-
conditioning. Accessed 21 Dec. 2024.
[2] “Everything You Need to Know about Habit Stacking for Self-Improvement.” Cleveland Clinic, 2 July
2024, health.clevelandclinic.org/habit-stacking.
[3] “Ultrasonic Distance Sensor - 5V (HC-SR04).” SEN-15569 - SparkFun Electronics, Ada Fruit,
www.sparkfun.com/products/15569. Accessed 21 Dec. 2024.
5
