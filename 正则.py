import re




str='asfdas123dasd(123)sdfas'

p=r'asfdas123dasd\((.*?)\)sdfas'

rname = r'<h1 class="video-tt">(.*?)</h1>'

sname='<h1 class="video-tt">fdfdfd</h1>'
# print(re.findall(rname,sname))
print(re.findall(p,str))
# print(str.replace("123","大叔"))
lll="https://www.2717.com/ent/meinvtupian/list_11_2.html"
# print(re.sub(r"\\d+\)", '456654', str))
print(re.sub(r"\d{1}?", '_3.', lll))
