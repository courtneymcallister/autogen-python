import random
import json
import post_results

#8.NS.1.2 Pattern 2

def run():
	temp_item_list = []
	item_count = 0

	for i in range(100):
		a = random.randrange(2, 1000)
		while (a ** 0.5) % 1 == 0:
			a = random.randrange(2, 1000)
		stem_text = "Write `sqrt%d` as a decimal to the nearest tenth." % a

		correct_answer = round(a ** 0.5, 1)

		#put equation response items into the item list
		item_data = { 'stem' : stem_text, 'answers' : ['`' + str(correct_answer) + "`"] }
		item = {'type' : 'Equation Response', 'data' : item_data, 'comments' : "Answer is `" + str(correct_answer) + '`'}
		temp_item_list.append(item)

	#check that items are unique	
	item_list = []
	for item in temp_item_list:
		if item not in item_list and item_count < 100:
			item_list.append(item)	
			item_count += 1

	# set up complete data structure
	data = {} 
	data['standard'] = 'MAFS.8.NS.1.2'
	data['description'] = 'Write the square root of 735 as a decimal to the nearest tenth.'
	data['items'] = item_list

	#save to a JSON file
	f = open("8-NS-1-2-Pattern2_output.json", 'w')
	f.write(json.dumps(data, sort_keys=False, indent=4, separators=(',', ': ')))
	f.close()	

    # submit to the server
	post_results.post_results_to_dev_page('8.NS.1.2 Pattern 2', data)
print run()
