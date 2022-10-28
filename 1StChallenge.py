import re
"""         Make sure it do not ask questions but when you press enter. it displays the result.
            Amount and formula has to be in one line.
                e.g 456 - 12
                    564/ 10
                    456*1234+09-12
"""

def Sum_of_Numbers(First_variable):
    x = re.split('(/|\*|-|\+)', First_variable)                          # Split string to small part
    a = []

    i = 0
    while("*" in x or "/" in x or "+" in x or "-" in x ):                          # Seperate Number and operater in different list
        if "*"== x[i] or "/" == x[i] or "+" == x[i] or "-" == x[i]:
            if (x[i]=="+"):
                a.append("+")
                x.pop(i)

                i=i+1

            elif (x[i] == "/"):
                a.append("/")
                x.pop(i)

                i = i + 1

            elif (x[i] == "-"):
                a.append("-")
                x.pop(i)

                i = i + 1

            elif (x[i] == "*"):
                a.append("*")
                x.pop(i)

                i = i + 1
            else:
                pass
        else:
            i = i + 1



    NewLenOFa=len(a)                                                     # Calculate the value
    while("*" in a or "/" in a or "+" in a or "-" in a):
        if "*" in a:
            for i in range(0,NewLenOFa):
                if (a[i]=="*"):
                    j=i+1
                    a.pop(i)
                    NewLenOFa=len(a)
                    b=int(x[i])*int(x[j])
                    x.pop(i)
                    x[i]=b

                    break

        elif "/" in a:
            for i in range(0,NewLenOFa):
                if (a[i]=="/"):
                    j=i+1
                    a.pop(i)
                    NewLenOFa=len(a)
                    b=int(x[i])/int(x[j])
                    x.pop(i)
                    x[i]=b
                    break

        elif "+" in a:
            for i in range(0,NewLenOFa):
                if (a[i]=="+"):
                    j=i+1
                    a.pop(i)
                    NewLenOFa=len(a)
                    b=int(x[i])+int(x[j])
                    x.pop(i)
                    x[i]=b
                    break
        else:
            for i in range(0,NewLenOFa):
                if (a[i]=="-"):
                    j=i+1
                    a.pop(i)
                    NewLenOFa=len(a)
                    b=int(x[i])-int(x[j])
                    x.pop(i)
                    x[i]=b
                    break

    return x


Send_Variable=str(input())
GetValue=Sum_of_Numbers(Send_Variable)
print(*GetValue)

