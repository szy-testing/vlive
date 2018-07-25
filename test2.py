# coding:utf8
import gevent


def win():
    return 'You win!'


def fail():
    raise Exception('You failed!')


winner = gevent.spawn(win)
loser = gevent.spawn(fail)
print winner.ready()
print loser.ready()

# try:
#     gevent.joinall([winner,loser])
# except Exception as e:
#     print "this will never be reached"
print winner.started  # True
print loser.started  # True
print winner.successful() # True
print loser.successful()  # False
print winner.value # 'You win!'
print loser.value  # None
