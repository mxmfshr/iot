import pandas as pd
import curses
import time

res = [('0', 1, '123', 'today', 'in'),
       ('1', 2, '456', 'yesterday', 'out')]

df = pd.DataFrame(res, columns=['id','card_id','card_text','last_used', 'status'])

def logging(i):
    stdscr.addstr(0, 0, '{0}\nTest: {1}'.format(df, i))
    stdscr.refresh()

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    while True:
        try:
            for i in range(5):
                logging(i)
                time.sleep(1)
        finally:
            curses.echo()
            curses.nocbreak()
            curses.endwin()
