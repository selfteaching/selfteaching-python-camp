import wxpy
bot = wxpy.Bot()

my_friends = bot.friends()
for friend in my_friends:
    print(friend)

sex_dict = {'male': 0, 'female': 0, 'other': 0}

for friend in my_friends:
    if friend.sex == 1:
        sex_dict['male'] += 1
    elif friend.sex == 2:
        sex_dict['female'] += 1
    else:
        sex_dict['other'] += 1

print(sex_dict)
print("Total numbers of my friends: ", len(my_friends))

province_dict = {
                    '北京': 0, '上海': 0, '天津': 0, '重庆': 0, '西藏': 0,
                    '河北': 0, '山西': 0, '吉林': 0, '辽宁': 0, '黑龙江': 0,
                    '陕西': 0, '甘肃': 0, '青海': 0, '山东': 0, '福建': 0,
                    '浙江': 0, '台湾': 0, '河南': 0, '湖北': 0, '湖南': 0,
                    '江西': 0, '江苏': 0, '安徽': 0, '广东': 0, '海南': 0,
                    '四川': 0, '贵州': 0, '云南': 0, '香港': 0, '澳门': 0, 
                    '内蒙古': 0, '新疆': 0, '宁夏': 0, '广西': 0, '其他': 0,         
                }
for friend in my_friends:
    if friend.province in province_dict.keys():
        province_dict[friend.province] += 1
    else:
        province_dict['其他'] += 1

print(province_dict)