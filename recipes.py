#!/usr/bin/env python

def list():
    recipes = ['1: peachango', '2: tigersblood']
    print recipes[0]
    print recipes[1]

def peacha(s):
    jp = 0.05 * s
    ma = 0.05 * s
    pi = 0.03 * s
    mm = 0.03 * s

    print jp, '- Juicy Peach'
    print ma, '- Mango'
    print pi, '- Pineapple'
    print mm, '- Marshmellow'

def tigersblood(s):
    st = 0.06 * s
    wm = 0.02 * s
    co = 0.02 * s

    print 'strawberry', st
    print 'watermelon', wm
    print 'double coconut', co
