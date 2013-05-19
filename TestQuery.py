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

        # Retrieving <amf:name> elements
        self.__query = Query(self.__session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="Ping Qin"]', {'amf': 'http://amf.openlib.org'})
        elements = self.__query.executeXml(etree)

        for e in elements:

            self.assertEqual(etree.tostring(e), '<name xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">Ping Qin</name>')

        # Retrieving <amf:text> elements for a given name
        self.__query = Query(self.__session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="Sarah Gibb"]/../../..', {'amf': 'http://amf.openlib.org'})
        elements = self.__query.executeXml(etree)

        for e in elements:

            self.assertEqual(etree.tostring(e), '<text xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="info:lib/RePEc:adv:wpaper:200804"><title>Microfinance&#8217;s Impact on Education, Poverty, and Empowerment: A Case Study from the Bolivian Altiplano</title><displaypage>http://econpapers.repec.org/RePEc:adv:wpaper:200804</displaypage><hasauthor><person><name>Sarah Gibb</name></person></hasauthor></text>')

        # Retrieving <amf:text> elements for a given name
        self.__query = Query(self.__session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="Ping Qin"]/../../..', {'amf': 'http://amf.openlib.org'})
        elements = self.__query.executeXml(etree)

        self.assertEqual(etree.tostring(elements[0]), '<text xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="info:lib/RePEc:adv:wpaper:200805"><title>Socio-economic differences in suicide risk vary by sex : A population-based case-control study of 18-65 year olds in Denmark</title><displaypage>http://econpapers.repec.org/RePEc:adv:wpaper:200805</displaypage><hasauthor><person><name>Antonio Rodr&#237;guez</name></person></hasauthor><hasauthor><person><name>Sunny Collings</name></person></hasauthor><hasauthor><person><name>Ping Qin</name></person></hasauthor></text>')

        self.assertEqual(etree.tostring(elements[1]), '<text xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="info:lib/RePEc:bla:chinae:v:15:y:2007:i:3:p:19-32"><title>How Has Rural Tax Reform Affected Farmers and Local Governance in China?</title><displaypage>http://econpapers.repec.org/RePEc:bla:chinae:v:15:y:2007:i:3:p:19-32</displaypage><hasauthor><person><name>Ran Tao</name></person></hasauthor><hasauthor><person><name>Ping Qin</name></person></hasauthor></text>')

        self.assertEqual(etree.tostring(elements[2]), '<text xmlns="http://amf.openlib.org" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" id="info:lib/RePEc:bla:chinae:v:16:y:2008:i:5:p:118-128"><title>Provision of Residential Solid Waste Management Service in Rural China</title><displaypage>http://econpapers.repec.org/RePEc:bla:chinae:v:16:y:2008:i:5:p:118-128</displaypage><hasauthor><person><name>Chunhui Ye</name></person></hasauthor><hasauthor><person><name>Ping Qin</name></person></hasauthor></text>')

    def tearDown(self):

        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestQuery)
unittest.TextTestRunner(verbosity=2).run(suite)
