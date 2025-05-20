# What is Threading in python and what is multi-processing in python?

# Normally when we write programs we tend to use only one thread. every process has a single thread which is called the main thread.
# what it does. it run the code sequentially

# but now if u have a code which u want to run couutnly and simously then u have to use multiprocessing threading 

# what is thread?
# thrread are typically basic unit of cpu uti;ozation
# a single procvessor have multiple thread runing 
#multiple codes runing at the same time, but all the thread share it process code data and files

# evey thread have its has different register and thier separate stack own its onw

# why or when threading is used

# main thread
# .
# .
# .
# while(thread)
#      displayScreen()
# .
# .
# .
# WHAT if u add heavy operatnion in while loop
# main thread
# .
# .
# .
# while(true)
#      // heavy operation
#      displayScreen()
# .
# .
# .
# you will have a screen flicker, which is not a user friendly

# while(true)
#      displayScreen()
# .
# .
# .
# WHAT if u add heavy operatnion in while loop
# main thread
# .
# .
# .
# while(true)
#      image = request(imageurl)
#      displayScreen()
# .
# .
# .
# network request take 1 second and ur screentake 1 second pop up
# main thread                         another thread
# Image = NULL
# .
# .
# .
# while(true)                         while (true)
#      image = request(imageurl)      image = request(imageurl)
#      displayScreen()
# .
# .
# .



# 