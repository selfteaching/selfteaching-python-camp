# import sys as system
# print(sys.platform)
# print(sys.maxsize)
# 建立 geometry 模组，载入使用
# import geometry
# result=geometry.distance(1,1,5,5)
# print(result)
# import sys 
# print(sys.path)
import sys
sys.path.append("modules")  #在模组的搜寻路径列表中个【新增路径】
print(sys.path)  # 印出模组的搜寻路径列表
print("------------------------")
import geometry
print(geometry.distance(1,1,5,5))