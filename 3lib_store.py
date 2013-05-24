
import web, json
from lxml import etree
from AmfAuthor import AmfAuthor
from BaseXClient import Query, Session

urls = (

    # Retrieving XML documents by author names
    '/author/(.*)/?(.*)', 'author'
)

class author:

    def GET(self, collection, name):

        if not collection:

            collection = "RePEc"

        # Create a BaseXSession with the database RePEc
        try:

            session = Session('localhost', 1984, 'admin', 'admin', collection)

            if not name:

                xQueryStr = '//amf:text/amf:hasauthor/amf:person/amf:name/../../..'
            else:
                xQueryStr = '//amf:text/amf:hasauthor/amf:person/amf:name[text()="' + name + '"]/../../..'

            # Pass the query returning all <amf:text> elements for a given author's name
            query = Query(session, xQueryStr, {'amf': 'http://amf.openlib.org'})
            results = query.execute(etree)

            response = ''

            for e in results:

                response += etree.tostring(e)

            # Close query object  
            query.close()
            
            # Close the session
            session.close()

            # Set the content type for the XML response
            web.header('Content-Type', 'application/xml')

            return response
        except IOError as e:
        
            return "I/O error({0}): {1}".format(e.errno, e.strerror)
        #except:

        #    return "Server error encountered: Please contact the web administrator."
            
if __name__ == '__main__':

    app = web.application(urls, globals())
    app.run()
