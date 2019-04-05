# 1. 获取到网页内容
# 2. 使用以前写的词频统计
# 3. 发送email到自己的邮箱


from mymodule.stats_word import stats_text_cn
from mymodule.utils import request,send_email
import json
# print(r.status_code)

# print(r.headers['content-type'])

# print(r.encoding)
text = request('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')

res = stats_text_cn(text,0)
res =json.dumps(res,ensure_ascii=False)
send_email(res)

print(res)
# print(r.text)



