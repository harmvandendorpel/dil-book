import xml.etree.ElementTree as ET
template = ET.parse('templates/template1.xml')
page_height = 972

page_number = 1

instance_id_counter = 0


def absolute_image_url(filename):
    return 'file:/Users/harm/webserver/dil-book/img/{}'.format(filename)


def get_unique_id():
    global instance_id_counter
    result = 'instance_{}'.format(instance_id_counter)
    instance_id_counter += 1
    return result

spread_attributes = template.find('Spread').attrib

id_a = get_unique_id() # store because it will be reused
spread_attributes['Self'] = id_a
spread_attributes['ItemTransform'] = '1 0 0 1 0 {}'.format((page_number-1) * page_height)

rectangle_attributes = template.find('.//Rectangle').attrib
rectangle_attributes['Self'] = get_unique_id()

list_item = template.find('.//Descriptor/ListItem[@type="long"]')
list_item.text = page_number

image_link_attributes = template.find('.//Image/Link').attrib

image_link_attributes['Self'] = get_unique_id()
print image_link_attributes['LinkResourceURI']
image_link_attributes['LinkResourceURI'] = absolute_image_url('filename1.jpg')
print image_link_attributes['LinkResourceURI']

spread_filename = 'Spread_{}'.format(id_a)
# template1.xml :
# Spread(@ItemTransform="1 0 0 1 0 [972*pageNumber])"
# Spread(@Self = 'ID-A')

# Rectangle(@Self = 'ID-B')
# idPkg:Spread.Spread.Page.Properties.Descriptor.ListItem(@type="long") = pageNumber
# Image.Link(@Self='ID-C')
# Image.Link(@LinkResourceURI = 'absolute filename to image')

# designmap.xml:
# <idPkg:Spread src="Spreads/Spread_[ID-A].xml" />

# make file 'Spread_[ID-A].xml' in folder 'Spreads/'