import jinja2
templateLoader = jinja2.FileSystemLoader(searchpath="./")
templateEnv=jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE="report1.tpl"
template=templateEnvi.get_template(TEMPLATE_FILE)
outputText=template.render(name='williamtoll',address=" Asuncion-Paraguay")
