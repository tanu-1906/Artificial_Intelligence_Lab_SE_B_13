print("select the subject\nmaths\nphysics\nchemistry\nbiology\nprogramming\ncircuits\nstatistics.\nAI Concepts")
sub1 = input("choose the 1st subject: ")
sub2 = input("choose the 2nd subject: ")
if((sub1=="Maths" and sub2=="Physics") or (sub1=="Physics" and sub2=="Maths")):
	print("Suggest branch is Mechanical Engineering")
elif((sub1=="Maths" and sub2=="Programming") or (sub1=="Programming" and sub2=="Maths")):
	print("Suggest branch is Computer Engineering")
elif((sub1=="Circuits" and sub2=="Physics") or (sub1=="Physics" and sub2=="Circuits")):
	print("Suggest branch is Electrical Engineering")
elif((sub1=="Chemistry" and sub2=="Biology") or (sub1=="Biology" and sub2=="Chemistry")):
	print("Suggest branch is Biotechnology")
elif((sub1=="Statistics" and sub2=="Programming") or (sub1=="Programming" and sub2=="Statistics")):
	print("Suggest branch is Artificial Intelligence")
elif((sub1=="Programming" and sub2=="AI Concepts") or (sub1=="AI Concepts" and sub2=="Programming")):
	print("Suggest branch is Artificial Intelligence and Machine Learning")

	
