# -*- coding: utf-8 -*-
# Quick Pytohn Script Explanation for progeammers
# 给程序员的超快速Py脚本解说
import os

def main():
    print 'Hello World!'
    
    print "这是Alice\'的问候."
    print '这是Bob\'的问候.'
    
    foo(5, 10)
    
    print '=' * 10
    print '这将直接执行'+os.getcwd()
    
    counter = 0
    counter += 1
    
    food = ['苹果', '杏子', '李子', '梨']
    for i in food：
        print '俺就爱整只：'+i
    
    print '数到10'
    for i in range(10):
        Print i
      
def foo (paraml, secondParam):
    res = paraml+secondParam
    print '%s 加 %s 等于 %s%(paraml, secondParam, res)
    if  res < 50:
        print '这个'
    elif (res>=50) and ((paraml==42) or (secondParam==24)):
        print '那个'
    else:
        print '嗯...'
    return res # 这是单行注释
    '''这是多
    行注释......'''
    
  if ____name____=='____main____':
      main()
