def Calculate_meet_Time(z):
    cockroach1=1                                #start form 1
    cockroach2=z+1                              #start form 100
    count=0                                     # Answer 38


    while cockroach1<cockroach2:
        if cockroach1 < cockroach2:
            if count % 5 ==0:                   # one step back
                cockroach2 = cockroach2 + 1
            if count % 10 == 0:                 # two step back
                cockroach1 = cockroach1 - 2
            cockroach1=cockroach1+1
            cockroach2=cockroach2-2

        else:
            cockroach1 = cockroach1 + 1
        if cockroach1<=cockroach2:
            count = count + 1

    return count


Distance_Between_cockroach=int(input("Enter Meter between rats "))
Display=Calculate_meet_Time(Distance_Between_cockroach)
print(Display)