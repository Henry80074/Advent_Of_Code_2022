f = open("6_input.txt", "rt")
datastream = f.readlines()[0]

def start_of_packet(datastream):
    for i in range(0, len(datastream)):
        packet = datastream[i:i+4]
        if len(list(set(packet))) == len(list(packet)):
            return(i+4)

def start_of_message(datastream):
    for i in range(0, len(datastream)):
        message = datastream[i:i+14]
        if len(list(set(message))) == len(list(message)):
            return(i+14)

print(start_of_packet(datastream))
print(start_of_message(datastream))