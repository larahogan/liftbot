#!/usr/bin/env python

workouts = {}
goals = {}


def process_msg(message):
	commands = message.split(' ')

	if commands[1] == 'goal':
		store_goal(commands[0], commands[2:])
	else:
		store_workout(commands[0], commands[1], commands[2:])


def store_workout(lift_type, when, sets):
	exercises = workouts.get(when, None)

	if exercises is None:
		workouts[when] = {lift_type: sets}
	else:
		if lift_type not in exercises:
			exercises[lift_type] = sets
		else:
			exercises[lift_type] += sets

	print_workouts()


def print_workouts():
	for when, exercises in workouts.iteritems():
		print when
		for lift_type, lifts in exercises.iteritems():
			print "%s: %s" % (lift_type, ', '.join(lifts))
		print


def store_goal(lift_type, new_goals):
	if lift_type not in goals:
		goals[lift_type] = new_goals
	else:
		goals[lift_type] += new_goals

	print_goals()


def print_goals():
	for lift_type, goal in goals.iteritems():
		print "%s: %s" % (lift_type, ', '.join(goal))
	print


while True:
	s = raw_input("> ")
	process_msg(s)