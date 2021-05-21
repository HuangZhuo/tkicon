#!/usr/bin/python3
# -*- encoding: utf-8 -*-
import os
import sys
import base64
import re

FILENAME = 'tk.ico'
FILEDATA = '''AAABAAEAEBAAAAEAIABoBAAAFgAAACgAAAAQAAAAIAAAAAEAIAAAAAAAAAQAAAAAAAAAAAAAAAAAAAAAAAD///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8COjo6MDQ0NKE0NDShOjo6MP///wL///8C////Av///wL///8C////Av///wL///8C////Av///wJaWloKNDQ0kTMzM/0wR1X/MEdV/zMzM/00NDSRW1tbCv///wL///8C////Av///wL///8C////Av///wJCQkIaMzMzyzI5Pf8pean/I6Xz/yOl8/8pean/Mjk9/zMzM8tCQkIa////Av///wL///8C////Av///wJCQkIYMzMz1zBDTv8lldn/I6b1/yOm9f8jpvX/I6b1/yWV2f8wQ07/MzMz10JCQhj///8C////Av///wJ8fHwGMzMzwzBCTf8km+L/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/JJvi/zBCTf8zMzPDfX19Bv///wL///8CNTU1cDI2Of8lkdP/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8lkdL/MjY5/zU1NXD///8Cenp6BjMzM+UrZ4r/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/ytmiv8zMzPlfn5+Bjk5OTYzMzP/JZLT/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8lktP/MzMz/zk5OTQ2NjZSMjMz/yOj8f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6Lv/zIzM/82NjZQNzc3QDMzM/8lltr/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yOm9f8jpvX/I6b1/yWV2f8zMzP/ODg4QF5eXgozMzPlLVt3/yOl8/8jpvX/I6b1/yOl8/8sYYD/LGGB/yOl8/8jpvX/I6b1/yOl8/8tW3b/MzMz5V9fXwj///8CNzc3SjMzM/kvT2P/KXmq/yl5qf8vTmH/MzMz+TMzM/kvTmH/KXmp/yl5qv8vT2P/MzMz+Tc3N0r///8C////Av///wI4ODg6MzMzvTMzM/czMzP3MzMztzk5OTY5OTk2MzMztzMzM/czMzP1MzMzvTg4ODr///8C////Av///wL///8C////Av///wLKysoCwMDAAv///wL///8C////Av///wLAwMACy8vLAv///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C////Av///wL///8C//8AAP5/AAD4HwAA8A8AAOAHAADAAwAAwAMAAIABAACAAQAAgAEAAIABAACAAQAAwAMAAOGHAAD//wAA//8AAA=='''


def use(func):
    if os.path.exists(FILENAME):
        func(FILENAME)
        return
    tmpfile = FILENAME + '.tmp'
    with open(tmpfile, 'wb') as f:
        f.write(base64.b64decode(FILEDATA))
    func(tmpfile)
    os.remove(tmpfile)


def main():
    icofile = sys.argv[1]
    if not os.path.exists(icofile):
        # todo:try find one?
        raise IOError('icon file NOT exist: {}'.format(icofile))

    # change 'this' file with ico name and data
    with open(__file__, 'r+') as f:
        str = f.read()
        with open(icofile, 'rb') as fi:
            fmt = 'FILENAME = \'{}\''
            str = re.sub(fmt.format('(.*)'), fmt.format(os.path.basename(icofile)), str)
            fmt = 'FILEDATA = \'\'\'{}\'\'\''
            str = re.sub(fmt.format('(.*)'), fmt.format(base64.b64encode(fi.read())), str, flags=re.DOTALL)
            if len(str) > 0:
                f.seek(0)
                f.write(str)
                f.truncate()


if __name__ == '__main__':
    main()
