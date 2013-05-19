
import web, json
from lxml import etree
from AmfAuthor import AmfAuthor
from BaseXClient import Query, Session

urls = (

    # Retrieving XML documents by author names
    '/author/(.+)', 'author'
)

class author:

    def GET(self, name):

        # Create a BaseXSession with the database RePEc
        try:

            session = Session('localhost', 1984, 'admin', 'admin', 'RePEc')

            # Pass the query returning all <amf:text> elements for a given author's name
            query = Query(session, '//amf:text/amf:hasauthor/amf:person/amf:name[text()="' + name + '"]/../../..', {'amf': 'http://amf.openlib.org'})
            results = query.execute(etree)

            response = ''

            for e in results:

                response += etree.tostring(e)

            # Close query object  
            query.close()
            
            # Close the session
            session.close()

            return response
        except IOError as e:
        
            return "I/O error({0}): {1}".format(e.errno, e.strerror)
        #except:

        #    return "Server error encountered: Please contact the web administrator."
            
if __name__ == '__main__':

    app = web.application(urls, globals())
    app.run()
