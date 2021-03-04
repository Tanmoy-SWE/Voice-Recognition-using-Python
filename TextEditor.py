from pathlib import Path
fh = open("TextFromAudio.txt",'r')
s = fh.read()
s.replace( ", ","COMMA")
s.replace( ". ", "FULL STOP")
s.replace( "? ", "QEUSTION MARK")
s.replace( ": ", "SEMICOLON")
s.replace("(","BRACKET START")
s.replace(")","BRACKET END")
s.replace('\n',"NEXT LINE")
badwords = ["FUCK", "PUSSY", "DICK", "BLOWJOB",
            "BOOBS", "COCK", "VAGINA", "BUTTS"]
for i in badwords :
    p = len(i)
    s.replace(p*"*", i)
print(s)
fh = open("TextFromAudio.txt", 'w')
fh.write(s)