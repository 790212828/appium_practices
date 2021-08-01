…or create a new repository on the command line
echo "# pytest_practices1" >> README.md
git init
git add README.md
git commit -m "selenium录播课练习和作业 "
git branch -M main
git remote add origin https://github.com/790212828/appium_practices.git
git push -u origin main

…or push an existing repository from the command line
git remote add origin https://github.com/790212828/appium_practices.git
git branch -M main
git push -u origin main



"""
生成allure-report命令：
cmd:cd .py文件路径下
pytest --clean --alluredir=./result/2/ test_homework.py
allure generate ./result/2/ -o ./report/2/
allure open -h 127.0.0.1 -p 8090 ./report/2/
"""



#1、CSS_SELECTOR定位方法
https://www.w3school.com.cn/cssref/css_selectors.asp

#2、学会使用时序图，plantUML,并理解

#3、学会时序图中的箭头指向，结合PageObject模式()
main_page-》contact_page
箭头开始的点是当前main_page的一个方法def function()，
箭头结束就是这个方法的返回到一个contact_page的实例：return ContactPage(self.driver) 

#4、代码思维和设计思维
将常用到相同方法的self.driver.find_element()方法等封装到基础base_page中
将常用到的定位元素参数封装为类中公有或者私有 类全局变量
PageObject设计思维了解、熟悉、熟练运用

























