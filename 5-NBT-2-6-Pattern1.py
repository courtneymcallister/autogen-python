import random
import json
import post_results

#5.NBT.2.6 Pattern 1

item_list = []

def run():

	def comma(number): # returns a number (up to 9,999) with an asciimath comma
		if number >= 1000:
			number = str(number)
			return '{}","{}'.format(number[:1], number[1:])
		else:
			return number

	a = random.randint(11, 99)

	# set up the stem text
	stem_text = "Select all the expressions that have a value of `{}`.".format(a)

	# set up the correct answers
	answers = []
	for x in range(12, 50):
		product = a * x
		answers.append('`{} -: {}`'.format(comma(product), x))
	random.shuffle(answers)
	correct_answers = answers[:2]

	#set up the distractors
	distractor_list = []
	d_range = range(12, 50)
	d_addends = range(-10, 10)
	d_addends.remove(0)

	for x in range(3):
		divisor = random.choice(d_range)
		addend = a + random.choice(d_addends)
		distractor_list.append('`{} -: {}`'.format(comma(addend * divisor), divisor))

	# sort answers and put them into a list
	all_answer_choices = correct_answers + distractor_list
	all_answer_choices.sort(key=lambda item: (len(item), item)) #sort by length, then value
	list_answers = []
	for y in all_answer_choices:
		list_answers.append({'correct': y in correct_answers, 'text': y})

	#put items into the item list
	item_data = { 'stem' : stem_text, 'answers' : list_answers}
	item = {'type' : 'Multiple Select', 'data' : item_data, 'comments' : ''}

	while item in item_list:
		return False
	item_list.append(item)

while len(item_list) < 25:
	run()

# set up complete data structure
data = {}
data['standard'] = 'MAFS.5.NBT.2.6'
data['description'] = 'Find whole-number quotients of whole numbers with up to four-digit dividends and two-digit divisors.'
data['items'] = item_list

#save to a JSON file
f = open("5-NBT-2-6-Pattern1_output.json", 'w')
f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
f.close()	

# submit to the server
post_results.post_results_to_dev_page('5.NBT.2.6 Pattern 1', data)