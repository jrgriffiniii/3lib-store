import unittest

# Dependencies
import socket, array
from BaseXClient import Query, Session
from lxml import etree

class TestQuery(unittest.TestCase):

    def setUp(self):
        
        self.__session = Session('localhost', 1984, 'admin', 'admin', 'RePEc')
        pass

    def testConstructor(self):

        self.__query = Query(self.__session, '')

        # Test for the ID assigned to the query
        self.assertEqual(self.__query._Query__id, '0')

    def testExecute(self):

        self.__query = Query(self.__session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="Sarah Gibb"]', {'amf': 'http://amf.openlib.org'})
        self.assertEqual(self.__query.execute(), '<name xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Sarah Gibb</name>')

    def testExecuteXml(self):

        self.__query = Query(self.__session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="Ping Qin"]', {'amf': 'http://amf.openlib.org'})
        elements = self.__query.executeXml(etree)

        for e in elements:

            self.assertEqual(etree.tostring(e), '<name xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Ping Qin</name>')
        pass
    
    def tearDown(self):

        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestQuery)
unittest.TextTestRunner(verbosity=2).run(suite)
