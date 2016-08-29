from .. import Child


c = Child.Child()

def test_haveParametersChanged():
	# Set up initial, relevant data in Child instance
	#c = Child.Child()
	c.oldGrammar = [0,0,0,0,0,1,1,1,1,1,0,0,0]
	c.grammar = [0,0,0,0,0,1,1,1,1,1,0,0,0]
	c.timeCourseVector = [[1,i] for i in range(1,14)]

	c.haveParametersChanged(5)

	# Assert that none of data has changed after
	# the function has run
	assert c.oldGrammar == [0,0,0,0,0,1,1,1,1,1,0,0,0]
	assert c.grammar == [0,0,0,0,0,1,1,1,1,1,0,0,0]
	assert c.timeCourseVector == [[1,i] for i in range(1,14)]

	# This grammar is the opposite of the original
	# and should cause the oldGrammar and timeCourseVector
	# to change after running haveParametersChanged
	c.grammar = [1,1,1,1,1,0,0,0,0,0,1,1,1]

	c.haveParametersChanged(6)

	# Assert oldGramar, grammar, and timeCourseVector
	# have changed accordingly
	assert c.oldGrammar == [1,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.grammar == [1,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.timeCourseVector == [[6,i] for i in range(1,14)]

	c.grammar = [0,1,1,1,1,0,0,0,0,0,1,1,1]

	c.haveParametersChanged(10)

	assert c.oldGrammar == [0,1,1,1,1,0,0,0,0,0,1,1,1]
	assert c.grammar == [0,1,1,1,1,0,0,0,0,0,1,1,1]
	temp1 = [[10,1]]
	temp2 = [[6,i] for i in range(2, 14)]
	assert c.timeCourseVector == temp1 + temp2


# Test various combinations of lists
# and values to draw out border cases
def test_findIndex():
	sampleList = [0,0,0]
	assert c.findIndex([0,0,0], 0) == 0
	assert c.findIndex([0,0,0], 0.01) == -1
	assert c.findIndex([0,0,434], 434) == 2
	assert c.findIndex([0,0,434], 435) == -1
	assert c.findIndex([0,0,434], 433) == -1