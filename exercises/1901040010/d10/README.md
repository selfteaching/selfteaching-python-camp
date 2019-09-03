#如何使用pip install 安装第三方库#

初次尝试：直接在Terminal键入”pip install jieba“
报错“SyntaxError: invalid syntax”

正确操作方式：
1. 打开Terminal
2. 找到Python下pip的路径
  /usr/local/lib/python3.6/site-packages
  *My compyter：/Users/min/anaconda3/lib/python3.6/site-packages/pip
3. 点住pip文件夹拖入Terminal，会显示“-bash: /Users/min/anaconda3/lib/python3.6/site-packages/pip: is a directory“
4. 键入”install jieba“，显示
usage: install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 file2
       install [-bCcpSsv] [-B suffix] [-f flags] [-g group] [-m mode]
               [-o owner] file1 ... fileN directory
       install -d [-v] [-g group] [-m mode] [-o owner] directory ...