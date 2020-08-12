# Creating Dictionary in Syetem , will take input from user and return the meaning of the word
d = {"sets":"Collection of words", "delima":"Confusion","rizwan":"Janath ka Darogha"}
#print(dictionary)
while True:
    u = input("Search For the Meaning : ")
    key = u.lower()
    if key=="done":
        break
    try:
        if key in d.keys():
            print("The Meaning of", key, "is", d[key])
        else:
            print("Sorry!")
    except:
        print("Invalid Input")
