#!/usr/bin/python
print('''
1) Shetland Pony      4) Connemara Pony	    7) About Us
2) Dartmoor Pony      5) General Facts	    8) Acknowledgements
3) Highland Pony      6) Quiz               9) Quit
''')

likeRead = input("What would you like to read? ")

if likeRead.lower() in ['1', 'one', 'shetland pony', 'shetland ponies']:
    exec(open("shet.py").read())
elif likeRead.lower() in ['2', 'two', 'dartmoor pony', 'dartmoor ponies']:
    exec(open("dart.py").read())
elif likeRead.lower() in ['3', 'three', 'highland pony', 'highland ponies']:
    exec(open("high.py").read())
elif likeRead.lower() in ['4', 'four', 'connemara pony', 'connemara ponies']:
    exec(open("conn.py").read())
elif likeRead.lower() in ['5', 'five', 'general facts']:
    exec(open("gen.py").read())
elif likeRead.lower() in ['6', 'six', 'quiz']:
    exec(open("quiz.py").read())
elif likeRead.lower() in ['7', 'seven', 'about us']:
    exec(open("about.py").read())
elif likeRead.lower() in ['8', 'eight', 'acknowledgements']:
    exec(open("ack.py").read())
elif likeRead.lower() in ['9', 'nine', 'quit']:
    exec(open("quit.py").read())
else:
    print("Please choose a valid option from the menu")
    exec(open("menu.py").read())
