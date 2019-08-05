# kills a process named killmenow

exec { 'pkill -f killmenow':
     path => '/bin/:/usr/bin/:/usr/local/bin/'
}