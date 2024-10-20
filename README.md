This program works by utilizing four different functions, a while loop, and some good ole' if/elif statements.
When ran the welcome message appears, then the while loop kicks off with the display menu. Using the while loop will allow the user to keep using the program until they want to quit. 

user_choice is an integer input. I use a try/except block to deal with possible errors such as the user inputting a string.
From there, the if/elif statements commence. 

When adding_task() is called, the user will enter a string response otherwise, my try/except block will handle the error. The input is then added to the incomplete list.

delete_task() functions the same as the adding_task() only it removes a task from the incomplete list.

view_task() will print both the incomplete and complete lists. If a list is empty, a message will appear saying so.

completed_task() does a few things: It will add the completed task to the completed list, check if it is in the incomplete list, if so it will remove the entry from that list. If the task is not in the incomplete list, a message will print saying so.

Should the user select 5, the program will thank the user for using the application and break the loop.
