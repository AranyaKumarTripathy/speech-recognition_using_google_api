# Python program to translate 
# speech to text and text to speech 


import speech_recognition as sr 
import pyttsx3 
import string 

# Initialize the recognizer 
r = sr.Recognizer() 

# Function to convert text to 
# speech 

def main():
    print('wait for 3 sec then, speak "hello glass" to start the model and "exit" to make it sleep')
    conv()
def SpeakText(command): 
	
	# Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
	
	
# Loop infinitely for user to 

# speak 
def start_conv():
    with sr.Microphone() as source2: 
        
			
		# wait for a second to let the recognizer 
		# adjust the energy threshold based on 
		# the surrounding noise level 
        
        r.adjust_for_ambient_noise(source2, duration=0.2) 
            
		#listens for the user's input 
            
        audio2 = r.listen(source2) 
            
        print("converting to text")
			# Using ggogle to recognize audio 
           
        MyText = r.recognize_google(audio2) 
        MyText = MyText.lower() 
            
    return MyText

def conv():
    
    keyword = start_conv()
    if str.lower(keyword) == "hello glass":
        SpeakText("yes master, you can speak now")
        while(1):	 
        	
        	# Exception handling to handle 
        	# exceptions at the runtime 
            try: 
        		
        		# use the microphone as source for input. 
                with sr.Microphone() as source2: 
        			
        			# wait for a second to let the recognizer 
        			# adjust the energy threshold based on 
        			# the surrounding noise level 
                    r.adjust_for_ambient_noise(source2, duration=0.2) 
                    
                    
        			#listens for the user's input 
                    
                    audio2 = r.listen(source2) 
                    
                    print("converting to text")
        			# Using ggogle to recognize audio 
                   
                    MyText = r.recognize_google(audio2) 
                    MyText = MyText.lower() 
                    
                    if str.lower(MyText) == "exit":
                        SpeakText("thank u master , it was a nice talk")
                        break
                    
                    print("Did you say "+MyText) 
                    SpeakText(MyText) 
        			
            except sr.RequestError as e: 
                print("Could not request results; {0}".format(e)) 
        		
            except sr.UnknownValueError: 
                print("unknown error occured") 
if __name__ == "__main__":
    main()