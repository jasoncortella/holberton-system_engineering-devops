# 0x05. Processes and signals
## This directory contains answer files to [Holberton School](https://www.holbertonschool.com/) devops project 0x05

### 0. What is my PID
* a Bash script that displays its own PID.
* File: 0-what-is-my-pid

### 1. List your processes
* a Bash script that displays a list of currently running processes.
* File: 1-list_your_processes

### 2. Show your Bash PID
* a Bash script that displays lines containing the bash word
   * allowing you to easily get the PID of your Bash process
* File: 2-show_your_bash_pid

### 3. Show your Bash PID made easy
* a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash
* File: 3-show_your_bash_pid_made_easy

### 4. To infinity and beyond
* a Bash script that displays To infinity and beyond indefinitely
* File: 4-to_infinity_and_beyond

### 5. Kill me now
* a Bash script that kills 4-to_infinity_and_beyond process
* uses kill
* File: 5-kill_me_now

### 6. Kill me now made easy
* a Bash script that kills 4-to_infinity_and_beyond process
* does not use kill or killall
* File: 6-kill_me_now_made_easy

### 7. Highlander
* a Bash script that displays:
   * To infinity and beyond indefinitely
   * With a sleep 2 in between each iteration
   * I am invincible!!! when receiving a SIGTERM signal
* File: 7-highlander

### 8. Beheaded process
* a Bash script that kills the process 7-highlander
* File: 8-beheaded_process

### 9. Process and PID file
* a Bash script that:
   * Creates the file /var/run/holbertonscript.pid containing its PID
   * Displays To infinity and beyond indefinitely
   * Displays I hate the kill command when receiving a SIGTERM signal
   * Displays Y U no love me?! when receiving a SIGINT signal
   * Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
* File: 100-process_and_pid_file

### 10. Manage my process
* a manage_my_process Bash script that:
   * Indefinitely writes I am alive! to the file /tmp/my_process
   * In between every I am alive! message, the program should pause for 2 seconds
* File: 101-manage_my_process, manage_my_process

### 11. Zombie
* a C program that creates 5 zombie processes.
* For every zombie process created, it displays Zombie process created, PID: ZOMBIE_PID
* File: 102-zombie.c
