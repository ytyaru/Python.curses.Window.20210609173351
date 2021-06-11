#!/usr/bin/env python3
# coding: utf8
import os, curses

# curses.doupdate()を使う。window.refresh()でも行われるため、２つ以上のwindowがないと効果がない。２つの窓を用意してみた。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index

        self.__init_cursor()
        self.__init_color_pair()

        self.__screen_sub1 = screen.subwin(curses.LINES, curses.COLS, 0, 0)
        self.__new1 = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        self.__new1_sub1 = self.__new1.subwin(curses.LINES, curses.COLS, 0, 0)
#        self.__win = curses.newwin(curses.LINES, curses.COLS)
#        self.__win = screen.subwin(curses.LINES, curses.COLS)
#        self.__win = screen.subwin(curses.LINES-1, curses.COLS-1)
#        self.__win = screen.subwin(curses.LINES-1, curses.COLS-1, 0, 0)
        self.__new2 = curses.newwin(curses.LINES, curses.COLS, 0, 0)
        self.__new2_sub1 = self.__new2.subwin(curses.LINES, curses.COLS, 0, 0)
        self.__init_cursor()

        self.__screen.noutrefresh()
        self.__new1.noutrefresh()
        self.__new1_sub1.noutrefresh()

        self.__screen.attron(curses.A_REVERSE | curses.color_pair(1))
        self.__screen.addstr('screen')

        self.__screen_sub1.attron(curses.A_REVERSE | curses.color_pair(2))
        self.__screen_sub1.addstr(1, 0, 'stdscr-subwin')

#        self.__new1.addstr('new1')
#        self.__new1.attron(curses.A_REVERSE | curses.color_pair(3))

#        self.__new1_sub1.addstr('new1-sub1')
#        self.__new1_sub1.attron(curses.A_REVERSE | curses.color_pair(4))

        curses.doupdate()
#        self.__draw()
        self.__input()
    def __init_cursor(self): curses.curs_set(0)
    def __init_color_pair(self):
        if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
        if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
        curses.use_default_colors()
        for i in range(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
    def __draw(self):
        self.__screen.noutrefresh()
        self.__screen_sub1.noutrefresh()
        self.__new1.noutrefresh()
        self.__new1_sub1.noutrefresh()

        self.__screen.clear()
        self.__screen.attron(curses.A_REVERSE | curses.color_pair(1))
        self.__screen.addstr(0, 0, 'screen')

        self.__screen_sub1.clear()
        self.__screen_sub1.attron(curses.A_REVERSE | curses.color_pair(2))
        self.__screen_sub1.addstr(1, 1, 'screen-sub1')

        self.__new1.clear()
        self.__new1.attron(curses.A_REVERSE | curses.color_pair(3))
        self.__new1.addstr(2, 2, 'new1')

        self.__new1_sub1.clear()
        self.__new1_sub1.attron(curses.A_REVERSE | curses.color_pair(4))
        self.__new1_sub1.addstr(3, 3, 'new1-sub1')

        curses.doupdate()

    def __input(self):
        while True:
            key = self.__screen.getch()
            if ord('q') == key: break
            self.__draw()


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

