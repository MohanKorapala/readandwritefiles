def main():
    infile = open("clients.txt", "r")
    
    counter = 1
    for client in infile:
        print(counter,'.', client.rstrip('\n'),sep="")
        counter += 1
        
    #my solution:
    #num = int('0')
    #for line in infile:
    #    num += 1
    #   print(num,'.',  line,sep='')
              
    infile.close()

main()