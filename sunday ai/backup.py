        f = open("sunday.txt","r")
        s = f.readlines()
        i=0
        while(i<len(s)):
            y = s[i].split(" ans")
            if(y[0] in command ):
                x = s[i].split("ans ")
                return x[1]
    
            i = i + 1 
        f.close()
        print("sorry i don't know could you please tell me the ans") 
        talk("sorry i don't know could you please tell me the answer")
        commandans = listen()
        f = open("sunday.txt" , "a")
        f.write(command  +" ans " +commandans + "\n")
        return ""