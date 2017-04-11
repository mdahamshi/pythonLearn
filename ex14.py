from sys import argv

script, uname = argv
prompt = 'THERE_IS_NO_GOD> '

print "Hi %s, I'm %s script." %(uname, script)
print "I'd like to ask you a few questions."

print "Do you like me %s?" %uname 
likes = raw_input(prompt)

print "Where do you live %s?" %uname
lives = raw_input(prompt)

print "What kind of computer you have?"
pc = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r, Not sure where that is.
And you have a %r computer. Nice.
""" %(likes, lives, pc)

