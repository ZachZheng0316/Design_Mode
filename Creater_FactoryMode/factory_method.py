import xml.etree.ElementTree as etree
import json

# 处理JSON文件类
class JSONConnector(object):
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as file:
            self.data = json.load(file)

    @property
    def parsed_data(self):
        return self.data

# 处理XML文件的类
class XMLConnector(object):
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


# 工厂方法:基于文件扩展名, 返回一个JSONConnector或XMLConnector的实例
def factory_mode(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError('Cannot connect to {}'.format(filepath))

    return connector(filepath)

# 对connector进行包装
def connect_to(filepath):
    factory = None

    try:
        factory = factory_mode(filepath)
    except ValueError as ve:
        print(ve)
    return factory

def main():
    # 确认异常处理是否有效
    sqlite_factory = connect_to('data/person.sq3')
    print()

    # 解析xml文件
    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//{}[{}='{}']".format('person', 'lastName', 'Liar'))
    print('found: {} persons'.format(len(liars)))
    for liar in liars:
        print('first name: {}'.format(liar.find('firstName').text))
        print('last name: {}'.format(liar.find('lastName').text))
        [print('phone number ({})'.format(p.attrib['type']), p.text) for p in liar.find('phoneNumbers')]
    print()

    # 解析json文件
    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print('found: {} donuts'.format(len(json_data)))
    for donut in json_data:
        print('name: {}'.format(donut['name']))
        print('price: ${}'.format(donut['ppu']))
        [print('topping: {} {}'.format(t['id'], t['type'])) for t in donut['topping']]

if __name__ == '__main__':
    main()
    
