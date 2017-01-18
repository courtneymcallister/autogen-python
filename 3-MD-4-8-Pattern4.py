import random
import json
import post_results
import nameslist

#3.MD.4.8 Pattern 4

item_list = []

def run():

	def factors(n):
		result = []
		for i in range(1, n + 1):
			if n % i == 0:
				result.append(i)
		return result

	a = random.randint(2, 10)
	b = random.randint(2, 10)
	area = a * b
	name = nameslist.random_name()

	#set up the stem text
	rectangles = ['sticky note', 'blanket', 'plot of land', 'piece of wood', 'swimming pool']
	rect = random.choice(rectangles)

	if rect == 'sticky note':
		unit = 'centimeters'
	elif rect == 'plot of land':
		unit = 'kilometers'
	else:
		unit = 'feet'

	stem_text = "{} has a rectangular {} with an area of `{}` square {}. Select all of the \
	possible lengths and widths of {}'s {}.".format(name, rect, area, unit, name, rect)

	# set up the correct answers
	correct_answers = []
	area_factors = factors(area)
	for i in range(len(area_factors)):
		length = area_factors[i]
		width = area / length
		if 1 < length < 11 and 1 < width < 11:
			 correct_answers.append('`{}` {} long by `{}` {} wide'.format(length, unit, width, unit))

	if len(correct_answers) < 2:
		return False

	# set up the distractors
	distractor_list = []
	perimeter = (2 * a) + (2 * b)
	max_length = 10
	max_width = (perimeter / 2 ) - 10
	d_list = []
	for i in range(9):
		p = max_length - i
		q = max_width + i
		if 1 < p < 11 and 1 < q < 11:
			distractor_list.append('`{}` {} long by `{}` {} wide'.format(p, unit, q, unit))	
	if b - 1 > 1:
		distractor_list.append('`{}` {} long by `{}` {} wide'.format(a + 2, unit, b - 1, unit))
	if b - 2 > 1:
		distractor_list.append('`{}` {} long by `{}` {} wide'.format(a + 1, unit, b - 2, unit))
	if a - 2 > 1:
		distractor_list.append('`{}` {} long by `{}` {} wide'.format(a - 2, unit, b + 1, unit))
	if a - 1 > 1:
		distractor_list.append('`{}` {} long by `{}` {} wide'.format(a - 1, unit, b + 2, unit))

	uq_distractors = []
	for distractor in distractor_list:
		if distractor not in uq_distractors and distractor not in correct_answers:
			uq_distractors.append(distractor)

	if len(uq_distractors) < 3:
		return False

	random.shuffle(uq_distractors)
	answer_choices = [correct_answers[0], correct_answers[1], uq_distractors[0], uq_distractors[1], uq_distractors[2]]
	if len(uq_distractors) > 3:
		answer_choices.append(uq_distractors[3])
	if len(correct_answers) > 2:
		answer_choices.append(correct_answers[2])
	answer_choices.sort()

	list_answers = []
	for ans in answer_choices:
		list_answers.append({'correct': ans in correct_answers, 'text': ans})

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
data['standard'] = 'MAFS.3.MD.4.8'
data['description'] = 'Solve real world and mathematical problems involving perimeters of polygons.'
data['items'] = item_list

#save to a JSON file
f = open("3-MD-4-8-Pattern4_output.json", 'w')
f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
f.close()	

# submit to the server
post_results.post_results_to_dev_page('3.MD.4.8 Pattern 4', data)	