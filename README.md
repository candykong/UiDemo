一、框架目录结构说明
1、config：配置文件路径、和配置信息，如账号密码，邮箱信息，页面weburl
2、util操作类，如处理yaml文件、ini文件、数据库、日志操作等等
3.testyaml存放页面元素
4.testdata存放测试数据，传参和期望值
5.pageobj：base.py是 基础类用于页面对象类的继承，其他是各个页面
6.testcase完成用例
7、report存放测试报告、测试截屏
8、log存放日志
10、run.py用来执行用例


二、依赖库 

三、使用allure运行 
1.运行生成结果pytest testCase/ --alluredir=./tmp/allure_results 
2.生成报告：allure generate ./tmp/allure_results/ -o ./report/ --clean 
3.打开报告：allure open -h 127.0.0.1 -p 8883 ./report/

allure open -h 10.7.9.43 -p 8883 ./report/
