class HtmlCM:

    def __init__(self):
        pass

    def __enter__(self):
        print("<TABLE>")
        print(" <TR>")
        print("     <TH>Number</TH><TH>Description</TH>")
        print(" </TR>")
        return self

    def __exit__(self, type, value, traceback):
        print("</TABLE>")


with HtmlCM() as html:
    print(" <TR>")
    print("     <TD>1</TD><TD>Say hello!</TD)")
    print(" </TR>")
    print(" <TR>")
    print("     <TD>2</TD><TD>Say good bye!</TD)")
    print(" </TR>")
