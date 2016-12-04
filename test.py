#!/usr/bin/env python

workouts = {}
goals = {}


def process_msg(message):
	commands = message.split(' ')

	if commands[1] == 'goal':
		store_goal(commands[0], commands[2:])
	else:
		store_workout(commands[0], commands[1], commands[2:])


def process_weight_reps(sets):
	weight_reps = []

	for weight, reps in (each_set.split('x') for each_set in sets):
		weight_reps.append({'weight': int(weight), 'reps': int(reps)})

	return weight_reps


def join_weights_reps(weight_reps_list):
	joined_weights_reps = []

	for each_set in weight_reps_list:
		joined_weights_reps.append('{weight}x{reps}'.format(**each_set))

	return ', '.join(joined_weights_reps)


def store_workout(lift_type, when, sets):
	weight_reps = process_weight_reps(sets)

	exercises = workouts.get(when, None)
	if exercises is None:
		workouts[when] = {lift_type: weight_reps}
	else:
		if lift_type not in exercises:
			exercises[lift_type] = weight_reps
		else:
			exercises[lift_type] += weight_reps

	print_workouts()

	lift_type_goals = goals.get(lift_type, [])

	for goal in lift_type_goals:
		for x in weight_reps:
			if x['reps'] >= goal['reps'] and x['weight'] >= goal['weight']:
				print 'YAY! You hit your goal of {weight}x{reps}'.format(**goal)


def print_workouts():
	for when, exercises in workouts.iteritems():
		print when

		for lift_type, lifts in exercises.iteritems():
			weight_reps = join_weights_reps(lifts)
			print "%s: %s" % (lift_type, weight_reps)
		print


# {'deadlift': [ {'weight': 100, 'reps': 1}, {'weight': 50, 'reps': 2} ] }


def store_goal(lift_type, new_goals):
	weight_reps = process_weight_reps(new_goals)

	if lift_type not in goals:
		goals[lift_type] = weight_reps
	else:
		goals[lift_type] += weight_reps

	print_goals()


def print_goals():
	for lift_type, goal_list in goals.iteritems():
		weight_reps = join_weights_reps(goal_list)
		print "%s goal: %s" % (lift_type, weight_reps)
	print


while True:
	s = raw_input("> ")
	process_msg(s)