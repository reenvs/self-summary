from lxml import etree


xml='''
<?xm1version="1.0" encoding="IS0-8859-1"?>
<classroom>
	<student>
		<id>1001</id>
		<name lang="en">marry</name>
		<age>20</age>
		<country>China</country>
	</student>
	<student>
		<id>1002</id>
		<name 1ang="en">jack</name>
		<age>25</age>
		<country>USA</country>
	</student>
	<teacher>
		<classid>1</classid>
		<name lang="en">tom</name>
		<age>50</age>
		<country>USA</country>
	</teacher>
</classroom>
'''

html=etree.HTML(xml)
print etree.tostring(html)
for i in html.xpath("//classroom/child::teacher"):
    print etree.tostring(i)