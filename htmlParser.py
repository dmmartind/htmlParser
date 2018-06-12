from html.parser import HTMLParser
from html.entities import name2codepoint

class MyHtmlParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start tag: ", tag)
        for attr in attrs:
            print("    attr:", attr)
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

parser.feed('<html><head><title>My Foot</title></head><body><p>My Foot</p></body></html>');
