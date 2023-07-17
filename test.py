def add_time(start, duration, day=None):

    week_day = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    additional_info = ""
    
    # Cast start string to list
    start_time = start.split(" ")[0]
    am_pm = start.split(" ")[1]

    # Transform AM/PM hours to 24 hours time format
    start_hour = int(start_time.split(":")[0])
    start_min = int(start_time.split(":")[1])

    if start_hour >= 1 and start_hour <= 11 and am_pm == "PM":
        start_hour = start_hour + 12
    elif start_hour == 12 and am_pm == "AM":
        start_hour = 0

    #Cast duration string to list
    duration_hour = int(duration.split(":")[0])
    duration_min = int(duration.split(":")[1])

    #Add minutes
    add_min = start_min + duration_min

    # if add_min is more or equal 60 min add one hour to start_hours and reduce minutes format value
    if(add_min >= 60):
        add_min = add_min - 60
        start_hour += 1

    # Add hours and return exactly hour if one day or more
    add_hours = ((start_hour + duration_hour) / 24)

    # Obtain num of days
    num_of_days = int(add_hours)
        
    # we get the exact time on a specific day
    final_hours = round((((add_hours - num_of_days) * 100) * 24) / 100)

    # Add text to return if the numbers of day is more to 1    
    if num_of_days == 1:
        additional_info = " (next day)"
    elif num_of_days > 1:
        additional_info = " (" + str(num_of_days) + " days later)"

    # Add text to additional info just if the arguments function contain text day
    if day:
        if num_of_days == 0:
            additional_info =  ", " + day.title() + additional_info
        else:
            add_idx_week = week_day.index(day.title()) + num_of_days
            if add_idx_week <= 6:
                additional_info = ", " + week_day[add_idx_week] + additional_info
            else:
                final_idx = round((((add_idx_week / 7 - int(add_idx_week / 7)) * 100) * 7) / 100)
                additional_info = ", " + week_day[final_idx] + additional_info

    # Transform 24 hours to AM/PM Hours for Return
    rtn_hour = str(12) if final_hours == 0 else str(final_hours - 12) if final_hours > 12 else str(final_hours)
    rtn_min = str(add_min) if add_min >= 10 else "0" + str(add_min)
    rtn_am_pm = "PM" if final_hours >= 12 else "AM"

    return rtn_hour + ":" + rtn_min + " " + rtn_am_pm + additional_info



print(add_time("3:00 PM", "3:10"))
print(add_time("11:30 AM", "2:32", "Monday"))
print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
print(add_time("11:43 PM", "24:20", "tueSday"))
print(add_time("6:30 PM", "205:12"))
print(add_time("8:16 PM", "466:02", "tuesday"))





