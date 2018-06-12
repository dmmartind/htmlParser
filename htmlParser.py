from html.parser import HTMLParser
from html.entities import name2codepoint

def openTag(tag,attr):
    sAttr = '['
    for attr in attrs:
        sAttr += attr + ','
    if(tag == 'html'):
        string = "$this->openHtml(FALSE);"
    if(tag == 'title')
        string = "$this->Title( {%s}, FALSE );" sAttr
    if(tag == 'span')
        string = "$this->openSpan( {%s}, FALSE );" sAttr
    if(tag == 'head')
        string = "$this->openHead( {%s}, FALSE );" sAttr
    if(tag == 'body')
        string = "$this->openBody( {%s}, FALSE );" sAttr
    if(tag == 'p')
        string = "$this->openP( {%s}, FALSE );" sAttr
    if(tag == 'noscript')
        string = "$this->NoScript( {%s}, FALSE );" sAttr
    if(tag == 'link')
        string = "$this->Link( {%s}, FALSE );" sAttr
    if(tag == 'button')
        string = "$this->Button( {%s}, FALSE );" sAttr
    if(tag == 'iframe')
        string = "$this->iFrame( {%s}, FALSE );" sAttr
    if(tag == 'meta')
        string = "$this->Meta( {%s}, FALSE );" sAttr
    if(tag == 'script')
        string = "$this->Script( {%s}, FALSE );" sAttr
    if(tag == 'div')
        string = "$this->openDiv( {%s}, FALSE );" sAttr
    if(tag == 'label')
        string = "$this->Label( {%s}, FALSE );" sAttr
    if(tag == 'input')
        string = "$this->Input( {%s}, FALSE );" sAttr

        

def closeTag(tag,attr):
    sAttr = '['
    for attr in attrs:
        sAttr += attr + ','
    if(tag == 'html'):
        string = "$this->closeHtml(FALSE);"
    if(tag == 'title')
        string = "$this->Title( {%s}, FALSE );" sAttr
    if(tag == 'span')
        string = "$this->closeSpan( {%s}, FALSE );" sAttr
    if(tag == 'head')
        string = "$this->closeHead( {%s}, FALSE );" sAttr
    if(tag == 'body')
        string = "$this->closeBody( {%s}, FALSE );" sAttr
    if(tag == 'p')
        string = "$this->closeP( {%s}, FALSE );" sAttr
    if(tag == 'noscript')
        string = "$this->NoScript( {%s}, FALSE );" sAttr
    if(tag == 'link')
        string = "$this->Link( {%s}, FALSE );" sAttr
    if(tag == 'button')
        string = "$this->Button( {%s}, FALSE );" sAttr
    if(tag == 'iframe')
        string = "$this->iFrame( {%s}, FALSE );" sAttr
    if(tag == 'meta')
        string = "$this->Meta( {%s}, FALSE );" sAttr
    if(tag == 'script')
        string = "$this->Script( {%s}, FALSE );" sAttr
    if(tag == 'div')
        string = "$this->closeDiv( {%s}, FALSE );" sAttr
    if(tag == 'label')
        string = "$this->Label( {%s}, FALSE );" sAttr
    if(tag == 'input')
        string = "$this->Input( {%s}, FALSE );" sAttr

    
    
    
    
    
    
        
    
    
        
    
        
    

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
        createTag(tag,attr);
    def handle_endtag(self, tag):
        print("End tag   :", tag)
    def handle_data(self, data):
        print("Data     :", data)
    def handle_comment(self, data):
        print("Comment    :", data)
    def handle_entityref(self,name):
        c = chr(name2codepoint[name])
        print("Named ent: ", c)
    def handle_charref(self, name):
        if name.startswitch('x'):
            c=chr(int(name[1:], 16))
        else:
            c= char(int(name))
        print("Num ent     :", c)
    def handle_decl(self, data):
        print("Decl     :", data)


parser = MyHtmlParser();
str = open('index.html', 'r').read()
parser.feed(str);
