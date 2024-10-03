#########################################################
#  Exercise 1: Function converts milliseconds to hours:minutes:seconds
#########################################################

def convert_millis(m):
    hours = str(round(m // 3600000))
    minutes = str(round((m % 3600000) // 60000))
    seconds = str(round((m % 60000) // 1000))
    print(hours + ":" + minutes + ":" + seconds)


milliseconds = int(input("Enter a value for milliseconds:"))
convert_millis(milliseconds)
