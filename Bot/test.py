# import xml.etree.ElementTree as ET

# start_pos = []
# max_betno = []
# pri_amount = []
# auto_ratio = []
# my_threshold = []
# inc_rate = []

# def read_parameters_from_file():
#     global start_pos
#     global max_betno
#     global pri_amount
#     global auto_ratio
#     global my_threshold
#     global inc_rate

#     myXMLtree = ET.parse('params_config.xml')
#     type_cnt = int(myXMLtree.find('Count').text)
#     print(type_cnt)
    
#     for _index in range(type_cnt):
#         x = myXMLtree.find(f'Type{_index}')
#         start_pos.append( int(x.find('startPoint').text))
#         max_betno.append( int(x.find('maxBetNumber').text))
#         pri_amount.append( float(x.find('primaryPrice').text))
#         auto_ratio.append( float(x.find('profitRatio').text))
#         my_threshold.append( int(x.find('threshold').text))
#         inc_rate.append( float(x.find('incBetRate').text))
        
#     print(start_pos[1])
    
# read_parameters_from_file()
# st = "😡 Lost : -  ${0}".format(round(2.54,2))
# print(st)
# print(round(2.45,0))

# print( not False)

x = 5 % 0.2
print(x)