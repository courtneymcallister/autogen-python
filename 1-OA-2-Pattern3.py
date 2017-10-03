import json
import random
import post_results
import nameslist

#1.OA.1.2 multiple choice Pattern 3

item_list = []

def run():
	red_circle = '&#128308;'
	blue_circle = '&#128309;'

	a = random.randrange(1, 20)
	b = random.randrange(1, 20)
	c = random.randrange(1, 20)
	while a + b + c > 20:
		a = random.randrange(1, 20)
		b = random.randrange(1, 20)
		c = random.randrange(1, 20)

	correct_answer = a + b + c

	name1 = nameslist.random_name()
	name2 = nameslist.random_name()
	name3 = nameslist.random_name()
	while name1 == name2 or name1 == name3 or name2 == name3:
		name1 = nameslist.random_name()
		name2 = nameslist.random_name()
		name3 = nameslist.random_name()

	obj_a = 'points'
	obj_b = 'points'
	obj_c = 'points'

	if a == 1:
		obj_a = 'point'
	if b == 1:
		obj_b = 'point'
	if c == 1:
		obj_c = 'point'

	red_table_cell = '<td style="text-align:center;">&nbsp;{}&nbsp;</td>'.format(red_circle)
	blue_table_cell = '<td style="text-align:center;">&nbsp;{}&nbsp;</td>'.format(blue_circle)
	empty_cell = '<td>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</td>'

	#set up logic for filling in the double ten frame
	if a <= 5:
		row1 = red_table_cell * a
		if a + b <= 5:
			if a + b == 5:
				remaining_cells1 = (blue_table_cell * b)
			else:
				remaining_cells1 = (blue_table_cell * b) + (empty_cell * (5 - a - b))
			row2 = empty_cell * 5
			row3 = empty_cell * 5
			row4 = empty_cell * 5
		elif a + b <= 10:
			if a + b == 10:
				remaining_cells1 = blue_table_cell * (5 - a)
				row2 = blue_table_cell * 5
			else:
				remaining_cells1 = blue_table_cell * (5 - a)
				row2 = (blue_table_cell * (a + b - 5)) + (empty_cell * (10 - a - b))
			row3 = empty_cell * 5
			row4 = empty_cell * 5
		elif a + b <= 15:
			if a + b == 15:
				remaining_cells1 = blue_table_cell * (5 - a)
				row2 = blue_table_cell * 5
				row3 = blue_table_cell * 5
			else:
				remaining_cells1 = blue_table_cell * (5 - a)
				row2 = blue_table_cell * 5
				row3 = (blue_table_cell * (a + b - 10)) + (empty_cell * (15 - a - b))
			row4 = empty_cell * 5
		else:
			remaining_cells1 = blue_table_cell * (5 - a)
			row2 = blue_table_cell * 5
			row3 = blue_table_cell * 5
			row4 = (blue_table_cell * (a + b - 15)) + (empty_cell * (20 - a - b))
		row1 = row1 + remaining_cells1

	elif a <= 10:
		row1 = red_table_cell * 5
		row2 = red_table_cell * (a - 5)
		if a + b <= 10:
			if a + b == 10:
				remaining_cells2 = (blue_table_cell * b) 
			else:
				remaining_cells2 = (blue_table_cell * b) + (empty_cell * (10 - a - b))
			row3 = empty_cell * 5
			row4 = empty_cell * 5
		elif a + b <= 15:
			if a + b == 15:
				remaining_cells2 = blue_table_cell * (10 - a)
				row3 = blue_table_cell * 5
			else:
				remaining_cells2 = blue_table_cell * (10 - a)
				row3 = (blue_table_cell * (a + b - 10)) + (empty_cell * (15 - a - b))
			row4 = empty_cell * 5
		else:
			remaining_cells2 = blue_table_cell * (10 - a)
			row3 = blue_table_cell * 5
			row4 = (blue_table_cell * (a + b - 15)) + (empty_cell * (20 - a - b))
		row2 = row2 + remaining_cells2
	
	elif a <= 15:
		row1 = red_table_cell * 5
		row2 = red_table_cell * 5
		row3 = red_table_cell * (a - 10)
		if a + b <= 15:
			if a + b == 15:
				remaining_cells3 = blue_table_cell * b
			else:
				remaining_cells3 = (blue_table_cell * b) + (empty_cell * (15 - a - b))
			row4 = empty_cell * 5
		else:
			remaining_cells3 = blue_table_cell * (15 - a)
			row4 = (blue_table_cell * (a + b - 15)) + (empty_cell * (20 - a - b))
		row3 = row3 + remaining_cells3
	
	else:
		row1 = red_table_cell * 5
		row2 = red_table_cell * 5
		row3 = red_table_cell * 5
		row4 = red_table_cell * (a - 15)
		row4 = row4 + (blue_table_cell * b) + (empty_cell * (20 - a - b))

	table1 = '<table border="1" width="150" height="62"><tr>{}</tr><tr>{}</tr></table>'.format(row1, row2)
	table2 = '<table border="1" width="150" height="62"><tr>{}</tr><tr>{}</tr></table>'.format(row3, row4)

	ten_frame = '<table style="margin-left:30pt;"><tr><td>{}</td><td>{}</td></tr></table>'.format(table1, table2)

	stem_text = "{}, {}, and {} are on a team. {} scored {} {}. {} scored {} {}.<br><br>{}<br><br>{} scored {} {}. How many points did their team score all together?".format(name1, name2, name3, name1, a, obj_a, name2, b, obj_b, ten_frame, name3, c, obj_c)

	#set up distractors
	distractors = [a + b, a + c, b + c]
	distractors = list(set([d for d in distractors if d > 0]))
	random.shuffle(distractors)
	distractors = distractors[:2]

	answer_choices = list(set(distractors + [correct_answer]))
	answer_choices.sort()
	list_answers = []
	for ans in answer_choices:
		list_answers.append({'correct': ans == correct_answer, 'text': ans})
	if len(list_answers) != 3:
		return False

	#put items into the item list
	item_data = { 'stem' : stem_text, 'answers' : list_answers }
	item = {'type' : 'Multiple Choice', 'data' : item_data, 'comments' : "Answer is " + str(correct_answer)}

	#discard duplicates
	if item in item_list:
		return False
	item_list.append(item)

#return 20 items
while len(item_list) < 20:
	run()

# set up complete data structure
data = {}

# # upload info
# data['uploadInfo'] = {}
# # # data['uploadInfo']['itemBankName'] = ''
# data['uploadInfo']['categoryList'] = {}
# data['uploadInfo']['categoryList']['CCSS - Math - Grade 1'] = ["1.OA.2"]
# data['uploadInfo']['categoryList']['CCSS - Mathematical Practice Standards'] = ["MP.1"]
# data['uploadInfo']['categoryList']['New TEKS - Math - Grade 1'] = ["2.1.5.G"]
# data['uploadInfo']['categoryList']['New TEKS - Math - Grade 1 - Process Skills'] = ["1.1.A", "1.1.B"]
# data['uploadInfo']['categoryList']['Cognitive Complexity'] = ["2"]
# data['uploadInfo']['categoryList']['Bloom\'s Taxonomy'] = ["Apply"]
# data['uploadInfo']['categoryList']['Quantile Measure'] = ["EM80Q"]

data['standard'] = 'MAFS.1.OA.2'
data['description'] = 'INCOMPLETE'
data['items'] = item_list

#save to a JSON file
f = open("1-OA-2-Pattern3_output.json", 'w')
f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
f.close()	

# submit to the server
post_results.post_results_to_dev_page('1.OA.2 Pattern 3', data)