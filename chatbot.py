
import random

import webbrowser



greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]
def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)
print("Hello, I am GALEXA.I'm adopted son of GOOGLE and ALEXA.I'm your personal assistant:")
greeting_inputs = ("hey", "good morning", "good evening", "morning", "evening", "hi", "whatsup")
greeting_responses = ["hey", "hey hows you?", "*nods*", "hello, how you doing", "hello", "Welcome, I am good and you"]
continue_dialogue = True
while(continue_dialogue == True):
    human_text = input()
    human_text = human_text.lower()
    if human_text != 'bye':
        if human_text == 'thanks' or human_text == 'thank you very much' or human_text == 'thank you':
            print("GALEXA: Most welcome")
        else:
               if generate_greeting_response(human_text) != None:
                    print("GALEXA: " + generate_greeting_response(human_text))
                    print("Are you a parent (or) student (or) faculty?")
               if human_text=='student':
                                       print("These are the questions students usually ask:\n1.about iit dharwad?\n2.timetable?\n3.campus life?\n4.student life?\n5.Gallery\n")
               if human_text=='parent':
                                       print("These are the questions parents usually ask :\n1.about iit dharwad?\n2.Health services?\n3.Permanent campus\n4.List of holidays\n5.Gallery\n6.Testimonials\n")
               if human_text=='faculty':
                                        print("These are the questions faculty usually ask:\n1.about iit dharwad?\n2.Regarding faculty\n3.Faculty area of research\n4.workshops\n5.projects\n")
               if 'about iit dharwad' in human_text:
                             print("Damn!it wouldn't be nice if I say that over here,How then I'm afraid?\nGotcha!!!\nEnter yes!!")

               if  human_text=='yes': 
                             webbrowser.open('http://iitdh.ac.in/about.php', new=0) 
               if 'time table' in human_text:
                        print("OK!let me open it!\n Enter timetable")
               if  human_text=='time table':
                        webbrowser.open('http://iitdh.ac.in/academics_Timetable.php', new=0)
               if 'campus life' in human_text:
                        print("All the students are provided with on-campus hostel accommodation. A well-equipped dining hall is functioning and the second student mess will be ready soon at the upcoming gymkhana. Students are drawn from nearly 20 states across the country thus providing a holistic environment for their growth.")
                        print("IIT Dharwad has a 10% girl student population. Sports facilities are being setup on campus (volley ball, football, cricket etc.). In addition, students are permitted to use neighboring University of Agricultural Sciences grounds. Astronomy Club, Electronics Club, Music Club etc. are active. More facilities and activity centers will be ready shortly. Limited medical facilities have been arranged.")
                        print("you wanna see some photos of how is it in iit dharwad?\nEnter campus for it!")
                     
               if human_text=='campus':
                        webbrowser.open('https://www.iitdh.ac.in/campus-life.php', new=0)
               if 'student life' in human_text:
                       print("Well!There are lots of great things in iit dharwad,Students are involved in various competetions and there are some clubs too!!!Like Robotics,Astronomy etc\n")
                       print("If you want to know more about Click 'Yes1' for Robotics club\n 'Yes2' for Astronomy club\n")
               if human_text=='Yes1':
                       print("you can contact ramaprabhu for more info\n want his mail id?\nThen click mail id!!")
               if human_text=='mail id':
                       print("prabhurama@iitdh.ac.in\n")
                       print("you want photos to show?\n then click photos!!")
               if human_text=='photos':
                        webbrowser.open('https://www.iitdh.ac.in/students.php ', new=0)
               if 'photos of iit dharwad' in human_text:
                       print("You wanna see pictures of iit dharwad?")
                       print("yes?enter gallery!")
               if human_text=='gallery':
                       webbrowser.open('https://www.iitdh.ac.in/gallery.php', new=0)
               if 'health services' in human_text:
                        print("There are 5 doctors working in iit dharwad")
                        print("do you want to know their details?\nenter doctors!")
                       
               if human_text=='doctors':
                        webbrowser.open('https://www.iitdh.ac.in/HealthServices.php', new=0)
               if 'permanent campus' in human_text:
                        print("permanent campus of dharwad is process.I mean construction process!")
                        print("do you want to see photos of it?\ntype new campus")
                        
               if human_text=='new campus':
                         webbrowser.open('https://www.iitdh.ac.in/campus.php', new=0)
                        
               if 'holidays' in human_text:
                        print("Lot of students ask this question!!!hahaha...\n")
                        print("You wanna see..\ntype holidays")
               if human_text=='holidays':
                        webbrowser.open('https://www.iitdh.ac.in/academics_HolidayList.php', new=0)
               if 'director' in human_text:
                        print("IIT Dharwad director is P.Sheshu\nDo you want to know more about him?\n enter him!")
                        flag=1
               if human_text=='him':
                        webbrowser.open('https://www.iitdh.ac.in/director.php', new=0)
               if 'computer science faculty' in human_text:
                        print("there are 11 professors in computer science\nYou wanna know their names?type cse")
               if 'who teaches computer science students' in human_text:
                        print("there are 11 professors in computer science\nYou wanna know their names?type cse") 
               if human_text=='cse':
                        print("1.G Nagaraja\n2.Gayathri Ananthanarayanan\n3.Kedar Khandeparkar\n4.N.L.Sarda\n5.Nikhil Hegde\n6.Prabuchandran\n7.K J Rajshekar\n8.K Ramchandra Phawade\n9.Sandeep R.B\n10.SIBA NARAYANA SWAIN\n11.Sudheendra Hangal")
               if 'electrical engineering faculty' in human_text:
                           print("there are 10 professors in electrical engineering\nyou wannaknow their names!!!enter ee")
               if 'electrical engineering professors' in human_text:
                           print("there are 10 professors in electrical engineering\nyou wannaknow their names!!!enter ee") 
               if human_text=='ee':
                           print("1.Ajit T Kalgatgi\n2.Ameer K Mulla\n3.Bharath B. N\n4.Naveen Kadayinti\n5.Naveen M B\n6. Pratyasa Bhui\n7.Rajshekhar V Bhat\n8.Ruma Ghosh\n9.SR Mahadeva Prasanna\n10.Satish Naik Banavath") 
               if 'mechanical engineering faculty' in human_text:
                           print("there are 15 professors in mechanical engineering\nyou wanna know their names!!!enter me")
             
               if human_text=='me':
                           print("1.Amar Gaonkar \n2.C Amarnath \n3.Dhiraj V. Patil\n4.Keerthi M C\n5.Nagesh R Iyer \n6.P Seshu\n7.R Santhosh\n8.Samarth S. Raut\n9.Sangamesh Deepak R \n10.Shrikanth V \n11.Somashekara M A \n12.Sudheer Siddapureddy\n13.Surya Prakash Ramesh \n14.SV Prabhu \n15.Tejas Prakash Gotkhindi\n") 
               if 'dean ap' in human_text:
                           print("SV.Prabhu is Dean AP")
               if 'dean sw' in human_text:
                           print("BL.Tembe is Dean SW")
               if 'deanap' in human_text:
                           print("SV.Prabhu is Dean AP")
               if 'deansw' in human_text:
                           print("BL.Tembe is Dean SW")
               if 'dean of academic programmes' in human_text:
                           print("SV Prabhu is the dean of academic programmes!!!")
               if 'dean of student welfare' in human_text:
                           print("BL Tembe is the dean of student welfares")
               if 'dean of faculty welfare' in human_text:
                           print("SR Mahadeva Prasanna is the dean of faculty welfare")
               if 'dean of reasearch and development' in human_text:
                           print("SR Mahadeva Prasanna is the dean of research &development")
               if 'dean of infrastructure' in human_text:
                           print("Nagesh Iyer is the dean of that category")
               if 'where is iit dharwad' in human_text:
                           print(" WALMI Campus, PB Road, near High Court DHarwad, Karnataka 580011") 
               if 'founded' in human_text:
                           print("2016")  
               if 'chairman' in human_text:
                           print("R. Subrahmanyam")
               if 'who are you' in human_text:
                           print("I told you,Galexa") 
               if 'sports' in human_text:
                            print("IIT Dharwad Sports is supported by a Senior Sports Officer with two Physical Education Instructors along with seven part-time Coaches.\n")
                            print("want to look at some photos of players in IIT dharwad\n click 'sports'")
               if human_text=='sports':
                            webbrowser.open('http://iitdh.ac.in/about_sport.php',new=0)  
   

    else:
         continue_dialogue = False 
         print("GALEXA: Good bye and take care of yourself...")

#responses part
def generate_greeting_response(greeting):
    for token in greeting.split():
        if token.lower() in greeting_inputs:
            return random.choice(greeting_responses)














