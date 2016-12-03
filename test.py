#!/usr/bin/env python

def store_workout(lift_type, when, *args):
	print lift_type, when, args


while True:
	s = raw_input("> ")
	commands = s.split(' ')
	store_workout(*commands)