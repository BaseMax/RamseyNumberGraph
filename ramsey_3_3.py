###
 # 1.0
 # 2019-07-15
 # Max
 # https://github.com/BaseMax/RamseyNumber
 ###
import math
import random
import sys
limitc=0
sys.setrecursionlimit(15000)
def R(art, *shapes):
	print("R(" + ", ".join(map(str,shapes)) + ") ?= " + str(art))
	vertices=list()
	lenShapes=len(shapes)
	for i in range(1, art+1):
		vertices.append(i)
	print("Art: " + str(art) + "k" )
	print("Shapes: " + "k, ".join(map(str,shapes)) + ("k" if lenShapes > 0 else "") + " (" + str(lenShapes) + 
")")
	print("Vertices of the graph: " + str(vertices))
	e=list()
	edgesSize=math.factorial(art) / ( math.factorial(art-lenShapes) * math.factorial(lenShapes) )
	print(edgesSize)
	edges=list()
	l=0
	for i in range(art):
		for j in range(i+1, art):
			edges.append( [i+1, j+1, None] )
			l+=1
	print("Edges of the graph: " + str(edges))
	# while True:
	#limit=20
	#limitc=0
	def check():
		#global limit
		global limitc
		limitc+=1
		if limitc == 10000:
			print("\nLimit.....")
			sys.exit()
		for edge in edges:
			edge[2]=random.randint(0, lenShapes-1)
		print("\n")
		print("Colorize edges of the graph: " + str(edges))
		# for shape in shapes:
		# 	print(shape)
		def found(i, j):
			# for edge in edges:
			for index, edge in enumerate(edges):
				# if edge[0] == i and edge[1] == j:
				if (edge[0] == i and edge[1] == j) or (edge[0] == j and edge[1] == i):
					# print(edge[0])
					return edge[2]
					# return index
			return None
		# print( found(1, 2) )
		q=0
		items=list()
		print("start...\n")
		for i in range(art):
			for j in range(i+1, art):
				for l in range(j+1, art):
					items.append( list() )
					# e.g: shapes[0] is 3 1 / 3
					items[q].append( (i+1, j+1) )
					# 2 / 3
					items[q].append( (i+1, l+1) )
					# 3 / 3
					items[q].append( (j+1, l+1) )
					q+=1
		# print(items) print("\n")
		print(".....\n")
		sameColor=0
		for item in items:
			print(item)
			checkContinue=True
			result=True
			color=None
			for item_child in item:
				# print(item_child)
				if color is None:
					color=found(item_child[0], item_child[1])
					# print(color)
					sys.stdout.write(str(color))
					continue
				else:
					tcolor=found(item_child[0], item_child[1])
					sys.stdout.write(" " + str(tcolor))
					# print(" " + str(tcolor))
					if tcolor is not color:
						# print(str(color) + " => Break")
						sys.stdout.write(" Break")
						checkContinue=False
						break
			# We has some edges with a (one) color.
			if checkContinue is True:
				sys.stdout.write(" OK")
				sameColor+=1
				check()
				return
			print("")
				# return break
			#else:
				#print("Colorize edges of the graph: " + str(edges)) check() break
			# return continue check() print(item[0]) print(item[1]) print(item[2])
		print("===> " + str(sameColor))
		# while True: break
		if sameColor is 0:
		    print("Done")
		    print("Colorize edges of the graph: " + str(edges))
		    sys.exit()
		    return False
		#limitCurrent+=1
		#if limitCurrent >= limit:
		#    print("Limit...")
		#    sys.exit()
    	check()
	check()
r=R(6, 3, 3)
#r=R(5, 3, 3)
print(r)
