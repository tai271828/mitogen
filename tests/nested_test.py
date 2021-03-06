import os
import unittest

import testlib


class NestedTest(testlib.RouterMixin, testlib.TestCase):
    def test_nested(self):
        context = None
        for x in range(1, 11):
            #print 'Connect local%d via %s' % (x, context)
            context = self.router.local(via=context, name='local%d' % x)

        pid = context.call(os.getpid)
        self.assertTrue(isinstance(pid, int))


if __name__ == '__main__':
    unittest.main()
