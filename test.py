#!/usr/bin/env python

workouts = {}


def store_workout(lift_type, when, *args):
	print lift_type, when, args

	exercises = workouts.get(when, None)

	if exercises is None:
		workouts[when] = {lift_type: args}
	else:
		if lift_type not in exercises:
			exercises[lift_type] = args
		else:
			exercises[lift_type] += args

while True:
	s = raw_input("> ")
	commands = s.split(' ')
	store_workout(*commands)