import os
import unittest
from v1.unmarshal import unmarshal

class TestEvent(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testEventMarshal(self):
        unmarshal(testEventStr)

if __name__ == '__main__':
    unittest.main()

testEventStr1 = '{"apiVersion": "v1", "kind": "Event"}'

testEventStr = '{"kind":"Event","apiVersion":"v1","metadata":{"name":"test1-2gv40.14d750b423324d9a","namespace":"fangying-5","uid":"470eaa98-783a-11e7-86de-0cc47ab1f7be","creationTimestamp":"2017-08-03T10:55:35Z"},"involvedObject":{"kind":"Pod","namespace":"fangying-5","name":"test1-2gv40","uid":"470a1db3-783a-11e7-86de-0cc47ab1f7be","apiVersion":"v1","resourceVersion":"10094735"},"reason":"FailedScheduling","message":"pod (test1-2gv40) failed to fit in \nany node fit failure summary on nodes : MatchNodeSelector (1)","source":{"component":"default-scheduler"},"firstTimestamp":"2017-08-03T10:55:35Z","lastTimestamp":"2017-08-04T03:07:38Z","count":3323,"type":"Warning"}'