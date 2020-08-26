#Ryan Mackenzie
#IT140 - Intro to Scripting
#Search and Replace Script Final - updated patterns based on instructor feedback
#Febraury 26th, 2020

import re

lorem_ipsum = '''Lorem ipsum dolor sit-amet, consectetur adipiscing elit. Phasellus iaculis velit ac nunc interdum tempor. 
Ut volutpat elit metus, vel auctor enim commodo at. Nunc quis quam non ligula ultricies luctus porta id justo. 
Quisque dapibus est ut sagittis bibendum. Mauris ullamcorper pellentesque porttitor. Ut sit:amet ex nec dolor gravida 
porttitor. Proin at justo finibus justo vestibulum congue. Suspendisse et ipsum et ipsum eleifend dapibus a fermentum 
lacus. Vivamus porta nunc eu nisl sagittis, quis vulputate metus dignissim. Integer non fermentum nisl, id vestibulum 
elit. Sed euismod vestibulum purus ut porttitor. Integer sit-amet mollis neque. Donec sed lacinia diam, ac finibus 
lectus. Mauris tempor ipsum nisl, vitae posuere est lacinia nec. Nam eget euismod odio.'''

pattern= '[a-zA-Z0-9]'                              #Pattern selects spaces and non alphabet
results= re.findall(pattern, lorem_ipsum)           #Finds all instances and combines them
print(len(results))                                 #Counts the amount of non alphabet in the text

pattern= 'sit[:-]amet'        #Looks for sit amet including with any non alphabet in between.
occurrance_sit_amet= re.findall(pattern, lorem_ipsum)
print(len(occurrance_sit_amet))

pattern= 'sit[:-]amet'      #\s means spaces, \W means all special charachters
new = 'sit amet'              #The new string that will replace the old ones
replace_results= re.sub(pattern, new, lorem_ipsum)  #Finds all instances of the old sit amet, and replaces them
occurrance_sit_amet= re.findall(pattern, replace_results) #Combines the instances of the new sit amet
print(len(occurrance_sit_amet))