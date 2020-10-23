# Speech2Text

                           ____                       _     ____ _____         _   
                          / ___| _ __   ___  ___  ___| |__ |___ \_   _|____  _| |_ 
                          \___ \| '_ \ / _ \/ _ \/ __| '_ \  __) || |/ _ \ \/ / __|
                           ___) | |_) |  __/  __/ (__| | | |/ __/ | |  __/>  <| |_ 
                          |____/| .__/ \___|\___|\___|_| |_|_____||_|\___/_/\_\__|
                                |_|                                                

This is the solution of Assignment given by Kratin Software Solutions Pvt. Ltd

<h2>Install Required Libraries</h2>

pip install -r requirements.txt

<h2>How to Start ?</h2>
<ul>
<li>You need python 3.6> environment to run the script.</li>
<li>After installing required libraies</li>
<li>For windows | cmd python code.py</li>
<li>Internet is requird because we are using Google API.</li></ul>

<h2>Project Description</h2>
<p> when you run code.py model will ask for your name you have to tell the name by speaking, after that the model will show message and prompt to say something.then after speaking it will show you your text message(wait for some time till it shows) and model will create a .txt file of your text in textfiles folder and it will record your message in .mp3 file located at audiofiles folder then you can share your files anywhere.</p>

<h2>Note</h2>
<ul>
  <li>API used to convert speech to text, the Recognizer class has following method:</li>

<li>recognize_google(): Uses Google Speech API</li>
<li>To create audio file you can use different format</li>   
<li>just change the .mp3 extension to that format such as WAV, AIFF,FLAC,RAW</li>
</ul>

